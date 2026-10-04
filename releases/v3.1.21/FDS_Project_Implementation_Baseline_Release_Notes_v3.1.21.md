# v3.1.21 Release Notes

CANDIDATE / NOT RELEASED. 기준 2026-10-03 KST.

- 78 Issue 최신 속성/원문·해시와 완료 CR/Decision을 WBS·Baseline·Ticket Pack·78 Description에 반영.
- 테스트 전략 TS01~16: 생성 전/후 Gate 분리, #119 failure contract, #125/#130 생산·인수 경계, source/CA/DNS/복구·비용 증적.
- D21 FINAL을 반영하되 raw publication·Issue Close HOLD 유지. Architecture/Stage-A/P1 Close 인수 아님.
- WBS 58→78 Record, 9→10 sheets(Test Strategy 추가). 상태 집계는 원문 그대로 {'Done': 27, 'In Progress': 12, 'To Do': 38, 'Todo': 1}. native lifecycle 불일치는 메모로 보존.
- 계획일 유지. 10/12 capacity 제안은 채택하지 않고 최초 Freeze 전 입력 제약으로 정렬. 실제 완료일 생성 없음.
- 현재 14 source main HEAD가 11:53 전체 수집과 동일함을 재확인. Architecture main은 추가 source로 기록. 257 merged 입력의 과거 capture 시각은 유지.
- v3.1.20 원본/Tag/Asset과 CURRENT.md 변경 없음. 현재 PR112는 코드 혼합이며 exact-head 독립 승인 미확보.

알려진 한계: #125/#128/#130 필수 속성 일부 미기재, #128 Todo vs closed/not_planned, 2 Record milestone 미배정. 원문을 임의 보완/승인하지 않는다. 계획 베이스라인은 이 차이를 명시적으로 보존하며 live ticket 동기화 결정은 별도다.
P1 Close10/6 결과와 Runtime 원본은 향후 새 수집/정본 변경으로 반영한다. 이번 산출물을 실제 실행 증적으로 사용하지 않는다.
