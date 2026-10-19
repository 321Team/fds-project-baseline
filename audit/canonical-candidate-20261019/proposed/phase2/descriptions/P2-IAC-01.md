<!-- cost-review-20261012:start -->
## 비용 책임·리뷰 적용 기준 — 2026-10-12 사용자 결정

[중앙 기준 및 과거 리뷰 정정](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6119458420)을 적용합니다. 아래 과거 본문/댓글의 비용 요구와 다르면 이 기준으로 책임·제출 범위를 해석합니다.
- **교육장 리포트 확보·사용액/예상 총액·비용 GO/중단 판단: 이권욱.** 구축 담당자는 예상 자원/수량·대략 가동/정리안·잔존 자원·변경 사항을 기존 자료로 인계합니다.
- 자체 단가표·상세 재견적·모든 절감안·사전 actual ID 전수 확정을 요구하지 않습니다. 비용 대기만으로 준비 산출물을 반려하지 않습니다.
- 본문의 ‘공식 단가 + projected/unbilled/teardown’ 자체 계산을 담당자의 필수 제출물로 요구하지 않습니다. subnet 태그 변경은 별도 비용 심사 없이 기술 Plan/소유권 검증으로 처리합니다.
- 현재 단계의 필수 기술 검증만 차단조건으로 적용합니다. 기존 증적/승인은 재사용하고 변경 영향만 재검토합니다. Terraform Plan은 실제 변경 검증이며 다른 도구에 일률 요구하지 않습니다.
- 기존 한도·유효 승인 범위·독립 리뷰·무결성/추적성/재현성/이식성 및 Phase 1 운영/AC 경계를 유지합니다. 새 비용·Apply·Create·삭제 GO나 티켓 종결이 아닙니다.
<!-- cost-review-20261012:end -->

<!-- cost-owner-20261009:start -->
## 비용 판정 책임 — 2026-10-09 사용자 결정

- **비용 판정·Cost GO/NO_GO·한도 초과 및 후속 절차 결정은 이권욱(@GWONUK) 담당.** [중앙 결정 기록](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6073631202)을 따릅니다.
- 교육장 지원 확정·팀 자부담0. 사용액/예상 총비용은 교육장 리포트 기준이며 USD400 목표 / 450 중단 / 500 상한은 유지합니다.
- 구현 담당자는 자기 범위의 자원·수량·운영/삭제 일정안 등 기술 입력을 인계합니다. 비용 판정 대기만으로 완료된 사전조사·정적 검증·코드 산출물을 반려하지 않습니다.
- 실제 유료 실행 및 G4/Create Gate의 비용 판단은 이권욱/#34 결과를 소비합니다. 이번 책임 이관은 Cost GO나 실행 승인이 아닙니다.
<!-- cost-owner-20261009:end -->

<!-- fds-canonical-live:v3.1.21 record-id:P2-IAC-01:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/P2-IAC-01.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 관련 추적 항목 **TS01, TS04**. 원본 AC와 각 항목의 환경·선행조건·중단/복구·증적 기준을 함께 적용한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:P2-IAC-01:end -->

<!-- p2-iac-d21-handoff-20261003:v1:start -->
## 2026-10-03 D21 → P2-IAC Stage-A 권위 Handoff

> 이 블록은 아래 과거 `VPN attachment type/identity=PENDING`, `VGW/TGW` 전제보다 우선한다. D21은 managed S2S attachment가 아니라 self-managed Transport Adapter를 선택했다.

### Transport Adapter
- `transport_adapter_type = "aws_ec2_eip_relay"`
- managed `vpn_attachment_type (vgw|tgw)` = **NOT APPLICABLE for selected D21 path**
- AWS Site-to-Site VPN quota exact read-back = **selected path의 Stage-A blocker 아님**
- Region: `ap-northeast-2`
- VPC: `10.20.0.0/16`
- Relay subnet: `10.20.110.0/24`
- Relay AZ / Zone ID: `ap-northeast-2a / apne2-az1`
- Relay private IP: `10.20.110.10`
- Instance: `t3.medium`
- AMI: `ami-079a2667364cee804`, owner `125523088429`
- Root: `gp3 40 GiB encrypted`
- EIP: 1; auto public IPv4 disabled
- ENI source/destination check: false
- public SSH: deny; management SSM/bootstrap
- SG public ingress: UDP/500·4500 only; source cannot depend on one observed /32
- selectors: `10.1.93.0/24 <-> 10.20.0.0/16`
- AWS route authority: Terraform; `10.1.93.0/24 -> Relay ENI`

