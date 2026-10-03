# DEC-P2-RHOAI-01 — RHOAI(Red Hat OpenShift AI) 도입 범위 결정

Version: v3.1.21 CANDIDATE
Source: https://github.com/321Team/fds-project-baseline/issues/95
Updated at: 2026-10-01T07:15:22Z
Source body SHA256: `82c3a5285f275ef6a8924835303f035dd778fa93eca296dc5b30742192e9df00`
GitHub: open / None
Current disposition: Source lifecycle/AC retained; no new acceptance by this publication.

| Property | Current source value |
|---|---|
| Record ID | DEC-P2-RHOAI-01 |
| Phase | Phase 2 |
| Category | OpenShift / AI Platform |
| Type | Decision |
| Status | To Do |
| Priority | P1 |
| Start | TBD — Deferred 우선 |
| End | TBD — 프로젝트 종료 후 별도 PoC는 Project Scope 밖 |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | RHOAI 도입/미도입/유예를 단일안으로 결정하고, 도입 시 적용 범위·ROSA 전제(Version/Quota/Operator 공급)·비용·삭제 절차와 Change Request 발행 근거를, 미도입·유예 시 N/A/Deferred 근거를 기록·승인 |
| Related Decision IDs | D26 — 기존 의미 유지(ROSA Operator 공급망). 신규 D 순번은 정본 Decision Register 대조 후 부여 |
| Related Risk IDs | 미부여 — 정본 Risk Register 대조 후 부여 |
| Source | 2026-09-23 팀 회고 합의([PR #94](https://github.com/321Team/fds-project-baseline/pull/94)); 사용자 2026-09-23 속성 결정(Type Decision·Lead 이하영·Priority P1·일정 10-06~10-16); 발행 docs-v3.1.20 Baseline §1.3/§3.2 |
| Schedule Note | P1 / Deferred 우선. 2026-10-26 Project Close 전 구현 일정을 배정하지 않는다. 도입 Decision이 남더라도 P0를 차단하지 않으며 10-27 이후 PoC는 별도 프로젝트/승인 범위로 취급한다. |

## Source checklist

- [ ] 도입 목적과 FDS 서비스 연계 범위를 명시한다.
- [ ] ROSA 지원 Version·Quota·Operator 공급 전제를 확인한다.
- [ ] 비용과 삭제·복구 절차를 기록한다.
- [ ] Baseline §1.3 Scope Out의 "AI Inference"와의 관계를 명시한다.
- [ ] 도입/미도입/유예가 단일안으로 승인된다.
- [ ] 도입 시 Baseline §3.2에 따른 Change Request와 후속 구현 티켓(Owner/Due)이 발행된다.
- [ ] 미도입·유예 시 N/A/Deferred 근거가 기록된다.
- [ ] 결정 결과가 P2-ARC-01·P2-ROSA-01과 차기 정본 후보에 연결된다.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

<!-- issue-decision-contract-20261001:v1:start -->
## 2026-10-01 RHOAI Decision Contract v1

### Default
`Deferred-first`. 프로젝트 종료 전 P0/Gate non-blocking.

### Shared OCP
read-only catalog/support/compatibility 확인만 기본 허용. Operator 설치, GPU/고자원 소비, cluster-wide 변경은 관리자 승인+Quota 없이는 수행하지 않는다.

### Go condition
실제 비즈니스/시연 가치, 지원 Version, 비용, Quota, 설치/삭제 경로, P0 영향이 모두 명확할 때만 별도 CR로 활성화한다.

### Deferred exit
도입하지 않는 이유와 재검토 조건만 기록해도 본 Decision 목적을 충족할 수 있다.
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
RHOAI는 cluster-wide Operator·GPU/고자원 사용 가능성이 있으므로 공용 OCP에서는 catalog/support/read-only 사전조사만 기본 허용한다. 관리자 명시 승인과 quota가 없으면 설치/PoC는 수행하지 않고 Deferred 유지한다.

<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/DEC-P2-RHOAI-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/DEC-P2-RHOAI-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

# DEC-P2-RHOAI-01 — RHOAI(Red Hat OpenShift AI) 도입 범위 결정

> 신규 발행: 2026-09-23 KST · 2026-09-23 팀 회고 합의 "Phase 2 착수 시 RHOAI 도입안 포함 필수"에 따른 신규 Decision 티켓.
> 현행 발행 정본 [docs-v3.1.20](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.20)의 Baseline/WBS/Ticket Pack에는 이 Record가 없다. 차기 정본 후보에 반영하기 전까지 이 Issue 본문이 운영 기록이며, 정본 발행 상태를 뜻하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-P2-RHOAI-01 |
| Phase | Phase 2 |
| Category | OpenShift / AI Platform |
| Type | Decision |
| Status | To Do |
| Priority | P1 |
| Start | TBD — Deferred 우선 |
| End | TBD — 프로젝트 종료 후 별도 PoC는 Project Scope 밖 |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | RHOAI 도입/미도입/유예를 단일안으로 결정하고, 도입 시 적용 범위·ROSA 전제(Version/Quota/Operator 공급)·비용·삭제 절차와 Change Request 발행 근거를, 미도입·유예 시 N/A/Deferred 근거를 기록·승인 |
| Related Decision IDs | D26 — 기존 의미 유지(ROSA Operator 공급망). 신규 D 순번은 정본 Decision Register 대조 후 부여 |
| Related Risk IDs | 미부여 — 정본 Risk Register 대조 후 부여 |
| Source | 2026-09-23 팀 회고 합의([PR #94](https://github.com/321Team/fds-project-baseline/pull/94)); 사용자 2026-09-23 속성 결정(Type Decision·Lead 이하영·Priority P1·일정 10-06~10-16); 발행 docs-v3.1.20 Baseline §1.3/§3.2 |
| Schedule Note | P1 / Deferred 우선. 2026-10-26 Project Close 전 구현 일정을 배정하지 않는다. 도입 Decision이 남더라도 P0를 차단하지 않으며 10-27 이후 PoC는 별도 프로젝트/승인 범위로 취급한다. |

---

# User Story

ROSA 플랫폼 담당자로서 Phase 2에서 RHOAI(Red Hat OpenShift AI)를 도입할지와 그 범위를 결정한다. 이를 통해 팀 회고에서 합의한 RHOAI 도입안을 Phase 2 계획에 포함하면서, 결정 전에 기존 P0 Hybrid 범위와 일정에 미확정 기능이 추가되지 않도록 한다.

---

# Scope

## In Scope

- RHOAI 도입/미도입/유예 대안 비교
- ROSA 대상 전제: 지원 Version, Worker/Quota, Operator 공급 방식(D26 연계)
- FDS 서비스(`transaction-api`, `fds-engine`)와의 연계 목적·범위
- 비용·삭제·복구 절차
- 도입 시 Change Request·후속 구현 티켓 정의

## Out of Scope

- 결정 전 RHOAI 설치·구성 등 구현 작업
- 기존 P0 Hybrid 범위·Gate 기준 변경
- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] 도입 목적과 FDS 서비스 연계 범위를 명시한다.
- [ ] ROSA 지원 Version·Quota·Operator 공급 전제를 확인한다.
- [ ] 비용과 삭제·복구 절차를 기록한다.
- [ ] Baseline §1.3 Scope Out의 "AI Inference"와의 관계를 명시한다.

---

# Acceptance Criteria

- [ ] 도입/미도입/유예가 단일안으로 승인된다.
- [ ] 도입 시 Baseline §3.2에 따른 Change Request와 후속 구현 티켓(Owner/Due)이 발행된다.
- [ ] 미도입·유예 시 N/A/Deferred 근거가 기록된다.
- [ ] 결정 결과가 P2-ARC-01·P2-ROSA-01과 차기 정본 후보에 연결된다.

---

# 검증 및 증적

- Decision 비교표
- ROSA 전제(Version/Quota/Operator) 확인 기록
- 비용·삭제 절차
- 신규 Decision Register 항목
- Evidence Path: `321Team/fds-project-evidence:evidence/DEC-P2-RHOAI-01/`

---

# Dependency

- **Blocked By:** MS-P2-START-01
- **Blocks / Next:** 도입 결정 시 Change Request 및 구현 티켓
- **Related Ticket:** P2-ARC-01 (#34), P2-ROSA-01 (#38), DEC-P2-OP-01 (#41)
- **Milestone:** G5 ROSA Application Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D26 (신규 D 순번은 정본 레지스터 대조 후 부여)
- **Decision Control:** 결정 전에 조건부 구현 작업을 시작하지 않는다. Scope Out 기능 추가는 Baseline §3.2의 Change Request 절차를 따른다.
- **Related Risk IDs:** 미부여 — 정본 레지스터 대조 후 부여
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** RHOAI 도입/미도입/유예를 단일안으로 결정하고, 도입 시 적용 범위·ROSA 전제(Version/Quota/Operator 공급)·비용·삭제 절차와 Change Request 발행 근거를, 미도입·유예 시 N/A/Deferred 근거를 기록·승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
