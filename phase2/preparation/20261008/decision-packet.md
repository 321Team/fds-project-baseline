# Phase 2 결정 입력 — 수용 전 검토안

기준과 실행 경계는 [README](README.md). 현재는 **1차 인수 준비 단계**다. 이번 기록은 설계·일정 변경 승인, 새 AC, 새로운 상시 Support 승인 절차가 아니다. Phase 2 사전 준비를 #33 Start·#34 Freeze·생성 GO로 승격하지 않는다.

## 현재 D23 결정 — 추가 Hybrid DNS 보류

**D23=DEFERRED / 결정자 이권욱 / 결정 접수·기록 2026-10-14 01:35 KST.** 사용자가 D23 설명과 기존 보류 권고에 대해 “보류”로 결정했다. 아래10/13 및10/14 01:09의 DRAFT/PENDING 문구는 결정 전 검토 이력이며 현재 미결 상태로 다시 사용하지 않는다. D22 Registry 결정은 계속 PENDING이다.

- **결정 범위:** 추가 Hybrid DNS 구축을 보류한다. DB `.55`·Harbor `.54`의 기존 IP 연결 기준과 ROSA public API·Route의 실제 DNS 이름/엄격 TLS 사용은 유지한다. DNS 전체 미사용이나 private zone 구축 승인이 아니다.
- **보류 근거:** 현재 public/public 및 Harbor IP 후보에서 추가 Hybrid DNS를 지금 활성화할 구체적 P0 위험 감소 근거가 확인되지 않았다. P0 준비와 Phase 1 인계에 불필요한 변경을 추가하지 않는다. 실제 ROSA DNS/통신 성공을 확인했다는 뜻은 아니다.
- **Owner/재검토:** 이권욱. 기존10/16 D23 점검 시 보류 유지/변경 필요를 확인한다. 그 전에 실제 이름 해석이 P0를 막거나 승인 image host/관리 경로가 바뀌면 영향 구간·최소 구현·비용/일정·원복 조건을 검토한다. 티켓 계획일을 변경하거나 새 상시 승인 절차를 만들지 않는다.
- **#48:** 구현 보류, OPEN 유지. 일시 Deferred를 Cancelled·AC PASS·종결로 처리하지 않는다. 실제 Go 또는 최종 비구현 결정이 생기면 그 결정 범위에 맞춰 별도 기록한다.
- **실행 경계:** DNS/Resolver/hosts·route/SG·공용 OCP·Phase 1 설정 변경0. 이 결정은 실제 Apply/Deploy·ROSA 생성·Gate 인수·정본 발행을 승인하지 않는다.

이번 반영 위치는 기존 준비 PR167의 결정 문서다. #40/#48 이슈 본문·상태·AC·일정 변경, 별도 댓글/알림 전송, PR 병합·정본 발행은 수행하지 않았다.