### Subnet/AZ map
- private-a: `10.20.10.0/24` / `ap-northeast-2a` / `apne2-az1`
- private-b: `10.20.20.0/24` / `ap-northeast-2b` / `apne2-az2`
- private-c: `10.20.30.0/24` / `ap-northeast-2c` / `apne2-az3`
- public-transport-a: `10.20.110.0/24` / `ap-northeast-2a` / `apne2-az1`

### State contract
- logical boundaries: `network / vpn / rosa-prereq / rosa-runtime` — CONFIRMED DESIGN BOUNDARY
- backend: S3 + native `use_lockfile=true`
- exact bucket / component state keys: **PENDING Stage-A**
- one shared `p2-iac/terraform.tfstate` key is not an approved final state model.

### #37 exact Stage-A artifact
Before #37 Runtime, provide actual IDs + exact source SHA:
1. VPC ID
2. subnet IDs + AZ Name/Zone ID
3. route-table IDs
4. Relay Instance ID / primary ENI ID / private IP
5. EIP allocation + public IP
6. SG ID and exact UDP/500·4500 rule read-back
7. `source_dest_check=false` read-back
8. route `10.1.93.0/24 -> Relay ENI`
9. state backend identity (secret 제외)
10. Terraform source SHA / plan evidence

### Execution boundary
- PR #3 schema must represent `transport_adapter_type`; `vgw|tgw`만 강제하면 D21과 충돌.
- Stage-A code/static validation은 가능하지만 MFA/backend exact identity/required approvals 이전 `apply` 금지.
- PLAN/APPLY/RUNTIME은 수행 결과가 있을 때만 상향한다.
<!-- p2-iac-d21-handoff-20261003:v1:end -->

<!-- phase2-execution-data-20261002:issue-35:v2:start -->
## 2026-10-02 #35 Bootstrap / Apply Gate v2

### AWS account / human identity
- 현재 작업 AWS Account는 Organizations **member account**이며 Management Account와 분리.
- Organization IAM Identity Center instance 존재/ACTIVE. 다만 현재 member-account root에서는 Permission Set/Assignment 관리 불가.
- 프로젝트 일정상 local IAM human user fallback 채택.
- Human users 3개: 생성 PASS.
- Console login profile: PASS x3 / 최초 비밀번호 변경 강제.
- Long-lived Access Key: **0 x3 / 기본 미발급 유지**.
- MFA: **PENDING/DEFERRED — privileged AssumeRole 사용 전 필수**.
- Work Role: **NOT ASSIGNED**.
- root 일상 사용 금지; root MFA=0은 외부 Owner 통제영역의 `EXTERNAL_RISK_NONBLOCKING`으로 기록.

### 권한 모델 — Apply 전 확정
- Human user에는 상시 Administrator 직접 부여 금지.
- 권한은 `FDS-*` AssumeRole 구조로 분리.
- 최소 후보 역할: `FDS-ReadOnly-Audit`, `FDS-IaC-Operator`, `FDS-Network-Operator`.
- Terraform Apply 전: 대상 Role policy/trust/MFA 조건과 실제 AssumeRole 성공 증적 필요.

### Toolchain / Audit / Cost
- Terraform CLI: **v1.16.4 / linux_amd64 / user-space install / SHA256 PASS**.
- 실제 source의 `required_version` / provider constraint는 코드 PR 독립리뷰 후 고정.
- CloudTrail Event History: PASS.
- durable account/org trail: **NOT OBSERVED** — 별도 장기 audit 통제로 자동 해석하지 않음.
- AWS Budget resource: **0**.
- Cost Explorer: member account에서 Organizations SCP explicit deny.
- 비용 GO는 Terraform resource inventory + 서울 Region 공식단가 + expected runtime + projected/unbilled/teardown residual + 제공 가능한 Daily Summary를 결합.

