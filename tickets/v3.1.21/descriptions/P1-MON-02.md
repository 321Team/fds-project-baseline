# P1-MON-02 — Dashboard / Alert Enhancement

Version: v3.1.21 CANDIDATE
Source: https://github.com/321Team/fds-project-baseline/issues/25
Updated at: 2026-10-01T07:14:02Z
Source body SHA256: `13756c85c0fffe6f87dc8d905476928e0c23545bfbf930cae0e8ec249fe28d8c`
GitHub: open / None
Current disposition: Source lifecycle/AC retained; no new acceptance by this publication.

| Property | Current source value |
|---|---|
| Record ID | P1-MON-02 |
| Phase | Phase 1 |
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
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #25 snapshot 2026-09-10T04:08:35Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | 프로젝트 종료일 2026-10-26 확정. 본 P1 carry-over에는 고정 구현일을 배정하지 않는다. P0 완료 후 실제 잔여 capacity가 있을 때만 착수하고, 미착수 시 Deferred/Known Issue로 Close한다. |

## Source checklist

- [ ] P1-MON-01의 Targets·Dashboard·Alert·PVC·Watchdog 인수 상태를 확인한다.
- [ ] Replica, PDB, TopologySpread와 실제 Worker/스토리지 장애영역의 제약을 함께 검토한다.
- [ ] 단일 Worker static local PV에 복제 수만 늘려 HA를 달성했다고 주장하지 않는다. 저장소 변경 시 별도 영향 검토를 연결한다.
- [ ] Threshold, Alert 지속/해제, 보존기간·용량은 실제 요구와 측정을 통해 확정하며 임의 값을 정본에 넣지 않는다.
- [ ] 기본 P0 시나리오의 회귀·복구와 Source 버전 추적을 유지한다.
- [ ] Prometheus 2 Replica·Alertmanager 3 Replica의 배치·Health와 장애/복구 Evidence가 확보된다.
- [ ] PDB·TopologySpread 적용, Drain/Failure 시 기대 가용성 및 저장소 제약을 검증한다.
- [ ] 기본 P0와 중복되지 않는 Dashboard/Alert 개선 및 Firing/Resolved Evidence를 확보한다.
- [ ] 장기 보존의 기간·용량·저장 방식과 변경 승인을 연결하고 재시작·복구를 검증한다.
- [ ] P0 Target·기본 3 View·기본 Alert·Watchdog 회귀에 이상이 없다.
- [ ] Source·Evidence Index·Known Limitation·Rollback/Recovery Runbook과 Review를 완료한다.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

<!-- issue-decision-contract-20261001:v1:start -->
## 2026-10-01 P1 Activation Contract v1

### Activate only if
- Phase 2 P0/G5 이후 capacity가 남고 Monitoring 개선이 Demo/운영가치에 직접 기여.
- 공용 OCP에서는 namespace-local dashboard/alert 기능만 검증하며 성능/용량 baseline은 만들지 않는다.

### Deferred is valid when
- P0 일정 또는 증적 정리에 영향을 주는 경우.
- Deferred 시 현행 대시보드/알람 한계, Owner, 차기 Due, 재개조건을 기록한다.

### Acceptance
실행 시 alert rule/source/threshold/test event/evidence를 추적하고 shared workload 수치를 SLO로 승격하지 않는다.
<!-- issue-decision-contract-20261001:v1:end -->

<!-- shared-ocp-boundary-20261001:start -->
## 2026-10-01 공용 OCP Lab 실행경계

교육기관 제공 OCP는 **공용 Multi-tenant Lab**으로 사용한다. Cluster/Node 독점은 전제하지 않으며, 이 환경의 결과는 기본적으로 `LAB-PRECHECK`이다.

### 공통 자원·명명 규칙
- 사람 간 Team Code는 `J1`, `J2` 형식으로 관리하되 Kubernetes Namespace 실제 이름은 소문자 DNS 형식으로 매핑한다.
- Namespace: `j1-<purpose>`, `j2-<purpose>` 형식. 예: `j1-fds-app`, `j1-monitoring`, `j1-cicd-test`.
- Team Code 미배정 상태에서는 문서 템플릿에 `jX-<purpose>`를 사용하고 실제 생성 전에 코드와 Owner를 고정한다.
- 생성 자원에는 최소 `team`, `project=fds-hybrid`, `purpose` label을 부여하고, Owner/만료일은 annotation 또는 동등 추적정보로 남긴다.
- ResourceQuota/LimitRange의 **정확한 수치**는 공용 OCP 관리자 정책을 따른다. 임의로 quota를 확대하거나 다른 조의 자원을 침범하지 않는다.

