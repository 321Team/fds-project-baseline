<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P2-E2E-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P2-E2E-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 계획 단계. D22/D23 반영 Hybrid 정상/Rule/Negative/터널 복구·Critical0의 고정 케이스.

**인계·관련 티켓:** [#44](https://github.com/321Team/fds-project-baseline/issues/44) · [#47](https://github.com/321Team/fds-project-baseline/issues/47).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P2-E2E-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P2-E2E-01 -->
# P2-E2E-01 — Hybrid E2E / Regression

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-E2E-01 |
| Phase | Phase 2 |
| Category | QA / Hybrid E2E |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-20 |
| End | 2026-10-22 |
| Calendar Days | 4 |
| Working Days | 4 |
| Lead | 이재환 |
| Support | 이권욱, 이하영 |
| Exit Criteria | ROSA transaction-api→fds-engine→On-Prem PostgreSQL Hybrid E2E, Rule/Negative/Recovery Regression PASS와 Critical Issue 0 |
| Related Decision IDs | D21; D22; D23 |
| Related Risk IDs | RISK-09; RISK-10; RISK-11; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #50 snapshot 2026-09-10T02:10:05Z |
| Schedule Note | IP Endpoint와 Registry N/A 여부는 승인 Decision 결과를 Expected에 반영한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T02:10:05Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #50](https://github.com/321Team/fds-project-baseline/issues/50), Issue 갱신 시각 `2026-09-10T02:10:05Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

QA 담당자로서 Cloud 애플리케이션과 On-Prem 데이터 경로의 최종 업무 흐름을 검증한다. 이를 통해 Tunnel UP과 같은 인프라 상태가 아닌 실제 거래 결과로 Hybrid 완료를 판정한다.

---

# Scope

## In Scope

- Hybrid Transaction E2E
- 4 Rule
- On-Prem DB
- Negative Test
- Tunnel/Recovery Regression
- Defect

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] Transaction ID로 ROSA/API/DB Evidence를 연결한다.
- [ ] Tunnel과 App Failure를 구분한다.
- [ ] 승인되지 않은 Source/Port 차단을 검증한다.
- [ ] Decision D22/D23 결과를 Expected에 반영한다.
- [ ] Critical Issue 0 기준을 적용한다.

---

# Acceptance Criteria

- [ ] Hybrid 정상 거래가 성공한다.
- [ ] 4개 Rule 결과와 DB 저장이 일치한다.
- [ ] 미승인 경로가 차단된다.
- [ ] Tunnel 복구 후 Regression이 통과한다.
- [ ] Critical Issue가 0건이다.

---

# 검증 및 증적

- Hybrid Test Case
- ROSA API/FDS Log
- On-Prem DB Query
- Route/Tunnel 상태
- Negative/Recovery Regression
- Defect Report
- Evidence Path: `321Team/fds-project-evidence:evidence/P2-E2E-01/`

---

# Dependency

- **Blocked By:** P2-HYB-01, P2-OADP-01
- **Blocks / Next:** P2-DOC-01
- **Related Ticket:** 전체 Phase 2 P0
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
- **Exit Criteria:** ROSA transaction-api→fds-engine→On-Prem PostgreSQL Hybrid E2E, Rule/Negative/Recovery Regression PASS와 Critical Issue 0
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `57312a6b53247777b56f4813edafac1b390e388a3669500c80b8b39e0c063414`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P2-E2E-01 -->
# P2-E2E-01 — Hybrid E2E / Regression

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P2-E2E-01 |
| Phase | Phase 2 |
| Category | QA / Hybrid E2E |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-19 |
| End | 2026-10-22 |
| Calendar Days | 4 |
| Working Days | 4 |
| Lead | 이재환 |
| Support | 이권욱, 이하영 |
| Exit Criteria | ROSA transaction-api→fds-engine→On-Prem PostgreSQL Hybrid E2E, Rule/Negative/Recovery Regression PASS와 Critical Issue 0 |
| Related Decision IDs | D21; D22; D23 |
| Related Risk IDs | RISK-09; RISK-10; RISK-11; RISK-12 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Phase1_Logical_Architecture_v3.1.2; Phase 2 OCI/AWS/ROSA Design; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | IP Endpoint와 Registry N/A 여부는 승인 Decision 결과를 Expected에 반영한다. |

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

QA 담당자로서 Cloud 애플리케이션과 On-Prem 데이터 경로의 최종 업무 흐름을 검증한다. 이를 통해 Tunnel UP과 같은 인프라 상태가 아닌 실제 거래 결과로 Hybrid 완료를 판정한다.

---

# 📌 Scope

## In Scope

- Hybrid Transaction E2E
- 4 Rule
- On-Prem DB
- Negative Test
- Tunnel/Recovery Regression
- Defect

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 📋 핵심 요구사항

- [ ] Transaction ID로 ROSA/API/DB Evidence를 연결한다.
- [ ] Tunnel과 App Failure를 구분한다.
- [ ] 승인되지 않은 Source/Port 차단을 검증한다.
- [ ] Decision D22/D23 결과를 Expected에 반영한다.
- [ ] Critical Issue 0 기준을 적용한다.

---

# ✅ Acceptance Criteria

- [ ] Hybrid 정상 거래가 성공한다.
- [ ] 4개 Rule 결과와 DB 저장이 일치한다.
- [ ] 미승인 경로가 차단된다.
- [ ] Tunnel 복구 후 Regression이 통과한다.
- [ ] Critical Issue가 0건이다.

---

# 🧪 검증 및 증적

- Hybrid Test Case
- ROSA API/FDS Log
- On-Prem DB Query
- Route/Tunnel 상태
- Negative/Recovery Regression
- Defect Report
- Evidence Path: `docs/evidence/P2-E2E-01/`

---

# 🔗 Dependency

- **Blocked By:** P2-HYB-01, P2-OADP-01
- **Blocks / Next:** P2-DOC-01
- **Related Ticket:** 전체 Phase 2 P0
- **Milestone:** G6 Hybrid Integration Ready

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D21; D22; D23
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-09; RISK-10; RISK-11; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** ROSA transaction-api→fds-engine→On-Prem PostgreSQL Hybrid E2E, Rule/Negative/Recovery Regression PASS와 Critical Issue 0
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>
