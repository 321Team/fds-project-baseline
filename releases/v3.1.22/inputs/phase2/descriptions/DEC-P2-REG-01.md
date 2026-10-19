<!-- cost-review-20261012:start -->
## 비용 책임·리뷰 적용 기준 — 2026-10-12 사용자 결정

[중앙 기준 및 과거 리뷰 정정](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6119458420)을 적용합니다. 아래 과거 본문/댓글의 비용 요구와 다르면 이 기준으로 책임·제출 범위를 해석합니다.
- **교육장 리포트 확보·사용액/예상 총액·비용 GO/중단 판단: 이권욱.** 구축 담당자는 예상 자원/수량·대략 가동/정리안·잔존 자원·변경 사항을 기존 자료로 인계합니다.
- 자체 단가표·상세 재견적·모든 절감안·사전 actual ID 전수 확정을 요구하지 않습니다. 비용 대기만으로 준비 산출물을 반려하지 않습니다.
- D22의 gross/transfer cost·비용 영향란은 기술 입력과 권욱의 중앙 비용 판단 링크로 연결합니다. 별도 단가 계산서를 담당자 완료조건으로 요구하지 않습니다.
- 현재 단계의 필수 기술 검증만 차단조건으로 적용합니다. 기존 증적/승인은 재사용하고 변경 영향만 재검토합니다. Terraform Plan은 실제 변경 검증이며 다른 도구에 일률 요구하지 않습니다.
- 기존 한도·유효 승인 범위·독립 리뷰·무결성/추적성/재현성/이식성 및 Phase 1 운영/AC 경계를 유지합니다. 새 비용·Apply·Create·삭제 GO나 티켓 종결이 아닙니다.
<!-- cost-review-20261012:end -->

<!-- fds-canonical-live:v3.1.21 record-id:DEC-P2-REG-01:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/DEC-P2-REG-01.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 관련 추적 항목 **TS08**. 원본 AC와 각 항목의 환경·선행조건·중단/복구·증적 기준을 함께 적용한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:DEC-P2-REG-01:end -->

<!-- phase2-decision-data-20261002:issue-42:v1:start -->
## 2026-10-02 Decision Data Contract — #42

### Ownership
- **Decision Lead:** 이권욱
- 이하영: ROSA/Trust/Security 입력 제공
- 이재환: APP/Hybrid 소비 관점 입력 제공
- 최종 Decision은 Lead가 기록하되, 자기 산출물에 독립 검토가 필요한 Code/Evidence가 포함되면 다른 팀원이 해당 산출물만 리뷰한다.

### Confirmed inputs
- Cloud Registry 비용 산정 Region: `ap-northeast-2`
- #38 Basic Ready의 Route/TLS/Credential prerequisite를 소비
- Phase 1 Harbor는 CA/Robot/Digest/Source allowlist 경계가 존재
- Shared OCP pull PASS는 ROSA Registry 경로 승인으로 승격하지 않음

### Final Decision에서 반드시 고정할 출력값
1. `REGISTRY_MODE` = Harbor 또는 승인 Cloud Registry
2. endpoint / project(repository) naming
3. push principal / pull principal / 최소권한
4. CA/trust 또는 public trust 방식
5. immutable digest 기준 및 tag 사용 규칙
6. Runner push path
7. ROSA pull path
8. fallback 조건 및 장애 시 사용 경로
9. 예상 gross cost / transfer cost / Cost Gate 영향
10. #43/#46이 소비할 credential **reference** (credential 원문 금지)
11. Decision evidence/source refs
12. `D22=GO:<mode>|NO_GO`

한 항목이라도 빠진 상태는 Final Decision이 아니며 #43/#46은 임의 Registry를 선택하지 않는다.

### 현재 Checkpoint
`REGION_INPUT=CONFIRMED / REGISTRY_MODE=PENDING / D22=PENDING / APP_CICD_HANDOFF=NOT_READY`
<!-- phase2-decision-data-20261002:issue-42:v1:end -->

<!-- issue-execution-contract-20261001:v1:start -->
## 2026-10-01 Registry Decision Contract v1

### Entry
- #38 Basic Ready의 Route/TLS/Credential 전제 수신.
- Phase 1 Harbor의 실제 CA/Robot/Digest 경계와 Cloud Registry 선택지 비교.

### 선택 기준
- Commit/Image Digest 추적성, Pull Route/TLS, Credential 최소권한, Hybrid 장애시 fallback, 비용/일정을 동일 기준으로 비교.
- Shared OCP pull 성공만으로 ROSA Registry 경로를 승인하지 않는다.

### Exit
10-15에 단일 Primary Source + Fallback + credential owner + #43/#46/#47 소비조건을 기록한다.
<!-- issue-execution-contract-20261001:v1:end -->