### Quota
- 일반 VPC quota 일부 read-back: VPC/Region=5, Subnet/VPC=200, RouteTable/VPC=200, SG/Region=2500, NATGW/AZ=5.
- EC2 Running On-Demand Standard quota (`L-1216C47A`): **100 vCPU CONFIRMED / Adjustable=True**. Quota change history: `DesiredValue=100 / CASE_CLOSED`.
- Site-to-Site VPN 관련 applied quota: **UNVERIFIED**.
- ROSA 별도 Service Quotas service code는 관측되지 않았으며 underlying EC2/VPC quota + ROSA prerequisite로 검증.
- 빈 결과를 quota=0으로 해석 금지.

### Terraform Apply 전 Hard Gate
다음이 모두 충족되기 전 `terraform apply`, Project VPC/VPN/ROSA create를 금지한다.
1. 3인 MFA read-back 완료
2. `FDS-*` Work Role 생성/최소권한 리뷰/AssumeRole 검증
3. backend/state locking/credential boundary 확정
4. Subnet/AZ/Route exact mapping 확정
5. VPN attachment/route authority 확정
6. EC2 Standard quota 100 vCPU read-back 유지 + Site-to-Site VPN 관련 applied quota exact read-back
7. topology(HCP/Classic)/Version/MachinePool + Cost GO
8. Terraform source SHA + fmt/validate + 독립 리뷰된 plan
9. expected cost/cleanup boundary

### 현재 Apply Readiness
`HUMAN_USERS=PASS / LOGIN_PROFILE=PASS / ACCESS_KEYS=0 / MFA=PENDING / WORK_ROLES=NOT_ASSIGNED / TERRAFORM_CLI=PASS / BACKEND_STATE=PENDING / EC2_STANDARD_QUOTA=100_PASS / VPN_QUOTA=UNVERIFIED / PLAN=NOT_RUN / APPLY=NOT_RUN`
<!-- phase2-execution-data-20261002:issue-35:v2:end -->

<!-- phase2-execution-data-20261002:issue-35:v1:start -->
## 2026-10-02 Execution Data / Review Contract — #35

### Ownership
- **Execution Lead / Runtime AC Acceptance:** 이하영
- **PMO/QA Review Owner:** 이권욱
- **Code/IaC Independent Review:** 이권욱 우선. 이권욱이 해당 변경 작성/실행에 참여한 경우 이재환 등 독립 Reviewer로 전환.
- **Evidence Independent Review:** 동일 독립성 규칙 적용.
- Support 역할은 Architecture/Cost/Plan 정합 지원이며 별도 상시 이중승인 조건이 아니다.

### Confirmed inputs
- AWS Region: `ap-northeast-2`
- Project VPC CIDR: `10.20.0.0/16` (**planned / not created**)
- Existing default VPC: `172.31.0.0/16`; project CIDR과 overlap 없음
- W0 inventory 기준 VGW/CGW/VPN/TGW/NATGW 및 project paid network resource: 0 관측
- #34의 Phase 2 구축 사양 권위표를 상위 입력으로 사용

### Stage-A 전에 확정해야 하는 값 — 임의 확정 금지
| 값 | 상태 | 확정 주체/시점 |
|---|---|---|
| Subnet CIDR / AZ | PENDING | 이하영 / Stage-A |
| Route table / route authority | PENDING | 이하영 + #34 / Stage-A |
| VPN attachment type/identity | PENDING | #34 Freeze → 이하영 / Stage-A |
| Terraform backend/state key/lock/secret boundary | PENDING | 이하영 / Stage-A |
| 실행 AWS identity/role 최소권한 | PENDING | 이하영 / plan 전 |
| ROSA topology/Region/Version | PENDING | #34 Freeze |
| MachinePool type/count | PENDING | #34 Freeze + 비용 입력 |

### Stage-A Handoff Artifact — #37 소비 필수
다음 값을 **actual ID/CIDR/Source SHA와 함께** 한 묶음으로 제공한다.
1. VPC ID/CIDR
2. Subnet ID/CIDR/AZ
3. Route Table ID + route authority
4. VPN attachment type/ID
5. Terraform source commit SHA
6. reviewed plan hash / plan evidence ref
7. State backend identity(Secret 제외)
8. Security boundary/SG input
9. Evidence ref
10. `STAGE_A_READY=YES|NO`

