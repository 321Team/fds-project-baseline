# P2-DOC-01 — Cloud / Hybrid Deliverable Freeze

Version: v3.1.21 CANDIDATE
Source: https://github.com/321Team/fds-project-baseline/issues/49
Updated at: 2026-10-01T07:11:45Z
Source body SHA256: `8b3d1477867433fdc110a07c1db8b21c175361699bd8be334103766c215d410e`
GitHub: open / None
Current disposition: Source lifecycle/AC retained; no new acceptance by this publication.

| Property | Current source value |
|---|---|
| Record ID | P2-DOC-01 |
| Phase | Phase 2 |
| Category | PMO / Documentation |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-23 |
| End | 2026-10-23 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | Terraform/ROSA/VPN/Hybrid Architecture, CI/CD, Test/Evidence, Backup/Recovery Runbook, D22/D23/D26 Decision, Known Issue 및 Deliverable Freeze 승인 |
| Related Decision IDs | D12; D21; D22; D23; D24; D25; D26 |
| Related Risk IDs | RISK-10; RISK-11; RISK-12; RISK-13 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #49 snapshot 2026-09-10T02:10:03Z |
| Schedule Note | 구현 티켓은 실행 시점에 Evidence/Runbook/결정기록을 각자 누적한다. #49는 10-23에 #50/G6 완료 산출물을 최종 집계·무결성 대조하고 Deliverable Freeze 입력을 확정한다. |

## Source checklist

- [ ] Plan/Apply와 실제 리소스를 대조한다.
- [ ] Tunnel/Route/Security와 E2E Evidence를 연결한다.
- [ ] OCI/Fallback·Registry·DNS Decision을 반영한다.
- [ ] 비용·삭제·복구 전제를 기록한다.
- [ ] 실제 금융 규제 준수 완료 표현을 금지한다.
- [ ] Phase 2 P0 Ticket별 Evidence 링크가 존재한다.
- [ ] As-built와 Baseline 차이가 승인된다.
- [ ] IaC/Runbook으로 핵심 환경을 재현할 수 있다.
- [ ] Critical 문서 결함이 0건이다.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

<!-- issue-execution-contract-20261001:v1:start -->
## 2026-10-01 Deliverable Aggregation Contract v1

### Rolling rule
10-07~10-22의 문서/증적은 각 실행 티켓 DoD에서 즉시 생산한다. #49에 마지막날 문서 backlog를 누적하지 않는다.

### 10-23 Final aggregation
- Architecture/IaC/ROSA/VPN/App/CICD/Hybrid/E2E/Cost/Known Issue를 최신 Issue와 대조.
- `SHARED_OCP_LAB` vs `ROSA_RUNTIME` evidence를 분리.
- stale 링크, 미병합 evidence, source SHA 불일치, manifest/checksum 누락을 식별.

### Exit
#54가 Freeze 가능한 immutable candidate set과 잔여 Known Issue/Deferred 목록을 제공한다.
<!-- issue-execution-contract-20261001:v1:end -->

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
최종 산출물은 Evidence를 `SHARED_OCP_LAB`과 `ROSA_RUNTIME`으로 분리 표기하고, Lab 결과가 ROSA Acceptance로 오인되지 않는지 무결성 점검한다.



<!-- schedule-realign-20261001:issue-49:start -->
## 2026-10-01 일정·Dependency 정합화

- **Rolling documentation rule:** 10-07~10-22 문서화는 각 책임 티켓의 Definition of Done 일부로 누적한다. #49는 10-23 최종 aggregation/integrity/freeze 작업만 수행하며 앞선 실행을 기다리며 별도 문서 backlog를 쌓지 않는다.

- Scope/AC/Priority/Milestone/Review Authority 변경 없음.
- 일정 조정은 재현성·무결성·추적성을 유지하면서 P0 동시 WIP와 선행조건 역전을 제거하기 위한 PMO 조정이다.
<!-- schedule-realign-20261001:issue-49:end -->
<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P2-DOC-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P2-DOC-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 계획 단계. P2 설계·실제 설정·시험·비용/삭제·인계의 고정 참조와 배포 묶음 대응.

**인계·관련 티켓:** [#50](https://github.com/321Team/fds-project-baseline/issues/50) · [#53](https://github.com/321Team/fds-project-baseline/issues/53) · [#54](https://github.com/321Team/fds-project-baseline/issues/54).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P2-DOC-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P2-DOC-01 -->
# P2-DOC-01 — Cloud / Hybrid Deliverable Freeze

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-DOC-01 |
| Phase | Phase 2 |
| Category | PMO / Documentation |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-23 |
| End | 2026-10-23 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | Terraform/ROSA/VPN/Hybrid Architecture, CI/CD, Test/Evidence, Backup/Recovery Runbook, D22/D23/D26 Decision, Known Issue 및 Deliverable Freeze 승인 |
| Related Decision IDs | D12; D21; D22; D23; D24; D25; D26 |
| Related Risk IDs | RISK-10; RISK-11; RISK-12; RISK-13 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #49 snapshot 2026-09-10T02:10:03Z |
| Schedule Note | 구현 티켓은 실행 시점에 Evidence/Runbook/결정기록을 각자 누적한다. #49는 10-23에 #50/G6 완료 산출물을 최종 집계·무결성 대조하고 Deliverable Freeze 입력을 확정한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T02:10:03Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #49](https://github.com/321Team/fds-project-baseline/issues/49), Issue 갱신 시각 `2026-09-10T02:10:03Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

PMO 담당자로서 Phase 2 Cloud/Hybrid 구성과 검증을 재현 가능한 정본으로 동결한다. 이를 통해 Review와 Project Close가 IaC·Evidence·Decision에 기반하도록 한다.

---

# Scope

## In Scope

- As-built Hybrid Architecture
- Terraform Inventory
- Test/Evidence Index
- VPN/Backup Runbook
- Decision/Known Issue
- D26 Operator 공급망 결정과 P2-OP-01 Cancelled/구현 결과
- Version Trace

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] Plan/Apply와 실제 리소스를 대조한다.
- [ ] Tunnel/Route/Security와 E2E Evidence를 연결한다.
- [ ] OCI/Fallback·Registry·DNS Decision을 반영한다.
- [ ] 비용·삭제·복구 전제를 기록한다.
- [ ] 실제 금융 규제 준수 완료 표현을 금지한다.

