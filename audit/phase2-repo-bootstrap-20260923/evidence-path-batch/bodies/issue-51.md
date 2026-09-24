<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P2-OP-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P2-OP-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 조건부 구현. D26 선택 이후 ImageSet/Package/Channel·Digest/Trust·Catalog Ready 또는 Cancelled 근거.

**인계·관련 티켓:** [#41](https://github.com/321Team/fds-project-baseline/issues/41).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-milestone-assignment:2026-09-11 issue:51 -->
## 대표 Milestone 배정 — 2026-09-11

- **추적 Milestone:** G6 Hybrid Integration Ready (GitHub #10)
- **배정 성격:** P2 잠정 계획 · 이권욱 사용자 지시에 따른 대표 추적 항목 지정.
- **배정 근거:** WBS 2026-10-19~10-20의 G5 이후 P1 조건부 작업을 다음 통합 검증 G6에서 잠정 추적한다. 새로운 G6 필수조건을 추가하지 않는다. D26에서 Mirror 선택 시 구현, Direct 선택 시 승인된 미구현 처리 원칙을 유지한다.
- **출처:** [발행 정본 v3.1.18 WBS](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/wbs/FDS_v3.1.18_WBS_and_Gantt_v1.0.xlsx)
- **일정 원칙:** 일정은 고정된 필수 기한이 아닌 조정 가능한 계획 목표다. 선행조건과 영향 확인 후 유연하게 조정하며, 실제 완료일·승인·Runtime 증적 요건과 구분한다.
- **적용 범위:** 대표 Milestone 연결과 이 근거 기록. 기존 상태·완료 사실·AC·담당·티켓 Start/End 및 Gate 요건을 유지한다.

---

<!-- fds-notion-migration:2026-09-09 record-id:P2-OP-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P2-OP-01 -->
# P2-OP-01 — Operator Supply Chain Implementation Conditional

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-OP-01 |
| Phase | Phase 2 |
| Category | Operator Supply Chain |
| Type | Task |
| Status | To Do |
| Priority | P1 |
| Start | 2026-10-20 |
| End | 2026-10-21 |
| Calendar Days | 2 |
| Working Days | 2 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | D26이 Mirror를 선택한 경우 oc-mirror ImageSet·Harbor Push·Custom CatalogSource·Package 조회 PASS; Direct Catalog 선택 시 Cancelled 결정 근거 승인 |
| Related Decision IDs | D22; D26 |
| Related Risk IDs | RISK-06; RISK-11; RISK-15 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #51 snapshot 2026-09-10T02:10:07Z |
| Schedule Note | DEC-P2-OP-01 / D26에서 Direct Catalog를 선택하면 Status=Cancelled와 결정 근거를 기록한다. Mirror 선택 시 구현을 진행한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T02:10:07Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #51](https://github.com/321Team/fds-project-baseline/issues/51), Issue 갱신 시각 `2026-09-10T02:10:07Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

OpenShift 담당자 이하영으로서 D26이 Mirror 방식을 선택한 경우 Operator 공급망을 구현한다. Direct Catalog가 선택되면 구현하지 않고 Cancelled 결정 근거를 승인받는다.

---

# Scope

## In Scope

- oc-mirror ImageSet
- Harbor Push
- Custom CatalogSource
- Package 조회
- 조건부 N/A

## Out of Scope

- D26 승인 전 구현
- 무관한 Operator 전체 Mirror

---

# 핵심 요구사항

- [ ] 필요 Operator와 Channel만 선택한다.
- [ ] Image/Catalog Source를 버전 관리한다.
- [ ] TLS와 Credential을 통제한다.
- [ ] Direct 선택으로 구현을 취소하면 Status=Cancelled와 결정 근거를 기록한다.

---

# Acceptance Criteria

- [ ] Mirror 선택 시 Image와 Metadata가 Harbor에 저장된다.
- [ ] CatalogSource가 Ready다.
- [ ] 필요 Package/Channel이 조회된다.
- [ ] Direct 선택 시 Cancelled 결정 근거가 승인된다.

---

# 검증 및 증적

- ImageSetConfiguration
- oc-mirror Log
- CatalogSource/PackageManifest
- N/A Decision
- Evidence Path: `321Team/fds-project-evidence:evidence/P2-OP-01/`

---

# Dependency

- **Blocked By:** DEC-P2-OP-01 / D26
- **Blocks / Next:** 필요 시 P2-OADP-01
- **Related Ticket:** P2-HBR-01 N/A; DEC-P2-REG-01
- **Milestone:** Phase 2 P1

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
- **Exit Criteria:** D26이 Mirror를 선택한 경우 oc-mirror ImageSet·Harbor Push·Custom CatalogSource·Package 조회 PASS; Direct Catalog 선택 시 Cancelled 결정 근거 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `e5ebde7aca5d6454c9c2bacfa9cd6b1c98266d03bd3aad024dd07be1b1ae4b07`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P2-OP-01 -->
# P2-OP-01 — Operator Supply Chain Implementation Conditional

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P2-OP-01 |
| Phase | Phase 2 |
| Category | Operator Supply Chain |
| Type | Task |
| Status | To Do |
| Priority | P1 |
| Start | 2026-10-19 |
| End | 2026-10-20 |
| Calendar Days | 2 |
| Working Days | 2 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | D26이 Mirror를 선택한 경우 oc-mirror ImageSet·Harbor Push·Custom CatalogSource·Package 조회 PASS; Direct Catalog 선택 시 Cancelled 결정 근거 승인 |
| Related Decision IDs | D22; D26 |
| Related Risk IDs | RISK-06; RISK-11; RISK-15 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Network_Baseline_v2.3; FDS_Phase1_Logical_Architecture_v3.1.2; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | DEC-P2-OP-01 / D26에서 Direct Catalog를 선택하면 Status=Cancelled와 결정 근거를 기록한다. Mirror 선택 시 구현을 진행한다. |

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

OpenShift 담당자 이하영으로서 D26이 Mirror 방식을 선택한 경우 Operator 공급망을 구현한다. Direct Catalog가 선택되면 구현하지 않고 Cancelled 결정 근거를 승인받는다.

---

# 📌 Scope

## In Scope

- oc-mirror ImageSet
- Harbor Push
- Custom CatalogSource
- Package 조회
- 조건부 N/A

## Out of Scope

- D26 승인 전 구현
- 무관한 Operator 전체 Mirror

---

# 📋 핵심 요구사항

- [ ] 필요 Operator와 Channel만 선택한다.
- [ ] Image/Catalog Source를 버전 관리한다.
- [ ] TLS와 Credential을 통제한다.
- [ ] Direct 선택으로 구현을 취소하면 Status=Cancelled와 결정 근거를 기록한다.

---

# ✅ Acceptance Criteria

- [ ] Mirror 선택 시 Image와 Metadata가 Harbor에 저장된다.
- [ ] CatalogSource가 Ready다.
- [ ] 필요 Package/Channel이 조회된다.
- [ ] Direct 선택 시 Cancelled 결정 근거가 승인된다.

---

# 🧪 검증 및 증적

- ImageSetConfiguration
- oc-mirror Log
- CatalogSource/PackageManifest
- N/A Decision
- Evidence Path: docs/evidence/P2-OP-01/

---

# 🔗 Dependency

- **Blocked By:** DEC-P2-OP-01 / D26
- **Blocks / Next:** 필요 시 P2-OADP-01
- **Related Ticket:** P2-HBR-01 N/A; DEC-P2-REG-01
- **Milestone:** Phase 2 P1

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D22; D26
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-06; RISK-11; RISK-15
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** D26이 Mirror를 선택한 경우 oc-mirror ImageSet·Harbor Push·Custom CatalogSource·Package 조회 PASS; Direct Catalog 선택 시 Cancelled 결정 근거 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>
