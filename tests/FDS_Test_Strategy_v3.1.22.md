# FDS Test Strategy v3.1.22

문서 버전 **v3.1.22 / RELEASED after reviewed finalization merge**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

기존 TS01~16와 승인된 기능224/실패233/부하228/HA221/DB11/DR21의 인수 범위를 재사용한다. 전략 내용은 기존 v3.1.21 기반이며 새 시험/AC를 추가하지 않는다.

## 기존 전략 원문과 범위

# FDS v3.1.21 테스트 전략 재검토

기준: 2026-10-03 수집본, baseline PR112 `226959ac0c5d3dcf79109ba8b914c18bcbab3c0c`, architecture PR8 `c421733e702c8923e26f6788fd8ade5e8657badf`. 문서 갱신이며 실행·AC 인수 아님. 기존 9/30 전략의 W0~W3 및 10/23 teardown 구조를 유지하고 아래 정정을 우선 적용한다.

## 판정과 정정

전략 방향은 유지하되, 생성 전/후 Gate와 증적 재사용 경계를 수정한다. D21은 FINAL이다. #119는 Done이며 DB 장애와 engine 장애의 기대값을 구분한다. #125의 backup/rollback P1 유지 및 preventive rotation NOT MET/RISK ACCEPTED, #130의 HBR 05A/05B와 #16 생산·#13 인수 구조를 테스트 추적에 반영한다. #126/#127/#128은 철회/거절 이력이며 AC 변경 입력으로 사용하지 않는다.

1. **생성 전 준비:** 승인 사양·지원 버전/수량·quota/IAM/OIDC/계정·backend·검토된 plan·관리 경로/DNS·Registry 논리 계약·capacity/cost·원복 절차를 확인한다. PG 항목별 설계 적합성과 실행 준비를 판정한다. 생성 후에만 얻을 actual IDs/Running/Ready/E2E 결과를 생성 전 PASS 조건으로 요구하지 않는다.
2. **생성 후 인수:** actual endpoint/ID/source와 적용 SHA/digest를 결박하고 각 Runtime AC를 실행한다. LAB이나 MOCK으로 ROSA Runtime을 대신하지 않는다. 미실행은 NOT RUN으로 유지한다.
3. **W0 접근 지연:** Shared OCP 접근이 늦으면 local/static을 진행하고 actual UID 검증을 승인된 W2 최초 구간으로 이관한다. ROSA 앱 인수 전에 반드시 실행한다. Shared OCP의 미실행 자체를 전체 설계의 무조건 차단으로 추가하지 않는다.
4. **중복 수집 절감:** 동일 환경·SHA/digest·설정·회차·판정 조건인 원본만 재사용한다. #16→#13 동일 Review Run 4/4 패키지 공유는 허용하지만 소비자의 인수는 별도 기록한다. 수정 영향 범위에만 재시험하되 security negative/recovery를 비용 때문에 생략하지 않는다.
5. **비용:** 최신 교육장 한도·기간·매일 리포트와 자원별 total-to-complete를 사용한다. 기존 400/450/500 입력은 교육장 한도와의 관계 미확정으로 기록한다. 임의 숫자 대체·미조회 금액 0·별도 Billing 관리자 권한 요구를 하지 않는다. 신규 실행 전에 적용 한도와 잔여 가동시간을 확정한다.

## 실행 창과 선행조건

| Window | 계획 목표 | 실행 책임 | Entry / Exit |
|---|---|---|---|
| P1 Close 준비 | 10/6 심사 전 | 각 P1 Lead / #30 이권욱 | #15 endpoint 보장·#16 Delivery·#19 rollback 잔여를 실제 증적 또는 Known Issue로 인계. 시험 변경창은 별도 조건 충족. Close 결과 미작성 |
| W0 | 10/8까지 선검증, 미완 actual은 W2 첫 구간 | #38 이하영 / #43 이재환 | source·base/overlay·mock·LAB 허용 범위. 실제 UID/Ready/업무·cleanup을 얻기 전 PG03 Runtime PASS 금지 |
| W1 | 10/7~14 | #34 이권욱 / #35 이하영 / #37 이재환 | D21 FINAL → 계약 Freeze → Stage-A → VPN. 읽기 전용 준비 병행. Freeze·계정·검토 plan·비용 조건 후 유료 생성 |
| W2 | 10/14~20, #38 본 작업 10/15~19 | #38 이하영 → #43 이재환 → #46 이권욱 | actual platform → 앱 → 정상 delivery/실패차단. 단일 승인 cluster/digest·회차를 연결 |
| W3 | 10/20~22 | #47/#50 이재환, 각 통제 Lead | 동일 ROSA에서 Hybrid → 정상/Rule → negative → 장애/복구 → 최종 회귀. 10/20 path 준비·10/21 본 시험·10/22 회귀는 내부 실행 목표 |
| 종료 | 10/23, 10/26 Evidence Close | #49/#55/#57 해당 Lead | 원본·해시·비용·inventory 보존 후 teardown 및 실제 삭제 확인. 별도 승인 live demo 없으면 새 시험/유지 없음 |

