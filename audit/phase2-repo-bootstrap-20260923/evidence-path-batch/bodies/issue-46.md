<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P2-CICD-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P2-CICD-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 계획 단계. ROSA API/SA·Token/Registry/Digest·성공/차단/복구 증거 계약을 실행 전에 고정.

**인계·관련 티켓:** [#38](https://github.com/321Team/fds-project-baseline/issues/38) · [#42](https://github.com/321Team/fds-project-baseline/issues/42) · [#43](https://github.com/321Team/fds-project-baseline/issues/43).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P2-CICD-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P2-CICD-01 -->
# P2-CICD-01 — Runner to ROSA Delivery

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 사용자 날짜 정정 — 2026-09-11

사용자 지시: “2차는 계획안이라 g5계획안으로 우선 앞당겨줘.” G5 목표 2026-10-16에 맞춰 계획 End를 2026-10-19에서 2026-10-16으로 조정했다. Start 2026-10-16 유지에 따라 Calendar Days/Working Days는 4/2에서 1/1로 재계산했다. 실제 GitHub Milestone은 기존 G5 ROSA Application Ready(#9)에 연결한다. 이는 유연한 계획 목표이며 1일 내 구현 가능성·실제 완료·G5 통과를 보증하지 않는다.

상태·담당자·기존 AC 체크·과거 승인 및 첨부 원문은 보존한다. 발행된 v3.1.18은 당시 스냅샷이며 이번 정정은 [후속 보완 PR #72](https://github.com/321Team/fds-project-baseline/pull/72)에 편입한다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-CICD-01 |
| Phase | Phase 2 |
| Category | CI/CD / OpenShift Delivery |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-18 |
| End | 2026-10-18 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | GitHub→Self-hosted Runner→승인 Registry→ROSA Deploy→Health/Rule Smoke Test 흐름과 실패 시 배포차단 Evidence 확보 |
| Related Decision IDs | D22; D25 |
| Related Risk IDs | RISK-06; RISK-08; RISK-11; RISK-14 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #46 snapshot 2026-09-10T02:09:57Z; 2026-09-11 사용자 날짜 정정 — Issue #46 날짜 정정 기록 / PR #72 후속 편입 |
| Schedule Note | P2-ROSA-01과 P2-APP-01의 Manifest/Image 계약을 사용하고 Registry는 D22 결과를 따른다. G5 ROSA Application Ready에 연결한다. 2026-09-11 사용자 지시에 따라 End를 G5 목표 2026-10-16으로 앞당겼다. Start 10/16 유지, Calendar Days/Working Days 1/1. 선행 작업과 가용성에 따라 조정 가능한 계획이며 Runtime 완료 판정은 아니다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T02:09:57Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

작성 당시에는 Plan End 2026-10-19와 G5 목표 2026-10-16의 충돌로 Milestone 매핑이 HOLD였다. 2026-09-11 사용자가 G5 계획안에 맞춰 앞당기도록 지시하여 Plan End를 2026-10-16으로 조정하고 G5 ROSA Application Ready로 연결했다. 날짜/G5 매핑 사유는 해소됐으며 실제 구현·Gate 승인은 별도다.

근거: [Issue #46](https://github.com/321Team/fds-project-baseline/issues/46), Issue 갱신 시각 `2026-09-10T02:09:57Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Cloud Delivery 담당자 이권욱으로서 검증된 Phase 1 Image를 승인 Registry에서 ROSA로 자동 배포한다. 이를 통해 On-Prem과 ROSA의 Delivery 추적성과 실패 차단 기준을 유지한다.

---

# Scope

## In Scope

- GitHub Private Repo
- Self-hosted Runner
- 승인 Registry
- oc/kubectl/Helm Deploy
- Health·Rule Smoke Test
- 실패 차단

## Out of Scope

- 승인되지 않은 Registry
- 수동 Secret 하드코딩
- Production 무중단 배포 보증

---

# 핵심 요구사항

- [ ] Commit SHA와 Image Digest를 연결한다.
- [ ] ROSA Credential을 Secret으로 통제한다.
- [ ] Test/Scan 실패 시 Deploy를 차단한다.
- [ ] D22 Registry 결정을 준수한다.

---

# Acceptance Criteria

- [ ] 정상 Commit이 ROSA까지 배포된다.
- [ ] Test 또는 Scan 실패 시 배포가 차단된다.
- [ ] 배포 Image와 Commit을 역추적할 수 있다.
- [ ] Health와 R01/R02/R04/R07 Smoke Test가 통과한다.

---

# 검증 및 증적

- Workflow Source
- Runner/Registry/ROSA Run
- Failed Gate Run
- Image Digest
- Evidence Path: `321Team/fds-project-evidence:evidence/P2-CICD-01/`

---

# Dependency

- **Blocked By:** P2-ROSA-01; P2-APP-01; DEC-P2-REG-01
- **Blocks / Next:** MS-G5-01; P2-HYB-01
- **Related Ticket:** P1-CICD-01
- **Milestone:** G5 ROSA Application Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D22; D25
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-06; RISK-08; RISK-11; RISK-14
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** GitHub→Self-hosted Runner→승인 Registry→ROSA Deploy→Health/Rule Smoke Test 흐름과 실패 시 배포차단 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `3e46119cea0b0ccfb1cd63e2851679112f4c402c114f3091157b99950fff72cb`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P2-CICD-01 -->
# P2-CICD-01 — Runner to ROSA Delivery

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P2-CICD-01 |
| Phase | Phase 2 |
| Category | CI/CD / OpenShift Delivery |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-16 |
| End | 2026-10-19 |
| Calendar Days | 4 |
| Working Days | 2 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | GitHub→Self-hosted Runner→승인 Registry→ROSA Deploy→Health/Rule Smoke Test 흐름과 실패 시 배포차단 Evidence 확보 |
| Related Decision IDs | D22; D25 |
| Related Risk IDs | RISK-06; RISK-08; RISK-11; RISK-14 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Network_Baseline_v2.3; FDS_Phase1_Logical_Architecture_v3.1.2; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | P2-ROSA-01과 P2-APP-01의 Manifest/Image 계약을 사용하고 Registry는 D22 결과를 따른다. G5 ROSA Application Ready에 연결한다. |

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

Cloud Delivery 담당자 이권욱으로서 검증된 Phase 1 Image를 승인 Registry에서 ROSA로 자동 배포한다. 이를 통해 On-Prem과 ROSA의 Delivery 추적성과 실패 차단 기준을 유지한다.

---

# 📌 Scope

## In Scope

- GitHub Private Repo
- Self-hosted Runner
- 승인 Registry
- oc/kubectl/Helm Deploy
- Health·Rule Smoke Test
- 실패 차단

## Out of Scope

- 승인되지 않은 Registry
- 수동 Secret 하드코딩
- Production 무중단 배포 보증

---

# 📋 핵심 요구사항

- [ ] Commit SHA와 Image Digest를 연결한다.
- [ ] ROSA Credential을 Secret으로 통제한다.
- [ ] Test/Scan 실패 시 Deploy를 차단한다.
- [ ] D22 Registry 결정을 준수한다.

---

# ✅ Acceptance Criteria

- [ ] 정상 Commit이 ROSA까지 배포된다.
- [ ] Test 또는 Scan 실패 시 배포가 차단된다.
- [ ] 배포 Image와 Commit을 역추적할 수 있다.
- [ ] Health와 R01/R02/R04/R07 Smoke Test가 통과한다.

---

# 🧪 검증 및 증적

- Workflow Source
- Runner/Registry/ROSA Run
- Failed Gate Run
- Image Digest
- Evidence Path: docs/evidence/P2-CICD-01/

---

# 🔗 Dependency

- **Blocked By:** P2-ROSA-01; P2-APP-01; DEC-P2-REG-01
- **Blocks / Next:** MS-G5-01; P2-HYB-01
- **Related Ticket:** P1-CICD-01
- **Milestone:** G5 ROSA Application Ready

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D22; D25
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-06; RISK-08; RISK-11; RISK-14
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** GitHub→Self-hosted Runner→승인 Registry→ROSA Deploy→Health/Rule Smoke Test 흐름과 실패 시 배포차단 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>
