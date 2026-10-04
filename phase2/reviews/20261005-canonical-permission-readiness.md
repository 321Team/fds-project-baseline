# Phase 2 담당별 권한 준비 — 정본 대조 및 ELB 후속

2026-10-05 KST · CODEX_ASSISTED · 준비 후보 / AWS 변경 미실행

## 권위와 적용 범위

기준은 [CURRENT.md](https://github.com/321Team/fds-project-baseline/blob/main/CURRENT.md)의 발행 v3.1.21 및 [P2-IAC-01](https://github.com/321Team/fds-project-baseline/blob/docs-v3.1.21/tickets/v3.1.21/descriptions/P2-IAC-01.md), [P2-ROSA-01](https://github.com/321Team/fds-project-baseline/blob/docs-v3.1.21/tickets/v3.1.21/descriptions/P2-ROSA-01.md)이다. 정본 스냅샷 이후 실행 사실은 #35의 개별 결과로 보완하며, 이 준비 문서는 정본·담당·AC·계획일을 변경하지 않는다.

Phase 1은 진행 중이다. 문서 발행, 조회 성공, IAM 사전 설정을 P1 인수 또는 P2 구축 허가로 해석하지 않는다. CloudShell은 실행 도구이고 그 안의 AWS 작업 권한은 실제 세션 principal의 권한으로 따로 판정한다.

## 정본 담당과 AWS principal 구분

| 업무 | 정본 책임 | 연결할 권한 / 현재 판정 |
|---|---|---|
| AWS/IaC 실행 및 Runtime AC 인수 (#35) | Lead 이하영; Support 이권욱 | FDS-IaC-Operator는 정본 후보. 실제 policy/trust/AssumeRole 완료 증거 없음 |
| ROSA platform/security (#38) | Lead 이하영; PMO/QA Review Owner 이권욱 | AWS 구축 권한과 ROSA namespace/RBAC를 별도 설계. PMO/QA 역할 자체는 AWS 쓰기 권한 아님 |
| 준비용 조회 | 승인된 3인 각 본인 | FDS-ReadOnly-Audit 설정 readback 성공; 본인 세션 검증은 권욱만 확인 |
| 자기 MFA·로그인·역할 전환 | 각 본인 | 하영·재환의 추가 성공 증적 필요. 다른 사람 세션으로 대체 불가 |
| ELB 계정 초기 설정 | #35 Lead가 범위·실행 주체 연결 | 기존 승인 IAM 관리자 또는 별도 최소권한 bootstrap principal 필요; exact ARN 미확정 |
| 코드·IAM 정책 독립 리뷰 | 작성/실행에 참여하지 않은 reviewer | 권욱 작성 후보는 권욱의 자기 승인 불가. 재환 등 독립 담당 연결; 재환을 AWS operator로 자동 배정하지 않음 |

[REVIEW_AUTHORITY_POLICY](https://github.com/321Team/fds-project-baseline/blob/main/governance/REVIEW_AUTHORITY_POLICY.md)에 따라 코드 병합·증적 PR의 독립 리뷰와 Lead의 실행/인수 판단을 구분한다. 일반 준비 문서에 상시 이중 승인을 추가하지 않는다. 실행용 IAM JSON은 보안 제어 코드이므로 순수 수집기 예외로 취급하지 않는다.

## 이미 확인된 것과 남은 것

| 항목 | 마지막 확인 근거 | 현재 기록상 상태 |
|---|---|---|
| 3인 조회 역할 연결 | #35 [5967153865](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5967153865) | v2 configuration readback PASS; bootstrap 재실행 불필요 |
| 권욱 CloudShell / STS / VPC / quota 조회 | [5967218680](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5967218680) | 10/3 본인 assumed-role 성공; 반복 수집 불필요 |
| 하영·재환 MFA 로그인 / 역할 / CloudShell | 성공 기록 미확인 | PENDING; 10/3 MFA count=0을 현재 상태로 단정하지 않음 |
| ROSA 선행 조회 추가 정책 | [5967317832](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5967317832) | 정책 readback 성공. exact ELB GetRole 거부 원인 미해소 |
| ELB 서비스 연결 역할 | [5967330388](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5967330388), [5967360872](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5967360872) | 10/3 ListRoles 성공 결과에서 미관측, CreateServiceLinkedRole 거부. 생성 완료 아님 |
| Marketplace / AWS–Red Hat 연계 | [5967360872](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5967360872) | 조회 오류 해소와 subscription/activation 완료는 별개; 완료 증거 없음 |
| 구축용 역할 / backend / plan | 정본 #35 계약 | 미완료; 조회 역할 성공으로 대체 불가 |
| pre-change 백업 외부 보관 | 기존 IAM runbook 후속 | 파일 생성과 별도 보관/hash 대조는 별개; 후자 PENDING |

실제 AWS 상태를 이번 작업에서 새로 조회하지 않았다. 위 결과는 10/3 사용자 실행 기록이며 현재 상태를 보증하지 않는다. 정적 검토 의견은 독립 APPROVED 또는 실행 성공으로 올리지 않는다.

## 권장 실행 순서와 이번 착수 결과

1. **담당·상태 대조 완료:** 이 표와 IAM runbook 머리말을 정리했다. 기존 성공 bootstrap·권욱 inventory를 반복하지 않는다.
2. **각 본인 조회 readiness:** 하영·재환은 다음 본인 세션에서 MFA 로그인→FDS-ReadOnly-Audit 전환→서울 CloudShell→STS/VPC 확인. 기존 [IAM runbook](../runbooks/20261003-team-iam-readonly-bootstrap.md)의 조회 명령을 사용한다. 세션 ARN·KST·명령 RC만 기록하고 credential/OTP는 남기지 않는다.
3. **ELB bootstrap 준비:** 전용 후보 JSON을 작성했다. 아래 사전 확인 후 #35 Lead가 exact 실행 principal·작업창을 연결한다. 계정 초기 설정은 IAM 변경이므로 이 문서 작성만으로 실행하지 않는다.
4. **구축용 권한 설계:** 정본의 FDS-IaC-Operator / FDS-Network-Operator 후보를 기준으로 실제 source/resource inventory에서 API를 추출한다. IaC와 network가 같은 자원을 중복 관리하지 않도록 Terraform route authority를 유지한다. exact backend bucket/key/lockfile, SSM instance role/PassRole 대상, STS/OIDC trust, topology/version/machinepool 입력 확정 후 policy를 고정한다. 현재 임의 wildcard operator 정책은 만들지 않는다.
5. **실제 구축:** #34 Freeze, #35 MFA/work-role/backend/source/검토된 plan/비용·정리 조건을 충족한 뒤 Lead 실행 판단. #38 Runtime은 G4 이후. 정본 최신 D21은 EC2/EIP relay이므로 과거 managed VPN quota를 해당 경로의 blocker로 되살리지 않는다.

Phase 1 공유 DNS/Runner/GW 변경은 위 IAM 준비와 분리한다. P1 진행 중에도 정적 설계와 본인 조회 검증은 가능하지만, P2 선행조건을 통과한 것으로 올리지 않는다.

## ELB 전용 후보의 범위와 검증

후보: [elb-service-linked-role-bootstrap.candidate.json](../inputs/elb-service-linked-role-bootstrap.candidate.json).
대상 계정의 정확한 ELB 서비스 연결 역할에 대한 생성 및 GetRole 조회만 포함한다. 조회 공용 역할에 붙이는 정책이 아니다. 관리자·운영자 역할 자체를 생성하거나 사람을 할당하는 코드도 아니다. SCP/boundary/session policy의 deny를 우회하지 않는다.

AWS [ELB 안내](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/elb-service-linked-roles.html)에서 서비스 이름과 역할 이름을, [IAM 안내](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html)에서 서비스 조건 및 ARN 제한 방식을 확인했다. 이 후보는 직접 CreateServiceLinkedRole API 경로만 대상으로 한다. IAM 일반 예시의 수동 AttachRolePolicy/PutRolePolicy는 포함하지 않았으며 콘솔 전체 workflow의 충분한 권한으로 주장하지 않는다.

실행 전 기존 승인 관리자 세션에서 아래 **조회만** 수행한다. 두 호출 각각 RC를 기록한다. 현재 본인 principal/account 확인 및 역할 존재 판정용이며, 성공 증적이 새로 생기면 기존 미관측 기록을 대체한다.

```bash
aws sts get-caller-identity --output json --no-cli-pager; printf 'IDENTITY_RC=%s\n' "$?"; aws iam get-role --role-name AWSServiceRoleForElasticLoadBalancing --query 'Role.{Arn:Arn,Path:Path,Trust:AssumeRolePolicyDocument}' --output json --no-cli-pager; printf 'ELB_ROLE_READ_RC=%s\n' "$?"
```

- 존재하면 생성은 건너뛴다. 오류가 AccessDenied이면 존재/부재를 판단하지 않고 principal·정책·SCP/boundary/session을 진단한다. NoSuchEntity일 때만 부재로 분류한다.
- 신규 부재일 때 exact bootstrap principal, 정책 부여/제거 담당과 시점, 후보 exact SHA 독립 리뷰, Lead 실행 판단을 기록한다. 승인된 관리자에게 이미 필요한 권한이 있으면 별도 정책을 중복 부여하지 않는다.
- 적용 이후 생성 결과와 GetRole의 ARN/path/trust를 대조하고 temporary grant 사용 시 그 grant만 회수·확인한다. 생성된 서비스 연결 역할 삭제를 자동 rollback으로 실행하지 않는다.
- 이 후보에는 ELB/TG 생성·Marketplace Subscribe·PassRole·일반 CreateRole·정책 부착/삭제 권한이 없다. ELB 선행 설정이 성공해도 ROSA activation, STS/OIDC, 프로젝트 생성은 별도다.

이번 검증: JSON 구문·허용 Action·정확한 ARN·서비스 조건 정적 대조. AWS policy validator/simulator/API 실행 없음. 정책 부착·서비스 연결 역할 생성·유료 리소스 생성 없음. PR draft / 독립 리뷰 미완료 / 인수 변경 없음.
