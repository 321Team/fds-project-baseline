# Phase 2 결정 입력 — 수용 전 검토안

기준과 실행 경계는 [README](README.md). 이번 기록은 설계·일정 변경 승인, 새 AC, 새로운 상시 Support 승인 절차가 아니다.

## 1. #34 Freeze: 생성 전 계약 / 생성 후 관측

| 항목 | 지금 받아 고정할 계약 | 이후 관측값 / 기존 생산 책임 |
|---|---|---|
| ROSA 모델·용량 | 지원 HCP version, 1AZ·3대의 subnet key/AZ, platform+APP+교체여유/N-1, disk와 Pod/Service CIDR·host prefix | Cluster/Node IDs·allocatable·실제 version/장애복구는 생성 후. #38 이하영 |
| platform egress | install mode, NAT/endpoint/외부 endpoint·return, API/Ingress Public/Private와 승인 client/Runner | 실제 route/ENI/endpoint ID·TCP 검사 후. Relay EIP를 ROSA 외부통신 충족 근거로 쓰지 않음. #35/#38 |
| IAM | full policy JSON/trust·source SHA·resource/tag/condition·PassRole/backend·회수/실패복구 | 중앙 grant/readback 및 각 본인 MFA/state-lock 이후 사용 가능. #35 이하영→권욱 중앙 |
| Relay | Stream9 후보·공식 Agent, exact Libreswan/repo/HTTP 필요 근거, root volume 보존·삭제/CPU credit, Session document 소유·공급 | 실제 Agent Online/firewalld/SELinux/EBS/세션·SA/경로/복구는 생성 후. #35/#37 |
| 관리/DNS | 아래 3절의 정방향/반환/source·필수 이름/query 권위·ACL·복구 | 실제 경로/IP/Query/strict TLS 관측. #40 권욱 + #35/#37/#38 입력 |
| DB source·security | worker 교체 source-set 생성/폐기 규칙, inventory/forwarding/DB 방화벽·pg_hba/NP 책임, credential reference, 실패 시 STOP·대체자 | 실제 API source·DB ALLOW, engine/비승인 source DENY·교체/복구. #38/#37/#43/#47 |
| Registry | D22 생성 전 trust/경로/principal 계약과 아래 2절 최종 선택 시점 분리 | actual node-source·cold-pull·digest/Ready는 Basic Ready 이후. #42 |

정확한 숫자·IAM JSON·worker key·endpoint는 [입력표](input-intake.tsv)에 PENDING으로 남겼다. 과거 추정 sizing, 단일 관측 IP, whole VPC 허용을 자동 채택하지 않는다. source 자동 갱신은 tag만으로 인증하지 않고 cluster/pool/subnet/ENI 대응·실패 시 차단·제한된 변경 범위·원복 조건을 확인한다. 새로운 source controller를 이번에 구현/등록하지 않았다.

## 2. #42 D22: 생성 전 준비와 최종 선택

**권고 후보:** 기존 Harbor 조건부 재사용 + P2 전용 pull-only identity + 승인된 이전 digest 보존. 후보 수용/계정 발급/실제 적용은 미수행이다. Cloud Registry도 아래 같은 기준으로 비교하며 실제 endpoint/credential을 발명하지 않는다.

| 판단 축 | Harbor 후보 | Cloud Registry 후보 | 결정 시 필요한 것 |
|---|---|---|---|
| 공급 추적 | 승인 APP source→Build/Scan→remote Harbor digest | 같은 source/scan→remote registry digest | 태그 대신 최종 digest, 이전 rollback 이미지 재획득 가능성 |
| 경로/trust | node-pull과 Pod egress 분리, strict FQDN TLS/CA·443/DNS/return | 선택 서비스의 endpoint/egress/trust·pull 인증 | 지원 HCP version의 CA 입력·rollout 영향은 생성 전 확인 |
| actor | Runner push / P2 worker pull 분리 | 최소 push/pull 주체·role/credential 분리 | owner/scope/expiry/reference·회수·안전 전달. Secret 원문 없음 |
| 실패·가용성 | tunnel/Harbor 중단 시 신규 rollout STOP, 정상 workload/이전 digest 보존 | registry/egress/credential 장애 시 같은 경계 | 자동 mirror/rebuild/tag fallback을 새로 승인하지 않음 |
| 비용/일정 | 네트워크·registry 범위를 교육장 리포트와 연결 | 같은 보고 범위·통화/기간으로 연결 | 보고 사용액·예상 총비용, 미수신 NOT_ASSESSED |

최신 소비 사실: APP `adc90410f99cb7af5b40bc8ff92c45272e9f8bee`의 [Build/Scan 인계](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-6041140607)는 존재한다. remote Push/승인 digest/ROSA imageID 완료는 아니다. Harbor [가용성 위험 보고](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-6042747313)는 D22 선택의 입력으로만 소비하며 Phase 1 수정·시험·인수는 이번 범위에서 수행하지 않는다.

