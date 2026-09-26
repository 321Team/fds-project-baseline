<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P1-DR-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P1-DR-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

## 2026-09-18 요구사항·AC 증적 대조

9/15 이재환의 [db01 직접 실행 보고](https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-5677777537)를 현재 체크리스트에 연결한다. 신규 격리 DB `fdsdb_repro_test_0915`에서 9/3 백업의 Schema/Data 복구, `transactions` 15건, 대표 `fds_rules` 결과와 `alembic_version=0001`을 확인한 보고다. 9/1의 13건 재현과 구분한다. 아래 9/14 점검 및 v3.1.18 작성 시점 설명은 이력이다.

백업은 `fdsdb_backup_20260903.dump`, 보고 크기 5,206 bytes, 보고 SHA-256 `80962dcd41c8afe3920c7194e8b5e2a4531ee901b4027aad1d47209ed4a46f3d`이다. 완료 체크 3개 AC와 운영 원본 미덮어쓰기 요구는 담당 Lead 이재환의 9/15 실행·판정 기록에 따라 반영한다. 이번 확인은 담당자 실행 보고와 기존 정정 기록의 대조이며 dump 원본·원시 실행 로그 확보 및 해시 독립 재계산을 수행한 결과가 아니다. `pg_dump`/`pg_restore` 16.14를 Source DB 서버 버전으로 대신하지 않는다. Restore 후 정본 E2E와 Runbook은 잔여이며 To Do·계획 일정·담당은 유지한다.

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 격리 Restore·원본 해시/버전·revision/Row/Rule·복구 E2E 기록 ; R02. 새 RPO/RTO 요구 추가 없음.

- 운영 원본을 덮어쓰지 않는 격리 대상·Source DB버전/시각·dump 원본 해시·schema/revision·대표 Row/Rule·Restore 후 E2E와 Runbook을 남긴다. 9/1 사전 실증/9/3 dump 보고와 정본 복구 인수를 구분한다.

