<!-- fds-canonical-description:v3.1.18 record-id:DEC-CAL-P1-01 -->
# DEC-CAL-P1-01 — Phase 1 Weekend Review Decision

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-CAL-P1-01 |
| Phase | Phase 1 |
| Category | Schedule / Governance |
| Type | Decision |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-11 |
| End | 2026-09-11 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | 09-20 일요일 Review 유지 또는 영업일 재배치, 참석자·승인권자·시간·대체일을 확정하고 WBS/Calendar 동기화 |
| Related Decision IDs | D20 |
| Related Risk IDs | RISK-05; RISK-13 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #28 snapshot 2026-09-09T12:04:41Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | 교육장 주말 작업 불가를 반영해 Review 09-22 오후를 권장한다. 참석자·승인자는 아직 확정하지 않으며 To Do를 유지한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

## 현재 실행·검토 상태

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다. 현재 후보 Plan: 2026-09-11 ~ 2026-09-11 (권장안; 실제 완료일·Gate 승인은 미확정).

근거: [Issue #28](https://github.com/321Team/fds-project-baseline/issues/28), Issue 갱신 시각 `2026-09-09T12:04:41Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 일정 권장안

주말 교육장 사용 불가에 따라 기존 요구사항의 주말 유지 선택지는 사용하지 않는다. 평일 재배치 옵션으로 참석자·시간·승인권자를 확정하며 실제 Review는 선행 Gate 통과 후 진행한다.

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

PMO 담당자로서 주말로 계획된 Phase 1 Review의 실제 실행 가능성을 확정한다. 이를 통해 참석자 부재로 승인과 Close가 지연되는 것을 방지한다.

---

# Scope

## In Scope

- 주말 유지 여부
- 대체 영업일
- 참석자/승인권자
- 회의시간/접속방식
- WBS 갱신

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] 필수 참석자의 가능시간을 확인한다.
- [ ] 유지 시 근무·승인 절차를 확인한다.
- [ ] 변경 시 G3와 Close 영향도를 검토한다.
- [ ] 결정 결과를 Milestone과 Calendar에 반영한다.

---

# Acceptance Criteria

- [ ] 단일 Review 날짜와 시간이 승인된다.
- [ ] 필수 참석자·승인권자가 확정된다.
- [ ] P1-REV-01/MS-P1-REVIEW-01 일정이 동일하다.

---

# 검증 및 증적

- Decision D20
- 참석 확인
- 갱신 Calendar/WBS
- Review Invite 또는 회의 계획
- Evidence Path: `docs/evidence/DEC-CAL-P1-01/`

---

# Dependency

- **Blocked By:** G3 준비도 확인
- **Blocks / Next:** MS-P1-REVIEW-01, P1-REV-01
- **Related Ticket:** P1-DOC-01
- **Milestone:** Phase 1 Review

---

# Decision / Risk Control

- **Related Decision IDs:** D20
- **Decision Control:** D20은 주말 일정 리스크의 승인 또는 재배치 결과를 기록한다.
- **Related Risk IDs:** RISK-05; RISK-13
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** 09-20 일요일 Review 유지 또는 영업일 재배치, 참석자·승인권자·시간·대체일을 확정하고 WBS/Calendar 동기화
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
