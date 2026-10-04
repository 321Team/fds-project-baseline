<!-- fds-canonical-live:v3.1.21 record-id:DEC-P2-OP-01:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/DEC-P2-OP-01.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 해당 업무의 기존 AC·Exit Criteria와 실행/인수 구분을 유지한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:DEC-P2-OP-01:end -->

<!-- issue-decision-contract-20261001:v1:start -->
## 2026-10-01 Operator Supply Decision Contract v1

### Activation
G5 이후 P0 잔여 capacity가 있을 때만 검토한다.

### Decision options
- Direct Catalog
- 승인된 mirror/Harbor/Custom CatalogSource
- Deferred / N/A

### Shared OCP guard
신규 cluster-wide Operator 설치나 CatalogSource 변경은 관리자 명시 승인 없이는 수행하지 않는다. 이미 설치된 Operator의 namespace-local CR 검증과 설치 여부 결정은 구분한다.

### Exit
선택안, 지원 Version, 권한, 공급경로, rollback/uninstall, 비용/일정 영향과 #51 활성화 여부를 기록한다.
<!-- issue-decision-contract-20261001:v1:end -->

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
Operator 공급망 결정은 `이미 설치된 Operator의 namespace-local 사용`과 `신규 Operator 설치`를 구분한다. 후자는 공용 OCP 관리자 명시 승인 없이는 실행하지 않고, P1 Decision/Deferred 근거로만 사용한다.



<!-- schedule-realign-20261001:issue-41:start -->
## 2026-10-01 일정·WIP 정합화

- **Deferred-first:** Operator 공급망 Decision은 G5 전 P0 작업과 겹치지 않는다. G5 이후 capacity가 없으면 미수행 사유/Owner/Due를 남기고 Deferred 처리한다.

- Scope/AC/Priority/Review Authority 변경 없음.
- P1 Decision은 P0 Gate를 자동 차단하지 않는다.
<!-- schedule-realign-20261001:issue-41:end -->
<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/DEC-P2-OP-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/DEC-P2-OP-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 조건부 결정. Direct 또는 Mirror 공급망·Owner/Due·#51 Cancelled/구현 기준을 D26으로 기록.

