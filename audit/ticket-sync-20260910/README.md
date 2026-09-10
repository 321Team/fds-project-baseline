# Ticket Property Synchronization Result

2026-09-10 · repository: 321Team/fds-project-baseline · Overall: PARTIAL

## 결과

| 항목 | 전 | 후 |
|---|---:|---:|
| 대상 Issue(PR 제외) | 64 | 64 |
| Lead와 일치하는 Assignee | 64 | 64 |
| 라벨이 있는 Issue | 61 | 64 |
| Record ID 중복 | 0 | 0 |
| 필수 17개 속성 키 누락 | 0 | 0 |
| 확정 속성 대비 라벨 차이 | 3 | 0 |
| 상태/종결 reason 불일치 | 0 | 0 |
| 실제 Issue Type 미설정 | 64 | 64 |
| 실제 Milestone 미배정 | 64 | 64 |
| 원본 속성 미확인 티켓 | 2 | 2 |

검색 응답의 labels/assignees/milestone=null을 실제 미설정으로 집계한 이전 안내는 오류였다. 이번에는 전체 REST Issue 응답과 적용 후 재조회로 검증했다. 본문에 필드가 있다는 것과 그 값이 확정되었다는 것도 구분했다.

## 실제 원격 변경

- [#4 DEC-P1-FDS-01](https://github.com/321Team/fds-project-baseline/issues/4): type:decision, priority:P0, status:done, phase:phase-1, area:application 추가.
- [#5 DEC-P1-TXN-01](https://github.com/321Team/fds-project-baseline/issues/5): 동일 라벨 추가.
- [#6 DEC-P1-ADMIN-01](https://github.com/321Team/fds-project-baseline/issues/6): type:decision, priority:P0, status:done, phase:phase-1, area:security 추가.
- 기존 Label 카탈로그를 사용한 additive 변경. 새 라벨 생성·기존 라벨 삭제 없음.
- 세 Issue 건별 직전 조회/적용/재조회 및 전체 64건 재조회 완료.
- 전체 64건의 body/title/state/state_reason/Assignee/native Type/Milestone 변경 0건. AC·승인/종결·계획일은 본문 SHA-256 동일로 보존 확인.

## 검증

- Python 구문 검사 PASS.
- 단위 테스트 18/18 PASS: 중복 Record ID, source drift, marker mismatch, 관리 라벨 충돌, 원본 미확인 보존, 계정/상태 불일치 차단, native Type 오분류 방지, Milestone 추정 방지 및 서버 반환 number 사용, due date 불일치 차단, 수동 Label 보존, PR 제외.
- 실제 재조회 스냅샷 감사: 변경할 Label 0, 강제 변경 차단 오류 0. 원본 미확인/미반영은 별도 예외이므로 전체 결과는 PARTIAL.
- native Type/Milestone gh 경로는 모의/로컬 검증만 수행. 실제 gh 실행 NOT RUN. 현재 실행 환경에는 gh 및 정상 설정된 GH_TOKEN/GITHUB_TOKEN이 없고 연결 도구에는 Type 쓰기와 Milestone 카탈로그 조회·생성 기능이 없다. 연결 자격증명을 추출하거나 다른 권한 경로를 사용하지 않음.
- 사실만 확인했으며 사람의 새 독립 리뷰/승인, CI PASS, Runtime PASS를 생성하지 않음.

## 잔여 항목

1. Native Type: 확정 업무 Type 62건은 type 라벨로 표현. 실제 Type은 아직 null. #59/#61은 업무 Type도 원본 미확인.
2. Milestone: 44건 문서상 단일 매핑 완료, 20건 매핑 HOLD. 실제 64건의 Milestone 필드는 미배정. 저장소의 카탈로그 부재를 단정하지 않음.
3. #59 D-ARC-01 / #61 D-WBS-01: 원본 속성 미확인 유지. 과거 종결/기간 일부 참조는 전체 속성 표의 완전 복원을 입증하지 않으므로 추정 보완하지 않음.
4. #46 P2-CICD-01: 본문 Milestone G5(2026-10-16)와 End(2026-10-19)의 차이. 기간이나 목표를 자동 이동하지 않고 해당 매핑 HOLD.
5. Notion 원격 변경, 완료 티켓의 누락 AC 증거 복원, WBS 재기준선화는 이번 메타데이터 동기화 완료에 포함하지 않음.

## 정본 인계

- README와 4개 핵심 정책 문서, 실행 Runbook, 기계 판독 매핑, 스크립트 및 테스트를 준비했다.
- 현재 RELEASED main 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c를 직접 수정하지 않는다.
- 기존 v3.1.18 Draft PR #3의 HEAD 15bdbac9b646f30c18d17b34fcf403fd12ef675c에서 파생한 별도 검토 브랜치로 제출한다. 기존 #3의 HEAD는 바꾸지 않는다.
- 본 변경 후보는 v3.1.18 전체 정본 묶음의 완성이나 발행이 아니다. 독립 리뷰와 기존 Release Gate 후 인계해야 한다. merge는 수행하지 않음.

기계 판독 결과: [result.json](result.json). 본문 전체 원본을 중복 배포하지 않고 전후 body SHA-256 및 실제 메타데이터를 기록한다.

