# Phase 2 ROSA Topology Portability Review — 2026-10-02 KST

## 1. 목적과 상태

- Record ID: **P2-ROSA-TOPOLOGY-REVIEW-01**
- 대상: ROSA with HCP vs ROSA classic architecture
- AWS/ROSA Region: **Asia Pacific (Seoul) / `ap-northeast-2` — APPROVED**
- 상태: **ASSESSMENT IN PROGRESS / TOPOLOGY NOT DECIDED**
- 연계: P2-ARC-01 #34, P2-IAC-01 #35, P2-ROSA-01 #38, P2-APP-01 #43, P2-CICD-01 #46, P2-HYB-01 #47, P2-E2E-01 #50, DEC-P2-COST-01
- 목적: 비용만이 아니라 Phase 1→ROSA→향후 다른 Kubernetes/OpenShift 환경으로의 **이식성(portability)** 을 topology 결정 Gate에 포함한다.

기존 `HCP_FAVORED_FOR_SHORT_POC_SUBJECT_TO_COST_GO` 방향은 비용 중심의 불완전한 중간판정이므로 철회한다. HCP/Classic은 아래 Portability Gate와 Cost GO를 모두 통과한 뒤 확정한다.

## 2. 우리 프로젝트에서 이식성의 의미

이 프로젝트의 핵심 이식 대상은 control plane VM 자체가 아니라 다음 계약이다.

1. **Workload contract** — 동일 transaction-api / fds-engine image와 health/readiness/business contract
2. **Kubernetes security contract** — Namespace, ServiceAccount/RBAC, NetworkPolicy, Pod SecurityContext
3. **Delivery contract** — Commit → Image Digest → 승인 Registry → Target cluster deploy → Runtime imageID 추적
4. **Hybrid interface contract** — Cloud workload → On-Prem PostgreSQL/Registry의 승인 Route/Source/TLS/Port
5. **Configuration contract** — endpoint/credential/registry/DNS를 환경별 입력으로 주입하고 image에 하드코딩하지 않음
6. **IaC contract** — AWS/ROSA provisioning과 cluster-independent workload/platform manifest를 분리
7. **Evidence contract** — Source → Runtime → Evidence chain이 topology 변경 후에도 동일 원칙으로 재현됨

반대로 AWS IAM/OIDC/STS, PrivateLink, VPC/Subnet, EBS, ELB/NAT/VPN과 ROSA provisioning 자체는 환경 종속 계층으로 보고 별도 모듈로 격리한다.

## 3. HCP / Classic 비교 — 이식성 관점

| 관점 | HCP | Classic | 프로젝트 해석 |
|---|---|---|---|
| Kubernetes/OpenShift workload API | 동일 OpenShift workload API 사용 | 동일 OpenShift workload API 사용 | **동등**. Deployment/Service/RBAC/NetworkPolicy/SecurityContext 수준에서는 topology가 이식성을 결정하지 않음 |
| Control plane 위치 | Red Hat-owned AWS account | Customer AWS account | Classic이 self-managed OCP와 구조적으로 더 유사하나, **ROSA에서는 둘 다 Red Hat managed service**이므로 self-managed 운영권과 동일하지 않음 |
| Customer VPC footprint | worker 중심, control plane은 PrivateLink로 연결 | control plane + infra + worker가 customer VPC | Classic은 인프라 가시성이 높지만 AWS 구조 결합도 함께 증가 |
| Platform components | ingress/image registry/monitoring 등이 worker에 배치 | dedicated infra nodes 사용 | HCP는 worker capacity 설계에 platform overhead 반영 필요. Classic은 infra-node 구조에 더 의존 |
| Hybrid data path | workload worker → VPC/network → On-Prem/OCI | workload worker → VPC/network → On-Prem/OCI | **애플리케이션 Hybrid path는 본질적으로 worker/data-plane 계약**. topology별 source/route 실측은 필요 |
| IaC 재사용성 | topology-specific ROSA/HCP module 필요 | topology-specific Classic module 필요 | 둘 다 AWS/ROSA 종속. 공통 VPC/interface와 workload layer를 별도 모듈로 분리해야 함 |
| Control-plane 운영 학습/증적 | customer가 control plane host를 직접 소유하지 않음 | customer account에 control plane/infra EC2가 존재 | control-plane host 수준 증적이 P0이면 Classic이 유리할 수 있으나 **현행 P2 AC에는 직접 host 운영이 요구되지 않음** |
| 다른 Kubernetes로의 app 이동 | OpenShift-specific object를 최소화하면 높음 | 동일 | topology보다 manifest 설계가 더 큰 영향 |
| 비용/footprint | customer EC2 footprint 작음, HCP cluster fee 존재 | customer control plane/infra footprint 추가 | Cost GO에서 별도 비교 |

