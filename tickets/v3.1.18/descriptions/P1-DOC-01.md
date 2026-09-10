<!-- fds-canonical-description:v3.1.18 record-id:P1-DOC-01 -->
# P1-DOC-01 — Architecture / Test / Runbook Freeze

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-DOC-01 |
| Phase | Phase 1 |
| Category | PMO / Documentation |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-11 |
| End | 2026-09-22 |
| Calendar Days | 12 |
| Working Days | 8 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | As-built Architecture, Test/Evidence Index, 구축·운영·복구 Runbook, P1 미완료 Known Issue의 풀네임 Owner·Due, Version/Source 및 Review 재현성 승인 |
| Related Decision IDs | D12; D20; D25 |
| Related Risk IDs | RISK-05; RISK-13 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #24 snapshot 2026-09-10T02:09:36Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | 구축 시 증적·Runbook을 병행 축적하고 09-22 오전 Final Evidence와 함께 동결한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

## 현재 실행·검토 상태

이번 v3.1.18은 정본 후보의 누적 이력·설명·배포 정합성 통합 작업이다. 독립 리뷰·명시적 병합 승인·발행은 아직 없으며 P1-DOC 전체 문서 Freeze/Done을 의미하지 않는다. 정본 발행 뒤 Issue Description 최신화, 마지막에 속성 재계획을 수행한다. 현재 후보 Plan: 2026-09-11 ~ 2026-09-22 (권장안; 실제 완료일·Gate 승인은 미확정).

근거: [Issue #24](https://github.com/321Team/fds-project-baseline/issues/24), Issue 갱신 시각 `2026-09-10T02:09:36Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

PMO 담당자로서 Phase 1의 설계·구축·검증 정보를 재현 가능한 정본으로 동결한다. 이를 통해 Review가 개인 설명에 의존하지 않고 문서와 Evidence로 반복 가능하게 한다.

---

# Scope

## In Scope

- As-built Architecture
- Configuration Inventory
- Test/Evidence Index
- Runbook
- Known Issue
- Version Trace

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] 설계와 실제 IP/Port/배치를 대조한다.
- [ ] 각 P0 Exit Criteria를 Evidence와 연결한다.
- [ ] 복구와 Rollback 명령의 전제조건을 명시한다.
- [ ] 금융 규제 준수 완료 표현을 금지한다.

---

# Acceptance Criteria

- [ ] P0 Ticket별 Evidence 링크가 존재한다.
- [ ] As-built와 Baseline 차이가 Change/Known Issue로 기록된다.
- [ ] 제3자가 Runbook으로 핵심 검증을 재현할 수 있다.
- [ ] Critical 문서 결함이 0건이다.

---

# 검증 및 증적

- Deliverable Index
- As-built Diagram
- Test Report
- Runbook Review
- Known Issue Register
- Evidence Path: `docs/evidence/P1-DOC-01/`

---

# Dependency

- **Blocked By:** P1-HA-01, P1-DR-01, P1-E2E-01
- **Blocks / Next:** P1-REV-01
- **Related Ticket:** 전체 Phase 1
- **Milestone:** G3 Review Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D12; D20
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-05; RISK-13
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** As-built Architecture, Test/Evidence Index, 구축·운영·복구 Runbook, Known Issue, Version/Source 및 Review 재현성 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
