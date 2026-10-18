# Phase 1 As-built 차이 원본 후보 — 2026-10-16 확정 상태 반영

CODEX_ASSISTED · **DRAFT / 최종 As-built 승인 전**. 편집 원본은 이 문서와 [논리 MMD](candidate/architecture/P1_LOGICAL_AS_BUILT_20261015.mmd)·[물리 MMD](candidate/architecture/P1_PHYSICAL_AS_BUILT_20261015.mmd)다. 그림 파생본은 아직 만들지 않았고 MMD 렌더 검증도 미실행이다. 아래 값은 각 증적의 관측 시점에 한정하며 현재 서버를 다시 조회한 결과가 아니다.

## 이번 상태 정정의 범위

이 후보는 [기존 2026-10-16 상태 후보](../as-built-candidate/P1_AS_BUILT_CANDIDATE.md)와 원본 3파일/선택 카드를 보존한 별도 후속이다. 오늘 확정된 역할185 격리 시험·회수, D02 최종 연결, APP38/39 문서 반영, D-07 관리값과 Harbor 검토/관측 결과만 [고정 영수증](SOURCE_BINDING.json)으로 소비한다. 아키텍처·IP·배치·승인 기준·기존 SEC30/Grafana 조건은 변경하지 않았다. 같은 성공 시험·전수 소스 탐색·서버 조회·렌더 검증은 수행하지 않았으며 전체 As-built 채택·DOC Freeze·인수·정본 발행은 미결정이다.

## 기준과 버전