Red Hat 공식 구조상 HCP는 control plane이 Red Hat 계정에 있고 worker가 고객 계정에 있으며 PrivateLink로 통신한다. Classic은 control plane과 worker가 고객 계정 VPC에 있다. HCP는 dedicated infra node를 사용하지 않고 platform component가 worker에 배치되며, Classic은 dedicated infra node를 사용한다.

## 4. Portability Gate — topology 확정 전 필수

다음은 **P0 topology decision input**이며 새로운 애플리케이션 AC를 추가하는 것이 아니라 기존 “동일 MSA/보안/Delivery/Hybrid 계약”을 이식성 관점에서 확인하는 설계 Gate다.

### PG-01 Workload base
- Deployment / Service / ConfigMap / Secret reference / ServiceAccount / RBAC / NetworkPolicy / Pod SecurityContext를 가능한 한 표준 Kubernetes API로 유지한다.
- HCP/Classic 전용 workload manifest를 별도 본체로 만들지 않는다.

### PG-02 OpenShift overlay
- OpenShift `Route` 등 OCP 전용 리소스는 base workload와 분리한 overlay/adaptor로 관리한다.
- 표준 Kubernetes Ingress로 대체 가능한 구간은 base contract와 분리해 비교 가능하게 유지한다.

### PG-03 Security
- 현행 `runAsNonRoot`, capability drop, seccomp, read-only rootfs 등 Pod SecurityContext를 주 계약으로 유지한다.
- custom SCC 또는 privileged/hostNetwork/hostPath를 portability 기본 전제로 만들지 않는다.
- OpenShift SCC는 workload securityContext의 수용/거부 검증 계층으로 취급한다.

### PG-04 Network policy
- 표준 NetworkPolicy로 표현 가능한 통제를 우선한다.
- Calico/OVN 등 CNI 전용 CRD가 필요하면 별도 adapter와 portability exception으로 기록한다.
- 같은 정책 문구라도 CNI 구현 차이가 있으므로 실제 ROSA에서 Negative test를 재검증한다.

### PG-05 Storage/data
- transaction 데이터의 권위 Source인 On-Prem PostgreSQL 계약을 유지한다.
- AWS EBS/StorageClass에 workload business contract가 직접 종속되지 않도록 한다.
- PVC가 필요한 구성은 StorageClass 이름/size/access mode를 환경 입력으로 분리한다.

### PG-06 Registry/delivery
- image는 digest로 추적하고 Registry hostname/credential을 환경 입력으로 분리한다.
- Self-hosted Runner의 deploy 대상은 kubeconfig/token/endpoint로 교체 가능해야 하며 HCP/Classic 전용 CI workflow 분기를 최소화한다.

### PG-07 Hybrid interface
- IF-17~IF-20의 CIDR/port/TLS/DNS/source contract를 topology-independent interface로 유지한다.
- HCP PrivateLink 또는 Classic control-plane subnet을 application data-path contract에 직접 노출하지 않는다.

### PG-08 IaC layering
Terraform/IaC는 최소 다음 계층으로 분리한다.
1. common network/interface inputs
2. AWS account/IAM/OIDC
3. ROSA topology-specific provisioning (HCP or Classic)
4. cluster platform configuration
5. application workload manifests

