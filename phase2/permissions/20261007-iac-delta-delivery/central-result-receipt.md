# 중앙 IAM delta 수집 결과 수신과 bootstrap 인계

CODEX_ASSISTED. 사용자 CloudShell 출력 수신: 2026-10-07 01:20:42 KST. #35 Lead 이하영·#37 Lead 이재환, 권욱 중앙 검증 지원. 이 문서는 수신 기록·후속 자료이며 정책 적용 입력/신규 apply helper가 아니다.

## 결론과 증적 범위

**부분 후보의 AWS 사전검증 결과를 수신했다:** archive/source 해시 검사, CloudShell unittest16 PASS, ValidatePolicy identity/bucket 각0 findings, delta46 PASS, Collection COMPLETE, RC0. 원본 capture 파일을 직접 받거나 AWS를 assistant 환경에서 재조회한 것은 아니다. [정리 JSON](received-central-result-summary.json)은 사용자 로그를 정리한 수신 기록이며 원본 API 응답/불변 증적을 대신하지 않는다.

summary.UTC `2026-10-06T16:14:01.215913+00:00`는 10/7 **01:14:01 KST**다. collector가 IAM snapshot과46 simulation 전에 만든 시각이며 수집 종료 시각으로 표시하지 않는다. 결과 보존 경로는 `/home/cloudshell-user/fds-iac-delta-precheck-j2uxfqvr`다.

| 확인 항목 | 수신 결과·의미 |
|---|---|
| 주체/지역 | account774055931866 exact root, 서울 endpoint |
| source | 후보 JSON3 해시·collector277f0b08…·archive d1ff91b5…가 배포값과 일치. CandidateSourceMerge f1e66492는 PR145 정책 출처이고 collector PR146 HEAD c55fd28/merge c34ca9c1와 다른 역할의 ref이며 불일치가 아님 |
| CloudShell 사전검사 | unittest16 OK, source manifest10+3 OK, Python3.13.15/AWS CLI2.37.6/Linux. Windows mode0600 실패가 대상 Linux에서는 재현되지 않음 |
| ValidatePolicy | identity0/bucket0, ERROR/SECURITY_WARNING/WARNING/SUGGESTION 모두0. 원본 findings 위치 검토가 필요한 행은 없음 |
| simulation | 부분 identity28 + user3 bucket Deny override fixture18 =46 PASS. 실제 EC2/IAM/S3 쓰기나 현 user RO/guard/full work-role 실효권한 검사는 아님 |
| IAM 부재 | IaC/Network/Relay role과 Relay profile이 수집시점 ABSENT. Audit은 PRESENT_SNAPSHOT_ONLY, 기대 trust/권한 인수 완료는 아님 |
| bucket 부재 | exact backend ABSENT_AT_CAPTURE, bootstrap NOT_RUN. 서울 위치/보호 설정 PASS가 아니며 전역 이름 확보도 보장되지 않음 |
| 미실행 | AWS mutation/role grant 없음, 본인 runtime/root 복구/실효권한 미검증, apply readiness 미평가. 이번 collector는 EC2 Relay/EIP/SSM document inventory를 하지 않았으므로 그 부재를 새로 주장하지 않음 |

현재는 **수집·부분 후보 사전검증 단계 통과**이며 전체 업무 권한 부여·bootstrap/Stage-A GO·본인 U1·AC 인수로 올리지 않는다. 일반 사용자/Audit/Network의 실제 S3 state 접근 차단은 bucket 정책이 적용되고 승인된 비밀 없는 fixture/본인 세션이 준비된 뒤 확인한다.

## 재실행 없이 음성 판정 근거 수신

review의 negative MissingContextValues/MatchedStatements 확인을 마무리한다. 아래는 **이미 보존된 파일을 조회·정리**하는 명령이며 AWS API 호출이나 capture 파일 수정이 없다. root46케이스를 다시 실행하지 않는다. 원본 정책·credential·state는 출력하지 않는다.

1. private capture manifest를 확인한다.

