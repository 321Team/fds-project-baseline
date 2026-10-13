# Phase 1 최종 APP·HA 실행 준비 카드

이권욱 / CODEX_ASSISTED · 2026-10-13 05:13 KST 읽기 기준. 준비안이며 새 Deploy·DB 쓰기·drain·재부팅·Probe 장애 허용서가 아니다. [기존 V07/V08](MINIMUM_VALIDATION.md)의 기준과 기존 인수 결정을 유지한다. Harbor manager/H6 구현은 별도 채팅 소유다.

## 1. 권장 순서와 이번에 줄인 공백

**승인된 Push → 해당 receipt로 별도 허용된 Deploy/복귀 → 최종 형상 확인 → 필요한 단일 Worker HA → 배치·서비스 회복 → 최종 APP 회귀** 순서를 권한다. Probe 장애는 필요한 미입증 사례만 별도 범위로 정하며 정상 회귀 중간에 끼우지 않는다. 같은 초기 형상으로 HA·회귀를 먼저 돌리고 새 이미지에서 반복하지 않는다.09:00 병행 준비 종료와 Push10:00 시작한도/12:00 종료창은 별개다.

| 항목 | 확인한 사실 | 남은 실제 조건 |
|---|---|---|
| 도구 | [APP PR30](https://github.com/321Team/fds-msa/pull/30)의 `rg.py`, [K8S PR50](https://github.com/321Team/infra-kubernetes/pull/50)의 probe/judge 고정 bytes 확보 | 공급 위치·현장 해시·Python·새 결과 경로 확인. 코드 변경 없이 기존 독립 리뷰/CI 재사용 |
| 앱 형상 |05:13 두 Deployment spec·template가00:34 관측과 동일. 각 Ready3, 분산 제약 `DoNotSchedule/maxSkew1/nodeTaintsPolicy Honor/matchLabelKeys pod-template-hash` | 새 Deploy 뒤 exact digest·UID/spec·Pod/imageID와 실제 분산을 다시 결속 |
| 경로 | `transaction-api-nodeport`30080/Local, ready·serving endpoint가 Worker01/02/03에 각1, HPA0 | 실제 edge 경로·HTTP·시간 동기 상태는 해당 회차 직전 확인 |
| 과거 HA | [증적92](https://github.com/321Team/fds-project-evidence/pull/92)의10/2 worker02, 같은 구 이미지, GET 범위 PASS | 이후 [K8S PR65](https://github.com/321Team/infra-kubernetes/pull/65) 분산 제약이 추가돼 스케줄링 영향이 있음. 과거 시험을 무효화하지 않고 새 형상 영향만 확인 |
| 복귀 | uncordon은 신규 스케줄링을 허용할 뿐 기존 Pod를1/1/1로 옮기지 않음 | 회차 허용에 필요 시 앱당1개·총2개 정상 Eviction의 조건부 배치 복구를 포함하는 안. 실제 대상 UID는 fresh 조회; 과거 새벽4개 허용을 재사용하지 않음 |

05:01 수집기의 `pod_spec`은 `topologySpreadConstraints`를 포함하지 않았다. 그 필드가 출력에 없다는 이유로 분산 규칙이 없다고 해석하지 않는다.05:13 보완 GET6건은 해당 누락·Service/EndpointSlice/HPA만 좁혀 수집했다. [원본·receipt](https://github.com/321Team/fds-project-evidence/blob/539d02fbbaf425d12e09827e46038f8fbce30640/records/p1-app-ha-inputs-20261013.md)는 PR208에 추가했다. 메타데이터 Ready는 실제 HTTP 성공이 아니다.

## 2. 공급물과 기준 고정

[공급 manifest](APP_HA_SUPPLY_20261013.json)는 저장소·고정 ref·Git blob·SHA-256·대조한 main을 가진다. 준비한 tar는 **30,720bytes/5members**, SHA256 `863fb9b07b4e88969efee68a7d2e584ad855f5e9d0020e85cd0a0d4b900034b7`이다. 로컬 전달물이며 서버 배치0. 묶음에는 P1 도구3개·manifest·SHA256SUMS만 있다.

| 파일 | 실제 SHA-256 | 역할 |
|---|---|---|
| `rg.py` | `f5dee1069ab96838355cf6269dd6cdff2a08107e880594c5dad98d20424594ed` | APP 요청·판정·DB 대조 |
| `ha-probe.py` | `e2603769cacef36dab6231052104f29f413b105a78d771b4e4c3db3c0a599804` | 기존 `probe.py`와 bytes 동일, 파일명만 구분 |
| `ha-judge.py` | `79f54c955991dacd0767885b0db5001fad39080ea7cf4b7c2a3ea13c6f1a6aad` | 기존 `judge.py`와 bytes 동일 |

APP 도구 ref `61fbf0bf1ace1fa3a5eb983c002de2a0ddac856a`는 조회 main `6e7acf1053b1e44164d38851e477a2d2d64b9c3a`의 해당 파일과 동일하다. 최신 main의 별도 Phase2 도구·계약은 이번 공급에 넣지 않았다. APP **이미지 후보 source** `affbc69beef9967f7977d09a6fec14f7fb6c0e94`·빌드 공급 source `8eac4c982076e3c219840a13686b15c46879981f`는 도구 ref와 다르며 자동 교체하지 않는다.

과거 [E2E68 기준](https://github.com/321Team/fds-project-evidence/blob/435ab3aeb9944cec9ba5b6b40c1819f8477b8b9a/evidence/P1-E2E-01/received-20260929T0400Z/edge01/criteria.txt) SHA `8aad7cc215137b97168230926d0e9655eba4dd3386944bf6efc06bfc83aae8d8`을 재사용한다. 새 `rg.py`는 RUN·도구 SHA가 들어간 새 criteria를 생성하므로 그 파일이 과거 기준 SHA와 같아야 한다고 요구하지 않는다. 기대값/기준의 출처와 새 회차의 파일 hash를 각각 기록한다.

## 3. 실행 입력 — 한 번에 채울 것

| 입력 | 상태 / 실제 채울 값 |
|---|---|
| 새 Push receipt와 final image digest2개 | 미생성. 이전 TBS manifest를 성공 Push receipt로 바꾸지 않음 |
| Deploy 결과·복귀 | 새 회차 미실행. exact Deployment/Pod/imageID·허용 복귀 digest·예산·console를 Deploy 카드에서 인계 |
| 작업 구간·동시 변경 배제 | 미확정. Harbor 변경/후관측 및 다른 앱·DB writer·MON 변경과 비중첩 |
| 요청·수집 접근 | edge01 기존 server08, db01 기존 server08, control01 기존 정상 경로. 역사상 계정이 현재 sudo/DB/MON 접근 성공을 보장하지 않음 |
| 현장 인수 | 이권욱 실행/console; 이재환 기존 HA/E2E 기준·DB/MON 수집 경로 확인, 이하영 기존 정책·격리 경계. 겸임 가능, 새 공통 Lead GO를 만들지 않음 |
| 새 경로 | edge01의 새 공급/결과 경로, control01 타임라인·원본, db01 SQL/rc·원본. 미확정 이름을 실행값으로 쓰지 않음 |
| DB 사전 0행·RUN | 아래 §5의 범위 선조회와 실제 생성 RUN 결속. 같은 RUN 재전송 금지 |
| HA 변경 범위 | 최종 형상에서 **worker02 1대, fds-app 앱만** cordon/drain/uncordon; 필요 시 종료 배치 복구 Eviction 각1개·총2개를 포함하는 구체안. 아직 허용받지 않음 |

기존 인계자에게 반복 자료 작성·전체 코드 재리뷰를 요구하지 않는다. 값 미확정인 창·접근·복귀점만 채우면 별도 Runtime 범위를 구체적으로 검토할 수 있다. 새 SA/RBAC/Token은 이 HA/APP 도구 자체의 필수 조건이 아니다.

## 4. 조건부 HA 회차

기존 [#22 결정안](https://github.com/321Team/fds-project-baseline/issues/22#issuecomment-5887966702)의 수치를 유지한다. 추천 대상은 과거와 같은 **worker02(.107)**다.05:01 PVC Pod0이며 Worker03의 MON local PV3개와 control01의 기존 제한을 피한다. 이것만으로 노드 변경이 허용되거나 영향이 없다고 단정하지 않는다.

1. fresh cluster/node/Deployment·Pod UID/spec/digest, PDB/HPA, taint/toleration·spread, 자원 여유, 최종 이미지 cache, Local ready endpoint각1을 기록한다. 두 앱3Ready·Worker별1/1/1, 다른 변경0, console 가능, edge01/control01 시각 오차 각각≤0.25초가 필요하다. 값 불일치면 변경을 시작하지 않는다.
2. edge01에서 hash 대조한 기존 probe를 새 결과 경로로 실행한다.0.5초 tick,3Worker 동시 GET `/readyz`, 연결1초/전체2초. **능동 요청 부하**는 초당6건이며 순수 metadata 읽기와 구분한다. 전체 probe 길이는 아래 모든 단계 상한+관측 여유를 덮도록 회차에서 고정한다. 과거480초를 긴 실패 경로에도 충분한 값으로 자동 복제하지 않는다.
3. 기준선≥60초 모두200을 확인한 뒤 control01에서 exact worker02·앱 selector drain1회. 기존 `--timeout=180s`를 다음 변경 중단 한도로 유지한다. 종료코드와 원본·`drain_start`를 남긴다. `--force`, 전체노드 앱 외 퇴거, 무조건 Pod delete로 실패를 우회하지 않는다.
4. 두 Deployment Ready3, 대상 node의 해당 Pod0이 될 때 `rescheduled_ready`; 이후≥60초→uncordon→≥60초→end. Ready 대기와 probe 관측의 종료 한도를 함께 정한다. 틱 누락·probe 조기 종료·시각 불충족이면 **NOT_VERIFIED**, 결과를 꾸미기 위해 timeline을 고치지 않는다.
5. 기존 judge의 A=정상 두 Worker 비200 **0건**, B=전체 성공응답 최대 간격 **≤1초**, 누락 tick0·발사 지연≤0.2초·기준선200을 그대로 사용한다. target Worker의000/503은 Local 동작으로 별도 기록한다. GET 가용성 결과를 업무 POST/DB 무손실로 확대하지 않는다.
6. uncordon 뒤 자동 재분산을 가정하지 않는다. 판정 구간 밖에서 실제2/0/1 등 배치를 보고, 허용한 경우에만 초과 배치된 같은 RS의 Pod를 **engine1개→회복→API1개** 순서로 fresh UID/RV 조건 Eviction한다. 기존 [새벽 분산 복구](https://github.com/321Team/fds-project-evidence/pull/208)의120초 Ready·90초 MON·30초 안정 확인 방식을 소비한다.2개로1/1/1이 되지 않으면 추가 반복하지 않고 잔여 배치를 인수한다.
7. 실패·timeout·SSH 단절 시 다음 퇴거를 멈추고 console에서 해당 노드의 cordon 여부·이미 접수된 퇴거·대체 Pod를 확인한다. 이 회차가 cordon한 worker02를 uncordon하고 rc/readback을 남긴다. Pod UID는 되살릴 수 없으며 기존 RS의 재생성을 관측한다. 정책 완화·image 변경·강제삭제는 자동 복귀에 넣지 않는다. 서비스 회복 전 APP 거래 회귀를 시작하지 않는다.

새벽에 성공한4개 Eviction은 이 새 회차의 허용이나 HA 성공 증거가 아니다. 재부팅도 이 drain 회차에 포함하지 않는다.

## 5. 최종 APP 회귀 — 도구 변경 없이 RUN 결속

`rg.py run` CLI는 시작할 때 KST 분 단위 RUN을 생성한다. **사전 DB 조회 분과 실행 분이 달라지면** 조회0행을 실제 RUN의 사전0행으로 주장할 수 없다. 이를 해결하려고 도구를 새로 수정하는 대신, 짧게 확정한 실행창의 모든 RUN 후보를 사전 조회하고 해당 범위0행·다른 작성자 배제를 확인하는 방식을 권한다.

- 예: 고정 창의 `run_first`/`run_last`는 둘 다12자리 KST `yyyymmddHHMM`, 같은 날짜05:00 이후여야 한다. db01에서 [조회 템플릿](APP_REGRESSION_QUERIES_20261013.sql)의 사전 COUNT가0인지 확인한다. 작업자가 다른 RUN을 만들지 않도록 배제하고, edge01에서 창 안의 시각에 1회 실행한다. `meta.json.run`이 조회 범위 안에 있는지 실제 결과와 대조한다. 시각/범위가 바뀌면 전송 전에 조회를 새로 하며, 이미 보낸 회차는 같은 RUN으로 다시 보내지 않는다.
- 사전 결과가0이 아니거나 범위를 고정할 수 없으면 중단한다. 기존 데이터를 DELETE하거나 출력만 바꿔0으로 만들지 않는다. 과거에는 없던 시험 결과를 합성하지 않는다.
- SQL 템플릿은 기존8열 조회의 prefix를 literal 비교로 좁힌 것이다. SQL 문법/권한을 실제 DB에서 실행한 검증은 아직 없다. DB 기존 접속 경로를 확인한 뒤 읽기만 먼저 한다. secret 값을 명령·원본·PR에 넣지 않는다.

순서:

1. 최종 digest/Pod별 imageID·Ready/재시작·Local endpoint·업무 metrics404/전용 scrape200·현재 MON 대상 집합과 사전 metrics6개 query를 수집한다. 최종 Pod가 교체되거나 다른 writer가 섞이면 단순 합계 차이로 회차를 판정하지 않는다.
2. db01 사전0행 → edge01 `python3 rg.py run <새 OUT_DIR>` **1회**, 즉시 rc 보존. 기존 도구가 사전 Worker3 `/readyz`200 확인 후25요청(24판정+I01)을 전송한다. HTTP5xx/연결실패는 남은 전송 중단이며 자동 재시도0회다. 도구가 모든 의미상 FAIL에 즉시 전송을 중단한다고 과장하지 않는다.
3. 실제 생성 RUN과 범위·도구/기준 hash를 확인한다. db01에서 같은 RUN의8열 결과·시각·rc를 수집하고 `python3 rg.py crosscheck <OUT_DIR> <DB_LOG>`를 수행한다. API24 PASS만으로 DB·metrics 전체 인수를 완료하지 않는다.
4. 사후 metrics/Pod·MON·업무 비노출·관련 N08 원본을 연결한다. 유효22건 저장/평가와 Rule각1회, N06/N07 HTTP422. I01이201이면 save/evaluated+23·DB23행,422이면+22·22행. I01 시각/Rule/DB 저장은 INFO로 구분한다. save_failure·missing_client_ip 증가0, restart 변화0을 기존 기준대로 확인한다.
5. 경로는 edge01→3Worker NodePort 직접이다. 현재 Client→edge upstream 관측과 별도 연결하며, 직접 경로의 성공을 모든 Client/LB 경로 성공으로 바꾸지 않는다. 기존6개 PromQL은 템플릿 하단에 보존했다.
6. 실패하면 후속 승격 중단·불확정 응답/Transaction ID·DB행·metrics·rc를 보존한다. 기능 시험 거래는 [기존 보존 결정](https://github.com/321Team/fds-project-baseline/issues/11#issuecomment-5887795557)을 유지한다. image 복귀는 별도 허용한 Deploy 경로만 사용한다. 구 image 복귀 시 업무 metrics 노출이 돌아오는 보안 잔여도 기록한다.

HTTP readiness 실패→Endpoint 제외/복귀와 liveness 실패→**동일 Pod UID의 container restart**는 각각 다른 증거다. 이번 정상 회귀·drain·rollout을 그 장애 성공으로 계산하지 않는다. [기존 DB/FDS 장애 성공 재사용과 실제 engine HTTP 최소 후속](HTTP_PROBE_REUSE_20261013.md)을 별도로 대조했다. 필요한 추가 Probe 사례의 대상·주입·관측·회수는 별도 구체화 대상이며 MON 단일 replica/local PV에 시험을 확대하지 않는다. Probe 회차를 선택하면 HA와 별도 구간에 두고, 모두 회복된 뒤 최종 거래 회귀를 수행한다.

## 6. 이번 검증 / 남은 단계

이번 수행은 API GET6 rc0, 명령·계정·시각·소스/출력 hash 및 투영 metadata 보존, 도구3개 Git blob/current bytes 대조·AST·tar5members/bytes 검증이다. 소스 독립 REVIEW=NOT_PERFORMED(Pre-check)인 metadata 수집을 리뷰된 실행기로 표시하지 않는다. 기존 도구 코드는 변경하지 않았고 완료한 MOCK/CI를 다시 돌리지 않았다.

RUNTIME 쓰기·서버 공급·Token·DB 거래·HA·reboot·Probe fault는 모두 이번 준비에서0회. 코드/증적의 과거 유효한 승인과 새 실행 승인·실제 결과·AC 최종 인수를 구분한다. reviewer에게 필요한 것은 현재 관측의 해석과 위 최소 실행/회수 범위 확인이며, 새 공통 Lead GO나 전체 Phase1 재승인이 아니다.
