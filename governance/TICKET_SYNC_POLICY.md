# Ticket Synchronization Policy

Version: 1.2 · 2026-09-18 · 사용자 결정에 따른 승인 절차 개정. [Lead 위임 정책](REVIEW_AUTHORITY_POLICY.md)에 따라 코드 병합만 독립 리뷰하며 문서·실행·증적 수용·종결은 해당 Lead가 결정한다. 운영 속성 보정과 정본 발행 상태는 구분한다.

## 1. 필드별 권위와 충돌

| 대상 | 권위 | 충돌 처리 |
|---|---|---|
| Record ID, 계획, Scope, 책임, 일정 | RELEASED 문서와 승인된 변경 기록 | 최신 날짜라는 이유만으로 덮어쓰지 않음 |
| 실제 실행, 리뷰, 완료일 | 해당 티켓의 실제 증적·승인·종결 이력 | 오래된 Ticket Pack 상태로 되돌리지 않음 |
| Label, Assignee, Issue Type, Milestone | 확인된 속성의 운영 표현 | 본문과 대조하고 불일치는 HOLD |
| 다음 정본 반영 | 후보 PR 및 RELEASE_POLICY | 이슈 동기화를 정본 발행으로 확대하지 않음 |
| Notion | 승인된 입력본 및 원격 반영 결과 | GitHub 갱신만으로 동기화 완료라고 하지 않음 |

Issue 본문 상단 17개 속성표만 메타데이터 입력으로 읽는다. 아래 `보관 입력본`은 역사적 기록이다. 본문 전체를 대충 검색하여 과거 상태를 현행 값으로 선택하지 않는다. 실행 상태 변경 근거는 해당 기록에 연결되어야 한다. 각 실행의 변경 범위는 그 실행 계획과 전후 증적으로 확인한다.

필수 속성: Record ID, Phase, Category, Type, Status, Priority, Start, End, Calendar Days, Working Days, Lead, Support, Exit Criteria, Related Decision IDs, Related Risk IDs, Source, Schedule Note.

## 2. 유일키와 Upsert

1. open/closed와 전체 페이지를 조회하고 PR을 제외한다.
2. Record ID가 없거나 중복, 제목 접두어/기존 migration marker와 불일치하면 Apply를 중단한다.
3. 알려진 Record ID를 기존 Issue에 Update한다. 이 스크립트는 새 Issue를 만들지 않는다.
4. `<!-- fds-notion-migration:... record-id:... -->`는 과거 이관 이력이다. 날짜 변경이나 재생성 없이 보존한다.
5. 대상 목록·본문 SHA-256·상태·기존 메타데이터를 계획에 고정하고 실제 반영 직전에 다시 대조한다.
6. 수동 변경/댓글 갱신 등으로 스냅샷이 달라지면 새 계획을 만든다. 반복 실행은 차이 없는 항목을 쓰지 않는다.

## 3. 상태와 종결

| 본문 Status | GitHub state | state_reason | Label |
|---|---|---|---|
| To Do | open | 해당 없음 | status:to-do |
| In Progress | open | 해당 없음 | status:in-progress |
| In Review | open | 해당 없음 | status:in-review |
| Blocked | open | 해당 없음 | status:blocked |
| Done | closed | completed | status:done |
| Cancelled | closed | not_planned | status:cancelled |

Blocked는 업무 진행 상태이며 Runtime Gate HOLD와 같은 값이 아니다. Gate HOLD만으로 Status를 자동 변경하지 않는다. 기존 티켓에 없는 확장값은 허용 사전일 뿐 상태 변경 지시가 아니다.

담당 Lead는 필수 AC·원본 증적·잔여 작업을 확인해 자기 업무의 인수·종결을 결정한다. 코드 병합 외 단계의 Support 독립 승인을 반복 필수화하지 않는다. 이 위임은 아래 동기화 스크립트의 자동 쓰기 범위를 확대하지 않는다.

동기화 스크립트는 state/state_reason을 쓰지 않는다. 불일치하면 근거와 담당자 판단을 요청한다. Done 티켓도 모든 AC를 자동 체크하지 않는다. 결정 완료·미도입/유예·N/A·이관·Runtime NOT RUN을 구분한다. 예를 들어 #4~6 Done은 미도입/유예 결정 종결이지 신규 기능 구현 PASS가 아니다. 기존 승인자·Reviewer를 새 승인으로 복제하지 않는다.

