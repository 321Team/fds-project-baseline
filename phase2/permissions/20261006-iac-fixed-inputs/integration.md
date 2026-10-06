# #35 구현 source와 검증 인계

CODEX_ASSISTED. Lead 채택 값은 `inputs/lead-values.json`을 사용한다. 이 문서는 부분 후보를 실제 Terraform/완성 IaC permissions에 연결하는 인계 요구사항이다. 담당·일정·AC를 바꾸지 않는다.

## 하영 구현 PR/SHA에 연결할 내용

| 항목 | 인계할 source·실제 검증 |
|---|---|
| 4 state 소유권 | component root/module 경로→채택 exact key→한 번만 관리하는 resource→actual output→소비자→생성/정리 순서. 동일 root 구성의 key만 바꾸어 네 번 실행하지 않음 |
| network/vpn 경계 | VPC/4 subnet/IGW/route-table/Relay/ENI/EIP/SG/route의 실제 한 소유자. inline route와 별도 route resource 중복 없음. AWS route authority=Terraform 유지 |
| API/권한 | actual resource/data/API/dependent action별 action/resource/조건. RunInstances의 AMI·subnet·SG·ENI·volume·instance, tag-on-create와 후속 tag mutation을 구분 |
| 태그 | Project=fds-hybrid/ManagedBy=terraform/Phase=phase2를 source와 IAM 양쪽에서 확인. 외부/default 자원 retag로 관리 범위 확대·보호 태그 제거의 음성 |
| backend/provider | 각각 account allow-list; component별 격리 workdir/TF_DATA_DIR; default workspace 검사. credential은 HCL/backend-config/plan에 미저장 |
| 중앙 bootstrap | 검토된 desired source→before snapshot→bucket 소유/서울/보호 설정→Relay role/profile/trust/정책/version/hash→readback 및 보호 복구. 일반 IaC는 profile data 참조 |
| Session document | #37 결정의 DocumentType=Session/content.sessionType=Standard_Stream 및 default version/content source. owner/type/version/hash/settings readback. public SSH 미개방 |
| Agent/profile | actual policy version/hash/API 범위와 Parameter 원문 미조회 통제, Agent Online/OS user/sudo/IMDSv2/management egress. 관리형 정책을 사람 role에 복사하지 않음 |
| EBS | gp3 40GiB encrypted, alias/aws/ebs의 실제 KmsKeyId와 생성/Start 복구 의존성, DeleteOnTermination source 기대·실제값 |
| #38/ROSA | 실제 prerequisite/runtime 소스가 나온 범위만 IAM/OIDC/Operator/API 추가. 이름/state key 채택만으로 사전 광역 부여하지 않음 |

현재 resource 0개 scaffold에는 이 source/API가 없으므로 EC2 write JSON을 추정 완성하지 않는다. 부분 정책 검토는 지금 진행하며 이후 source 변경과 영향 범위만 검증한다.

## provider account guard 반영안

아래는 현재 `infra-terraform` provider 블록에 반영할 제안 diff다. **이 묶음이 실제 infra-terraform 코드를 변경한 것은 아니다.** account guard를 추가하는 구현 PR에서 fmt/validate를 확인하며 backend의 같은 guard는 각 candidate HCL에 있다.

```diff
 provider "aws" {
   region = var.aws_region
+  allowed_account_ids = ["774055931866"]
```

별도 component root마다 기존 Terraform 1.16.4/provider 6.66.0 pin·검토된 lock을 유지한다. 다른 OS/architecture에서 실행할 때는 설치 bytes/플랫폼/lock 지원을 확인한다. adapter의 account/region/ARN/AZ Name·ZoneID/AMI는 provider-neutral VPN 계약과 분리한다.

## 중앙 validation과 실제 시험

1. **실행 소스/정책 완성·검토:** 정확한 PR HEAD, 실제 module/API와 부분 정책의 합성 diff, trust·개인 AssumeRole의 변경 유무를 연결한다. 작성자 외 적격 reviewer가 코드/정책을 검토한다. AI 자체 fixture PASS는 독립 승인이 아니다.
2. **중앙 순수 사전검증:** 기존 허용 root 경로에서 Account/ARN 확인, 현재 정책·trust·profile·bucket 보호 snapshot/소유 충돌 확인, JSON 변경의 ValidatePolicy와 delta simulation. partial policy만으로 전체 업무 권한 PASS를 표시하지 않는다. resource-policy/role simulator 제한은 별도 표시한다. 이 묶음에는 해당 AWS collector나 apply helper가 없다.
3. **중앙 적용/readback:** 검토된 source와 승인된 실행 범위에서 새 bootstrap/role 부여분만 적용하며 before/after semantic/bytes hash를 구분한다. bucket Versioning/PAB/Ownership/Encryption/정책과 profile 실제 부여분이 기대와 같아야 한다. 불일치·이름 소유 충돌·잘못된 account/region·예상 밖 IAM/destroy면 STOP.
4. **각 본인 runtime:** 권욱·하영의 IaC MFA AssumeRole/본인 session name, 대표 allow/deny/복구를 각각 수신한다. 일반 사용자 3인·Audit의 비밀 없는 state fixture GetObject/GetObjectVersion 거부, IaC의 정상 state/lock 접근·미허용 key/role/region/PassRole 거부를 확인한다. 공통 ReadOnly 대표 검증 재사용과 개별 write-role 본인 검증을 구분한다.
5. **backend 정상·실패·복구:** init/lock 경합/정상 해제/중단 후 lock 상태. live writer 부재·lock ID 확인 후에만 force-unlock. 중앙 복구는 before 원본·선택 VersionId·lineage/serial·현재 resource drift·복구 후 plan 비교. 자동 DeleteVersion/강제 copy/force-push로 우회하지 않는다.
6. **유료 생성·실제 인계:** 기존 #34 Freeze·reviewed plan·교육장 비용 정보/예상 가동·cleanup 조건이 충족된 작업창에서 #35가 구축한다. source/입력 식별/backend/workspace/toolchain/lock/plan SHA/검토 HEAD/apply RC·UTC/actual ID·설정/원본 증적을 manifest로 연결한다. 비용 설정 권한 보류 유지. #37에는 비밀 없는 actual artifact를 전달하고 원문 state 접근을 열지 않는다.
7. **Network 후속:** 새 actual Relay/profile/document/Agent readback→exact bind/grant→권욱·재환 각각 U1. 교체 시 옛 ARN 제거/새 ARN 추가 및 변경 부분 validation/simulation/readback/U1. 새 인계를 합성 ID로 대신하지 않는다.

기존 10/8 actual Stage-A handoff→#37 10/12 착수→#35 Full/#37 10/14 G4 목표와 선행조건을 유지한다. 미완료 인계는 STAGE_A_READY=NO이다. 새 승인 문서를 단계마다 추가하거나 Support 상시 이중승인을 만들지 않는다. 현재 blocker는 실제 implementation/API/full permissions source와 검증 증적이며 채택 값 재회신이 아니다.

## 중단·복구 경계

AWS 미적용 상태인 이 후보의 정리는 PR 수정/닫기 및 로컬 후보 삭제로 충분하다. 이후 적용 회차의 원복은 실제 before snapshot과 정확한 새 부여분으로 정한다. 운영 중 profile·backend/state 버전·증적을 일괄 삭제하지 않는다. source/ARN/key/정책 drift, 예상 밖 파괴·권한 상승·비밀 노출·원복 불명확·기존 GO 조건 미충족이면 그 쓰기를 중단하고 원본을 보존한다.