Topology 교체 시 4~5 계층을 가능한 한 그대로 재사용할 수 있어야 한다.

### PG-09 Evidence
- HCP에서도 현행 P0 AC를 판정하는 데 필요한 workload/platform evidence를 수집할 수 있는지 확인한다.
- control-plane host-level evidence가 필수로 확인되면 HCP 제약을 명시하고 Classic 또는 AC/증적 경계의 정식 결정이 필요하다.
- 비용 때문에 증적을 약화하지 않는다.

## 5. 현재 프로젝트에 대한 중간 판단

### 사실
- #38의 P0 범위는 ROSA API/Worker Ready, Namespace/RBAC/NetworkPolicy/SecurityContext/Hybrid Route와 Application 선행조건이다.
- #43은 Phase 1과 동일 image/contract를 ROSA에 배포하는 것이 목적이다.
- #46은 외부 self-hosted Runner에서 승인 Registry를 거쳐 ROSA로 배포하고 digest/imageID 추적성을 유지한다.
- #47/#50은 ROSA workload에서 On-Prem PostgreSQL/Registry로 이어지는 Hybrid data path와 업무 E2E를 검증한다.
- 공용 OCP Lab에서도 cluster-wide/node 변경은 인수범위가 아니며 namespace-local workload/security precheck가 중심이다.

### 해석
따라서 **현행 P0 인수범위만 놓고 보면 HCP와 Classic의 workload 이식성 차이는 작고**, topology보다 manifest/IaC 계층화가 이식성을 좌우한다.

Classic은 self-managed OCP와 **구조적으로 더 유사**하지만, control plane이 고객 AWS 계정에 있다는 이유만으로 Phase 1 온프레미스 Kubernetes/OCP 운영 모델이 자동 재현되는 것은 아니다.

HCP는 control plane host-level 가시성이 낮지만, 현재 프로젝트가 검증하려는 MSA/보안/Delivery/Hybrid 계약은 worker/workload 계층에 집중되어 있어 **그 자체로 이식성 차단 근거는 아직 확인되지 않았다.**

### 현재 판정
**TOPOLOGY = UNDECIDED / PORTABILITY GATE REQUIRED**

Cost GO 이전에 다음을 확인한다.
1. PG-01~PG-09 충족 여부
2. HCP에서 현행 #38/#43/#46/#47/#50 Evidence를 모두 확보 가능한지
3. topology-specific manifest/IaC diff의 실제 크기
4. 동일 workload 조건의 HCP/Classic Cost-to-Complete

그 뒤 Architecture Freeze에서 topology를 결정한다.

## 5A. 2026-10-02 Phase 1 실제 Source 대조 결과

대조한 main HEAD:
- `321Team/infra-kubernetes@7329bf2eb988b552483af48ff660d6a3f1f1d4f5`
- `321Team/fds-msa@5120b7df72d24ada3dbcf23fc0292fb58ae778af`
- `321Team/infra-cicd@52cf494bec02ab4b814bed07e4cf66f37a3547b6`
- `321Team/infra-terraform@1c5ce75b81c0c103b46c546b015246183a317e56`
- `321Team/infra-rosa@d5e6226d4e8eca45af757a16bfce5c0b89caf66a`

상세 machine-readable inventory:
- `source-portability-inventory.json`

W0 실행계획:
- `w0-portability-precheck.md`

### 분류 요약

| 분류 | 현재 주요 항목 | 조치 |
|---|---|---|
| 그대로 재사용 가능 | 앱 business code, HTTP/PostgreSQL contract, probes/resources, core RBAC intent, ServiceAccount token 최소화 | target Runtime 재검증 후 재사용 |
| OpenShift overlay 필요 | NodePort+edge01, 고정 UID/GID, PSA v1.36 pin, target CIDR NetworkPolicy, Route/SCC/target credential | portable base와 분리 |
| ROSA 종속 | target API/access, managed platform evidence, HCP/Classic provisioning adapter | `infra-rosa` / topology layer에 격리 |
| AWS 종속 | VPC/Subnet, IAM/OIDC, VPN/SG/NACL, EBS/ELB/NAT/data transfer | `infra-terraform` / network layer에 격리 |

