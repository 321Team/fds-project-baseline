<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P2-OCI-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P2-OCI-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 계획 단계. OCI Go/No-Go 및 단일 Fallback·비용/일정/보안 승인 기록. 체크포인트와 완료일 구분.

**인계·관련 티켓:** [#35](https://github.com/321Team/fds-project-baseline/issues/35) · [#37](https://github.com/321Team/fds-project-baseline/issues/37).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-milestone-assignment:2026-09-11 issue:36 -->
## 대표 Milestone 배정 — 2026-09-11

- **추적 Milestone:** G4 Cloud / VPN Ready (GitHub #8)
- **배정 성격:** P2 잠정 계획 · 이권욱 사용자 지시에 따른 대표 추적 항목 지정.
- **배정 근거:** WBS 2026-09-28~10-02 OCI Go/No-Go와 후속 VPN 구축 관계에 따라 G4에 연결한다. 티켓의 10-02 의사결정 체크포인트는 유지하며 G4 날짜로 대체하지 않는다.
- **출처:** [발행 정본 v3.1.18 WBS](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/wbs/FDS_v3.1.18_WBS_and_Gantt_v1.0.xlsx)
- **일정 원칙:** 일정은 고정된 필수 기한이 아닌 조정 가능한 계획 목표다. 선행조건과 영향 확인 후 유연하게 조정하며, 실제 완료일·승인·Runtime 증적 요건과 구분한다.
- **적용 범위:** 대표 Milestone 연결과 이 근거 기록. 기존 상태·완료 사실·AC·담당·티켓 Start/End 및 Gate 요건을 유지한다.

---

<!-- fds-notion-migration:2026-09-09 record-id:P2-OCI-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P2-OCI-01 -->
# P2-OCI-01 — OCI Relay Go / No-Go

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-OCI-01 |
| Phase | Phase 2 |
| Category | Milestone / Hybrid Network |
| Type | Decision |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-06 |
| End | 2026-10-09 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | OCI Relay 가능성·권한·Public Endpoint·IPsec/NAT-T·Route를 검증하고 Primary 또는 승인 Fallback 경로를 선택 |
| Related Decision IDs | D10; D21 |
| Related Risk IDs | RISK-10; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #36 snapshot 2026-09-09T12:07:26Z |
| Schedule Note | 10-02 Go/No-Go를 넘기지 않는다. No-Go 시 Vendor Endpoint→AWS EC2+EIP Relay→Overlay 순으로 승인된 Fallback을 선택한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-09T12:07:26Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #36](https://github.com/321Team/fds-project-baseline/issues/36), Issue 갱신 시각 `2026-09-09T12:07:26Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Hybrid Network 담당자로서 OCI Relay를 Primary Transit으로 사용할 수 있는지 조기에 판정한다. 이를 통해 실패 가능성이 큰 경로를 G4 직전까지 끌고 가지 않고 대체경로를 통제한다.

---

# Scope

## In Scope

- OCI 권한/Endpoint
- IPsec/NAT-T
- Route
- AWS VPN 연계 가능성
- Fallback 비교
- Go/No-Go 승인

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] 필요 계정·권한·Quota를 확인한다.
- [ ] Public Endpoint와 NAT 조건을 검증한다.
- [ ] On-Prem/AWS CIDR 중복을 확인한다.
- [ ] Fallback별 비용·일정·보안 영향을 기록한다.

---

# Acceptance Criteria

- [ ] OCI Primary의 실행 가능 여부가 증적으로 판정된다.
- [ ] Go 또는 단일 Fallback이 승인된다.
- [ ] P2-VPN-01과 P2-IAC-01 입력값이 확정된다.
- [ ] 미결 전제와 Owner/Due가 0건이다.

---

# 검증 및 증적

- OCI/AWS 권한·리소스 확인
- Endpoint/Route Test
- Fallback 비교표
- Decision D21
- 갱신 Architecture/WBS
- Evidence Path: `321Team/fds-project-evidence:evidence/P2-OCI-01/`

---

# Dependency

- **Blocked By:** MS-P1-CLOSE-01
- **Blocks / Next:** P2-VPN-01
- **Related Ticket:** P2-IAC-01
- **Milestone:** OCI Go/No-Go — 2026-10-02

---

# Decision / Risk Control

- **Related Decision IDs:** D10; D21
- **Decision Control:** D21 결과로 Primary/Fallback과 비용·일정 영향도를 승인한다.
- **Related Risk IDs:** RISK-10; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** OCI Relay 가능성·권한·Public Endpoint·IPsec/NAT-T·Route를 검증하고 Primary 또는 승인 Fallback 경로를 선택
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `25fa85700fabf55d1988551283ccbfc3edeb3514646e3400da22b0b81b32048d`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P2-OCI-01 -->
# P2-OCI-01 — OCI Relay Go / No-Go

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P2-OCI-01 |
| Phase | Phase 2 |
| Category | Milestone / Hybrid Network |
| Type | Decision |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-28 |
| End | 2026-10-02 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | OCI Relay 가능성·권한·Public Endpoint·IPsec/NAT-T·Route를 검증하고 Primary 또는 승인 Fallback 경로를 선택 |
| Related Decision IDs | D10; D21 |
| Related Risk IDs | RISK-10; RISK-12 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Phase1_Logical_Architecture_v3.1.2; Phase 2 OCI/AWS/ROSA Design; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 10-02 Go/No-Go를 넘기지 않는다. No-Go 시 Vendor Endpoint→AWS EC2+EIP Relay→Overlay 순으로 승인된 Fallback을 선택한다. |

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

Hybrid Network 담당자로서 OCI Relay를 Primary Transit으로 사용할 수 있는지 조기에 판정한다. 이를 통해 실패 가능성이 큰 경로를 G4 직전까지 끌고 가지 않고 대체경로를 통제한다.

---

# 📌 Scope

## In Scope

- OCI 권한/Endpoint
- IPsec/NAT-T
- Route
- AWS VPN 연계 가능성
- Fallback 비교
- Go/No-Go 승인

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 📋 핵심 요구사항

- [ ] 필요 계정·권한·Quota를 확인한다.
- [ ] Public Endpoint와 NAT 조건을 검증한다.
- [ ] On-Prem/AWS CIDR 중복을 확인한다.
- [ ] Fallback별 비용·일정·보안 영향을 기록한다.

---

# ✅ Acceptance Criteria

- [ ] OCI Primary의 실행 가능 여부가 증적으로 판정된다.
- [ ] Go 또는 단일 Fallback이 승인된다.
- [ ] P2-VPN-01과 P2-IAC-01 입력값이 확정된다.
- [ ] 미결 전제와 Owner/Due가 0건이다.

---

# 🧪 검증 및 증적

- OCI/AWS 권한·리소스 확인
- Endpoint/Route Test
- Fallback 비교표
- Decision D21
- 갱신 Architecture/WBS
- Evidence Path: `docs/evidence/P2-OCI-01/`

---

# 🔗 Dependency

- **Blocked By:** MS-P1-CLOSE-01
- **Blocks / Next:** P2-VPN-01
- **Related Ticket:** P2-IAC-01
- **Milestone:** OCI Go/No-Go — 2026-10-02

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D10; D21
- **Decision Control:** D21 결과로 Primary/Fallback과 비용·일정 영향도를 승인한다.
- **Related Risk IDs:** RISK-10; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** OCI Relay 가능성·권한·Public Endpoint·IPsec/NAT-T·Route를 검증하고 Primary 또는 승인 Fallback 경로를 선택
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>