```bash
capture_dir="$HOME/fds-iac-delta-precheck-j2uxfqvr"
(cd "$capture_dir" && sha256sum -c --status SHA256SUMS)
printf 'CAPTURE_MANIFEST_RC=%s\n' "$?"
```

정상 RC0이어야 다음을 실행한다. RC가 다르면 원본을 보존하고 차이를 먼저 확인한다. 새 hash를 만들거나 파일을 고쳐 통과시키지 않는다.

2. simulator 응답에서 정제된 집계를 조회한다.

```bash
jq -s '
  [ .[] | .EvaluationResults[]? ] as $rows |
  {
    SimulationResponseCount: ([.[] | select(has("EvaluationResults"))] | length),
    ActionEvaluationCount: ($rows | length),
    DecisionCounts: ($rows | group_by(.EvalDecision) |
      map({Decision: .[0].EvalDecision, Count: length})),
    NegativeRowsWithMissingContext: [
      $rows[] | select(.EvalDecision != "allowed") |
      ([.MissingContextValues[]?,
        (.ResourceSpecificResults[]? | .MissingContextValues[]?)] | unique) as $missing |
      select(($missing | length) > 0) |
      {Action: .EvalActionName, Decision: .EvalDecision, Missing: $missing}
    ],
    ExplicitDenyRowsWithoutMatchedStatements: [
      $rows[] | select(.EvalDecision == "explicitDeny") |
      select(((.MatchedStatements // []) | length) == 0) |
      {Action: .EvalActionName, Decision: .EvalDecision}
    ],
    ExplicitDenySourceCounts: [
      $rows[] | select(.EvalDecision == "explicitDeny") |
      .MatchedStatements[]? |
      {SourcePolicyId: .SourcePolicyId, SourcePolicyType: .SourcePolicyType}
    ] | group_by([.SourcePolicyId, .SourcePolicyType]) |
      map(.[0] + {MatchedStatementCount: length})
  }
' "$capture_dir"/*-case-*-attempt*.stdout
printf 'NEGATIVE_EVIDENCE_RC=%s\n' "$?"
```

소스상 정상 기준은 response46, action evaluation93, allowed28/explicitDeny50/implicitDeny15다. 이 숫자는 **reviewed source에서 계산한 기대값**이며 아직 수신한 raw 집계가 아니다. negative MissingContext가 있으면 누락 때문에 발생한 거부인지 `Null` 조건에서 의도한 키 부재인지 해당 조건/ResourcePolicy/MatchedStatements를 원본과 대조한다. 배열이 있다는 이유만으로 FAIL로 바꾸지 않는다. explicitDeny의 근거 없는 행도 별도 조사한다. IAM custom input/ResourcePolicy에서 온 source 식별을 확인하고 예상 밖 policy origin을 검토한다. implicitDeny에는 matched statement가 없는 것이 가능하므로 explicitDeny의 근거 검사와 혼동하지 않는다.

위 집계는 자동 grant/merge gate가 아니라 결과 수신용 조회다. retry의 partial/에러 stdout 때문에 jq parse 실패 또는 response 수 차이가 나면 해당 private 파일·성공 attempt를 구분해서 다시 **조회**한다. 그 이유만으로 AWS46케이스 전체를 재실행하지 않는다. 공개 채널에는 정제 집계만, private 정책/전체 raw는 기존 승인된 비공개 증적 경로로만 전달한다.

## bootstrap source와 작업 역할 인계

최신 조회에서 infra-terraform main은 `1f166d5c27ff24316887ae8ee2f2211fbb9a1a7d`, 열린 PR0이며 기존 resource0 scaffold 상태다. 하영이 요청을 인지했지만 actual source/full IAM JSON은 아직 저장소로 인계되지 않았다. 값 재채택이나 전체46 재시험을 새 조건으로 붙이지 않는다. 이미 검증된 부분은 재사용하고 아래 필요한 source만 구체화한다.

