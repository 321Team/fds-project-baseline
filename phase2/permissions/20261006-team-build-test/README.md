# Phase 2 팀원별 구축·시험·정리 권한 설계 v1.0

기준: 2026-10-06 KST 사용자 지시, 발행 정본 docs-v3.1.21 및 아래 재조회한 원본. CODEX_ASSISTED.
상태: 설계 후보 / AWS 권한 부여·ELB 생성 NOT_RUN / 독립 코드 리뷰 NOT_RUN.
이 문서는 기존 담당·AC·일정·Freeze 판정을 변경하지 않는다.

## 1. 이번 지시와 권장안

- 비용 설정 권한은 보류한다. Budgets/비용 경보/결제 설정/자동 Budget Action 권한을 이번 묶음에 넣지 않는다. 교육장 일일 비용 정보 + 자원 inventory/예상 가동시간/삭제 후 잔여로 통제한다.
- 현재3인 기본 IAM 계정의 공통 ReadOnlyAccess와 기존 자기관리/Audit 설정을 유지한다.
- 담당 구축 권한을 먼저 준비하고, 테스트 대상이 확정되면 같은 배정표의 시험 프로필을 활성화한다. 모든 모듈의 완료를 기다려 IAM 준비를 시작하는 구조로 만들지 않는다.
- 권욱은 CI/CD·QA 실행자이자 모듈 검증·지원 실행자로 배정한다. 하영/재환에게도 담당 모듈의 정상·실패·복구·정리 권한을 제공한다.
- AWS IAM, OpenShift RBAC, Red Hat OCM, Registry Robot, 온프레미스 OS/DB 권한을 따로 구현한다. IAM 역할 하나로 모든 층의 접근이 생기지 않는다.
- 기본 계정에 쓰기를 누적하지 않고 필요한 역할로 전환한다. 새 역할 이름은 아래 후보이며 실제 생성 완료가 아니다. 권한을 공유해도 업무 Lead/인수 책임은 바뀌지 않는다.

## 2. 확인된 기준과 현황