### 허용/금지 경계
- 허용: Namespace-local Deployment/Service/Route, namespace RBAC, NetworkPolicy, SecurityContext, manifest/schema, health, image pull, 이미 제공된 Operator의 허용 범위 내 namespace-local CR 사전검증.
- 금지/사전승인 필요: 신규 cluster-wide Operator 설치, CRD/ClusterRole/SCC/MachineConfig/Node 설정 변경, cluster-admin 사용, Node 전용 affinity/taint로 사실상 독점, hostNetwork/hostPort/privileged의 임의 사용, Node reboot/drain·장애주입·대규모 load/performance/HA 시험.
- 공용 OCP의 다른 사용자 workload 영향을 받는 성능·용량·HA 수치는 **인수 증적이 아니다**.

### Evidence / Cleanup
- 증적에는 `ENV=SHARED_OCP_LAB`, Cluster/Version, Team Code, Namespace, 실행시각, manifest/source SHA, 명령/RC/원본 로그를 포함한다.
- 공용 OCP PASS를 ROSA Runtime PASS로 승격하지 않는다. ROSA P0 인수조건은 실제 ROSA에서 재검증한다.
- 시험 종료 시 자기 Team Namespace/자원만 정리하고, 삭제 전/후 resource inventory를 보존한다.
<!-- shared-ocp-boundary-20261001:end -->

### 이 티켓 적용
Dashboard/Alert 개선은 공용 OCP의 namespace-local 관측 대상으로 선검증할 수 있으나, shared workload 영향을 받는 성능/용량 수치를 기준선 또는 인수값으로 사용하지 않는다.

<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23 (누락분 2026-09-25 반영)

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P1-MON-02/` → 변경 후: `321Team/fds-project-evidence` `evidence/P1-MON-02/`
- 이 티켓은 2026-09-23 일괄 반영(49건)의 대상 추출에서 누락되어 2026-09-25 같은 형식으로 반영했다(“Evidence Path:” 표기 없이 경로만 적힌 형식). 근거: `audit/phase2-repo-bootstrap-20260923/evidence-path-followup-20260925/`.
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** P1 고도화/HA·보존 확대 후속. #17 기본 Dashboard/Alert 중복 금지; DB 알림 편입은 선택 필요.

- P1 고도화의 Prometheus2/Alertmanager3·PDB/TopologySpread·보존 확대는 단일 Worker PV에 Replica만 늘려 HA라고 선언하지 않는다. DB 실패 알림 제안 편입 여부를 #17/infra-db #2와 연결한다.

**인계·관련 티켓:** [#17](https://github.com/321Team/fds-project-baseline/issues/17) · [#26](https://github.com/321Team/fds-project-baseline/issues/26) · [#27](https://github.com/321Team/fds-project-baseline/issues/27).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-milestone-assignment:2026-09-11 issue:25 -->
## 대표 Milestone 배정 — 2026-09-11

- **추적 Milestone:** Phase 1 Close (GitHub #6)
- **배정 성격:** WBS 기반 대표 추적 항목 · 이권욱 사용자 지시에 따른 지정.
- **배정 근거:** WBS의 Phase 1 P1 / Close Tracking 및 09-23 Known Issue·Owner 인계 계획에 따라 Phase 1 Close에 배정한다. 이 배정은 미결 사항 인계 추적이며 구현 완료 약속이 아니다.
- **출처:** [발행 정본 v3.1.18 WBS · WBS/Fast Track Plan 시트](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/wbs/FDS_v3.1.18_WBS_and_Gantt_v1.0.xlsx)
- **유예 처리:** Start/End TBD와 To Do를 유지한다. 09-23은 Known Issue·Owner 인계 계획, 09-28은 차기 착수·납기 결정 계획이며 구현 완료일이 아니다. P0 인수 후 재계획하며 Phase 2 공수를 자동 배정하지 않는다.
- **일정 원칙:** 일정은 고정된 필수 기한이 아닌 조정 가능한 계획 목표다. 선행조건과 영향 확인 후 유연하게 조정하며 실제 완료일·승인·Runtime 증적 요건과 구분한다.
- **적용 범위:** 대표 Milestone 연결과 근거 기록. 기존 상태·AC·담당·Start/End·Gate 요건과 보관 이력을 유지하며 새로운 Gate 필수조건을 추가하지 않는다.

---

<!-- fds-notion-migration:2026-09-09 record-id:P1-MON-02 -->
<!-- fds-canonical-description:v3.1.18 record-id:P1-MON-02 -->
# P1-MON-02 — Dashboard / Alert / HA / Retention Enhancement

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-MON-02 |
| Phase | Phase 1 |
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
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #25 snapshot 2026-09-10T04:08:35Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | 프로젝트 종료일 2026-10-26 확정. 본 P1 carry-over에는 고정 구현일을 배정하지 않는다. P0 완료 후 실제 잔여 capacity가 있을 때만 착수하고, 미착수 시 Deferred/Known Issue로 Close한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T04:08:35Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.
- 수집된 운영 댓글은 원래 위치에 보존한다. 신규 구현 제출/리뷰 요청은 실행 PASS나 승인으로 간주하지 않는다.
  - [5612850684](https://github.com/321Team/fds-project-baseline/issues/25#issuecomment-5612850684) · 2026-09-10T04:08:35Z

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

담당자 보고 기준 미착수 / NOT RUN, Plan 2026-09-12~09-18 유지. Baseline §1.2/§11과 D33의 P1 범위인 HA·Dashboard/Alert 고도화·장기 보존을 수행한다. P0 기본 3 View·기본 Alert·15일 Retention·Watchdog은 P1-MON-01 책임이며 중복 완료 기준을 제거한다. P1 미완료는 P0 Gate를 자동 차단하지 않는다. 현재 후보 Plan: TBD — P0 인수 후 재계획 ~ TBD — 구현 유예 권장 (권장안; 실제 완료일·Gate 승인은 미확정).

근거: [Issue #25](https://github.com/321Team/fds-project-baseline/issues/25), Issue 갱신 시각 `2026-09-10T04:08:35Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

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

