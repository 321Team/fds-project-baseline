# #50 B2 장애 패킷 초안 후속 검토

CODEX_ASSISTED. 대상 [이재환 초안6051891259](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6051891259), 2026-10-08 12:58:55 KST. 기존 [PMO/QA 리뷰6051518639](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6051518639) B2의 대응분을 검토했다. 판정: **설계 구체화 진전 / 실행 전 보완 잔여 / Runtime GO 없음**. 실제 target 값이 생성 후에 나오는 것은 정상이며 그 사실만으로 준비안을 반려하지 않는다.

## 수용 가능한 방향

승인 ROSA source→DB5432만 대상으로 하는 별도 forward chain, 기존 firewalld/conntrack 보존, counter·Pod 내부 readyz·Ready/EndpointSlice 동시 관측, engine 원래 replicas/HPA 대조, 제한 시간·복구 후 실제 거래 확인은 기존 요청 방향과 맞다. 원래 ESTABLISHED accept 뒤의 단순 규칙 추가 문제를 분리 체인으로 보완했다.

공식 [nftables 설명](https://netfilter.org/projects/nftables/manpage.html)의 규칙상 다른 base chain의 accept가 뒤의 drop/reject를 무효화하지 않는다. 다만 이는 설계 근거이며 실제 패킷이 지정 경로/규칙에 도달하는지와 기존 세션에 장애가 전달됐는지는 counter·대상 앱 실패로 관측해야 한다. 이번 nft 명령 실행이나 Linux packet 시험은 없다.

## 실행 차단 잔여 F1 — 제한 시간과 복구를 하나의 절차로 결속

근거: 초안 F-D는 `F×P+T+20`초 관측 후 60초 유지, 규칙 존재 최대5분, 삭제 후3분 정상복귀 확인, 삭제 후10분 미회복 시 restart, 기존15분 중단을 함께 사용하지만 기산점·복구 실패 시 종료 순서가 완결되지 않았다. 예를 들어 관측 한도가240초를 넘는 live probe 설정이면 60초 유지와 5분 규칙 상한을 동시에 충족할 수 없다. 이는 실제 설정값에 대한 주장이 아닌 경계조건이다.

**영향/기존 조건:** #50 B2의 한정 주입·중단/복구 조건을 실행자가 일관되게 따를 수 없다. shell/세션 종료 또는 삭제 오류 시 잔존 규칙 처리도 필요하다.

**보완:** 주입 시작 t0·관측/유지 종료·삭제 시도·삭제 확인·기존15분 중단 기산점을 하나의 시간표로 제출한다. 300초 hard limit이 관측/유지보다 우선하도록 하고, 충분한 제거 여유가 없으면 주입 전에 중단한다. 주입/관측/제거 명령 자체의 timeout, 오류/세션 유실 시 담당자가 독립 관리 경로로 자기 시험 테이블만 제거·재조회하는 분기를 명시한다. 기존 테이블 발견 시 합치거나 삭제하지 말고 STOP한다. 이름만으로 소유가 불명확한 잔존 테이블을 무조건 삭제하지 않는다.

F-E도 0개 유지5분·복구10분의 기산점과 복구 원래값/HPA 통제를 연결한다. `rollout restart`는 초안의 '사전 승인된' 문구만으로 이번에 승인된 것이 아니다. 기존 승인 근거·정확한 대상/회차·영향을 실행 입력에 연결하고 없으면 자동 실행 분기에서 제외한다.

**완료조건:** 실제 P/T/F와 작업창을 대입한 시간표, 정상·관측 timeout·규칙 삭제 실패·관리 세션 유실의 대응, 정리 readback·원본 보존 방법을 제출한다. 새 자동 원복 코드를 쓰면 해당 코드 리뷰를 적용한다. 기존 제한을 임의 확대하거나 공유 DB를 중지할 필요는 없다.

## 실행 차단 잔여 F2 — 독립 복구 경로·timeout을 실측 입력과 연결

근거: 초안은 'oc는 터널과 무관', 'reset이면 즉시503'으로 단정한다. #34/#38/#40 관리 API 모드/route는 아직 미결이고, 실제 기준 앱 `adc90410`의 [db.py](https://github.com/321Team/fds-msa/blob/adc90410f99cb7af5b40bc8ff92c45272e9f8bee/transaction-api/app/db.py)는 pool_pre_ping을 사용하되 별도 command timeout을 지정하지 않는다. [readyz](https://github.com/321Team/fds-msa/blob/adc90410f99cb7af5b40bc8ff92c45272e9f8bee/transaction-api/app/main.py)는 DB 예외가 반환된 뒤503을 낸다.

[asyncpg 공식 API](https://magicstack.github.io/asyncpg/current/api/index.html)는 connection timeout과 command_timeout을 구분한다. 따라서 DROP의 모든 DB 작업이60초로 끝나거나 REJECT 뒤 앱/EndpointSlice가 즉시 바뀐다는 보장은 없다. 연결 풀 대기·DB 작업·readiness probe·관측 요청 시간을 구분해야 한다.

**영향/기존 조건:** 복구 접근이 장애 경로에 묶여 있거나 관측 호출이 오래 걸리면 #50의 제한시간·복구 조건을 지키지 못할 수 있다.

**보완/완료조건:** 실행 직전 SSM과 ROSA API의 실제 endpoint·DNS/route/권한·도달성과 장애 범위 외 경로를 기록한다. 열어 둔 세션만으로 독립 경로를 입증하지 않는다. 실제 source 집합·hook·rule readback을 결속하고 counter, Pod 내부503, Pod Ready=false, 해당 EndpointSlice ready=false의 **4항목**을 모두 관측한다. 관측 명령은 자체 제한시간을 가지며 timeout/Router503을 성공으로 바꾸지 않는다. actual image의 DB timeout·Probe P/T/F를 실행본에 명시하고 불일치 시 원복/INCONCLUSIVE로 끝낸다. 관측 편의를 위해 보안 통제나 앱 timeout을 임의 변경하지 않는다.

여기서 독립은 **해당 장애 범위로부터의 독립**이다. F-D의 DB5432 차단과 F-E의 engine scale에 영향받지 않는 관리 경로면 되며 물리적 별도 VPN/새 관리망을 요구하지 않는다. 같은 터널을 쓰더라도 이 한정 규칙에 매칭되지 않고 복구 접근이 유지됨을 확인할 수 있다. A7 터널 단절의 관리 경로는 A7의 기존 별도 계약으로 확인한다.

## 비차단 정리와 유지할 잔여

- 초안의 '세 가지'를 표의4항목과 맞춘다. F-D는 DB 접근불가, F-E는 engine 부재이며 #43 D-03의 engine read timeout/오류 응답/DB 저장 rollback 시험을 각각 대체하지 않는다.
- 14:50 KST 수신 갱신: #50 B1 도구는 MSA PR24 R1~R4 해소·독립 APPROVED·merge `6a95e1a5` 완료. [생산자 기록](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6053198464)을 수신했다. B2 F1/F2는 별도 잔여이며 코드 승인이 실제 장애 실행을 허용하지 않는다.
- A7 1회 원본 재사용·한 번에 한 장애·최소 source 범위·P1 DB 별도 이관 창 원칙을 유지한다. F1/F2는 생성 전 전체 프로젝트 차단이 아니라 해당 장애 실행의 필수 준비다.
- 실제 규칙/대상 값과 복구 절차를 수신하면 이 보완분만 재검토한다. 동일 소스의 완료된 시험·과거 리뷰를 근거 없이 반복하지 않는다.
