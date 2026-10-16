변경된 Flowise 노드를 사용 목적과 실제 연결로 구분합니다. 모니모 Agent의 옵션을 기본 Agent나 독립 Tool·LLM 노드의 동작으로 일반화하지 않습니다.

## 모델 노드

ChatMnc·ChatOpenAI·ChatOpenAICustom·MncOpenAIEmbedding과 Agentflow LLM·Agent 경로가 변경되었습니다. 모델 요청의 trace 문맥, 메시지·도구 직렬화, 기본 모델 설정과 출력 경계를 확인해야 합니다. 한 provider에서 확인한 모델 요청을 다른 provider의 실제 전송 검증으로 대신하지 않습니다.

## GenosMCP 도구 선택

연결된 MCP의 사용가능한 도구 목록을 고르면 해당 액션을 사용합니다. 목록을 비워 두면 런타임에서 서버 도구 전체가 열릴 수 있습니다. 설계 화면은 체인 전용·폴백 도구를 개별 이름으로 선택할 수 있도록 빈 선택 MCP의 실제 도구 목록을 조회합니다. 조회 실패 시 노드 이름만 표시될 수 있으므로 실제 실행 이름과 일치하는지 확인하세요.

공식 MCP 입력 스키마와 모델용 설명·스키마, 실행 시 검증을 구분합니다. 일반 직접 호출은 원래 스키마로, 체인의 qvo 자동 감싸기와 슬롯 입구 입력포맷은 각기 별도 규칙으로 동작합니다. _meta의 브릿지·확인 선언과 표준 annotation hint도 구분하세요.

## 도구 이름과 실행 이력

모델의 도구 이름은 ASCII 문자·숫자·밑줄·하이픈으로 정리하며 길이 제한을 적용합니다. 표시용 한국어 이름과 런타임 호출 이름은 다를 수 있습니다. 스킬 tools, 체인 tool, 체인 전용·폴백 목록은 실제 호출 이름에 맞춰야 합니다. 실행 상세에는 편집한 내부 도구 설명과 실제 모델 요청의 도구 정의를 함께 확인합니다.

## 기타 변경 노드

CurrentDateTime, RetrieverTool, Tool·Retriever Agentflow, GenOS 장기 메모리 노드도 포함합니다. 정확한 입력 선언과 분기 조건은 노드별 입력 선언, 파일별 변경 함수와 연결 커밋은 전체 변경 색인에서 볼 수 있습니다. 이름만 보고 동작을 추측하지 않도록 소스 링크를 같이 제공합니다.


근거: [GenosMCP.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/tools/MCP/GenosMCP/GenosMCP.ts) · [core.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/tools/MCP/core.ts) · [genosMcpSelect.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genosMcpSelect.ts) · [genosMcpTags.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genosMcpTags.ts).


## ChatMnc 제한시간과 재시도

ChatMnc의 Timeout을 비워 두면 현재 기본 제한시간은 **60,000ms**, 자동 재시도 기본값은 **1회**입니다. 제한시간과 A2A 전체 요청 기한은 별개이므로 재시도까지 포함한 총 시간을 고려하세요.

| 설정 | 적용 규칙 |
| --- | --- |
| 노드 Timeout | 유효한 양수 입력이 환경변수보다 우선합니다. 1 이상은 정수로 내림합니다. |
| GENOS_LLM_TIMEOUT_MS | 노드에 유효한 값이 없을 때 적용합니다. `0`은 무제한이며 미설정·잘못된 값은 60,000ms입니다. |
| GENOS_LLM_MAX_RETRIES | 유효한 0 이상 숫자는 정수로 내림합니다. 미설정·잘못된 값은 1입니다. |

이 기본값은 ChatMnc가 사용하는 해석 함수의 계약입니다. 다른 모델 노드 전체에 같은 상한이 강제된다고 가정하지 않습니다.

## MCP 연결 수명

MCP 세션 정리는 `GENOS_MCP_SESSION_CLEANUP`의 기본값 true, 클라이언트 재사용은 `GENOS_MCP_CLIENT_REUSE`의 기본값 false입니다. 재사용을 켰을 때 `GENOS_MCP_CLIENT_IDLE_MS` 기본 30,000ms, `GENOS_MCP_CLIENT_MAX_AGE_MS` 기본 300,000ms가 적용됩니다. 연결 풀은 toolkit 내에서 관리하며 동시 요청이 하나의 클라이언트를 중복 사용하지 않도록 합니다. 세션 ID를 발급한 연결이나 SSE 폴백은 재사용 대상이 아닙니다. 환경 설정 변경 후 해당 프로세스를 재시작하세요.

## CurrentDateTime의 한국 시간

날짜·시간·요일·ISO8601 출력을 호스트 시간대나 tzdata와 무관한 UTC+9 기준으로 맞춥니다. 서버가 UTC로 실행되더라도 한국 시간 기준 출력인지 확인하세요.

근거: [genosLlmDefaults.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genosLlmDefaults.ts).