<!-- shared-ocp-boundary-20261001:start -->
## 2026-10-01 공용 OCP Lab 실행경계

교육기관 제공 OCP는 **공용 Multi-tenant Lab**으로 사용한다. Cluster/Node 독점은 전제하지 않으며, 이 환경의 결과는 기본적으로 `LAB-PRECHECK`이다.

### 공통 자원·명명 규칙
- 사람 간 Team Code는 `J1`, `J2` 형식으로 관리하되 Kubernetes Namespace 실제 이름은 소문자 DNS 형식으로 매핑한다.
- Namespace: `j1-<purpose>`, `j2-<purpose>` 형식. 예: `j1-fds-app`, `j1-monitoring`, `j1-cicd-test`.
- Team Code 미배정 상태에서는 문서 템플릿에 `jX-<purpose>`를 사용하고 실제 생성 전에 코드와 Owner를 고정한다.
- 생성 자원에는 최소 `team`, `project=fds-hybrid`, `purpose` label을 부여하고, Owner/만료일은 annotation 또는 동등 추적정보로 남긴다.
- ResourceQuota/LimitRange의 **정확한 수치**는 공용 OCP 관리자 정책을 따른다. 임의로 quota를 확대하거나 다른 조의 자원을 침범하지 않는다.

### 허용/금지 경계
- 허용: Namespace-local Deployment/Service/Route, namespace RBAC, NetworkPolicy, SecurityContext, manifest/schema, health, image pull, 이미 제공된 Operator의 허용 범위 내 namespace-local CR 사전검증.
- 금지/사전승인 필요: 신규 cluster-wide Operator 설치, CRD/ClusterRole/SCC/MachineConfig/Node 설정 변경, cluster-admin 사용, Node 전용 affinity/taint로 사실상 독점, hostNetwork/hostPort/privileged의 임의 사용, Node reboot/drain·장애주입·대규모 load/performance/HA 시험.
- 공용 OCP의 다른 사용자 workload 영향을 받는 성능·용량·HA 수치는 **인수 증적이 아니다**.

### Evidence / Cleanup
- 증적에는 `ENV=SHARED_OCP_LAB`, Cluster/Version, Team Code, Namespace, 실행시각, manifest/source SHA, 명령/RC/원본 로그를 포함한다.
- 공용 OCP PASS를 ROSA Runtime PASS로 승격하지 않는다. ROSA P0 인수조건은 실제 ROSA에서 재검증한다.
- 시험 종료 시 자기 Team Namespace/자원만 정리하고, 삭제 전/후 resource inventory를 보존한다.
<!-- shared-ocp-boundary-20261001:end -->

### 이 티켓 적용
공용 OCP의 image pull/Route/TLS/Credential 확인은 호환성 Precheck이다. 최종 Registry Source와 Pull Route/TLS/Credential Acceptance는 실제 ROSA 조건으로 확정한다.



<!-- schedule-realign-20261001:issue-42:start -->
## 2026-10-01 일정·Dependency 정합화

- **Final-decision gate:** Harbor vs Cloud Registry 비교자료는 사전 준비 가능하나, 최종 선택은 #38 Basic Ready의 Route/TLS/Credential 전제를 확인한 뒤 10-15 확정한다.

- Scope/AC/Priority/Milestone/Review Authority 변경 없음.
- 일정 조정은 재현성·무결성·추적성을 유지하면서 P0 동시 WIP와 선행조건 역전을 제거하기 위한 PMO 조정이다.
<!-- schedule-realign-20261001:issue-42:end -->
<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/DEC-P2-REG-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/DEC-P2-REG-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 조건부 결정. Harbor 또는 Cloud Registry·Digest/Trust/경로/비용/Fallback을 D22로 기록.

**인계·관련 티켓:** [#38](https://github.com/321Team/fds-project-baseline/issues/38) · [#43](https://github.com/321Team/fds-project-baseline/issues/43) · [#47](https://github.com/321Team/fds-project-baseline/issues/47).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:DEC-P2-REG-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:DEC-P2-REG-01 -->
# DEC-P2-REG-01 — ROSA Image Registry Source Decision

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-P2-REG-01 |
| Phase | Phase 2 |
| Category | Architecture / Registry |
| Type | Decision |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-10-15 |
| End | 2026-10-15 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | ROSA Image Source를 On-Prem Harbor 또는 승인 Cloud Registry로 확정하고 Route·TLS·Credential·비용·Fallback을 승인 |
| Related Decision IDs | D22 |
| Related Risk IDs | RISK-06; RISK-10; RISK-11; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #42 snapshot 2026-09-09T12:08:53Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 사전 Option 분석은 준비자료로만 수행하고, 최종 D22 결정은 10-15 #38 Basic Ready 실측 입력을 확인한 뒤 당일 확정한다. #43은 이 결정 이후 착수한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-09T12:08:53Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #42](https://github.com/321Team/fds-project-baseline/issues/42), Issue 갱신 시각 `2026-09-09T12:08:53Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Registry·OpenShift 담당자로서 ROSA가 사용할 이미지 원본을 확정한다. 이를 통해 불필요한 Hybrid Registry 의존성을 피하면서 Commit/Image 추적성을 유지한다.

---

# Scope

## In Scope

- Harbor vs Cloud Registry 비교
- Route/TLS
- Credential
- 비용
- Image Promotion
- Fallback

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] Phase 1 Image와 Digest 추적성을 유지한다.
- [ ] Private Credential을 Secret으로 관리한다.
- [ ] Hybrid 장애 시 배포 지속 가능성을 비교한다.
- [ ] 선택안의 보안·비용·일정 영향을 기록한다.

