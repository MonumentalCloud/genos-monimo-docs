이 브랜치는 지식 검색과 스킬 실행 근거 검색을 구분합니다. 문서가 검색됐다는 사실만으로 업무 도구를 사용할 권한이 생기지는 않습니다.

## 지식 도구와 스킬 DB

MonimoAgent는 문서 저장소 또는 벡터 저장소·임베딩 연결로 지식 도구를 만듭니다. 이름·설명은 모델이 검색할 대상을 고르는 데 쓰고 출처 반환을 별도로 설정합니다. 스킬 DB는 doc_id·출처·실행 정책을 선언 검증에 사용하므로 단순 참고 문서와 구분합니다.

## 검색 노드의 변경 위치

MncUnifiedRagChain, MncLLMFilterCompressionRetriever, MncMergeRetriever, MncRerankRetriever와 MncRerank, MncRerankAgentflow, Retriever 노드가 변경 목록에 있습니다. 각 노드의 모든 입력·표시 조건·기본값은 [노드별 입력 선언](node-settings.html)에 있는 원문 선언에서 확인합니다. 병합·필터·재정렬을 한 기능처럼 취급하지 말고 실제 연결 순서를 보세요.

## 저장소와 임베딩

DeepSearfing·SkillPipeline·Weaviate와 MncOpenAIEmbedding 경로가 변경되었습니다. 스킬 본문 재조회는 이미 연결된 client·collection·textKey·filter를 재사용하고 선택한 ID의 정확한 본문을 읽습니다. 본문 조회를 위해 임의로 검색 K를 바꾸거나 청크를 새 순서로 이어 붙이지 않습니다. 여러 레코드 병합은 기존 문서 수집 계약을 따릅니다.

## 문제를 좁히는 순서

질의·필터·K → 원본 검색 결과 → 병합·필터·rerank 결과 → 모델에 제공된 문서를 비교합니다. 선언 후보 frontmatter와 실행 본문도 분리해 봅니다. 문서 ID가 같아도 출처·정책·지문이 다르면 같은 승인 사본이라고 가정하지 않습니다. 소스 문서가 없다는 이유로 모델이 검색 결과를 만들어내게 하지 않습니다.


근거: [MncUnifiedRagChain.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/chains/MncUnifiedRagChain/MncUnifiedRagChain.ts) · [SkillPipeline.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/vectorstores/DeepSearfing/SkillPipeline.ts) · [Weaviate.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/vectorstores/Weaviate/Weaviate.ts) · [weaviateSkillBody.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genos/weaviateSkillBody.ts).


## 암호화된 검색 결과와 손상된 문서

MncRAG·retriever·rerank 경로는 암호화 표식과 is_encrypted에 따라 실제 청크 텍스트를 복호화한 뒤 필터·rerank·모델 입력·출처 처리에 사용합니다. 모든 metadata 필드를 무조건 복호화하는 계약은 아닙니다. 복호화할 수 없는 청크는 제외합니다. FAQ 답변 필드가 손상되면 해당 FAQ를 건너뛰고 일반 RAG로 진행하는 경로가 있습니다. 입력 배열을 그대로 변형하지 않도록 복사한 결과를 사용합니다.

## 검색 경로별 차이

DeepSearfing은 요청 metadata 중 실제 스키마에 존재하는 키만 전달하여 없는 tools 필드로 인한 오류를 피합니다. vectorless 제외·재시도 래퍼·용어집 표식 처리는 각각의 경로를 따릅니다. SkillPipeline은 adminTools의 Skills drive를 선택해 Weaviate의 doc_id·tools를 활용하는 스킬 경로와 일반 vector DB 경로를 구분합니다. `SKILLS_POLICY_ENABLED=false`이면 비활성 정책 표시를 확인하세요.

RetrieverTool에서 출처 문서 반환 옵션을 끄면 불필요한 원문 문서 직렬화도 생략합니다. 검색 결과 자체를 사용하지 않는다는 뜻은 아닙니다.
