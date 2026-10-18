# Phase 1 As-built 차이 원본 후보 — 2026-10-16 상태 정합화

CODEX_ASSISTED · **DRAFT / 최종 As-built 승인 전**. 편집 원본은 이 문서와 [논리 MMD](candidate/architecture/P1_LOGICAL_AS_BUILT_20261015.mmd)·[물리 MMD](candidate/architecture/P1_PHYSICAL_AS_BUILT_20261015.mmd)다. 그림 파생본은 아직 만들지 않았고 MMD 렌더 검증도 미실행이다. 아래 값은 각 증적의 관측 시점에 한정하며 현재 서버를 다시 조회한 결과가 아니다.

## 이번 상태 정정의 범위

이 후보는 2026-10-15 원본을 보존한 별도 상태 정합화본이다. [중앙 ROUND33](../references/ROUND33.md)·[잔여 목록](../references/PHASE1_REMAINING_WORK_20261016.md)과 [APP 결과 연결](../APP_LINKAGE.md), [기존 SEC30 11행](../../sec30-adopted-linkage-20261016/README.md)을 소비했다. S08 문서 판독·APP 담당 결과 수신은 완료됐지만 I01 문서 미게시·음수 미래 transfer 영향의 정적 추론/실제 재현 NOT_RUN·APP 추가 판단 미결정, D02 SEC 초안 완료/미판정은 유지한다. MON/DOC 반영은 중앙의 별도 작업으로 연결하며 이 후보가 병합·발행 완료를 입증하지 않는다. 아키텍처·IP·배치·승인 기준은 변경하지 않았고 새 서버 조회·렌더 검증을 하지 않았다.

## 기준과 버전

