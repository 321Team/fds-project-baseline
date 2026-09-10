<!-- fds-canonical-description:v3.1.18 record-id:P2-VPN-01 -->
# P2-VPN-01 — OCI Relay / AWS Site-to-Site VPN

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-VPN-01 |
| Phase | Phase 2 |
| Category | Hybrid Network / VPN |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-01 |
| End | 2026-10-08 |
| Calendar Days | 8 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | 승인 Transit 경로의 Tunnel UP, On-Prem↔VPC Route, UDP 500/4500/IPsec, Source·승인 TCP Path 및 장애 Evidence 확보 |
| Related Decision IDs | D10; D21 |
| Related Risk IDs | RISK-04; RISK-10; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #37 snapshot 2026-09-10T02:09:49Z |
| Schedule Note | 10-05는 비근무일이다. OCI No-Go 시 D21에서 승인된 Fallback만 사용한다. |

## 현재 실행·검토 상태

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #37](https://github.com/321Team/fds-project-baseline/issues/37), Issue 갱신 시각 `2026-09-10T02:09:49Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Hybrid Network 담당자로서 On-Prem과 AWS VPC 사이의 승인된 암호화 경로를 구축한다. 이를 통해 ROSA가 On-Prem DB와 필요한 서비스에 최소 포트로 접근한다.

---

# Scope

## In Scope

- vpn-gw01 `.51`
- OCI/Fallback Relay
- AWS S2S VPN
- Route
- Firewall
- Tunnel/Fail Test

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] On-Prem/VPC CIDR 중복을 방지한다.
- [ ] UDP 500/4500과 NAT-T 조건을 검증한다.
- [ ] 필수 목적지·포트만 허용한다.
- [ ] Route 전파와 Static Route의 권위 Source를 명시한다.
- [ ] Tunnel 재협상 절차를 기록한다.

---

# Acceptance Criteria

- [ ] 승인 Tunnel이 UP이다.
- [ ] On-Prem↔VPC 승인 TCP 경로가 성공한다.
- [ ] 미승인 경로가 차단된다.
- [ ] Tunnel 중단·복구가 Runbook대로 재현된다.

---

# 검증 및 증적

- Tunnel Status
- Route Tables
- Firewall/Security Group
- TCP/Source Test
- Failure/Recovery Log
- Evidence Path: `docs/evidence/P2-VPN-01/`

---

# Dependency

- **Blocked By:** P2-OCI-01, P2-IAC-01
- **Blocks / Next:** P2-ROSA-01, P2-HYB-01
- **Related Ticket:** P2-E2E-01
- **Milestone:** G4 Cloud / VPN Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D10; D21
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-04; RISK-10; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** 승인 Transit 경로의 Tunnel UP, On-Prem↔VPC Route, UDP 500/4500/IPsec, Source·승인 TCP Path 및 장애 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