- 승인 요구: `docs-v3.1.21` / `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`. Architecture 원본/파생 규칙 N02, 기준 변경 N03, 기존 D-ARC-01 N16, 승인 설계 MMD N39/N40을 재사용한다. [원천 인덱스](../../SOURCE_INDEX.json)
- 기존 문서 수용 이력: baseline PR178 merge `0b7e8a0a1a6b920828b7e69e7e16e56016806351`, CICD 최종6190258707. 아래 오늘의 문서/상태 결과를 함께 읽으며 전체 O01/Phase1 인수는 미완료다.
- 저장소 HEAD의 기존 확인([2026-10-15 20:31:14 KST 재조회](../../FINAL_HEAD_READBACK.json))에서는 11개 모두 최초 대조 값과 같다. 이 값은 **문서/코드 저장소 버전**이며 배포 버전으로 자동 치환하지 않는다.
- 실제 정상 Delivery의 APP source는 `affbc69beef9967f7977d09a6fec14f7fb6c0e94`, CICD source는 `147f760298dd4a683ea58f2a887483769352b97d`. API manifest digest `338b8a2871507ce8b42deedc916b26e350577ee6efd18df23d7ff2dd4b17dff0`, engine `8b257adb08b6d381f72b66d3386efea6112a8f072ecfafcbcd463bcd1c3be89d`. [최종 수용 원문](https://github.com/321Team/fds-project-baseline/issues/16#issuecomment-6190258707)
- MON R10의 이미지·PV·배치는 10/2 관측을 기록한다. 줄임 digest를 전체 hash로 보충하지 않고 해당 source/원본 참조를 보존한다. 현재 main과 실제 전체 배포 형상의 동등성은 새로 입증하지 않았다.

## 오늘 확정된 문서·상태 입력

| 항목 | 소비한 확정 사실 | 유지할 경계 |
|---|---|---|
| 역할185 | [실제 결과/회수 인계](references/ANSIBLE_RUNTIME_FINAL_HANDOFF.md), [중앙17:31 수용](references/ANSIBLE_ROLE185_FINAL_HANDOFF_CENTRAL.json). 185 PASS/0 FAIL/0 SKIP, 컨테이너 create/start/rm 각1회, 17:17:55 정확 CID 부재·실행기0 확인 | 서비스/chronyc 등 모의 관측 포함. 운영 호스트 적용/전체 AC가 아님. [17:47 후속 인계](references/ANSIBLE_POST_PASS_HANDOFF_CENTRAL.json)의 새 증적 공개 위치·실제 caller/source/config/targets 채택은 미결정. 08:50 부분 실패 원본은 과거 이력으로 보존 |
| D02 | [최종6208668917](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6208668917)·[확정 보충](references/D02_IMPACT_ROWS.json). 수행자 이재환, 위험 소유 이권욱. MON PR44 문서 반영·수행 인수 대기 해소 | 현재 edge HTTP80·실습망 시험/합성 데이터, 10/26 P1 자원 회수까지. 회수 지연·하루 이상 확인 불가·노출/감시 구성 변경·실제 데이터 유입 시 재검토. 자동 연장/HTTPS 충족/실제 점검 소급 생성 아님 |
| APP 문서 | PR38 입력 규약·I01/D-07 분리 기록에 이어 [PR39](https://github.com/321Team/fds-msa/pull/39) §5–7 정정이 18:00:23 KST merge `93800f09d2f5de61f6e2336771e62881f036c9ff`로 반영. 문서 SHA256 `3a721545aa469527dc03f0f3624c7be20d04f67c2e93b71f1553db5752e96c6c`. [merge](references/APP39_MERGE_RECEIPT.json)·[main CI38877485275](references/APP39_CI_RECEIPT.json) attempt1 SUCCESS, 실제 validate1/skipped2 | 최종 패키지 전체 완료를 가정하지 않고 두 확정 영수증만 소비. 문서 main과 기존 배포 affbc69b는 별도. 코드/서버 검증 구현·제품 잔여 해소·전체 APP/E2E 인수 아님 |
| D-07 | [Lead6211817978](https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-6211817978): ID D-07, Owner 이재환(APP Lead), 첫 재검토 APP 최종 인수 판정 직전. [18:04 중앙 연결 수용](references/D07_CENTRAL_ACCEPTANCE.json) | Major·P1 코드 무수정·잔여위험·실제 음수 저장/후속 미탐 NOT_RUN·운영 db01 제약 NOT_VERIFIED·I01 별도. 기존 Critical0·Regression/Defect 승인은 유지. 첫 재검토는 수정 완료기한/P2 이관/위험수용 만료일 아님. 공식 대장 채택·외부 반영·전체 인수는 별도 |
| Harbor | [정확 코드 기술 검토](references/HARBOR_EFFECT_FULL_REVIEW_CENTRAL.json) 완료·코드 차단0, 운영 HOLD. [기록상 ID2 만료17:02:37 경과](references/HARBOR_BUILD_EXPIRY_READINESS_CENTRAL.json). [17:38 metadata](references/HARBOR_CORE_METADATA_CENTRAL.json)와 [공식 config 결속](references/HARBOR_OFFICIAL_IMAGE_BINDING.json)의 동일 config ID 기준 불일치 확인 | 공식 config `701038c9f9cfed2052de8a458a820be7569df80f1e926f84e3509a0caa31d205` / 관측 imageID `a22b58594cea54a78d1c670a81b9dfa3c5af8b4bdd1f89750fdf1c5876c72eab`. 차이의 원인·설치/build/serializer provenance·현재 인증/건강은 미확인. 비공식/침해 확정 아님. 구 credential 원복/새 회전 성공을 가정하지 않음 |

## 논리 구성과 실제 범위

| 경로·기능 | 승인 설계 / 실제 확인된 구성 | 증적·차이·한계 / 책임 |
|---|---|---|
| Client→edge→앱 | edge01 `.50` nginx, HTTP80→Worker NodePort30080→transaction-api Service80/target8000 | APP6190096759의169+234+224/228 결합 재사용. 현행 digest Client→edge 새 POST는 없음. 읽은 nginx3파일만 연결, include 전체/모든 정책 실효 동일성 미입증. [D02 최종6208668917](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6208668917)으로 MON 수행 인수·문서 반영 대기는 해소. HTTPS NOT_MET·평문·자동 통보 공백과 기존 한정 조건은 유지. APP 이재환 / 위험 소유 이권욱 |
| transaction-api→engine | 두 서비스 각3 Ready·Worker별 분산 관측, 내부 engine8001; API metrics9091/engine9090 분리 | Delivery/Probe 원본·N29/N37. 고정 app source의 `/livez`,`/readyz` 직접 대조. startupProbe는 실제 manifest별 판단. APP 이재환/SEC 이하영 |
| transaction-api→DB | db01 `.55:5432` 저장/조회, engine DB 직접 접근은 정책상 차단 | DB#11 최종6159292006·224 23ID/23행. N42의10/13 API7조회는 NP3/GNP7 형상 동일성이지 새 패킷 허용/거부 시험이 아님. 전체 namespace/모든5xx는 미입증. 이재환/이하영 |
| API 관리 | k8s-api-lb01 `.109:6443` HAProxy TCP TLS passthrough→CP `.102/.103/.104:6443` | N31/N41·StageB backend 제외/복귀·기존#9 종결. 실제 source allowlist/예산 한계는 Runbook 연결. 이권욱 |
| 이미지 공급 | Runner `.20`→Harbor `.54:443` push, Worker `.105/.107/.108` pull/Pod start | CICD AC02/06 기존 인수 소비. Harbor 코드 기술 검토는 완료했으나 운영 HOLD다. ID2 기록상 만료 및 공식 config/관측 imageID 불일치는 아래 확정 범위로 연결한다. provenance·현재 인증·건강·새 회전은 미확인/미완료이며 .50 예외의 기존 한정 회수와 구분. 이하영/이권욱 |
| 자동화 | ansible01 `10.250.10.10`→승인 SSH/관리 경로 | 기존 P1-ANS/O02·CI86 결과 재사용. source `affaad6b1a31d680164d9e3d5ef5d2a9d3fce95a`의 17:09~17:13 격리 컨테이너 LOCAL/MOCK 7묶음 185/185 PASS·회수/부재 확인 완료. 실제 Ansible/module·파일/parser 경로와 모의 서비스/호스트 관측을 구분하며 운영 MON/NTP/SSH 적용 인수는 아님. 코드/증적 공개·운영 caller/source/config/targets 채택·전환/복귀는 잔여. 이권욱 |
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
5. 확정된 SEC30/Grafana 조건과 APP 기존 승인은 유지한다. 역할185의 실제 LOCAL/MOCK 실행·회수 공백은 해소됐고 공개/운영 호출 경로 채택·전환은 별도다. D-07 ID·Owner·첫 재검토 확정은 중앙의 로컬 연결 수용까지 소비하며 공식 대장 채택·전체 인수는 별도다. Harbor 운영 HOLD와 provenance/현재 인증/건강 미확인, 다른 Known Issue의 미확정 책임/기한, DR02·MON02·Phase2 미완료 범위를 유지한다.
