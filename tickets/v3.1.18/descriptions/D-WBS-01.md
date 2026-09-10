<!-- fds-canonical-description:v3.1.18 record-id:D-WBS-01 -->
# D-WBS-01 — WBS / Backlog / Interface Management Freeze

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | D-WBS-01 |
| Phase | 원본 속성 미확인 |
| Category | 원본 속성 미확인 |
| Type | 원본 속성 미확인 |
| Status | Done |
| Priority | 원본 속성 미확인 |
| Start | 원본 속성 미확인 |
| End | 원본 속성 미확인 |
| Calendar Days | 원본 속성 미확인 |
| Working Days | 원본 속성 미확인 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | 3인 WBS, Backlog, Decision / Milestone, Interface Register, 의존성, Exit Criteria, 상태 및 변경통제 기준 Freeze; 최신 WBS와 Notion 수동 입력본 배포 |
| Related Decision IDs | D01`~`D24 |
| Related Risk IDs | RISK-05`, `RISK-13 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #61 snapshot 2026-09-09T12:15:55Z |
| Schedule Note | 원본 속성 미확인 |

## 현재 실행·검토 상태

D-WBS-01 Done/2026-08-26 유지. FUP-07 WBS 참조 편입은 완료됐으나 당시 개인별 승인 회신·시각 및 WBS 바이너리 실제 열람 확인은 잔여다. 원본 미확인 속성과 기존 승인 범위를 임의 확정하지 않는다.

