<!-- fds-canonical-description:v3.1.18 record-id:P1-MON-02 -->
# P1-MON-02 — Dashboard / Alert / HA / Retention Enhancement

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-MON-02 |
| Phase | Phase 1 |
| Category | Monitoring / Observability |
| Type | Task |
| Status | To Do |
| Priority | P1 |
| Start | 2026-09-12 |
| End | 2026-09-18 |
| Calendar Days | 7 |
| Working Days | 1 |
| Lead | 이재환 |
| Support | 이권욱, 이하영 |
| Exit Criteria | Prometheus 2 Replica·Alertmanager 3 Replica, PDB/TopologySpread, Dashboard/Alert·장기보존 고도화와 장애·복구·P0 회귀 Evidence 및 Review |
| Related Decision IDs | D25; D33 |
| Related Risk IDs | RISK-05; RISK-07; RISK-09; RISK-14 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #25 snapshot 2026-09-10T04:08:35Z |
| Schedule Note | P1-MON-01의 P0 기본 3 View·Alert·15일 Retention·Watchdog 인수 후 HA·Dashboard/Alert·장기보존을 고도화한다. P1 Non-blocking. 이재환 09-14~17 부재를 반영한 가용일 1일이며 범위/일정 재평가는 별도 Lead 결정이다. |

## 현재 실행·검토 상태

담당자 보고 기준 미착수 / NOT RUN, Plan 2026-09-12~09-18 유지. Baseline §1.2/§11과 D33의 P1 범위인 HA·Dashboard/Alert 고도화·장기 보존을 수행한다. P0 기본 3 View·기본 Alert·15일 Retention·Watchdog은 P1-MON-01 책임이며 중복 완료 기준을 제거한다. P1 미완료는 P0 Gate를 자동 차단하지 않는다.

근거: [Issue #25](https://github.com/321Team/fds-project-baseline/issues/25), Issue 갱신 시각 `2026-09-10T04:08:35Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- [후속 기록](https://github.com/321Team/fds-project-baseline/issues/25#issuecomment-5612850684)

---

# User Story

모니터링 담당자로서 P1-MON-01의 P0 관측 기반을 인수한 뒤 HA·Dashboard/Alert·장기 보존을 고도화한다.

# Scope

## In Scope

- Prometheus 2 Replica, Alertmanager 3 Replica 구성과 장애·복구 검증
- PDB 및 TopologySpread로 가용성·배치 제약 검증
- 기본 3 View와 기본 Alert를 재사용한 Dashboard·업무 Threshold·Alert 고도화
- P0의 목표 15일 Local Retention을 넘는 장기 보존 방안 및 자원·저장소 영향 검증
- 변경 Source, Known Limitation, 장애·복구 Evidence와 Runbook

## Out of Scope

- P1-MON-01의 기본 3 View·기본 Alert·15일 Retention·외부 Watchdog 재구현
- Loki/SIEM, Production 통합관제·금융 HA 적합성 주장
- 승인되지 않은 저장소·네트워크·외부 알림·Plugin 추가

# 핵심 요구사항

- [ ] P1-MON-01의 Targets·Dashboard·Alert·PVC·Watchdog 인수 상태를 확인한다.
- [ ] Replica, PDB, TopologySpread와 실제 Worker/스토리지 장애영역의 제약을 함께 검토한다.
- [ ] 단일 Worker static local PV에 복제 수만 늘려 HA를 달성했다고 주장하지 않는다. 저장소 변경 시 별도 영향 검토를 연결한다.
- [ ] Threshold, Alert 지속/해제, 보존기간·용량은 실제 요구와 측정을 통해 확정하며 임의 값을 정본에 넣지 않는다.
- [ ] 기본 P0 시나리오의 회귀·복구와 Source 버전 추적을 유지한다.

# Acceptance Criteria

아래는 기존 Baseline §1.2/§11 및 D33의 P1 범위를 구체화한 후보다. 미실행 상태로 유지하며 발행 전 리뷰 대상이다.

- [ ] Prometheus 2 Replica·Alertmanager 3 Replica의 배치·Health와 장애/복구 Evidence가 확보된다.
- [ ] PDB·TopologySpread 적용, Drain/Failure 시 기대 가용성 및 저장소 제약을 검증한다.
- [ ] 기본 P0와 중복되지 않는 Dashboard/Alert 개선 및 Firing/Resolved Evidence를 확보한다.
- [ ] 장기 보존의 기간·용량·저장 방식과 변경 승인을 연결하고 재시작·복구를 검증한다.
- [ ] P0 Target·기본 3 View·기본 Alert·Watchdog 회귀에 이상이 없다.
- [ ] Source·Evidence Index·Known Limitation·Rollback/Recovery Runbook과 Review를 완료한다.

# 검증 및 증적

- `docs/evidence/P1-MON-02/`: 배치·Replica·PDB·TopologySpread·장애/복구·저장·Dashboard/Rule Source.
- 고도화 내용별 적용 Commit·측정 환경·실행 결과·SHA-256을 연결한다.

# Dependency

- Blocked By: P1-MON-01, P1-APP-01의 기본 관측 입력 및 P1-K8S-01의 실제 Worker/Storage 기반.
- Related: P1-SEC-01, P1-HA-02, P1-DOC-01.
- Phase 1 P1 / Close Tracking. P1 미완료는 P0 Gate의 자동 차단 사유가 아니며 Known Issue·Owner·Due로 관리한다.

# Decision / Risk Control

- D33과 Baseline §1.2/§11의 P0/P1 구분을 따른다. 새 통신·저장소·노출 변경은 CR/ICR 영향 검토 대상이다.
- 기존 Risk ID는 재명명하거나 해소 처리하지 않는다.

# Review / Handoff

- Lead 이재환, Support 이권욱·이하영. Monitoring/Storage/보안 변경과 P0 회귀 결과를 함께 검토한다.

# Completion Record

- Result: NOT RUN — 미착수.
- Status: To Do.
- Completed Date: 미입력.
- Reviewer / Approver: 미입력.
