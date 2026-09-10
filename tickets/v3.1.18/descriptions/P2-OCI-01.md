<!-- fds-canonical-description:v3.1.18 record-id:P2-OCI-01 -->
# P2-OCI-01 — OCI Relay Go / No-Go

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-OCI-01 |
| Phase | Phase 2 |
| Category | Milestone / Hybrid Network |
| Type | Decision |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-28 |
| End | 2026-10-02 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | OCI Relay 가능성·권한·Public Endpoint·IPsec/NAT-T·Route를 검증하고 Primary 또는 승인 Fallback 경로를 선택 |
| Related Decision IDs | D10; D21 |
| Related Risk IDs | RISK-10; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #36 snapshot 2026-09-09T12:07:26Z |
| Schedule Note | 10-02 Go/No-Go를 넘기지 않는다. No-Go 시 Vendor Endpoint→AWS EC2+EIP Relay→Overlay 순으로 승인된 Fallback을 선택한다. |

## 현재 실행·검토 상태

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #36](https://github.com/321Team/fds-project-baseline/issues/36), Issue 갱신 시각 `2026-09-09T12:07:26Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Hybrid Network 담당자로서 OCI Relay를 Primary Transit으로 사용할 수 있는지 조기에 판정한다. 이를 통해 실패 가능성이 큰 경로를 G4 직전까지 끌고 가지 않고 대체경로를 통제한다.

---

# Scope

## In Scope

- OCI 권한/Endpoint
- IPsec/NAT-T
- Route
- AWS VPN 연계 가능성
- Fallback 비교
- Go/No-Go 승인

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] 필요 계정·권한·Quota를 확인한다.
- [ ] Public Endpoint와 NAT 조건을 검증한다.
- [ ] On-Prem/AWS CIDR 중복을 확인한다.
- [ ] Fallback별 비용·일정·보안 영향을 기록한다.

---

# Acceptance Criteria

- [ ] OCI Primary의 실행 가능 여부가 증적으로 판정된다.
- [ ] Go 또는 단일 Fallback이 승인된다.
- [ ] P2-VPN-01과 P2-IAC-01 입력값이 확정된다.
- [ ] 미결 전제와 Owner/Due가 0건이다.

---

# 검증 및 증적

- OCI/AWS 권한·리소스 확인
- Endpoint/Route Test
- Fallback 비교표
- Decision D21
- 갱신 Architecture/WBS
- Evidence Path: `docs/evidence/P2-OCI-01/`

---

# Dependency

- **Blocked By:** MS-P1-CLOSE-01
- **Blocks / Next:** P2-VPN-01
- **Related Ticket:** P2-IAC-01
- **Milestone:** OCI Go/No-Go — 2026-10-02

---

# Decision / Risk Control

- **Related Decision IDs:** D10; D21
- **Decision Control:** D21 결과로 Primary/Fallback과 비용·일정 영향도를 승인한다.
- **Related Risk IDs:** RISK-10; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** OCI Relay 가능성·권한·Public Endpoint·IPsec/NAT-T·Route를 검증하고 Primary 또는 승인 Fallback 경로를 선택
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
