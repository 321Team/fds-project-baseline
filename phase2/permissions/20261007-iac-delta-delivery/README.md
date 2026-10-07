# PR146 승인 소스의 중앙 CloudShell 실행 인계

CODEX_ASSISTED. 기준 시점 2026-10-07 KST. #35 Lead 이하영·#37 Lead 이재환, 권욱 중앙 권한 검증 지원. 비용 설정 보류·교육장 daily 비용 기반 통제·기존 일정/AC/Freeze/reviewed plan/cleanup 기준은 유지한다.

## 확인 결과와 실행 범위

- PR146 검토 HEAD `c55fd28afbba183103dec7636f67d3fa9e365f5a`: 재환 APPROVED(2026-10-07 00:29:40 KST), 하영 APPROVED(00:33:05 KST). source 기준 독립 승인이며 AWS 실행/권한 부여/인수 승인이 아니다.
- PR146은 재환의 해당 HEAD 승인 후 **00:31:47 KST**에 merge `c34ca9c12d7cb38d610829cc59460ec6a8d87b1a`로 편입됐다. 하영의 00:33:05 승인 회신은 병합 뒤 같은 HEAD의 추가 리뷰다. 병합 후 조회에서 head/merge/tree를 확인했으며 실제 GitHub `merged_at`과 마지막 `updated_at`을 구분한다.
- 이번 배포는 위 소스의 **파일15개 bytes를 변경 없이 묶은 것**이다. 새 helper/권한 JSON/실행 gate를 넣지 않았다. 기존 source 리뷰를 그대로 연결하며 단순 포장 때문에 동일 코드를 다시 승인 대기시키지 않는다.
- Linux에서 기존 단위시험16 PASS, SHA 기존10+신규3 항목 PASS. reviewer Windows의 mode0600 단언1 실패는 Linux에서 재현되지 않았다. CloudShell에서도 실행 전 같은 시험을 확인한다.
- 최초 배포 시점 AWS 실행은 NOT_RUN이었다. 이후 사용자 root 수집46케이스와 보존 capture 집계를 수신했으며 현재 상태는 [수신 기록](central-result-receipt.md)을 따른다. 본 작업 환경에는 AWS 실행 연결이 없으므로 사용자 root CloudShell에서 다음 명령을 실행하고 결과를 전달한다. collector는 IAM/S3 변경 API·S3 state 원문·SSM Parameter 값·credentials를 조회하지 않는다.

