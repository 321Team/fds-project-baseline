<!-- fds-canonical-description:v3.1.18 record-id:P2-APP-01 -->
# P2-APP-01 — ROSA Application Deployment

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-APP-01 |
| Phase | Phase 2 |
| Category | Application / OpenShift |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-12 |
| End | 2026-10-16 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이재환 |
| Support | 이하영 |
| Exit Criteria | Phase 1과 동일한 transaction-api/fds-engine Image/Contract를 ROSA에 배포하고 Route/Health/Rule 기본검증 PASS |
| Related Decision IDs | D03; D22 |
| Related Risk IDs | RISK-06; RISK-07; RISK-11 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #43 snapshot 2026-09-10T02:09:53Z |
| Schedule Note | Image Source는 D22 결정에 따르며 Harbor 사용을 사전 가정하지 않는다. Manifest/Image 계약은 P2-CICD-01의 Runner 기반 ROSA Delivery에 연결한다. |

## 현재 실행·검토 상태

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #43](https://github.com/321Team/fds-project-baseline/issues/43), Issue 갱신 시각 `2026-09-10T02:09:53Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

애플리케이션 담당자로서 검증된 Phase 1 MSA를 ROSA에 동일 계약으로 배포한다. 이를 통해 플랫폼 차이를 최소화하고 Hybrid 데이터 경로 검증에 집중한다.

---

# Scope

## In Scope

- transaction-api/fds-engine
- OpenShift Route/Service
- Config/Secret
- Health
- Rule Smoke Test

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] Phase 1 OpenAPI와 Rule 계약을 유지한다.
- [ ] 환경별 Config/Secret을 분리한다.
- [ ] Image Digest/Tag를 추적한다.
- [ ] OpenShift Security 제약을 충족한다.
- [ ] DB 연결 전 Health/Rule Smoke Test를 분리한다.

---

# Acceptance Criteria

- [ ] 두 서비스가 ROSA에서 Ready다.
- [ ] Route를 통한 transaction-api Health가 성공한다.
- [ ] fds-engine이 외부에 직접 노출되지 않는다.
- [ ] 4개 Rule Smoke Test가 통과한다.

---

# 검증 및 증적

- Deployment/Route/Service
- Image Digest
- Health/Rule Test
- Config/Secret Mapping
- Pod Security 상태
- Evidence Path: `docs/evidence/P2-APP-01/`

---

# Dependency

- **Blocked By:** P2-ROSA-01, DEC-P2-REG-01
- **Blocks / Next:** P2-CICD-01, P2-HYB-01
- **Related Ticket:** P1-APP-01, P2-CICD-01
- **Milestone:** G5 ROSA Application Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D03; D22
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-06; RISK-07; RISK-11
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** Phase 1과 동일한 transaction-api/fds-engine Image/Contract를 ROSA에 배포하고 Route/Health/Rule 기본검증 PASS
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
