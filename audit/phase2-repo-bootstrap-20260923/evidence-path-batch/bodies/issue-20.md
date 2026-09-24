<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P1-E2E-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P1-E2E-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 현재 API/Rule/실패·Negative의 고정 기대값과 정본 E2E 연결 ; A04/A05. Critical 0·증적 승인 유지.

- 정상·4개 Rule·엔진 timeout/오류·DB 저장 실패·미승인 Source/경로·복구마다 고정 입력/기대 HTTP·DB row/result·metric·실제환경/소스 SHA를 연결한다. 201 자원 생성과 업무 승인/송금을 구분하며 #4~6 유예 기능을 케이스에 자동 추가하지 않는다.

**현재 앱·Rule·시간 계약 (A04)** — 앱 main `01758583c03bcbf45c96eb9d7b868cee4a2ed9df`를 현재 접근 가능한 소스로 연결한다. 계약 v1.0은 DRAFT·실패정책 OPEN·옛 Probe/P1-MSA-01 표기가 남아 있다. 구현의 엔진 실패 fail-open(connect1s/read2s), DB 실패 rollback/HTTP500, R04 KST01:00≤시각<05:00·100만원 이상을 소스/fixture/승인 근거와 대조한다. UTC 전송·KST 판정은 양립 가능하다. 입력 offset/naive 처리·DB timezone·저장 자료형·표시 기준을 분리해 기록하며 새 정책 승인으로 간주하지 않는다.
근거: [계약](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/docs/transaction-api_fds-engine_contract_v1.0.md) · [Rule](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/fds-engine/app/rules.py) · [API](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/transaction-api/app/main.py) · [client](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/transaction-api/app/fds_client.py)