- `321Team/fds-project-evidence:evidence/P1-MON-02/`: 배치·Replica·PDB·TopologySpread·장애/복구·저장·Dashboard/Rule Source.
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

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `34d11a2cb5b53d4a510a21cabe02f92178b090320cd793e1d242529d8e6bcd69`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P1-MON-02 -->
# P1-MON-02 — Dashboard / Alert Enhancement

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
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
| Exit Criteria | 거래·FDS·Node·Pod 상태 Dashboard와 최소 Alert Rule을 구성하고 정상·장애 시나리오 Evidence 확보 |
| Related Decision IDs | D25 |
| Related Risk IDs | RISK-05; RISK-07; RISK-09; RISK-14 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Network_Baseline_v2.3; FDS_Phase1_Logical_Architecture_v3.1.2; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | P1-MON-01의 Metric 수집 완료 후 수행한다. Grafana 또는 Prometheus UI 중 승인된 최소 구현을 사용하며 Loki/SIEM은 Scope Out이다. |

## 이관 기준 및 확인 사항

- 속성의 일정·담당·상태는 RELEASED v3.1.17 WBS(기준일 2026-09-04)를 우선 반영했다. 이후 별도 근거가 있는 변경만 아래에 명시한다.
- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`
- `FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx`

---

## Description — 보관 입력본

> 원본: `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

# 🎯 User Story

모니터링 담당자 이재환으로서 핵심 거래·FDS·플랫폼 지표를 Dashboard와 Alert로 가시화한다. 이를 통해 이상 상태를 수동 조회에 의존하지 않고 빠르게 식별한다.

---

# 📌 Scope

## In Scope

- 거래·FDS Dashboard
- Node/Pod 상태 Dashboard
- 최소 Alert Rule
- 정상·장애 시나리오
- Runbook·Evidence

## Out of Scope

- Loki/SIEM 통합
- 고급 On-call 체계
- Production 통합관제

---

# 📋 핵심 요구사항

- [ ] P1-MON-01 Metric을 재사용한다.
- [ ] Alert 조건·지속시간·해제조건을 명시한다.
- [ ] 과도한 오탐을 피하도록 최소 Rule만 적용한다.
- [ ] Dashboard/Rule Source를 버전 관리한다.

---

# ✅ Acceptance Criteria

- [ ] 거래·FDS·오류·상태 지표가 Dashboard에 표시된다.
- [ ] 승인 장애 시 Alert가 발생한다.
- [ ] 정상 복구 후 Alert가 해제된다.
- [ ] Metric·Dashboard·Alert Evidence가 연결된다.

---

# 🧪 검증 및 증적

- Dashboard Export/화면
- Alert Rule Source
- Firing/Resolved 결과
- Known Issue
- Evidence Path: docs/evidence/P1-MON-02/

---

# 🔗 Dependency

- **Blocked By:** P1-MON-01; P1-APP-01
- **Blocks / Next:** P1-DOC-01 또는 Known Issue 이관
- **Related Ticket:** P1-E2E-01
- **Milestone:** Phase 1 P1 / Close Tracking

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D25
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-05; RISK-07; RISK-09; RISK-14
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** 거래·FDS·Node·Pod 상태 Dashboard와 최소 Alert Rule을 구성하고 정상·장애 시나리오 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>

