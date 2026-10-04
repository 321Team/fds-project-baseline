# Issue Body Addenda Candidate — Supplied OpenShift Lab Precheck

> 대상 PR: #112 / branch release/v3.1.21
> 기준일: 2026-09-30 KST
> 상태: **CANDIDATE / HUMAN APPLY REQUIRED**
> 증적 경계: 현재 근거는 사용자 제공 read-only capture와 PR 감사 요약이며, 원본 출력의 fds-project-evidence 독립 편입은 아직 수행하지 않았다. 따라서 본 addendum은 Runtime Acceptance 증적이 아니다.
>
> governance/TICKET_SYNC_POLICY.md §5.1에 따라 AI가 Issue 본문 절/문단을 직접 추가하지 않는다. 아래 블록은 담당자가 최신 Issue 원문과 updated_at을 재확인한 뒤 수동 적용할 후보 문안이다. 적용 자체가 AC 충족·승인·종결을 의미하지 않는다.

## #120 DEC-P2-GITOPS-01

권장 삽입 위치: Decision Control 앞.

~~~markdown
<!-- fds-ocp-lab-precheck:20260930:gitops:start -->
## Supplied OCP Lab Precheck — 2026-09-30 KST

교육기관 제공 OCP 4.20.0 환경에서 read-only 사전조사를 수행했다.

- Red Hat redhat-operators CatalogSource: READY
- openshift-gitops-operator: catalog available
- Default channel: latest
- Current CSV: openshift-gitops-operator.v1.21.4
- InstallMode: AllNamespaces=true; OwnNamespace/SingleNamespace/MultiNamespace=false
- 현재 CSV/Subscription 기준 OpenShift GitOps는 **미설치**
- 사용자 계정은 기술적으로 광범위한 cluster-wide 권한을 보유하지만 공급자 변경 승인은 **미확인**
- Worker memory request snapshot은 68% / 73%로 신규 Operator 병행 설치에 보수적 접근이 필요함

판정:
- Catalog/Package 사전확인: **LAB-RUNTIME/PRECHECK PASS**
- GitOps Operator Runtime: **NOT RUN**
- Shared Lab 신규 설치: **HOLD — 공급자 정책 확인 대기**
- 실제 P2 도입 결정: **PENDING / P1 non-blocking**
- #120 Go 전 #46 Runner direct deploy 계약 유지
- 이 Lab 결과는 ROSA HCP/IAM/STS/AWS/VPN 또는 최종 GitOps Runtime 검증을 대체하지 않음
<!-- fds-ocp-lab-precheck:20260930:gitops:end -->
~~~

## #121 DEC-P2-COMP-01

권장 삽입 위치: Decision Control 앞.

~~~markdown
<!-- fds-ocp-lab-precheck:20260930:compliance:start -->
## Supplied OCP Lab Precheck — 2026-09-30 KST

교육기관 제공 OCP 4.20.0 환경에서 read-only 사전조사를 수행했다.

- Red Hat redhat-operators CatalogSource: READY
- compliance-operator: catalog available
- Default channel: stable
- Current CSV: compliance-operator.v1.10.0
- InstallMode: OwnNamespace/SingleNamespace/MultiNamespace/AllNamespaces=true
- 현재 CSV/Subscription 기준 Compliance Operator는 **미설치**
- Namespace install mode 지원은 실제 ComplianceScan 대상이 Namespace에만 제한됨을 의미하지 않음
- Node/Platform/Cluster scan 및 remediation은 공급자 정책 확인 전 실행하지 않음
- Worker memory request snapshot은 68% / 73%

판정:
- Catalog/Package 사전확인: **LAB-RUNTIME/PRECHECK PASS**
- Compliance Operator Runtime/Scan: **NOT RUN**
- Shared Lab 설치/scan: **HOLD — 공급자 정책 확인 대기**
- 실제 P2 도입 결정: **PENDING / P1 non-blocking**
- 자동 remediation은 이번 precheck 범위 밖
- 실제 ROSA/HCP scheduling/scan 결과는 별도 Runtime 검증 대상
<!-- fds-ocp-lab-precheck:20260930:compliance:end -->
~~~

## #34 P2-ARC-01

~~~markdown
<!-- fds-ocp-lab-precheck:20260930:arc:start -->
## Supplied OCP Lab Architecture Precheck — 2026-09-30 KST

OCP 4.20.0 교육 Lab에서 API/Auth/Node/Catalog 가용성을 read-only로 확인했다. 이 결과는 OpenShift 공통 호환성 사전자료이며 P2 Architecture Freeze의 AWS ROSA/HCP, IAM/STS, OCI/VPN, Region/AZ, API/Ingress 결정을 대체하지 않는다.

