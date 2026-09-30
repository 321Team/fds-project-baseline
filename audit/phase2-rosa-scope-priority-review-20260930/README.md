# Phase 2 ROSA Scope / Priority 전수 검수 — 2026-09-30 KST

## 1. 목적과 적용 기준

- **현행 운영 정본 인용 기준:** `docs-v3.1.20 / RELEASED`
- **차기 정본 후보:** Draft PR #112, `release/v3.1.21`
- **팀 구성:** 3인
- **검수 목적:** ROSA 도입으로 바뀌는 책임경계와 3인 수행 가능성을 기준으로 Phase 2 P0/P1을 다시 고정하고, P1이 P0 Gate를 역으로 차단하는 의존성을 제거한다.
- **프로젝트 가치:** 재현성, 추적성, 무결성
- **완료 판정 원칙:** Source → Apply → Runtime → Positive/Negative/Recovery → Evidence를 구분하며 STATIC/MOCK/CI를 Runtime PASS로 확대하지 않는다.

이번 검수는 GitHub Issue의 최신 본문/라벨/의존성과 v3.1.20 §1.4 Phase 2 목표를 대조했다. ROSA 제품 동작은 Red Hat 공식 문서의 현재 ROSA 4 문서를 확인했다.

공식 참조:
- ROSA architecture models: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/introduction_to_rosa/rosa-architecture-models
- ROSA Terraform: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/install_clusters/creating-a-red-hat-openshift-service-on-aws-cluster-with-terraform
- ROSA monitoring: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/epub/monitoring/getting-started
- ROSA OADP: https://docs.redhat.com/en-us/documentation/red_hat_openshift_service_on_aws/4/pdf/backing_up_and_restoring_applications/Red_Hat_OpenShift_Service_on_AWS-4-Backing_up_and_restoring_applications-en-US.pdf

## 2. Priority 재정의

### P0 — Project Success / Gate Critical

아래 중 하나라도 해당하면 P0다.

1. v3.1.20 §1.4의 Phase 2 핵심 성공체인에 직접 필요
2. 다른 P0 구현을 시작하기 위한 필수 Decision
3. G4/G5/G6/Deliverable Freeze/Review/Close의 실제 Gate
4. 없으면 Hybrid Demo 또는 Source→Runtime→Evidence 체인이 성립하지 않음

P0 기술 핵심 체인:

```text
P2-ARC-01
  → P2-IAC-01
  → P2-OCI-01 Go/No-Go
  → P2-VPN-01
  → P2-ROSA-01
  → DEC-P2-REG-01
  → P2-APP-01
  → P2-CICD-01
  → P2-HYB-01
  → P2-E2E-01
  → P2-DOC-01 / Review / Close
```

### P1 — Enhancement / Conditional / Deferred

- P0 Hybrid E2E 없이도 Project Close 가능
- 운영 완성도, HA, Backup, DNS 편의성, Operator mirror, 추가 제품 등
- P1 미완료는 P0 Gate를 자동 차단하지 않음
- 실행하지 않는 경우 `Deferred / N/A / Cancelled` 근거와 Owner/Due를 남김
- 새로운 P1을 P0로 승격할 때는 Change Request 및 인력/일정 영향 검토가 필요

## 3. Phase 2 전체 Priority 판정

