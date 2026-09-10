<!-- fds-canonical-description:v3.1.18 record-id:DEC-P2-DNS-01 -->
# DEC-P2-DNS-01 — Hybrid DNS Scope Decision

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-P2-DNS-01 |
| Phase | Phase 2 |
| Category | Architecture / DNS |
| Type | Decision |
| Status | To Do |
| Priority | P1 |
| Start | 2026-10-12 |
| End | 2026-10-16 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | P0 IP Endpoint 유지 또는 Hybrid DNS P1 적용을 확정하고 Resolver/Forwarding/Zone/Route/테스트·Cancelled 결정 근거를 승인 |
| Related Decision IDs | D11; D23 |
| Related Risk IDs | RISK-10; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #40 snapshot 2026-09-09T12:08:24Z |
| Schedule Note | Hybrid P0 E2E는 IP Endpoint를 허용하므로 본 P1 결정 미완료가 G5/G6를 자동 차단하지 않는다. |

## 현재 실행·검토 상태

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #40](https://github.com/321Team/fds-project-baseline/issues/40), Issue 갱신 시각 `2026-09-09T12:08:24Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Hybrid Network 담당자로서 Phase 2에서 Hybrid DNS를 적용할지 결정한다. 이를 통해 P1 기능이 P0 Hybrid E2E 일정을 불필요하게 차단하지 않도록 한다.

---

# Scope

## In Scope

- IP Endpoint 유지안
- Hybrid DNS 적용안
- Conditional Forwarding
- Route/ACL
- Test/N/A 기준

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] P0 DB `.55`와 필요 시 Harbor `.54` IP Endpoint를 보장한다.
- [ ] 적용안은 Resolver와 Zone 권위를 명시한다.
- [ ] 미적용 시 P1 Backlog Owner/Due를 기록한다.
- [ ] Reverse/PTR을 자동 포함하지 않는다.

---

# Acceptance Criteria

- [ ] P0/P1 범위가 단일안으로 승인된다.
- [ ] 적용 시 Query Path와 Test가 정의된다.
- [ ] 미적용 시 N/A/Deferred 근거가 기록된다.

---

# 검증 및 증적

- Decision 비교표
- DNS/Route 영향도
- Decision D23
- 갱신 Interface/WBS
- Evidence Path: `docs/evidence/DEC-P2-DNS-01/`

---

# Dependency

- **Blocked By:** P2-VPN-01 Route 설계
- **Blocks / Next:** P2-HYB-01
- **Related Ticket:** P1-DNS-01
- **Milestone:** G5 / G6 Non-blocking Decision

---

# Decision / Risk Control

- **Related Decision IDs:** D11; D23
- **Decision Control:** D23 결과는 P0 E2E 차단 여부와 후속 P1 Due를 함께 기록한다.
- **Related Risk IDs:** RISK-10; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** P0 IP Endpoint 유지 또는 Hybrid DNS P1 적용을 확정하고 Resolver/Forwarding/Zone/Route/테스트·Cancelled 결정 근거를 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
