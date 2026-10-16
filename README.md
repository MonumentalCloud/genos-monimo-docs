# Monimo 커스터마이징 문서

한국어 정적 문서 사이트입니다. 서버·로그인·운영 API 연결이 필요 없습니다.

## 미리보기

```sh
python3 -m http.server 8765
```

브라우저에서 http://localhost:8765 를 엽니다. 파일을 직접 열면 검색 색인을 읽지 못할 수 있습니다.

## 문서 수정

1. content/*.md를 수정합니다.
2. Python 환경에 Markdown 패키지를 설치하고 `python3 build.py`를 실행합니다.
3. `python3 verify.py`로 본문 보존·색인·로컬 자산을 검사하고 브라우저에서 내용을 확인합니다.
4. Markdown과 생성 HTML·색인을 함께 커밋해 게시 브랜치에 push합니다.

```sh
python3 -m pip install Markdown
python3 build.py
```

ChatGPT Page와 자동 동기화되지 않습니다. Page의 수정도 content에 반영하고 빌드해야 합니다.

## GitHub Pages 게시

문서 전용 저장소를 정한 뒤 이 폴더의 파일을 저장소 루트에 넣습니다. GenOS 제품 저장소를 공개로 바꿀 필요가 없습니다.

1. 저장소 Settings → Pages를 엽니다.
2. Source에서 Deploy from a branch를 선택합니다.
3. main 브랜치와 /(root)를 선택해 저장합니다.
4. 배포 완료 뒤 Visit site에서 공개 URL을 확인합니다.
5. 로그아웃한 브라우저에서 본문·이미지·검색·데모를 확인합니다.

index.html과 .nojekyll을 루트에 유지하세요. 문서 전용 공개 저장소는 GitHub Free에서도 Pages를 사용할 수 있습니다. 비공개 저장소는 플랜·조직 정책에 따라 가능 여부가 달라집니다.

게시 저장소: https://github.com/MonumentalCloud/genos-monimo-docs

공개 사이트: https://monumentalcloud.github.io/genos-monimo-docs/

main 브랜치 루트에서 게시합니다.

## 기준

- 브랜치: project/monimo/v1.9.3.4
- 기준 커밋: 7936b3166da1127a1e9e9161ed89efb4a8abbfbd
- 변경 시작점: fa4b2a5478bf93584fd499d31abc4e7bcc3ea114
- 범위: Flowise 전체 경로, 관련 MonimoAgent 커스터마이징 설명
- 제외: 관리자·FAM·포털·독립 서비스 구현

catalog.json은 지정 구간의 파일·커밋 색인입니다. 소스가 업데이트되면 이 색인과 설명·설정 사전도 함께 갱신해야 합니다. 공개 문서의 코드 링크는 원본 저장소 권한을 별도로 요구할 수 있습니다.

## 확인 범위

문서 브라우저 QA와 GenOS 제품의 실제 모델·네이티브 앱·운영 빌드·Langfuse 적재 검증은 별개입니다. 데모는 합성 시뮬레이션이며 업무를 실행하지 않습니다.

공식 게시 안내: https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site