| Issue | Record | 기존 | 판정 | Gate 영향 | 검수 결과 |
|---:|---|---|---|---|---|
| #33 | MS-P2-START-01 | P0 | **P0 유지** | Start | Phase 2 착수/범위/권한 확인 |
| #34 | P2-ARC-01 | P0 | **P0 유지** | Start/G4 | HCP/Classic, API/Ingress, Region/AZ, 책임경계 Freeze 필요 |
| #35 | P2-IAC-01 | P0 | **P0 유지** | G4 | AWS+ROSA provisioning 재현성의 Source of Truth |
| #36 | P2-OCI-01 | P0 | **P0 유지** | G4 | OCI 실행 강제가 아니라 Primary/Fallback 선택 Decision이 P0 |
| #37 | P2-VPN-01 | P0 | **P0 유지** | G4 | 승인 단일 Transit/VPN 경로 필수 |
| #38 | P2-ROSA-01 | P0 | **P0 유지** | G5 | Platform/Security Runtime 필수 |
| #39 | MS-G4-01 | P0 | **P0 유지** | Gate | Cloud/VPN 준비 Gate |
| #40 | DEC-P2-DNS-01 | P1 | **P1 유지** | Non-blocking | P0는 IP Endpoint 허용, Hybrid DNS는 선택 |
| #41 | DEC-P2-OP-01 | P1 | **P1 유지** | Non-blocking | Direct/Mirror Decision; P1 Operator 실행 경로 |
| #42 | DEC-P2-REG-01 | P0 | **P0 유지** | G5 | App/CI가 사용할 단일 image source 결정 필수 |
| #43 | P2-APP-01 | P0 | **P0 유지** | G5 | ROSA workload/Route/Rules 필수 |
| #44 | P2-OADP-01 | P0 | **P1로 하향** | **G6 비차단** | Backup/Restore는 중요하나 §1.4 최소 Hybrid E2E 필수조건 아님 |
| #45 | MS-G5-01 | P0 | **P0 유지** | Gate | Platform+App+CI/CD Gate |
| #46 | P2-CICD-01 | P0 | **P0 유지** | G5 | §1.4 Runner-based ROSA Delivery 직접 요구 |
| #47 | P2-HYB-01 | P0 | **P0 유지** | G6 | ROSA→On-Prem DB 통합 핵심 |
| #48 | P2-DNS-01 | P1 | **P1 유지** | Non-blocking | D23 선택 시에만 구현 |
| #49 | P2-DOC-01 | P0 | **P0 유지** | Freeze | As-built/Evidence/Runbook 필수 |
| #50 | P2-E2E-01 | P0 | **P0 유지** | G6 | Hybrid 성공의 최종 기술 인수 |
| #51 | P2-OP-01 | P1 | **P1 유지** | Non-blocking | D26 Mirror 선택 시에만 구현 |
| #52 | DEC-CAL-P2-01 | P0 | **P0 유지(거버넌스)** | Review | 기술범위는 아니나 Close 일정 확정 필요 |
| #53 | MS-G6-01 | P0 | **P0 유지** | Gate | Hybrid Integration Gate. OADP P1 제거 |
| #54 | MS-DELIVERABLE-FREEZE-01 | P0 | **P0 유지** | Gate | 최종 버전/Decision/Known Issue Freeze |
| #55 | P2-REV-01 | P0 | **P0 유지** | Close | Review/비용/리소스 정리 |
| #56 | MS-P2-REVIEW-01 | P0 | **P0 유지** | Gate | Review milestone |
| #57 | MS-PROJECT-CLOSE-01 | P0 | **P0 유지** | Gate | 최종 Close |
| #95 | DEC-P2-RHOAI-01 | P1 | **P1 유지 / Deferred 우선** | Non-blocking | AI Inference Scope Out과 연결, 10/26 전 구현 기본계획에서 제외 |
| #120 | DEC-P2-GITOPS-01 | 신규 | **P1** | Non-blocking | Go 시 #46 Delivery Contract CR 필요; 미결정이면 Runner direct 유지 |
| #121 | DEC-P2-COMP-01 | 신규 | **P1** | Non-blocking | ROSA 보안 점검 고도화; HCP scheduling/managed boundary 반영 |

## 4. Phase 1 P1 carry-over 3건

기존 Record ID는 이력 추적을 위해 유지하고, GitHub Phase/Milestone만 Phase 2로 이동한다.

| Issue | 기존 | 적용 | ROSA 기준 |
|---:|---|---|---|
| #25 P1-MON-02 | Phase 1 / P1 | **Phase 2 / P1 / G6 non-blocking** | 자체 Prometheus HA 복제 대신 ROSA User Workload Monitoring 우선 |
| #26 P1-DR-02 | Phase 1 / P1 | **Phase 2 / P1 / G6 non-blocking** | On-Prem Harbor DR 조건부, kubeadm etcd는 ROSA AC에서 제외, app backup은 #44 |
| #27 P1-HA-02 | Phase 1 / P1 | **Phase 2 / P1 / G6 non-blocking** | HCP control-plane 직접 장애주입 제외, worker/machine-pool/workload resilience 중심 |

적용된 GitHub metadata:
- #25/#26/#27: `phase:phase-2`, `priority:P1`, Milestone = G6
- #44: `priority:P1`

## 5. ROSA 공통 구현 기준

모든 ROSA 연결 티켓은 아래 기준을 공유한다.

1. **Managed boundary**
   - HCP 사용 시 control plane/API server/etcd는 Red Hat 소유 AWS 계정의 관리영역
   - worker/machine pool, workload, 프로젝트 AWS 자원은 Customer-managed 범위로 구분
2. **Provisioning**
   - #35를 AWS/ROSA provisioning Source of Truth로 사용
   - #38은 Namespace/RBAC/SCC/NetworkPolicy/Access/Runtime configuration과 validation 담당
3. **Security**
   - STS/OIDC, 최소권한 IAM/Operator Role, RBAC/SCC, NetworkPolicy, TLS/Trust, Secret 비노출
4. **Source→Runtime**
   - Terraform/Commit/Manifest/Image Digest/Operator Version을 실제 Cluster ID/Version/Object/ImageID와 연결