한 항목이라도 실제값이 없으면 `STAGE_A_READY=NO`이며 #37 Runtime apply 입력으로 사용하지 않는다.

### Full completion
IAM/OIDC/ROSA prerequisite, 최소권한, apply 결과, state 무결성, destroy/recreate/잔존 resource 확인과 G4 Evidence를 완료한다.

### 현재 Checkpoint
`W0_AWS_INVENTORY=COMPLETE / STAGE_A=NOT_READY / FULL_IAC=NOT_RUN / G4_ACCEPTANCE=NOT_READY`
<!-- phase2-execution-data-20261002:issue-35:v1:end -->

<!-- issue-execution-contract-20261001:v1:start -->
## 2026-10-01 IaC Execution Contract v1

### Entry
- #34 Architecture Freeze의 CIDR/Route/Security/Cost 입력 확정.
- Terraform backend/state/credential 저장경계와 실행 Account를 확인.

### Stage-A — 10-08 Handoff
- VPC/Subnet/Route/VPN attachment 입력과 state identity를 고정.
- `terraform fmt/validate/plan`과 secret/state 비노출 확인.
- #37가 소비할 값은 evidence/commit과 함께 인계한다.
- Stage-A는 #35 전체 PASS가 아니다.

### Full — 10-14
- IAM/OIDC/ROSA prerequisite, 최소권한, apply 결과, state 무결성 및 G4 Evidence 완료.
- Drift/재실행 시 destructive change가 발생하면 즉시 중단하고 plan 차이를 기록한다.

### Stop / Rollback
- 예상 밖 destroy/recreate, 과도한 IAM 권한, secret 평문 노출, 비용 Hard Stop 위험 시 apply 금지/중단.
- 성공 산출물은 exact source SHA + plan/apply RC + resource identity로 추적한다.
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
공용 OCP는 Terraform AWS/ROSA IaC의 대체 실행대상이 아니다. Provider-independent manifest/CLI 입력 검증은 가능하지만 AWS/ROSA apply·IAM/OIDC·State 인수 증적은 실제 대상 환경에서만 판정한다.



<!-- schedule-realign-20261001:issue-35:start -->
## 2026-10-01 일정·Dependency 정합화

- **Stage-A handoff (10-08):** VPC/Subnet/Route 및 #37이 소비할 VPN attachment 입력을 고정하고 Terraform state/secret 경계의 기본 검증을 완료한다. 이 checkpoint는 #37 착수용이며 #35 전체 완료로 해석하지 않는다.
- **Full completion (10-14):** IAM/OIDC/ROSA prerequisite, 전체 Terraform 검증과 G4 Evidence까지 완료한다.

- Scope/AC/Priority/Milestone/Review Authority 변경 없음.
- 일정 조정은 재현성·무결성·추적성을 유지하면서 P0 동시 WIP와 선행조건 역전을 제거하기 위한 PMO 조정이다.
<!-- schedule-realign-20261001:issue-35:end -->
<!-- fds-oci-schedule:20260924:v1:start -->
## OCI 연계 일정 정합화 — 2026-09-24 KST

사용자 “일정 불일치부터 해소” 지시에 따라 일정 표시와 기간 계산을 정정했다. [2026-09-22 재계획](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5779875658) 및 발행 docs-v3.1.20 WBS의 비근무일을 근거로 한다. 기존 10-06~10-09의 작업 가능일은 10-06·07·08의 3일이므로 **OCI 종료/D21 목표를 10-08로 통일**한다.

