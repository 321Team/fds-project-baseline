<!-- fds-canonical-description:v3.1.18 record-id:P2-IAC-01 -->
# P2-IAC-01 — AWS / ROSA Terraform IaC

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
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
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #35 snapshot 2026-09-10T02:09:47Z |
| Schedule Note | 10-05는 비근무일이다. OCI Go/No-Go 결과에 따라 VPN 입력과 경로를 갱신한다. |

## 현재 실행·검토 상태

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #35](https://github.com/321Team/fds-project-baseline/issues/35), Issue 갱신 시각 `2026-09-10T02:09:47Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

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
- Evidence Path: `docs/evidence/P2-IAC-01/`

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