**DB 병합·운영·복구 기록 (R02)** — 앱 PR#2는 2026-09-11T03:01:53Z에 84a79c8550d23737b15eda3aacb8950ceafd8d17로 병합됐고 0002가 main에 있다. “PR 병합 필요”는 과거 상태다. 운영 db01의 schema fingerprint/revision·stamp 또는 조건부 변경 판단·백업/rollback과 신규 DB upgrade 재현은 별도로 기록한다. dump 원본 URI/해시/DB버전·시각·독립 확인/Restore·Row/Rule/E2E 증거는 미완료 범위로 유지한다.
근거: [앱 PR #2](https://github.com/supreme33-kr/fds-msa/pull/2) · [0002](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/alembic/versions/0002_add_fds_evaluation_columns.py) · [DB #11](https://github.com/321Team/fds-project-baseline/issues/11) · [DR #21](https://github.com/321Team/fds-project-baseline/issues/21)

**인계·관련 티켓:** [#11](https://github.com/321Team/fds-project-baseline/issues/11) · [#20](https://github.com/321Team/fds-project-baseline/issues/20).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P1-DR-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P1-DR-01 -->
# P1-DR-01 — PostgreSQL Backup / Restore

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-DR-01 |
| Phase | Phase 1 |
| Category | DR / Data Recovery |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-09-11 |
| End | 2026-09-21 |
| Calendar Days | 11 |
| Working Days | 3 |
| Lead | 이재환 |
| Support | 이권욱 |
| Exit Criteria | pg_dump Backup, 승인된 초기화/격리 환경 Restore, Row/Rule 결과 정합성 및 Restore 후 Final E2E PASS와 Runbook 확보 |
| Related Decision IDs | D04 |
| Related Risk IDs | RISK-05; RISK-09 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #21 snapshot 2026-09-10T04:02:43Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | 09-11 복구 절차·격리 대상 준비, 실제 Restore 및 후속 E2E는 09-21 오후 전용 창에서 수행한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T07:33:26Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.
- 수집된 운영 댓글은 원래 위치에 보존한다. 신규 구현 제출/리뷰 요청은 실행 PASS나 승인으로 간주하지 않는다.
  - [5612786465](https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-5612786465) · 2026-09-10T04:02:43Z
  - [5614865778](https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-5614865778) · 2026-09-10T07:33:26Z

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

9/1 격리 신규 DB의 pg_dump→TRUNCATE→pg_restore 13건 재현과 9/3 dump 보관이 담당자에 의해 보고됐다. 운영 db01 원본 변경을 뜻하지 않는다. 백업 원본 해시 독립 검증, 정식 Evidence 등록·Runbook·정본 Restore 후 E2E는 미완료다. 사전 착수 보고만으로 To Do를 자동 변경하지 않는다. 현재 후보 Plan: 2026-09-11 ~ 2026-09-21 (권장안; 실제 완료일·Gate 승인은 미확정).

근거: [Issue #21](https://github.com/321Team/fds-project-baseline/issues/21), Issue 갱신 시각 `2026-09-10T04:02:43Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- [후속 기록](https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-5612786465)

---

# User Story

데이터 담당자로서 PostgreSQL 논리 Backup으로 거래·FDS 데이터를 복구한다. 이를 통해 단일 DB 구조에서도 최소 복구 가능성과 절차 재현성을 입증한다.

---

# Scope

## In Scope

- pg_dump
- Backup Integrity
- pg_restore
- Row/Schema 검증
- Restore 후 E2E
- Runbook

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] Backup 시점과 Source DB Version을 기록한다.
  - 증적 대조(2026-09-18): 9/3 백업 시점 및 생성/복구 도구 16.14는 기록됨. Source DB 서버 버전은 별도 직접 기록 확인이 남아 있어 체크를 유지한다. [실행 보고](https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-5677777537)
- [x] 운영성 원본을 직접 덮어쓰지 않는다.
  - 증적 대조(2026-09-18): 9/15 담당자 보고상 신규 격리 DB에 복원하고 운영 `fdsdb` 미접촉·시험 DB 정리를 확인했다. 이번 원시 실행 로그 직접 검증은 미수행이다. [실행 보고](https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-5677777537)
- [ ] Schema와 Data 복구 순서를 명시한다.
- [ ] Credential과 Backup 파일 접근권한을 통제한다.

---

# Acceptance Criteria

- [x] Backup 파일이 정상 생성되고 검증된다.
  - 증적 대조(2026-09-18): 9/15 담당자 판정 PASS: `pg_restore -l` TOC 15항목·해시 일치 보고. 원본 dump 및 해시 독립 재계산은 이번에 확인하지 못했다. [실행 보고](https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-5677777537)
- [x] 빈 Restore 대상에 Schema/Data가 복구된다.
  - 증적 대조(2026-09-18): 9/15 담당자 판정 PASS: 신규 `fdsdb_repro_test_0915` 복원, 15행·revision `0001`. 운영 정본 E2E 완료 판정과 구분한다. [실행 보고](https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-5677777537)
- [x] 대표 Transaction/FDS Result가 일치한다.
  - 증적 대조(2026-09-18): 9/15 담당자 판정 PASS: 대표 Transaction 및 R01/R02/R04/R07 `fds_rules`가 로컬 사전 판독본과 일치했다고 보고됐다. 전체 현행 서비스 경로 검증은 별도다. [실행 보고](https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-5677777537)
- [ ] Restore 후 E2E가 통과한다.
  - 증적 대조(2026-09-18): NOT RUN: #11·#20·#10 선행조건 및 정본 앱 경로의 Restore 후 Final E2E 결과가 남아 있다. [실행 보고](https://github.com/321Team/fds-project-baseline/issues/21#issuecomment-5677777537)

---

# 검증 및 증적

- Backup Command/Checksum
- Restore Log
- Row Count/Sample Query
- Final E2E
- Backup/Restore Runbook
- Evidence Path: `321Team/fds-project-evidence:evidence/P1-DR-01/`

---

# Dependency

- **Blocked By:** P1-DB-01, P1-E2E-01 Initial
- **Blocks / Next:** P1-DOC-01
- **Related Ticket:** P1-APP-01
- **Milestone:** G3 Review Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D04
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-05; RISK-09
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** In Progress
- **Exit Criteria:** pg_dump Backup, 승인된 초기화/격리 환경 Restore, Row/Rule 결과 정합성 및 Restore 후 Final E2E PASS와 Runbook 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `a2df04100634e4d73d5e8652897955597e211ca9dd59b43be1c4a92bba24be20`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P1-DR-01 -->
# P1-DR-01 — PostgreSQL Backup / Restore

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-DR-01 |
| Phase | Phase 1 |
| Category | DR / Data Recovery |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-10 |
| End | 2026-09-13 |
| Calendar Days | 4 |
| Working Days | 2 |
| Lead | 이재환 |
| Support | 이권욱 |
| Exit Criteria | pg_dump Backup, 승인된 초기화/격리 환경 Restore, Row/Rule 결과 정합성 및 Restore 후 Final E2E PASS와 Runbook 확보 |
| Related Decision IDs | D04 |
| Related Risk IDs | RISK-05; RISK-09 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Network_Baseline_v2.3; FDS_Phase1_Logical_Architecture_v3.1.2; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | Harbor Restore와 etcd Snapshot/Restore는 P1이다. 운영 데이터 삭제 없이 별도 Restore DB 또는 승인 절차를 사용한다. |

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

데이터 담당자로서 PostgreSQL 논리 Backup으로 거래·FDS 데이터를 복구한다. 이를 통해 단일 DB 구조에서도 최소 복구 가능성과 절차 재현성을 입증한다.

---

# 📌 Scope

## In Scope

- pg_dump
- Backup Integrity
- pg_restore
- Row/Schema 검증
- Restore 후 E2E
- Runbook

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 📋 핵심 요구사항

- [ ] Backup 시점과 Source DB Version을 기록한다.
- [ ] 운영성 원본을 직접 덮어쓰지 않는다.
- [ ] Schema와 Data 복구 순서를 명시한다.
- [ ] Credential과 Backup 파일 접근권한을 통제한다.

---

# ✅ Acceptance Criteria

- [ ] Backup 파일이 정상 생성되고 검증된다.
- [ ] 빈 Restore 대상에 Schema/Data가 복구된다.
- [ ] 대표 Transaction/FDS Result가 일치한다.
- [ ] Restore 후 E2E가 통과한다.

---

# 🧪 검증 및 증적

- Backup Command/Checksum
- Restore Log
- Row Count/Sample Query
- Final E2E
- Backup/Restore Runbook
- Evidence Path: `docs/evidence/P1-DR-01/`

---

# 🔗 Dependency

- **Blocked By:** P1-DB-01, P1-E2E-01 Initial
- **Blocks / Next:** P1-DOC-01
- **Related Ticket:** P1-APP-01
- **Milestone:** G3 Review Ready

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D04
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-05; RISK-09
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** pg_dump Backup, 승인된 초기화/격리 환경 Restore, Row/Rule 결과 정합성 및 Restore 후 Final E2E PASS와 Runbook 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>
