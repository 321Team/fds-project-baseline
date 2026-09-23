<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P1-HA-02/` → 변경 후: `321Team/fds-project-evidence` `evidence/P1-HA-02/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** P1 회복력 후속 유예. 가용성 기준은 착수 전에 확정 ; A03의 P0 범위와 분리.

- 기존 유예 계획을 유지한다. Rolling Update·CP1대 장애·PDB/TopologySpread별 가용성 관찰/허용 오류·복구 판정을 착수 전에 정한다. P0 #22와 적용 범위·결과를 분리한다.

**인계·관련 티켓:** [#10](https://github.com/321Team/fds-project-baseline/issues/10) · [#22](https://github.com/321Team/fds-project-baseline/issues/22).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-milestone-assignment:2026-09-11 issue:27 -->
## 대표 Milestone 배정 — 2026-09-11

- **추적 Milestone:** Phase 1 Close (GitHub #6)
- **배정 성격:** WBS 기반 대표 추적 항목 · 이권욱 사용자 지시에 따른 지정.
- **배정 근거:** WBS의 Phase 1 P1 / Close Tracking 및 09-23 Known Issue·Owner 인계 계획에 따라 Phase 1 Close에 배정한다. 플랫폼 복원력 검증 완료일로 해석하지 않는다.
- **출처:** [발행 정본 v3.1.18 WBS · WBS/Fast Track Plan 시트](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/wbs/FDS_v3.1.18_WBS_and_Gantt_v1.0.xlsx)
- **유예 처리:** Start/End TBD와 To Do를 유지한다. 09-23은 Known Issue·Owner 인계 계획, 09-28은 차기 착수·납기 결정 계획이며 구현 완료일이 아니다. P0 인수 후 재계획하며 Phase 2 공수를 자동 배정하지 않는다.
- **일정 원칙:** 일정은 고정된 필수 기한이 아닌 조정 가능한 계획 목표다. 선행조건과 영향 확인 후 유연하게 조정하며 실제 완료일·승인·Runtime 증적 요건과 구분한다.
- **적용 범위:** 대표 Milestone 연결과 근거 기록. 기존 상태·AC·담당·Start/End·Gate 요건과 보관 이력을 유지하며 새로운 Gate 필수조건을 추가하지 않는다.

---

<!-- fds-notion-migration:2026-09-09 record-id:P1-HA-02 -->
<!-- fds-canonical-description:v3.1.18 record-id:P1-HA-02 -->
# P1-HA-02 — Platform Resilience P1 Validation

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-HA-02 |
| Phase | Phase 1 |
| Category | HA / Platform Resilience |
| Type | Task |
| Status | To Do |
| Priority | P1 |
| Start | TBD — P0 인수 후 재계획 |
| End | TBD — 구현 유예 권장 |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | Rolling Update, Control Plane 1대 장애, PDB 및 TopologySpreadConstraint 검증 결과와 복구 Evidence 확보 |
| Related Decision IDs | D02; D25 |
| Related Risk IDs | RISK-03; RISK-05; RISK-07; RISK-14 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #27 snapshot 2026-09-10T02:09:41Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | P0 마감 보호를 위해 신규 구현을 유예하는 권장안이다. 기존 Lead·Type·Priority·AC·To Do는 유지한다. 09-23은 Known Issue/Owner 인계 기한, 09-28은 차기 착수·납기 결정 기한이며 구현 완료일은 TBD다. Phase 2 공수를 자동 배정하지 않는다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T02:09:41Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다. 현재 후보 Plan: TBD — P0 인수 후 재계획 ~ TBD — 구현 유예 권장 (권장안; 실제 완료일·Gate 승인은 미확정).

근거: [Issue #27](https://github.com/321Team/fds-project-baseline/issues/27), Issue 갱신 시각 `2026-09-10T02:09:41Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Kubernetes 담당자 이하영으로서 Phase 1의 선택적 플랫폼 복원력 항목을 통합 검증한다. 이를 통해 Rolling Update, Control Plane 장애 및 배치제약의 운영 영향과 복구 절차를 Evidence로 남긴다.

---

# Scope

## In Scope

- Rolling Update
- Control Plane 1대 장애
- PDB
- TopologySpreadConstraint
- 장애·복구·E2E 검증

## Out of Scope

- 다중 Control Plane 동시 장애
- 다중 Site DR
- Production SLA 보증

---

# 핵심 요구사항

- [ ] 실행 전 정상 Baseline을 기록한다.
- [ ] 업무 서비스 가용성 기준을 사전 정의한다.
- [ ] 장애 주입과 복구 순서를 Runbook으로 작성한다.
- [ ] 미완료 항목은 Known Issue에 Owner 이하영과 Due를 기록한다.

---

# Acceptance Criteria

- [ ] Rolling Update 중 승인 서비스 기준을 충족한다.
- [ ] Control Plane 1대 중단 후 API와 Workload 상태가 기대와 일치한다.
- [ ] PDB/TopologySpreadConstraint가 배포·Drain 시 기대대로 작동한다.
- [ ] 복구 후 E2E가 통과한다.

---

# 검증 및 증적

- Node/Pod 상태 전후 비교
- Update/Failure/Recovery Log
- PDB/TopologySpread Manifest
- E2E 결과
- Evidence Path: `321Team/fds-project-evidence:evidence/P1-HA-02/`

---

# Dependency

- **Blocked By:** P1-K8S-01; P1-E2E-01 Initial
- **Blocks / Next:** P1-DOC-01 또는 Known Issue 이관
- **Related Ticket:** P1-HA-01
- **Milestone:** Phase 1 P1 / Close Tracking

---

# Decision / Risk Control

- **Related Decision IDs:** D02; D25
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-03; RISK-05; RISK-07; RISK-14
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** Rolling Update, Control Plane 1대 장애, PDB 및 TopologySpreadConstraint 검증 결과와 복구 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `6208cea8d4738b3b94a75c359b63bb37e0c38d6f6ee7060c1f3f72a9ca0c83b8`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P1-HA-02 -->
# P1-HA-02 — Platform Resilience P1 Validation

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-HA-02 |
| Phase | Phase 1 |
| Category | HA / Platform Resilience |
| Type | Task |
| Status | To Do |
| Priority | P1 |
| Start | 2026-09-14 |
| End | 2026-09-18 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | Rolling Update, Control Plane 1대 장애, PDB 및 TopologySpreadConstraint 검증 결과와 복구 Evidence 확보 |
| Related Decision IDs | D02; D25 |
| Related Risk IDs | RISK-03; RISK-05; RISK-07; RISK-14 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Network_Baseline_v2.3; FDS_Phase1_Logical_Architecture_v3.1.2; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 기존 P1-HA-02와 P1-HA-03 및 기준선의 PDB/TopologySpreadConstraint P1 범위를 통합한다. 미완료 시 Phase 1 Close의 Known Issue에 Owner 이하영과 Due를 기록한다. |

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

Kubernetes 담당자 이하영으로서 Phase 1의 선택적 플랫폼 복원력 항목을 통합 검증한다. 이를 통해 Rolling Update, Control Plane 장애 및 배치제약의 운영 영향과 복구 절차를 Evidence로 남긴다.

---

# 📌 Scope

## In Scope

- Rolling Update
- Control Plane 1대 장애
- PDB
- TopologySpreadConstraint
- 장애·복구·E2E 검증

## Out of Scope

- 다중 Control Plane 동시 장애
- 다중 Site DR
- Production SLA 보증

---

# 📋 핵심 요구사항

- [ ] 실행 전 정상 Baseline을 기록한다.
- [ ] 업무 서비스 가용성 기준을 사전 정의한다.
- [ ] 장애 주입과 복구 순서를 Runbook으로 작성한다.
- [ ] 미완료 항목은 Known Issue에 Owner 이하영과 Due를 기록한다.

---

# ✅ Acceptance Criteria

- [ ] Rolling Update 중 승인 서비스 기준을 충족한다.
- [ ] Control Plane 1대 중단 후 API와 Workload 상태가 기대와 일치한다.
- [ ] PDB/TopologySpreadConstraint가 배포·Drain 시 기대대로 작동한다.
- [ ] 복구 후 E2E가 통과한다.

---

# 🧪 검증 및 증적

- Node/Pod 상태 전후 비교
- Update/Failure/Recovery Log
- PDB/TopologySpread Manifest
- E2E 결과
- Evidence Path: docs/evidence/P1-HA-02/

---

# 🔗 Dependency

- **Blocked By:** P1-K8S-01; P1-E2E-01 Initial
- **Blocks / Next:** P1-DOC-01 또는 Known Issue 이관
- **Related Ticket:** P1-HA-01
- **Milestone:** Phase 1 P1 / Close Tracking

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D02; D25
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-03; RISK-05; RISK-07; RISK-14
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** Rolling Update, Control Plane 1대 장애, PDB 및 TopologySpreadConstraint 검증 결과와 복구 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>