**생성 전:** 지원 trust 방식/공개 CA·FQDN·principal/route/source 계약·실패 처리 준비. **Basic Ready 후 기존 10-15 Final 목표:** actual TLS/인증/negative/cold-pull·업무/복구 자료로 단일 Primary/Fallback·credential owner 및 #43/#46/#47 소비조건을 확정하고 IF-19에 연결한다. 생성 전 actual ROSA cold-pull을 요구하지 않는다.

## 3. #40 관리 경로·DNS 입력

| 경로 | 확인할 원본 | 설계 닫는 조건 |
|---|---|---|
| Runner→local router→vpn-gw→ROSA API | 각 구간 route/get 및 인터페이스·source 선택·return, API private/public 모드 | 현재 selector 밖 관리 출발지를 기존 DB envelope에 포함됐다고 가정하지 않음. 명시한 source/port/return 계약 |
| On-Prem DNS→필수 private name | authoritative zone·선택 Resolver/forward rule, query source, TCP/UDP53, 반환과 loop 방지 | 실제 필요한 최소 zone만. 양방향 전체 DNS 확장과 별개 |
| ROSA node→Registry | node-pull source/DNS/443/TLS와 반환 | Pod DB egress/NetworkPolicy로 node pull까지 검증됐다고 표시하지 않음 |

기존 DNS 원본·TLS 관측을 재사용하고 변화/미확인 구간만 기존 계정으로 읽기 수집한다. 준비 완료 전 route/SG/ACL/selector 변경은 수행하지 않는다. [기존 관리 조회 Runbook](../../runbooks/20261004-local-management-route-readonly.md)을 사용하며 그 실행 위치·권한 범위가 맞지 않으면 STOP한다.

## 4. #43 앱/시험 DB 단계안

기존 [리뷰 6041356020](https://github.com/321Team/fds-project-baseline/issues/43#issuecomment-6041356020)를 구현 PR에서 확인한다. 권고 위치는 fds-msa/deploy의 base/components/overlays, 플랫폼 Namespace/RBAC/NP 실제 소유는 #38과 충돌하지 않아야 한다.

- base: 앱 2개·Service·Secret reference·SA·SecurityContext·probe·digest 변수. 최신 source/render/live 비교와 허용 차이 명시.
- Lab: 선택형 namespace-local 시험 DB, arbitrary UID·Ready·health·Rule 검증. 허용 자원만 정리.
- ROSA #43: 임시 시험 DB 사용 시 그 사실과 데이터 격리/수명/Secret 정리를 명시. #47 On-Prem DB 전환 전에 복구 가능한 이전 상태·데이터 처분/중복 방지·검증 fixture를 고정.
- 외부 Route는 API만, engine과 metrics 비노출 확인. 시험 DB 성공을 Hybrid DB 인수로 표현하지 않음. 실제 DB role/schema/credential 생성·전환은 이번에 하지 않음.

## 5. #47→#50 일정·handoff 결정안

**10/20 준비·10/21 H1 뒤 본시험·10/22 회귀의 구성은 PMO/QA 동의, 실제 실행은 보완 대기다.** [생산자 작업창](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6051395052)과 [PARTIAL ACCEPT / 실행 전 CHANGES REQUIRED](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-6051518639)를 수신했다. 정확한 시각은 제출 계획이며 Runtime GO·본문/날짜 필드 변경과 구분한다.

| 날짜 | 제안 실행 구간 | 진입/중단/출력 |
|---|---|---|
| 10-20 | #50 준비, G5 입력 및 fixture/source/원본 수집·복구 확인 | #47 handoff 전 Hybrid Runtime 시험으로 계산하지 않음 |
| 10-21 | #47 필수 검증·handoff 먼저, 그 뒤 #50 본 시험 | actual Cluster/Namespace/App digest/schema·DB 승인 source/route·API 저장/조회·engine/비승인 DENY·선택 Registry/D22/D23·원본 링크 전체 고정. 필수 미충족이면 전환 STOP |
| 10-22 | 최종 회귀·원본 확정 | 결함 수정으로 source/환경이 바뀐 영향 범위 재시험. 미실행은 NOT_RUN, 미해결은 Gate 판단 입력 |
| 10-23 | 집계/Freeze/Review | 신규 대규모 시험을 자동 추가하지 않음 |

생산자는 10/21 12:00~12:30 H1, 이후 #50 본시험 등을 제안했다. H1 미충족이면 그 시각이 되어도 시험을 시작하지 않는다. [최신 실행 준비](execution-readiness-update.md)의 도구 PR24 R4·장애 패킷 보완을 수신하고 실제 진입조건을 확인해야 한다. Working Test Plan은 이 수용 범위를 반영하며 Issue 본문/날짜 필드는 이번에 변경하지 않는다. 이 구성을 Runtime GO나 Gate 인수로 표시하지 않는다.