10-08 후속: [설계 입력 승인](https://github.com/321Team/infra-rosa/issues/3#issuecomment-6054292320)과 [#34 수용](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6054304386)을 수신했다. worker private_a(2a/apne2-az1)·공인 NAT1, fds-app/monitoring-api/ci-cd 및 기본 모니터링 재사용은 설계 방향 수용 상태다. OCM 개인 조직 방향 수용은 billing 연결·팀 접근 완료가 아니며 exact version/N-1/전체 egress·IAM/Freeze는 잔여다. 이후 미결은 이 수용 범위를 반복 요구하지 않는다.

## 1. #34 Freeze: 생성 전 계약 / 생성 후 관측

| 항목 | 지금 받아 고정할 계약 | 이후 관측값 / 기존 생산 책임 |
|---|---|---|
| ROSA 모델·용량 | 지원 HCP version, 1AZ·3대의 subnet key/AZ, platform+APP+교체여유/N-1, disk와 Pod/Service CIDR·host prefix | Cluster/Node IDs·allocatable·실제 version/장애복구는 생성 후. #38 이하영 |
| platform egress | install mode, NAT/endpoint/외부 endpoint·return, API/Ingress Public/Private와 승인 client/Runner | 실제 route/ENI/endpoint ID·TCP 검사 후. Relay EIP를 ROSA 외부통신 충족 근거로 쓰지 않음. #35/#38 |
| IAM | full policy JSON/trust·source SHA·resource/tag/condition·PassRole/backend·회수/실패복구 | 중앙 grant/readback 및 각 본인 MFA/state-lock 이후 사용 가능. #35 이하영→권욱 중앙 |
| Relay | Stream9 후보·공식 Agent, exact Libreswan/repo/HTTP 필요 근거, root volume 보존·삭제/CPU credit, Session document 소유·공급 | 실제 Agent Online/firewalld/SELinux/EBS/세션·SA/경로/복구는 생성 후. #35/#37 |
| 관리/DNS | 아래 3절의 정방향/반환/source·필수 이름/query 권위·ACL·복구 | 실제 경로/IP/Query/strict TLS 관측. #40 권욱 + #35/#37/#38 입력 |
| DB source·security | worker 교체 source-set 생성/폐기 규칙, inventory/forwarding/DB 방화벽·pg_hba/NP 책임, credential reference, 실패 시 STOP·대체자 | 실제 API source·DB ALLOW, engine/비승인 source DENY·교체/복구. #38/#37/#43/#47 |
| Registry | D22 생성 전 trust/경로/principal 계약과 아래 2절 최종 선택 시점 분리 | 생성 후 actual node-source·cold-pull·digest를 Basic Ready 입력으로 확보 → Basic Ready → D22 Final. #38/#42 |

10/08 당시 정확한 용량·IAM JSON·endpoint는 [입력표](input-intake.tsv)에 미결로 남겼고 worker key/AZ는 위 승인으로 부분 수용했다. 이후 수용된 IAM·CA·공급 입력의 현재 상태는 [인수표의 I01~I16 대조](evidence-handoff.md#1014-입력표와-현재-증적의-대조)를 따른다. 과거 추정 sizing, 단일 관측 IP, whole VPC 허용을 자동 채택하지 않는다. 단일 AZ/subnet이 단일 DB source IP를 뜻하지 않는다. source 자동 갱신은 tag만으로 인증하지 않고 cluster/pool/subnet/ENI 대응·실패 시 차단·제한된 변경 범위·원복 조건을 확인한다. 새로운 source controller를 이번에 구현/등록하지 않았다.

## 2. #42 D22: 생성 전 준비와 최종 선택

**권고 후보:** 기존 Harbor 조건부 재사용 + P2 전용 pull-only identity + 승인된 이전 digest 보존. 후보 수용/계정 발급/실제 적용은 미수행이다. Cloud Registry도 아래 같은 기준으로 비교하며 실제 endpoint/credential을 발명하지 않는다.

[10-08 D22 Lead 검토](d22-lead-review.md)에 하영 최신 Primary/Fallback 제안, A 우선 상세화 권고와 B의 배포 중단 영향, 12개 최종 출력, 전환/복귀 조건을 기록했다. VPN 장애의 배포 지속성과 DB 업무 복구를 구분하고 비용 $1 미만·digest 자동 보존·장기 인증을 확정값으로 소비하지 않는다. REGISTRY_MODE/FALLBACK/D22는 PENDING이며 새로운 ECR 자원·권한·복사 승인이 아니다.

| 판단 축 | Harbor 후보 | Cloud Registry 후보 | 결정 시 필요한 것 |
|---|---|---|---|
| 공급 추적 | 승인 APP source→Build/Scan→remote Harbor digest | 같은 source/scan→remote registry digest | 태그 대신 최종 digest, 이전 rollback 이미지 재획득 가능성 |
| 경로/trust | node-pull과 Pod egress 분리, strict FQDN TLS/CA·443/DNS/return | 선택 서비스의 endpoint/egress/trust·pull 인증 | 지원 HCP version의 CA 입력·rollout 영향은 생성 전 확인 |
| actor | Runner push / P2 worker pull 분리 | 최소 push/pull 주체·role/credential 분리 | owner/scope/expiry/reference·회수·안전 전달. Secret 원문 없음 |
| 실패·가용성 | tunnel/Harbor 중단 시 신규 rollout STOP, 정상 workload/이전 digest 보존 | registry/egress/credential 장애 시 같은 경계 | 자동 mirror/rebuild/tag fallback을 새로 승인하지 않음 |
| 비용/일정 | 네트워크·registry 범위를 교육장 리포트와 연결 | 같은 보고 범위·통화/기간으로 연결 | 보고 사용액·예상 총비용, 미수신 NOT_ASSESSED |

10/08 당시 소비 사실: APP `adc90410f99cb7af5b40bc8ff92c45272e9f8bee`의 [Build/Scan 인계](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-6041140607)는 존재한다. 당시 remote Push/승인 digest/ROSA imageID 완료는 아니었다. 새 Push 원본의 앱별 digest는 [D22의 10/14 생산 원본 대조](d22-lead-review.md#1014-생산-원본-대조--앱별-currentprevious)를 현재 입력으로 연결한다. Harbor [가용성 위험 보고](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-6042747313)는 D22 선택의 입력으로만 소비하며 Phase 1 수정·시험·인수는 이번 범위에서 수행하지 않는다.

**생성 전:** 지원 trust 방식/공개 CA·image host(IP/FQDN)·principal/route/source 계약·실패 처리 준비. **생성 후 Basic Ready 판정 전:** 승인된 경로에서 실제 cold-pull·digest 등 #4 handoff 입력을 확보한다. **Basic Ready 후 D22 Final:** 이 결과와 TLS/인증/negative·업무/복구 자료를 소비해 단일 Primary/Fallback·credential owner 및 #43/#46/#47 소비조건을 확정하고 IF-19에 연결한다. 생성 전 actual ROSA cold-pull을 요구하지 않고, Basic Ready에 필요한 경로 준비를 D22 Final 이후로 미루지 않는다. 기존 10-15 Final 목표의 실현 가능성은 G4·실제 운영창과 정합화하며 날짜만으로 GO하지 않는다.

17:40 리뷰 수신: [버전·Pool](https://github.com/321Team/infra-rosa/issues/3#issuecomment-6056067368), [Runner](https://github.com/321Team/infra-rosa/issues/10#issuecomment-6056067704), [CA·경로](https://github.com/321Team/infra-rosa/issues/11#issuecomment-6056068014). 4.22.16·300 GiB·IMDSv2·AutoRepair는 설계 후보이며 전체 Freeze가 아니다. 자발적 업그레이드 미계획과 공급자 필수 업데이트를 구분하고, 하위 minor는 생성 전 재선정 후보로만 다룬다. replicas=3은 목표 대수이며 교체 중 실제 대수 불변을 보장하지 않는다. 기존 4건 보고 정정은 수용했지만 Quota PARTIAL·역할 이름 필터 미발견·ROSA 활성화/청구 연결 미확인은 유지한다. Runner 날짜만을 위한 재시험은 요청하지 않으며 OS/CI/Podman trust·실제 principal의 미확인 구분을 먼저 보완한다.

## 3. #40 관리 경로·DNS 입력 — 10/08 당시 전제

| 경로 | 확인할 원본 | 설계 닫는 조건 |
|---|---|---|
| Runner→local router→vpn-gw→ROSA API | 각 구간 route/get 및 인터페이스·source 선택·return, API private/public 모드 | 현재 selector 밖 관리 출발지를 기존 DB envelope에 포함됐다고 가정하지 않음. 명시한 source/port/return 계약 |
| On-Prem DNS→필수 private name | authoritative zone·선택 Resolver/forward rule, query source, TCP/UDP53, 반환과 loop 방지 | 실제 필요한 최소 zone만. 양방향 전체 DNS 확장과 별개 |
| ROSA node→Registry | node-pull source/DNS/443/TLS와 반환 | Pod DB egress/NetworkPolicy로 node pull까지 검증됐다고 표시하지 않음 |

기존 DNS 원본·TLS 관측을 재사용하고 변화/미확인 구간만 기존 계정으로 읽기 수집한다. 준비 완료 전 route/SG/ACL/selector 변경은 수행하지 않는다. [기존 관리 조회 Runbook](../../runbooks/20261004-local-management-route-readonly.md)을 사용하며 그 실행 위치·권한 범위가 맞지 않으면 STOP한다.

### 10/13 보완: D23 결정에 사용할 문안과 소비 계약

**DRAFT / Lead 이권욱 / 실제 D23 판정 PENDING.** 10/13 17:48 KST 확인한 [Terraform PR29](https://github.com/321Team/infra-terraform/pull/29) HEAD `3079ddcb8712a761c7c1c3fe59189689eb2e38fe`의 public API/public Ingress와 [source 승인](https://github.com/321Team/infra-terraform/pull/29#pullrequestreview-5500767150)을 설계 입력으로 소비한다. 승인된 설계를 다시 묻지 않는다. PR은 당시 OPEN이며 실제 API/Route 호스트·DNS/TLS·클러스터 생성 완료가 아니다. 위 private API 경로/Resolver 표를 현재 필수 구축 목록으로 사용하지 않는다.

**권고 결정 문안(미등록·미확정):** “P0 DB/Registry 연결은 기존 IP Endpoint 기준을 유지한다. ROSA public API와 Route는 실제 발급된 DNS 이름 및 엄격한 TLS 검증을 사용한다. 전체 Hybrid DNS는 P1 조건부이며 P0 위험을 줄이는 구체적 필요와 구현 여유가 확인될 때만 Go로 결정한다. 현재는 추가 구현을 보류하고 10/16 D23 판단 때 최종 선택한다. IP 유지로 구현하지 않기로 최종 결정하면 #48의 Cancelled 근거를 남기며, Deferred를 완료/Cancelled로 대체하지 않는다.”

| 소비 경로 | 지금 고정할 기준 | 아직 필요한 실제 입력 / 생산 책임 | 실패 시 처리 |
|---|---|---|---|
| Runner → ROSA API | public/public 승인, 실제 API DNS 이름·승인 CA·identity 사용 | API URL/CA/identity·Runner의 DNS/443 접근 receipt: #38 이하영 → #46 이권욱 | 이름/TLS/identity 불일치면 배포 STOP. 임의 IP/hosts·검증 해제로 우회하지 않음 |
| 사용자/시험기 → Route | 실제 Route host와 TLS를 app/render 계약에 결속 | transaction-api의 `transaction-api-api`·`transaction-api-readyz` 두 Route가 공유하는 승인 host 1개: #38/#43 이하영·이재환 → #46/#47 | PENDING host이면 실행 입력 생성 STOP. engine·metrics용 외부 Route를 추가하지 않으며 public Ingress가 DB 공개를 뜻하지 않음 |
| ROSA APP → DB | DB `10.1.93.55`, 승인 VPN/source/포트 계약 | #37/#47 실제 승인 source·ALLOW/비승인 DENY·원복 결과: 이재환 | 통신 실패를 DNS 변경으로 해결했다고 가정하지 않음. DB runtime 예외의 정확한 범위만 적용 |
| ROSA node → Harbor | P0 IP `10.1.93.54`; 실제 image host와 CA key/SAN 일치 | #42가 선택할 실제 image reference·pull principal·node 경로: 이하영·이재환 | IP 기반 이미지와 FQDN 기반 이미지를 자동 치환하지 않음. TLS/pull 실패면 신규 rollout STOP |
| Hybrid DNS 확장 | D23 Go일 때만 #48 착수 | 최소 권위 zone/query source·TCP/UDP53·return·loop 방지·원복: 이권욱, 경로 입력 이하영·이재환 | 기존 DNS 설정 보존. 새 규칙 원복 범위가 없으면 실행하지 않음 |

`fds-app`이 소비 namespace이며 `rosa-app`은 overlay 이름이다. #46 댓글의 표기 차이를 namespace 변경 승인으로 사용하지 않는다. API/Route 이름은 아직 수신하지 않은 값을 생성하지 않는다. Harbor CA/경로의 이미 접수된 입력은 [D22 보완](d22-lead-review.md)을 재사용한다.

10/13 18:45 정합성 검토: Route 대상은 [fds-msa 병합 계약](https://github.com/321Team/fds-msa/blob/6e7acf1053b1e44164d38851e477a2d2d64b9c3a/deploy/delivery/rosa.yaml)의 객체명과 대조했다. 이전 초안의 “API·engine Route host”를 위 두 transaction-api Route로 정정한 문서 변경이며 앱 객체·권한·승인 host 실제값을 변경하지 않는다. PR29는 18:29:11 KST merge `bd3b79c681d580cfceba31d6c62844727c5aeef8`로 병합됐고, 위 17:48 OPEN 표기는 당시 이력이다. 병합을 ROSA 생성/Runtime 완료로 소비하지 않는다.

| 후속 결정 | 권장 담당·기한 / 실제 확정 여부 | 완료조건·재검토 계기 |
|---|---|---|
| D23 단일 선택 | 이권욱 / 기존 10/16 목표, 현재 PENDING | P0 IP 유지와 P1 Go/No-Go/Deferred 이유를 #40에 하나로 연결; #45/#47 소비값 일치 |
| #48 비구현 처리 | 이권욱 / D23 결정 직후, 권장 순서 | 최종 IP 유지 선택이면 기존 AC에 맞는 Cancelled 근거. 일시 보류면 Owner·다음 검토 시점 명시; 지금 상태 자동 변경 없음 |
| Deferred 재검토 | 이권욱 / 10/16 이후에는 필요 발생 시, 제안 | 실제 이름 해석 실패가 P0를 막거나 승인 image host가 바뀔 때 영향 구간만 검토. 새 비용/일정 영향은 중앙 판단 |
| DNS Go 시 인수 | #48 이권욱 / Go 후 실행창 별도 | 승인·미승인 Query, UDP/TCP53, 장애·복구 결과. 기존 52/53 자료는 변경 없는 부분에 재사용 |

현재 단계는 결정 준비다. 실제 DNS/hosts/Resolver·공용 OCP·DNS/LB 설정 변경이나 전체 DNS 시험을 요구하지 않는다. 나중에 Go가 되면 실제 선택 구성에 대한 실행/복구안을 별도로 고정한다.

### 10/14 D23 선택 직전 대조 — Phase 1 변경 없이 닫는 범위

[이번 작업 경계](phase-boundary-20261014.md)에 따라 위 단일 권고를 유지한다. **추가 Hybrid DNS Deferred 권고 / 실제 Lead 결정 PENDING**이다. public API/Ingress 설계 재승인, DNS/hosts 설정 변경, #48 상태 변경은 수행하지 않았다.

| 선택 입력 | 기존 자료로 준비할 수 있는 것 | 확정 전 남은 것 / 완료조건 |
|---|---|---|
| P0 IP 유지 | DB·Harbor의 기존 endpoint와 승인 경로/TLS 계약 연결. 기존 Phase 1 DNS/CA를 바꾸지 않음 | 하영·재환이 전달할 actual ROSA 경로·image host가 기존 계약과 맞는지 권욱이 소비. 새 호스트명을 임의 생성하지 않음 |
| public API/Route | public/public 병합 source와 두 transaction-api Route의 host1개 계약 | 실제 API/Route DNS·CA·namespace UID 수신 후 동일 source/render에 결속. 아직 없다는 이유로 임시 IP/hosts 우회 금지 |
| 추가 DNS 보류 | P0가 추가 Resolver 없이 진행 가능한 단일안과 실패 시 STOP/재검토 trigger | 권욱의 D23 최종 선택·이유·Owner/재검토 조건. 단순 Deferred이면 #48 Cancelled로 바꾸지 않음 |
| 추가 DNS Go가 필요해지는 경우 | 기존 권위 zone/허용·거부 query/반환·복구 기준 재사용 | 실제 P0 차단 근거와 변경할 최소 zone/source, 비용·일정 영향 및 실행/원복 범위가 구체화된 뒤 별도 판단 |

결정 기록의 `날짜·결정자·선택·이유·적용 경로·변경할 설정 유무·#48 처리·재검토 trigger`는 하나의 D23에 연결한다. 이번에는 선택 제안과 확인 필요를 준비했으며 실제 승인값/회의 기록을 생성하지 않았다. 조건부 항목의 P1 표기는 **우선순위**이고 Phase 1 작업 범위를 뜻하지 않는다.

### 10/14 D23 AC 대조 결과와 결정용 필드

01:09 KST [#40](https://github.com/321Team/fds-project-baseline/issues/40)·[#48](https://github.com/321Team/fds-project-baseline/issues/48)의 현행 Decision Contract/AC와 위 문안을 대조했다. **설계 수준에서 추가 Hybrid DNS를 지금 활성화해야 하는 새 근거는 확인되지 않았다.** 실제 ROSA 이름 해석/통신 성공을 검증했다는 뜻은 아니다. 권고는 기존 Deferred 하나로 유지한다.

| 결정용 필드 | 검토가 끝난 제안 / 남은 사람의 결정 |
|---|---|
| P0 정책 | DB `.55`·Harbor `.54`의 IP 경로 유지. public API/Route는 플랫폼이 실제 발급한 DNS 이름과 엄격 TLS. “전체 endpoint를 IP로 통일”하는 결정이 아님 |
| 추가 Hybrid DNS | Deferred 권고. 구체적 P0 위험 감소 근거·capacity가 확보된 경우에만 Go 재검토 |
| 이유·변경 영향 | 현재 public/public과 Harbor IP 후보는 private zone 확장을 자동 요구하지 않음. Resolver/forward rule/hosts·기존 Phase 1 DNS 설정의 이번 변경0 |
| Owner / Due | 기존 Lead 이권욱 / 기존10/16 D23 단일 결정 목표 유지. 일시 Deferred의 후속 Due를 없애지 않음 |
| #48 처리 | 현재 OPEN 유지. 일시 Deferred는 Cancelled/AC PASS가 아님. 최종 IP 유지로 구현 취소를 결정할 때만 기존 AC에 따른 Cancelled 근거를 별도로 남김 |
| Go가 되는 경우 | 최소 권위 zone·query source·정방향/반환·UDP/TCP53·허용/거부/NXDOMAIN·장애복구 범위를 선택 구성에 한정해 준비. Reverse/PTR 자동 추가 없음 |
| 아직 없는 실제값 | ROSA API/Route/namespace UID 및 실제 DNS/TLS 관측은 생성 후 소비 입력. 이를 임의로 채우거나 Deferred 결정 준비의 선행 Runtime으로 요구하지 않음 |
| 판정 기록 | `D23=PENDING`, `DECISION_DATE=PENDING`, `APPROVED_BY=PENDING`. 이번 착수는 검토 실행이며 최종 선택 등록·AC 수용·일정 변경이 아님 |

[#40의 AC](https://github.com/321Team/fds-project-baseline/issues/40)는 단일안 승인·적용 시 Query/Test 정의·미적용 근거 기록이다. 이 문서로 비교/영향/미적용 근거의 검토 준비를 닫고, Lead의 실제 선택 기록만 별도 남긴다. #48 구현 시험과 실제 ROSA 통신을 D23 사전 검토 완료에 끌어오지 않는다.

## 4. #43 앱/시험 DB 단계안

기존 [리뷰 6041356020](https://github.com/321Team/fds-project-baseline/issues/43#issuecomment-6041356020)를 구현 PR에서 확인한다. 권고 위치는 fds-msa/deploy의 base/components/overlays, 플랫폼 Namespace/RBAC/NP 실제 소유는 #38과 충돌하지 않아야 한다.

- base: 앱 2개·Service·Secret reference·SA·SecurityContext·probe·digest 변수. 최신 source/render/live 비교와 허용 차이 명시.
- Lab: 선택형 namespace-local 시험 DB, arbitrary UID·Ready·health·Rule 검증. 허용 자원만 정리.
- ROSA #43: 임시 시험 DB 사용 시 그 사실과 데이터 격리/수명/Secret 정리를 명시. #47 On-Prem DB 전환 전에 복구 가능한 이전 상태·데이터 처분/중복 방지·검증 fixture를 고정.
- 외부 Route는 API만, engine과 metrics 비노출 확인. 시험 DB 성공을 Hybrid DB 인수로 표현하지 않음. 실제 DB role/schema/credential 생성·전환은 이번에 하지 않음.

## 5. #47→#50 일정·handoff 결정안

생성/삭제·보존·Review는 [이벤트 기준 작업창과 인계](lifecycle-review-preparation.md)를 사용한다. 10/23 정리 목표를 Review 전 자동 삭제로 해석하지 않으며 exact 시각/참석자는 미정이다.

**10/20 준비·10/21 H1 뒤 본시험·10/22 회귀의 구성은 PMO/QA 동의, 실제 실행은 보완 대기다.** [생산자 작업창](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6051395052)과 [PARTIAL ACCEPT / 실행 전 CHANGES REQUIRED](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6051518639)를 수신했다. 정확한 시각은 제출 계획이며 Runtime GO·본문/날짜 필드 변경과 구분한다.

| 날짜 | 제안 실행 구간 | 진입/중단/출력 |
|---|---|---|
| 10-20 | #50 준비, G5 입력 및 fixture/source/원본 수집·복구 확인 | #47 handoff 전 Hybrid Runtime 시험으로 계산하지 않음 |
| 10-21 | #47 필수 검증·handoff 먼저, 그 뒤 #50 본 시험 | actual Cluster/Namespace/App digest/schema·DB 승인 source/route·API 저장/조회·engine/비승인 DENY·선택 Registry/D22/D23·원본 링크 전체 고정. 필수 미충족이면 전환 STOP |
| 10-22 | 최종 회귀·원본 확정 | 결함 수정으로 source/환경이 바뀐 영향 범위 재시험. 미실행은 NOT_RUN, 미해결은 Gate 판단 입력 |
| 10-23 | 집계/Freeze/Review | 신규 대규모 시험을 자동 추가하지 않음 |

생산자는 10/21 12:00~12:30 H1, 이후 #50 본시험 등을 제안했다. H1 미충족이면 그 시각이 되어도 시험을 시작하지 않는다. [최신 실행 준비](execution-readiness-update.md)에서 도구 PR24 R1~R4 해소·승인·병합 수신을 확인했다. 장애 패킷 F1/F2 보완과 실제 진입조건은 계속 확인해야 한다. Working Test Plan은 이 수용 범위를 반영하며 Issue 본문/날짜 필드는 이번에 변경하지 않는다. 이 구성을 Runtime GO나 Gate 인수로 표시하지 않는다.
