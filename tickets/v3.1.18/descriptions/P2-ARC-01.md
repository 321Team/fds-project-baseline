<!-- fds-canonical-description:v3.1.18 record-id:P2-ARC-01 -->
# P2-ARC-01 — Hybrid / OCI / AWS / ROSA Architecture Freeze

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-ARC-01 |
| Phase | Phase 2 |
| Category | Architecture / Hybrid Cloud |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-28 |
| End | 2026-09-28 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | OCI Relay·AWS VPC/VPN·ROSA·On-Prem 연계 Architecture, Interface IF-17~IF-20, Security, Decision, Exit Criteria Freeze 승인 |
| Related Decision IDs | D10; D21; D22; D23; D25; D26 |
| Related Risk IDs | RISK-10; RISK-11; RISK-12; RISK-14; RISK-15 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #34 snapshot 2026-09-10T02:09:45Z |
| Schedule Note | MS-P2-START-01 직후 완료하며 Phase 2 모든 구현 티켓이 참조하는 Phase 2 OCI/AWS/ROSA Design의 권위 Source를 생성한다. |

## 현재 실행·검토 상태

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #34](https://github.com/321Team/fds-project-baseline/issues/34), Issue 갱신 시각 `2026-09-10T02:09:45Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Hybrid Architecture 담당자 이권욱으로서 OCI Relay, AWS VPN, ROSA 및 On-Prem 서비스의 설계 계약을 동결한다. 이를 통해 Phase 2 구현 티켓이 동일한 CIDR·Interface·Security·Fallback 기준을 사용하도록 한다.

---

# Scope

## In Scope

- Phase 2 Logical/Physical Architecture
- OCI/AWS/ROSA CIDR·배치
- IF-17~IF-20
- Security·Identity·Registry·DNS 결정
- Gate Exit Criteria

## Out of Scope

- 다중 DR Site
- 승인되지 않은 Transit
- Phase 1 동결 구성의 무단 변경

---

# 핵심 요구사항

- [ ] On-Prem/AWS CIDR 중복을 방지한다.
- [ ] Primary/Fallback 경로의 전환 조건을 명시한다.
- [ ] Producer/Consumer/Port/Owner/Acceptance를 동결한다.
- [ ] Phase 2 Ticket과 Source를 상호 연결한다.

---

# Acceptance Criteria

- [ ] Architecture와 Interface가 이권욱·이하영·이재환 검토 대상으로 배포된다.
- [ ] P2-OCI/IAC/VPN/ROSA/APP/CICD의 의존성이 연결된다.
- [ ] D21~D23·D26의 결정 시점과 조건부 범위가 명시된다.
- [ ] 변경 통제 기준이 승인된다.

---

# 검증 및 증적

- Phase 2 Architecture Source
- Interface Register
- Decision/Risk Mapping
- Review Record
- Evidence Path: docs/evidence/P2-ARC-01/

---

# Dependency

- **Blocked By:** MS-P1-CLOSE-01; MS-P2-START-01
- **Blocks / Next:** P2-OCI-01; P2-IAC-01; P2-VPN-01; P2-ROSA-01
- **Related Ticket:** P2-DOC-01
- **Milestone:** Phase 2 Start / G4

---

# Decision / Risk Control

- **Related Decision IDs:** D10; D21; D22; D23; D25; D26
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-10; RISK-11; RISK-12; RISK-14; RISK-15
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** OCI Relay·AWS VPC/VPN·ROSA·On-Prem 연계 Architecture, Interface IF-17~IF-20, Security, Decision, Exit Criteria Freeze 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
