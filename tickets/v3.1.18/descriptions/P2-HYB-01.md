<!-- fds-canonical-description:v3.1.18 record-id:P2-HYB-01 -->
# P2-HYB-01 — Hybrid DB / Registry Integration

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-HYB-01 |
| Phase | Phase 2 |
| Category | Hybrid Integration |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-16 |
| End | 2026-10-22 |
| Calendar Days | 7 |
| Working Days | 5 |
| Lead | 이재환 |
| Support | 이권욱, 이하영 |
| Exit Criteria | ROSA→On-Prem db01 .55:5432와 승인 Registry 경로의 Route·Security·Source·Application 통합 검증 PASS |
| Related Decision IDs | D21; D22; D23 |
| Related Risk IDs | RISK-09; RISK-10; RISK-11; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #47 snapshot 2026-09-10T02:09:59Z |
| Schedule Note | Harbor는 D22에 따라 사용 또는 Cancelled 처리한다. Hybrid DNS는 D23에 따라 적용 또는 IP Endpoint로 검증한다. |

## 현재 실행·검토 상태

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #47](https://github.com/321Team/fds-project-baseline/issues/47), Issue 갱신 시각 `2026-09-10T02:09:59Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

통합 담당자로서 ROSA 애플리케이션과 On-Prem 데이터 서비스를 승인된 Hybrid 경로로 연결한다. 이를 통해 Cloud 애플리케이션이 실제 On-Prem FDS 데이터 흐름을 완성한다.

---

# Scope

## In Scope

- ROSA→DB 5432
- 승인 Registry 443
- Route/Security
- Source 확인
- Application Integration
- Failure Isolation

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] DB는 승인된 ROSA Source만 허용한다.
- [ ] Client 또는 fds-engine의 직접 DB 접근을 허용하지 않는다.
- [ ] Registry 경로는 D22를 따른다.
- [ ] DNS 경로는 D23을 따른다.
- [ ] 단계별 TCP와 App Test를 분리한다.

---

# Acceptance Criteria

- [ ] ROSA에서 DB 5432 승인 연결이 성공한다.
- [ ] Transaction/FDS Result 저장·조회가 성공한다.
- [ ] 미승인 Source가 차단된다.
- [ ] Registry 사용 시 Pull이 성공하고 미사용 시 Cancelled 결정 근거가 있다.

---

# 검증 및 증적

- Route/Security Tables
- TCP/Source Test
- DB Connection/Query
- Registry Pull 또는 N/A
- Application Integration Log
- Evidence Path: `docs/evidence/P2-HYB-01/`

---

# Dependency

- **Blocked By:** P2-VPN-01, P2-APP-01, DEC-P2-REG-01, DEC-P2-DNS-01
- **Blocks / Next:** P2-E2E-01
- **Related Ticket:** P2-OADP-01
- **Milestone:** G6 Hybrid Integration Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D21; D22; D23
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-09; RISK-10; RISK-11; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** ROSA→On-Prem db01 .55:5432와 승인 Registry 경로의 Route·Security·Source·Application 통합 검증 PASS
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
