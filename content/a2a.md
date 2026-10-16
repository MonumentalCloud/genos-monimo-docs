MonimoAgent의 서브에이전트 도구는 모델이 Agent Card를 보고 대상을 선택하는 경로입니다. GenOS A2A 노드는 작성자가 캔버스에서 대상을 고정하는 경로입니다. 두 경로의 검증 결과를 서로 대신 쓰지 않습니다.

## 연결과 Agent Card

설정의 **하위 에이전트**에서 내부 배포 에이전트 또는 외부 URL을 고릅니다. 이름·설명·주요 기능은 Agent Card에서 가져옵니다. 입력 메시지만으로 자식이 작업을 이해할 수 있도록 실제 대상·앞 단계 확인값·출력 형식을 포함합니다. 이름·설명 프롬프트 편집이 실행 권한이나 Card의 사실을 바꾸지는 않습니다.

## 동시 실행과 의존 관계

subAgentConcurrency 기본 1은 순차 실행입니다. 이 값은 A2A에 적용하며 일반 업무 도구 병렬 실행 정책을 바꾸지 않습니다. 앞 결과가 필요한 작업은 결과를 받은 뒤 보내고 독립된 요청만 동시에 실행합니다. fan-out에서 일부 실패와 일부 성공이 공존할 수 있으므로 성공한 업무를 다시 실행하지 않도록 각 자식 결과를 구분합니다.

## HITL 전달과 진행 중계

사용자 확인 요청 전달은 기본 true입니다. 자식이 멈춘 작업·대화·메시지 식별자를 유지한 채 응답 후 이어갑니다. 진행 상황 실시간 중계는 기본 false이며 켜면 진행과 중간 이벤트를 화면에 전달합니다. 단순 최종 텍스트를 받은 것과 실제 interrupt·resume가 연결된 것은 다릅니다.

부모가 승인 문구를 새로 쓰거나 이전 대화의 금액으로 자식 승인을 대신 만들지 않습니다. 취소·재시도·다중 대기 카드에서 어느 자식의 요청에 답했는지와 나머지 작업 상태를 확인해야 합니다.

## 라우팅 종료 정책

agentRoutingPolicy의 delegate-or-clarify는 라우팅 마스터에서 선택적으로 사용합니다. 서브에이전트 위임 또는 분류 질문을 요구하고 마스터가 로컬 판단만으로 업무 최종 응답을 만들지 않게 합니다. off가 기본입니다. 단순 문구 규칙만으로 실행 승인이나 올바른 위임이 보장되지는 않습니다. 실제 도구·자식 checkpoint를 대조하세요.

## 상태 전달과 범위

task·context·message와 trace 문맥을 이어받으며 사용 주체·대화 범위가 맞아야 합니다. 실행 ID는 HITL 재개에도 유지합니다. A2A chain/deadline 제어 헤더는 검증된 실행 문맥으로 전달하고 일반 사용자 입력에서 임의로 승계하지 않습니다. 공유 루트 턴의 Vault와 노드별 프라이버시 래치는 서로 다른 범위입니다.

## 실패 추적

부모의 도구 호출 → A2A 전송·정규화 → 자식 처리 → 자식 도구 → 부모 최종 종료까지 확인합니다. 최초/재개·부분 실패·정상 완료마다 traceId, 부모 observation, 오류 수준, 원인과 최종 출력이 맞는지 보세요. SDK export 성공이나 직접 A2A 노드 하나의 통과로 모델 선택 위임 전체가 검증됐다고 판단하지 않습니다.


근거: [GenosA2A.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/GenosA2A/GenosA2A.ts) · [subAgentTool.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/a2a/subAgentTool.ts) · [MonimoAgent.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/MonimoAgent/MonimoAgent.ts).