검토 원문: [PR146](https://github.com/321Team/fds-project-baseline/pull/146), [하영 회신](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6019776035), [수집 source README](https://github.com/321Team/fds-project-baseline/blob/c55fd28afbba183103dec7636f67d3fa9e365f5a/phase2/permissions/20261007-iac-delta-precheck/README.md).

## 파일과 무결성

| 항목 | 고정 값 |
|---|---|
| archive | `fds-iac-delta-precheck-20261007.tar.gz` |
| archive SHA256 | `d1ff91b564ad8c08ade9ce0e0166cee9e481cc6f81ab013864364771a7efda73` |
| collector SHA256 | `277f0b08695e486186820ec26d2087502467e2de585d10a64cf6b5f59d3b04f5` |
| 파일 수 | exact source15, `__pycache__` 제외 |
| reviewed source | `c55fd28afbba183103dec7636f67d3fa9e365f5a` |
| merged source | `c34ca9c12d7cb38d610829cc59460ec6a8d87b1a` |

archive는 경로 순서·gzip/tar mtime0·uid/gid0·파일mode600으로 만들고 풀린 파일 bytes15개를 원문과 대조했다. SHA는 배포 bytes/변경 탐지 근거이며 별도 생성자 인증·장기 audit의 대체가 아니다. source provenance는 GitHub source/독립 리뷰 기록으로 연결한다.

## 실행 전제와 순서

AWS 계정 `774055931866`의 **root CloudShell**, Python3, AWS CLIv2, Linux를 사용한다. archive와 `.sha256`를 CloudShell의 Actions → Upload file로 `$HOME`에 올린다. IAM user/Audit/Network 세션에서 중앙 수집을 실행하지 않는다. AWS CLI profile/env를 임의 전환하지 않는다. collector 첫 AWS 조회는 exact root/account 확인이며 일치하지 않으면 다음 호출을 중단한다.

**각 단계의 성공을 확인한 뒤 다음 단계로 진행한다.** `set -e/-u/pipefail`에 의존하지 않는다. 단계1 해시 불일치, 단계2 기존 경로 존재/명령 실패, 단계3 시험 실패 시 이후 실행을 중단하고 원문을 보존한다.

### 1. 업로드 archive bytes 확인

```bash
cd "$HOME"
printf '%s\n' 'd1ff91b564ad8c08ade9ce0e0166cee9e481cc6f81ab013864364771a7efda73  fds-iac-delta-precheck-20261007.tar.gz' | sha256sum -c -
```

정상: `fds-iac-delta-precheck-20261007.tar.gz: OK`. 불일치하면 재다운로드/업로드하고 그 bytes부터 다시 확인한다. 임의 정책 재작성으로 해시를 맞추지 않는다.

### 2. 새 private 경로에 압축 해제

```bash
umask 077
mkdir -m 700 "$HOME/fds-iac-delta-run-20261007-01"
```

위 mkdir가 성공해야 아래를 실행한다. 경로가 이미 있으면 **그 경로에 덮어쓰지 말고 중단**한다. 새 회차 경로를 지정할 경우 이하 경로도 동일하게 바꾼다.

```bash
tar --no-same-owner -xzf "$HOME/fds-iac-delta-precheck-20261007.tar.gz" -C "$HOME/fds-iac-delta-run-20261007-01"
cd "$HOME/fds-iac-delta-run-20261007-01/fds-iac-delta-precheck-20261007"
pwd
```

정상 pwd는 `/home/cloudshell-user/fds-iac-delta-run-20261007-01/fds-iac-delta-precheck-20261007`이다. cd 실패나 다른 위치이면 중단한다.

### 3. 대상 환경의 시험/해시 검사

```bash
python3 -m unittest discover -s phase2/permissions/20261007-iac-delta-precheck/tests -p 'test_*.py' -v
(cd phase2/permissions/20261006-iac-fixed-inputs && sha256sum -c SHA256SUMS)
(cd phase2/permissions/20261007-iac-delta-precheck && sha256sum -c SHA256SUMS)
```

정상: unittest `Ran 16 tests` + `OK`, hash 검사10항목+3항목 모두OK. 로컬 Linux 통과를 CloudShell의 실제 검사를 생략할 근거로 사용하지 않는다. 권한 mode 오류/누락/불일치가 있으면 raw를 보존하고 AWS 호출을 실행하지 않는다.

### 4. 중앙 읽기 전용 수집

```bash
python3 phase2/permissions/20261007-iac-delta-precheck/capture-iac-delta-precheck.py
printf 'IAC_DELTA_RC=%s\n' "$?"
```

첫 출력 `CAPTURE_DIR`와 마지막 `PRESERVED_DIR`, RC, 전체 summary/46행 또는 실패 행을 보존한다. 결과는 새 `$HOME/fds-iac-delta-precheck-*` private 경로이다. IAM/S3 snapshot과 ValidatePolicy·IAM simulator만 실행하며 AWS 설정 rollback 대상이 없다.

## 결과 수신 기준 — 리뷰 제안 반영

| 항목 | 수용 방식·판정 |
|---|---|
| RC0 | capture COMPLETE·ValidatePolicy NO_FINDINGS·candidate delta46 PASS만 의미. **bucket State/Readback/Checks를 별도로 읽는다.** IAM snapshot PRESENT는 기대 trust/권한 일치·grant 완료가 아님 |
| bucket 부재/차이 | ABSENT_AT_CAPTURE는 bootstrap 필요 항목, 이름 확보 보장은 아님. DIFFERENCES_REQUIRE_REVIEW는 raw protection/policy를 검토할 차이. RC0을 protection 완료/적용GO로 올리지 않음 |
| 정책 구조 비교 | 현재 비교는 dict key 순서만 무시하고 array 순서/scalar-vs-single-list 등을 구분. 구조 불일치를 즉시 권한 의미 불일치로 단정하지 않고 private raw와 후보를 대조. 자동 정규화·덮어쓰기 없음 |
| RC2/finding | WARNING/SUGGESTION도 검토 필요. summary의 identity/bucket Findings 배열을 받아 findingType별 건수와 issueCode/원본 위치를 정리하고 소스 차이를 판단. 수집기가 아직 type별 count를 자동 출력한다고 주장하지 않음 |
| 음성 판정 | EvalDecision만으로 원인 검토 완료를 표시하지 않음. private 원본의 MissingContextValues 및 explicitDeny의 MatchedStatements/SourcePolicy를 확인. 누락 context 때문에 나온 implicitDeny와 의도한 범위 거부를 구분하고 예상 밖 원인은 해당 case만 재검증 |
| malformed 응답 | 현재 main의 예외 처리에 AttributeError/IndexError 추가는 후속 방어 코드 제안으로 기록. 현 승인 코드를 포장하면서 바꾸지 않음. traceback/비정상RC이면 capture 미완료로 취급, finally manifest·raw를 보존하며 PASS/COMPLETE로 올리지 않음. source 수정이 필요하면 그 delta SHA를 리뷰 |
| IAM snapshot | 현재 trust/inline/managed/boundary/profile을 **기록**하는 단계. 완성된 desired source 대조·grant/readiness 검사는 아님. managed default version race·조회 실패는 중단 |
| role state 음성 | IAM user18 fixture가 Network/Audit/IaC 역할 세션 시험을 대신하지 않음. resource-policy role simulation은 NOT_SUPPORTED. #37 U1 때 승인된 비밀 없는 fixture가 준비되면 재환 Network role의 GetObject **및 GetObjectVersion** 거부를 별도 수신. 권욱 Network/일반 user/Audit·IaC 정상/거부 및 root 복구도 기존 경계대로 받음 |

`summary.json`에 Collection/ValidatePolicy/CandidateDeltaMatrix/BucketSnapshot/IAMSnapshot/ROOT_RECOVERY_RUNTIME/EFFECTIVE_PERMISSIONS/APPLY_READINESS 상태가 분리돼 있다. collector에 type counts/음성근거 추가/exception 변경을 적용한 것으로 표시하지 않는다. 비차단 제안은 위 수신 체크/명확한 후속 source 작업으로 수용하며 현재 승인된 수집을 다시 값 승인 대기로 돌리지 않는다.

## 전달할 결과와 다음 조치

이 대화에는 다음을 전달한다: source/collector/archive SHA, CloudShell unittest·hash 결과, 전체 수집 stdout summary·46행 또는 마지막 실패 행, `IAC_DELTA_RC`, `CAPTURE_DIR`/`PRESERVED_DIR`, 실행 UTC/KST. summary의 Findings 배열이 있으면 그대로 보존해 type별 건수 분석에 사용한다. private 원본은 기존 승인된 비공개 증적 경로로만 인계하고 공개 Issue에 IAM 전체원본/archive/state/plan/credential을 붙이지 않는다.

하영의 실제 component/resource/API/dependent-action/bootstrap/document 구현 PR/SHA 및 full IaC JSON 인계는 아직 잔여다. 관측 infra-terraform main `1f166d5c27ff24316887ae8ee2f2211fbb9a1a7d` resource0 scaffold를 완성 구현으로 올리지 않는다. 현재 결과를 받은 뒤 해당 source delta로 필요한 중앙 bootstrap/grant/readback을 구체화하고 권욱·하영 각각 자신의 IaC MFA runtime를 수신한다. #37은 actual Relay/profile/document/Agent/EBS readback → exact bind → 권욱·재환 각 본인 U1을 유지한다.

중단/실패 시 새 AWS 설정을 삭제하거나 기존 profile·backend·state 버전/증적을 초기화하지 않는다. 이 회차 source 정리는 배포 기록 수정/revert이고 실제 AWS mutation/role grant/유료 생성은 발생하지 않는다. 다음 회차는 새 경로/실행 기록으로 분리하며 과거 raw/progress를 완료 결과에 이어붙이지 않는다.

`PR146_SOURCE=APPROVED_MERGED / DELIVERY_BYTES=15_EXACT / LOCAL_LINUX_TESTS=16_PASS / AWS_VALIDATION_SIMULATION=NOT_RUN_AT_DELIVERY / AWS_MUTATION=NOT_RUN / ROLE_GRANT=NOT_RUN / USER_RUNTIME=NOT_TESTED / APPLY_READINESS=NOT_ASSESSED`
