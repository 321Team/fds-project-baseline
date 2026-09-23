<!-- fds-oci-schedule:20260924:v1:start -->
## OCI 연계 일정 정합화 — 2026-09-24 KST

사용자 “일정 불일치부터 해소” 지시에 따라 일정 표시와 기간 계산을 정정했다. [2026-09-22 재계획](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-5779875065) 및 발행 docs-v3.1.20 WBS의 비근무일을 근거로 한다. 기존 10-06~10-09의 작업 가능일은 10-06·07·08의 3일이므로 **OCI 종료/D21 목표를 10-08로 통일**한다.

- **이 티켓의 계획:** 2026-10-06 ~ 2026-10-06 · 달력 1일 / 작업 1일. 10-06 설계 동결 목표. MS-P2-START-01 및 기존 선행조건 충족 후 Phase 2 구현이 참조할 설계 Source를 확정한다.
- **연계 목표:** Phase 2 착수/설계 10-06, D21 10-08, IaC 10-06~13, VPN 준비 10-08~13, G4 10-13. VPN 적용은 기존 선행조건 충족 후이며, IaC 완료 목표와 G4가 같은 날이므로 실제 적용·검증 작업창 확보를 확인해야 한다.
- 아래 이전 정본 머리말·마일스톤 배정·보관 원문의 과거 일정은 이력이다. 현행 계획 일정은 이 정정과 갱신한 티켓 속성표를 따른다. [정정 근거 및 차기 정본 반영안](https://github.com/321Team/fds-project-baseline/blob/docs/oci-schedule-align-20260924/audit/oci-schedule-20260924/README.md).
- 계획 정정이며 OCI 도입 승인, D21 판정 완료, G4 통과를 뜻하지 않는다. 발행 정본 편입은 별도이며 상태·AC·담당·기존 선행조건은 유지한다.
- 동기화 잔여: #36의 별도 Target date는 10-09→10-08, GitHub Milestone #7 기한/현행 설명은 09-28→10-06, #8은 10-08→10-13 갱신이 필요하다. 현재 연결은 해당 필드 쓰기를 제공하지 않아 본문 갱신과 구분해 추적한다.
<!-- fds-oci-schedule:20260924:v1:end -->

---

<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P2-ARC-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P2-ARC-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 계획 단계. P2 CIDR·IF17~20·Region/배치·D21~23/26·Gate 기준은 설계 Freeze 전에 고정.

**인계·관련 티켓:** [#35](https://github.com/321Team/fds-project-baseline/issues/35) · [#36](https://github.com/321Team/fds-project-baseline/issues/36) · [#37](https://github.com/321Team/fds-project-baseline/issues/37) · [#38](https://github.com/321Team/fds-project-baseline/issues/38) · [#40](https://github.com/321Team/fds-project-baseline/issues/40) · [#41](https://github.com/321Team/fds-project-baseline/issues/41) · [#42](https://github.com/321Team/fds-project-baseline/issues/42).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-milestone-assignment:2026-09-11 issue:34 -->
## 대표 Milestone 배정 — 2026-09-11

- **추적 Milestone:** Phase 2 Start (GitHub #7)
- **배정 성격:** P2 잠정 계획 · 이권욱 사용자 지시에 따른 대표 추적 항목 지정.
- **배정 근거:** WBS 2026-09-28 설계 확정 및 MS-P2-START-01 직후 완료 계획에 따라 Phase 2 Start에 연결한다. G4 선행 설계 관계는 유지한다.
- **출처:** [발행 정본 v3.1.18 WBS](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/wbs/FDS_v3.1.18_WBS_and_Gantt_v1.0.xlsx)
- **일정 원칙:** 일정은 고정된 필수 기한이 아닌 조정 가능한 계획 목표다. 선행조건과 영향 확인 후 유연하게 조정하며, 실제 완료일·승인·Runtime 증적 요건과 구분한다.
- **적용 범위:** 대표 Milestone 연결과 이 근거 기록. 기존 상태·완료 사실·AC·담당·티켓 Start/End 및 Gate 요건을 유지한다.

---

<!-- fds-notion-migration:2026-09-09 record-id:P2-ARC-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P2-ARC-01 -->
# P2-ARC-01 — Hybrid / OCI / AWS / ROSA Architecture Freeze

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-ARC-01 |
| Phase | Phase 2 |
| Category | Architecture / Hybrid Cloud |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-06 |
| End | 2026-10-06 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | OCI Relay·AWS VPC/VPN·ROSA·On-Prem 연계 Architecture, Interface IF-17~IF-20, Security, Decision, Exit Criteria Freeze 승인 |
| Related Decision IDs | D10; D21; D22; D23; D25; D26 |
| Related Risk IDs | RISK-10; RISK-11; RISK-12; RISK-14; RISK-15 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #34 snapshot 2026-09-10T02:09:45Z; 일정: docs-v3.1.20 WBS + 2026-09-22 재계획 + 2026-09-24 일정 정합화 |
| Schedule Note | 10-06 설계 동결 목표. MS-P2-START-01 및 기존 선행조건 충족 후 Phase 2 구현이 참조할 설계 Source를 확정한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T02:09:45Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #34](https://github.com/321Team/fds-project-baseline/issues/34), Issue 갱신 시각 `2026-09-10T02:09:45Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

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
- Evidence Path: `321Team/fds-project-evidence:evidence/P2-ARC-01/`

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

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `309fc769d79ad7301fa62d54a130bfc32c5ec6d0651b3fffceb7792fc43aa74c`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P2-ARC-01 -->
# P2-ARC-01 — Hybrid / OCI / AWS / ROSA Architecture Freeze

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
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
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Network_Baseline_v2.3; FDS_Phase1_Logical_Architecture_v3.1.2; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | MS-P2-START-01 직후 완료하며 Phase 2 모든 구현 티켓이 참조하는 Phase 2 OCI/AWS/ROSA Design의 권위 Source를 생성한다. |

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

Hybrid Architecture 담당자 이권욱으로서 OCI Relay, AWS VPN, ROSA 및 On-Prem 서비스의 설계 계약을 동결한다. 이를 통해 Phase 2 구현 티켓이 동일한 CIDR·Interface·Security·Fallback 기준을 사용하도록 한다.

---

# 📌 Scope

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

# 📋 핵심 요구사항

- [ ] On-Prem/AWS CIDR 중복을 방지한다.
- [ ] Primary/Fallback 경로의 전환 조건을 명시한다.
- [ ] Producer/Consumer/Port/Owner/Acceptance를 동결한다.
- [ ] Phase 2 Ticket과 Source를 상호 연결한다.

---

# ✅ Acceptance Criteria

- [ ] Architecture와 Interface가 이권욱·이하영·이재환 검토 대상으로 배포된다.
- [ ] P2-OCI/IAC/VPN/ROSA/APP/CICD의 의존성이 연결된다.
- [ ] D21~D23·D26의 결정 시점과 조건부 범위가 명시된다.
- [ ] 변경 통제 기준이 승인된다.

---

# 🧪 검증 및 증적

- Phase 2 Architecture Source
- Interface Register
- Decision/Risk Mapping
- Review Record
- Evidence Path: docs/evidence/P2-ARC-01/

---

# 🔗 Dependency

- **Blocked By:** MS-P1-CLOSE-01; MS-P2-START-01
- **Blocks / Next:** P2-OCI-01; P2-IAC-01; P2-VPN-01; P2-ROSA-01
- **Related Ticket:** P2-DOC-01
- **Milestone:** Phase 2 Start / G4

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D10; D21; D22; D23; D25; D26
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-10; RISK-11; RISK-12; RISK-14; RISK-15
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** OCI Relay·AWS VPC/VPN·ROSA·On-Prem 연계 Architecture, Interface IF-17~IF-20, Security, Decision, Exit Criteria Freeze 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>
