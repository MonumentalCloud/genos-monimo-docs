대화 메모리, 장기 기억 자동 recall, 에이전트가 호출하는 메모리 도구는 서로 다릅니다. 개인화 기능을 켰다고 모든 대화·서비스의 데이터가 한 범위가 되는 것은 아닙니다.

## 대화 메모리

agentEnableMemory는 같은 대화의 이전 메시지를 사용합니다. allMessages, windowSize, conversationSummary, conversationSummaryBuffer를 고를 수 있으며 최근 대화 범위·요약 토큰 한도는 설정 사전을 확인하세요. HITL 표시 이력과 모델용 본문을 구분해 사용자 카드 원문이나 보호 값을 일반 이력으로 재확산하지 않도록 합니다.

## 장기 기억 자동 recall

enableLongTermRecall은 기본 false입니다. 켜면 노드 실행의 첫 LLM 호출 전에 한 번 검색하며 Iteration은 항목별 실행입니다. 모델이 메모리 도구를 고르는 과정과 별개입니다. 개인화 MCP 서버, top K 기본 8, threshold 기본 0, 개인·현재 서비스 범위를 설정합니다. threshold 0은 컷 없음이며 점수 척도에 맞춰 작성자가 정합니다.

## 주입 위치와 템플릿

기본 userContext는 현재 질문 앞의 낮은 권한 참고 문맥으로 두며 system은 호환 방식입니다. 템플릿에는 `{memories}` 또는 `{memories_json}`이 필요하고 `{query_time}`, `{count}`, `{safety}`를 사용할 수 있습니다. 저장 기억을 업무 실행 지시나 시스템 권한으로 승격하지 않습니다.

## 명시적 장기 메모리 도구

GenOSLongTermMemory는 선택한 메모리 MCP 연결로 에이전트가 작업하는 별도 도구입니다. 자동 recall 사용 여부와 연결 도구의 노출·허용은 독립적으로 확인합니다. 외부 메모리 접근 토큰과 사용자·서비스 주체는 해당 연결 범위에서만 전달해야 하며 일반 도구나 기록으로 확산하지 않습니다.

## 디버깅

검색 없음·검색 실패·주입 생략을 구분하고 설정한 scope, K, threshold와 실제 모델 요청을 대조합니다. 실행 상세에는 recall 원문이 생략될 수 있습니다. 원문이 필요하면 해당 모델 관측의 승인된 보호 로그를 확인하세요. 대화 메모리 끄기, 슬롯 만료, 장기 기억 삭제는 서로 다른 동작입니다.


근거: [longTermRecall.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/Agent/longTermRecall.ts) · [GenOSLongTermMemory.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/tools/GenOSMemory/GenOSLongTermMemory.ts) · [externalMemoryAccess.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/externalMemoryAccess.ts).