**인계·관련 티켓:** [#11](https://github.com/321Team/fds-project-baseline/issues/11) · [#15](https://github.com/321Team/fds-project-baseline/issues/15) · [#17](https://github.com/321Team/fds-project-baseline/issues/17) · [#22](https://github.com/321Team/fds-project-baseline/issues/22).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P1-E2E-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P1-E2E-01 -->
# P1-E2E-01 — Initial / Final E2E & Regression

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-E2E-01 |
| Phase | Phase 1 |
| Category | QA / Integration Test |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-11 |
| End | 2026-09-22 |
| Calendar Days | 12 |
| Working Days | 4 |
| Lead | 이재환 |
| Support | 이권욱, 이하영 |
| Exit Criteria | Client→edge→transaction-api→fds-engine→PostgreSQL→Prometheus E2E, Rule·Negative·Regression PASS, Critical Issue 0 및 Evidence 승인 |
| Related Decision IDs | D03; D05; D17; D18 |
| Related Risk IDs | RISK-05; RISK-07; RISK-09 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #20 snapshot 2026-09-10T04:08:25Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | 09-11은 케이스·명령·판정 기준 준비일, Runtime은 09-18 이후, 최종 회귀는 09-22 오전이다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T04:08:25Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.
- 수집된 운영 댓글은 원래 위치에 보존한다. 신규 구현 제출/리뷰 요청은 실행 PASS나 승인으로 간주하지 않는다.
  - [5612849293](https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-5612849293) · 2026-09-10T04:08:25Z

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

담당자 보고 기준 미착수 / NOT RUN. 정본 3CP+3Worker, Stage B, App 배포와 기존 Initial/Final E2E·Regression 증적이 필요하다. 단일노드 개별 실증을 통합 E2E로 인정하지 않는다. Decision #4~6의 신규 기능 유예와 기존 실패 경로·보안 부정시험 경계는 유지한다. 현재 후보 Plan: 2026-09-11 ~ 2026-09-22 (권장안; 실제 완료일·Gate 승인은 미확정).

근거: [Issue #20](https://github.com/321Team/fds-project-baseline/issues/20), Issue 갱신 시각 `2026-09-10T04:08:25Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- [후속 기록](https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-5612849293)

---

# User Story

QA 담당자로서 Phase 1 전체 업무 흐름과 보안 실패 경로를 검증한다. 이를 통해 개별 구성 성공이 아니라 사용자 거래 기준의 통합 완료를 증명한다.

---

# Scope

## In Scope

- Initial/Final E2E
- 4 Rule
- DB Persistence
- Metrics
- Negative Test
- Regression
- Defect

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] 테스트 데이터와 Expected Result를 사전 정의한다.
- [ ] Positive와 Negative 경로를 분리한다.
- [ ] Transaction ID로 API/DB/Metric Evidence를 연결한다.
- [ ] Critical Issue는 Review 전 0건이어야 한다.
- [ ] 실패 재현과 수정 버전을 기록한다.

---

# Acceptance Criteria

- [x] 정상 거래 E2E가 성공한다.
- [x] R01/R02/R04/R07 기대결과가 일치한다.
- [x] 비인가 DB/Management 접근이 차단된다.
  - **DB(비인가 앱 접근)**: fds-engine → db01:5432가 K8s NetworkPolicy Default-Deny로 차단됨(fds-engine은 `allow-transaction-api-to-db` selector에서 제외 — 의도적 설계). pg_hba.conf도 `fdsdb/fds_app`을 worker01·02·03·edge01(`.105/.107/.108/.50`) 4개 IP로만 제한. 근거: [S1/TC-NET-DB, 2026-09-23 원인 규명](https://claude.ai/artifact/UCatzSQWiTdLxHXzeABRhe).
  - **Management(비인가 SSH)**: db01 firewalld `public` zone rich-rule로 SSH를 `10.1.93.29`·`10.1.93.23`·`10.250.10.10`(ansible01) 3개 소스로만 허용, services 목록엔 ssh 없음 — 그 외 소스는 zone 기본 정책(REJECT)으로 차단. K8s 6노드 SSH도 동일하게 Gate2 A1에서 ansible01 단일 소스만 허용 확인(9/22 PASS).
- [ ] DB 저장과 Metrics가 동일 거래를 반영한다.
- [ ] Regression 결과와 Defect 상태가 승인된다.

---

# 검증 및 증적

- Test Case/Expected
- API Request/Response
- FDS Rule Result
- DB Query
- Prometheus Query
- Defect/Regression Report
- Evidence Path: `321Team/fds-project-evidence:evidence/P1-E2E-01/`

---

# Dependency

- **Blocked By:** P1-APP-01, P1-CICD-01, P1-SEC-01, P1-MON-01
- **Blocks / Next:** P1-HA-01, P1-DR-01, P1-DOC-01
- **Related Ticket:** 전체 Phase 1 P0
- **Milestone:** G3 Review Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D03; D05; D17; D18
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-05; RISK-07; RISK-09
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** Client→edge→transaction-api→fds-engine→PostgreSQL→Prometheus E2E, Rule·Negative·Regression PASS, Critical Issue 0 및 Evidence 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `be9c6750be56d1f8ff84c4d56d437dcb6749af834b87774a5e7fea6d74cab856`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P1-E2E-01 -->
# P1-E2E-01 — Initial / Final E2E & Regression

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-E2E-01 |
| Phase | Phase 1 |
| Category | QA / Integration Test |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-09 |
| End | 2026-09-18 |
| Calendar Days | 10 |
| Working Days | 4 |
| Lead | 이재환 |
| Support | 이권욱, 이하영 |
| Exit Criteria | Client→edge→transaction-api→fds-engine→PostgreSQL→Prometheus E2E, Rule·Negative·Regression PASS, Critical Issue 0 및 Evidence 승인 |
| Related Decision IDs | D03; D05; D17; D18 |
| Related Risk IDs | RISK-05; RISK-07; RISK-09 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Network_Baseline_v2.3; FDS_Phase1_Logical_Architecture_v3.1.2; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 이재환 09-14~09-17 부재 중 지원자가 Evidence 정리와 결함 추적을 수행하고, 최종 판정은 09-18 복귀 후 완료한다. |

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

QA 담당자로서 Phase 1 전체 업무 흐름과 보안 실패 경로를 검증한다. 이를 통해 개별 구성 성공이 아니라 사용자 거래 기준의 통합 완료를 증명한다.

---

# 📌 Scope

## In Scope

- Initial/Final E2E
- 4 Rule
- DB Persistence
- Metrics
- Negative Test
- Regression
- Defect

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 📋 핵심 요구사항

- [ ] 테스트 데이터와 Expected Result를 사전 정의한다.
- [ ] Positive와 Negative 경로를 분리한다.
- [ ] Transaction ID로 API/DB/Metric Evidence를 연결한다.
- [ ] Critical Issue는 Review 전 0건이어야 한다.
- [ ] 실패 재현과 수정 버전을 기록한다.

---

# ✅ Acceptance Criteria

- [ ] 정상 거래 E2E가 성공한다.
- [ ] R01/R02/R04/R07 기대결과가 일치한다.
- [ ] 비인가 DB/Management 접근이 차단된다.
- [ ] DB 저장과 Metrics가 동일 거래를 반영한다.
- [ ] Regression 결과와 Defect 상태가 승인된다.

---

# 🧪 검증 및 증적

- Test Case/Expected
- API Request/Response
- FDS Rule Result
- DB Query
- Prometheus Query
- Defect/Regression Report
- Evidence Path: `docs/evidence/P1-E2E-01/`

---

# 🔗 Dependency

- **Blocked By:** P1-APP-01, P1-CICD-01, P1-SEC-01, P1-MON-01
- **Blocks / Next:** P1-HA-01, P1-DR-01, P1-DOC-01
- **Related Ticket:** 전체 Phase 1 P0
- **Milestone:** G3 Review Ready

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D03; D05; D17; D18
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-05; RISK-07; RISK-09
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** Client→edge→transaction-api→fds-engine→PostgreSQL→Prometheus E2E, Rule·Negative·Regression PASS, Critical Issue 0 및 Evidence 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>

