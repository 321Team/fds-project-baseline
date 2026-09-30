# Supplied OpenShift Lab Precheck — 2026-09-30 KST

## 1. 목적과 판정 경계

이 기록은 교육기관이 제공한 OpenShift Cluster를 사용한 read-only 사전조사 결과를 차기 정본 후보 PR #112에 수집한다.

- 현행 정본: docs-v3.1.20 / RELEASED
- 후보 브랜치: release/v3.1.21
- 대상 Decision: #120 DEC-P2-GITOPS-01, #121 DEC-P2-COMP-01
- 연계: #34, #38, #41, #46, #49, #53
- 분류: **LAB-RUNTIME / PRECHECK**
- **ROSA Runtime PASS, Operator Runtime PASS, 도입 승인, 공급자 변경 승인으로 확대하지 않는다.**
- 사용자 제공 read-only 출력에는 정확한 실행 시각이 포함되지 않아 기준일만 2026-09-30 KST로 기록한다.

## 2. 환경 사실

확인된 Lab 환경:

- OpenShift Container Platform: **4.20.0**
- Kubernetes: **v1.33.5**
- 설치 형태: **UPI Baremetal**
- 사용자 OAuth identity: admin
- oc auth can-i '*' '*' --all-namespaces = **yes**
- namespace/project 생성 및 Operator Subscription/ClusterRoleBinding 생성 권한 = **yes**
- 이 권한은 **기술적 capability**이며 교육기관/공급자의 **변경 승인**과 동일하지 않다.
- 사용자 workload용 ResourceQuota/LimitRange는 별도로 관찰되지 않았다.
- Worker memory request snapshot:
  - worker-1: **4677Mi / 68%**
  - worker-2: **5011Mi / 73%**
- 따라서 공용 Lab에서 신규 Operator를 여러 개 동시에 설치하는 것은 자원·영향 측면에서 보수적으로 판단한다.

## 3. Operator 설치 현황과 Catalog

### 설치 현황

oc get csv -A에서 사용자 설치 Operator는 관찰되지 않았고, 기본 packageserver만 확인됐다.

oc get subscriptions.operators.coreos.com -A 결과: **No resources found**.

따라서:

- OpenShift GitOps: **NOT INSTALLED**
- Compliance Operator: **NOT INSTALLED**
- Operator Runtime: **NOT RUN**

### CatalogSource

redhat-operators CatalogSource:

- Display: Red Hat Operators
- Type: grpc
- Publisher: Red Hat
- .status.connectionState.lastObservedState: **READY**

따라서 Red Hat Catalog 접근은 **LAB-RUNTIME/PRECHECK PASS**로 기록한다.

## 4. OpenShift GitOps 조사 결과

Package: openshift-gitops-operator

- Provider: Red Hat
- Default channel: **latest**
- Current CSV: **openshift-gitops-operator.v1.21.4**
- InstallModes:
  - OwnNamespace: **false**
  - SingleNamespace: **false**
  - MultiNamespace: **false**
  - AllNamespaces: **true**

판정:

1. 해당 Lab에서 Red Hat GitOps package **가용성은 확인**됐다.
2. 현재 package는 **AllNamespaces 설치만 지원**하므로 우리 팀 Namespace에 Operator 자체를 격리 설치하는 방식은 사용할 수 없다.
3. 공용 Cluster로 보이는 환경에서 사용자 단독 판단으로 설치하지 않는다.
4. #120의 제품 도입 여부는 여전히 **P1 / PENDING DECISION**이다.
5. #120 Go 전에는 #46 **Runner direct deploy**를 P0 기준선으로 유지한다.
6. 이 Lab 결과는 제품 가용성/설치 특성 사전조사이며 **ROSA HCP/IAM/STS/AWS/VPN/GitOps Runtime 검증을 대체하지 않는다.**

현재 권고 상태: **SHARED-LAB INSTALL HOLD / PROVIDER POLICY PENDING**.

## 5. Compliance Operator 조사 결과

Package: compliance-operator

- Provider: Red Hat
- Default channel: **stable**
- Current CSV: **compliance-operator.v1.10.0**
- InstallModes:
  - OwnNamespace: **true**
  - SingleNamespace: **true**
  - MultiNamespace: **true**
  - AllNamespaces: **true**

판정:

1. 해당 Lab에서 Red Hat Compliance package **가용성은 확인**됐다.
2. Namespace 범위 설치 mode가 지원되므로 GitOps보다 Operator 설치 격리 선택지는 넓다.
3. 그러나 InstallMode는 Operator의 설치/watch 범위이며 **ComplianceScan의 실제 Node/Platform/Cluster 대상 범위와 동일하지 않다.**
4. 공용 Cluster에서 Node/Platform scan, remediation, MachineConfig 등은 공급자 허용범위 확인 전 실행하지 않는다.
5. #121의 제품 도입 여부는 여전히 **P1 / PENDING DECISION**이다.
6. 자동 remediation은 본 precheck 범위가 아니며 실행하지 않았다.
7. 실제 ROSA/HCP에서의 지원·scheduling·scan은 별도 Runtime 검증 대상이다.

