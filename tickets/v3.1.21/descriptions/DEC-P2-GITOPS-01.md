# DEC-P2-GITOPS-01 — OpenShift GitOps (Argo CD) 도입 범위 결정

Version: v3.1.21 CANDIDATE
Source: https://github.com/321Team/fds-project-baseline/issues/120
Updated at: 2026-10-01T07:15:46Z
Source body SHA256: `cc8f7d50a43a39113018d67d519ca7eeb5093684853b53cb0081dee914819b2a`
GitHub: open / None
Current disposition: Source lifecycle/AC retained; no new acceptance by this publication.

| Property | Current source value |
|---|---|
| Record ID | DEC-P2-GITOPS-01 |
| Phase | Phase 2 |
| Category | CI/CD / OpenShift GitOps |
| Type | Decision |
| Status | To Do |
| Priority | P1 |
| Start | TBD — G5 이후 P0 잔여 capacity 시 |
| End | TBD — 10-26 이전 강제하지 않음 |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | OpenShift GitOps 도입/미도입/유예를 단일안으로 결정하고, 도입 시 #46 Delivery Contract 변경 CR·권한모델·Git Source·재생성/Rollback·D26 Operator 공급경로를 승인 |
| Related Decision IDs | D26(Operator 공급망); 신규 Decision Register 순번은 차기 정본에서 부여 |
| Related Risk IDs | RISK-06; RISK-08; RISK-11 |
| Source | 2026-09-29 팀 회의 Red Hat 제품 검토; 2026-09-30 사용자 범위 결정; Red Hat ROSA/OpenShift GitOps 공식 문서 |
| Schedule Note | P1/non-blocking. #42/#46 P0 Registry/Delivery와 겹치지 않도록 G5 이후 capacity가 있을 때만 Go/No-Go를 판단한다. Go 전에는 기존 Runner direct ROSA Delivery Contract를 유지한다. |

## Source checklist

- [ ] 도입 / 미도입 / 유예가 단일안으로 기록된다.
- [ ] 미도입 또는 유예 시 기존 #46 Runner Delivery Contract가 그대로 유지됨을 확인한다.
- [ ] 도입 시 #46의 Deploy 단계 변경을 별도 CR로 승인한다.
- [ ] Build/Test/Scan/Registry Push와 Runtime Sync의 Producer/Consumer 경계를 명시한다.
- [ ] Argo CD RBAC/Namespace 권한을 최소권한으로 설계한다.
- [ ] Source Commit → Registry Digest → Git desired state → Argo CD sync revision → ROSA Runtime imageID → Evidence 체인을 정의한다.
- [ ] Sync failure/drift/rollback/recreate 검증과 Evidence 위치를 정한다.
- [ ] P0 G5/G6 지연 예상 시 Deferred로 전환한다.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

<!-- issue-decision-contract-20261001:v1:start -->
## 2026-10-01 GitOps Decision Contract v1

### Default
G5 이후 capacity-based / Deferred-first. Go 전 #46 Runner direct ROSA Delivery Contract 유지.

### Shared OCP
현재 관측된 AllNamespaces-only 설치조건 때문에 신규 설치는 HOLD. 사전 설치된 경우에만 허용 RBAC/Namespace 범위에서 비파괴 Precheck.

### Go condition
권한모델, Git Source, reconciliation/rollback, D26 공급경로, #46 Delivery Contract 변경 필요성이 모두 승인돼야 한다.

### Exit
Go / No-Go / Deferred 중 하나를 명시하고 Go인 경우에만 별도 구현 CR을 발행한다.
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
현재 Lab precheck에서 GitOps가 AllNamespaces-only로 관측된 조건을 유지한다. 공용 OCP 신규 설치는 HOLD이며, 사전 설치된 경우에만 허용 Namespace/RBAC 범위에서 비파괴 Precheck를 검토한다.



<!-- schedule-realign-20261001:issue-120:start -->
## 2026-10-01 일정·WIP 정합화

- **Deferred-first:** GitOps Decision은 #46 P0 Delivery를 선행 차단하지 않는다. G5 이후 capacity가 있을 때만 검토하고, 그렇지 않으면 현행 Runner direct Delivery를 유지한 채 Deferred한다.

- Scope/AC/Priority/Review Authority 변경 없음.
- P1 Decision은 P0 Gate를 자동 차단하지 않는다.
<!-- schedule-realign-20261001:issue-120:end -->
# DEC-P2-GITOPS-01 — OpenShift GitOps (Argo CD) 도입 범위 결정

> 신규 Decision · 2026-09-30 KST
> 현행 정본: `docs-v3.1.20 / RELEASED`
> 차기 정본 후보: Draft PR #112
> **Priority P1 / G5·G6·Project Close non-blocking**

