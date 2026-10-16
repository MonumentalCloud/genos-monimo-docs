Vault 참조 전달, AIM 마스킹·화이트리스트, 내부 모델 전환, 로그 암호화는 서로 다른 경계입니다. 하나를 켰다고 다른 기능의 권한이나 보관 정책이 자동으로 생기지 않습니다.

## AIM 화이트리스트 수집

MonimoAgent의 화이트리스트 수집은 기본 false입니다. 현재 응답과 HITL·브릿지 대기에서 선언 스킬의 unmask 유형을 AIM으로 탐지해 Redis에 저장합니다. 이 옵션 자체가 출력 마스킹·차단을 수행하는 것은 아닙니다. 노드의 AIM 인증 정보를 선택해야 하며 뒤에 연결한 AIM 노드의 인증 설정을 자동으로 읽지 않습니다.

process_type 기본 input, 제한 시간 기본 10초입니다. AIM 마스킹 노드와 입력 포맷터·표 처리·Vault 허용 유형은 별도 설정입니다.

## AIM 입력 변환 JavaScript

`$input`의 text·content·prompt·component·chainPendingValue·chainSequenceValue·unmaskTypes로 AIM에 보낼 문자열만 구성합니다. 동기 코드로 비어 있지 않은 문자열을 반환하며 제한 250ms입니다. 외부 모듈·네트워크·비동기는 지원하지 않습니다. 비우면 기존 입력 형식을 쓰고, 포맷터 오류는 기존 입력으로 수집하며 formatter 상태를 남깁니다. 원래 카드·브릿지와 AIM 응답은 이 포맷터가 바꾸지 않습니다.

## 내부 전용 모델과 프라이버시 래치

external_llm:N 스킬 선언 뒤 해당 에이전트의 현재 턴 남은 모델 호출에 내부 전용 모델을 사용합니다. 설정이 없으면 실패합니다. 선언 뒤 외부 모델로 돌아가는 선택 스위치가 아니며 노드·실행 범위가 중요합니다. 다른 에이전트와 다음 턴에 무조건 상속되는 전역 전환으로 설명하지 않습니다.

## AIM 마스킹 노드

현재 AimMask 노드의 표시명은 AIM 화이트리스트 수집입니다. AIM의 BLOCK·MASK·오류 여부와 관계없이 입력 텍스트를 그대로 전달하고, 선언된 스킬의 unmask 유형 값을 수집하는 별도 흐름 노드입니다. MonimoAgent의 수집 토글과 역할이 다르므로 어느 지점에서 마스킹하고 어느 모델이 원문을 받는지 플로우를 따라 확인하세요. 위임된 결과·사용자 표시·이력의 마스킹과 Vault 참조를 혼동하지 않습니다.

## Langfuse 본문 보호

관측 메타데이터에는 식별·단계 정보를, 입출력과 원인 본문에는 기존 보호 정책을 적용합니다. 오류의 code·message·구조화 원인도 민감한 값을 가질 수 있으므로 단순 metadata 복사로 우회하지 않습니다. 로그가 암호화·마스킹·청크로 보이면 원문 부재와 구분합니다.

암호화·마스킹 provider와 실패 시 보관·재전송은 배포 설정의 영향을 받습니다. 필드별 문서 암호화와 로그 본문 암호화도 별도입니다. 이 문서는 실제 키·토큰·운영 본문을 포함하지 않습니다. 추적 문제를 해결하기 위해 보호를 끄는 절차를 권장하지 않습니다.

## 실행 범위를 확인할 때

사용자 주체, 대화, 루트 턴, Agent 노드, 실제 provider 호출 경계를 따로 확인합니다. 조회된 스킬 정책이 후보와 선언에서 달라지지 않는지, 현재 카드와 이전 이력의 값이 섞이지 않는지, 실패·취소·재개 후에도 같은 보호가 적용되는지 보세요.


근거: [AimMask.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/nodes/agentflow/AimMask/AimMask.ts) · [aimStarfort.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/aimStarfort.ts) · [servingLatch.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/servingPrivacy.ts) · [genosLogBody.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genosLogBody.ts) · [genosDocumentCrypto.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/genosDocumentCrypto.ts).
