<!-- fds-canonical-live:v3.1.21 record-id:P2-APP-01:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/P2-APP-01.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 관련 추적 항목 **TS02, TS03, TS11**. 원본 AC와 각 항목의 환경·선행조건·중단/복구·증적 기준을 함께 적용한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:P2-APP-01:end -->

<!-- phase2-execution-data-20261002:issue-43:v1:start -->
## 2026-10-02 Execution Data / Review Contract — #43

### Ownership
- **Execution Lead / Runtime AC Acceptance:** 이재환
- **PMO/QA Review Owner:** 이권욱
- 이하영은 #38 Platform/Security Producer이며 #43의 상시 Reviewer가 아니다.
- Code/Manifest/Evidence 독립 리뷰는 이권욱 우선; 작성/실행 충돌 시 다른 독립 Reviewer.

### Entry Gate
- #38 `BASIC_READY=YES`
- #42 Final D22 Registry Decision
- portable base/overlay source가 review 가능한 commit으로 존재
- 승인 image digest가 존재

### Portable manifest contract — 현재 미완성
현재 Phase 1 YAML은 migration/reference/security patch에 분산되어 있으므로 그대로 Phase 2 권위 Source로 사용하지 않는다.

#43 구현 전 다음 두 계층을 고정한다.
1. **Portable Kubernetes base**
   - transaction-api / fds-engine Deployment
   - ClusterIP Service
   - Config/Secret **reference**
   - ServiceAccount/RBAC
   - portable SecurityContext
   - health/readiness probe
   - image digest 변수
2. **OpenShift overlay**
   - target Namespace
   - Route(transaction-api만 외부노출)
   - registry pull/trust
   - restricted-v2/arbitrary UID 호환
   - environment NetworkPolicy

### 실행 전 반드시 실제값으로 채울 항목
| 항목 | Source | 현재 |
|---|---|---|
| portable base repo/path/SHA | #43 구현 PR | PENDING |
| transaction-api image digest | #42/#46 source chain | PENDING |
| fds-engine image digest | #42/#46 source chain | PENDING |
| Namespace/SA/RBAC | #38 Basic Ready | PENDING |
| Route host/TLS mode | #38/#43 | PENDING |
| DB endpoint/credential ref | #47 전 단계에서는 dependency ref만 | PENDING |
| Config/Secret key contract | Phase 1 source → portable base | PENDING |
| SecurityContext | #38 PG-03 결과 | **BLOCKED** |
| NetworkPolicy | #38 security handoff | PENDING |

### Runtime PASS
- 두 workload Ready
- transaction-api Route Health 성공
- fds-engine 직접 외부노출 없음
- desired digest == Pod runtime imageID/digest
- DB 연결 전/후 Health와 Rule 결과를 구분
- 4 Rule smoke(R01/R02/R04/R07) 결과 및 raw evidence

### Handoff
- #46: deploy target/API/Namespace/digest/health contract
- #47: app endpoint + DB dependency + route/security state

### 현재 Checkpoint
`PORTABLE_BASE=NOT_READY / PG03=HOLD / BASIC_READY=PENDING / D22=PENDING / APP_RUNTIME=NOT_RUN`
<!-- phase2-execution-data-20261002:issue-43:v1:end -->

<!-- issue-execution-contract-20261001:v1:start -->
## 2026-10-01 App Deployment Contract v1

### Entry
- #38 Basic Ready
- #42 Registry Decision
- Phase 1의 transaction-api/fds-engine Image/Contract exact reference

### Success
- 승인 Namespace에서 동일 계약의 image digest를 배포.
- Route/Health/기본 거래 Rule과 실제 Pod imageID를 확인.
- 변경이 필요하면 Phase 1 Contract를 암묵적으로 변형하지 않고 차이를 기록한다.

### Stop / Rollback
- image digest 불일치, readiness 상실, 보안예외 필요, 데이터 계약 변경이 발생하면 중단.
- 이전 승인 deployment/image로 복귀 가능한 manifest를 유지한다.

### Handoff
#46에는 deploy target/health/digest를, #47에는 app endpoint/DB dependency를 제공한다.
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
공용 OCP에서는 `jX-fds-app` 계열 Namespace로 App manifest/Route/Health를 선검증할 수 있다. G5 App Acceptance는 실제 ROSA 재배포/Health/Rule 결과가 필요하다.



<!-- schedule-realign-20261001:issue-43:start -->
## 2026-10-01 일정·Dependency 정합화

- **Start gate:** #38 Basic Ready와 #42 Final Registry Decision이 모두 기록된 뒤 착수한다. #38 전체 Security AC가 10-19까지 병행되므로, #43 실행 중 새 보안 예외를 임의로 만들지 않는다.

- Scope/AC/Priority/Milestone/Review Authority 변경 없음.
- 일정 조정은 재현성·무결성·추적성을 유지하면서 P0 동시 WIP와 선행조건 역전을 제거하기 위한 PMO 조정이다.
<!-- schedule-realign-20261001:issue-43:end -->
<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P2-APP-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P2-APP-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 계획 단계. P2 승인 Registry/Digest·Namespace/Source·DB/Probe·보안 계약으로 배포 ; A04 후속 참조.

