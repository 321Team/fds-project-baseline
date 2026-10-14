# APP/E2E 최종 인수안 — D03 후속

2026-10-15 KST · CODEX_ASSISTED. 생산·업무 Lead 이재환, 통합 검토 이권욱. [#15](https://github.com/321Team/fds-project-baseline/issues/15), [#20](https://github.com/321Team/fds-project-baseline/issues/20), [#30](https://github.com/321Team/fds-project-baseline/issues/30)의 기존 AC·담당·일정·상태를 유지한다. 아래는 처분 후보이며 새 최종 승인 또는 면제가 아니다.

**후속 구체화:** [D02·D04·I01 변경 영향과 처분안](D02_D04_I01.md). 실제 Backup/네트워크 증적 재사용은 [MON·SEC 잔여안](RESIDUAL_MON_SEC.md)에 연결한다. I01은 UTC Z 입력 후보와9개 오프라인 소스 사례, R01/R07 이력 영향까지 분석했으며 새 Runtime·계약 승인으로 표시하지 않는다.

## 1. 이번 대조에서 바뀐 부분

- 기능회귀224: 24 PASS/0 FAIL/1 INFO, HTTP201 23건과 DB23행 거래별 대조. 병합 `89f9d4cbd3ff77aa6fc70cfe3de34a71ffb09758`.
- 이미지 전환 후 축약부하228: 20rps2분+50rps2분, 8,400건201·DB8,400행·저장/평가 카운터 일치. 병합 `ee4a9a25212dc5b7eb76c1125f4368d68026ff0a`. 기존 §8 충족을 유지하며 다시 미실행으로 표기하지 않는다.
- D03: [PR233](https://github.com/321Team/fds-project-evidence/pull/233) HEAD `fc5714488453bc28eba6d0a676a75728649a1d1e`에 실제 격리 회차 결과가 제출됐다. **LAB_RUNTIME_PASS / 독립 증적 편입 대기**이며 운영 전체 E2E/최종 인수는 아니다.
- DB#11·DR#21은 최신 조회 CLOSED(completed)다. APP/E2E 잔여 때문에 이미 수용된 DB·DR 시험을 다시 열지 않는다.

## 2. D03 요구→실제 결과→한계

| 경로 | RUN202610150030 결과 | 이번 연결 |
|---|---|---|
| engine read timeout | 2.017526초, API201·null/null·skipped=true·DB저장1, evalerror 증가 | 기존 ‘미검증’에서 격리 실측 제출로 갱신 |
| engine HTTP500 | API201·null/null·skipped=true·DB저장1, evalerror 증가 | HTTP 오류 응답의 fail-open 근거 |
| DB INSERT 실패 | API500·저장0·save_failure 증가, marker PID84 뒤 동일 PID ROLLBACK | DB 오류·롤백 근거 |
| 오류 뒤 정상 회복 | 각 정상201/저장1, 총7POST·고유6행·save6/fail1/evalerror2 | 세 실패 직후 회복과 전체 집계 연결 |
| 정리 | 정확4컨테이너·임시env2 부재, claim/원본 보존, 00:30:47 재조회 후 Runner 사용 종료 | 새 Runtime·자동재실행 없이 편입 단계로 이동 |

호스트 cicd-runner01/rootless Podman, 실제 10/15 00:30:11~32 KST, 앱 PR36 병합본 `6531b51c991535794c1f9705dc14f199001d1961`. PG16.8/운영16.14 차이·DB 새 scan 미수행·운영 K8S/TLS 제외·고정 occurred_at=당일12:00/실제 수신00:30 차이를 유지한다. 야간 Rule 증거로 사용하지 않는다. 실행 원본을 이번 문서에서 생성하거나 수정하지 않았다.

## 3. Defect 처분 후보와 완료조건

[원 Defect/QA 수용 기록](https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-5989190539)과 후속 실제 증적을 사용한다. 새 Severity·Due·위험수용을 자동 확정하지 않는다.

| 항목 | 권고 처분 후보 | 결정 전에 필요한 최소 조건 |
|---|---|---|
| D-01 local endpoint | 검증 회차의 해소 근거 유지 | Deploy219·HA221·Probe223·회귀224의 Worker별 배치 연결. 미래 재분산 보장으로 확대 금지 |
| D-02 감시·통보 | MON의 알려진 감시 한계와 최종 처분에 연결 | cluster IF05C Discord 수신과 monitor01 IF24 부재·worker03 장애영역을 구분. MON Lead가 영향·대응/복구·잔여 인수안을 명시; 새 외부 통보 구축을 자동 추가하지 않음 |
| D-03 실패 경로 | 격리 Runtime 충족 근거 제출, 편입 이후 해당 범위 수용 검토 | PR233 동일 HEAD 독립 편입 결과→기존 기능/부하/보안 근거와 연결. 환경 차이가 인수에 미치는 영향 명시. 반복 시험을 기본조건으로 삼지 않음 |
| D-04 Client→edge | 기존 경로 실증과 최신 앱 회귀의 결합 재사용 우선 | 169의 PC→edge POST201/DB1행과 224·228 NodePort 경로를 분리. edge/upstream/source 정책·새 앱 API 계약의 변경 영향이 미포함이면 그 행만 추가 검증안 작성 |
| D-05 DB | 기존 DB 최종 인수·종결 유지 | W4 HTTP5xx NOT_MEASURED, 콘솔 제출 출처, 다른 Namespace 전수 미검증 한계를 삭제하지 않음 |
| D-06 provenance | 최종 앱의 supply→deploy→회귀 결속 재사용 | 217→218→219→224/228의 source/digest를 최종 문서 목록에 고정. 과거 이미지의 미확인 최초 provenance를 소급 확정하지 않음 |
| I01 시간 입력 | 명시적 offset 사용을 클라이언트 계약에 설명하는 후보 우선 | naive 입력의 현재 해석·DB표현·Rule 영향과 기존224 INFO를 보존해 APP Lead 판단. parser 변경·기존 데이터 보정·자동 위험수용은 별도이며 여기서 수행하지 않음 |

## 4. 인수 절차

1. PR233의 최신 HEAD·독립 리뷰·편입 상태를 확인한다. 새로운 변경이 없으면 이미 통과한 제품 시험을 반복하지 않는다.
2. 이재환은 위 D-02/D-04/I01과 D03 환경 차이의 처분·근거를 기존 #15/#20에 남긴다. 담당·기한이 미정인 새 Action은 ‘미정’으로 남겨 확정을 받는다.
3. 이권욱은 Critical0·실패 재현/수정 버전·Regression/Defect 최종 승인 3개 잔여를 실제 판정과 연결한다. 24PASS/0FAIL 또는 부하8,400건 성공만으로 Critical0을 선언하지 않는다.
4. 인수 가능한 행과 미충족/기존 위험수용을 구분해 APP/E2E 결과를 #30·#24에 연결한다. 문서 편입·테스트 성공·업무 인수·Close를 분리한다.

새 변경이 요구되면 변경 파일/고정 SHA·영향 행·필요한 시험만 명시한다. 실행 실패 원본213/230/232와 수정 버전 연결을 보존한다. 새 POST/DB쓰기/부하/rollback은 이번 준비의 실행 범위에 포함하지 않는다.

근거: [기능224](https://github.com/321Team/fds-project-evidence/pull/224), [부하228](https://github.com/321Team/fds-project-evidence/pull/228), [D03 최신 결과](https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-6172099041), [DB 인수](https://github.com/321Team/fds-project-baseline/issues/11#issuecomment-6159292006), [DR 현행](https://github.com/321Team/fds-project-baseline/issues/21).