현재 권고 상태: **SHARED-LAB INSTALL/SCAN HOLD / PROVIDER POLICY PENDING**.

## 6. 공용 Lab 사용 경계

공급자 답변 전 권장 경계:

- 우선 수행 후보: 팀 전용 Project/Namespace 내 transaction-api, fds-engine의 OpenShift 호환성 확인
- 확인 항목: arbitrary UID/SCC 호환, SecurityContext, Service/Route, Probe, ServiceAccount/RBAC, NetworkPolicy, restart/recovery
- 금지/보류: 신규 GitOps Operator 설치, Compliance Operator 설치/scan, SCC 변경, ClusterRoleBinding 변경, MachineConfig, StorageClass, Node drain/reboot, Cluster Operator 변경
- Lab 결과 표기는 **LAB-RUNTIME/PRECHECK**로 제한한다.

공급자 확인 필요:

1. 팀 전용 Project/Namespace 생성 허용 여부 및 naming/resource 정책
2. GitOps/Compliance Operator 설치 허용 여부
3. Compliance의 Node/Platform/Cluster scan 허용 범위
4. Cluster-wide 설정 변경의 승인 절차

## 7. 검증 단계

| 단계 | 상태 | 근거/한계 |
|---|---|---|
| STATIC | PASS | PackageManifest/InstallMode metadata 확인 |
| LAB-RUNTIME | PASS(PRECHECK) | API/Auth/CatalogSource/Package visibility/read-only 조회 |
| Operator Runtime | NOT RUN | GitOps/Compliance 미설치 |
| App Compatibility | NOT RUN | 팀 Namespace 정책 답변 대기 |
| ROSA Runtime | NOT RUN | 실제 AWS ROSA 별도 |
| REVIEW | THIS PR CANDIDATE | 독립 리뷰 전 정본 아님 |
| MERGE | NOT DONE | PR #112 Draft |
| PUBLICATION | NOT DONE | docs-v3.1.20 유지 |

## 8. 티켓 반영 정책

직접 Issue 본문 쓰기는 governance/TICKET_SYNC_POLICY.md §5.1에 따라 AI 도구가 수행하지 않는다.

대신 이 PR에 ticket-body-addenda.md를 포함해 #120/#121 및 연계 티켓에 적용할 **정확한 addendum 후보**를 제공한다. 담당자가 반영 직전에 최신 updated_at과 원문을 다시 확인하고 수동 반영한다.

Source issue snapshot (이 PR 작성 직전 조회):

- #34: updated_at 2026-09-30T08:59:02Z — [P2-ARC-01] Hybrid / OCI / AWS / ROSA Architecture Freeze
- #38: updated_at 2026-09-30T08:59:46Z — [P2-ROSA-01] ROSA Platform / Security
- #41: updated_at 2026-09-30T09:00:04Z — [DEC-P2-OP-01] Operator Supply Chain Scope Decision
- #46: updated_at 2026-09-30T09:00:40Z — [P2-CICD-01] Runner to ROSA Delivery
- #49: updated_at 2026-09-30T09:01:09Z — [P2-DOC-01] Cloud / Hybrid Deliverable Freeze
- #53: updated_at 2026-09-30T09:01:24Z — [MS-G6-01] G6 Hybrid Integration Ready
- #120: updated_at 2026-09-30T09:06:38Z — [DEC-P2-GITOPS-01] OpenShift GitOps (Argo CD) 도입 범위 결정
- #121: updated_at 2026-09-30T09:06:45Z — [DEC-P2-COMP-01] Compliance Operator 도입 범위 결정

## 9. 재현용 read-only 조회

~~~powershell
$OC="$env:USERPROFILE\oc-cli\oc.exe"

& $OC get csv -A
& $OC get subscriptions.operators.coreos.com -A
& $OC get catalogsource redhat-operators -n openshift-marketplace -o wide
& $OC get catalogsource redhat-operators -n openshift-marketplace -o jsonpath='{.status.connectionState.lastObservedState}'

$g = (& $OC get packagemanifest openshift-gitops-operator -n openshift-marketplace -o json) | ConvertFrom-Json
$c = (& $OC get packagemanifest compliance-operator -n openshift-marketplace -o json) | ConvertFrom-Json

$gc = $g.status.channels | Where-Object { $_.name -eq $g.status.defaultChannel }
$cc = $c.status.channels | Where-Object { $_.name -eq $c.status.defaultChannel }

$g.status.defaultChannel
$gc.currentCSV
$gc.currentCSVDesc.installModes | Format-Table type,supported -AutoSize

$c.status.defaultChannel
$cc.currentCSV
$cc.currentCSVDesc.installModes | Format-Table type,supported -AutoSize
~~~

이 조회는 변경 없이 Catalog/Package metadata만 확인한다.