W1~W3의 내부 창은 티켓의 Start/End·AC·권한을 변경하지 않는다. #34 목표 10/8과 #43 pre-Freeze 입력 checkpoint 제안 10/12 18:00은 충돌하므로 채택하지 않는다. 용량 입력의 상대 기한은 **최초 Freeze 심사 전**이다. 정확 제출일은 Leads가 정렬하며 일정 목표를 자동 순연하지 않는다. D22는 생성 전 논리 trust/digest/fallback 계약과 Basic Ready 이후 actual cold-pull 인수를 분리한다. D23 전체 P1 범위와 private 접근에 필수인 DNS subset을 구분한다.

## 테스트·증적 추적표

아래 ID는 문서 내 검토 항목이며 새 AC나 티켓을 발급한 것이 아니다. 실제 인수는 연결된 원본 AC/Decision을 따른다.

| ID | 책임/원본 | 환경·시점 | 성공 / 실패·중단 조건 | 필수 증적 / 현재 |
|---|---|---|---|---|
| TS01 | #34/#35/#38 | 생성 전 | supported version/type/AZ/pool·CIDR·quota·계정·계약 완비. 미확인 값 적용 금지 | read-only 원본/command RC/source SHA, plan. HOLD |
| TS02 | #38/#43 | LAB 선검증 → ROSA 인수 | 승인 digest, restricted-v2 arbitrary UID, non-root/RO rootfs/probe/Ready/업무. broad SCC·root 우회 금지 | effective UID/GID/SCC/imageID·write paths·cleanup. actual NOT RUN |
| TS03 | #34/#38/#43 | Freeze 전 모델 / 생성 후 관측 | P1 live requests/limits·platform·surge·N-1 allocatable 수용. missing=0 금지, AZ고정 PVC 복구경로 | live sanitized inventory/LimitRange/Quota/PVC, 계산·drain/replacement 판정. HOLD |
| TS04 | #35/#37/#38/#40 | 생성 전 tuple / W1~W2 | 승인 관리 source·양방향 route/DNS/TLS/API 접근, 비승인 source·잘못된 CA 거부 | actual DNS FQDN/SAN/SG·port/return route; resolver loop/장애/복구. NOT RUN |
| TS05 | #36/#37 | D21 수집 / W1 실증 | 최종 raw 수신hash 일치와 cleanup. 실제 Child SA는 별도 인증 시험. mismatch-PSK pathcheck를 tunnel PASS로 사용 금지 | final responder 8706B/e5f754a3…45cb0, initiator/cleanup, manifest. HOLD_RAW_INTAKE |
| TS06 | #37 | production VPN, 승인 창 | 정상 SA·DB path·return route. SA-down/plaintext/미허용 source·port 차단. dynamic public source 장시간·rekey·DPD·rebuild 복구 | 양쪽 SA/route/FORWARD·fresh connections·시간·RC/원복. NOT RUN |
| TS07 | #38/#47 | 모델 Freeze / W3 | 승인 최소 source 집합·권한/SLA, replacement 중 동기화·미분류 fail-closed, engine DB DENY | inventory provenance/전후 diff/실제 DB source/정책 union/복구. 모델 미확정 |
| TS08 | #13/#16/#42/#47 | P1 delivery / ROSA cold-pull | CA/SAN 검증·pull-only·push 분리·immutable digest·cold/replacement pull. anonymous/pull-principal push 거부 | trust chain/권한·Harbor artifact/imageID, CA rollout 영향·복구. TLS/allowlist/audience 잔여 |
| TS09 | #16/#46 → #13 | 동일 Review Run | 정상 Test→Build→Scan→Push→Deploy→Health와 4/4 digest 일치. 고의 Test/Scan 실패 시 deploy 차단 | source/scan/manifest/artifact/runtime imageID, 실패 RC. P1 delivery NOT VERIFIED |
| TS10 | #16/#46/#13 | 승인 rollback 창 | 이전 승인 digest가 신규와 다름, 실제 이전 workload 복귀·Harbor/worker 인수. 동일 digest/미검증 입력 BLOCK | 이전/신규digest·revision·probe·rollback·소비자 회신. NOT RUN |
| TS11 | #43/#47/#50 | W2 smoke / W3 | 정상 거래·R01/R02/R04/R07 기대 응답과 DB row/Rule trace 일치. HTTP200 단독 PASS 금지 | Transaction ID 연결, 고정 fixture·KST 경계/history 분리·schema revision. ROSA NOT RUN |
| TS12 | #119/#15/#20/#50 | 승인 장애 창 | DB 장애 /readyz503·Endpoint 제외. engine 장애 API Ready·HTTP201·skipped=true·DB 저장. 복구 후 회귀 | 장애/복구 명령·RC/replicas·API·DB row·metric delta. #119 Done, ROSA NOT RUN |
| TS13 | #19/#125 | P1 승인 변경창 | v2 4 blockers 해소 후 재심사. restart identity/critical failure 누적/exact LB/모든 경로 cleanup 필수 | script SHA·negative fixture·3CP baseline·원복hash. 변경창 HOLD, rollback NOT MET |
| TS14 | #38/#44/#47/#50 | 설계 mapping / actual 복구 | 관리형 encryption/Secret 권한·expiry·backup/recovery·관측 동등성. root disk 암호화=Secret 인수 아님 | source/reference만 수집, secret 원문 제외. Receiver 없는 P2 승계 완료 금지 |
| TS15 | #37/#38/#47/#50 | 승인 복합장애 창 | worker 교체+Relay 장애 후 DB·cold-pull·DNS·업무 복구. AZ고정 PVC 제약/RPO-RTO 준수 | 순서/시간/정책·inventory·data diff. 실패영향 내 중단·원상복구. NOT RUN |
| TS16 | #49/#55/#57 | 10/23 | 증적 보존 후 cluster/NAT/EIP/ENI/LB/endpoint/EBS 잔여와 비용 확인 | 삭제 전후 inventory·비용data source·hash·미삭제owner. NOT RUN |

