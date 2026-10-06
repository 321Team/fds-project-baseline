# Network 실제 bind 의존성 조회 — Pre-check

CODEX_ASSISTED. 책임 #35/#37, Lead 권욱. PR143 후보 HEAD `87d1bb2533dc05927b64ed9ab7f4d9b9ff1f0ca7`는 재환 review5426140186의 독립 승인과 Lead review5426256383을 근거로 2026-10-06 18:16:11 KST merge `1059713f1a56a1a9d0d88aa37470c5e582e1d580`에 병합됐다. 하영 review5426272751은 동일 HEAD에 18:17:14 KST 추가 승인했다. 승인 범위는 star-Bool 정책 **후보 소스와 수신 결과 기록**이며 실제 grant·사용자 runtime·AC 인수가 아니다.

## 이번 후속 범위

중앙 root가 현재 서울 자원에서 실제 bind 선행조건을 조회한다. 기존 identity-side22 및 중앙 permission120 비교를 다시 실행하지 않는다. 하영의 #35 comment6011033747에 있는 3태그(`Project=fds-hybrid`, `ManagedBy=terraform`, `Phase=phase2`)와 Relay 형태(`t3.medium`, `ami-079a2667364cee804`)를 후보 식별 참고값으로 사용한다. 실제 instance ID·구현 PR/SHA·profile·문서 KMS/logging 결정을 대체하지 않는다.

| 실행 모드 | 조회/결과 |
|---|---|
| 기본 | exact account root 확인 → 기본 문서 describe/get/재조회와 self Session 문서 목록 → 기존 Network role/trust/inline·attached 목록 → 3태그가 일치하는 EC2 목록. 후보가 한 개여도 Relay를 자동 선택하지 않음 |
| `--relay-id i-…` | 위 문서/role 확인 후 지정한 실제 instance 한 개 → 해당 Agent 정보/profile·role/붙은 EBS → EBS KMS metadata·default key policy. 전체 profile/key 조회 없음 |
| `--offline` | 고정 source 해시 확인과 조회 계획 저장만 수행. AWS 호출0 |

기존 PR142 helper의 raw 보존·60초 timeout·0600 파일·exclusive write·manifest 기능을 고정 SHA256으로 재사용한다. helper의 허용 operation 집합을 **이번 조회 API 집합으로 교체**한다. simulator, AssumeRole, Start/Resume/TerminateSession, TokenValue, StreamUrl, 비용 API, 생성/수정/삭제/재시작, Secret/parameter/object 내용, 인스턴스 user-data는 호출하지 않는다. AWS CLI 자동 retry는1, 이 수집기의 조회 retry는0이다.

self Session 목록과 태그 inventory는 페이지당20·최대5페이지, 그 외 목록은 잘림을 감지하면 STOP한다. 모든 지역 API는 서울이다. 불명확한 AWS 오류·계정/반환 대상 불일치·문서 drift·과도한 pagination·manifest 저장 실패는 RC1/STOP이며 partial raw를 보존한다. `InvalidDocument`와 `NoSuchEntity`만 각각 문서 이용 불가/역할 부재로 기록한다. 문서 이용 불가에 완전한 self 목록의 이름 부재가 함께 있어도 **현재 서울 self Session 목록에서 찾지 못함**까지만 말한다. Relay 미선택/문서 부재/profile 부재/Agent 미등록은 수집 결과이며 적용 준비 완료로 판정하지 않는다.

## 실행

저장소 또는 전달 packet의 sibling 폴더 배치를 유지한다. `SHA256SUMS`는 본 폴더의3 source 파일과2 고정 dependency를 포함한다. 후보 JSON은 byte 그대로이며 placeholder가 남는다.

```bash
sha256sum -c SHA256SUMS || exit 1
python3 capture-network-binding-precheck.py
rc=$?
printf 'NETWORK_BINDING_PRECHECK_RC=%s\n' "$rc"
```

담당자가 actual Relay를 확정한 다음 같은 source로 `--relay-id`를 명시한다. 첫 inventory 결과를 이유로 자동 실행하지 않는다. 출력은 UTC/ExecutionArn/원본 capture 경로, 문서 상태와 선택된 metadata 및 미실행 경계를 포함한다. 사용자 작업 경로에만 저장하며 설정·배포 입력으로 자동 소비하지 않는다. private raw/manifest는 CloudShell에 보존하고 공개 GitHub에 통째로 붙이지 않는다. 중앙 stdout부터 수신·해시·범위를 기록한다. RC0와 COMPLETE는 조회 수집 성공이고 `ROLE_GRANT=NOT_RUN / FINAL_POLICY=NOT_CREATED / USER_RUNTIME=NOT_TESTED / APPLY_READINESS=NOT_ASSESSED`다.

