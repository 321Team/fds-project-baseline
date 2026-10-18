# Phase 1 As-built — p1-as-built-20261018-r1 채택·발행 후보

CODEX_ASSISTED · **PROPOSED / 채택·발행·Freeze 미승인**. 제안 개정 식별자는 p1-as-built-20261018-r1이다. 편집 원본은 이 설명과 [배치 조정 논리 MMD](source-set/payload/current/render-validation-20261016/proposal-layout-constraints/P1_LOGICAL_LAYOUT_PROPOSAL.mmd)·[물리 MMD](source-set/payload/current/candidate/architecture/P1_PHYSICAL_AS_BUILT_20261015.mmd)다. 기존 렌더·시각 검토를 재사용하며 [필수 렌더러와 파생물 결속](DERIVATIVE_PROVENANCE.json)을 함께 관리한다. 아래 값은 각 증적의 관측 시점에 한정한다. DOC의 새 서버 조회는 없으며10/18 19:00~19:02 중앙 관측을 아래 보충으로 소비한다.

## 이번 상태 정정의 범위

이 후보는 [기존 2026-10-16 상태 후보](source-set/payload/as-built-candidate/P1_AS_BUILT_CANDIDATE.md)와 원본 3파일/선택 카드를 보존한 별도 후속이다. 10/16에 확정된 역할185 격리 시험·회수, D02 최종 연결, APP38/39 문서 반영, D-07 관리값과 Harbor 검토/관측 결과만 [고정 영수증](source-set/payload/current/SOURCE_BINDING.json)으로 소비한다. 아키텍처·IP·배치·승인 기준·기존 SEC30/Grafana 조건은 변경하지 않았다. 이번 발행 후보 작성에서는 같은 성공 시험·전수 소스 탐색·서버 조회·렌더를 반복하지 않았으며 전체 As-built 채택·DOC Freeze·인수·정본 발행은 미결정이다.

## 기준과 버전