| 책임·범위 | 다음 source/readback |
|---|---|
| #35 중앙 backend bootstrap | exact bucket의 fresh owner/지역/충돌 확인 → reviewed desired source로 SSE-S3 AES256·Versioning Enabled·PAB4·BucketOwnerEnforced·TLS/PR145 정책 → before/after bytes/구조·설정 readback → 비밀 없는 fixture·lock/version 및 지정 root 복구 시험. 부재는 자동 create 승인이 아니며 이름 충돌/예상 밖 기존자원은 덮어쓰지 않음 |
| #35 중앙 Relay identity bootstrap | FDS-Relay-SSM role/profile path `/`, EC2 service trust, 결정된 Agent 정책 source/version/hash와 실제 profile role 연결 readback. IAM role 생성·Agent attach는 사람 work-role grant와 구분. 광역 관리형 정책을 사람 계정에 복사하지 않음 |
| #35 일반 IaC 역할 | 권욱·하영의 기존 trust/개인 AssumeRole 후보를 연결하고 실제 component/resource/API/dependent-action/full permissions JSON을 backend·PassRole fragment와 합성. 이번28-case fragment만 붙여 Terraform 구축 가능이라고 하지 않음 |
| #35 actual Stage-A | 승인 profile data 참조·exact PassRole·각 component 자원 소유권, user_data/PSK 비밀 제외, EBS 실제 key/정리 경계, Session document source를 reviewed plan/Freeze·비용/cleanup 조건에서 구축하고 actual output/readback 인계 |
| #37 Network 역할 | actual Relay instance/profile/document/Agent/EBS 정보 후 exact ARN bind+role permissions source → 중앙 delta grant/readback → 권욱·재환 각각 본인 MFA U1. user fixture18을 Network 역할 세션 시험으로 대체하지 않음 |

**우선 권고:** 준비 가능한 중앙 backend/Relay identity bootstrap source를 최소 범위로 먼저 연결하고, Stage-A 실제 resource/API/full IAM source를 별도 delta로 이어간다. 미래 ROSA/OIDC 모듈 전체 완성을 기다리거나 광역 EC2/IAM 권한을 먼저 부여하지 않는다. 서명/리뷰 절차는 기존 정책을 따르고 동일 채택 값의 재회신·상시 Support 이중승인을 추가하지 않는다.

코드/실행 정책의 새 source는 정확한 HEAD 독립 리뷰가 필요하다. 이미 승인된 PR145/146의 bytes·AWS validation을 그 범위에서 재사용한다. 이 문서 자체에는 bootstrap/apply 명령이나 새 업무 권한이 없으며 실제 before/desired/readback·복구가 없는 적용을 완료로 기록하지 않는다.

10/8 actual Stage-A→10/12 #37→10/14 G4, 비용 설정 보류·교육장 daily 통제·담당/AC/Freeze 조건은 유지한다. 현재 root capture만으로 이 일정의 actual handoff가 완성됐다고 표시하지 않는다.

## 연결·복구

- [PR146 승인 source](https://github.com/321Team/fds-project-baseline/pull/146), [PR147 배포 기록](https://github.com/321Team/fds-project-baseline/pull/147)
- [Lead 값 채택](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6015740112), [#35 구현 인계 조건](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6015979237), [#37 재결속](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-6014503123)
- [IAM simulator 공식 범위/원문 필드](https://docs.aws.amazon.com/cli/latest/reference/iam/simulate-custom-policy.html)

이 회차는 AWS 변경이 없어 AWS rollback 대상이 없다. 원본 capture·SHA256SUMS·stdout을 보존하고 잘못된 수신 기록은 새 정정 기록으로 보완한다. 실제 bootstrap/grant 원복은 미래 회차의 before snapshot과 정확한 새 부여분으로 정의하며 운영 backend/state 버전/증적/profile을 일괄 삭제하지 않는다.

`ROOT_CAPTURE=COMPLETE_REPORTED / VALIDATE_POLICY=NO_FINDINGS_REPORTED / DELTA=46_PASS_REPORTED / NEGATIVE_RAW_REVIEW=PENDING / BOOTSTRAP=NOT_RUN / ROLE_GRANT=NOT_RUN / USER_RUNTIME=NOT_TESTED / APPLY_READINESS=NOT_ASSESSED`
