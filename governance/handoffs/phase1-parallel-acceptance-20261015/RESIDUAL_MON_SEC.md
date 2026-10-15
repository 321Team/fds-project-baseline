# MON·SEC 잔여 처분안 — 기존 관측 재사용과 최소 보완

2026-10-15 KST · CODEX_ASSISTED · 사용자 “1~2번 착수”의 1번 결과. MON Lead 이재환, SEC Lead 이하영, 통합 검토 이권욱. **기술 대조·처분 제안이며 새 AC 인수·위험수용·Runtime GO가 아니다.** [기존 대응표](MON_SEC.md)와 [조회 근거](RESIDUAL_SOURCE_INDEX.json)를 함께 읽는다. Phase 2 제외.

## 1. 이번에 구체화한 차이

| 항목 | 기존 자료로 확인한 사실 | 이번 처리 |
|---|---|---|
| Backup | [증적152](https://github.com/321Team/fds-project-evidence/pull/152) merge `9dbc2f8ba3f913aab143d273eae9e89333b94e96`. 실제 snapshot 격리 복원·임시 etcd health·revision3287996/keys620 일치·secretbox prefix7/7·정리/사후 확인이 있음 | 단순 snapshot 존재/해시 수준으로 축소하지 않는다. 같은 격리 복원 재시험 후보 제거. AC05 요구별 최종 수용만 남김 |
| IF-03·IF-13A | [증적157](https://github.com/321Team/fds-project-evidence/pull/157) merge `6014e9a961af497e78be9c383d270291013db5cf`. 일반 Pod34건과 hostNetwork/외부대조20건이 편입됨 | 10/7 표의 ‘목적지 ingress·외부 UDP·일반 egress·hostNetwork 미실행’을 현재 값으로 복제하지 않음 |
| IF-05C | 157의 전용 규칙 Firing→Alertmanager→복원·Discord 두 메시지와 [정정180](https://github.com/321Team/fds-project-evidence/pull/180) 존재 | 감지/외부 수신을 미실행으로 되돌리지 않음. 원 collector rc3·별도 사후 점검rc0·수신 시각 한계 유지 |
| Grafana | [10/7 MON Lead](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-6032975302)가 과거 승인 PF와 직접 외부 음성 시험 재사용 범위를 한정 수용 | 해당 성공 재시험을 기본안에서 제거. ‘PF만 가능’이라는 배타성·비상 접근·감사 처분은 별도 |
| Probe | 177은 6종 정의/Pod10 Ready, 173은 격리 exec 전이, 223은 실제 engine HTTP 실패/재시작/회복 | 세 증거 유형을 구분. 전체6종 장애 주입이나 모든 startupProbe를 새 요구로 추가하지 않음 |

Backup의 [SEC Lead 보고 수용](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-6049595085)과 현재 #19의 완료된 보완 행도 확인했다. 이 문서가 이미 체크된 하위 결과를 새로 승인하는 것은 아니다. 이전 준비표의 ‘backup 복구 가능성 확인’은 아래처럼 남은 **인수 범위 판단**으로 좁힌다.

## 2. SEC-AC02 행별 후속 — 원장 유지, 확정 합계 없음

기준은 [10/7 행별표](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-6039967923), [Review Owner 정정·한정 관측 수용](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-6040616297), 이후 편입 증적이다. RISK 표기는 RISK ACCEPTED가 아니다.

| 흐름 | 재사용 가능한 범위 | 실제 남은 판단·최소 보완 |
|---|---|---|
| IF-03 API→engine8001 | 157: API 네트워크→engine3개 TCP3/3; CoreDNS 출발 비허용3/3 TIMEOUT, Worker별 정확한 SYN3개와 목적지 DROP+3 연결 | L3/L4 표본이며 업무 프로세스/UID·모든 source의 검증 아님. 동일 selector/label/정책에 대해 이 표본을 인수할지 이하영 판단. 과거 KSM SKIP이나 MON TIMEOUT을 소급 성공 처리하지 않음 |
| IF-13A 일반 Pod | APP6+MON4 CoreDNS UDP10/10, 외부8.8.8.8 UDP10/10 TIMEOUT·외부 대조응답1; API3+MON4 외부TCP7/7 TIMEOUT·egress DROP 연결 | namespace/PID/Pod UID에 결속한 호스트 Python 관측. 애플리케이션 바이너리의 egress 기능이나 모든 외부 목적지 보장으로 확대하지 않음 |
| IF-13A hostNetwork | Worker3 내부 DNS UDP6+TCP6, 외부UDP EPERM3·TCP TIMEOUT3, 외부 대조2 | 최초 UDP syscall 단계 누락·collector 오류 보존. Worker03 DROP+10을 시험3패킷과 일대일 귀속하지 않음. 다른 hostNetwork 소스는 자동 인수하지 않음 |
| IF-12B | 144 및 기존 수용: CP02/03→Worker3 TCP/TLS handshake6경로 | CA verify error20/21·인증 미실행을 성공으로 바꾸지 않음. 남은 CA/Auth/API 권한 요구를 기존 kubelet TLS/RBAC 근거와 연결; 이6경로 단순 접속 반복 없음 |
| IF-09 | [145](https://github.com/321Team/fds-project-evidence/pull/145)의 비승인 `.23` timeout/guard DROP 관측은 편입됨 | ‘비승인 source 능동시험 없음’은 부정확. Harbor 담당의 최신 정책·예외 변경 영향과 해당 표본 수용을 #13/#16에서 소비. 새 Harbor 시험을 이 문서로 추가하지 않음 |
| IF-06B | 207의 gateway 구간·canary 만료/회수·정리, 기존 source/401 | 특정 nft rule의 유일 귀속·모든 payload/실패경로까지 확대하지 않고 기존 gateway 구간 판정 범위로 연결 |
| IF-05C | 157·180의 규칙 전이·Alertmanager·Discord 수신 | 9093 긍정 전달과 Default Deny 부정 검증은 구분. 남은 source/정책 행을 원 Matrix와 대조한 뒤 필요한 경우만 지정 |
| IF-12A/12C | 기존 정상 노드 쌍과 NNRD 범위 | 정상 쌍의 일괄 Negative를 추가하지 않되 비승인 Source DENY·TCP179/IP protocol4 미허용 등 정본 조건까지 면제하지 않음 |
| IF-10 | 기존 Worker3 Pull/RepoDigest·Push DENY·Pod 기동 수용 | 최초 실패/절차 이탈 근거를 유지하고 동일 범위 재시험 없음 |

**권고:** 이번에 원장에 남길 값은 ‘새 관측 편입 완료 + 표본/한계 + 담당자의 인수 대기’다. 전체 AC02를 PASS로 바꾸거나, 남은 모든 행을 다시 시험하라는 결론은 내리지 않는다. 현 정책 변경이 확인되면 바뀐 source/destination/port 행만 재검토한다.

## 3. Grafana·부팅·Backup의 결정 카드

| 카드 | 사실·영향 | 권고안과 완료조건 | 책임 |
|---|---|---|---|
| G1 관리 배타성 | 과거 제한PF 성공/회수, 175의 ClusterIP·Ingress0·관리 wildcard binding·root0600 파일, 185의 Secret 참조, 212의 관리 선언을 재사용. 팀3명 control01 경로 사용 가능·개인별 과거 사용 기록 미보유는 기존 회신 | 정상 PF와 admin.conf/super-admin.conf·exec 비상 경로를 별도 행으로 유지. 허용자/조건/회수 범위를 현행 장부에 연결하고 ‘승인 단말만’ 요구와의 차이를 MON·SEC가 처분. 소유자 확정을 자격증명 실제 회수 완료로 바꾸지 않음 | 이재환·이하영; Grafana 보관/회수 책임 이권욱 |
| G2 감사 공백 | 212의 mirror Pod3개 선언에 audit 인자0은 관측 사실. 전체 auditd/외부 감사 부재나 과거 행위 없음은 증명하지 못함 | 미보유 과거 원본 재요청 금지. 과거 공백의 영향·수용 여부를 기록. 앞으로의 기록 방법은 기존 운영 절차 보완 또는 별도 감사 변경안으로 제안하며 자동 승인하지 않음 | 이하영 보안 판단, 이권욱 통합 |
| B1 부팅 연속 보호 | 144 방식B의 기존 누락6행 관측은 해소. steady-state 통신과 부팅 중 보호는 다름. 과거 CP3 한정 위험수용을 현6노드에 확대 불가 | 최신 보호 입력/적용 상태·시작 순서/기존 reboot 증거의 차이만 대조. 실제 공백이 남으면 영향 노드의 보완 또는 정확 범위 처분을 제시. 6대 재부팅을 기본조건으로 만들지 않음 | 이하영 K8S/SEC, 이권욱 ICR |
| S1 Backup 복합 AC | 152는 실제 고정 snapshot의 격리 restore·health·정리 성공. Secret 복호화/APP 소비·운영 etcd member 복원/DR은 시험하지 않음 | 기존 encryption MET·control03 rollback MET·예방 rotation NOT MET/RISK ACCEPTED와 각각 결합해 AC05 인수안을 제출. 추가 복호화/운영복원 시험이 필수라고 판단한다면 정확한 승인 요구 문구와 미충족 범위를 먼저 지목; 새 AC로 자동 추가하지 않음 | 이하영; 기존 Review Owner 판단 별도 |

이 카드의 새 Due·수용자는 미확정이다. 이전 회신에 없는 값·예외를 생성하지 않는다. [기존 Grafana 장부](https://github.com/321Team/infra-monitoring/blob/0dd0235b07d44ba7965490e3808e0a67a3bd903b/docs/GRAFANA_ACCESS_LEDGER_20261009.md)의 ‘보관자 미확인’은 이후 [이권욱 책임 확정](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-6139012660)으로 보완해 읽는다.

## 4. Probe 요구별 대응

[177 analysis.json](https://github.com/321Team/fds-project-evidence/blob/43e26384ae422f2017f1e96e6c1bb5fe46d087d4/evidence/P1-SEC-01/six-probe-inventory-20261009T011520/analysis.json)의 **10/9 snapshot**이다. 현재 서버를 재조회한 값은 아니다.

| 대상 | liveness / readiness | 증거 수준·남은 판단 |
|---|---|---|
| fds-engine | 8001 `/livez` / `/readyz` | 177 정의·Ready + 223 실제 HTTP 실패→Endpoint 제외→kubelet 재시작→회복. APP 실제 사례로 재사용; 관측기rc1·최초 HTTP 회복시각 한계 유지 |
| Prometheus | 9090 `/-/healthy` / `/-/ready` | 177 정의·Ready·startup `/-/ready`. 재시작/PVC 유지 증거와 Probe에 의한 장애 회복은 구분 |
| Alertmanager | 9093 `/-/healthy` / `/-/ready` | 177 정의·Ready·startup `/-/ready`. 알림 Firing/Resolved가 자체 Probe 실패 증거는 아님 |
| Grafana | 3000 `/api/health` / `/api/health` | 177 정의·Ready·startup 동일. PF health 성공·Secret 참조와 장애 주입을 혼동하지 않음 |
| kube-state-metrics | 8080 `/livez` / 8081 `/readyz` | 이름 포트 http-metrics=8080·telemetry=8081. 과거 `/healthz` 불일치와 구분. TargetDown 알림과 실제 Probe 원인별 회복은 분리 |
| node-exporter | 9100 `/` / `/metrics` | 177 정의·Ready. 누적 restart4/1/1은 원인·시각 불명, 성공 장애주입 증거 아님 |

transaction-api는 이 ‘6종’ 목록에 포함되지 않는다. 이를 APP 전체 인벤토리로 쓰지 않는다. MON 보조통제 B01의 올바른 경로·정상 결과와 SEC-AC06의 장애/Endpoint 제외는 다른 주장이다.

**다음 결정:** 이재환·이하영이 기존 MON 실패/복구 원본 중 AC06에 대응하는 것을 먼저 지정한다. 이번 조회로 MON5종 실제 HTTP 실패 전이를 확인했다고 하지 않는다. 대응 원본이 없다면 부족한 행에 대한 최소 대표 사례 후보를 제출한다. 모든5종 재시험 또는 startup 미정의 컴포넌트의 startup 신설을 자동 요구하지 않는다.

## 5. 후속 수집·실행의 최소 경계

지금 가능한 것은 원본·설정 차이의 오프라인 대조와 담당자의 범위 판단이다. 새 서버 명령은 이번에 실행하지 않았다.

- 추가 읽기가 필요한 경우: 기존 승인 관리 경로, 정확 호스트·계정·원본 경로/조회 필드·고정 SHA·timeout을 한 회차 카드로 고정한다. Secret 값·kubeconfig 본문·개인별 미보유 과거 로그는 요청하지 않는다.
- 새 장애/트래픽 시험이 필요한 경우: 요구 행, 대상 workload/UID, 비중첩 창, 관측자, 시작 기준, 최대 중단시간, 복구 입력·종료 확인을 먼저 완성한다. 이 문서는 실행 GO가 아니다.
- 정상 기준: 지정 행의 관측/원본과 기대값이 대응하고 변경 전후 상태·정리가 확인되어야 한다. hash만 일치하거나 Ready만 확인한 결과로 전체 AC를 판정하지 않는다.
- 중단 기준: 대상/버전 불일치, 기존 증거로 이미 충족된 재시험, 공유 작업 중첩, 관측·복구 경로 부재. 실패 원본을 보존하고 해당 회차 소유 자원만 정리한다. 보안 통제 해제·일괄 재부팅·운영 etcd 복원·자격증명 회전을 자동 수행하지 않는다.

현재 단계: STATIC 대조 완료 / 새 서버 RUNTIME 미실행 / Lead 인수·REVIEW·MERGE·Close 별도. 이 문서의 구체화는 공통 실행 Gate 신설이 아니다.
