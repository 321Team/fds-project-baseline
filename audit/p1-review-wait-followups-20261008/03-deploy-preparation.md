# 3. Deploy 실행·복구 입력 묶음

CODEX_ASSISTED. [CICD PR66](https://github.com/321Team/infra-cicd/pull/66)의 Session과
[PR67](https://github.com/321Team/infra-cicd/pull/67)의 Workflow/broker를 재사용한다.
현재 PR67은 PR66 기반이므로 66 검토/병합 후 67의 최종 diff·SHA·CI를 확인해야 한다.
이 문서는 새 승인이나 실행용 plan/approval 생성기가 아니다.

## 실제 준비한 것

[deploy-input-worksheet.json](deploy-input-worksheet.json)은 실제 deploy_plan.py의 필드 집합을 추출한 계획표다.
운영의 P1-CICD-deploy-inputs-1 schema가 아니므로 Workflow에 공급하지 않는다.
Build Run37642123031/attempt1, APP adc90410, 로컬 이미지2개는 확인된 값이고,
Push·원격 digest·대상 UID·이전 이미지·승인·창은 null로 남겼다.

| 실행 입력 | 지금 근거/생산 책임 | 완료조건 |
|---|---|---|
| workflow.repository/ref/workflow_sha | CICD 병합된 main | 최종 검토·병합 SHA 및 dispatch 실행 문맥 일치. 현재 후보 SHA를 미래 main으로 기입하지 않음 |
| delivery + push_execution + push_receipt_sha256 | 새 Push 회차 / 이권욱 | 새 Run·receipt 원문·원격 digest 결속. Build Run을 Push Run으로 재사용하지 않음 |
| kubernetes 5필드 | 기존 SEC TokenRequest 정책 및 CICD 소비 | API·SA·audience·TTL·정책 reference 일치. 새 RBAC/토큰값을 만들지 않음 |
| targets 서비스별5필드 | 실행 직전 CP1의 최신 대상 + APP 복구 입력 | namespace/deployment/container/UID/previous_image 고정. UID 변경 시 재계획 |
| 이전 이미지 보존/Pull·APP/DB 호환 | APP/K8S/HBR 각 생산 범위, CICD 소비 | 실제 롤백 가능한 digest 및 데이터 호환성 근거. 이전 image 문자열만으로 충족 아님 |
| approval 원문/plan hash/window/allow_rollback | CICD 책임 Lead의 현재 issue11 기록 | 실제 승인 원문과 현재 GitHub 조회 일치. 이미 만료/소비된 승인 금지 |
| sa_uid·CA·SSH·source bundle | 기존 승인된 CP1/ansible01/Runner 경로 | 최신 UID/CA/소스 hash와 Run/record/plan 결속. 키/토큰 내용 비노출 |
| 작업창·관측/중단 책임 | 현장 조율 기록 | Edge/Harbor/SEC 작업과 실제 비중첩, 종료·복구 상한 확정 |

## 리뷰 이후 실행 순서

1. 최종 main/source·이 문서 입력을 고정하고 정상 Runner 계정/기존 SSH 접근을 읽기 전용으로 확인.
2. 새 private0700 입력 폴더/0600 record에 실제 plan·승인·Push receipt UTF-8 원문과 SA UID를 묶고 외부 record SHA256 고정.
3. 기본 execute=false의 정상 판정은 SUPPLIED_BYTES_MATCH / TOKEN_ISSUED=false / DEPLOY=NOT_EXECUTED.
   입력 미완료인 현재는 이 실제 경로를 dispatch하지 않는다.
4. 별도 승인된 새 Run/attempt1 execute=true에서 issue11 fresh 승인 조회 뒤 소켓 대기.
5. ansible01 broker가 binding/소스/SA·기존 경로를 대조하고, 발급 전 유효 창을 확인한 후 한 회차만 전달.
6. broker 수신 확인과 Workflow rollout 성공을 구분하고 result/journal/claim·최종 대상 상태를 보존.
7. 실제 앱 Health/E2E, Harbor→Manifest→Pod 4/4 및 rollback 증적은 별도 완료조건으로 확인.

정확한 실행 명령과 기존 경로는 [고정 PR67 runbook](https://github.com/321Team/infra-cicd/blob/258952bb57d0e9eb91a66132136273a6f73876b5/docs/deploy-workflow-handoff.md)을 사용한다.
독립된 새 절차로 복제하지 않는다. sudo/SSH 인증은 정상 계정의 기존 경로에서만 수행한다.

## 실패·복구 책임

승인 철회/만료·UID/hash drift·401/403·timeout·부분 rollout·전달 실패 시 자동 rerun/재발급하지 않는다.
broker 실패만으로 미배포를 단정하지 않고 해당 Run/result/영속 claim과 현재 Deployment를 조회한다.
allow_rollback과 살아 있는 인증 범위 안에서만 이전 digest로 복구하며, 불명확하면 추가 변경 없이 담당자에게 상태를 전달한다.
claim 삭제, 공용 자격증명/홈 초기화, cluster-admin 공급은 복구안이 아니다.
복구 실행도 source/명령/rc/시각/이전·이후 UID/image/health·잔여를 기록한다.

현 단계: INPUT_WORKSHEET=PREPARED / TOKENREQUEST=PUSH=DEPLOY=ROLLBACK=NOT_RUN / DELIVERY_GATE=NOT_VERIFIED.
