표 도구는 원본 행을 모델이 다시 작성하지 않고 서버에서 필터·계산하도록 합니다. 일반 Vault 목록 저장과 다릅니다. MonimoAgent의 **표 데이터 처리**를 켜고 응답의 payload에서 type:table을 명시해야 합니다. 선언하지 않은 배열은 자동으로 표가 되지 않습니다.

## 표 저장과 목록 확인

```json
{"payload":{"rows":[{"category":"식비","amount":"15000"},{"category":"교통","amount":"5000"}],"genos-vault":[{"type":"table","path":"$output.payload.rows"}]}}
```

`table_load({})`는 현재 실행의 표 목록과 수집 오류를 반환합니다. `table_load({"tableRef":"발급된 참조"})`는 출처·경로·행 수·열 목록을 반환하며 원본 행을 모델에 반환하지 않습니다. 목록은 ref, 특정 표 결과는 tableRef를 사용합니다. 실제 호출에는 반환받은 UUID 또는 Vault table 참조를 그대로 넣습니다.

## table_filter

```json
{"tableRef":"{{$vault.table_a0000000-0000-4000-8000-000000000001}}","combine":"and","predicates":[{"column":"category","operator":"eq","value":"식비"}]}
```

새 tableRef를 반환하며 원본은 바꾸지 않습니다. combine은 and 또는 or이고 조건은 1~20개입니다. eq·ne는 타입까지 비교하므로 숫자 1과 문자열 "1"은 다릅니다. gt·gte·lt·lte는 숫자나 십진 문자열을 수치로 비교합니다. contains는 대소문자를 구분한 문자열 포함 비교입니다. is_null·not_null에는 value를 넣지 않습니다.

## table_calculate 집계

```json
{"tableRef":"{{$vault.table_a0000000-0000-4000-8000-000000000001}}","aggregates":[{"name":"total","column":"amount","operation":"sum"},{"name":"rows","operation":"count"}]}
```

count는 column을 생략하고 나머지는 column이 필요합니다. sum·average·min·max를 지원합니다. 집계 결과는 results의 각 키에 발급된 값 참조로 반환됩니다. 반환된 참조를 최종 답변이나 다음 도구에 그대로 사용하세요. 모델이 합계를 다시 계산하지 않습니다.

## table_calculate 행 계산

```json
{"tableRef":"{{$vault.table_a0000000-0000-4000-8000-000000000001}}","calculations":[{"name":"doubled","operation":"multiply","left":{"column":"amount"},"right":{"constant":"2"}}]}
```

add·subtract·multiply·divide를 지원합니다. 피연산자는 column 또는 십진 문자열 constant 중 정확히 하나입니다. 새 열을 가진 새 표 참조를 반환합니다. 십진 정밀도 50, half-up 반올림이며 결과 숫자는 decimal-string입니다. 0으로 나누기·기존 열과 이름 충돌·집계 결과 이름 중복을 거절합니다. aggregates와 calculations는 하나만 지정하고 각 배열은 1~20개입니다.

## 한도와 오류

표는 객체 행의 배열로 최대 10,000행·100열·JSON 2 MiB입니다. 연산 실패는 ok:false와 TABLE 계열 코드로 전달합니다. 잘못된 연산을 수정하거나 제한을 설명해야 하며 표를 되살리기 위해 완료된 업무 도구를 다시 호출하지 않습니다. 표 참조의 보관 범위·종료·보호 로그는 Vault 규칙을 따릅니다.


근거: [tabularData.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/tabularData.ts) · [tabularTools.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/tabularTools.ts) · [tabularStore.ts](https://github.com/genonai/GenOS/blob/7936b3166da1127a1e9e9161ed89efb4a8abbfbd/flowise/3.0.0/before_install/packages/components/src/tabularStore.ts).
