<!-- fds-canonical-description:v3.1.18 record-id:DEC-P2-OP-01 -->
# DEC-P2-OP-01 — Operator Supply Chain Scope Decision

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-P2-OP-01 |
| Phase | Phase 2 |
| Category | Architecture / Operator Supply Chain |
| Type | Decision |
| Status | To Do |
| Priority | P1 |
| Start | 2026-10-12 |
| End | 2026-10-16 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | ROSA Operator 공급망을 Direct Catalog 또는 oc-mirror/Harbor/Custom CatalogSource 중 하나로 결정하고 구현·N/A 기준 승인 |
| Related Decision IDs | D22; D26 |
| Related Risk IDs | RISK-06; RISK-11; RISK-15 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #41 snapshot 2026-09-09T12:08:39Z |
| Schedule Note | D26에서 Direct Catalog 선택 시 P2-OP-01은 Cancelled 처리하고, Mirror 선택 시 P2-OP-01을 활성화한다. |

## 현재 실행·검토 상태

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #41](https://github.com/321Team/fds-project-baseline/issues/41), Issue 갱신 시각 `2026-09-09T12:08:39Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

OpenShift 담당자 이하영으로서 ROSA Operator 공급망 방식을 결정한다. 이를 통해 불필요한 Mirror 구현을 피하면서도 필요한 경우 재현 가능한 CatalogSource 경로를 확보한다.

---

# Scope

## In Scope

- Direct OperatorHub
- oc-mirror/Harbor
- Custom CatalogSource
- 권한·비용·네트워크
- 적용 또는 N/A 기준

## Out of Scope

- 결정 전 Mirror 구축
- 승인되지 않은 CatalogSource

---

# 핵심 요구사항

- [ ] ROSA 네트워크 접근성과 Catalog 사용 가능성을 확인한다.
- [ ] Mirror 적용 시 Harbor 용량·TLS·Credential을 검토한다.
- [ ] 직접 사용 시 P2-OP-01 Cancelled 근거를 기록한다.
- [ ] 결정은 D26에 남긴다.

---

# Acceptance Criteria

- [ ] Direct 또는 Mirror 방식이 하나로 결정된다.
- [ ] Owner·Due·구현 또는 N/A 기준이 승인된다.
- [ ] P2-OP-01 상태 전환 조건이 명확하다.

---

# 검증 및 증적

- Decision D26
- ROSA Catalog/권한 확인
- 비용·경로 비교
- N/A 또는 구현 계획
- Evidence Path: docs/evidence/DEC-P2-OP-01/

---

# Dependency

- **Blocked By:** P2-ROSA-01 선행정보
- **Blocks / Next:** P2-OP-01
- **Related Ticket:** DEC-P2-REG-01
- **Milestone:** G5 / Phase 2 P1

---

# Decision / Risk Control

- **Related Decision IDs:** D22; D26
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-06; RISK-11; RISK-15
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** ROSA Operator 공급망을 Direct Catalog 또는 oc-mirror/Harbor/Custom CatalogSource 중 하나로 결정하고 구현·N/A 기준 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
