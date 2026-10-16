"""Build the static Korean guide: python3 -m pip install Markdown; python3 build.py."""
from pathlib import Path
import html, json, re
import markdown

ROOT=Path(__file__).resolve().parent
CAT=json.loads((ROOT/'catalog.json').read_text())
REFS=json.loads((ROOT/'assets/references.json').read_text())
PAGES=[('index','시작하기'),('skills','스킬 검색과 선언'),('slots','genos-slots'),('chain','genos-chain'),('vault','genos-vault'),('tables','표 필터와 계산'),('hitl','사용자 확인과 브릿지'),('a2a','A2A 위임'),('prompts','프롬프트 편집'),('memory','대화와 장기 기억'),('retrieval','지식 검색'),('nodes','모델과 MCP 노드'),('privacy','AIM과 로그 보호'),('debug','Langfuse 디버깅'),('settings','Monimo 설정 사전'),('node-settings','노드별 입력 선언'),('environment','환경변수 참조'),('operations','운영과 호환성'),('changes','전체 변경 색인')]

def escape(s):return html.escape(str(s),quote=True)

def replace_reference(match):
    title,ref=match.groups()
    if ref not in REFS:raise ValueError('Unresolved Page reference: '+ref)
    data=REFS[ref];url=data['file']
    if ref.startswith('visualize:'):
        return f'<iframe class="demo-frame" title="{escape(title)}" src="{escape(url)}" loading="lazy" sandbox="allow-scripts allow-same-origin"></iframe><p class="caption">합성 동작 데모 · 실제 도구 호출 없음 · <a href="{escape(url)}" target="_blank" rel="noopener">크게 열기</a></p>'
    meta=data.get('metadata',{}).get('image',{});crop=meta.get('crop')
    img=f'<img src="{escape(url)}" alt="{escape(title)}" loading="lazy">'
    if crop:
        l=crop.get('left',0);r=crop.get('right',0);t=crop.get('top',0);b=crop.get('bottom',0)
        w=meta['width'];h=meta['height'];style=f'aspect-ratio:{w*(1-l-r)}/{h*(1-t-b)}'
        image_style=f'width:{100/(1-l-r)}%;left:{-100*l/(1-l-r)}%;top:{-100*t/(1-t-b)}%'
        img=f'<span class="crop" style="{style}"><img src="{escape(url)}" alt="{escape(title)}" style="{image_style}" loading="lazy"></span>'
    return f'<figure><a href="{escape(url)}" target="_blank" rel="noopener">{img}</a><figcaption>{escape(title)} · 눌러 원본 보기</figcaption></figure>'

def disclosures(body):
    # Markdown headings are flat; close each disclosure at its next sibling/ancestor.
    tokens=re.split(r'(<h([2-6])\b[^>]*>.*?</h\2>)',body,flags=re.S)
    result=[];levels=[];i=0
    while i<len(tokens):
        token=tokens[i]
        match=re.fullmatch(r'<h([2-6])\b([^>]*)>(.*?)</h\1>',token,flags=re.S)
        if match:
            level=int(match[1]);attrs=match[2];title=match[3]
            while levels and levels[-1]>=level:result.append('</div></details>');levels.pop()
            anchor=re.search(r'\bid="([^"]+)"',attrs)
            aid=f' id="{anchor[1]}"' if anchor else ''
            result.append(f'<details class="section section-{level}"{aid}><summary><span role="heading" aria-level="{level}">{title}</span></summary><div class="section-body">');levels.append(level);i+=2
        else:result.append(token);i+=1
    while levels:result.append('</div></details>');levels.pop()
    return ''.join(result)

