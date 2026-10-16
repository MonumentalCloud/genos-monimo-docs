HITL은 모델이 사용자에게 질문하는 독립 도구, 업무 도구의 실행 전 승인, genos-chain 관문, A2A 자식의 확인 중계로 나타납니다. 같은 카드처럼 보여도 실행을 이어받는 주체와 체크포인트가 다릅니다.

## request_user_input 입력 전체

```json
{"question":"어느 계좌를 사용할까요?","type":"single-select","options":[{"value":"a1","label":"생활 계좌","desc":"예제 선택지"}],"allowCustomInput":true,"timeout":60}
```

| 필드 | 규칙 |
| --- | --- |
| question | 그대로 표시할 실제 질문. 빈 문자열·null 불가. test·테스트 같은 전체 자리표시자 거절 |
| type | confirm·single-select·multi-select·direct-input |
| options | 선택형은 실제 항목 1개 이상. 각 항목 value·label 필수, desc 선택 |
| allowCustomInput | single-select만 목록 외 입력 허용. multi-select는 불가 |
| timeout | 선택. 양의 유한 숫자 초 단위 |

confirm의 options는 생략하면 기본 버튼이며 직접 지정하면 true·false boolean 각각 하나와 label을 씁니다. confirm에는 allowCustomInput을 쓰지 않습니다. single/multi의 value는 문자열입니다. direct-input은 options를 생략하며 입력을 false로 끌 수 없습니다. 알려지지 않은 입력 키는 strict 스키마에서 거절합니다.

잘못된 요청은 HITL_REQUEST_INVALID 피드백을 반환하며 카드를 열지 않습니다. 질문 형식을 몰래 바꾸거나 가짜 선택지를 만드는 대신 같은 질문 의도로 인자를 고쳐 재시도합니다.

## 질문 본문과 모델 출력의 경계

request_user_input.question이 카드 질문의 정본입니다. assistant content·reasoning_content·직렬화 응답·오류 문자열을 질문 앞뒤에 붙이지 않습니다. 최초 실행·대기 도구·재개·한도 도달 카드에도 같은 규칙입니다. 사용자 답변 이력의 질문에도 실제 카드 질문을 기록합니다.

## 사용 정책과 라우팅 전용 노드

사용자 입력 요청 도구 정책은 auto·always·never입니다. auto는 토글 또는 호출자의 hitl-ui 확장에 따라 노출하고 always는 항상, never는 확장이 있어도 숨깁니다. 실제 업무 도구 없는 A2A 라우팅 전용 마스터는 자신이 업무 승인을 재구성하지 않고 분류용 선택·직접 입력만 요청합니다. 자식의 현재 승인 요청은 해당 자식의 경로로 전달합니다.

## call_native_bridge

```json
{"service":"GET_PUSH_SETTING","option":{},"timeout":15}
```

노드에서 네이티브 브릿지 도구를 켜고 허용 서비스 목록을 반드시 지정합니다. service 필수, option 객체·command 유한 숫자·timeout은 선택입니다. 대상은 모델이 고르므로 허용 목록과 런타임 검사를 모두 따릅니다. 서버에서 이 도구를 직접 실행하려 하면 명시적으로 실패합니다.

MCP 도구의 고정 브릿지 선언은 이 토글과 별개입니다. `_meta.genosBridge`로 선언합니다. 실행 전 확인은 `_meta.genosHitl`로 선언합니다. annotations의 임의 키가 보존된다고 가정하지 않습니다. 고정 option은 같은 키의 모델 인자보다 우선합니다. `await:true`는 무응답을 성공으로 처리하지 않는 판정에 쓰입니다.

## 타임아웃과 응답 재시도

timeout 상한은 2,147,483.647초이며 소수도 됩니다. 숫자 문자열·0·음수·null은 안 됩니다. 서버 체크포인트의 절대 만료는 새로고침으로 연장되지 않습니다. 응답이 만료 시각 이후 도착하면 GENOS_INTERACTION_TIMEOUT이며 후속 실행을 하지 않습니다. 글로벌 GENOS_CHECKPOINT_TTL_SEC 기본 1,800초도 추가 상한입니다.

잘못된 응답과 거절·취소·만료를 구분하세요. 유효하지 않은 선택을 사용자 거절로 바꾸지 않습니다. timeout이 기기의 네이티브 작업을 실제로 취소했다는 보장은 없으며 이미 시작된 업무의 결과를 확인해야 합니다.

## 화면과 이력

표시용 옵션과 원본 객체, 사용자가 제출한 ID와 표시 라벨, 사용자 메시지와 모델용 메시지를 구분합니다. UI의 진행 중 카드와 저장된 이력에서 질문·선택·직접 입력이 맞게 남는지 확인합니다. 임의의 assistant 본문을 카드 질문의 대체 데이터로 사용하지 않습니다.


근거: [hitlRequestTool.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/a2a/hitlRequestTool.ts) · [nativeBridgeTool.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/nativeBridgeTool.ts) · [EXTENSION_HITL_UI_v1.md](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/docs/a2a/EXTENSION_HITL_UI_v1.md) · [monimo-iteration-limit.md](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/docs/a2a/monimo-iteration-limit.md).


## MCP 선언 형식과 이전 형식의 거절

```json
{
  "_meta": {
    "genosBridge": {"service": "GET_PUSH_SETTING"},
    "genosHitl": {"confirm": "설정을 확인할까요?"}
  }
}
```

위 예시는 도구 정의의 메타데이터 부분입니다. 도구의 name·description·inputSchema와 함께 선언하세요. description의 `[genos:bridge]`·`[genos:hitl]`을 포함한 이전 genos 태그는 로더가 오류로 거절합니다. 해당 서버의 도구 조회가 실패해도 다른 서버의 조회 성공 결과가 남을 수 있으므로 전체 도구 목록도 확인하세요.

일부 브릿지 처리기 주석에는 description 태그 우선 지원이라고 남아 있지만 현재 MCP 로더와 일치하지 않습니다. 이 문서는 Marvin이 확인한 **_meta만 지원**하는 계약을 따릅니다. 주석을 근거로 이전 태그를 새 설정에 넣지 마세요.