근거: [Issue #61](https://github.com/321Team/fds-project-baseline/issues/61), Issue 갱신 시각 `2026-09-09T12:15:55Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.

---

# User Story

PMO 및 프로젝트 관리 담당자로서 3인 프로젝트의 전체 일정, 업무분장, Backlog, Decision, Milestone, Dependency, Exit Criteria 및 Interface 관리체계를 동결한다.

이를 통해 각 티켓의 책임·선후행·완료조건·증적을 동일한 기준으로 관리하고, 종결 티켓과 Remaining Backlog를 분리하며, 설계 동결 이후 변경을 추적 가능한 Change Request로 통제한다.

---

# Scope

## In Scope

- 2026-08-24 착수부터 2026-10-26 Project Close까지 Phase 1 / Phase 2 WBS와 Milestone 기준 수립
- 이권욱·이하영·이재환 3인의 Lead / Support 업무분장과 인수인계 기준 수립
- P0 / P1 / Scope Out 우선순위와 Gate 차단 여부 구분
- Task / Decision / Milestone 유형, 상태, 일정, 의존성, Exit Criteria 및 Evidence 기준 수립
- Decision Register, Risk Register, Closed Ticket Register 및 Interface Freeze Register 연계
- Notion 수동 입력용 17개 데이터 속성 정의
- 신규 티켓용 고정 Description 템플릿 정의
- 종결 티켓 제외 원칙과 Remaining Backlog 갱신·배포 절차 확정
- Freeze 이후 일정·범위·인터페이스·우선순위 변경에 대한 Change Request 통제 확정

## Out of Scope

- 개별 구현 티켓의 기술 작업 수행 또는 완료 판정 대행
- `D-SEC-01` 승인권자·검토 범위·Exit Criteria 결정 — Lead 이하영은 확정
- `D17` 등 미결 Decision의 선택안 승인
- G0 전체의 무조건부 종결 선언
- Remaining Backlog의 후속 실행 결과 보장

---

# 핵심 요구사항

- [x] 전체 프로젝트 일정을 Phase, Gate, Review, Close 기준으로 구조화한다.
- [x] 각 레코드에 `Record ID`, `Phase`, `Category`, `Type`, `Status`, `Priority`, `Start`, `End`, `Calendar Days`, `Working Days`, `Lead`, `Support`, `Exit Criteria`, `Related Decision IDs`, `Related Risk IDs`, `Source`, `Schedule Note`를 적용한다.
- [x] 의사결정이 필요한 항목은 Milestone Description에 묻지 않고 별도 `Type=Decision` 레코드로 관리한다.
- [x] 각 Task의 `Blocked By`, `Blocks / Next`, Related Ticket 및 Milestone을 식별한다.
- [x] 단순 구현 완료가 아니라 Exit Criteria와 Evidence 확인 후에만 `Status=Done`을 적용한다.
- [x] 종결 티켓은 Closed Ticket Register에 보존하고 Remaining Backlog에서 제외한다.
- [x] 신규 티켓 Description은 `User Story`, `Scope`, `핵심 요구사항`, `Acceptance Criteria`, `검증 및 증적`, `Dependency`, `Decision / Risk Control`, `Completion Record` 순서로 고정한다.
- [x] Interface의 Endpoint, Port, Protocol, Contract, Owner, Acceptance 및 State를 관리한다.
- [x] P1 미완료는 해당 P0 Gate를 자동 차단하지 않으며 Owner, Due, Known Issue를 남긴다.
- [x] 휴가·비근무일·주말 Review는 Schedule Note, Support 인계 및 Decision 레코드로 통제한다.

---

# Acceptance Criteria

- [x] 3인 Lead / Support와 Phase 1·2 업무분장이 WBS에 반영되었다.
- [x] 프로젝트 착수, G0~G6, Phase Review, Deliverable Freeze 및 Project Close 일정이 정의되었다.
- [x] Task / Decision / Milestone이 구분되고, 의사결정 필요 건에 `Decision` 항목이 포함되었다.
- [x] 각 Backlog 레코드에 17개 Notion 데이터 속성과 측정 가능한 Exit Criteria가 정의되었다.
- [x] 신규 티켓용 상세 Description 고정 템플릿이 배포되었다.
- [x] 주요 Producer / Consumer 경로가 Interface Freeze Register에 등록되고 변경통제 규칙이 정의되었다.
- [x] `D-ARC-01`, `D-NET-01`, `D-WBS-01`, `P1-LNX-01`이 Closed Ticket Register에 기록되고 Remaining Backlog에서 제외되었다.
- [x] Remaining Backlog, Decision / Milestone, Closed / Decision / Risk Register가 최신 사양 기준으로 재정비되었다.
- [x] `D-SEC-01`은 완료로 처리하지 않고 `Decision / IN PROGRESS / Lead 이하영`으로 분리되었다.
- [x] 최신 WBS와 Notion 수동 입력본이 동일한 ID·상태·일정·의존성·Exit Criteria 기준으로 배포되었다.

---

# 검증 및 증적

- `FDS_Project_Implementation_Baseline_v3.1.4.md`
  - Closed Ticket Register / Remaining Backlog Authority
  - Backlog Freeze Rules
  - Gate Exit Criteria
  - Decision Register
  - Interface Freeze Register / Interface Change Control
  - Project Status Register
- `FDS_Remaining_Backlog_WBS_v3.1.4.xlsx`
  - Overview
  - Remaining Backlog
  - Decision & Milestone
  - Closed Register
  - Decision Register
  - Risk Register
  - Code Lists
  - Description Template
- `FDS_Notion_Remaining_Backlog_Manual_v1.1.md`
  - 17개 Notion 속성
  - 종결 제외 목록
  - 고정 Description 템플릿
  - 상세 Remaining Backlog / Decision / Milestone 입력본
- `FDS_Network_Baseline_v2.3.md`
- `FDS_Phase1_Logical_Architecture_v3.1.2.mmd`
- `FDS_Phase1_Physical_Architecture_v3.1.2.mmd`

---

# Dependency

- **Blocked By:** `D-ARC-01`, `D-NET-01` — `DONE / CLOSED`
- **Blocks / Next:** Remaining Backlog의 Phase 1·2 Task / Decision / Milestone 실행 및 상태관리
- **Related Ticket:** 모든 WBS 레코드; `D-SEC-01`은 별도 Governance Decision으로만 연계
- **Milestone Contribution:** G0의 Architecture / Network / WBS 항목 중 WBS `PASS`

---

# Decision / Risk Control

- **Related Decision IDs:** `D01`~`D24`
- **Decision Control:** `D01`~`D16`의 확정·선택 상태, `D17`의 In Progress / Owner Assigned 상태와 `D18`~`D24`의 Decision Required / Scheduled 상태를 구분해 기록한다. 미결 Decision은 별도 `Type=Decision` 레코드의 승인 전까지 완료로 간주하지 않는다.
- **Related Risk IDs:** `RISK-05`, `RISK-13`
- **Risk Control:** 3인 일정, 휴가·비근무일 및 주말 Review 리스크는 Lead / Support 인계, 중간 Evidence, Schedule Note, `D20` / `D24` 일정 Decision으로 통제한다.
- **Change Control:** Freeze 이후 P0 범위, 우선순위, 일정, 의존성, Exit Criteria, Interface 또는 Owner 변경은 Change Request와 영향도 검토 후 새 Version에 반영한다.

---

# Completion Record

- **Result:** `PASS`
- **Status:** `DONE`
- **Ticket Gate:** `CLOSED`
- **Exit Criteria:** 3인 WBS, Backlog, Decision / Milestone, Interface Register, 의존성, Exit Criteria, 상태 및 변경통제 기준 Freeze; 최신 WBS와 Notion 수동 입력본 배포
- **Completed Date:** `2026-08-26`
- **Reviewer / Approver:** 프로젝트 공통 검토 및 Baseline 승인 기록 참조
- **Closure Basis:** `FDS_Project_Implementation_Baseline_v3.1.4`, `FDS_Remaining_Backlog_WBS_v3.1.4.xlsx`, `FDS_Notion_Remaining_Backlog_Manual_v1.1.md`
- **Closure Boundary:** 본 티켓의 종결은 WBS / Backlog 관리체계의 동결을 의미한다. `D-SEC-01`은 `IN PROGRESS / Lead 이하영`, 관련 `D17`은 Scope·Approver·Exit Criteria 검토 중이며, G0 Design Freeze는 `CONDITIONAL PASS`다. 이후 Backlog 갱신은 D-WBS-01 재개가 아니라 동결된 Change Control에 따른 Version Update로 관리한다.
- **Next:** Remaining Backlog 실행 및 Evidence 기반 상태 갱신

## 담당자 속성 복원 근거 (2026-09-09)

`FDS_Project_Implementation_Baseline_v3.1.2.md` §3.1 Frozen WBS의 해당 Record ID 행에서 Lead 이권욱 / Support 이하영, 이재환을 확인했다. 본문 17개 속성 항목을 유지하고 Lead·Support만 복원했다. Type의 원본 값은 해당 표에 없어 `원본 속성 미확인`을 유지한다. 이후 정본의 완료 이력과 충돌하는 과거 D-SEC/G0 상태는 이번 복원의 근거로 사용하지 않았다.