**인계·관련 티켓:** [#38](https://github.com/321Team/fds-project-baseline/issues/38) · [#51](https://github.com/321Team/fds-project-baseline/issues/51).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-milestone-assignment:2026-09-11 issue:41 -->
## 대표 Milestone 배정 — 2026-09-11

- **추적 Milestone:** G5 ROSA Application Ready (GitHub #9)
- **배정 성격:** P2 잠정 계획 · 이권욱 사용자 지시에 따른 대표 추적 항목 지정.
- **배정 근거:** WBS 2026-10-12~10-16 Operator 공급망 범위 결정 계획에 따라 G5에 연결한다. Direct/Mirror 선택과 조건부 구현 여부는 D26 승인으로 결정한다.
- **출처:** [발행 정본 v3.1.18 WBS](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/wbs/FDS_v3.1.18_WBS_and_Gantt_v1.0.xlsx)
- **일정 원칙:** 일정은 고정된 필수 기한이 아닌 조정 가능한 계획 목표다. 선행조건과 영향 확인 후 유연하게 조정하며, 실제 완료일·승인·Runtime 증적 요건과 구분한다.
- **적용 범위:** 대표 Milestone 연결과 이 근거 기록. 기존 상태·완료 사실·AC·담당·티켓 Start/End 및 Gate 요건을 유지한다.

---

<!-- fds-notion-migration:2026-09-09 record-id:DEC-P2-OP-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:DEC-P2-OP-01 -->
# DEC-P2-OP-01 — Operator Supply Chain Scope Decision

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-P2-OP-01 |
| Phase | Phase 2 |
| Category | Architecture / Operator Supply Chain |
| Type | Decision |
| Status | To Do |
| Priority | P1 |
| Start | TBD — G5 이후 P0 잔여 capacity 시 |
| End | TBD — 10-26 이전 강제하지 않음 |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | ROSA Operator 공급망을 Direct Catalog 또는 oc-mirror/Harbor/Custom CatalogSource 중 하나로 결정하고 구현·N/A 기준 승인 |
| Related Decision IDs | D22; D26 |
| Related Risk IDs | RISK-06; RISK-11; RISK-15 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #41 snapshot 2026-09-09T12:08:39Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | P1/non-blocking. #38 ROSA와 G5 P0를 침해하지 않도록 G5 이후 capacity가 있을 때만 결정하며, 여유가 없으면 Deferred로 기록한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-09T12:08:39Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #41](https://github.com/321Team/fds-project-baseline/issues/41), Issue 갱신 시각 `2026-09-09T12:08:39Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

OpenShift 담당자 이하영으로서 ROSA Operator 공급망 방식을 결정한다. 이를 통해 불필요한 Mirror 구현을 피하면서도 필요한 경우 재현 가능한 CatalogSource 경로를 확보한다.

---

# Scope

## In Scope

- Direct OperatorHub
- oc-mirror/Harbor
- Custom CatalogSource
- 권한·비용·네트워크
- 적용 또는 N/A 기준

## Out of Scope

- 결정 전 Mirror 구축
- 승인되지 않은 CatalogSource

---

# 핵심 요구사항

- [ ] ROSA 네트워크 접근성과 Catalog 사용 가능성을 확인한다.
- [ ] Mirror 적용 시 Harbor 용량·TLS·Credential을 검토한다.
- [ ] 직접 사용 시 P2-OP-01 Cancelled 근거를 기록한다.
- [ ] 결정은 D26에 남긴다.

---

# Acceptance Criteria

- [ ] Direct 또는 Mirror 방식이 하나로 결정된다.
- [ ] Owner·Due·구현 또는 N/A 기준이 승인된다.
- [ ] P2-OP-01 상태 전환 조건이 명확하다.

---

# 검증 및 증적

- Decision D26
- ROSA Catalog/권한 확인
- 비용·경로 비교
- N/A 또는 구현 계획
- Evidence Path: `321Team/fds-project-evidence:evidence/DEC-P2-OP-01/`

---

# Dependency

- **Blocked By:** P2-ROSA-01 선행정보
- **Blocks / Next:** P2-OP-01
- **Related Ticket:** DEC-P2-REG-01
- **Milestone:** G5 / Phase 2 P1

---

# Decision / Risk Control

- **Related Decision IDs:** D22; D26
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-06; RISK-11; RISK-15
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** ROSA Operator 공급망을 Direct Catalog 또는 oc-mirror/Harbor/Custom CatalogSource 중 하나로 결정하고 구현·N/A 기준 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `0d6ac7cf62ac7952384509f17bc275eb083235493e9c1eb69e052582ea695621`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:DEC-P2-OP-01 -->
# DEC-P2-OP-01 — Operator Supply Chain Scope Decision

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | DEC-P2-OP-01 |
| Phase | Phase 2 |
| Category | Architecture / Operator Supply Chain |
| Type | Decision |
| Status | To Do |
| Priority | P1 |
| Start | 2026-10-12 |
| End | 2026-10-16 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | ROSA Operator 공급망을 Direct Catalog 또는 oc-mirror/Harbor/Custom CatalogSource 중 하나로 결정하고 구현·N/A 기준 승인 |
| Related Decision IDs | D22; D26 |
| Related Risk IDs | RISK-06; RISK-11; RISK-15 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Network_Baseline_v2.3; FDS_Phase1_Logical_Architecture_v3.1.2; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | D26에서 Direct Catalog 선택 시 P2-OP-01은 Cancelled 처리하고, Mirror 선택 시 P2-OP-01을 활성화한다. |

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

OpenShift 담당자 이하영으로서 ROSA Operator 공급망 방식을 결정한다. 이를 통해 불필요한 Mirror 구현을 피하면서도 필요한 경우 재현 가능한 CatalogSource 경로를 확보한다.

---

# 📌 Scope

## In Scope

- Direct OperatorHub
- oc-mirror/Harbor
- Custom CatalogSource
- 권한·비용·네트워크
- 적용 또는 N/A 기준

## Out of Scope

- 결정 전 Mirror 구축
- 승인되지 않은 CatalogSource

---

# 📋 핵심 요구사항

- [ ] ROSA 네트워크 접근성과 Catalog 사용 가능성을 확인한다.
- [ ] Mirror 적용 시 Harbor 용량·TLS·Credential을 검토한다.
- [ ] 직접 사용 시 P2-OP-01 Cancelled 근거를 기록한다.
- [ ] 결정은 D26에 남긴다.

---

# ✅ Acceptance Criteria

- [ ] Direct 또는 Mirror 방식이 하나로 결정된다.
- [ ] Owner·Due·구현 또는 N/A 기준이 승인된다.
- [ ] P2-OP-01 상태 전환 조건이 명확하다.

---

# 🧪 검증 및 증적

- Decision D26
- ROSA Catalog/권한 확인
- 비용·경로 비교
- N/A 또는 구현 계획
- Evidence Path: docs/evidence/DEC-P2-OP-01/

---

# 🔗 Dependency

- **Blocked By:** P2-ROSA-01 선행정보
- **Blocks / Next:** P2-OP-01
- **Related Ticket:** DEC-P2-REG-01
- **Milestone:** G5 / Phase 2 P1

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D22; D26
- **Decision Control:** 관련 Decision은 이권욱·이하영·이재환이 확인할 수 있는 기록으로 남기며, 승인 전 조건부 작업을 시작하지 않는다.
- **Related Risk IDs:** RISK-06; RISK-11; RISK-15
- **Risk Control:** 예방·탐지·복구 통제를 Acceptance Criteria와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** ROSA Operator 공급망을 Direct Catalog 또는 oc-mirror/Harbor/Custom CatalogSource 중 하나로 결정하고 구현·N/A 기준 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>