GitOps(#120)와 Compliance(#121)는 P1 optional Decision을 유지한다. 공급자 정책 확인 전 공용 Lab의 cluster-wide 변경은 수행하지 않으며, Lab은 우선 namespace-contained application compatibility 용도로 사용한다.
<!-- fds-ocp-lab-precheck:20260930:arc:end -->
~~~

## #38 P2-ROSA-01

~~~markdown
<!-- fds-ocp-lab-precheck:20260930:rosa:start -->
## Supplied OCP Lab Precheck Boundary — 2026-09-30 KST

교육 Lab에서 OCP 4.20 API/Auth/Node Ready 및 Red Hat Operator Catalog 접근을 확인했다. 이는 **LAB-RUNTIME/PRECHECK**이며 실제 AWS ROSA Cluster Ready, STS/IAM, HCP scheduling, Hybrid Route, P2 security AC 또는 G5 Runtime PASS로 승격하지 않는다.

GitOps/Compliance Operator는 현재 Lab에 설치되어 있지 않으며, #120/#121 Decision 및 공급자 정책 확인 전 설치/scan을 수행하지 않는다.
<!-- fds-ocp-lab-precheck:20260930:rosa:end -->
~~~

## #41 DEC-P2-OP-01

~~~markdown
<!-- fds-ocp-lab-precheck:20260930:opsupply:start -->
## Operator Catalog Precheck — 2026-09-30 KST

교육 OCP Lab에서 redhat-operators CatalogSource가 READY이고 GitOps/Compliance package가 노출됨을 확인했다. 이는 **Direct Catalog path의 Lab 가용성**만 확인한 결과다.

D26의 P2 실제 공급방식(Direct vs Mirror)은 AWS ROSA의 실제 egress/보안/운영 조건을 기준으로 별도 결정한다. Lab Catalog 가용성만으로 Mirror를 N/A 처리하거나 P2 공급경로를 확정하지 않는다.
<!-- fds-ocp-lab-precheck:20260930:opsupply:end -->
~~~

## #46 P2-CICD-01

~~~markdown
<!-- fds-ocp-lab-precheck:20260930:cicd:start -->
## GitOps Lab Precheck Impact — 2026-09-30 KST

OpenShift GitOps package 가용성은 확인했지만 현재 Lab의 GitOps 1.21.4는 AllNamespaces install mode만 지원하며 Operator는 미설치다. 공용 Lab 공급자 정책 확인 전 설치하지 않는다.

따라서 #120 Go/별도 CR 전까지 본 티켓의 P0 기준은 기존 **Runner direct ROSA Delivery**로 유지한다. GitOps 미설치는 #46 P0 AC 실패 또는 G5/G6 blocker가 아니다.
<!-- fds-ocp-lab-precheck:20260930:cicd:end -->
~~~

## #49 P2-DOC-01

~~~markdown
<!-- fds-ocp-lab-precheck:20260930:doc:start -->
## OpenShift Lab Evidence Classification — 2026-09-30 KST

교육 OCP 결과는 최종 문서에서 LAB-RUNTIME/PRECHECK로 표시하고 실제 ROSA Runtime과 구분한다. GitOps/Compliance는 Catalog/InstallMode 확인과 Operator Runtime/Scan 실행 여부를 별도로 기록한다.

공급자 정책 답변과 #120/#121 최종 Adopt/Deferred/No-Go 상태를 최종 산출물에 추적하되, 미실행 Operator를 PASS로 표기하지 않는다.
<!-- fds-ocp-lab-precheck:20260930:doc:end -->
~~~

## #53 MS-G6-01

~~~markdown
<!-- fds-ocp-lab-precheck:20260930:g6:start -->
## Optional Operator Gate Boundary — 2026-09-30 KST

#120 GitOps와 #121 Compliance는 P1 / G5·G6 non-blocking을 유지한다. 교육 Lab의 Operator 미설치 또는 공급자 정책 대기는 G6 실패 조건으로 추가하지 않는다.

P1 미수행 시 Deferred/N/A/Cancelled 근거와 Owner/Due를 문서화하며, G6는 기존 P0 AC와 실제 ROSA/Hybrid/E2E 증적으로 판정한다.
<!-- fds-ocp-lab-precheck:20260930:g6:end -->
~~~

## 적용 전 재확인

- #34: updated_at 2026-09-30T08:59:02Z — [P2-ARC-01] Hybrid / OCI / AWS / ROSA Architecture Freeze
- #38: updated_at 2026-09-30T08:59:46Z — [P2-ROSA-01] ROSA Platform / Security
- #41: updated_at 2026-09-30T09:00:04Z — [DEC-P2-OP-01] Operator Supply Chain Scope Decision
- #46: updated_at 2026-09-30T09:00:40Z — [P2-CICD-01] Runner to ROSA Delivery
- #49: updated_at 2026-09-30T09:01:09Z — [P2-DOC-01] Cloud / Hybrid Deliverable Freeze
- #53: updated_at 2026-09-30T09:01:24Z — [MS-G6-01] G6 Hybrid Integration Ready
- #120: updated_at 2026-09-30T09:06:38Z — [DEC-P2-GITOPS-01] OpenShift GitOps (Argo CD) 도입 범위 결정
- #121: updated_at 2026-09-30T09:06:45Z — [DEC-P2-COMP-01] Compliance Operator 도입 범위 결정

적용 시점에 위 값과 최신 GitHub updated_at이 다르면 원문을 다시 읽고 후보를 재검토한다.