---

# Acceptance Criteria

- [ ] Phase 2 P0 Ticket별 Evidence 링크가 존재한다.
- [ ] As-built와 Baseline 차이가 승인된다.
- [ ] IaC/Runbook으로 핵심 환경을 재현할 수 있다.
- [ ] Critical 문서 결함이 0건이다.

---

# 검증 및 증적

- Deliverable Index
- Terraform/ROSA Inventory
- Hybrid Test Report
- Runbook Review
- Decision/Known Issue
- D26 Operator 공급망 결정과 P2-OP-01 Cancelled/구현 결과 Register
- Evidence Path: `321Team/fds-project-evidence:evidence/P2-DOC-01/`

---

# Dependency

- **Blocked By:** P2-E2E-01
- **Blocks / Next:** P2-REV-01
- **Related Ticket:** 전체 Phase 2; P2-OADP-01은 P1 / 실행 시 결과 또는 Deferred/N/A를 산출물에 반영
- **Milestone:** Deliverable Freeze

---

# Decision / Risk Control

- **Related Decision IDs:** D12; D21; D22; D23; D24
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-10; RISK-11; RISK-12; RISK-13
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** Terraform/ROSA/VPN/Hybrid Architecture, Test/Evidence, Backup/Recovery Runbook, Decision/Known Issue 및 Deliverable Freeze 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `d835a47245541f063b4d449a22e9406b58e27cde76174cd745c8efdbd847e31b`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P2-DOC-01 -->
# P2-DOC-01 — Cloud / Hybrid Deliverable Freeze

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P2-DOC-01 |
| Phase | Phase 2 |
| Category | PMO / Documentation |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-19 |
| End | 2026-10-23 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | Terraform/ROSA/VPN/Hybrid Architecture, CI/CD, Test/Evidence, Backup/Recovery Runbook, D22/D23/D26 Decision, Known Issue 및 Deliverable Freeze 승인 |
| Related Decision IDs | D12; D21; D22; D23; D24; D25; D26 |
| Related Risk IDs | RISK-10; RISK-11; RISK-12; RISK-13 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Phase1_Logical_Architecture_v3.1.2; Phase 2 OCI/AWS/ROSA Design; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 10-23 Deliverable Freeze와 DEC-CAL-P2-01을 함께 완료한다. |

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

PMO 담당자로서 Phase 2 Cloud/Hybrid 구성과 검증을 재현 가능한 정본으로 동결한다. 이를 통해 Review와 Project Close가 IaC·Evidence·Decision에 기반하도록 한다.

---

# 📌 Scope

## In Scope

- As-built Hybrid Architecture
- Terraform Inventory
- Test/Evidence Index
- VPN/Backup Runbook
- Decision/Known Issue
- D26 Operator 공급망 결정과 P2-OP-01 Cancelled/구현 결과
- Version Trace

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 📋 핵심 요구사항

- [ ] Plan/Apply와 실제 리소스를 대조한다.
- [ ] Tunnel/Route/Security와 E2E Evidence를 연결한다.
- [ ] OCI/Fallback·Registry·DNS Decision을 반영한다.
- [ ] 비용·삭제·복구 전제를 기록한다.
- [ ] 실제 금융 규제 준수 완료 표현을 금지한다.

---

# ✅ Acceptance Criteria

- [ ] Phase 2 P0 Ticket별 Evidence 링크가 존재한다.
- [ ] As-built와 Baseline 차이가 승인된다.
- [ ] IaC/Runbook으로 핵심 환경을 재현할 수 있다.
- [ ] Critical 문서 결함이 0건이다.

---

# 🧪 검증 및 증적

- Deliverable Index
- Terraform/ROSA Inventory
- Hybrid Test Report
- Runbook Review
- Decision/Known Issue
- D26 Operator 공급망 결정과 P2-OP-01 Cancelled/구현 결과 Register
- Evidence Path: `docs/evidence/P2-DOC-01/`

---

# 🔗 Dependency

- **Blocked By:** P2-E2E-01, P2-OADP-01
- **Blocks / Next:** P2-REV-01
- **Related Ticket:** 전체 Phase 2
- **Milestone:** Deliverable Freeze

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D12; D21; D22; D23; D24
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-10; RISK-11; RISK-12; RISK-13
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** Terraform/ROSA/VPN/Hybrid Architecture, Test/Evidence, Backup/Recovery Runbook, Decision/Known Issue 및 Deliverable Freeze 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>