- 승인 요구: `docs-v3.1.21` / `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`. Architecture 원본/파생 규칙 N02, 기준 변경 N03, 기존 D-ARC-01 N16, 승인 설계 MMD N39/N40을 재사용한다. [원천 인덱스](../../SOURCE_INDEX.json)
- 현재 문서 수용: baseline PR178 merge `0b7e8a0a1a6b920828b7e69e7e16e56016806351`, CICD 최종6190258707. 전체 O01/Phase1 인수는 미완료다.
- 저장소 HEAD의 기존 확인([2026-10-15 20:31:14 KST 재조회](../../FINAL_HEAD_READBACK.json))에서는 11개 모두 최초 대조 값과 같다. 이 값은 **문서/코드 저장소 버전**이며 배포 버전으로 자동 치환하지 않는다.
- 실제 정상 Delivery의 APP source는 `affbc69beef9967f7977d09a6fec14f7fb6c0e94`, CICD source는 `147f760298dd4a683ea58f2a887483769352b97d`. API manifest digest `338b8a2871507ce8b42deedc916b26e350577ee6efd18df23d7ff2dd4b17dff0`, engine `8b257adb08b6d381f72b66d3386efea6112a8f072ecfafcbcd463bcd1c3be89d`. [최종 수용 원문](https://github.com/321Team/fds-project-baseline/issues/16#issuecomment-6190258707)
- MON R10의 이미지·PV·배치는 10/2 관측을 기록한다. 줄임 digest를 전체 hash로 보충하지 않고 해당 source/원본 참조를 보존한다. 현재 main과 실제 전체 배포 형상의 동등성은 새로 입증하지 않았다.

## 논리 구성과 실제 범위

| 경로·기능 | 승인 설계 / 실제 확인된 구성 | 증적·차이·한계 / 책임 |
|---|---|---|
| Client→edge→앱 | edge01 `.50` nginx, HTTP80→Worker NodePort30080→transaction-api Service80/target8000 | APP6190096759의169+234+224/228 결합 재사용. 현행 digest Client→edge 새 POST는 없음. 읽은 nginx3파일만 연결, include 전체/모든 정책 실효 동일성 미입증. D02 HTTPS NOT_MET·SEC 초안 완료/미게시/미판정, APP 비차단 처분과 수동 확인 체계 수신. APP 이재환 |
| transaction-api→engine | 두 서비스 각3 Ready·Worker별 분산 관측, 내부 engine8001; API metrics9091/engine9090 분리 | Delivery/Probe 원본·N29/N37. 고정 app source의 `/livez`,`/readyz` 직접 대조. startupProbe는 실제 manifest별 판단. APP 이재환/SEC 이하영 |
| transaction-api→DB | db01 `.55:5432` 저장/조회, engine DB 직접 접근은 정책상 차단 | DB#11 최종6159292006·224 23ID/23행. N42의10/13 API7조회는 NP3/GNP7 형상 동일성이지 새 패킷 허용/거부 시험이 아님. 전체 namespace/모든5xx는 미입증. 이재환/이하영 |
| API 관리 | k8s-api-lb01 `.109:6443` HAProxy TCP TLS passthrough→CP `.102/.103/.104:6443` | N31/N41·StageB backend 제외/복귀·기존#9 종결. 실제 source allowlist/예산 한계는 Runbook 연결. 이권욱 |
| 이미지 공급 | Runner `.20`→Harbor `.54:443` push, Worker `.105/.107/.108` pull/Pod start | CICD AC02/06 기존 인수 소비. 현재 source/manifest 연결과 새 자격증명 회전은 다름. .50 예외 회수 실제 범위·r2 회전 준비와 Runtime 미실행 분리. 이하영/이권욱 |
| 자동화 | ansible01 `10.250.10.10`→승인 SSH/관리 경로 | 기존 P1-ANS/O02·CI86 결과 재사용. 10/16 08:50 역할185 시험은 첫 MON/2.16.19의 45사례 묶음 부분 실행·집계 불가, 나머지140 미시작·인정PASS0/185이며 해당 컨테이너 회수/부재 확인 완료. 이후 F1/F2 보완·독립 코드 검토 완료(새 코드 차단0)와 새 후보 Runtime 미검증·운영전환 잔여를 구분. 이권욱 |
| 클러스터 MON | monitoring-api Prometheus/Alertmanager/Grafana/KSM, monitoring-node node-exporter; 앱 metrics9091/9090·node9100·kubelet10250 | R10의10/2 구성. MON 핵심3종 single replica·local PV worker03 고정·Recreate 공백. Prometheus 보존15d/size16GB. N10 MON02 다중 replica 고도화는 P1 우선순위 후속. 이재환 |
| 외부 Watchdog | in-cluster Prometheus(worker03 `.108`)→mgmt-gw01→monitor01 `.30:443`→nginx8443→localhost receiver19090 | R10 10/2 구조. localhost blackbox9115가 `.109:6443` TCP probe. 기존 IF06B 한계/귀속은 원천 SEC 판정 연결. monitor01 전체광범위 scrape 설계로 복원하지 않음. 이재환/이하영 |
| Grafana 관리 | ClusterIP, 승인된 관리 PF 요구와 실제 배타성 입증을 구분 | 19:14:40 PF NOT_MET+한정 위험수용. E1/E2/E4 조건 내 유효·E3 정상 사용 금지·C1 회전 보류. 사람 사본·과거 감사 공백 유지. 이권욱/이하영 |
| Backup/Restore | PostgreSQL16.14,9/29 dump51,491B·1,209행·격리복원·R02 E2E·원복/정리 | N21/N43·DR#21 최종6138444604. 9/3 D01 5,206B dump와 다른 원본. PC/SHARE 보관·10/26 재검토는 자동 폐기 아님. 이재환/이권욱 |
| 보호·복구 경계 | Default Deny·required allowlist·RBAC·Secretbox·HEP/GNP·SELinux 기준 유지 | SEC30 확정6205182638의 Worker3 한정 위험수용·K8S Known Issue 비차단·backup 하위 한정 MET·OID02 계약4/5 처분을 연결. 기술 NOT_MET/NOT_VERIFIED/PARTIAL 및 AC05 전체 [ ]·#14 CRI/재부팅 소비·OID03 조건부 잔여는 유지. 기존 11행 완료본을 재사용하며 새 예외/통제 해제 없음. 이하영 |

## 물리 배치 기준과 확인 수준

주소 앞의 `.xx`는 `10.1.93.xx`다. 아래 Windows Host IP/전체 VM 배치는 N39 승인 설계에서 상속한 값이며 이 작업에서 현장 전수 재확인하지 않았다. 관측이 있는 VM/경로만 위 표의 증적으로 연결한다.

| 배치 | 상속한 물리·VM 정보 | 최근 연결 증적 / 미확인 |
|---|---|---|
| server01 / Windows `.23` | mgmt-gw01 `.58`/`10.250.10.1`, ansible `.10`, runner `.20`, monitor `.30`, API LB `.109`, dns01 `.52`; 관리망10.250.10.0/24 | LB N31, MON R10, CICD최종/O02. 전체 VM 실제 host inventory 최신성은 별도 미확인 |
| server02 / Windows `.30` | control01 `.102` | K8S/SEC 원천 결과의 노드별 범위 소비 |
| server03 / Windows `.31` | control02 `.103` | 동일; 부팅/표본 미판정 범위 유지 |
| server04 / Windows `.22` | control03 `.104` | control03 rollback 부분 결과·API LB backend 연결 |
| server05 / Windows `.26` | worker01 `.105` | Probe/APP/HA·Harbor 기존 관측 연결 |
| server06 / Windows `.24` | worker02 `.107` | Probe223 이벤트 시각/clock 한계 보존 |
| server07 / Windows `.25` | worker03 `.108`, MON local PV 3종 | R10 Retain·nodeAffinity·local path 관측. 노드 장애 시 다른 Worker로 PVC 자동 이동 불가 |
| server08 / Windows `.29` | edge01 `.50`, harbor01 `.54`, db01 `.55`, dns02 `.53` | edge234·DB#11/DR#21·Harbor 실제 결과 연결. Phase2 VPN `.51`은 이번 구현 범위에서 제외 |

VMnet0/물리망 `10.1.93.0/24`, VMnet1 관리망 `10.250.10.0/24`, FDS workload VM의 VMnet8 연결 금지, 관리망 return route `10.250.10.0/24 via 10.1.93.58`, 내부 source NAT 금지는 승인 설계 기준을 유지한다. 모든 host에서 현재 실제로 적용됐다는 새 증명은 아니다. Reserved `.56/.57/.59`, DO_NOT_USE `.100/.101/.106`도 상속한 IPAM 기준으로 표시한다.

## 기존 자료와의 차이·채택 전 해소할 항목

1. N14의 형상 목록에는 Logical/Physical v3.1.3 MMD RELEASED(D33)가 있으나 이번 조회의 D-ARC 보관 경로에서는 v3.1.2만 확보했다. v3.1.3가 프로젝트 전체에 없다고 판정하지 않는다. 정확한 기존 source를 찾으면 우선 재사용하고, 없다면 후보를 새 개정 원본으로 채택하는 결정이 필요하다.
2. Architecture logical HTML(N19)은 edge HAProxy/80·443, DB IN_PROGRESS, 과거 MON/egress 상태가 남아 있다. 이 후보는 증적234·CICD/DB 최신 인수와 MON R10을 별도 연결한다. 설계 목표80/443과 실제 현재 HTTPS 제공을 혼동하지 않는다.
3. physical HTML(N20)은 과거 커밋 `8af821ecf76cd13442210a1bb32b829696200b80`의 physical HTML을 fetch하는 JS loader를 포함한다. 이번 보존본은 visible-text 추출이므로 전체 실행 화면·원격 payload·렌더 성공을 확인한 것으로 세지 않는다. 최종 오프라인 편집 원본을 별도로 고정한다.
4. 새 MMD는 승인된 물리 배치와 증적별 논리 차이를 표현한 후보다. 아직 전체 As-built 승인·render QA를 받지 않았다. 최종 문서 source/version, 변경점의 기존 증적 대응, 남은 미확인/처분을 Lead가 확인해야 한다.
5. 확정된 SEC30 조건과 APP 회신의 해당 판단은 기존 완료본에 연결하고, 다른 Known Issue Owner/Due·잔여 기술 인수의 미확정 값은 유지한다. 역할185 부분 실행·회수 완료와 새 후보 Runtime 미검증을 구분하며 준비된 회전·운영전환·DR02·MON02·Phase2를 완료로 그리지 않는다.
