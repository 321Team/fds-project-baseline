# 기존 증적 재사용과 남은 최소 검증

이권욱 / CODEX_ASSISTED · 2026-10-10 KST. [전체 인계 대응표](README.md)의 S03 및 관련 실행을 구체화한다. 아래는 시험 완료 기록이 아니라 기존 기준에 따른 조건부 실행안/처분안이다. 수신한 원본은 재작성하지 않으며 이미 수용된 시험은 변경 영향이 없으면 반복하지 않는다.

## V01 — K8S 17파일 형상과 복귀

- 연결: H01/H02/S03, [#10 최신 AC](https://github.com/321Team/fds-project-baseline/issues/10), [고정 PLAN][kplan]. 5호스트45개 중 변경17/유지28, control02 제외. control01 audit1개, control03/worker01/worker02/worker03 각4개다.
- 준비: 승인 소스·manifest의 파일별 bytes/해시, H02 목표 root:root·0750·`system_u:object_r:usr_t:s0`·기본 ACL과 **원본의 복귀 metadata**를 별도 기록한다. worker01의 유지5개도 관측 type 차이가 있으나 이번17개에 추가하지 않는다. 전체 xattr 미수집이라는 오래된 문구는 PLAN §8의 열람 가능 목록 수집으로 보완됐으며 실행 직전 상태는 별도다.
- 실제 시작 조건: 정상 계정/sudo·Console 복구 인수, 호스트별 원본/목표/제3의 hash 구분, 일반 파일/link·부모 권한·공간, 실제 수동/예약 호출자 배제, 검토한 부분집합·시간과 원복 예산. fresh0700 백업과 임시 복원에서 bytes/uid/gid/mode/context/ACL 확인 후 교체한다. 현재 이 값들은 미확정이다.
- 순서: 새 staging 대조 → 호스트 한 대의 승인 집합 백업/복원 검증 → 호출 배제 유지 중 집합 교체 → import 없는 구문 검사·17/28/metadata 대조 → 해당 호스트 사용 재개 판단 → 다음 호스트. 원 PLAN의 control01 우선은 후보이며 이번 문서가 자동 실행 선택을 확정하지 않는다.
- 정상: 승인 집합 전체 목표값 일치·유지28 불변·혼합 버전 없음·백업/원복 원본 연결. 파일 정합화만으로 Calico 보호/AC4 전체 PASS를 선언하지 않는다.
- 실패/복귀: drift·새 호출자·부분 교체·시간 부족이면 다음 호스트 중단. 이번에 바꾼 파일만 실제 백업 bytes/복원 가능한 metadata로 복귀하고 검증한다. inode/ctime 동일성을 복귀조건으로 만들지 않는다. 구버전의 알려진 도구 결함은 남으므로 `RESTORED_WITH_KNOWN_TOOL_DEFECT`/해당 도구 사용 보류. 정책 YAML 재적용·서비스 재시작은 파일 복귀 절차에 포함하지 않는다.

## V02 — K8S 별도 미충족 행의 처분 대조

근거: [기존 7건 요청](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-6040248632), [후속 AC4e 수집](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-6063150237), [#19 현행 AC](https://github.com/321Team/fds-project-baseline/issues/19). 날짜·심각도·Known Issue 수용을 여기서 확정하지 않는다.

| 기존 행 | 지금 유지할 근거/차이 | 다음 최소 조치와 판정 경계 |
|---|---|---|
| AC4f 방식B | 증적144 첫 완결 회차의 한정 관측 수용, 중복 회차는 이탈 원본 | 전부 미실행으로 되돌리지 않음. Calico 특정 차단 귀속/전체 AC 인수와 구분 |
| AC4c | OFF 직후 CONNECTED×3/후속 귀속 한계 | 기존 NOT MET 유지. 원인·영향·보완 또는 한계 처분을 #30에 연결; 새 OFF 반복시험 자동 시작 금지 |
| AC4d② | 부팅 직후 연속 보호 미충족, 단순 reboot 정상은 대체 증거 아님 | 유지/부팅 이후 정상·연속 보호를 분리. V06으로 이 공백을 소급 해소하지 않음 |
| AC4e | 5대 미대조는 해소, 실제17개 불일치 확인 | V01의 정확 범위 결과를 연결. 45개 관측/사본 보관만으로 교체 완료 아님 |
| AC4g | 미시험4대 위험수용은 제안 이력 | 유효한 수용자·범위·재검토조건이 없으면 미확정 유지; 대량 재시험/자동 수용 없음 |
| 요구5/T14·T15 | 직접 라우팅 결과≠VXLAN/MTU 전부, UDP 무응답·TCP179 listener 부재≠방화벽 차단 | [기존 Matrix][kmatrix]의 route/캡슐화·도착/차단 원본과 CAPTURE_INVALID/NOT_VERIFIED를 대조. 필요한 출발 권한/관측이 없으면 해당 보완 회차만 보류; 구성 대체 인정은 별도 판단 |
| 요구8 Secret | #19 AC05의 하위 판정 소비 | encryption/control03 rollback/격리 backup 성공, 예방 rotation NOT MET/RISK ACCEPTED를 각각 유지. 별도 전수 복원 시험 추가 없음 |

이 대조로 처분 대상은 식별했지만 새 위험수용 결정은 만들지 않았다. 해당 결정을 실제 채택할 때 영향·근거·담당·완료/재검토조건을 기존 #30 기록에 남긴다.

## V03 — SEC 최소 Matrix

기준은 [#19 최신 AC](https://github.com/321Team/fds-project-baseline/issues/19)와 원 증적이다. 폐기된 집계나 철회 CR126~128을 사용하지 않는다.

| AC | 이미 있는 근거 | 남은 최소 검증/처분 |
|---|---|---|
| 01·03 | PSA 거부·SA can-i 승인 Matrix ACCEPTED | 새 권한/이미지/정책 변경 영향이 없는 범위 재사용. 실제 신규 Token 소비 성공과 구분 |
| 02 | [157](https://github.com/321Team/fds-project-evidence/pull/157) IF03/IF13A 일반Pod·hostNetwork 및 IF05C, [169](https://github.com/321Team/fds-project-evidence/pull/169) edge 회차 | 원 Matrix의 미입증 행과 확정 실패/수용 행을 분리해 기록. Source·정책·실제 목적지 관측 없는 timeout은 PASS 금지. 같은54건을 전부 다시 실행하지 않음 |
| 04 | [144](https://github.com/321Team/fds-project-evidence/pull/144) IF12B6경로·방식B | 특정 HEP/GNP 유일 귀속·OFF 직후·부팅 연속 보호를 V02와 연결. TLS error20/21을 인증/API권한 성공으로 바꾸지 않음 |
| 05 | [152](https://github.com/321Team/fds-project-evidence/pull/152) snapshot 격리 restore/health/정리, 기존 encryption/rollback | Secret 복호화·APP 소비·운영DR 전체는 별도. 필요한 부족 행의 원본/판정만 보완; 기존 예방 rotation 위험수용 유지 |
| 06 | [173](https://github.com/321Team/fds-project-evidence/pull/173) 격리 exec 전이, [177](https://github.com/321Team/fds-project-evidence/pull/177) 실제6종 정의/Ready | 실제 APP HTTP 등 부족한 해당 사례는 V08. 6종 전수 장애 주입·없는 startupProbe를 새 필수조건으로 추가하지 않음 |

새 패킷/장애 회차는 기존 AC의 정확 행·source/destination·기대값·관측 위치·상한·자동 회수·복귀점을 먼저 채운다. 이 표는 그 미확정 행의 Runtime PASS나 실행 허가를 생성하지 않는다. 현재 증적이 부족한 행은 미확인으로 보존하며 합성 결과를 대신 사용하지 않는다.

## V04 — IF06B 8443 gateway 구간 귀속

연결 H04/J05/S03, #14 AC12/15~17·#17 보조통제. [MON42 원안][if06]을 재사용하고 [H04 회신](https://github.com/321Team/fds-project-baseline/pull/160#issuecomment-6083293377)의 gateway 구간 귀속을 적용한다. 특정 nft rule 귀속은 새 필수조건이 아니다. 기존 T2의 monitor01 SYN 도착 조건과 차이를 실행 기록에 명시한다.

- 재사용: 증적122의 `.108` Source·wrong-auth401, 증적151의 gateway 원본. 새401 전수 재시험 없음. 과거 handle606에 counter가 없었으므로 해당 handle이나 counter 차이를 고정 기대값으로 쓰지 않는다.
- 대상: 기존 worker03 송신, mgmt-gw01 양측, monitor01 수신. 정상 계정·sudo/Console·live route/interface/정책·listener·CA·시간 정합·캡처 누락률을 이번 회차에서 확인한다.
- 최소 순서: 원안의 120초 관측/180초 canary 상한은 **제안**으로 유지. 독립 만료 회수·정확 UID 삭제·Console 담당 및 구현 확인 전 canary 생성 금지. 준비 성공 뒤443 CA검증 GET `/` 양성대조1회(승인 live설정404일 때),8443 새 연결1회(상한5초·앱재시도0), 후관측·회수. 이 문서가 도구·canary 구현 완료를 주장하지 않는다.
- 판정: 같은 창의443 양방향 유효, worker 송신·gateway ingress 있음/egress 없음, 필터·drop/관측 누락·route/정책 변경 문제가 없으면 **gateway 구간 소실과 정합**으로 기록. 특정 규칙 DROP 확정과 구별한다. receiver SYN0만으로 PASS 금지.
- STOP/복구: 양성대조 실패·예상 외 연결·Source drift·관측 불능·회수409·시간 초과면 다음 요청 중단. 소유 canary/관측 프로세스만 정상 경로로 회수, 강제 삭제·8443 개방·reload/flush·광범위 프로세스 종료 없음. 정책 불변·기존 remote write/heartbeat 회복을 기록한다.

## V05 — MON 실제 관리 접근과 관측

J04/J05, [#17](https://github.com/321Team/fds-project-baseline/issues/17), [MON 최소안][monplan]. 증적130 PF 성공/회수·175/185 Secret 참조·180 Discord Firing/Resolved·177 Target/Probe 자료를 재사용한다.

현장 전에 정상/비상 principal·승인 단말·기존 RBAC/접근 경로·감사·종료/회수·앱 credential 인적 보유 범위를 확인한다. 이미 모른다고 답한 원 생성자/옛 감사 자료를 다시 요구하지 않는다. 조회 가능 범위로 통제된 사실과 미확인을 나눠 접근 배타성/최종 처분에 연결한다. Secret 값 조회·회전은 이 확인의 대체 작업이 아니다.

필요한 신규 접근 사례만 승인된 단말/비승인 경로·포트·기대 응답·회수 기준으로 고정한다. 새 PF/Token 발급·fault injection은 해당 실제 회차 조건이 채워진 후 수행한다. 기존 listener/권한과 다르거나 정상 모니터링 저하 시 중단·그 회차 소유 리스너/권한만 기존 승인 복귀 절차로 회수한다. Probe 필요분은 V08로 연결한다.

## V06 — ICR reboot 지속성과 OID 입력

H04/J05/S03, [#14](https://github.com/321Team/fds-project-baseline/issues/14), ICR-AC18. Node reboot를 MON 신규 AC로 추가하지 않고 Pod restart·Drain과 구별한다. [OID02 preloaded](https://github.com/321Team/infra-kubernetes/blob/c42ea6cc3ccd197d12993823bed439d40946a54c/docs/change/ICR-D-NET-01-01/OID02_PRELOADED_20261004.md) 경계를 유지하며 control01 drain 금지·OID03 미해결·두 digest의 공급 출처/반입 원본 공백을 자동 해소하지 않는다.

먼저 실제 대상 노드·변경된 정책/부팅 경로·원 정책/복구점·Console·노드별 system image 출처/캐시·local PV/배치 영향을 고정한다. OID 근거가 필요한 재생성/변경 회차는 해당 공백 해소 전 보류한다. 기존6노드 전수 reboot는 요구하지 않는다.

정확 대상이 정해진 회차에서 pre boot ID/정책/Ready/서비스·허용/거부 관측 → 한 노드 reboot → 새 boot ID/Ready·정책 지속성·해당 허용/거부·Target/회복 관측 → 정상 종료 순으로 계획한다. 재부팅 후 정상만으로 부팅 직후 연속 보호(V02 d②)를 입증하지 않는다. 복귀 예산 초과·정책 drift·API/모니터링 손상 시 다음 노드 중단·Console에서 검토된 원 정책 복귀, 결과/실패 원본 보존. 실제 명령·회차 상한은 대상/복구점 입력 확정 후 기존 runbook으로 고정한다.

## V07 — HA 형상 변경 영향과 조건부 최소 재시험

J07/S03, [#22](https://github.com/321Team/fds-project-baseline/issues/22). 증적92의10/2 worker02 1회 `/readyz` GET과 당시 수용된 AC8/8을 보존한다.9/27 NOT_VERIFIED와10/8 철회 Close 요청은 성공/유예 근거가 아니다.

1. 당시와 현행 manifest/digest·replicas·placement/affinity·PDB·local PV·readiness·LB 경로를 대조하고10/7 PR65의 영향 행을 식별한다. 현재 형상은 직접 관측 전 미확정이다.
2. 관측 대상/장애 허용치가 변한 경우 해당 Worker1대 Drain 회차만 준비한다. 허용 오류·관찰 간격·시간은 기존 승인 기준/증적92에서 가져오고 새 수치를 임의 설정하지 않는다. 기존0.5초 tick/표본 한계 유지.
3. pre 정상·비중첩/Console → 정확한 한 Worker drain → 동일 기준의 요청/Ready/placement/metrics → uncordon·배치/서비스 회복 확인. 종료 형상을 고정한 뒤 필요한 Final Regression을 연결한다.
4. 오류 초과·퇴거/스케줄 실패·local PV 위험·기한 초과면 중단하고 그 회차의 정상 복귀 절차를 수행한다. control01 drain이나 정책 완화로 우회하지 않는다.

변경 영향 없음/제한 처분으로 닫으려면 비교 근거와 유효한 결정이 필요하다. 현재 그 결정을 만들어 내지 않았고 무조건 재시험도 지시하지 않았다.

## V08 — APP 최종 회귀와 필요한 HTTP Probe

J02/J05/S01, [#15](https://github.com/321Team/fds-project-baseline/issues/15)/[#20](https://github.com/321Team/fds-project-baseline/issues/20)/SEC06. [병합된 실행 준비](https://github.com/321Team/fds-msa/blob/61fbf0bf1ace1fa3a5eb983c002de2a0ddac856a/docs/p1-final-regression-readiness-20261010.md)를 소비한다. 이번 작업에서 중복 구현하지 않는다.

새 RUN_ID·실제 최종 digest·기존 criteria/fixture·사전 DB0행·HTTP/Rule·DB22행/metrics·KST/UTC·업무 metrics404/전용 scrape200을 연결한다. 신규 도구 bytes와 APP 공급 Source는 별도 pin이다. 과거 원본은 당시 도구/기준을 보존하며 새 도구 통과를 위해 meta/hash를 고치지 않는다.

실제 HTTP readiness/liveness 전이 부족 사례만 AC와 대조한 뒤 선정한다. Ready=false/Endpoint 제외·복귀와 같은 Pod container restart·회복을 구별하며 rollout을 liveness 성공으로 계산하지 않는다. 운영 MON 단일 replica/local PV를 임의 장애 대상으로 고르지 않는다. 실패/관측 불능/DB 오염 우려면 다음 사례 중단, 원본 보존과 정확한 승인 복귀 digest/정리만 수행한다. 이전 image로 복귀하면 업무 metrics 노출도 돌아오는 종료 보안 상태를 함께 기록한다. 구체 회차는 S01 후속 작업에서 준비한다.

## V09 — 과거 원본 공백 처분

J06/S05, [#11](https://github.com/321Team/fds-project-baseline/issues/11). W4 Edge9파일·1,217기록 및 선택 관측의 범위와 미측정 구간을 분리한다. FUP는 기존 생산자/소비 AC·원본 존재·승인 참조 공백별로 연결하며 이미 종료된 DB 접근통제 위험수용을 다시 승인받지 않는다.

기록할 결과: `없는 원본/구간 → 증명할 수 없는 주장 → 기존 유효 부분 근거 → 현재 인수 영향 → 보완 가능/소급 불가 → 결정 필요 사항/기존 수신 티켓`. 새 시험으로 과거 W4 전체5xx0이나 당시 실행 조건을 만들지 않는다. 처분 제안과 실제 수용을 분리한다. 역사자료가 없어도 무관한 개발/현장 준비는 계속한다.

## V10 — Ansible worker02 회차와 운영 엔진

S04, [Ansible9](https://github.com/321Team/infra-ansible/issues/9), [기존 단일 회차](https://github.com/321Team/infra-ansible/issues/9#issuecomment-6078278748). PR76 승인 HEAD `0d58598d8a3ce77ccd7eaa9e1dfba820b0a436ea` 경로와 기존 strict host-key·정상키·become을 재사용한다. PR77 CI/증적197을 실제 worker02 적용으로 집계하지 않는다.

대상 worker02 한 대의 정상 Console·동시 작성자 배제·source/engine·현재 DNS/서비스·기존 제한을 확인한 뒤 새 회차 prepare/외부 snapshot SHA 고정 → check-only/apply → reapply → 실제 새 SSH/이름해석/API·서비스 → 회차 rollback/재관측을 수행할 계획이다. 기존 T0+30분 유한 예산 및15분 apply 유효조건은 실행 전에 최신 runbook/해당 입력과 확인한다. source 변경 시 그 영향만 재검증한다.

이미 목표와 같은 DNS를 일부러 망가뜨리지 않는다. 원본=목표의 무변경 결과를 실패상태 복원 성공으로 확대하지 않는다. drift/failed/unreachable/시간 초과 시 다음 행위 중단·원 snapshot 결속의 복귀 또는 Console 인수; hash 재승인 우회·다른 노드 확대·전역 PATH/RPM 교체 없음. 다른 role 호환·6대 전환 비교·운영 호출경로 전환은 DNS1회와 별도 잔여다.

[kplan]: https://github.com/321Team/infra-kubernetes/blob/c42ea6cc3ccd197d12993823bed439d40946a54c/ops/p1-k8s-01-v4/reconciliation/PLAN.md
[kmatrix]: https://github.com/321Team/infra-kubernetes/blob/c42ea6cc3ccd197d12993823bed439d40946a54c/ops/p1-k8s-01-v4/TEST_MATRIX.md
[if06]: https://github.com/321Team/infra-monitoring/blob/0dd0235b07d44ba7965490e3808e0a67a3bd903b/docs/IF06B_REMAINING_TEST_INPUTS_20261009.md
[monplan]: https://github.com/321Team/infra-monitoring/blob/0dd0235b07d44ba7965490e3808e0a67a3bd903b/docs/MON_MINIMUM_TEST_PREPARATION_20261009.md