| 원본 | 재확인 결과 | 이번 판단 |
|---|---|---|
| [CURRENT](https://github.com/321Team/fds-project-baseline/blob/main/CURRENT.md) | 발행 v3.1.21; 정본 commit 979facb98de8ca1f1e2ce22f38b27ac3366f3fc3 | 정본 담당·시험 요구 유지 |
| [#35](https://github.com/321Team/fds-project-baseline/issues/35), [#37](https://github.com/321Team/fds-project-baseline/issues/37) | D21=aws_ec2_eip_relay; AWS route authority=Terraform | CGW/VGW/TGW/managed VPN 쓰기 기본 제외 |
| [infra-terraform PR3](https://github.com/321Team/infra-terraform/pull/3) | ebfc56e25125784187e36a0c1dd2ca0463e82acd; providers/variables/outputs/versions/backend example 재조회 | resource block 없음; 실제 API 의존성을 모두 추출했다고 주장할 수 없음 |
| 동일 source | Project=fds-hybrid, ManagedBy=terraform, Phase=phase2; S3 native use_lockfile=true; bucket/component key placeholder | 태그 대소문자 유지; exact backend는 추가 입력 필요 |
| [#38](https://github.com/321Team/fds-project-baseline/issues/38) | topology/version/pool/cluster/namespace 미확정; #35 provisioning, #38 내부 플랫폼 담당 | HCP/Classic system-role 세트와 실제 RBAC binding 미확정 |
| [#43](https://github.com/321Team/fds-project-baseline/issues/43), [#46](https://github.com/321Team/fds-project-baseline/issues/46) | portable base/digest/namespace/registry/credential reference 미확정 | 배포 프로필 설계 가능; actual binding은 대상 확정 후 |
| [#47](https://github.com/321Team/fds-project-baseline/issues/47), [#50](https://github.com/321Team/fds-project-baseline/issues/50) | transaction-api→DB 허용, engine→DB 거부; 실제 DB source 미확정 | engine에 DB credential/5432 egress 부여 금지 |
| [공통 RO 연결](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6008668288), [권욱 대표 조회](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6008686445) | 사용자 실행 PASS; 타2인 실제 세션은 미확인 | 기존 공통 연결 반복 불필요; 새 쓰기 role 실측은 별도 |
| 10/5 permission-readiness 및 10/6 사용자 출력 | IaC/Network 역할은 10/5 NoSuchEntity; ELB SLR은 10/6 GetRole NoSuchEntity | 현재 AWS 직접 재조회 아님; 생성 전 존재·정책 drift 확인 |

계정은 774055931866, 인간 principal은 user/321team-gwonuk, user/321team-hayeoung, user/321team-jaehwan이다. 기존 default VPC vpc-09c8159d7a476bc5c 조회 성공은 프로젝트 10.20.0.0/16 VPC 생성 증거가 아니다.

## 3. 사용자별 배정안

표의 배정은 이번 요청을 구체화한 제안이다. '사용 가능'은 설정 완료 상태가 아니다.

| 프로필 / 구현 층 | 권욱 | 하영 | 재환 | 대상 |
|---|---|---|---|---|
| 공통 ReadOnly / 기본 IAM | 유지 | 유지 | 유지 | 기존3인과 MFA/서울 제한 유지 |
| ELB account bootstrap | 초기 설정 실행·검증 | IaC 선행 지원·검증 | 조회 | 기존 교육장 root의 1회 exact-role 생성 권장. 사람의 상시 IAM 쓰기 추가 불필요 |
| FDS-IaC-Operator / AWS | 지원·모듈 검증·검토된 plan 실행·정리 | 주 구축·복구·정리 | 조회 | 프로젝트 Terraform resource/state 경계. 일반 사용자/IAM 권한 관리 제외 |
| FDS-Network-Operator / AWS+Relay OS | VPN 검증·지원·복구 | 조회 및 IaC handoff | 주 Relay 구성·검증·복구 | exact Relay/SSM document, 자체 세션; AWS route 수동 변경 제외 |
| ROSA platform / OCM+OpenShift | 플랫폼 모듈 검증 | 주 플랫폼 구성 | 앱 namespace 구성 소비·시험 | namespace-local 우선; 필요 cluster-scope 작업은 별도 시험 프로필 |
| CI/CD deploy / OpenShift+Registry | 주 파이프라인·배포·롤백 | 플랫폼 지원·모듈 시험 | 앱 구현·배포·모듈 시험 | 전용 인간 그룹과 Runner SA/Robot을 분리 |
| QA module-test / OpenShift+API+DB | 공통 QA·회귀 | 플랫폼/보안/복구 시험 | App/Hybrid/E2E 시험 | 팀 전용 시험 namespace/fixture; namespace 밖 쓰기·실제업무 데이터 변경 제외 |
| Recovery test / AWS+OCM+OpenShift+OS | 지정 시험 실행 | 플랫폼 replacement/복구 | Relay/App/Hybrid 복구 | 역할별 허용 대상 분리, 한 회차 한 장애주입 실행자 |
| Teardown / Terraform+OCM | 비용 통제에 따른 정리·확인 | 인프라/클러스터 정리 | 담당 임시 workload/fixture/OS 설정 정리 | Terraform/클러스터 정상 삭제 경로; 임의 worker 종료·state 삭제 제외 |
| DNS / 선택 후 해당 층 | 주 구현·시험 | IaC/platform 지원 | 연결성 시험 | D23 Go 및 exact zone/resolver만 |
| OADP/Operator / 조건부 | backup/restore 검증 | 주 설치·설정·시험 | app-consistency 검증 | #44/#51의 기존 Go/Capacity 조건 충족 후 |

권욱에게 타 담당자의 구축 역할을 제공하는 목적은 실제 모듈 검증/지원/정리다. 전체 관리자 역할 또는 임의 IAM 정책 변경 권한을 대신 제공하지 않는다. 검증에 쓰기가 필요하면 표의 역할로 직접 수행하고, 인수 책임과 독립 리뷰는 원래 업무 범위로 유지한다.

## 4. 프로필별 구체적 허용 범위와 주의점

### A. ELB 초기 설정 — 지금 독립적으로 준비 가능한 항목

- 정확한 대상: arn:aws:iam::774055931866:role/aws-service-role/elasticloadbalancing.amazonaws.com/AWSServiceRoleForElasticLoadBalancing.
- CreateServiceLinkedRole은 iam:AWSServiceName=elasticloadbalancing.amazonaws.com으로 제한한다. 검증은 GetRole의 account/ARN/path/service trust로 한다.
- [기존 ELB 정책 후보](https://github.com/321Team/fds-project-baseline/blob/72d798d5c784bf2270566b60374d1632d3152981/phase2/inputs/elb-service-linked-role-bootstrap.candidate.json)는 CreateServiceLinkedRole/GetRole만 있다. 이 문서에서 변경하지 않았다.
- 권장 구현은 교육장 root의 승인된 1회 초기 설정이다. 기존 관리자 권한이 있으므로 일반 사용자에게 새 grant를 남길 필요가 없다. 권욱은 범위와 결과를 확인한다.
- 개인 역할 위임이 필요해지면 위 exact Allow만 전용 Bootstrap role에 넣고 권욱/하영 exact principal+MFA trust와 identity-side AssumeRole을 구성한다. 이번 문서는 그 role을 생성하지 않는다.
- ELB SLR은 ELB 서비스가 사용하는 역할이며 사람이 AssumeRole할 업무 역할이 아니다. ELB role 한 개 생성은 LB/TG 또는 유료 클러스터 생성이 아니다.
- 부재 재확인은 NoSuchEntity만 인정한다. AccessDenied/timeout은 STOP. 이미 존재하면 검증 후 SKIP. 성공 후 자동 SLR 삭제 rollback을 하지 않는다.

### B. IaC — 하영 주 구축, 권욱 지원·시험·정리

- network/vpn component: 프로젝트 VPC, 4 subnet, route table/association/route, 필요한 인터넷/egress 경로, SG/rule, Relay EC2/ENI/EIP/EBS/instance profile 생성·수정·삭제.
- 필요한 EC2 API 후보는 CreateVpc/CreateSubnet/CreateRouteTable/CreateRoute/AssociateRouteTable/CreateSecurityGroup/AuthorizeSecurityGroupIngress/RunInstances/AllocateAddress/AssociateAddress/ModifyInstanceAttribute 및 해당 update/delete/revoke/release이다. 이것은 API 후보 분류이며 완결된 실행 정책이 아니다.
- NATGW/VPC endpoint/ROSA runtime 자원은 선택된 실제 topology·egress/source에 있는 경우만 포함한다. 현재 scaffold가 이 구현을 정의하지 않았으므로 가정으로 먼저 부여하지 않는다.
- RunInstances는 instance뿐 아니라 AMI/subnet/SG/ENI/volume 등 해당 API의 resource 종류와 dependent action을 대조한다. 생성 시 태그 조건과 후속 수정/삭제의 resource 조건을 구분한다.
- 정확한 state key GetObject/PutObject, lockfile key GetObject/PutObject/DeleteObject, 필요한 prefix ListBucket. 기본 state DeleteObject는 일반 apply에 필요하지 않다. KMS 사용 여부 확정 시 exact key 권한 추가. workspace 사용 여부도 별도 확인.
- ROSA account/operator/OIDC·Relay instance role의 IAM 생성은 인프라 쓰기보다 높은 위험이다. 지정 path/ARN·정책·trust·PassRole 대상만 허용한다. 인간 work role/공통 guard/Audit/자신의 boundary 수정은 제외한다.
- 일반 workload role에는 권한 상한 boundary 강제 및 그 boundary 수정/제거 거부를 검토한다. ROSA 서비스·operator role에 임의 boundary를 일괄 적용하지 않고 topology별 지원 정책과 공식 prerequisite를 대조한다.
- IAM 생성/정책편집을 구현하기 전에는 bootstrap 관리자에게 이 부분만 맡기고 Terraform IaC Operator에는 이미 승인된 exact 역할의 사용만 허용하는 대안을 쓴다. iam:* 또는 FDS-* 이름만으로 광역 쓰기 허용하지 않는다.

### C. Network/Relay — 재환 주 구성, 권욱 시험·지원

- exact Relay에 StartSession + 선택한 session document, 필요한 data channel, 본인 ResumeSession/TerminateSession 및 진단 읽기를 제공한다.
- Run Command가 필요하면 reviewed document/version + exact instance + parameter 범위로 제한한다. 범용 shell 문서와 자유 parameter는 사실상 host root 실행일 수 있다.
- SSM shell도 OS 관리자 권한을 가질 수 있으므로 단순 조회로 표시하지 않는다. OS 사용자/sudo, 세션 로그/암호화, port-forwarding 허용 여부를 함께 확정한다.
- IPsec/Libreswan·firewalld·systemd·승인 route/selector 설정·rekey/restart는 host 권한으로 구현한다. 온프레미스 vpn-gw01도 별도 OS 계정 권한을 사용한다.
- Relay reboot/start/stop은 복구 시험에 필요한 exact instance만. EC2 role 생성, instance profile 교체, 임의 user-data·태그 변경, EIP/route 재구성은 기본 Network 프로필 제외.
- AWS route/SG/EIP 구조 변경은 IaC profile의 검토된 Terraform 변경으로 수행한다. 재환에게 managed VPN/전체 EC2FullAccess를 주지 않는다.

### D. ROSA 플랫폼 — 하영 구축, 권욱 검증

- AWS 구축/STS-OIDC account role/서비스 operator role과 사람의 OCM/cluster RBAC를 분리한다. 시스템 operator role을 인간 trust에 추가하지 않는다.
- Namespace/Project 초기 구성, approved SA/RBAC, NetworkPolicy, quota/limit, Route/security handoff를 담당한다.
- cluster-scope RBAC/SCC/Operator/CRD/IdentityProvider 등의 실제 필요를 선정한 후 그 작업만 포함한다. PG03 문제를 broad SCC/privileged 우회로 해결하지 않는다.
- 실제 project ROSA의 worker replacement/drain/machinepool 시험은 지원되는 관리 경로와 승인 시험 범위로 제한한다. 임의 EC2 worker TerminateInstances를 사람 권한의 기본값으로 넣지 않는다.
- Shared OCP Lab에는 이번 AWS role이 cluster 권한을 만들지 않는다. 공용 cluster의 SCC/CRD/Node/Operator 및 장애·부하 시험 금지 경계를 유지한다.
- Terraform이 생성/관리하는 클러스터 설정을 OCM에서 병행 수정할 경우 drift를 만들 수 있으므로 실행 경로를 source-of-truth와 맞춘다.

### E. App/CI/CD/QA — namespace와 credential 분리

- App builder(재환): 팀 app namespace의 Deployment/Service/Route/ConfigMap, 승인 Secret reference와 필요한 초기 Secret 설정, probe/security config, 배포·롤백·smoke.
- CI/CD operator(권욱): Runner direct deploy, 승인 image digest 업데이트, rollout/status/rollback, Test/Scan 실패 시 deploy 차단. Registry 결정 전 ECR 권한은 자동 추가하지 않는다.
- Runner deploy identity: namespace-local SA/RBAC, 짧은 수명 token/reference, pipeline OIDC 사용 시 exact repo/environment/audience trust. 인간 MFA 조건을 workload identity에 그대로 붙이지 않는다.
- Helm 사용은 아직 실제 manifest/설치 방식에 따라 달라진다. Helm release Secret 저장 방식은 QA의 'Secret 읽기 없음'과 충돌할 수 있으므로 무조건 Helm+no-Secret 정책으로 충분하다고 하지 않는다.
- QA3인: 전용 test fixture/API 쓰기, 필요한 test Job/Pod 생성·로그·정리, 승인 app Deployment patch/scale/rollback; DB fixture 계정은 필요한 schema/table INSERT/SELECT/UPDATE/DELETE만. migration/DDL/admin은 앱/DB 담당의 별도 작업.
- 단순 get/patch만으로 보안을 과장하지 않는다. workload 생성/변경은 같은 namespace Secret을 mount하거나 다른 SA로 실행하는 우회가 가능하다. 시험 namespace에는 민감 Secret/고권한 SA를 함께 두지 않고 restricted-v2와 필요한 admission 제약으로 보호한다.
- pods/exec는 컨테이너 Secret 접근·변경 경로가 되므로 기본 QA에서 제외하고 필요 시 target/scope를 별도 시험 프로필로 구현한다. RBAC의 resourceNames/label만으로 모든 create/exec를 완전히 제한한다고 주장하지 않는다.
- 부하/장애 시험은 실행 창·수량 제한·단일 실행자로 통제한다. RBAC만으로 '업무시간에만' 또는 'scale<=N'을 자동 보장하지 않는다.

### F. Recovery/Teardown — 시험과 원복 권한을 함께 제공

- Relay 서비스 stop/start/rekey/reboot, engine test scale 0/restore, fixture DB failure/recovery, cold-pull/rollout regression 등 원본 TS06/08/10/12/15에 필요한 작업을 선택한다.
- DB 장애와 engine 장애는 기대값이 다르다. DB /readyz503·Endpoint 제외, engine 장애는 API Ready·201·skipped=true·DB 저장을 구분한다.
- 하영 platform replacement, 재환 Relay/App/DB 복구, 권욱 QA/CI rollback과 전체 원복 확인에 각각 해당 실제 쓰기를 제공한다.
- 삭제 권한은 생성 권한과 함께 검토하되 teardown profile의 대상 inventory/state component를 고정한다. 동일 정책의 모든 delete를 전 계정 Resource=*로 허용하지 않는다.
- ROSA 정상 삭제→프로젝트 Terraform component 정리→NAT/EIP/ENI/LB/endpoint/EBS 등 잔여 확인. state·원본 증적·공유 자원·서비스 연결 역할은 무조건 삭제 대상으로 넣지 않는다.
- EBS/PVC/백업 데이터 파괴 시험은 별도 케이스와 복구 전제가 있는 경우에만. 일반 QA나 비용 통제라는 이유로 모든 데이터 삭제를 허용하지 않는다.
- 공통 RO가 미래 state/데이터 읽기에 미칠 영향도 검토한다. backend/secret/backup 저장소는 업무상 민감 범위이며 '조회 공통'만으로 모든 원문 읽기를 의도한 것으로 간주하지 않는다.

## 5. 공통 IAM 통제 — 새 role에 직접 구현

1. exact 사용자 ARN allowlist + MFA true를 trust와 사용자 identity-side AssumeRole에 구현한다. 신규 role마다 권한 범위가 다르므로 현재 그룹 전체에 모든 role AssumeRole을 한 번에 허용하지 않는다.
2. role-session 권한은 기본 사용자 권한을 합산하지 않는다. 해당 role에 작업에 필요한 read 권한도 포함한다.
3. 현재 사용자 그룹 guard는 role session으로 자동 이전되지 않는다. 각 role의 서울 endpoint 제한/global API 예외·허용 자원·IAM 상한을 따로 구현한다.
4. MFA는 AssumeRole 시 검증하는 trust 조건이다. MFA-authenticated AssumeRole session의 후속 API마다 aws:MultiFactorAuthPresent=true가 제공된다고 가정하여 Allow를 작성하지 않는다.
5. role session naming/CloudTrail actor 추적, session duration 상한, session-tag 사용 시 위조 방지 trust 조건을 검토한다. SourceIdentity는 지원 경로 확인 후 적용하며 기존 Switch Role을 가정으로 깨뜨리지 않는다.
6. 요청 태그와 resource tag의 action별 지원을 확인한다. protected Project/ManagedBy/Phase 변경으로 범위를 벗어나거나 타 자원에 Project 태그를 붙여 권한을 얻는 경로를 막는다.
7. PassRole은 exact 역할 ARN + PassedToService. 자체 권한/trust/boundary/공통 guard 수정·다른 인간 credential 생성은 부여하지 않는다.
8. SCP/boundary/resource policy/session policy의 Deny를 광역 Allow로 해결하지 않는다. 유료 ROSA 생성 권한이 생겨도 비용·Freeze·source/plan 선행조건이 충족된 것은 아니다.
9. 3인 MFA device=1씩 확인된 10/5 기록은 유지한다. 과거 commonRO 일괄 적용 예외는 새 쓰기 role 실제 사용 성공을 증명하지 않는다. 각 배정 user-role의 본인 AssumeRole 및 대표 API를 실제 확인한다.

## 6. 역할·모듈별 시험 매트릭스

[발행 시험 전략 TS01–16](https://github.com/321Team/fds-project-baseline/blob/docs-v3.1.21/tests/FDS_Test_Strategy_v3.1.21.md)을 추적한다. 아래는 시험 계획이며 아직 simulator/실측 PASS가 아니다.

| 층/모듈 | 정상 허용 | 거부/실패 경로 | 복구·회귀 |
|---|---|---|---|
| Trust/MFA | 배정 본인 MFA AssumeRole | 미배정 사용자·noMFA·타 계정·비허용 role | 기본 RO/Audit/self-service 유지 |
| ELB bootstrap | exact ELB SLR 한 개 생성, 기존 존재 SKIP | 타 서비스/일반 role 생성 없음, AccessDenied를 부재로 해석 금지 | timeout/응답 유실 후 조회로 확인, 자동 삭제 없음 |
| IaC/backend TS01 | 검토된 project plan/apply, state/lock 접근 | 다른 Region·타 Project·다른 state key·protected tag 변경·권한 상승 | lock 경쟁/실패 후 해제, 같은 source 무의도 drift 없음 |
| Relay TS04/06 | 승인 SSM/UDP500·4500/selector/path | 타 instance/document/미허용 source-port·plaintext 우회 | rekey/restart/reboot/rebuild 원복, DB 연결 회귀 |
| Platform TS02/03/07/14 | restricted-v2 arbitrary UID, namespace handoff | broad SCC/SA/RBAC 우회·engine DB 접근 | 승인 replacement/capacity/Cold pull 복구 |
| CI TS08/09/10 | 승인 digest Test→Build→Scan→Push→Deploy→Health | anonymous/pull-only push·잘못된 audience·scan 실패 deploy | 이전 승인 digest rollback/health |
| App/E2E TS11/12 | Normal+4 Rule+DB row 추적 | engine→DB·미승인 client·다른 namespace 쓰기 | DB/engine 장애 기대값 각각 확인, fixture 정리 |
| 복합 TS15 | 지정 단일 회차 역할별 장애 실행 | scope 밖 Node/DB·동시 장애주입·예외 보안 우회 | VPN+worker/registry/DNS+업무 전체 회귀 |
| Teardown TS16 | 프로젝트 component 정상 정리 | 타 자원/state/공유 데이터/SLR 삭제 | 잔여 inventory+교육장 비용 자료 비교 |

IAM simulator는 candidate 조합과 resource/context 조건을 검증한다. RBAC can-i는 API authorization만 확인하며 실제 Admission/OS/네트워크/DB 동작을 증명하지 않는다. 실제 거부 시험은 비파괴 방법으로 수행하고 허용되지 않아야 하는 유료 생성 API를 무작정 호출하지 않는다.

## 7. 단계별 실행 가능 범위와 미확정 입력

| 묶음 | 지금 준비할 작업 | 정책 적용에 필요한 입력 |
|---|---|---|
| ELB 초기 설정 | exact role 생성·존재/identity/readback 확인 도구 | 적용 파일 SHA 독립 코드 리뷰, 교육장 root 실제 CloudShell 실행 |
| Network/IaC Stage-A | action/resource별 정책 초안, 생성·복구·정리 경계 | 실제 resource blocks, backend bucket/component keys, approved Relay instance role/PassRole, AMI/root encryption 경로 |
| Relay 운영/시험 | SSM/OS/session/document 프로필 | Stage-A actual instance/ENI/EIP/SG, agent/management path, document/version/OS account |
| ROSA | HCP/Classic별 비교 및 OCM/RBAC 설계 | topology/version/pool, approved account/operator/OIDC roles, actual cluster/identity/group/namespace |
| App/CI/QA | SA/Role/RoleBinding·API/DB 시험 프로필 | reviewed portable source, exact namespaces/SA/registry/digests/token ref/DB fixture role |
| DNS/OADP/Operator | 선택 시 최소 권한 분류 | 기존 조건부 Go + exact target/resource + capacity |
| Recovery/Teardown | 케이스별 변경·원복·삭제 목록 | actual inventory/state ownership, 원복 source/data, 실행 창 |

이 목록은 사용자에게 이미 제공된 정보를 다시 묻는 목록이 아니다. 구축 source와 handoff에서 생산해야 하는 기술 입력이다. 한 입력이 미확정이어도 다른 묶음의 설계·정적 검증·리뷰를 계속한다. 광역 정책을 먼저 붙인 후 사후 축소하는 방식을 기본안으로 사용하지 않는다.

## 8. ELB 도구 사용·중단·복구

동봉 bootstrap-elb.py는 기본 읽기 전용이며 --apply에서만 exact ELB 역할 생성 한 번을 호출한다. 실행 위치는 교육장 AWS CloudShell, Python3/AWS CLI, 승인된 관리자 세션이다. Apply mode는 기존 교육장 root의 정확한 ARN과 account만 허용한다. credential/OTP를 출력하지 않는다.

1. 독립 코드 리뷰 대상은 bootstrap-elb.py와 tests/test_bootstrap_elb.py의 exact commit이다. 기존 ReadOnly/guard 승인으로 새 코드를 승인했다고 표시하지 않는다.
2. 실행자는 리뷰 완료 SHA의 파일을 사용한다. 기본 확인: python3 bootstrap-elb.py. 읽기 권한 부족/다른 계정/예상 밖 기존 ARN/path/trust는 STOP.
3. 적용: python3 bootstrap-elb.py --apply. root identity 확인→GetRole→NoSuchEntity일 때만 CreateServiceLinkedRole→GetRole 재조회. 존재하면 생성 SKIP.
4. 정상: ELB_ROLE_CHECK=PASS 및 ELB_CREATE=CREATED 또는 SKIP_EXISTING. default mode에서 부재는 ELB_ROLE_CHECK=ABSENT/AWS_MUTATION=NOT_RUN으로 반환한다.
5. 생성 결과 불명/timeout/readback 실패는 STOP, 자동 재시도/삭제 없음. IAM eventual consistency 또는 응답 유실이면 기본 조회 mode로 실제 상태를 먼저 확인한다.
6. 원상복구가 필요해도 서비스 연결 역할은 자동 삭제하지 않는다. 정책 grant를 사용한 경우 해당 temporary grant만 회수한다. 이 root 경로는 인간 grant를 생성하지 않는다.
7. 이후 권욱 기본 RO 세션에서 GetRole 확인과 ROSA start 화면 재확인. 이 성공은 Marketplace/STS-OIDC/ROSA cluster 구축 완료가 아니다.

별도의 승인 문서나 단계별 새 PR을 반복 생성할 필요는 없다. 현재 패킷에서 코드 리뷰와 범위별 실행 결과를 연결한다. AWS 연결은 이 세션에 제공되지 않았으며 Assistant의 실제 AWS 실행은 없다.

## 9. 출처·검증·잔여

- 원본 GitHub 재조회: CURRENT/AGENTS/REVIEW_AUTHORITY_POLICY, #35/#37/#38/#43/#44/#46/#47/#48/#50/#51, #35 운영 댓글, PR137 HEAD72d798d5, infra-terraform PR3 HEADebfc56e2의 실제 .tf4개/backend example/README.
- 공식 문서: [ELB SLR](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/elb-service-linked-roles.html), [IAM MFA API](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html), [IAM boundaries](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_boundaries.html), [SSM Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-restrict-access-quickstart.html), [Terraform S3 backend](https://developer.hashicorp.com/terraform/language/backend/s3), [Kubernetes RBAC escalation](https://kubernetes.io/docs/concepts/security/rbac-good-practices/), [ROSA responsibilities](https://docs.aws.amazon.com/rosa/latest/userguide/rosa-responsibilities.html).
- STATIC=원본/담당/시험/권한 경계 대조; MOCK=동봉 ELB 단위시험 실제 결과를 PR에 기록; IAM_SIMULATOR=NOT_RUN; AWS_RUNTIME=NOT_RUN; ROLE_GRANT=NOT_RUN; ELB_CREATE=NOT_RUN; REVIEW/MERGE=NOT_RUN.
- 새 권한 부여·유료 생성·IAM/Role/Pipeline/RBAC 변경은 문서 작성만으로 실행되지 않는다. 원본 Lead/AC/기한을 유지한다.

