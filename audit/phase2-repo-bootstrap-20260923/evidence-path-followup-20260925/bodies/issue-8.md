<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23 (누락분 2026-09-25 반영)

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/MS-G0-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/MS-G0-01/`
- 이 티켓은 2026-09-23 일괄 반영(49건)의 대상 추출에서 누락되어 2026-09-25 같은 형식으로 반영했다(“Evidence Path:” 표기 없이 경로만 적힌 형식). 근거: `audit/phase2-repo-bootstrap-20260923/evidence-path-followup-20260925/`.
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** G0 종결 유지. 후속 변경은 A07/R01/R05의 v19 변경 이력으로 연결.

**인계·관련 티켓:** [#24](https://github.com/321Team/fds-project-baseline/issues/24) · [#78](https://github.com/321Team/fds-project-baseline/issues/78).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:MS-G0-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:MS-G0-01 -->
# MS-G0-01 — G0 Design Freeze

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | MS-G0-01 |
| Phase | Design |
| Category | Milestone / Design Freeze |
| Type | Milestone |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-26 |
| End | 2026-09-01 |
| Calendar Days | 7 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | D-ARC-01·D-NET-01·D-WBS-01·D-SEC-01 승인과 정본 Evidence를 확인하고 G0 FULL PASS 기록 확보 |
| Related Decision IDs | D17; D28; D32; D34; D35 |
| Related Risk IDs | RISK-05; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #8 snapshot 2026-09-09T12:14:17Z |
| Schedule Note | G0 Design Freeze FULL PASS (2026-09-01). |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **Done / closed**. 원본 갱신 시각: `2026-09-09T12:14:17Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 Done 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #8](https://github.com/321Team/fds-project-baseline/issues/8), Issue 갱신 시각 `2026-09-09T12:14:17Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.

---

### User Story

프로젝트 Gate Owner 이권욱으로서 Architecture·Network·WBS·Security 설계 동결을 Evidence로 승인하고, Runtime Gate와 구분된 G0 결과를 확정한다.

### Scope

#### In Scope

- D-ARC-01, D-NET-01, D-WBS-01, D-SEC-01 승인 확인
- D17/D34와 Baseline v3.1.15 연결; D35 정합성 보정 추적
- G0 FULL PASS 기록

#### Out of Scope

- G1/G2 Runtime 구현과 후속 티켓의 실제 PASS 판정

### 핵심 요구사항

- [x] 설계 Ticket의 Lifecycle과 Gate Result를 분리한다.
- [x] 승인일·승인자·정본 Source를 동일하게 기록한다.

### Acceptance Criteria

- [x] 4개 Design Ticket Done
- [x] D17/D34 PASS
- [x] Baseline v3.1.15 RELEASED
- [x] G0 FULL PASS와 Lifecycle Done 동기화

### Evidence

- Baseline v3.1.15
- D-SEC-01 Security Design Baseline v1.0
- D34 승인 기록
- `321Team/fds-project-evidence:evidence/MS-G0-01/`

### Dependency

- Blocked By: 없음 — D17/D34 승인 완료
- Blocks / Next: G1 Infrastructure Ready, G2 Security / Feature Ready

### Decision / Risk Control

- Decision: D34에 따라 G0 FULL PASS를 확정한다.
- Risk Control: G0 종결을 G1/G2 Runtime 완료로 오인하지 않는다.

### Review / Handoff

- Review Owner: 이하영, 이재환
- Handoff: 각 구현 티켓은 자체 Runtime Evidence로 별도 종결한다.

### Completion Record

- Result: FULL PASS
- Status: Done
- Completed Date: 2026-09-01
- Approver: 이권욱

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `168963d707fbc59ed37d38de62fb097ea869f240bc3123268ff61ef413b526e1`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:MS-G0-01 -->
# MS-G0-01 — G0 Design Freeze

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | MS-G0-01 |
| Phase | Design |
| Category | Milestone / Design Freeze |
| Type | Milestone |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-26 |
| End | 2026-09-01 |
| Calendar Days | 7 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | D-ARC-01·D-NET-01·D-WBS-01·D-SEC-01 승인과 정본 Evidence를 확인하고 G0 FULL PASS 기록 확보 |
| Related Decision IDs | D17; D28; D32; D34; D35 |
| Related Risk IDs | RISK-05; RISK-07 |
| Source | FDS_Project_Implementation_Baseline_v3.1.15; D-SEC-01 Security Design Baseline v1.0; D35; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | G0 Design Freeze FULL PASS (2026-09-01). |

## 이관 기준 및 확인 사항

- 속성의 일정·담당·상태는 RELEASED v3.1.17 WBS(기준일 2026-09-04)를 우선 반영했다. 이후 별도 근거가 있는 변경만 아래에 명시한다.
- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`
- `FDS_v3.1.15_Canonical_Ticket_Update_Pack_v1.0.md`
- `FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx`

---

## Description — 보관 입력본

> 원본: `FDS_v3.1.15_Canonical_Ticket_Update_Pack_v1.0.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

### 🎯 User Story

프로젝트 Gate Owner 이권욱으로서 Architecture·Network·WBS·Security 설계 동결을 Evidence로 승인하고, Runtime Gate와 구분된 G0 결과를 확정한다.

### 📌 Scope

#### In Scope

- D-ARC-01, D-NET-01, D-WBS-01, D-SEC-01 승인 확인
- D17/D34와 Baseline v3.1.15 연결; D35 정합성 보정 추적
- G0 FULL PASS 기록

#### Out of Scope

- G1/G2 Runtime 구현과 후속 티켓의 실제 PASS 판정

### 📋 핵심 요구사항

- [x] 설계 Ticket의 Lifecycle과 Gate Result를 분리한다.
- [x] 승인일·승인자·정본 Source를 동일하게 기록한다.

### ✅ Acceptance Criteria

- [x] 4개 Design Ticket Done
- [x] D17/D34 PASS
- [x] Baseline v3.1.15 RELEASED
- [x] G0 FULL PASS와 Lifecycle Done 동기화

### 🧪 Evidence

- Baseline v3.1.15
- D-SEC-01 Security Design Baseline v1.0
- D34 승인 기록
- `docs/evidence/MS-G0-01/`

### 🔗 Dependency

- Blocked By: 없음 — D17/D34 승인 완료
- Blocks / Next: G1 Infrastructure Ready, G2 Security / Feature Ready

### ⚖️ Decision / Risk Control

- Decision: D34에 따라 G0 FULL PASS를 확정한다.
- Risk Control: G0 종결을 G1/G2 Runtime 완료로 오인하지 않는다.

### 🔍 Review / Handoff

- Review Owner: 이하영, 이재환
- Handoff: 각 구현 티켓은 자체 Runtime Evidence로 별도 종결한다.

### 📝 Completion Record

- Result: FULL PASS
- Status: Done
- Completed Date: 2026-09-01
- Approver: 이권욱
````

</details>