- 승인 요구: `docs-v3.1.21` / `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`. Architecture 원본/파생 규칙 N02, 기준 변경 N03, 기존 D-ARC-01 N16, 승인 설계 MMD N39/N40을 재사용한다. [원천 인덱스](source-set/SOURCE_INDEX.json)
- 기존 문서 수용 이력: baseline PR178 merge `0b7e8a0a1a6b920828b7e69e7e16e56016806351`, CICD 최종6190258707. 아래10/16 문서/상태 결과와10/18 보충를 함께 읽으며 전체 O01/Phase1 인수는 미완료다.
- 저장소 HEAD의 기존 확인([2026-10-15 20:31:14 KST 재조회](source-set/FINAL_HEAD_READBACK.json))에서는 11개 모두 최초 대조 값과 같다. 이 값은 **문서/코드 저장소 버전**이며 배포 버전으로 자동 치환하지 않는다.
- 실제 정상 Delivery의 APP source는 `affbc69beef9967f7977d09a6fec14f7fb6c0e94`, CICD source는 `147f760298dd4a683ea58f2a887483769352b97d`. API manifest digest `338b8a2871507ce8b42deedc916b26e350577ee6efd18df23d7ff2dd4b17dff0`, engine `8b257adb08b6d381f72b66d3386efea6112a8f072ecfafcbcd463bcd1c3be89d`. [최종 수용 원문](https://github.com/321Team/fds-project-baseline/issues/16#issuecomment-6190258707)
- MON R10의 이미지·PV·배치는 10/2 관측을 기록한다. 줄임 digest를 전체 hash로 보충하지 않고 해당 source/원본 참조를 보존한다. 현재 main과 실제 전체 배포 형상의 동등성은 새로 입증하지 않았다.

## 2026-10-16 확정 문서·상태 입력 — 당시 기록

| 항목 | 소비한 확정 사실 | 유지할 경계 |
|---|---|---|
| 역할185 | [실제 결과/회수 인계](source-set/payload/current/references/ANSIBLE_RUNTIME_FINAL_HANDOFF.md), [중앙17:31 수용](source-set/payload/current/references/ANSIBLE_ROLE185_FINAL_HANDOFF_CENTRAL.json). 185 PASS/0 FAIL/0 SKIP, 컨테이너 create/start/rm 각1회, 17:17:55 정확 CID 부재·실행기0 확인 | 서비스/chronyc 등 모의 관측 포함. 운영 호스트 적용/전체 AC가 아님. [17:47 후속 인계](source-set/payload/current/references/ANSIBLE_POST_PASS_HANDOFF_CENTRAL.json)의 새 증적 공개 위치·실제 caller/source/config/targets 채택은 미결정. 08:50 부분 실패 원본은 과거 이력으로 보존 |
| D02 | [최종6208668917](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6208668917)·[확정 보충](source-set/payload/current/references/D02_IMPACT_ROWS.json). 수행자 이재환, 위험 소유 이권욱. MON PR44 문서 반영·수행 인수 대기 해소 | 현재 edge HTTP80·실습망 시험/합성 데이터, 10/26 P1 자원 회수까지. 회수 지연·하루 이상 확인 불가·노출/감시 구성 변경·실제 데이터 유입 시 재검토. 자동 연장/HTTPS 충족/실제 점검 소급 생성 아님 |
| APP 문서 | PR38 입력 규약·I01/D-07 분리 기록에 이어 [PR39](https://github.com/321Team/fds-msa/pull/39) §5–7 정정이 18:00:23 KST merge `93800f09d2f5de61f6e2336771e62881f036c9ff`로 반영. 문서 SHA256 `3a721545aa469527dc03f0f3624c7be20d04f67c2e93b71f1553db5752e96c6c`. [merge](source-set/payload/current/references/APP39_MERGE_RECEIPT.json)·[main CI38877485275](source-set/payload/current/references/APP39_CI_RECEIPT.json) attempt1 SUCCESS, 실제 validate1/skipped2 | 최종 패키지 전체 완료를 가정하지 않고 두 확정 영수증만 소비. 문서 main과 기존 배포 affbc69b는 별도. 코드/서버 검증 구현·제품 잔여 해소·전체 APP/E2E 인수 아님 |
| D-07 | [Lead6211817978](https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-6211817978): ID D-07, Owner 이재환(APP Lead), 첫 재검토 APP 최종 인수 판정 직전. [18:04 중앙 연결 수용](source-set/payload/current/references/D07_CENTRAL_ACCEPTANCE.json) | Major·P1 코드 무수정·잔여위험·실제 음수 저장/후속 미탐 NOT_RUN·운영 db01 제약 NOT_VERIFIED·I01 별도. 기존 Critical0·Regression/Defect 승인은 유지. 첫 재검토는 수정 완료기한/P2 이관/위험수용 만료일 아님. 공식 대장 채택·외부 반영·전체 인수는 별도 |
| Harbor | [정확 코드 기술 검토](source-set/payload/current/references/HARBOR_EFFECT_FULL_REVIEW_CENTRAL.json) 완료·코드 차단0, 운영 HOLD. [기록상 ID2 만료17:02:37 경과](source-set/payload/current/references/HARBOR_BUILD_EXPIRY_READINESS_CENTRAL.json). [17:38 metadata](source-set/payload/current/references/HARBOR_CORE_METADATA_CENTRAL.json)와 [공식 config 결속](source-set/payload/current/references/HARBOR_OFFICIAL_IMAGE_BINDING.json)의 동일 config ID 기준 불일치 확인 | 공식 config `701038c9f9cfed2052de8a458a820be7569df80f1e926f84e3509a0caa31d205` / 관측 imageID `a22b58594cea54a78d1c670a81b9dfa3c5af8b4bdd1f89750fdf1c5876c72eab`. 차이의 원인·설치/build/serializer provenance·현재 인증/건강은 미확인. 비공식/침해 확정 아님. 구 credential 원복/새 회전 성공을 가정하지 않음 |

## 2026-10-18 18:59 KST 기록 대조 보충

아래는 이후 확정된 기록의 보충이다. 위10/16 표와 MMD의 당시 상태는 이 표와 함께 읽는다. 도식은 구성 관계·기존 관측 시점의 설명이며 현재 서비스 정상 표시가 아니다. 이18:59 보충 이후의19:00~19:02 제한 관측은 다음 절에 별도로 연결한다. 그 이후의 운영 전환·복구 결과는 포함하지 않는다.

| 영향 행 | 현재 소비할 확정 기록 | 유지할 미완료·한계 |
|---|---|---|
| Ansible 코드·증적 공개 | [PR87](https://github.com/321Team/infra-ansible/pull/87) 코드와 [증적PR243](https://github.com/321Team/fds-project-evidence/pull/243) 병합 완료. PR243 exact HEAD adc4f716638bfa5a471b3308b39c1c703722f8c2, merge417dbdec9f0dade9260f95c3894c7df6bc519722. [DOC 수신6234461630](https://github.com/321Team/fds-project-baseline/issues/24#issuecomment-6234461630) 소비 | 185 격리 결과 재사용. 공유 원본17파일 사람 직접 열람·운영 caller/source/config/engine/target 채택·전환/복귀 인수는 별도 |
| MON·Harbor 운영 상태 | [10/17 MON6 HTTP401/ImagePullBackOff 관측6233452581](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-6233452581), 소비처4 전환과 연결. #24 최신 연결은 로컬 R1~R4 보완 완료와 Native/운영 잔여를 구분 | 과거 정상23/23을 현재 health로 사용하지 않음.10/16 Harbor metadata/ID2 표는 당시 이력. 현재 인증·MON 복구는 새 회차 결과를 받은 뒤 해당 행만 갱신 |
| APP·D-07·D02 | [APP 확정 수신6224992618](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-6224992618), APP38/39·D02 수행 인수/MON44 완료 재사용 | D-07 Owner 이재환, 첫 재검토 APP 최종 인수 직전. 코드 무수정·NOT_RUN/운영 DB 제약 NOT_VERIFIED, HTTPS·자동 통보 공백 유지 |
| S08·F2 | [S08 회신6205472774](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-6205472774), MON43 mergee2898851·DOC179 mergeb1db7e6d의 기존 정정/판독·병합 연결 재사용 | 같은 판독 요청 없음. 실제 Silence NOT_RUN, F2 전체 대응와 O01/Freeze 판단 별도 |
| SEC·Grafana | [SEC30 한정 결정6205182638](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6205182638), [Grafana6189715333](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6189715333) 재사용 | AC05 하위 MET와 rotation NOT_MET/RISK_ACCEPTED·전체[ ] 구분. C1 실제 미회전 및 인수 전 사용 기록 검토 유지 |
| 렌더·원본 | [기존 렌더 상태 보충](source-set/RENDER_ADOPTION_ADDENDUM.md)의 논리 배치 제안과 물리 MMD/SVG 채택 권장 | MMD·renderer·SVG bytes 변경 없음. 새 렌더·현재 실행 검증·공식 채택·아키텍처 승인 없음 |

## 2026-10-18 19:00~19:02 제한 관측 연결

관측 구간은19:00:23~19:02:42 KST, 중앙 snapshot 작성은19:07:40 KST다. [관측값·원본 해시·게시 기록](observations/20261018T1902.json)으로 구분한다. 아래 표는 이미 수집된 읽기 결과의 문서 반영이며 DOC가 서버를 새로 조회하거나 시험한 결과가 아니다.

| 대상 | 이번 확정 관측 | 주장하지 않는 범위·후속 |
|---|---|---|
| 가용성 조회 범위 | Linux13/18대, Windows1/8대(SERVER01)의 실행 VM6개 | 전체18 Linux/8 Windows 확인·데이터 무결성·최종 인수 아님 |
| Harbor/Robot | 컨테이너10 running/healthy. 관리자 RUN/HEALTHY·pending0. Robot2·Push3는 DB 메타데이터상 만료, Push3 만료10/18 17:16:55 KST. Robot23은 Pull 전용·11/15 23:39:37 KST까지 기간유효 | Robot23 인증 성공·Worker/Push 소비 성공 미검증. 공급·Native·Robot23 소비처 전환 미실행. 이전 boot의 claim 재사용 불가 |
| K8S/APP/etcd | Node6 Ready, APP6 Ready·모두worker03 배치. etcd3 status/alarm에 보고된 오류·alarm 없음 | Ready를 업무 거래·DB 저장·HA 현재 분산·모든 경로 인수로 확대하지 않음. 기존 HA 인수는 당시 범위로 재사용 |
| K8S MON | monitoring-api4개+monitoring-node3개, 총7개 Not Ready/ImagePullBackOff. 마지막 Pull 오류401. 기존6개에 kube-state-metrics 추가 | Secret 참조·UID/RV만 확인. 비밀값·실제 credential-Robot 대응·단일 실패 원인 미확정. 인증 복구 후7개 실제 Pull·Ready·Probe 확인 잔여 |
| 별도 monitor01 | 사용자 관리자 콘솔 결과: user unit2개 active/exited·Result success·DropInPaths 빈값, receiver/blackbox/nginx3개 실행. 기존 실행기 hash 유지 | 사용자 직접 회신이며 DOC의 독립 원격 수집 아님. K8S MON7 복구·지표 수신·D02 수동통제 전체 이행 완료 아님 |
| DB | 사용자 콘솔19:01:48 KST: unit success/active/running, 읽기rc0, pg_is_in_recovery=false, 현재 DB prepared transaction0 | 전체 DB 무결성·신규 업무 POST/영속화·복구 시험 아님. 기존 DB/DR 인수를 다시 실행하거나 확대하지 않음 |
| 문서·승인 경계 | #24에서 S08 대기1줄 정정, APP39 §5~7 완료 재사용. 중앙은 현재 버전·새 경로·기존 묶음을 문서 PR 준비안으로 선택 | 사람 As-built 최종 채택·DOC/O01/Freeze·Phase1 인수 아님. #25~27 인계 Due/수신은 사용자 판단 대기이며 이 후보가 승인하지 않음 |

근거: [Harbor #13/6248601196](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-6248601196), [MON #17/6248601609](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-6248601609), [DOC #24/6248602308](https://github.com/321Team/fds-project-baseline/issues/24#issuecomment-6248602308), [중앙 #30/6248602739](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6248602739). 댓글 게시19:09~19:10과 서버 관측19:00~19:02는 다른 시각이다. 서버변경·Native·자격증명전환0이며 실제 후속 실행은 이 관측만으로 승인되지 않는다.

## 논리 구성과 실제 범위

| 경로·기능 | 승인 설계 / 실제 확인된 구성 | 증적·차이·한계 / 책임 |
|---|---|---|
| Client→edge→앱 | edge01 `.50` nginx, HTTP80→Worker NodePort30080→transaction-api Service80/target8000 | APP6190096759의169+234+224/228 결합 재사용. 현행 digest Client→edge 새 POST는 없음. 읽은 nginx3파일만 연결, include 전체/모든 정책 실효 동일성 미입증. [D02 최종6208668917](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6208668917)으로 MON 수행 인수·문서 반영 대기는 해소. HTTPS NOT_MET·평문·자동 통보 공백과 기존 한정 조건은 유지. APP 이재환 / 위험 소유 이권욱 |
| transaction-api→engine | 두 서비스 각3 Ready·Worker별 분산은 기존 인수 관측.10/18 19:02 APP6 Ready이나 모두 worker03 배치. 내부 engine8001; API metrics9091/engine9090 분리 | Delivery/Probe 원본·N29/N37. 고정 app source의 `/livez`,`/readyz` 직접 대조. startupProbe는 실제 manifest별 판단. APP 이재환/SEC 이하영 |
| transaction-api→DB | db01 `.55:5432` 저장/조회, engine DB 직접 접근은 정책상 차단 | DB#11 최종6159292006·224 23ID/23행. N42의10/13 API7조회는 NP3/GNP7 형상 동일성이지 새 패킷 허용/거부 시험이 아님. 전체 namespace/모든5xx는 미입증. 이재환/이하영 |
| API 관리 | k8s-api-lb01 `.109:6443` HAProxy TCP TLS passthrough→CP `.102/.103/.104:6443` | N31/N41·StageB backend 제외/복귀·기존#9 종결. 실제 source allowlist/예산 한계는 Runbook 연결. 이권욱 |
| 이미지 공급 | Runner `.20`→Harbor `.54:443` push, Worker `.105/.107/.108` pull/Pod start | CICD AC02/06 기존 인수 소비. Harbor 코드 기술 검토 이후19:02 컨테이너10 healthy를 제한 관측했다. Robot2/Push3 만료·Robot23 기간유효는 메타데이터이며 인증 성공은 미검증이다.10/16 config/imageID 차이의 provenance 판단과 실제 새 회전·소비처 전환은 별도 잔여이며 .50 예외의 기존 한정 회수와 구분. 이하영/이권욱 |
| 자동화 | ansible01 `10.250.10.10`→승인 SSH/관리 경로 | 기존 P1-ANS/O02·CI86 결과 재사용. source `affaad6b1a31d680164d9e3d5ef5d2a9d3fce95a`의 17:09~17:13 격리 컨테이너 LOCAL/MOCK 7묶음 185/185 PASS·회수/부재 확인 완료. 실제 Ansible/module·파일/parser 경로와 모의 서비스/호스트 관측을 구분하며 운영 MON/NTP/SSH 적용 인수는 아님. 코드/증적 병합은10/18 보충의 PR87/243으로 해소됐다. 운영 caller/source/config/engine/targets 채택·전환/복귀는 잔여. 이권욱 |
| 클러스터 MON | monitoring-api Prometheus/Alertmanager/Grafana/KSM, monitoring-node node-exporter; 앱 metrics9091/9090·node9100·kubelet10250 | R10의10/2 구성에19:02 monitoring-api4개/monitoring-node3개 Not Ready·ImagePullBackOff/401 관측을 보충한다. MON 핵심3종 single replica·local PV worker03 고정·Recreate 공백. Prometheus 보존15d/size16GB. N10 MON02 다중 replica 고도화는 P1 우선순위 후속. 이재환 |
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
4. 새 MMD는 승인된 물리 배치와 증적별 논리 차이를 표현한 후보다. 기존 렌더·시각 검토는 완료됐고 전체 As-built 승인은 미결정이다. 중앙의 이번 원천 선택은 문서 PR 준비 범위이며 사람 최종 채택·Freeze가 아니다. 최종 문서 source/version, 변경점의 기존 증적 대응, 남은 미확인/처분을 Lead가 확인해야 한다.
5. 확정된 SEC30/Grafana 조건과 APP 기존 승인은 유지한다. 역할185의 실제 LOCAL/MOCK 실행·회수 공백은 해소됐고 코드/증적 공개는 PR87/243 완료로 대체하고 운영 호출 경로 채택·전환은 별도로 유지한다. D-07 ID·Owner·첫 재검토 확정은 중앙의 로컬 연결 수용까지 소비하며 공식 대장 채택·전체 인수는 별도다. Harbor 컨테이너10 healthy의 제한 관측과 별개인 운영 전환·provenance/현재 인증 미확인, 다른 Known Issue의 미확정 책임/기한, DR02·MON02·Phase2 미완료 범위를 유지한다.
