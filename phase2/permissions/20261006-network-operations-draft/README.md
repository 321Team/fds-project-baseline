# Network 업무 권한 초안 — 검토용, 미적용

2026-10-06 사용자 IAM 업무 역할 진행 지시의 후속. CODEX_ASSISTED.
입력: [재환 #37 운영·시험 범위](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-6010498202), [보완 리뷰·초안 GO](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-6010632111).
역할 진입 trust/개인 AssumeRole 후보는 [PR140](https://github.com/321Team/fds-project-baseline/pull/140) merge b5d8b88f676d7e0a5f586478347bae3a4b6a4746를 재사용하며 재승인·동일22-case 재시험을 요구하지 않는다.

## 이번 산출물과 제한

`network-permissions.template.json`은 사람 역할 FDS-Network-Operator의 **부분 permissions 초안**이다. `__RELAY_INSTANCE_ID__`는 실제 ID가 아니며 IAM 변수도 아니다. 해당 이름을 임의 instance/와일드카드로 치환해 적용하지 않는다. 데이터 채널 미확정과 실제 입력 결속·검증/리뷰가 남아 있어 이 파일은 배포 입력이 아니다. 적용 도구/명령은 제공하지 않는다.

| 범위 | 초안 |
|---|---|
| 접속 | exact Relay + account-owned SSM-SessionManagerRunShell 문서만 StartSession; 문서 접근검사 true 요구 |
| 본인 세션 관리 | Resume/Terminate는 서울 account session ARN과 AWS 제공 owner=`${aws:userid}`, target=exact Relay의 두 태그가 모두 일치해야 허용 |
| 복구 | exact Relay의 Reboot/Stop/Start만 허용 |
| 제한 가능한 조회 | exact Relay GetConsoleOutput/GetConnectionStatus |
| account/서울 조회 | EC2 Describe6종·SSM metadata/session 목록·CloudWatch GetMetricData. Resource="*"는 Relay 한 대만 조회하는 IAM 경계가 아님 |
| 데이터 채널 | 별도 channel-options.review.json에 두 공식 근거의 후보를 보존, permissions에 둘 다 미편입 |

ssmmessages CreateControlChannel/CreateDataChannel/OpenControlChannel은 사람 역할에서 제외한다. Agent 4종 채널은 #35의 instance profile 범위로 분리한다. Network 사람 역할에 IAM/PassRole/Secret·Parameter/KMS/비용 설정, Run Command, 포트포워딩/SSH 문서, EC2 Terminate/Modify/tag/EIP/route/SG/NACL 변경은 허용하지 않는다. 이 초안에 없는 action은 최소 정책만 부여하는 최종 role에서는 implicit deny이며, 다른 정책을 추가한 role의 전체 효과는 중앙에서 별도 검증한다.

MFA+본인 RoleSessionName은 승인된 trust에서 요구한다. role 내부 API에 MFA=true를 다시 요구하지 않는다. 일반 계정의 ReadOnlyAccess는 role 세션과 합산되지 않으며, 업무 role에 ReadOnlyAccess 전체를 편의상 연결하지 않는다. 두 사람 이름의 session 패턴을 단순 합치지 않는다. aws:userid 소유자 태그의 exact 조건은 후보이며 실제 공급된 태그·caller 매핑을 첫 세션에서 확인한다.

## 채널·문서 결속에서 남은 판단

AWS Session Manager 예제는 OpenDataChannel에 session ARN 패턴을 제시하고 ssmmessages 권한 표는 resource ARN 미지원으로 적는다. 두 설명을 대조했지만 actual client/plugin의 접속 판정은 미확인이다. 예제를 복사해 채널별 격리를 증명했다고 하거나 실패 뒤 Resource="*"/Agent 4종으로 자동 확대하지 않는다. 두 옵션은 선택·적용된 정책이 아닌 검토 입력이다. Resource="*" 선택 시에도 sole human OpenDataChannel, region 및 Start/Resume/Terminate의 target/owner 통제를 유지하고 최종 변경 범위를 리뷰한다. 이 선택은 채널 ARN 격리의 실증이 아니다.

중앙에서 실제 SSM 문서 존재/Owner/account/DocumentType=Session/default version/content SHA/sessionType=Standard_Stream을 readback한다. 내용·버전이 바뀌면 최종 검증 입력을 다시 고정한다. StartSession에는 DocumentVersion 입력이 없으므로 지원하지 않는 버전 옵션이나 IAM condition을 추가하지 않는다. 문서명을 생략하면 API는 default shell을 사용한다. 따라서 이름 생략 자체를 무조건 거부라고 쓰지 않고, 승인된 default 문서로 해석되는 요청만 허용되는지 문서 접근검사와 실제 client에서 확인한다. 다른 문서/port forwarding/SSH/SendCommand 거부를 따로 시험한다.

aws:userid·session owner/target 태그는 service가 공급한 값으로 실제 확인해야 한다. simulator에 넣은 context 값이 서비스 readback 증거는 아니다. OpenDataChannel·문서 접근검사·소유자 결속이 미확인인 현재 template만으로 완결된 최소권한 또는 적용 GO를 선언하지 않는다.

## 중앙 및 본인 시험 계획 — 아직 미실행

| 시험 | 정상/음성 기대 |
|---|---|
| StartSession | Relay+승인 문서+검사 true 허용; 다른 instance/다른 문서/검사 false·키 없음 거부. 두 resource의 판정과 실제 client 결속을 함께 확인 |
| Resume/Terminate | 본인+Relay 허용; 타인/다른 target/owner·target 키 없음 거부 |
| 복구 | exact Relay의 Reboot/Stop/Start 허용; 다른 instance·서울 외 요청 거부 |
| 구조/Secret/권한 | Terminate/Modify/route/SG/tag/EIP/SendCommand/IAM/PassRole/KMS/Secret·Parameter/비용 설정의 미허용을 평가 |
| 조회 | 명시한 서울 진단 허용; 서울 외 요청 거부; account-wide metadata 조회 범위를 명시 |
| 사람/Agent 채널 | CreateControl/CreateData/OpenControl 사람 role 미허용; OpenData는 선택 후보 검증/실제 client 확인, 태그 context 주입만으로 격리 PASS 금지 |

최종 JSON 결속 후 중앙 root에서 ValidatePolicy 및 role permission 후보 simulator를 실행하고 원본/해시·누락 context를 보존한다. 비용·자원 생성 없이 후보 시험할 수 있으며 root 자체의 권한으로 사용자 허용을 증명하지 않는다. 실제 role이 있으면 trust/attachment/inline/boundary 전체와 동시 변경을 확인한다. 적용은 검토된 최종 정책과 별도 중앙 grant/readback/기존 설정 보존·원복 절차로 준비한다. 이 초안의 merge나 PR140 승인으로 grant GO를 대체하지 않는다.

권한 음성은 중앙 simulator와 지원 EC2 API의 --dry-run으로 우선 검증한다. UnauthorizedOperation=거부 기대, DryRunOperation=허용되어 음성 FAIL이다. 실제 Terminate/구조 변경을 호출해 거부를 기대하지 않는다. 타인의 진행 중 세션을 종료 시험 대상으로 사용하지 않는다. 본인 계정 U1은 권욱/재환 각각 받고, 동일 target/source의 터널·모듈 복구 전체는 담당자1회 증적을 재사용한다. 기존 TS06 SA-down/평문 우회 차단·DPD/rekey·복구 및 TS04/05/15를 유지하며 실제 source/return route와 앱 접근 범위를 결속한다. selector 범위를 VPC 전체 앱 접근 허용으로 해석하지 않는다.

## #35 인계 및 현재 상태

하영의 Terraform resource implementation/API/backend/KMS·PassRole 입력은 아직 미수신이다. 미래 ARN/tag로 권한 초안을 설계할 수 있고 actual ID 부재 자체를 초안 준비의 차단으로 만들지 않는다. 현재는 broad target 대신 exact ID placeholder를 사용하고 Stage-A의 실제 Relay 생성 후 결속한다. 태그 기반 허용을 선택하려면 확정된 Relay 구분 tag 계약이 별도 필요하며 이 초안은 이를 임의 생성하지 않았다.

CentOS Stream10은 확인 시점 AWS 지원표에 명시되지 않고 CentOS Stream9만 명시된다. Agent 버전·공식 RPM/서명·install/enable/start 및 S3 download/repo/DNS/HTTPS 경로를 #35 bootstrap에 결속하고 기존 Stage-A의 첫 Relay에서 Online→지정 셸 접속을 확인한다. 별도 유료 PoC·생성 전 runtime PASS·public SSH 우회를 추가하지 않는다. AMI를 임의 교체하지 않는다.

sudo SSM 셸은 OS 관리자 접근이며 IAM에서 Run Command/포트 문서를 제외했다고 root 명령/터널링까지 제한한 것은 아니다. Instance profile은 Agent 전용으로 분리하고 AmazonSSMManagedInstanceCore의 GetParameter/GetParameters를 사람 role의 미요청과 구분한다. PSK input logging/xtrace/argv/증적 포함 금지와 root-owned0600 저장, local transcript의 한계는 #37 보완 리뷰를 따른다. 중앙 S3/CloudWatch 세션 로깅/Parameter Store 전환을 새 필수 조건으로 넣지 않는다.

상태: DRAFT=부분 permissions/미확정 채널 후보 작성; STATIC=JSON 구문·한정 action/resource/region·소유자 조건 점검; AWS_VALIDATE/SIMULATOR/RUNTIME/ROLE_GRANT=NOT_RUN; APPLY_READINESS=NOT_ASSESSED. 비용 설정 제외, 담당/AC/일정/Freeze·티켓 종결은 불변이다. 새 JSON은 실행형 정책 입력으로 확정될 소스이므로 독립 코드 리뷰 대상이며 작성자 자기 승인/PR140 승인 재사용은 하지 않는다.

## 공식 근거

- [Session Manager 예제·AWS session tags](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-restrict-access-examples.html)
- [SSM action/resource/condition](https://docs.aws.amazon.com/service-authorization/latest/reference/list_ssm.html)
- [ssmmessages 권한 표](https://docs.aws.amazon.com/service-authorization/latest/reference/list_ssmmessages.html)
- [StartSession API](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartSession.html)
- [SSM 지원 OS](https://docs.aws.amazon.com/systems-manager/latest/userguide/operating-systems-and-machine-types.html)