---

# Acceptance Criteria

- [ ] 단일 Image Source와 Fallback이 승인된다.
- [ ] Pull Route/TLS/Credential Test가 정의된다.
- [ ] P2-APP/HYB WBS와 Interface IF-19 상태가 갱신된다.

---

# 검증 및 증적

- Option 비교표
- Pull Connectivity Test
- Credential/TLS 계획
- Decision D22
- 갱신 WBS/Interface
- Evidence Path: `321Team/fds-project-evidence:evidence/DEC-P2-REG-01/`

---

# Dependency

- **Blocked By:** P2-ROSA-01 Basic Ready checkpoint
- **Blocks / Next:** P2-APP-01, P2-HYB-01
- **Related Ticket:** P1-HBR-01
- **Milestone:** G5 ROSA Application Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D22
- **Decision Control:** D22에서 Harbor 사용 여부와 N/A 조건을 명확히 기록한다.
- **Related Risk IDs:** RISK-06; RISK-10; RISK-11; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** ROSA Image Source를 On-Prem Harbor 또는 승인 Cloud Registry로 확정하고 Route·TLS·Credential·비용·Fallback을 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `6108be4c4e21c9bac3f9b38120edc7efb23a7b8242f84990a131ed895e856be2`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:DEC-P2-REG-01 -->
# DEC-P2-REG-01 — ROSA Image Registry Source Decision

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | DEC-P2-REG-01 |
| Phase | Phase 2 |
| Category | Architecture / Registry |
| Type | Decision |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-12 |
| End | 2026-10-16 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | ROSA Image Source를 On-Prem Harbor 또는 승인 Cloud Registry로 확정하고 Route·TLS·Credential·비용·Fallback을 승인 |
| Related Decision IDs | D22 |
| Related Risk IDs | RISK-06; RISK-10; RISK-11; RISK-12 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Phase1_Logical_Architecture_v3.1.2; Phase 2 OCI/AWS/ROSA Design; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 기준선의 ROSA→Harbor는 Optional이다. P2-APP-01 최종 Image 경로 전 10-16까지 확정한다. |

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

Registry·OpenShift 담당자로서 ROSA가 사용할 이미지 원본을 확정한다. 이를 통해 불필요한 Hybrid Registry 의존성을 피하면서 Commit/Image 추적성을 유지한다.

---

# 📌 Scope

## In Scope

- Harbor vs Cloud Registry 비교
- Route/TLS
- Credential
- 비용
- Image Promotion
- Fallback

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 📋 핵심 요구사항

- [ ] Phase 1 Image와 Digest 추적성을 유지한다.
- [ ] Private Credential을 Secret으로 관리한다.
- [ ] Hybrid 장애 시 배포 지속 가능성을 비교한다.
- [ ] 선택안의 보안·비용·일정 영향을 기록한다.

---

# ✅ Acceptance Criteria

- [ ] 단일 Image Source와 Fallback이 승인된다.
- [ ] Pull Route/TLS/Credential Test가 정의된다.
- [ ] P2-APP/HYB WBS와 Interface IF-19 상태가 갱신된다.

---

# 🧪 검증 및 증적

- Option 비교표
- Pull Connectivity Test
- Credential/TLS 계획
- Decision D22
- 갱신 WBS/Interface
- Evidence Path: `docs/evidence/DEC-P2-REG-01/`

---

# 🔗 Dependency

- **Blocked By:** P2-ROSA-01 기본 Ready
- **Blocks / Next:** P2-APP-01, P2-HYB-01
- **Related Ticket:** P1-HBR-01
- **Milestone:** G5 ROSA Application Ready

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D22
- **Decision Control:** D22에서 Harbor 사용 여부와 N/A 조건을 명확히 기록한다.
- **Related Risk IDs:** RISK-06; RISK-10; RISK-11; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** ROSA Image Source를 On-Prem Harbor 또는 승인 Cloud Registry로 확정하고 Route·TLS·Credential·비용·Fallback을 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>
