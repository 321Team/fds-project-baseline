# Network 업무 권한 후보 — 중앙 비교 수집기

2026-10-06 사용자 착수 지시의 후속. CODEX_ASSISTED. 책임 #35 / #37, [PR141](https://github.com/321Team/fds-project-baseline/pull/141) merge `711ad113246cf9ae6c18918ce702e3c8d3bc569c` 기준이다. 기존 trust/개인 AssumeRole(PR140)과 중앙22-case는 변경·반복하지 않는다.

## 목적과 경계

이 수집기는 **배포하지 않는 가상 정책 비교와 SSM 문서 readback**만 수행한다. 실제 Relay를 생성/탐색/선택하지 않고, 역할·정책을 생성/연결하지 않으며, 세션 접속·EC2 dry-run·복구 API도 실행하지 않는다. `ROLE_GRANT=NOT_RUN`, `APPLY_READINESS=NOT_ASSESSED`는 결과와 무관하게 유지한다.

`inputs/` 2파일은 PR141의 byte 그대로이며 내부 SHA-256으로 고정한다. 기존 부분 초안은 바꾸지 않는다. 비교 정책은 해당 소스의 가상 Relay ID 치환, 문서 조건 operator 비교, human OpenDataChannel 한 statement 추가만 한다. 출력 파일명에 `SYNTHETIC-NOT-FOR-ATTACHMENT`를 붙인다. 정책 선택/실제 target 결속/최종 정책 출력이나 적용 도구는 없다.

| 비교 | 내용 |
|---|---|
| 데이터 채널 | 공식 예제의 session ARN `${aws:userid}-*` vs 권한 표의 Resource="*"; human OpenDataChannel 1종, 서울 조건 유지 |
| 문서 검사 | Bool true vs BoolIfExists true; `키 없음`은 가상 IAM context이며 **CLI의 문서 이름 생략 요청 실측이 아님** |
| 가상 target | `i-00000000000000000`, 다른 target `i-00000000000000001`; 실제 존재/승인 주장 없음 |
| 가상 caller | 권욱·재환 이름을 사용한 가상 role-id:RoleSessionName/context; 본인 로그인·trust 평가가 아님 |
| 범위 | 각 후보8 statements/18 unique actions; PR141의 17개 + OpenDataChannel만. 선택 조회3종/KMS/비용 권한 추가 없음 |

네 조합마다 30개 request 그룹(24개 기대 비교 + 6개 채널 관찰)을 준비한다. 시작/본인 세션/다른 target·문서·owner/필수 context 누락/다른 리전/복구·정확한 조회/서울 account 진단/미허용 구조·권한·Secret·Agent action을 비교한다. 각 action은 요청한 각 resource와 대조한다. 이 결과는 개별 API의 실제 resource 지원/서비스 context/의존 권한 전체를 증명하지 않는다.

