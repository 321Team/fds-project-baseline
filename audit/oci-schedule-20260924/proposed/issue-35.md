<!-- fds-oci-schedule:20260924:v1:start -->
## OCI 연계 일정 정합화 — 2026-09-24 KST

사용자 “일정 불일치부터 해소” 지시에 따라 일정 표시와 기간 계산을 정정했다. [2026-09-22 재계획](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5779875658) 및 발행 docs-v3.1.20 WBS의 비근무일을 근거로 한다. 기존 10-06~10-09의 작업 가능일은 10-06·07·08의 3일이므로 **OCI 종료/D21 목표를 10-08로 통일**한다.

- **이 티켓의 계획:** 2026-10-06 ~ 2026-10-13 · 달력 8일 / 작업 5일. 10-06~10-13 계획. D21 목표는 10-08이며 Transit 의존 입력과 경로는 D21 결정 후 확정한다.
- **연계 목표:** Phase 2 착수/설계 10-06, D21 10-08, IaC 10-06~13, VPN 준비 10-08~13, G4 10-13. VPN 적용은 기존 선행조건 충족 후이며, IaC 완료 목표와 G4가 같은 날이므로 실제 적용·검증 작업창 확보를 확인해야 한다.
- 아래 이전 정본 머리말·마일스톤 배정·보관 원문의 과거 일정은 이력이다. 현행 계획 일정은 이 정정과 갱신한 티켓 속성표를 따른다. [정정 근거 및 차기 정본 반영안](https://github.com/321Team/fds-project-baseline/blob/docs/oci-schedule-align-20260924/audit/oci-schedule-20260924/README.md).
- 계획 정정이며 OCI 도입 승인, D21 판정 완료, G4 통과를 뜻하지 않는다. 발행 정본 편입은 별도이며 상태·AC·담당·기존 선행조건은 유지한다.
- 동기화 잔여: #36의 별도 Target date는 10-09→10-08, GitHub Milestone #7 기한/현행 설명은 09-28→10-06, #8은 10-08→10-13 갱신이 필요하다. 현재 연결은 해당 필드 쓰기를 제공하지 않아 본문 갱신과 구분해 추적한다.
<!-- fds-oci-schedule:20260924:v1:end -->

---

<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P2-IAC-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P2-IAC-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 계획 단계. AWS 10.20.0.0/16 유지. State/권한/버전·승인 Plan·비용/복구 기록은 Apply 전에 확정.

**인계·관련 티켓:** [#34](https://github.com/321Team/fds-project-baseline/issues/34) · [#36](https://github.com/321Team/fds-project-baseline/issues/36) · [#37](https://github.com/321Team/fds-project-baseline/issues/37).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P2-IAC-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P2-IAC-01 -->
# P2-IAC-01 — AWS / ROSA Terraform IaC

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-IAC-01 |
| Phase | Phase 2 |
| Category | Cloud / Terraform |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-06 |
| End | 2026-10-13 |
| Calendar Days | 8 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | AWS VPC 10.20.0.0/16, ROSA 선행 인프라와 IAM/OIDC 최소권한의 Terraform fmt/validate/plan/apply, State·Secret 통제 및 G4 Evidence 확보 |
| Related Decision IDs | D10; D21; D25 |
| Related Risk IDs | RISK-10; RISK-11; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #35 snapshot 2026-09-10T02:09:47Z; 일정: docs-v3.1.20 WBS + 2026-09-22 재계획 + 2026-09-24 일정 정합화 |
| Schedule Note | 10-06~10-13 계획. D21 목표는 10-08이며 Transit 의존 입력과 경로는 D21 결정 후 확정한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T02:09:47Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #35](https://github.com/321Team/fds-project-baseline/issues/35), Issue 갱신 시각 `2026-09-10T02:09:47Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Cloud IaC 담당자로서 AWS/ROSA 선행 인프라를 Terraform으로 재현 가능하게 구축한다. 이를 통해 수동 Drift를 줄이고 Plan과 실제 리소스의 추적성을 확보한다.

---

# Scope

## In Scope

- AWS VPC/Subnet/Route/Security
- ROSA Prerequisite
- IAM/OIDC 및 최소권한 Role
- Terraform State
- Variables/Outputs
- Plan/Apply Evidence

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] AWS VPC는 `10.20.0.0/16`을 사용한다.
- [ ] Secret을 tfvars/Source/Output에 평문 노출하지 않는다.
- [ ] IAM/OIDC Trust와 최소권한 Policy를 Source로 관리한다.
- [ ] Remote State 또는 승인된 State 통제를 적용한다.
- [ ] Plan을 검토 후 Apply한다.
- [ ] Destroy/Recovery 전제와 비용 리소스를 기록한다.

---

# Acceptance Criteria

- [ ] fmt/validate가 통과한다.
- [ ] 승인 Plan과 Apply 결과가 일치한다.
- [ ] 필수 Route/Security/Output과 IAM/OIDC가 생성된다.
- [ ] State와 Secret 접근이 통제된다.
- [ ] 재실행 시 비의도 변경이 없다.

---

# 검증 및 증적

- Terraform Source/Version
- fmt/validate/plan
- Apply/Output
- AWS Resource Inventory
- State/Secret Control
- Evidence Path: `321Team/fds-project-evidence:evidence/P2-IAC-01/`

---

# Dependency

- **Blocked By:** MS-P1-CLOSE-01
- **Blocks / Next:** P2-VPN-01, P2-ROSA-01
- **Related Ticket:** P2-OCI-01
- **Milestone:** G4 Cloud / VPN Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D10; D21
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-10; RISK-11; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** AWS VPC 10.20.0.0/16 및 ROSA 선행 인프라의 Terraform fmt/validate/plan/apply, State·Secret 통제와 G4 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `9cc1eb76ce9e15ce96e292c37d853167be22bd33d828294111030d372638aa17`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P2-IAC-01 -->
# P2-IAC-01 — AWS / ROSA Terraform IaC

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P2-IAC-01 |
| Phase | Phase 2 |
| Category | Cloud / Terraform |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-28 |
| End | 2026-10-08 |
| Calendar Days | 11 |
| Working Days | 8 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | AWS VPC 10.20.0.0/16, ROSA 선행 인프라와 IAM/OIDC 최소권한의 Terraform fmt/validate/plan/apply, State·Secret 통제 및 G4 Evidence 확보 |
| Related Decision IDs | D10; D21; D25 |
| Related Risk IDs | RISK-10; RISK-11; RISK-12 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Phase1_Logical_Architecture_v3.1.2; Phase 2 OCI/AWS/ROSA Design; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 10-05는 비근무일이다. OCI Go/No-Go 결과에 따라 VPN 입력과 경로를 갱신한다. |

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

Cloud IaC 담당자로서 AWS/ROSA 선행 인프라를 Terraform으로 재현 가능하게 구축한다. 이를 통해 수동 Drift를 줄이고 Plan과 실제 리소스의 추적성을 확보한다.

---

# 📌 Scope

## In Scope

- AWS VPC/Subnet/Route/Security
- ROSA Prerequisite
- IAM/OIDC 및 최소권한 Role
- Terraform State
- Variables/Outputs
- Plan/Apply Evidence

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 📋 핵심 요구사항

- [ ] AWS VPC는 `10.20.0.0/16`을 사용한다.
- [ ] Secret을 tfvars/Source/Output에 평문 노출하지 않는다.
- [ ] IAM/OIDC Trust와 최소권한 Policy를 Source로 관리한다.
- [ ] Remote State 또는 승인된 State 통제를 적용한다.
- [ ] Plan을 검토 후 Apply한다.
- [ ] Destroy/Recovery 전제와 비용 리소스를 기록한다.

---

# ✅ Acceptance Criteria

- [ ] fmt/validate가 통과한다.
- [ ] 승인 Plan과 Apply 결과가 일치한다.
- [ ] 필수 Route/Security/Output과 IAM/OIDC가 생성된다.
- [ ] State와 Secret 접근이 통제된다.
- [ ] 재실행 시 비의도 변경이 없다.

---

# 🧪 검증 및 증적

- Terraform Source/Version
- fmt/validate/plan
- Apply/Output
- AWS Resource Inventory
- State/Secret Control
- Evidence Path: `docs/evidence/P2-IAC-01/`

---

# 🔗 Dependency

- **Blocked By:** MS-P1-CLOSE-01
- **Blocks / Next:** P2-VPN-01, P2-ROSA-01
- **Related Ticket:** P2-OCI-01
- **Milestone:** G4 Cloud / VPN Ready

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D10; D21
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-10; RISK-11; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** AWS VPC 10.20.0.0/16 및 ROSA 선행 인프라의 Terraform fmt/validate/plan/apply, State·Secret 통제와 G4 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>


---
_Generated by [Claude Code](https://claude.ai/code)_