### 현재 차단 Gate

- **PG-01 HOLD:** 권위 있는 단일 portable workload base가 아직 없다. `fds-msa/references/upstream/kubernetes`는 reference snapshot이고 `infra-kubernetes/manifests/02-securitycontext.yaml`은 Security patch/reference 성격이다.
- **PG-02 HOLD:** Phase 1 외부 진입은 NodePort 30080 + edge01이며 OpenShift Route overlay는 아직 구현되지 않았다.
- **PG-03 HOLD:** Phase 1 manifest가 `runAsUser: 10001`, `runAsGroup: 999/10001`을 고정한다. OpenShift restricted-v2 namespace UID range와의 호환성을 Shared OCP에서 확인해야 한다.
- **PG-08 HOLD:** `infra-terraform` / `infra-rosa`는 저장소 초기 구성만 존재하고 실제 계층형 IaC/manifest가 아직 없다.

### 비차단이나 이식성 비용이 큰 항목

- Phase 1 monitoring storage는 `fds-local-storage` + `k8s-worker03` local PV에 결합되어 있어 ROSA에 직접 이식할 수 없다. P0 App topology blocker는 아니지만 full-system portability에는 CSI-backed storage overlay가 필요하다.
- node-exporter는 hostNetwork/hostPID/hostPort/hostPath를 사용하므로 managed OpenShift/ROSA에서 별도 권한/운영 모델 검토가 필요하다. P1 Monitoring 영역으로 분리한다.
- 현재 CI workflow의 build/scan 계약은 재사용 가능하지만 `cicd-runner01` hostname/user/label 및 local offline path에 결합되어 있다. ROSA API/namespace/token/registry를 target adapter로 분리해야 한다.

### Topology 영향

이 대조로 **HCP 또는 Classic을 직접 선택할 근거는 아직 생기지 않았다.** 현재 blocker 대부분은 두 topology 공통의 OpenShift admission/workload/adapter 문제다.

따라서:
1. Shared OCP W0에서 PG-03 UID/SCC와 portable securityContext를 먼저 실증
2. portable workload base + OpenShift overlay 경계 확정
3. Terraform/ROSA topology module 경계 확인
4. 그 뒤 HCP/Classic의 운영·증적·Hybrid path·비용을 비교

순서로 진행한다.

## 6. 설계 권고

- **Kubernetes base + OpenShift overlay** 구조를 사용한다.
- ROSA topology를 workload manifest에 전파하지 않는다.
- Terraform에서 HCP/Classic cluster module을 교체 가능한 경계로 둔다.
- Registry/DB/DNS/credential은 환경 변수·Secret·ConfigMap/CI input으로 외부화한다.
- custom SCC, CNI-specific policy, AWS-specific storage/identity를 P0 workload contract에 직접 결합하지 않는다.
- 최종 topology 판정에는 **Portability / Security & Evidence / Hybrid Networking / Operability / Cost / Schedule**을 함께 사용한다.

## 7. 공식 근거

- ROSA architecture models: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/rosa-architecture-models
- ROSA classic architecture models: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws_classic_architecture/4/html/architecture/rosa-architecture-models
- OpenShift Routes / Ingress: https://docs.redhat.com/en/documentation/openshift_container_platform/4.21/html/ingress_and_load_balancing/routes
- OpenShift SCC: https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/authentication_and_authorization/managing-pod-security-policies

## 8. 상태

- REGION: **APPROVED — ap-northeast-2**
- PORTABILITY REVIEW: **IN PROGRESS**
- TOPOLOGY: **UNDECIDED**
- COST COMPARISON: **IN PROGRESS / exact project inputs pending**
- TERRAFORM APPLY: **NOT RUN**
- ROSA RUNTIME: **NOT RUN**
- REVIEW/MERGE/PUBLICATION: **NOT DONE**