[재환의 독립 리뷰](https://github.com/321Team/fds-project-baseline/pull/142#pullrequestreview-5425414640)에 따라 case29/30에 `session/321team-{gwonuk,jaehwan}-0123456789abcdef0` 형태를 추가했다. 역할 ID 없는 SessionId는 **검토자가 제시한 형식 가설**이며 실측값이 아니다. 기존 case01–28과 후보 정책/기대값은 그대로다. 첫 Stage-A에서는 실제 SessionId 형식과 본인 client 데이터 채널 동작을 함께 기록한다.

## 중앙 실행

환경: AWS CLI v2, Python3 표준 라이브러리. 위치: 교육 계정 **774055931866 root의 CloudShell**. 일반 계정·다른 계정이면 STS 확인 후 중단한다. 운영 파일/credential을 읽지 않으며 AWS 호출은 아래 allowlist뿐이다.

- STS GetCallerIdentity
- SSM DescribeDocument/GetDocument: account-owned `SSM-SessionManagerRunShell`만
- Access Analyzer ValidatePolicy
- IAM GetContextKeysForCustomPolicy/SimulateCustomPolicy

실행 묶음의 `SHA256SUMS` 검증 후 디렉터리 안에서 실행한다. archive 파일 SHA는 배포 코멘트/사용자 전달문에 별도로 제공한다. 묶음은 후보·원본·스크립트·안내·시험 코드와 내부 manifest만 포함한다.

```bash
(
umask 077
cd "$HOME/fds-network-permission-precheck-20261006" || exit 1
sha256sum -c SHA256SUMS || exit 1
python3 capture-network-permission-precheck.py
rc=$?
printf 'NETWORK_PRECHECK_RC=%s\n' "$rc"
exit "$rc"
)
```

수집기는 기본 `$HOME`에 새 `fds-network-permission-precheck-*` 디렉터리를 만들고 CAPTURE_DIR를 출력한다. 실제 IAM 허용을 root API 성공으로 판정하지 않는다. custom-policy에 후보만 입력하며 사용자 ReadOnlyAccess/guard·trust/permissions boundary/SCP/resource policy/실제 role의 다른 정책을 합산하지 않는다. 기존 identity-side22-case와 새로운 업무 permissions 평가를 구분한다.

AWS 호출 없이 실행 자료만 확인하려면 `python3 capture-network-permission-precheck.py --offline`을 사용한다. 이는 **OFFLINE_PREPARED**이며 IAM evaluator 시험이 아니다.

## 60초 중단 후 이어 실행

2026-10-06 사용자 회신의 `/home/cloudshell-user/fds-network-permission-precheck-d_poz3u_`는 arn-Bool case01–28 및 arn-BoolIfExists case01–04를 수집한 뒤 다음 호출에서 TimeoutExpired로 중단됐다. **기대 비교28개와 채널 관찰4개가 보존됐으며, 권한 판정 불일치가 아니다.** 지연의 상세 원인은 터미널 출력만으로 확정하지 않는다. 문서/validation 상태와 채널별 decision도 이 출력만으로 선언하지 않는다.

수정 묶음을 새 작업 디렉터리에 추출하고 source manifest를 검증한 뒤 다음 명령을 실행한다.

```bash
(
umask 077
python3 capture-network-permission-precheck.py \
  --resume-from "$HOME/fds-network-permission-precheck-d_poz3u_"
rc=$?
printf 'NETWORK_PRECHECK_RC=%s\n' "$rc"
exit "$rc"
)
```

- 원본 디렉터리에 쓰지 않는다. 모든 flat regular file을 SHA256SUMS와 대조하고, 원본 collector SHA(최초 PR142 `ec395ac1…` 또는 현재 수집기), PR141 입력·candidate 정책·root/계정·경계 및 transient simulator 실패를 확인한다. 이전 수집기 파일을 실행하지 않는다.
- 완료로 기록된 각 case의 **request·expectations·raw status/stdout**을 확인하고 현재 파서로 재판정한다. summary의 PASS만 믿고 건너뛰지 않는다. InvalidInput 관찰도 raw 오류를 확인한 검토 항목으로만 재사용한다. byte manifest는 일관성 검증이며 외부 서명/실제 서비스 증명이 아니다.
- 새 private 디렉터리에 원본 바이트를 `prior-*` 이름으로 복사하고 원본 manifest/collector/UTC 및 case별 evidence 경로를 보존한다. 기존 디렉터리를 수정/삭제하지 않는다. 새 중단도 같은 수집기에서 이어 실행할 수 있다.
- **현재 root와 기본 문서를 다시 조회**하고 문서 상태/버전/내용 SHA/KMS/logging이 이전 capture와 다르면 중단한다. ValidatePolicy/context keys는 현재 상태로 다시 수집한다. 완료 simulation 요청32개는 반복하지 않고 나머지 및 신규 관찰8개를 호출한다(정상 완료 시 reuse32/fresh88). 각 후보의 신규 case29/30은 해당 후보의 기존 case들 뒤에 실행된다.
- AWS CLI child에 connect10초/read45초, subprocess60초 및 `AWS_MAX_ATTEMPTS=1`을 적용한다. **SimulateCustomPolicy의 timeout/명시된 연결·throttling 오류에만 3초 후 최대1회 추가 시도**한다(호출 그룹 최대123초). 각 시도의 원본/timeout 조각을 따로 저장한다. 다른 조회는1회이고 AccessDenied/InvalidInput/JSON 오류·판정 불일치는 자동 재시도하지 않는다. 프로필/credential/정책·예상값은 바꾸지 않는다.

CLI 설정은 child process에만 적용하며 계정의 설정 파일을 변경하지 않는다. 반복된 transient 실패는 STOP/RC1로 보존한다. 네 후보 중 채널 ARN 오류를 `*` 권한 적용으로 바꾸지 않는다. 위 timeout/retry 제한은 네트워크 장애나 서비스 장애가 실제 원인임을 단정하는 조치가 아니다.

## 결과 수신·중단 기준

| RC/표시 | 의미·처리 |
|---|---|
| 0 + NETWORK_CANDIDATE_CAPTURE=COMPLETE | 수집 및 기대 비교가 끝났고 ValidatePolicy findings가 없음. 채널/문서 선택·적용 GO·본인 runtime PASS는 아님 |
| 2 + NETWORK_CANDIDATE_CAPTURE=COMPLETE | findings 또는 채널 실험 InvalidInput을 보존했고 검토 필요. ERROR findings 후보는 matrix를 건너뛰며 다른 고정 후보를 비교함 |
| 1 / STOP / COMPLETE 없음 | 계정·원본 해시·CLI·version drift·예상 판정/누락·증적 저장 실패 등. 이후 적용 금지, PRESERVED_DIR의 원본으로 원인 확인 |
| OFFLINE_PREPARE=COMPLETE | AWS 미호출 입력 준비만 완료 |

정상 수집에서는 summary.json의 각 후보 Validation/Findings/Matrix/Cases, Document 상태, CHANNEL_SELECTION=NOT_MADE를 확인한다. ValidatePolicy 경고도 자동 수용하지 않는다. 채널은 관찰 결과만 기록하고, ARN 비교의 allowed 또는 InvalidInput을 서비스 격리의 성공/거부 증거로 바꾸지 않는다. 후보 ARN 실패 뒤 Resource="*"를 **자동 선택하지 않는다**. 별도 최종 변경 diff·검증·리뷰가 필요하다.

최신 IAM 응답의 action 요약과 `ResourceSpecificResults`를 구분한다. 요청 action/resource 누락·중복·예상 밖 context·truncation은 중단한다. 복수 resource를 최상위 EvalDecision 하나로 통과시키지 않는다. 단일 `*` aggregate 및 정확한 단일 resource를 식별한 과거 응답만 제한적으로 수용한다. 채널 aggregate만 있으면 ARN별 결론 없이 관찰 표시한다.

COMPLETE는 summary와 SHA256SUMS 저장 이후에만 출력한다. COMPLETE 문자열만 확인하지 말고 실제 RC와 manifest를 함께 확인한다. 저장 실패가 있으면 summary에 앞선 계산 결과가 있어도 완결된 증적이 아니다. raw stdout/stderr와 timeout 부분 응답은 private0600으로 보존하며 터미널에 원문을 출력하지 않는다. 정상 완료 후 Document 상태, validation/findings 수, 재사용/새 case 수 및 합성 CHANNEL_OBSERVATION만 터미널에 표시한다. 실제 문서 내용·logging/key 설정은 자동 출력하지 않는다.

CAPTURE_DIR 내부에서 다음 검증을 수행하고 터미널 결과·summary.json을 회신한다. 기본 문서 원문을 포함한 전체 수집물은 private 상태로 보존하고 공개 코멘트에 그대로 붙이지 않는다. 실제 credential/TokenValue/PSK/Parameter/Secret/S3 object content는 이 수집기의 조회 대상이 아니다.

```bash
# 아래 경로는 실제 CAPTURE_DIR 출력값으로 치환한다.
(
cd "$HOME/fds-network-permission-precheck-출력값" || exit 1
sha256sum -c SHA256SUMS || exit 1
cat summary.json
)
```

AWS 변경이 없으므로 원복 API는 없다. 실패 원본을 보존하고 수정 SHA에서 필요한 범위만 재검증한다. 중단 상태를 grant로 진행하지 않는다.

## 문서와 최종 인계

기본 문서가 없거나 SSM이 InvalidDocument를 반환하면 ABSENT_OR_UNAVAILABLE로 기록하고 가상 후보 비교는 계속한다. 수집기가 문서를 만들거나 AWS 제공 문서로 대체하지 않는다. 존재하면 전후 DescribeDocument의 owner/name/type/default-version/hash/status와 GetDocument version/name/type·Standard_Stream을 대조한다. 내용 UTF-8 해시 및 session KMS/S3/CloudWatch 설정을 기록한다. default-version/metadata 변경·owner/type 불일치는 중단한다. readback은 문서명 생략/콘솔/CLI client 동작의 실측이 아니다.

KMS 항목은 **SSM 세션 데이터 암호화 설정**이다. Relay EBS Start 복구에 사용하는 key/키 정책/필요 grant와는 별도이며 #35 handoff에서 확인한다. 현재 KMS·로그 설정을 조회했다고 그 의존 권한을 새 allow로 추가하지 않는다. EC2 콘솔의 Agent 자동 업데이트 요구가 나오면 기존 #35 bootstrap에서 해결하며 사람 Network에 SendCommand를 자동 추가하지 않는다.

수집 결과 → 채널·문서 조건의 최종 후보 판단/변경 범위 리뷰 → 실제 Relay/document/profile/EBS key에 결속 → 중앙 role grant/readback/기존 설정 보존·원복 → 권욱/재환 각각 본인 U1 및 첫 Stage-A client 확인으로 연결한다. 실제 서비스 판정이 미확인이므로 완결 최소권한/격리를 선언하지 않는다. 모듈 복구는 담당자1회 증적을 재사용하고 기존 TS06 SA-down·평문 우회 차단/DPD·rekey/복구를 유지한다.

하영의 IaC JSON은 현 시점 로컬 미커밋이다. backend/key/KMS/profile 생성 책임/API 구현 입력을 #35에 연결하며, IaC 전체나 실제 ID가 나올 때까지 이 가상 후보 준비를 막지 않는다. 기존 일정/담당/AC/Freeze·티켓 상태는 변경하지 않는다.

## 검증·리뷰 분류

후보 비교를 위한 Pre-check이며 운영 배포 입력이 아니다. 수집기·비배포 fixture/시험·안내를 PR로 공유하고 하영/재환에게 코드·평가 경계 리뷰를 요청한다. [REVIEW_AUTHORITY_POLICY §4](https://github.com/321Team/fds-project-baseline/blob/main/governance/REVIEW_AUTHORITY_POLICY.md)에 따라 병합 전에도 이 read-only 후보 시험을 할 수 있으며, 새 IAM 실행 정책/최종 적용 코드의 독립 리뷰를 대체하지 않는다. 두 명의 별도 필수 서명을 추가하지 않는다.

오프라인 시험은 API 응답 파서의 실패/누락/중복·잘못된 root·쓰기 차단·private raw 보존·timeout·manifest 실패·default-version drift·findings 및 resume 분기를 검증한다. 29개 unit/mock 시험은 정책 evaluator가 아닌 응답/실행 제어 시험이다. 원본 hash 변조·재서명된 request 변경·summary와 raw 불일치·문서 drift·이중 중단 후 원본 재사용을 다룬다. 최초 AWS 수집은 위 사용자 회신의 부분 결과로 한정하며, 수정 수집기의 실제 이어 실행은 회신 전 NOT_RUN이다.

공식 근거(2026-10-06 확인): [SimulateCustomPolicy](https://docs.aws.amazon.com/IAM/latest/APIReference/API_SimulateCustomPolicy.html), [EvaluationResult](https://docs.aws.amazon.com/IAM/latest/APIReference/API_EvaluationResult.html), [ResourceSpecificResult](https://docs.aws.amazon.com/IAM/latest/APIReference/API_ResourceSpecificResult.html), [ValidatePolicy](https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_ValidatePolicy.html), [SSM action/resource](https://docs.aws.amazon.com/service-authorization/latest/reference/list_ssm.html), [ssmmessages action/resource](https://docs.aws.amazon.com/service-authorization/latest/reference/list_ssmmessages.html), [Session Manager 예제](https://docs.aws.amazon.com/systems-manager/latest/userguide/getting-started-restrict-access-examples.html), [DescribeDocument](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DescribeDocument.html), [GetDocument](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_GetDocument.html).

CLI 실행 제한 참고: [AWS CLI retry 설정](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-retries.html), [CLI SimulateCustomPolicy 옵션](https://docs.aws.amazon.com/cli/latest/reference/iam/simulate-custom-policy.html). API 성공을 실제 세션 성공으로 해석하지 않는다.