## 4. 속성 예외

- `원본 속성 미확인`: 해당 필드는 추정하여 쓰지 않는다. #59 D-ARC-01·#61 D-WBS-01은 2026-09-11 첨부 원본으로 속성 복원이 완료됐다. 날짜·기간 모순은 같은 날 사용자 정정(#59 End 8/26, #61 Completed Date 8/26)으로 해소됐고 차기 정본 반영은 별도 잔여이며, 과거 미확인 표시는 이력으로 보존한다.
- 필드 존재와 값 확정을 구분한다. `TBD`인 승인 일정은 누락 값으로 임의 대체하지 않는다.
- Start/End는 유연하게 조정 가능한 계획 목표이며 Completed Date와 구분한다. 날짜 변경 자체를 승인 차단이나 Runtime FAIL로 판정하지 않는다. 계획 변경 시 현행 문서와 티켓의 값·근거를 정합화하고 실제 완료일·기간은 원본 증적 없이 바꾸지 않는다.
- Category의 전체 의미는 본문에 보존하고 기존 대표 `area:*`만 유지한다. 임의 다중 라벨 대량 추가 없음.
- 단일 Milestone 매핑 미확정은 null을 확정 N/A로 해석하지 않는다. `HOLD`로 기록한다.
- 존재하지 않는 Label/Type/Milestone을 즉석 생성하지 않는다. 카탈로그 계획과 별도 명시적 적용으로 관리한다.

## 5. 안전한 쓰기와 감사

- 허용 쓰기: 확정된 labels, assignees, 기존 카탈로그의 정확한 native type/milestone.
- 금지 쓰기: body/title/Record ID/AC/Source/일정/승인/종결, 댓글 삭제, close/reopen, 권한·Ruleset 변경, main push/merge/발행.
- 사용자 수동 라벨과 추가 Assignee를 보존한다. 같은 관리 namespace의 충돌 라벨은 자동 삭제하지 않고 중단한다.
- 인증/권한 실패, 403/404/409/422, stale plan 또는 응답 불일치가 발생하면 중단한다. 연결 토큰 추출·권한 우회·다른 계정 전환은 하지 않는다.
- 적용 건마다 before → 요청 필드 → 재조회 결과를 기록한다. 실패 시 이후 건을 멈추고 부분 완료를 보고한다. 자동 롤백으로 동시 편집을 덮어쓰지 않는다.
- 원본 본문·메타데이터 스냅샷은 보안 통제된 별도 감사 경로에 보관한다. 토큰·Secret·개인키를 기록하지 않는다.

## 6. 완료 판정

`COMPLETE`: 중복/필수 속성 누락/허용값 오류/계정·상태·메타데이터 불일치가 0이며, 요구된 native Type 및 Milestone이 확인되거나 근거 있는 N/A·대체 승인이 있다.

`PARTIAL`: Label/담당자 일부 완료라도 source unknown, native 기능 미반영, Milestone HOLD가 남음. 전체 PASS로 쓰지 않는다.

`STOP`: 권한 오류, 식별 충돌, 변경 중 drift, 결과 검증 실패. 추가 쓰기를 중단하고 원인·적용 완료 번호·미적용 번호를 보고한다.

## 7. 정본 인계

현재 발행 정본은 [CURRENT.md](../CURRENT.md)와 실제 GitHub Release로 확인하며 후속 검토 후보와 구분한다. 승인된 이번 운영 속성 보정은 다음 후보의 정책·감사 기록에 연결한다. README/정책만 변경한 PR은 정본 Lead가 정확한 SHA를 검토·결정한다. 코드/자동화 변경이 함께 있으면 최소 1인의 독립 코드 리뷰가 필요하다. 기존 Release 묶음 검증은 유지하며 최종화·발행은 정본 Lead가 결정한다. Ticket Pack/WBS/Release의 상태·기간·증적을 이번 메타데이터 작업만으로 재발행하지 않는다.
