스킬은 실행 근거와 허용 도구를 선언하는 문서입니다. 검색 후보를 본 것과 해당 스킬을 선언한 것은 다릅니다. 슬롯 절차가 없는 안내도 스킬로 사용할 수 있습니다.

## 노드 설정과 선언 관문

**설정 → 스킬 선언과 검색 → 스킬 선언 필수**는 auto·on·off입니다. auto는 앞 노드의 관문 상태를 이어받고 on은 항상 선언을 요구합니다. off는 스킬 검색·선언·슬롯 실행에 참여하지 않으며 앞 노드 상태를 변경하지 않습니다. 체인 전용 제한은 별도로 유지됩니다.

선언 전에는 설정된 검색 경로와 선언·확인에 필요한 도구만 사용합니다. declare_skills는 검색으로 실제 도착한 doc_id를 선택합니다. 임의의 스킬 이름이나 미조회 ID가 실행 권한을 만들지 않습니다. 선언한 문서의 tools 합집합 밖 도구는 열리지 않으며, tools가 없으면 아무 도구도 허용하지 않는 엄격한 계약입니다.

## 스킬 문서 앞머리

```yaml
---
doc_id: DEMO_TRANSFER
title: 예제 송금
description: 계좌와 금액을 검증해 준비합니다
tools: [lookup_accounts, verify_account, verify_amount, prepare_transfer]
unmask: [PERSON_NAME]
external_llm: N
---
```

tools는 실제 런타임 이름입니다. 절차가 쓰는 도구도 여기에 포함해야 합니다. unmask는 AIM 복원·수집 정책이며 Vault 유형 등록과 별개입니다. external_llm:N은 선언한 에이전트의 현재 턴 남은 모델 호출을 내부 전용 모델로 제한합니다. 필요한 내부 모델이 없으면 실패합니다. 다른 에이전트나 다음 턴의 설정을 자동으로 바꾸지 않습니다.

## 내장 검색과 외부 검색 결과 연결

노드 내 스킬 검색을 켜면 스킬 DB를 검색하는 경로를 사용합니다. 끄면 search_skills와 지정 검색 도구를 모델에서 숨기고 **스킬 JSON 상태 변수**를 선언 후보로 사용합니다. 선언 필수 여부는 별도 설정입니다. 상태 변수에는 사용자 질문이 아니라 앞 노드의 스킬 객체·배열 또는 그 JSON 문자열을 연결하세요. 결과가 없으면 []입니다.

문서 목록 경로, 문서 ID 키, 프론트매터 키, 본문 키를 매핑할 수 있습니다. 점 경로와 배열의 .0 인덱스를 사용합니다. ID에는 숫자뿐 아니라 문자열도 가능합니다. doc_ids에는 매핑 키 이름이 아니라 실제 식별자 값을 보냅니다.

## 선언할 때 본문 읽기

후보는 ID·설명·프론트매터로 고르고 본문은 선언 시 가져올 수 있습니다. 외부 후보에는 **선언 시 본문을 불러올 스킬 DB 1개**를 연결합니다. 스킬 파이프라인·GenOS VectorDB·Weaviate를 지원하며 ID별 완전한 본문 한 개가 필요합니다. 임베딩으로 유사 본문을 찾는 과정이 아니라 지정 ID의 원문 확인입니다. docIdProperty는 기본 doc_id, 본문 속성은 설정된 text key를 사용합니다.

검색 K·필터·컬렉션은 작성자가 설정한 값을 유지합니다. 조회 장애·삭제·접근 거절·불완전 상태를 낡은 본문으로 대체하지 않습니다. SKILL_BODY_UNAVAILABLE, SKILL_STATE_INCOMPLETE, SKILL_DOC_STALE 등을 확인하세요. 관리 저장소와 필드별 복호화는 같은 문서 ID·정책을 보존해야 합니다.

## 후보와 선언 사본의 저장

미선언 후보는 Redis에 ID·출처·정책 참조 중심으로 저장합니다. 선언된 문서는 유효한 지문이 있는 파싱 사본을 슬롯 상태에 남겨 DB가 없는 뒤 노드도 이어받을 수 있습니다. 부모 스킬 상태는 참조를 사용합니다. 승인 사본의 본문·정책 지문이 맞지 않으면 거절합니다.

선언 뒤 매 턴 VDB 정책을 새로 읽는 계약은 아닙니다. 변경된 정책은 다음 선언부터 적용됩니다. 참조만 남고 본문 사본이 없을 때는 신뢰할 수 있는 reader로 복원해야 합니다. 서로 다른 저장 형식의 워커를 섞거나 롤백할 때 후보 재검색·대기 선언 복원 여부를 확인하세요.

## 폴백과 필수 결정

맞는 스킬이 없으면 declare_fallback으로 근거 없는 업무 실행을 끝냅니다. 열리는 도구는 노드의 폴백 도구 목록으로 한정되며 체인 전용 도구는 열리지 않습니다. 목록이 비어 있으면 업무 도구 없이 안내 없음으로 마무리하는 폴백을 제공합니다. 검색·선언 의무와 단계 한도는 별개이므로 한도에서 스킬 또는 폴백을 결정하지 못하면 기존 필수 결정 정책을 따릅니다.

## 스킬 선택 전용 모드

기본은 꺼짐입니다. 검색과 선언은 모델이 그대로 수행하고, 선언이 하나로 확정되면 뒤의 JSON 작성·구조화 변환 두 호출을 코드가 대신해 skill_id·skill_name을 채웁니다. 다음 조건이 맞아야 적용됩니다.

- 선언 필수 on, 현재 새 선언 결정이 필요함
- 새 실행이며 열린 절차·deferred 실행·이미 선언한 폴백이 없음
- 내장 search_skills 하나를 사용하며 외부 검색 도구가 없음
- 업무 도구와 서브에이전트가 없음
- 라우팅 정책 off, 구조화 출력이 skill_id:string·skill_name:string 두 키
- 고급 프롬프트 레이아웃을 사용하지 않음

조건이 맞지 않으면 기존 실행으로 돌아갑니다. GENOS_SKILL_SELECTOR_MODE=off는 이 최적화를 끕니다. 검색 결과나 최종 선택을 캐시해 같은 요청의 판단을 재사용하는 기능은 아닙니다.

## 과업 종료

Agent 한 노드가 끝나도 선언은 노드 사이·HITL 재개에 유지됩니다. 워크플로우 FINISHED에서 과업을 해제하므로 같은 대화의 다음 요청에서 새 스킬을 선택할 수 있습니다. STOPPED는 유지합니다. 검색 후보와 봉인 목록의 보관은 별도이며 상태 만료와 대화 삭제도 다릅니다.


근거: [skillGate.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/skillGate.ts) · [externalSkillInput.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/externalSkillInput.ts) · [skillSelectorMode.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genos/skillSelectorMode.ts) · [redis-candidate-payload.md](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/docs/skills/redis-candidate-payload.md) · [skill-task-completion.ko.md](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/docs/a2a/skill-task-completion.ko.md).