def catalog_html():
    labels={'skills':'스킬과 Agent','slots':'슬롯','chain':'체인','vault':'Vault','tables':'표','hitl':'확인과 브릿지','a2a':'A2A','prompts':'프롬프트와 UI','memory':'메모리','retrieval':'검색','nodes':'모델과 MCP','privacy':'보호','debug':'추적','operations':'서버와 빌드','tests':'테스트'}
    parts=[f'<p class="catalog-count">변경 파일 {len(CAT["files"])}개 · 관련 커밋 {len(CAT["commits"])}개</p><label class="filter-label">변경 목록 검색 <input id="catalog-filter" type="search" placeholder="파일 경로·함수·커밋 제목"></label><p id="catalog-status" role="status"></p>']
    for key,label in labels.items():
        files=[x for x in CAT['files'] if x['category']==key]
        parts.append(f'<details class="file-group"><summary>{label} · {len(files)}개 파일</summary>')
        for item in files:
            path=item['path'];href=f'https://github.com/genonai/GenOS/blob/{CAT["tip"]}/{path}'
            if item['status']=='D':href=f'https://github.com/genonai/GenOS/blob/{CAT["baseline"]}/{path}'
            search=' '.join([path,*item['hunks']])
            parts.append(f'<details class="catalog-item" data-search="{escape(search.lower())}"><summary><span class="change-status">{escape(item["status"])}</span> {escape(path)}</summary><p><a href="{escape(href)}">해당 버전 소스</a> · <a href="https://github.com/genonai/GenOS/compare/{CAT["baseline"]}...{CAT["tip"]}">전체 비교</a></p>')
            if item['hunks']:parts.append('<p>변경 지점의 함수 문맥</p><ul>'+''.join('<li><code>'+escape(x)+'</code></li>' for x in item['hunks'])+'</ul>')
            else:parts.append('<p>새 파일·전체 변경·바이너리 또는 함수 문맥이 없는 변경입니다. 소스와 이력을 확인하세요.</p>')
            parts.append('</details>')
        parts.append('</details>')
    parts.append('<details class="file-group"><summary>관련 커밋 전체</summary><ol class="commits">')
    for item in CAT['commits']:
        parts.append(f'<li class="commit-item" data-search="{escape((item["title"]+" "+item["sha"]).lower())}"><time>{item["date"]}</time> <a href="https://github.com/genonai/GenOS/commit/{item["sha"]}"><code>{item["sha"][:10]}</code> {escape(item["title"])}</a></li>')
    parts.append('</ol></details>');return ''.join(parts)

def build():
    groups=[('시작과 스킬',['index','skills']),('실행 설계',['slots','chain','hitl']),('데이터 전달',['vault','tables']),('연결과 확장',['a2a','prompts','memory','retrieval','nodes']),('운영과 디버깅',['privacy','debug','operations']),('기술 참조',['settings','node-settings','environment','changes'])]
    labels=dict(PAGES)
    index=[]
    for slug,title in PAGES:
        nav=''.join('<details class="nav-group"'+(' open' if slug in members else '')+'><summary>'+escape(label)+'</summary>'+''.join(f'<a href="{key}.html" data-page="{key}">{escape(labels[key])}</a>' for key in members)+'</details>' for label,members in groups)
        text=(ROOT/'content'/f'{slug}.md').read_text()
        text=re.sub(r'!\[([^\]]*)\]\(((?:library-file|visualize):[^)]+)\)',replace_reference,text)
        body=markdown.markdown(text,extensions=['tables','fenced_code','toc','sane_lists'])
        body=disclosures(body)
        if slug=='changes':body=body.replace('<div id="catalog-root"></div>',catalog_html())
        page=f'''<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{escape(title)} · Monimo 커스터마이징</title><meta name="description" content="Monimo v1.9.3.4 Flowise 커스터마이징 한국어 사용법과 기술 명세"><link rel="stylesheet" href="assets/style.css"><script src="assets/app.js" defer></script></head>
<body data-current="{slug}"><a class="skip" href="#main">본문으로 이동</a><header><a class="brand" href="index.html">Monimo <span>커스터마이징</span></a><button id="nav-toggle" aria-expanded="false" aria-controls="site-nav">목차</button><form id="site-search" role="search"><label for="search">문서 검색</label><input id="search" type="search" placeholder="기능·설정·오류 코드" autocomplete="off"><button type="submit">검색</button></form></header>
<div id="search-panel" hidden><div class="search-top"><strong>검색 결과</strong><button id="close-search">닫기</button></div><p id="search-status" role="status"></p><ul id="search-results"></ul></div>
<aside id="site-nav"><p class="nav-heading">FLOWISE · MONIMOAGENT</p>{nav}<p class="revision">v1.9.3.4<br>2026.10.16 · {CAT['tip'][:10]}</p></aside>
<main id="main"><div class="page-kicker">MONIMO DOCUMENTATION</div><h1>{escape(title)}</h1><div class="page-actions"><button id="expand-all">이 페이지 모두 펼치기</button><button id="collapse-all">모두 접기</button></div><article>{body}</article><footer>기준 {CAT['tip'][:10]} · 내용 수정은 content/{slug}.md<br>동작 설명과 합성 데모는 배포 환경의 출시 검증을 대신하지 않습니다.</footer></main></body></html>'''
        (ROOT/f'{slug}.html').write_text(page)
        plain=re.sub(r'<[^>]+>',' ',body)
        index.append({'title':title,'url':slug+'.html','text':html.unescape(plain)})
    (ROOT/'search-index.json').write_text(json.dumps(index,ensure_ascii=False))
    (ROOT/'.nojekyll').write_text('')
    print(f'Built {len(PAGES)} pages, {len(CAT["files"])} files, {len(CAT["commits"])} commits')

if __name__=='__main__':build()
