# #46/#50 Phase 2 실행 입력·실패·복구 계약 초안

CODEX_ASSISTED. 문서 전용 준비안, 실행 설정/새 코드/실제 시험 결과가 아니다. 기존 [Delivery 준비](../20261007/delivery-preparation.md) 및 [16개 case](../20261007/test-case-draft.tsv)를 확장하며 동일 case를 중복 생성하지 않는다.

10-08 오후 후속: [CICD PR68](https://github.com/321Team/infra-cicd/pull/68) a466370은 오프라인 입력 진단만 구현됐고 독립 리뷰 대기다. 실제 adapter/배포 구현은 여전히 미완료다. [실행 자료16행](test-execution-matrix.tsv)과 [최신 수신·도구/장애 잔여](execution-readiness-update.md)를 함께 사용한다. 업무 시험16case NOT_RUN과 PR68 합성 단위시험16 PASS를 구분한다.

## P2 target adapter 설계

Build/Test/Scan 로직을 복제하지 않고 대상 연결부를 분리한다. source 소비 기준: infra-cicd main `4e9324cd8acf0ba67b35f950b4c952db8064540e`, APP main `adc90410f99cb7af5b40bc8ff92c45272e9f8bee`. PR65/66은 진행 중인 별도 생산 작업이며 이 패킷에서 수정하지 않는다.

| 입력 그룹 | 필드 / 생산자 | 미충족 시 준비/실행 구분 |
|---|---|---|
| 대상 | #38 Cluster identity/API URL/CA reference/context/namespace, 허용 workload/container 목록 | STATIC 설계 가능, live 연결/쓰기 금지. 공용 Lab context를 ROSA로 자동 대체하지 않음 |
| 공급 | #42/#46 source SHA·workflow SHA·run/attempt·Test/Scan·remote digest·provenance | build 성공만으로 remote digest 확정 금지. 검증 실패/미확정이면 Deploy 차단 |
| 배포 원본 | #43 base/overlay repo/path/SHA·rendered hash·approved SecurityContext | 고정 UID 강제/root 예외·임의 manifest 합성 금지 |
| 인증 | #38/#46 credential reference·issuer/audience·TTL/expiry·최소 RBAC·전달/회수 주체 | token/kubeconfig 원문은 문서에 저장하지 않음. 기존 발급 경로 없는 상태에서 새 발급/Secrets 등록 없음 |
| 현재 상태 | 실제 Deployment UID/resourceVersion/container/current image·승인 previous digest | mismatch/기존 상태 불명/expiry 시 STOP. 이전 승인값을 새 대상에 복제하지 않음 |
| 판정 | #43/#50 health/Rule fixture·사전 기대값·DB mode/Schema·evidence path·복구 범위 | health 미정 상태에서 배포 성공 판정 금지 |

실행 시 흐름: 입력/승인 범위 재조회 → source/target/credential/claim 확인 → 제한된 대상 변경 → rollout/health/actual imageID 대조 → receipt/raw → credential 정리. 실패 상태가 불명확하면 임의 재시도/강제 overwrite 대신 실제 API 상태와 claim/checkpoint를 먼저 대조한다. 이 흐름의 P2 CLI/workflow 구현은 아직 없으며 문서만으로 executable adapter가 완성됐다고 표시하지 않는다.

## 기존 16 case를 실행 자료로 완결하는 방법

| case | 지금 준비할 구체 입력 | 성공/실패 판정 및 원본 |
|---|---|---|
| 01~02 | 승인 image·overlay·Lab 대상/자원·Registry reference, arbitrary UID/쓰기 경로 기대값 | admission과 Running/Ready를 구분. uid/SCC/imageID/health·정리 inventory. LAB-PRECHECK 한정 |
| 03 | actual ROSA namespace/Route·두 workload·DB mode·metrics 비노출 검사 | Ready/Route health와 engine/metrics 외부 비노출. 임시 DB 사용을 명시 |
| 04~08 | 승인 fixture repo/path/SHA와 사전 기대값·고유 시험 ID·시각/offset·schema | 정상/R01/R02/R04/R07 각각 API/FDS 결과/DB row 연결. Rule threshold나 metric TransactionID label을 새로 만들지 않음 |
| 09 | 실제 허용 API source/DB port와 비허용 engine/source/port·route/NP/firewall/pg_hba | 양성/음성 별도 원본. 실패를 timeout 하나만으로 정상 DENY라고 단정하지 않음 |
| 10 | 한정 DB 장애·복구·관측 명령/창, 이전 상태 | readyz503/Endpoint 제외·Liveness 재시작 루프 없음, 복구 health/DB 검사 |
| 11 | 한정 engine 장애·복구·동일 fixture | API Ready·HTTP201·fds_evaluation_skipped=true·DB 저장, engine 복구. DB 장애와 기대값 다름 |
| 12 | #37 승인 Tunnel 장애/복구 범위·SA/route snapshot·재개 fixture | network failure와 app failure 분리, 복구 후 동일 E2E. 단순 Tunnel UP은 업무 PASS 아님 |
| 13 | RUN-A: source→Test/Build/Scan/Push→Deploy→health·actual imageID | 각 run/attempt·hash/digest/RC/raw를 연결. 서로 다른 source의 성공을 합성하지 않음 |
| 14 | RUN-B: 기존 허용된 Test 또는 Scan 실패 입력과 배포 전 상태 | 실제 Deploy 미실행 근거와 전후 대상 불변 확인. MOCK 차단을 Runtime PASS로 표시하지 않음 |
| 15 | 승인 previous digest·재pull 경로·복구 범위·health | 실제 previous imageID/health 확인. 코드 롤백으로 DB 데이터가 자동 복구됐다고 표시하지 않음 |
| 16 | #47 exact handoff·최종 source·case 결과·Known Issue | 04~15의 해당 최종 회귀/제한을 고정. 미실행 case를 PASS로 채우지 않음 |

## 원본 수집과 중단

각 회차는 ticket/case·ENV·실행자/대상·KST start/end·source/digest·명령/RC·stdout/stderr·runtime identity·fixture/DB schema·복구 전후·원본 hash와 리뷰 링크를 연결한다. 보존 위치는 기존 evidence 저장소의 해당 ticket 경로이며 template/TSV는 raw evidence가 아니다.

source/target/권한/fixture 불일치, 거래 무결성 오류, 범위 밖 영향·Secret 노출, 복구/정리 실패 시 다음 쓰기를 중단한다. 기존 approved 이전 상태로 복구할 수 있는 범위만 실행한다. 데이터 삭제·schema rollback·다른 환경 변경을 image rollback에 포함하지 않는다.

현재 결과는 16개 모두 기존대로 NOT_RUN. 이 문서에서 실제 credential 발급/Push/Deploy·Lab 생성·장애주입을 실행하지 않았다.
