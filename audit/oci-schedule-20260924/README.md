# OCI 연계 일정 정합화 — 2026-09-24 KST

사용자 지시: “일정 불일치부터 해소”. 일정과 문서 표시의 정정이다. OCI 도입 여부(D21), Runtime, AC, 상태, 담당, 비용·보안 승인 및 선행조건은 별도로 판정한다.

## 적용 계획

| 대상 | 정정/유지할 계획 | 달력일 / 작업일 |
| --- | --- | --- |
| #33 Phase 2 착수 | 2026-10-06 | 1 / 1 |
| #34 설계 동결 | 2026-10-06 | 1 / 1 |
| #35 IaC | 2026-10-06~13 | 8 / 5 |
| #36 OCI 검증 / D21 | 2026-10-06~08, D21 10-08 | 3 / 3 |
| #37 VPN | 2026-10-08~13 (선행조건 전 준비만) | 6 / 3 |
| #39 G4 | 2026-10-13 | 1 / 1 |

발행본의 OCI WBS는 10-06~09이고 D21/마일스톤 요약은 10-02로 남아 있었다. WBS의 비근무일 10-09를 제외하면 작업 가능일은 10-06·07·08의 3일이다. 따라서 종료/D21 계획 목표를 10-08로 통일해 가용 작업일을 보존한다. 이미 재계획한 P2 착수 10-06과 G4 10-13은 유지한다.

VPN의 10-08 착수는 선행조건을 우회하지 않는다. 기존 Blocked By P2-OCI-01·P2-IAC-01을 유지하고, 충족 전에는 준비 작업만 수행한다. IaC 완료 목표와 G4가 모두 10-13이므로 경로 적용·검증 작업창의 확보는 아직 보장되지 않았다. 선행 완료가 늦으면 G4를 자동 통과시키지 않고 일정 영향을 다시 판단한다.

## 반영 상태와 남은 동기화

- Issue #33~37·#39 본문의 계획 속성/기간/현행 설명을 이번 요청 범위에서 갱신한다. 실행 결과는 `execution-result.json`을 확인한다.
- 별도 Issue field **#36 Target date: 2026-10-09 → 2026-10-08** 갱신 필요.
- [Milestone #7 Phase 2 Start](https://github.com/321Team/fds-project-baseline/milestone/7): 기한 및 현행 계획 설명 **2026-09-28 → 2026-10-06** 갱신 필요. 09-18 당시 평가는 이력으로 보존하고 최신 정정을 상단에 추가한다.
- [Milestone #8 G4](https://github.com/321Team/fds-project-baseline/milestone/8): 기한 및 계획 설명 **2026-10-08 → 2026-10-13** 갱신 필요.
- 위 별도 필드와 마일스톤 기한/설명은 현재 연결의 쓰기 기능에 없어 미변경 상태다. 다른 마일스톤으로 재배정하지 않는다.
- 이 PR은 감사 기록과 정정안이다. 병합 및 차기 정본 발행과 구분한다. 기존 docs-v3.1.20 태그·Release asset·정본 경로는 덮어쓰지 않는다.
- 차기 정본 제작 시 Baseline §2·§13·D21·상태표, Ticket Pack, 티켓 Description, WBS, Milestone map 및 자동 생성 ticket-sync-map을 같은 계획으로 재생성한다. CHECKSUM/manifest/문서·슬라이드 배포본은 차기 전체 정본 검증 단계에서 갱신한다.

## 정정안 파일

- `proposed/canonical-schedule.patch`: v3.1.20 기준 Baseline/Ticket Pack/Milestone map의 최소 날짜 차이. 발행본에 직접 적용하기 위한 실행 지시가 아니며 차기 정본의 변경 근거다.
- `proposed/issue-*.md`: 적용할 티켓 본문. 기존 체크박스, Blocked By, 보관 원문을 보존했다.
- `proposed/FDS_OCI_Schedule_Correction_20260924.xlsx`: v3.1.20 기반 미발행 정정본. 9개 탭을 유지하고 WBS→마일스톤/간트 날짜 연결 및 기간을 계산했다.
- `source-snapshot.json`: 변경 직전 상태·일정·마일스톤과 본문 SHA-256.

## 검증

- WBS 재계산: OCI 달력 3일/작업 3일, IaC 8일/5일, VPN 6일/3일.
- D21 표시 및 Phase 2 Gantt: 10-08까지 표시, 10-09 제외.
- 기존 9개 탭, 수식 기반 날짜/기간, 조건부 서식·유효성·병합·테이블·그림 구조 개수 유지. 논리 셀 변경 22개(일정·메모·미발행 표시·변경 이력).
- 변경 영역 렌더 확인 및 수식 오류 검색 0건. 티켓 체크박스/선행조건/보관 원문 동일성 검증.
- 기존 Status To Do/open과 실제 Gate 판정은 바꾸지 않는다.

## 근거

- [발행 docs-v3.1.20](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.20), 조회 main `8bbe706c5339d77819f9db75bb7ed9a226c76087`.
- [Phase 2 착수 재계획](https://github.com/321Team/fds-project-baseline/issues/33#issuecomment-5779469087).
- [OCI 재계획 및 D21 동시 검토 필요 기록](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-5779876206).
- [IaC 재계획](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5779875658), [VPN 재계획](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-5779876610), [G4 재계획](https://github.com/321Team/fds-project-baseline/issues/39#issuecomment-5779877201).
- 비근무일은 발행 WBS Sources & Change Log / Team Calendar를 사용했다. 날짜는 KST 계획일이다.