## 리뷰 권고 반영과 다음 적용 순서

1. **기본 문서가 final bind 및 U1의 선행조건**이다. 담당 IaC/bootstrap에서 account owner·Session/Standard_Stream·default version/내용 SHA·KMS/S3/CloudWatch 설정과 생성/구성 source를 인계한다. 없는 문서로 발생한 오류를 사람 IAM 허용 부족으로 해석하지 않는다. 중앙 조회가 빈 KMS/logging 값을 반환해도 승인된 무KMS/무로그 설계로 간주하지 않는다.
2. 하영은 actual Relay ID/profile ARN·Agent/SourceDestCheck·EBS 및 구현 PR/SHA를 인계하고, IaC 업무 권한용 state bucket/prefix/4 key·state KMS·Relay role creator/PassRole exact ARN을 확정한다. 현재 draft JSON 전체를 후보 검토의 새 승인 대기로 삼지 않는다. 수집기로 확인 가능한 실제 상태를 먼저 수집한다.
3. 중앙은 값과 정책/trust/개인 AssumeRole 범위·기존 설정 backup·원복 계획을 연결해 actual-bound 최종 입력과 적용 code를 준비한다. PR143 후보와의 변경 부분을 validation/simulation/필요한 정확한 SHA 리뷰로 확인한 후 권한을 적용한다. 현재 조회 packet에는 적용 code가 없다. 비용 설정은 계속 보류한다.
4. 이후 권욱·재환은 **각 본인 일반 계정**으로 U1을 수행한다. CLI/plugin과 `--document-name SSM-SessionManagerRunShell`을 명시하고, STS assumed-role ARN/UserId/RoleSessionName, 실제 SessionId, owner/target 시스템 태그, shell, 본인 Resume/Terminate 및 허용된 복구·거부 경계를 제출한다. 실제 서비스에서 태그/context를 수신하지 못하면 추정해서 PASS하지 않는다. Bool 누락/오류를 보고도 BoolIfExists로 자동 완화하지 않는다.
5. StartSession/ResumeSession은 세션·호출자 정보를 가진 연결 인증 토큰을 반환한다. 허용된 Start/Resume 범위는 토큰 취득 경계를 구성하지만 **OpenDataChannel `Resource="*"`의 실제 소유자/대상 격리 증명은 아니다**. TokenValue/StreamUrl/STS credential을 보고서·로그·GitHub에 저장하지 않는다. 다른 소유자 음성 시험은 사전에 합의된 테스트용 fixture만 사용하며 **다른 사람의 진행 중인 업무 세션을 시험 대상으로 쓰지 않는다**. 실제 client/negative 증적 없이 합성 ARN deny를 격리 PASS로 바꾸지 않는다.

`ssm:DescribeSessions Resource="*"`는 서울의 다른 사용자 세션 metadata를 보여줄 수 있는 조회 범위다. 공통 ReadOnly/진단 의도에 맞는 metadata 열람이며 다른 사용자의 세션 resume/terminate 허용과는 별개다. `CompareHumanOpenDataChannelOnly` Sid 정리는 필요하면 최종 bind diff에서 한다. 이번 후속은 승인된 정책 바이트를 바꾸지 않는다.

## 검증과 분류

순수 Pre-check: 승인된 root 조회 권한 안에서 한 번 실행하고 작업 디렉터리에만 결과를 저장한다. 서버 변경·상주 설치·부하 시험·AWS 쓰기가 없다. REVIEW_AUTHORITY_POLICY §3.2/§4에 따라 후보 조회는 병합을 기다리지 않고 실행 가능하다. PR에서 reviewer를 지정하더라도 새 이중 승인 조건으로 해석하지 않는다. merge/runtime/AC는 별도 상태다.

로컬 Linux unit/mock22 PASS 및 offline packet smoke/내부 manifest 확인 PASS. 실제 AWS 실행은 NOT_RUN이다. 로컬 시험은 mock CLI를 통해 계정 guard, 고정 dependency, 실제 대상/pagination/drift/불일치, read-only allowlist, 누락과 오류의 구분, manifest 저장 전 성공 금지 및 offline0호출을 검증한다. CI 정본 검사와 이 unit/mock 시험은 별도 기록한다. 실제 AWS 실행은 사용자 결과 수신 전 NOT_RUN이다.

공식 근거(2026-10-06 확인): [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html), [ListDocuments](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ListDocuments.html), [DescribeInstanceInformation](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeInstanceInformation.html), [StartSession](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartSession.html), [ResumeSession](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_ResumeSession.html), [GetKeyPolicy](https://docs.aws.amazon.com/kms/latest/APIReference/API_GetKeyPolicy.html).
