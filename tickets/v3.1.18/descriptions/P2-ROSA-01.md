<!-- fds-canonical-description:v3.1.18 record-id:P2-ROSA-01 -->
# P2-ROSA-01 — ROSA Platform / Security

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-ROSA-01 |
| Phase | Phase 2 |
| Category | OpenShift / ROSA |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-06 |
| End | 2026-10-16 |
| Calendar Days | 11 |
| Working Days | 8 |
| Lead | 이하영 |
| Support | 이권욱 |
| Exit Criteria | ROSA Cluster Ready, Namespace/RBAC/NetworkPolicy/SecurityContext, Hybrid Route 및 Application 배포 선행조건과 G5 Evidence 확보 |
| Related Decision IDs | D10; D12; D17; D21 |
| Related Risk IDs | RISK-07; RISK-10; RISK-11; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #38 snapshot 2026-09-10T02:09:51Z |
| Schedule Note | 10-09는 비근무일이다. 계정·Quota·리전 전제는 G4 이전에 확인하고 Cluster 범위를 최소화한다. |

## 현재 실행·검토 상태

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #38](https://github.com/321Team/fds-project-baseline/issues/38), Issue 갱신 시각 `2026-09-10T02:09:51Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

OpenShift 담당자로서 Phase 1 보안통제를 ROSA에 적용할 실행 플랫폼을 구축한다. 이를 통해 동일 MSA를 Cloud에서 운영하고 Hybrid E2E를 수행한다.

---

# Scope

## In Scope

- ROSA Cluster
- Namespace/Project
- RBAC
- NetworkPolicy
- SecurityContext
- Hybrid Route
- Access

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] 지원 Region/Version/Quota를 확인한다.
- [ ] Cluster Admin 접근을 최소화한다.
- [ ] Business Workload Namespace와 System 구성의 예외를 분리한다.
- [ ] On-Prem CIDR Route와 Egress 정책을 반영한다.
- [ ] 비용·삭제·복구 절차를 기록한다.

---

# Acceptance Criteria

- [ ] ROSA Cluster와 Worker가 Ready다.
- [ ] 관리·배포 접근이 승인된 계정으로 성공한다.
- [ ] 기본 보안정책이 적용된다.
- [ ] On-Prem 승인 경로의 선행 TCP Test가 성공한다.

---

# 검증 및 증적

- ROSA Cluster Inventory
- Access/RBAC
- Namespace/NetworkPolicy
- Worker/Operator 상태
- Hybrid Route Test
- Evidence Path: `docs/evidence/P2-ROSA-01/`

---

# Dependency

- **Blocked By:** P2-IAC-01, P2-VPN-01
- **Blocks / Next:** P2-APP-01, P2-OADP-01
- **Related Ticket:** DEC-P2-REG-01, DEC-P2-DNS-01
- **Milestone:** G5 ROSA Application Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D10; D12; D17; D21
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-07; RISK-10; RISK-11; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** ROSA Cluster Ready, Namespace/RBAC/NetworkPolicy/SecurityContext, Hybrid Route 및 Application 배포 선행조건과 G5 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