**인계·관련 티켓:** [#38](https://github.com/321Team/fds-project-baseline/issues/38) · [#42](https://github.com/321Team/fds-project-baseline/issues/42) · [#47](https://github.com/321Team/fds-project-baseline/issues/47).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P2-APP-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P2-APP-01 -->
# P2-APP-01 — ROSA Application Deployment

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-APP-01 |
| Phase | Phase 2 |
| Category | Application / OpenShift |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-16 |
| End | 2026-10-19 |
| Calendar Days | 4 |
| Working Days | 2 |
| Lead | 이재환 |
| Support | 이하영 |
| Exit Criteria | Phase 1과 동일한 transaction-api/fds-engine Image/Contract를 ROSA에 배포하고 Route/Health/Rule 기본검증 PASS |
| Related Decision IDs | D03; D22 |
| Related Risk IDs | RISK-06; RISK-07; RISK-11 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #43 snapshot 2026-09-10T02:09:53Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 10-15 #38 Basic Ready + #42 Registry Decision 수신 후 10-16 착수. #38 전체 Security 검증과 병행하되, #43은 승인된 Namespace/RBAC/Registry 경계 밖으로 확장하지 않는다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T02:09:53Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #43](https://github.com/321Team/fds-project-baseline/issues/43), Issue 갱신 시각 `2026-09-10T02:09:53Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

애플리케이션 담당자로서 검증된 Phase 1 MSA를 ROSA에 동일 계약으로 배포한다. 이를 통해 플랫폼 차이를 최소화하고 Hybrid 데이터 경로 검증에 집중한다.

---

# Scope

## In Scope

- transaction-api/fds-engine
- OpenShift Route/Service
- Config/Secret
- Health
- Rule Smoke Test

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] Phase 1 OpenAPI와 Rule 계약을 유지한다.
- [ ] 환경별 Config/Secret을 분리한다.
- [ ] Image Digest/Tag를 추적한다.
- [ ] OpenShift Security 제약을 충족한다.
- [ ] DB 연결 전 Health/Rule Smoke Test를 분리한다.

---

# Acceptance Criteria

- [ ] 두 서비스가 ROSA에서 Ready다.
- [ ] Route를 통한 transaction-api Health가 성공한다.
- [ ] fds-engine이 외부에 직접 노출되지 않는다.
- [ ] 4개 Rule Smoke Test가 통과한다.

---

# 검증 및 증적

- Deployment/Route/Service
- Image Digest
- Health/Rule Test
- Config/Secret Mapping
- Pod Security 상태
- Evidence Path: `321Team/fds-project-evidence:evidence/P2-APP-01/`

---

# Dependency

- **Blocked By:** P2-ROSA-01 Basic Ready checkpoint; DEC-P2-REG-01
- **Blocks / Next:** P2-CICD-01, P2-HYB-01
- **Related Ticket:** P1-APP-01, P2-CICD-01
- **Milestone:** G5 ROSA Application Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D03; D22
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-06; RISK-07; RISK-11
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** Phase 1과 동일한 transaction-api/fds-engine Image/Contract를 ROSA에 배포하고 Route/Health/Rule 기본검증 PASS
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `bbd659b1920f9fe77c28706425a59f8fef2a69c858dda6ced8f752300cd71a6b`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P2-APP-01 -->
# P2-APP-01 — ROSA Application Deployment

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P2-APP-01 |
| Phase | Phase 2 |
| Category | Application / OpenShift |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-12 |
| End | 2026-10-16 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이재환 |
| Support | 이하영 |
| Exit Criteria | Phase 1과 동일한 transaction-api/fds-engine Image/Contract를 ROSA에 배포하고 Route/Health/Rule 기본검증 PASS |
| Related Decision IDs | D03; D22 |
| Related Risk IDs | RISK-06; RISK-07; RISK-11 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Phase1_Logical_Architecture_v3.1.2; Phase 2 OCI/AWS/ROSA Design; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | Image Source는 D22 결정에 따르며 Harbor 사용을 사전 가정하지 않는다. Manifest/Image 계약은 P2-CICD-01의 Runner 기반 ROSA Delivery에 연결한다. |

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

애플리케이션 담당자로서 검증된 Phase 1 MSA를 ROSA에 동일 계약으로 배포한다. 이를 통해 플랫폼 차이를 최소화하고 Hybrid 데이터 경로 검증에 집중한다.

---

# 📌 Scope

## In Scope

- transaction-api/fds-engine
- OpenShift Route/Service
- Config/Secret
- Health
- Rule Smoke Test

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 📋 핵심 요구사항

- [ ] Phase 1 OpenAPI와 Rule 계약을 유지한다.
- [ ] 환경별 Config/Secret을 분리한다.
- [ ] Image Digest/Tag를 추적한다.
- [ ] OpenShift Security 제약을 충족한다.
- [ ] DB 연결 전 Health/Rule Smoke Test를 분리한다.

---

# ✅ Acceptance Criteria

- [ ] 두 서비스가 ROSA에서 Ready다.
- [ ] Route를 통한 transaction-api Health가 성공한다.
- [ ] fds-engine이 외부에 직접 노출되지 않는다.
- [ ] 4개 Rule Smoke Test가 통과한다.

---

# 🧪 검증 및 증적

- Deployment/Route/Service
- Image Digest
- Health/Rule Test
- Config/Secret Mapping
- Pod Security 상태
- Evidence Path: `docs/evidence/P2-APP-01/`

---

# 🔗 Dependency

- **Blocked By:** P2-ROSA-01, DEC-P2-REG-01
- **Blocks / Next:** P2-CICD-01, P2-HYB-01
- **Related Ticket:** P1-APP-01, P2-CICD-01
- **Milestone:** G5 ROSA Application Ready

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D03; D22
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-06; RISK-07; RISK-11
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** Phase 1과 동일한 transaction-api/fds-engine Image/Contract를 ROSA에 배포하고 Route/Health/Rule 기본검증 PASS
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>