- **이 티켓의 계획:** 2026-10-06 ~ 2026-10-13 · 달력 8일 / 작업 5일. 10-06~10-13 계획. D21 목표는 10-08이며 Transit 의존 입력과 경로는 D21 결정 후 확정한다.
- **연계 목표:** Phase 2 착수/설계 10-06, D21 10-08, IaC 10-06~13, VPN 준비 10-08~13, G4 10-13. VPN 적용은 기존 선행조건 충족 후이며, IaC 완료 목표와 G4가 같은 날이므로 실제 적용·검증 작업창 확보를 확인해야 한다.
- 아래 이전 정본 머리말·마일스톤 배정·보관 원문의 과거 일정은 이력이다. 현행 계획 일정은 이 정정과 갱신한 티켓 속성표를 따른다. [정정 근거 및 차기 정본 반영안](https://github.com/321Team/fds-project-baseline/blob/docs/oci-schedule-align-20260924/audit/oci-schedule-20260924/README.md).
- 계획 정정이며 OCI 도입 승인, D21 판정 완료, G4 통과를 뜻하지 않는다. 발행 정본 편입은 별도이며 상태·AC·담당·기존 선행조건은 유지한다.
- 동기화 잔여: #36의 별도 Target date는 10-09→10-08, GitHub Milestone #7 기한/현행 설명은 09-28→10-06, #8은 10-08→10-13 갱신이 필요하다. 현재 연결은 해당 필드 쓰기를 제공하지 않아 본문 갱신과 구분해 추적한다.
<!-- fds-oci-schedule:20260924:v1:end -->

---

<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P2-IAC-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P2-IAC-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 계획 단계. AWS 10.20.0.0/16 유지. State/권한/버전·승인 Plan·비용/복구 기록은 Apply 전에 확정.

**인계·관련 티켓:** [#34](https://github.com/321Team/fds-project-baseline/issues/34) · [#36](https://github.com/321Team/fds-project-baseline/issues/36) · [#37](https://github.com/321Team/fds-project-baseline/issues/37).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P2-IAC-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P2-IAC-01 -->
# P2-IAC-01 — AWS / ROSA Terraform IaC

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-IAC-01 |
| Phase | Phase 2 |
| Category | Cloud / Terraform |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-10-08 |
| End | 2026-10-14 |
| Calendar Days | 7 |
| Working Days | 4 |
| Lead | 이하영 |
| Support | 이권욱 |
| Exit Criteria | AWS VPC 10.20.0.0/16, ROSA 선행 인프라와 IAM/OIDC 최소권한의 Terraform fmt/validate/plan/apply, State·Secret 통제 및 G4 Evidence 확보 |
| Related Decision IDs | D10; D21; D25 |
| Related Risk IDs | RISK-10; RISK-11; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #35 snapshot 2026-09-10T02:09:47Z; 일정: docs-v3.1.20 WBS + 2026-09-22 재계획 + 2026-09-24 일정 정합화; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 10-08 Stage-A 목표는 #36 D21 결정 → #34 최종 Freeze 이후에만 유효하다. Transport Adapter·Subnet/AZ·Route·backend/state 계약 및 reviewed plan/evidence를 고정한 뒤 #37(10-12)이 소비한다. 10-14 Full completion/G4 목표 유지. 당일 작업창 부족 또는 선행 HOLD 시 handoff를 완료로 기록하지 않고 후속 일정 재평가; Stage-A는 전체 AC PASS가 아니다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T02:09:47Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #35](https://github.com/321Team/fds-project-baseline/issues/35), Issue 갱신 시각 `2026-09-10T02:09:47Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Cloud IaC 담당자로서 AWS/ROSA 선행 인프라를 Terraform으로 재현 가능하게 구축한다. 이를 통해 수동 Drift를 줄이고 Plan과 실제 리소스의 추적성을 확보한다.

---

# Scope

## In Scope

- AWS VPC/Subnet/Route/Security
- ROSA Prerequisite
- IAM/OIDC 및 최소권한 Role
- Terraform State
- Variables/Outputs
- Plan/Apply Evidence

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] AWS VPC는 `10.20.0.0/16`을 사용한다.
- [ ] Secret을 tfvars/Source/Output에 평문 노출하지 않는다.
- [ ] IAM/OIDC Trust와 최소권한 Policy를 Source로 관리한다.
- [ ] Remote State 또는 승인된 State 통제를 적용한다.
- [ ] Plan을 검토 후 Apply한다.
- [ ] Destroy/Recovery 전제와 비용 리소스를 기록한다.

---

# Acceptance Criteria

- [ ] fmt/validate가 통과한다.
- [ ] 승인 Plan과 Apply 결과가 일치한다.
- [ ] 필수 Route/Security/Output과 IAM/OIDC가 생성된다.
- [ ] State와 Secret 접근이 통제된다.
- [ ] 재실행 시 비의도 변경이 없다.

---

# 검증 및 증적

- Terraform Source/Version
- fmt/validate/plan
- Apply/Output
- AWS Resource Inventory
- State/Secret Control
- Evidence Path: `321Team/fds-project-evidence:evidence/P2-IAC-01/`

---

# Dependency

- **Blocked By:** MS-P1-CLOSE-01; P2-ARC-01
- **Blocks / Next:** P2-VPN-01, P2-ROSA-01
- **Related Ticket:** P2-OCI-01
- **Milestone:** G4 Cloud / VPN Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D10; D21
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-10; RISK-11; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** AWS VPC 10.20.0.0/16 및 ROSA 선행 인프라의 Terraform fmt/validate/plan/apply, State·Secret 통제와 G4 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `9cc1eb76ce9e15ce96e292c37d853167be22bd33d828294111030d372638aa17`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P2-IAC-01 -->
# P2-IAC-01 — AWS / ROSA Terraform IaC

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P2-IAC-01 |
| Phase | Phase 2 |
| Category | Cloud / Terraform |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-28 |
| End | 2026-10-08 |
| Calendar Days | 11 |
| Working Days | 8 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | AWS VPC 10.20.0.0/16, ROSA 선행 인프라와 IAM/OIDC 최소권한의 Terraform fmt/validate/plan/apply, State·Secret 통제 및 G4 Evidence 확보 |
| Related Decision IDs | D10; D21; D25 |
| Related Risk IDs | RISK-10; RISK-11; RISK-12 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Phase1_Logical_Architecture_v3.1.2; Phase 2 OCI/AWS/ROSA Design; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 10-05는 비근무일이다. OCI Go/No-Go 결과에 따라 VPN 입력과 경로를 갱신한다. |

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

Cloud IaC 담당자로서 AWS/ROSA 선행 인프라를 Terraform으로 재현 가능하게 구축한다. 이를 통해 수동 Drift를 줄이고 Plan과 실제 리소스의 추적성을 확보한다.

---

# 📌 Scope

## In Scope

- AWS VPC/Subnet/Route/Security
- ROSA Prerequisite
- IAM/OIDC 및 최소권한 Role
- Terraform State
- Variables/Outputs
- Plan/Apply Evidence

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 📋 핵심 요구사항

- [ ] AWS VPC는 `10.20.0.0/16`을 사용한다.
- [ ] Secret을 tfvars/Source/Output에 평문 노출하지 않는다.
- [ ] IAM/OIDC Trust와 최소권한 Policy를 Source로 관리한다.
- [ ] Remote State 또는 승인된 State 통제를 적용한다.
- [ ] Plan을 검토 후 Apply한다.
- [ ] Destroy/Recovery 전제와 비용 리소스를 기록한다.

---

# ✅ Acceptance Criteria

- [ ] fmt/validate가 통과한다.
- [ ] 승인 Plan과 Apply 결과가 일치한다.
- [ ] 필수 Route/Security/Output과 IAM/OIDC가 생성된다.
- [ ] State와 Secret 접근이 통제된다.
- [ ] 재실행 시 비의도 변경이 없다.

---

# 🧪 검증 및 증적

- Terraform Source/Version
- fmt/validate/plan
- Apply/Output
- AWS Resource Inventory
- State/Secret Control
- Evidence Path: `docs/evidence/P2-IAC-01/`

---

# 🔗 Dependency

- **Blocked By:** MS-P1-CLOSE-01
- **Blocks / Next:** P2-VPN-01, P2-ROSA-01
- **Related Ticket:** P2-OCI-01
- **Milestone:** G4 Cloud / VPN Ready

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D10; D21
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-10; RISK-11; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** AWS VPC 10.20.0.0/16 및 ROSA 선행 인프라의 Terraform fmt/validate/plan/apply, State·Secret 통제와 G4 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>


---
_Generated by [Claude Code](https://claude.ai/code)_