## 실행·중단·재시험 공통 규칙

각 Runtime Window 시작 전에 대상 환경/호스트·계정·권한·작업경로, 명령·source SHA/digest, AC/기대값, 변경 전 상태, 승인 작업창·단일 장애주입 실행자, 중단 기준·원복 명령·확인자를 해당 runbook에 고정한다. 이 전략은 실행 명령 또는 서버 적용 승인을 대체하지 않는다. 승인되지 않은 source/selector/NAT·TLS 검증 해제·SELinux/방화벽 완화로 시험을 통과시키지 않는다.

실패 시 신규 변경을 멈추고 검토된 절차로 원복·health/정책/잔여 Secret·자원을 확인한다. Failure → 가설/원인 → 변경 SHA 또는 일시오류 재시도 사유 → STATIC/MOCK/LAB → 영향 Runtime 재시험 순서를 따른다. 동일 시험 반복을 인수 대신 누적하지 않는다. DB 공유 시험은 전용 fixture/ID namespace·mutation 창과 정리/보존 정책으로 P1/P2 오염을 방지한다.

증적 체인: source/입력 revision → rendered manifest/plan → image digest/actual imageID → case/transaction/schema → command/RC/raw → 수신hash/secret scan/manifest → 필요한 독립 review → 승인된 편입·발행. 수집 시각(KST), 환경, 생산자/소비자, 성공과 미실행 범위를 기록한다. Summary/hash만으로 AC PASS를 만들지 않는다.

## 검토 근거와 한계

- 기존 승인 전략: `audit/phase2-test-strategy-20260930/README.md` 및 runtime-window-plan.json.
- 현재 잔여 증적: `audit/canonical-hold-recheck-20261003-1955/sources.json`과 README.
- 최신 설계 후보: architecture PR8 c421733 revision2. topology/source/비용 후보는 미승인으로 보존한다.
- 현재 78 Issue 본문은 이번 발행 준비에서 재조회해 source hash와 함께 기록한다. 과거 보관 본문과 최신 결정 충돌은 최신 명시적 disposition을 우선 표시하며 원문을 보존한다.
- STATIC 전략 검토만 수행. MOCK/CI/RUNTIME 신규 실행은 이 문서 작성으로 수행되지 않았다. P1 Close 및 Architecture Freeze가 HOLD여도 현 상태를 정확히 기록한 계획 베이스라인의 발행과는 별개다. 발행 자체의 무결성·독립 코드 리뷰 Gate는 충족해야 한다.
