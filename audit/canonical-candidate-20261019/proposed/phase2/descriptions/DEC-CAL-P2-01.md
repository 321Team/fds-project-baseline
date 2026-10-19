<!-- fds-canonical-live:v3.1.21 record-id:DEC-CAL-P2-01:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/DEC-CAL-P2-01.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 해당 업무의 기존 AC·Exit Criteria와 실행/인수 구분을 유지한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:DEC-CAL-P2-01:end -->

<!-- issue-decision-contract-20261001:v1:start -->
## 2026-10-01 Calendar Decision Contract v1

### Decision
10-07 Phase 2 Start 시 10-23 Deliverable Freeze/Phase 2 Review, 10-26 Project Close를 고정한다.
과거 10-24 토요일 Review 선택지는 사용하지 않는다.

### Required record
- Review 날짜/시간
- 참석자/승인권자
- 10-23 순서(#49→#54→#56→#55 action intake)
- 10-24~25 Non-working
- 10-26 Close action/sign-off

### Change control
이후 변경은 명시적 Schedule Change 근거 없이 암묵적으로 이동하지 않는다.
<!-- issue-decision-contract-20261001:v1:end -->

<!-- shared-ocp-boundary-ref-20261001:issue-52:start -->
## 2026-10-01 공용 OCP 경계 상속

본 티켓은 Calendar/Governance Decision으로 OCP Runtime을 수행하지 않는다. Phase 2 일정 내 Lab 사용이 발생하면 #34의 Multi-tenant/Non-exclusive 경계와 Cleanup 원칙을 상속한다.

- Source of truth: #34 P2-ARC-01의 공용 OCP Multi-tenant 실행경계
- Scope/AC/Priority/Milestone/Review Authority 변경 없음.
<!-- shared-ocp-boundary-ref-20261001:issue-52:end -->



<!-- schedule-realign-20261001:issue-52:start -->
## 2026-10-01 일정·WIP 정합화

- **Early calendar freeze:** 10-07에 10-23 Deliverable Freeze/Phase 2 Review와 10-26 Project Close를 고정한다. 과거 10-24 토요일 Review 선택지는 사용하지 않으며, 이후 변경은 명시적 Schedule Change로만 처리한다.

- Scope/AC/Priority/Review Authority 변경 없음.
- P1 Decision은 P0 Gate를 자동 차단하지 않는다.
<!-- schedule-realign-20261001:issue-52:end -->
<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/DEC-CAL-P2-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/DEC-CAL-P2-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 계획 단계. 평일 Review 참석·시각·승인 근거. 주말 작업을 자동 배정하지 않음.

- Phase2 Review의 실제 참석자·시각·평일 작업창과 승인 기록은 후속 결정한다. 기존 계획안 날짜와 실제 개최/Close 일자를 구분한다.

**인계·관련 티켓:** [#55](https://github.com/321Team/fds-project-baseline/issues/55) · [#56](https://github.com/321Team/fds-project-baseline/issues/56).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:DEC-CAL-P2-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:DEC-CAL-P2-01 -->
# DEC-CAL-P2-01 — Phase 2 Weekend Review Decision

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-CAL-P2-01 |
| Phase | Phase 2 |
| Category | Schedule / Governance |
| Type | Decision |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-10-07 |
| End | 2026-10-07 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | 10-23 Deliverable Freeze/Phase 2 Review와 10-26 Project Close 일정, 참석자·승인권자·시간을 확정하고 WBS/Calendar에 동기화 |
| Related Decision IDs | D24 |
| Related Risk IDs | RISK-05; RISK-13 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #52 snapshot 2026-09-09T12:11:51Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | Phase 2 Start 시점에 10-23 Review/Freeze와 10-26 Project Close 일정을 고정한다. 10-22까지 Review 일정을 미결 상태로 남기지 않는다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-09T12:11:51Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다. 현재 후보 Plan: 2026-10-07 ~ 2026-10-07. 10-23 평일 Review/Freeze와 10-26 Project Close를 고정하는 일정 Decision이며, 실제 참석자·시각·승인 기록은 별도 확인 전 미확정이다.

근거: [Issue #52](https://github.com/321Team/fds-project-baseline/issues/52), Issue 갱신 시각 `2026-09-09T12:11:51Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 일정 권장안

주말 교육장 사용 불가에 따라 기존 요구사항의 주말 유지 선택지는 사용하지 않는다. 평일 재배치 옵션으로 참석자·시간·승인권자를 확정하며 실제 Review는 선행 Gate 통과 후 진행한다.

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

PMO 담당자로서 주말로 계획된 Phase 2 Review의 실행 가능성과 Project Close 영향을 확정한다. 이를 통해 승인 지연 없이 10-26 종결 여부를 판단한다.

---

# Scope

## In Scope

- 주말 유지 여부
- 대체 영업일
- 참석자/승인권자
- Project Close 영향
- WBS/Calendar 갱신

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] 필수 참석자의 가능시간을 확인한다.
- [ ] 유지 시 근무·승인 절차를 확인한다.
- [ ] 변경 시 Deliverable Freeze와 Close 영향도를 검토한다.
- [ ] 결정 결과를 관련 레코드에 반영한다.

---

# Acceptance Criteria

- [ ] 단일 Review 날짜와 시간이 승인된다.
- [ ] 필수 참석자·승인권자가 확정된다.
- [ ] P2-REV-01/MS-P2-REVIEW-01 일정이 동일하다.

---

# 검증 및 증적

- Decision D24
- 참석 확인
- 갱신 Calendar/WBS
- Review Invite 또는 회의 계획
- Evidence Path: `321Team/fds-project-evidence:evidence/DEC-CAL-P2-01/`

---

# Dependency

- **Blocked By:** MS-P2-START-01
- **Blocks / Next:** MS-P2-REVIEW-01, P2-REV-01
- **Related Ticket:** MS-PROJECT-CLOSE-01
- **Milestone:** Phase 2 Review

---

# Decision / Risk Control

- **Related Decision IDs:** D24
- **Decision Control:** D24는 주말 일정 승인 또는 대체 영업일을 기록한다.
- **Related Risk IDs:** RISK-05; RISK-13
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** 10-24 토요일 Review 유지 또는 영업일 재배치, 참석자·승인권자·시간·Project Close 영향도를 확정하고 WBS 동기화
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `80b6b248e86e83d0b582e76106dede0423f322af368112f654666d56e602f2b5`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:DEC-CAL-P2-01 -->
# DEC-CAL-P2-01 — Phase 2 Weekend Review Decision

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | DEC-CAL-P2-01 |
| Phase | Phase 2 |
| Category | Schedule / Governance |
| Type | Decision |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-22 |
| End | 2026-10-23 |
| Calendar Days | 2 |
| Working Days | 2 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | 10-24 토요일 Review 유지 또는 영업일 재배치, 참석자·승인권자·시간·Project Close 영향도를 확정하고 WBS 동기화 |
| Related Decision IDs | D24 |
| Related Risk IDs | RISK-05; RISK-13 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; 2026 Calendar; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 2026-10-24는 토요일이며 Working Days 0이다. Project Close 10-26 영향을 함께 검토한다. |

## 이관 기준 및 확인 사항

- 속성의 일정·담당·상태는 RELEASED v3.1.17 WBS(기준일 2026-09-04)를 우선 반영했다. 이후 별도 근거가 있는 변경만 아래에 명시한다.
- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`
- `FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx`

---

## Description — 보관 입력본

> 원본: `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

# 🎯 User Story

PMO 담당자로서 주말로 계획된 Phase 2 Review의 실행 가능성과 Project Close 영향을 확정한다. 이를 통해 승인 지연 없이 10-26 종결 여부를 판단한다.

---

# 📌 Scope

## In Scope

- 주말 유지 여부
- 대체 영업일
- 참석자/승인권자
- Project Close 영향
- WBS/Calendar 갱신

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 📋 핵심 요구사항

- [ ] 필수 참석자의 가능시간을 확인한다.
- [ ] 유지 시 근무·승인 절차를 확인한다.
- [ ] 변경 시 Deliverable Freeze와 Close 영향도를 검토한다.
- [ ] 결정 결과를 관련 레코드에 반영한다.

---

# ✅ Acceptance Criteria

- [ ] 단일 Review 날짜와 시간이 승인된다.
- [ ] 필수 참석자·승인권자가 확정된다.
- [ ] P2-REV-01/MS-P2-REVIEW-01 일정이 동일하다.

---

# 🧪 검증 및 증적

- Decision D24
- 참석 확인
- 갱신 Calendar/WBS
- Review Invite 또는 회의 계획
- Evidence Path: `docs/evidence/DEC-CAL-P2-01/`

---

# 🔗 Dependency

- **Blocked By:** MS-G6-01, P2-DOC-01 진행상태
- **Blocks / Next:** MS-P2-REVIEW-01, P2-REV-01
- **Related Ticket:** MS-PROJECT-CLOSE-01
- **Milestone:** Phase 2 Review

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D24
- **Decision Control:** D24는 주말 일정 승인 또는 대체 영업일을 기록한다.
- **Related Risk IDs:** RISK-05; RISK-13
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** 10-24 토요일 Review 유지 또는 영업일 재배치, 참석자·승인권자·시간·Project Close 영향도를 확정하고 WBS 동기화
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>
