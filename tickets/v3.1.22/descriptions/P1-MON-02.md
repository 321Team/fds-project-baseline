문서 버전 **v3.1.22 / CANDIDATE**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# P1-MON-02 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/25) · updated_at `2026-10-19T10:20:17Z` · body SHA256 `1e1ce4b452787924003da6d37bb9690a733656e73cdcc45069ae8b06b49044c6`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P1-MON-02 |
| Phase | Phase 2 |
| Category | Monitoring / Observability |
| Type | Task |
| Status | To Do |
| Priority | P1 |
| Start | TBD — P0 인수 후 재계획 |
| End | TBD — 구현 유예 권장 |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이재환 |
| Support | 이권욱, 이하영 |
| Exit Criteria | Prometheus 2 Replica·Alertmanager 3 Replica, PDB/TopologySpread, Dashboard/Alert·장기보존 고도화와 장애·복구·P0 회귀 Evidence 및 Review |
| Related Decision IDs | D25; D33 |
| Related Risk IDs | RISK-05; RISK-07; RISK-09; RISK-14 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #25 snapshot 2026-09-10T04:08:35Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 프로젝트 종료일 2026-10-26 확정. 본 P1 carry-over에는 고정 구현일을 배정하지 않는다. P0 완료 후 실제 잔여 capacity가 있을 때만 착수하고, 미착수 시 Deferred/Known Issue로 Close한다. |

기존 P1 Record ID를 유지한 Phase2 이월이다. 구현 To Do·고정 구현 Due 미정·실제 인계수신과 기존 Activation Contract를 보존한다. Phase 변경은 실행/기술 Done 승인이 아니다.

### P2 업무 대시보드 기존 조건·대체안 보충

[기존 조건부 설계 선택](https://github.com/321Team/fds-project-baseline/issues/25#issuecomment-6158755475)의 “10/19까지 조건 미충족 시 콘솔 Observe → Metrics 대체안 사용, 미수행 Grafana 개선 Deferred/Known Issue”를 유지한다. 설치·회수 소스/버전, Thanos tenancy, 수집 경로, P2 대시보드 보정의 네 선행조건은 미완료이며 실제 설치 승인·수집 AC2 구현 완료가 아니다. 이 날짜를 고정 구현 Due로 전환하거나 이 문서로 새 ROSA 실행·대체안 시연 완료를 만들지 않는다. P0·G5 이후 여력 Activation Contract·Phase2 To Do·기존 담당/원 AC를 보존한다. 날짜만 있는 기존 조건의 시각을 임의로 정하거나, 10/19 당일 작성된 이 보충으로 자정 경과를 주장하지 않는다.

## 현재 원 AC — 체크 상태 보존

아래는 기존 Baseline §1.2/§11 및 D33의 P1 범위를 구체화한 후보다. 미실행 상태로 유지하며 발행 전 리뷰 대상이다.

- [ ] Prometheus 2 Replica·Alertmanager 3 Replica의 배치·Health와 장애/복구 Evidence가 확보된다.
- [ ] PDB·TopologySpread 적용, Drain/Failure 시 기대 가용성 및 저장소 제약을 검증한다.
- [ ] 기본 P0와 중복되지 않는 Dashboard/Alert 개선 및 Firing/Resolved Evidence를 확보한다.
- [ ] 장기 보존의 기간·용량·저장 방식과 변경 승인을 연결하고 재시작·복구를 검증한다.
- [ ] P0 Target·기본 3 View·기본 Alert·Watchdog 회귀에 이상이 없다.
- [ ] Source·Evidence Index·Known Limitation·Rollback/Recovery Runbook과 Review를 완료한다.

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