5. **Failure/Recovery**
   - 정상 경로뿐 아니라 DENY, timeout, route/tunnel 장애, worker failure, rollback/recreate 검증
6. **Evidence**
   - 실행 시각, 대상, Source SHA, 명령/Run ID, RC, 원본 로그, Artifact SHA-256 보존

## 6. 전수 검수에서 발견한 의존성 정정

이번에 GitHub Issue 본문에 즉시 반영:

- #45 G5: `P2-CICD-01`을 Blocked By에 추가
- #44 OADP: P1 / G6 non-blocking으로 변경, 실행 시 D26 Operator 경로 참조
- #49 Deliverable Freeze: #44 OADP를 필수 Blocked By에서 제거
- #50 E2E: #44 OADP를 필수 Blocked By에서 제거
- #53 G6: #44 OADP를 필수 Blocked By/Exit Criteria에서 제거하고 실행 시 결과 또는 Deferred/N/A만 요구
- #54 Deliverable Freeze: Related Decision에 D25/D26 누락을 보완

차기 Ticket Pack 재생성 시 위 Issue 최신 본문을 Source로 수집한다.

## 7. 추가 ROSA 정제 대상 — Priority는 유지

Priority 변경 없이 정본 후보에서 상세화할 항목:

- **#34:** HCP/Classic, public/private API·Ingress, Region/AZ, CIDR, managed/customer boundary
- **#35/#38:** Terraform provisioning과 platform configuration 책임 분리
- **#37/#47:** ROSA 실제 egress/source를 목적지에서 관측 후 allowlist 확정
- **#40/#48:** DNS Operator / Route 53 Resolver / IP fallback을 방향별로 구분
- **#41/#51:** Direct catalog vs mirror, custom CatalogSource, trust/image mirror, recreate 절차
- **#43:** arbitrary UID/SCC/OpenShift security adapter, #119 fail-open CR 승인상태 반영
- **#44:** OADP STS/OIDC/IAM Role/S3/Restore, control-plane etcd와 구분
- **#46:** Direct Runner deploy와 OpenShift GitOps 중 단일 Delivery Contract 확정. GitOps는 별도 승인 전 P0 요구로 확대하지 않음
- **#50:** Route→transaction-api→fds-engine→On-Prem DB + DENY + tunnel recovery + recreate regression
- **#55/#57:** Cluster/MachinePool/NAT/LB/EBS/S3/VPN/Resolver 잔존 비용과 삭제 evidence

## 7.1 선택 제품 유입 결정 — 2026-09-30

- 추가 절차 간소화안은 **미적용 / 현행 유지 / 후속 재검토**.
- 활성 추가 제품 검토:
  - #120 OpenShift GitOps(Argo CD) — P1, non-blocking
  - #121 Compliance Operator — P1, non-blocking
- #120 Go 전에는 #46 Runner direct deploy를 유지한다. Go 시 Delivery Contract 변경 CR이 필요하다.
- #121 Go 전에는 #38 P0 Security AC를 유지한다. Compliance 결과를 자동 P0 blocker나 규제 준수 인증으로 확대하지 않는다.
- 상세: `audit/phase2-product-intake-20260930/README.md`

## 8. P0 WIP 통제

Open P0 개수 자체가 많아도 Milestone/Review Ticket과 기술 구현을 같은 WIP로 취급하지 않는다.

### 기술 P0 실행 큐

1. #34 Architecture
2. #35 IaC
3. #36 OCI Go/No-Go
4. #37 VPN
5. #38 ROSA
6. #42 Registry Decision
7. #43 App
8. #46 CI/CD
9. #47 Hybrid
10. #50 E2E
11. #49 Documentation/Freeze 준비

동시에 3개 이상 신규 기술 P0를 벌이지 않고, 각 담당자당 활성 핵심 작업 1개를 기본으로 한다.

### P1 실행 원칙

#25/#26/#27/#40/#41/#44/#48/#51/#95/#120/#121은 P0 완료를 침범하지 않는 범위에서만 수행한다.
10/26 이전 시간이 부족하면 Deferred/N/A/Cancelled 근거만 정리하고 구현을 강행하지 않는다.

## 9. 정본 반영 경계

이 검수에서 **실제 적용한 것**:
- Issue metadata/priority/dependency 정정
- Phase 2 carry-over 3건 이동
- P0/P1 policy와 ROSA scope review를 Draft PR #112에 수집

아직 **미완료**:
- 후보 WBS의 Priority/Phase/Milestone 셀 재생성
- Baseline/Ticket Pack/Description 전체 재생성
- 일정 Working Days 재계산
- Manifest/SHA256SUMS/ZIP/WEB snapshot
- Review/Merge/Tag/Release

Workbook은 기존 후보 바이너리를 임의 패치하지 않고 전체 canonical regeneration 시 Source Issue 최신값으로 재생성한다.
