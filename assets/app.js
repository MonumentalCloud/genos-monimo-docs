const current=document.body.dataset.current;
document.querySelector(`[data-page="${current}"]`)?.setAttribute('aria-current','page');
document.getElementById('nav-toggle').addEventListener('click',event=>{const open=document.getElementById('site-nav').classList.toggle('open');event.currentTarget.setAttribute('aria-expanded',String(open));});
document.getElementById('expand-all').addEventListener('click',()=>document.querySelectorAll('article details').forEach(item=>item.open=true));
document.getElementById('collapse-all').addEventListener('click',()=>document.querySelectorAll('article details').forEach(item=>item.open=false));
let searchIndex;
document.getElementById('site-search').addEventListener('submit',async event=>{
 event.preventDefault();const query=document.getElementById('search').value.trim();
 const panel=document.getElementById('search-panel'),list=document.getElementById('search-results'),status=document.getElementById('search-status');
 panel.hidden=false;list.replaceChildren();if(!query){status.textContent='검색어를 입력하세요.';return;}
 try{
  if(!searchIndex){const response=await fetch('search-index.json');if(!response.ok)throw Error('index unavailable');searchIndex=await response.json();}
  const terms=query.toLowerCase().split(/\s+/);const matches=searchIndex.filter(page=>terms.every(term=>(page.title+' '+page.text).toLowerCase().includes(term)));
  status.textContent=`${matches.length}개 문서에서 찾았습니다.`;
  for(const page of matches){const li=document.createElement('li'),a=document.createElement('a'),p=document.createElement('p');a.href=page.url;a.textContent=page.title;const at=page.text.toLowerCase().indexOf(terms[0]);p.textContent=page.text.slice(Math.max(0,at-50),at+180).replace(/\s+/g,' ');li.append(a,p);list.append(li);}
 }catch{status.textContent='검색 색인을 불러오지 못했습니다. 웹 서버 또는 GitHub Pages에서 열고 다시 시도하세요.';}
});
document.getElementById('close-search').addEventListener('click',()=>document.getElementById('search-panel').hidden=true);
document.addEventListener('keydown',event=>{if(event.key==='Escape')document.getElementById('search-panel').hidden=true;});
const catalogFilter=document.getElementById('catalog-filter');
catalogFilter?.addEventListener('input',()=>{
 const words=catalogFilter.value.trim().toLowerCase().split(/\s+/).filter(Boolean);let visible=0;
 document.querySelectorAll('[data-search]').forEach(item=>{const matches=words.every(word=>item.dataset.search.includes(word));item.hidden=!matches;if(matches)visible++;});
 document.querySelectorAll('.file-group').forEach(group=>{const matches=group.querySelectorAll('.catalog-item:not([hidden]),.commit-item:not([hidden])').length;group.hidden=matches===0;if(words.length)group.open=matches>0;});
 document.getElementById('catalog-status').textContent=`표시 항목 ${visible}개`;
});
function revealAnchor(){if(!location.hash)return;const target=document.getElementById(decodeURIComponent(location.hash.slice(1)));if(!target)return;for(let item=target;item;item=item.parentElement)if(item.tagName==='DETAILS')item.open=true;target.scrollIntoView();}
window.addEventListener('hashchange',revealAnchor);revealAnchor();