## 티켓 속성

| Property | 입력값 |
|---|---|
| Record ID | DEC-P2-GITOPS-01 |
| Phase | Phase 2 |
| Category | CI/CD / OpenShift GitOps |
| Type | Decision |
| Status | To Do |
| Priority | P1 |
| Start | TBD — G5 이후 P0 잔여 capacity 시 |
| End | TBD — 10-26 이전 강제하지 않음 |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | OpenShift GitOps 도입/미도입/유예를 단일안으로 결정하고, 도입 시 #46 Delivery Contract 변경 CR·권한모델·Git Source·재생성/Rollback·D26 Operator 공급경로를 승인 |
| Related Decision IDs | D26(Operator 공급망); 신규 Decision Register 순번은 차기 정본에서 부여 |
| Related Risk IDs | RISK-06; RISK-08; RISK-11 |
| Source | 2026-09-29 팀 회의 Red Hat 제품 검토; 2026-09-30 사용자 범위 결정; Red Hat ROSA/OpenShift GitOps 공식 문서 |
| Schedule Note | P1/non-blocking. #42/#46 P0 Registry/Delivery와 겹치지 않도록 G5 이후 capacity가 있을 때만 Go/No-Go를 판단한다. Go 전에는 기존 Runner direct ROSA Delivery Contract를 유지한다. |

## User Story

CI/CD 담당자로서 ROSA의 Application Delivery에 Red Hat OpenShift GitOps(Argo CD)를 도입할지 결정한다. 이를 통해 Git 선언 기반 재현성과 추적성을 높일 수 있는지 검토하되, 3인 프로젝트의 P0 Delivery 일정은 보호한다.

## In Scope

- OpenShift GitOps Operator / Argo CD 도입 실익
- #46 Runner 직접 Deploy와 GitOps Deploy의 책임 분리
- Runner가 Build/Test/Scan/Registry Push까지 담당하고 Argo CD가 Runtime Sync를 담당하는 대안
- Argo CD 권한/RBAC 및 관리 Namespace 범위
- Application/Project/SyncPolicy Source 관리
- Cluster recreate 후 Git 기반 재적용
- Rollback/Sync failure/Drift Evidence
- D26 Operator 공급방식과 설치경로 연계

## Out of Scope

- 결정 전 Operator 설치
- P0 요구로 자동 승격
- OpenShift Pipelines/Tekton 도입
- 자동 승인/자동 병합
- Cluster-admin 또는 과도한 Namespace admin 권한을 기본값으로 부여

## Acceptance Criteria

- [ ] 도입 / 미도입 / 유예가 단일안으로 기록된다.
- [ ] 미도입 또는 유예 시 기존 #46 Runner Delivery Contract가 그대로 유지됨을 확인한다.
- [ ] 도입 시 #46의 Deploy 단계 변경을 별도 CR로 승인한다.
- [ ] Build/Test/Scan/Registry Push와 Runtime Sync의 Producer/Consumer 경계를 명시한다.
- [ ] Argo CD RBAC/Namespace 권한을 최소권한으로 설계한다.
- [ ] Source Commit → Registry Digest → Git desired state → Argo CD sync revision → ROSA Runtime imageID → Evidence 체인을 정의한다.
- [ ] Sync failure/drift/rollback/recreate 검증과 Evidence 위치를 정한다.
- [ ] P0 G5/G6 지연 예상 시 Deferred로 전환한다.

## Dependency / Relation

- Related: #34 P2-ARC-01, #38 P2-ROSA-01, #41 DEC-P2-OP-01, #46 P2-CICD-01, #49 P2-DOC-01
- **P0 Blocker: 없음**
- 도입 결정 시: #46 CR 및 필요하면 별도 구현 Task 발행
- Milestone: G5 ROSA Application Ready (추적용이며 Gate blocker 아님)

## Decision Control

OpenShift GitOps는 ROSA에서 지원되는 Operator이며 Argo CD를 declarative GitOps engine으로 사용한다. 다만 제품 지원 여부와 프로젝트 채택 여부는 별개다.

도입 전에는 P2-CICD-01 현행 P0 계약을 변경하지 않는다. 결정이 늦어져도 P0는 Runner 직접 Deploy로 진행 가능해야 한다.

공식 참조:
- https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/gitops/about-redhat-openshift-gitops
- https://docs.redhat.com/en/documentation/red_hat_openshift_gitops/1.19/html/argo_cd_instance/setting-up-argocd-instance

## Completion Record

- Result: PENDING DECISION
- Runtime: NOT RUN
- Review: NOT DONE

