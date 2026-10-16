"""Check the built guide locally: python3 verify.py. Does not call GenOS services."""
from pathlib import Path
from html.parser import HTMLParser
import html,json,re
import markdown
import build

class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[]
    def handle_starttag(self,tag,attrs):
        for k,v in attrs:
            if k in ('href','src') and v:self.links.append(v)

def words(s):return re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>',' ',s))).strip()
root=Path(__file__).resolve().parent
index=json.loads((root/'search-index.json').read_text())
assert len(index)==len(build.PAGES)
for slug,title in build.PAGES:
    text=(root/'content'/f'{slug}.md').read_text()
    text=re.sub(r'!\[([^\]]*)\]\(((?:library-file|visualize):[^)]+)\)',build.replace_reference,text)
    before=markdown.markdown(text,extensions=['tables','fenced_code','toc','sane_lists'])
    after=build.disclosures(before)
    assert words(before)==words(after),f'Disclosure content loss: {slug}'
    if slug=='changes':after=after.replace('<div id="catalog-root"></div>',build.catalog_html())
    built=(root/f'{slug}.html').read_text()
    assert '<article>'+after+'</article>' in built,f'Stale HTML: {slug}'
    record=next(x for x in index if x['url']==slug+'.html')
    assert record['text']==html.unescape(re.sub('<[^>]+>',' ',after)),f'Stale search: {slug}'
for page in [*root.glob('*.html'),*root.glob('demos/*.html')]:
    parser=Links();parser.feed(page.read_text())
    for url in parser.links:
        if not url or url.startswith(('#','https:','http:','data:','mailto:')):continue
        assert (page.parent/url.split('#')[0].split('?')[0]).exists(),f'Missing local resource: {page.name} {url}'
files=build.CAT['files'];assert len({x['path'] for x in files})==len(files)
assert all(x['path'].startswith('flowise/') for x in files)
print(f'PASS: {len(build.PAGES)} pages preserve content; current HTML/search; local resources; {len(files)} unique Flowise file records')
