<!-- fds-canonical-description:v3.1.18 record-id:DEC-P2-REG-01 -->
# DEC-P2-REG-01 — ROSA Image Registry Source Decision

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-P2-REG-01 |
| Phase | Phase 2 |
| Category | Architecture / Registry |
| Type | Decision |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-12 |
| End | 2026-10-16 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | ROSA Image Source를 On-Prem Harbor 또는 승인 Cloud Registry로 확정하고 Route·TLS·Credential·비용·Fallback을 승인 |
| Related Decision IDs | D22 |
| Related Risk IDs | RISK-06; RISK-10; RISK-11; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #42 snapshot 2026-09-09T12:08:53Z |
| Schedule Note | 기준선의 ROSA→Harbor는 Optional이다. P2-APP-01 최종 Image 경로 전 10-16까지 확정한다. |

## 현재 실행·검토 상태

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #42](https://github.com/321Team/fds-project-baseline/issues/42), Issue 갱신 시각 `2026-09-09T12:08:53Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Registry·OpenShift 담당자로서 ROSA가 사용할 이미지 원본을 확정한다. 이를 통해 불필요한 Hybrid Registry 의존성을 피하면서 Commit/Image 추적성을 유지한다.

---

# Scope

## In Scope

- Harbor vs Cloud Registry 비교
- Route/TLS
- Credential
- 비용
- Image Promotion
- Fallback

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] Phase 1 Image와 Digest 추적성을 유지한다.
- [ ] Private Credential을 Secret으로 관리한다.
- [ ] Hybrid 장애 시 배포 지속 가능성을 비교한다.
- [ ] 선택안의 보안·비용·일정 영향을 기록한다.

---

# Acceptance Criteria

- [ ] 단일 Image Source와 Fallback이 승인된다.
- [ ] Pull Route/TLS/Credential Test가 정의된다.
- [ ] P2-APP/HYB WBS와 Interface IF-19 상태가 갱신된다.

---

# 검증 및 증적

- Option 비교표
- Pull Connectivity Test
- Credential/TLS 계획
- Decision D22
- 갱신 WBS/Interface
- Evidence Path: `docs/evidence/DEC-P2-REG-01/`

---

# Dependency

- **Blocked By:** P2-ROSA-01 기본 Ready
- **Blocks / Next:** P2-APP-01, P2-HYB-01
- **Related Ticket:** P1-HBR-01
- **Milestone:** G5 ROSA Application Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D22
- **Decision Control:** D22에서 Harbor 사용 여부와 N/A 조건을 명확히 기록한다.
- **Related Risk IDs:** RISK-06; RISK-10; RISK-11; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** ROSA Image Source를 On-Prem Harbor 또는 승인 Cloud Registry로 확정하고 Route·TLS·Credential·비용·Fallback을 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
