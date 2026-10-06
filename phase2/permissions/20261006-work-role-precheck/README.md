# IaC·Network 역할 진입 후보와 중앙 Pre-check

기준: 2026-10-06 사용자 다음 절차 착수 지시, PR139 배정 설계, docs-v3.1.21. CODEX_ASSISTED.

ELB SLR 생성·권욱 일반 조회·ROSA 화면 확인은 [PR139 결과](https://github.com/321Team/fds-project-baseline/pull/139#issuecomment-6009344711)로 완료됐다. 비용 설정은 계속 제외한다. 이 묶음은 다음 IAM 입력 수집과 역할 진입 후보 시험이며 역할 생성·권한 연결·Terraform apply를 실행하지 않는다.

## 1. 이번 실제 후보 파일

| 역할 | 허용할 본인 | trust·identity 조건 |
|---|---|---|
| FDS-IaC-Operator | 321team-gwonuk, 321team-hayeoung | exact IAM ARN, MFA true, RoleSessionName=본인 IAM 사용자명 |
| FDS-Network-Operator | 321team-gwonuk, 321team-jaehwan | 동일 조건 |

`candidates/`에 trust2개와 본인별 identity-side AssumeRole3개 JSON을 제공한다. Action은 sts:AssumeRole만, identity Resource는 정확한 배정 role ARN만 있다. trust에는 인간2인만 있고 root/계정 전체/다른 role/service principal은 없다. identity JSON은 배정 사용자별 후보이며 공통 그룹에 일괄 연결하는 정책이 아니다. 기존 기본 ReadOnly/guard/self-service/Audit에 변경을 하지 않는다.

이번 후보는 MFA 기반 기본 IAM 로그인·CloudShell 및 콘솔 Switch Role을 대상으로 한다. 장기 Access Key를 발급하거나 role chaining 경로를 추가하지 않는다. 향후 생성 시 역할의 MaxSessionDuration 후보는3600초이며 이 값은 trust JSON의 조건으로 구현한 것이 아니다. 후속 role session API에 MFA=true가 항상 전달된다고 가정하지 않는다.

**업무 role의 EC2/S3/SSM 쓰기 permissions JSON은 아직 이 묶음에 없다.** 아래 실제 입력을 생산한 뒤 완결된 JSON·정상/음성/원복 시험으로 추가한다. trust만 연결한 빈 역할이나 role의 ReadOnlyAccess 연결을 '업무 쓰기 권한 부여 완료'로 표시하지 않는다.

## 2. 현재 source와 필요한 입력

infra-terraform [PR3](https://github.com/321Team/infra-terraform/pull/3)은 2026-10-06 13:30:18 KST 병합됐다. source HEAD ebfc56e25125784187e36a0c1dd2ca0463e82acd / merge1f166d5c27ff24316887ae8ee2f2211fbb9a1a7d. 실제8파일 diff는 resource block0, S3 bucket/component key placeholder, Terraform1.16.4/provider6.66.0 계약 scaffold다. 기존 same-HEAD 외부 승인과 병합은 scaffold 범위이며 plan/apply/runtime 승인으로 확대하지 않는다.

| 묶음 | 확정된 범위 | 기존 담당의 후속 입력 |
|---|---|---|
| IaC 구축·복구·정리 | 서울, Project=fds-hybrid/ManagedBy=terraform/Phase=phase2, D21 EC2+EIP Relay | #35 하영: 실제 resource implementation SHA/API·dependent resource, backend bucket + network/vpn/rosa-prereq/rosa-runtime 각각의 key, KMS 선택·exact ARN, Relay instance role/PassRole |
| Network Relay 운영·시험 | 재환 주 구성, 권욱 지원; AWS route authority=Terraform | #37 실제 Relay instance/ENI/SG/EIP와 SSM document/version·management/OS 경로. Terraform rebuild는 하영/권욱, 재환 구성 재적용·검증 |
| ROSA/App/CI/QA | PR139의 층별 배정 유지 | #38 topology/cluster/OCM/RBAC, #43/#46/#47 namespace/SA/registry/DB fixture·OS handoff |

생성 전 IAM 쓰기 정책은 미래 자원 ARN/tag 조건으로 설계할 수 있지만, 실제 구현/API 및 backend 계약 없이 완결된 최소권한을 확정할 수 없다. actual ID가 없는 것과 source 구현이 없는 것을 구분한다. 이 collector의 목록에서 임의 bucket/instance를 자동 선택하지 않는다. AZ-name/zone-ID·AMI의 관측값도 계약 변경이나 구현 승인이 아니다.

## 3. 중앙 CloudShell 후보 검증

실행자는 이권욱, 기존 교육장 root `arn:aws:iam::774055931866:root`, Python3/AWS CLI. 이 파일 하나를 홈에 업로드하고 전달한 SHA256을 먼저 검사한 후:

```bash
python3 capture-work-role-precheck.py --simulate-assume
```

기본 모드(옵션 없음)는 입력 수집만 한다. --apply 옵션이나 AWS 변경 명령은 없다.

수집 범위:
- 정확한3인 common group membership, 각 user의 모든 소속 그룹/inline/attached policy, boundary가 있으면 해당 정책, MFA 장치 및 Access Key **메타데이터**.
- 기존 Audit와 새 IaC/Network 역할의 현재 존재·trust/inline/attached/boundary. NoSuchEntity만 ABSENT, AccessDenied/timeout/기타 오류는 STOP.
- 연결된 managed policy의 default version/document·짧은 구간의 version drift 확인. 전체 IAM snapshot이 원자적이거나 이후 변경이 없다는 증거는 아니다.
- 서울 AZ mapping/지정 AMI metadata/프로젝트 CIDR VPC/정확한3개 tag로 조회한 instance metadata/계정 bucket 이름·생성일. 태그가 누락된 다른 자원을 모두 찾았다고 주장하지 않는다. 객체/state/Parameter/Secret 값·credential은 읽지 않는다.

--simulate-assume의 추가 작업:
1. 도구에 포함된 후보5개를 로컬 파일로 만들고 Access Analyzer ValidatePolicy로 분석한다. trust는 RESOURCE_POLICY + AWS::IAM::AssumeRolePolicyDocument, identity는 IDENTITY_POLICY다. findings가 하나라도 있으면 보존하고 STOP한다. warning은 곧바로 IAM 문법 실패를 뜻하지 않으며 검토가 필요하다는 의미다.
2. SimulatePrincipalPolicy의 PolicySourceArn은 각 **일반 IAM 사용자**, PolicyInputList는 해당 개인 후보만 추가한다. 실제 user/group/managed/boundary 입력을 사용하며 거대한 ReadOnlyAccess 문서 문자열을 직접 재주입하지 않는다. root 권한을 사용자의 권한으로 평가하지 않는다.
3. 사용자3×role2×MFA(true/false/키 없음)=18건과 배정4쌍의 잘못된 session name4건, 총22건을 평가한다. 배정·MFA·본인 이름 모두 만족한4건은 allowed + MissingContextValues없음; 나머지는 implicitDeny 또는 explicitDeny를 요구한다. 예상과 다르거나 context 부족이면 STOP이다.

이 판정은 **기존 identity 정책 + 추가 후보의 identity-side AssumeRole 모의 판정**이다. role trust 자체/존재/실제 MFA 로그인·AssumeRole 또는 role 내부 쓰기 권한을 성공한 것으로 표시하지 않는다. simulator는 live 환경과 다를 수 있고 resource policy/endpoint/session/RCP 등 모든 층을 완전 증명하지 않는다. actual trust·최종 정책 적용 후 각 본인 역할 전환·대표 API 결과가 필요하다.

정상 출력: CENTRAL_PRECHECK_CAPTURE=COMPLETE, CANDIDATE_VALIDATION=NO_FINDINGS, IDENTITY_SIDE_CANDIDATE_SIMULATION=PASS, SIMULATION_CASES=22, ROLE_GRANT=NOT_RUN, APPLY_READINESS=NOT_ASSESSED, AWS_MUTATION=NOT_RUN. 이는 준비·후보 시험 결과이며 적용 허가 또는 전체 C1 완료가 아니다.

결과는 `~/fds-work-role-precheck-*`의 개인0700 디렉터리/0600 파일에 보존하고 SHA256SUMS를 만든다. stdout과 STOP 원문을 먼저 회신한다. 전체 capture는 기존 비공개 경로로 보존하며 임의 공개 게시하지 않는다. 오류 이후 grant/apply로 넘어가지 않는다. AWS 변경이 없어 AWS rollback은 없고 원본 수집 파일을 보존한다. 수정 후 새 디렉터리로 다시 수집할 수 있다.

## 4. 리뷰·실행 순서와 현재 검증

후보 root 검증은 REVIEW_AUTHORITY_POLICY §4의 병합 전 후보 시험 및 §3.2(4-1)의 순수 검증기 범위로 준비한다. IAM/자원/서버 변경·설치·상주 없음, 기존 root 권한 사용, 개인 작업 디렉터리에만 결과 저장, 부하/장애/전체 데이터 스캔 없음. 이것을 security policy 변경 실행의 리뷰 면제로 확대하지 않는다.

trust/identity JSON과 후속 업무 permissions·적용 코드는 §2/§3의 작성자 외 적격 검토자 최소1인 독립 리뷰 대상이다. PR139의 설계/ELB 승인으로 새 JSON을 승인했다고 표시하지 않는다. 혼합 PR의 병합은 코드 리뷰 기준을 유지하며 작성자 자기 APPROVE를 등록하지 않는다.

중앙 validation/simulation → 완결된 정책 리뷰 → 중앙 grant/readback/기존 설정 보존 → 해당 본인 일반 계정 MFA 역할 전환 → 업무 허용·거부·모듈 복구 → PR139 결과 양식 회신. 담당자에게 중앙 발급을 맡기거나 발급 전 쓰기 성공을 요구하지 않는다. 비용 설정·유료 구축·#35 전체 AC/Freeze 해제는 별도 기존 조건이다.

로컬 테스트 위치는 이 README 디렉터리, `python3 -m unittest discover -s tests -v`. 13개 offline unittest PASS이며 mock은 IAM simulator 실제 실행이 아니다. canonical-integrity CI는 이 단위시험을 실행한 것으로 표시하지 않는다. 준비 시점의 AWS NOT_RUN 상태는 아래 사용자 실행 결과로 갱신한다.

### 중앙 후보 검증 실행 결과 — 2026-10-06

사용자 이권욱의 CloudShell stdout 기준: UTC 2026-10-06T04:50:55.355960+00:00 / KST 13:50:55.355960. 수신 시각은13:53 KST다. 실행 source `ff85a32d79a09895a428e0fdf3fb5283739e9916`, collector SHA256 `aee2a9c4faac0abef9c2d91795250e16d34fce2a503e34c1380e3d2c081b727c`, 파일 checksum OK 및 정상 종료 출력을 수신했다.

| 항목 | 사용자 출력 판정 |
|---|---|
| 입력 수집 | CENTRAL_PRECHECK_CAPTURE=COMPLETE |
| 후보5개 분석 | CANDIDATE_VALIDATION=NO_FINDINGS |
| identity-side AssumeRole 후보22건 | PASS — 배정/MFA/본인 session name을 만족한4건 허용, 나머지18건 거부 기대 충족 |
| 현재 역할 | 기존 Audit 존재; IaC·Network ABSENT |
| 실제 trust·역할 전환 | TRUST_RUNTIME=NOT_TESTED |
| 업무 permissions 시험·역할 발급 | WORK_ROLE_PERMISSION_SIMULATION=NOT_RUN / ROLE_GRANT=NOT_RUN |
| AWS 변경·적용 준비 판정 | AWS_MUTATION=NOT_RUN / APPLY_READINESS=NOT_ASSESSED |

CASE04/08/12/22는 MFA=True라도 잘못된 session name의 거부 시험이다. 기존 Audit의 PRESENT_REVIEW_REQUIRED는 역할이 존재한다는 collector 분류이며 Audit 장애 또는 새 승인을 요구하는 판정이 아니다. 역할 부재 상태에서도 후보 simulator는 실행할 수 있으므로 allowed 결과를 실제 역할 존재·전환·쓰기 성공으로 해석하지 않는다.

원본 capture 경로는 `/home/cloudshell-user/fds-work-role-precheck-v0wj2i2q`다. Assistant가 AWS에 직접 접속하거나 capture 원본 파일·manifest를 독립 수신/재해시한 결과는 아니다. 다음은 이 후보 JSON/코드의 독립 리뷰 및 실제 resource implementation/backend/Relay SSM 입력을 받아 업무 쓰기 permissions를 완결하는 단계다. 비용 설정 제외와 각 본인 grant 후 runtime 결과 제출 순서를 유지한다.

공식 근거: [SimulatePrincipalPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulatePrincipalPolicy.html), [ValidatePolicy](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidatePolicy.html), [STS condition keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_iam-condition-keys.html), [MFA API](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_mfa_configure-api-require.html).
