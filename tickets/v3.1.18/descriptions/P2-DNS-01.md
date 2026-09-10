<!-- fds-canonical-description:v3.1.18 record-id:P2-DNS-01 -->
# P2-DNS-01 — Hybrid DNS Implementation Conditional

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-DNS-01 |
| Phase | Phase 2 |
| Category | DNS / Hybrid Integration |
| Type | Task |
| Status | To Do |
| Priority | P1 |
| Start | 2026-10-19 |
| End | 2026-10-20 |
| Calendar Days | 2 |
| Working Days | 2 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | D23이 Hybrid DNS를 선택한 경우 Resolver/Conditional Forwarding/Route/Query Test PASS; IP Endpoint 유지 시 Cancelled 결정 근거 승인 |
| Related Decision IDs | D11; D23 |
| Related Risk IDs | RISK-10; RISK-12; RISK-15 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #48 snapshot 2026-09-10T02:10:01Z |
| Schedule Note | DEC-P2-DNS-01 / D23 결정 결과가 미구현이면 Status=Cancelled와 결정 근거를 기록한다. 구현 시 Hybrid E2E IP Endpoint에 대한 영향을 검증한다. |

## 현재 실행·검토 상태

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #48](https://github.com/321Team/fds-project-baseline/issues/48), Issue 갱신 시각 `2026-09-10T02:10:01Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Hybrid DNS 담당자 이권욱으로서 D23이 Hybrid DNS 적용을 선택한 경우 Resolver와 Conditional Forwarding을 구현한다. IP Endpoint 유지가 선택되면 구현하지 않고 Cancelled 결정 근거를 승인받는다.

---

# Scope

## In Scope

- Resolver/Forwarding
- Zone/Query 경로
- Route/Security
- Positive/Negative Query
- 조건부 N/A

## Out of Scope

- D23 승인 전 구현
- P0 Hybrid E2E의 DNS 강제 의존
- DNSSEC

---

# 핵심 요구사항

- [ ] On-Prem과 ROSA의 권위 Zone을 정의한다.
- [ ] 필수 Query Source만 허용한다.
- [ ] Route와 UDP/TCP 53을 검증한다.
- [ ] IP Endpoint 선택으로 구현을 취소하면 Status=Cancelled와 결정 근거를 기록한다.

---

# Acceptance Criteria

- [ ] Hybrid DNS 선택 시 양방향 승인 Query가 성공한다.
- [ ] 미승인 Query가 차단된다.
- [ ] 장애 시 IP Endpoint 또는 승인 Fallback이 동작한다.
- [ ] IP Endpoint 선택 시 Cancelled 결정 근거가 승인된다.

---

# 검증 및 증적

- Resolver/Forward Rule
- Route/Security
- dig/nslookup 결과
- N/A Decision
- Evidence Path: docs/evidence/P2-DNS-01/

---

# Dependency

- **Blocked By:** DEC-P2-DNS-01 / D23; P2-VPN-01
- **Blocks / Next:** 선택 시 P2-HYB-01
- **Related Ticket:** P1-DNS-01
- **Milestone:** Phase 2 P1 / G6 Non-blocker

---

# Decision / Risk Control

- **Related Decision IDs:** D11; D23
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-10; RISK-12; RISK-15
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** D23이 Hybrid DNS를 선택한 경우 Resolver/Conditional Forwarding/Route/Query Test PASS; IP Endpoint 유지 시 Cancelled 결정 근거 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
