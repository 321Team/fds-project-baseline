# #34 Architecture Freeze — 통합 사양 검토안

기준 시각: 2026-10-19 12:21 KST. Lead: 이권욱. 기술 입력: 이하영(#35/#38), 이재환(#37/#43/#47). AI 사용: CODEX_ASSISTED. 10/18 후보의 보완본이며 이전 검토·승인 이력은 보존한다.

**판정: 설계 계약 보완 완료 / DESIGN_FREEZE=READY_FOR_LEAD_DECISION.** 하영·재환의 기술 입력과 [통합 리뷰](https://github.com/321Team/fds-project-baseline/pull/182#pullrequestreview-5566547829)의 차이를 반영했다. 아래 `권고`는 이 검토본의 구체적인 채택안이며 최종 Freeze 승인과 구분한다. 실제 UID·인증 reference·관측 결과는 담당/완료조건이 있는 `후속 실측` 슬롯이다. 빈 실제 값을 합성하거나 이를 이유로 정리한 설계 전체를 다시 미결로 돌리지 않는다. 이 문서는 tfvars, 적용 manifest, 새 GO 또는 발행 정본이 아니다. 최종 Lead 판단·병합·정본 발행은 각각 실제 기록으로 남긴다.

## 1. 적용 기준과 과거 문구 정정

발행 기준은 [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21)(`979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`)와 이후 명시적 변경결정이다. 본 후보는 baseline main `87b948d4f86d6180377ba7c2d015d4b0599e6261`에서 작성했다. 과거 문서·티켓 본문·AC를 덮어쓰거나 체크하지 않는다.

| 과거 빈칸/표현 | 현재 소비할 기준 | 근거 |
|---|---|---|
| OCI Primary / D21 PENDING | D21 FINAL: AWS EC2+EIP Libreswan relay. OCI는 비교·검토 이력 | [현행 정본](../../../baseline/FDS_Project_Implementation_Baseline_v3.1.21.md), [기존 D21 계약](../../README.md#2-confirmed-transport-adapter) |
| private API/Ingress, worker 3-AZ 후보, 4.22.16 | HCP / public API + public Ingress / worker 단일 AZ 3대 / 4.22.17 | [#34 방향 채택](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6207926205), [버전·이름 결정](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-6162036785) |
| D22 미선택 | Harbor Primary + P2 pull-only + ECR 수동 fallback A. FINAL은 Runtime 잔여 | [#42 채택](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-6207939448) |
| D23 미선택 | 추가 Hybrid DNS 보류. public DNS와 IP 기반 연결·엄격 TLS 유지 | [기존 D23 결정](decision-packet.md#현재-d23-결정--추가-hybrid-dns-보류) |
| D1 종료 때 3600초 원복 | FDS-IaC-Operator 최대 세션 **10800초 고정**. 실제 발급 credential 잔여시간은 별도 | [고정·반영 기록](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6209035655) |
| 생성 전에 G4 전체 PASS 필요 | 승인된 create-only 예외 유지. 생성 뒤 C/D 실측으로 G4 판단 | [#39 예외](https://github.com/321Team/fds-project-baseline/issues/39#issuecomment-6207939140) |
| F5 실제 삭제→재생성 필수 | 이번 교육 회차 재생성 생략 위험수용. RECREATE=NOT_RUN. 최종 실제 삭제·잔존 확인은 유지 | [#38 결정](https://github.com/321Team/fds-project-baseline/issues/38#issuecomment-6207939779) |

적용 상태의 스냅샷: [10/18 정확 saved Plan GO](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6248569180)의 [실제 생성 결과](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6248849533)는 3 added/rc0, cluster ready로 수신·검토됐다. [readback 수용 범위](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6258494105)는 BASIC_READY/G4 완료와 다르다. 과거 Plan-only GO와 실패 회차는 이력으로 보존하며 새 Apply/재생성/삭제·작업창을 이 문서로 승인하거나 연장하지 않는다.

## 2. 고정할 구성과 권장 상세

### 2.1 네트워크·ROSA·데이터

| 항목 | 채운 사양 | 분류·담당 |
|---|---|---|
| AWS 범위 | 계정 `774055931866`, 서울 `ap-northeast-2`, VPC `10.20.0.0/16` | 기존 결정 / 이하영 |
| 기존 subnet 4개 | private_a `10.20.10.0/24`(2a/apne2-az1), private_b `10.20.20.0/24`(2b/apne2-az2), private_c `10.20.30.0/24`(2c/apne2-az3), public_transport_a `10.20.110.0/24`(2a/apne2-az1) | 기존 D21 배치. b/c 보유를 worker 3-AZ 배치로 해석하지 않음 |
| ROSA 제출 subnet | worker=private_a, public Ingress용=public_transport_a. public b/c 신설 없음 | 기존 결정 + 생성 코드 / 이하영 |
| Transit / egress | Relay `10.20.110.10`, t3.medium, encrypted gp3 40GiB, EIP 1. 일반 인터넷 egress NAT 1은 Relay와 역할 분리 | 기존 결정. 단일 Relay/NAT 장애 위험 유지 |
| Cluster | ROSA HCP, 이름 `fds-rosa-hcp`, 버전 `4.22.17`, public API / public default Ingress | 기존 결정. 생성 직전 지원성·실제 Plan 판정은 기존 #4 키트 |
| Worker | pool `workers`, m5.xlarge ×3, root 300GiB/대, IMDSv2 required, autoscaling=false, auto_repair=true | 생성 코드는 disk size를 지정하고 타입은 플랫폼 기본값. 기존 EBS readback 3대는 gp3/300GiB/Encrypted=true. single-AZ는 worker 배치이며 managed control-plane 배치를 의미하지 않음 |
| 교체 설정 | worker pool max_surge=1 / max_unavailable=0. 실제 용량·quota·IP 여유는 기존 precheck 소비 | 생성 코드. 이 설정만으로 무중단이나 실제 Ready 수를 보장하지 않음 |
| 내부 주소 | Pod `10.128.0.0/14`, Service `172.30.0.0/16`, host prefix `/23` | 생성 코드 값을 설계 계약으로 채택 **권고**. 코드/Plan/승인 계약 일치 확인 후 Freeze |
| 관리·업무 주소 | API `https://api.fds-rosa-hcp.khht.p3.openshiftapps.com:443`, Ingress `apps.rosa.fds-rosa-hcp.khht.p3.openshiftapps.com`. 앱 host는 `fds-api.<실제 default Ingress domain>` | [actual 인계](https://github.com/321Team/fds-project-baseline/issues/38#issuecomment-6249632930) 재사용. 재환 [MSA PR40](https://github.com/321Team/fds-msa/pull/40#pullrequestreview-5566547370)에 두 Route host 기록. default 인증서 wildcard/SAN·실제 A09는 후속 확인, 이 기록만으로 Route 실행 GO 아님 |
| 데이터 위치 | 업무 DB는 기존 db01 `10.1.93.55:5432`. 앱 2종은 stateless, 초기 P2 앱 PVC·새 DB 없음 | 기존 앱 계약. #37 TCP runtime 예외와 #47 DB 인증/A2 예외를 분리. 창 단위 운영이며 영구 유지·P1 credential 재사용은 자동 승인하지 않음 |
| state | network/vpn/rosa-prereq/rosa-runtime 소유 분리. runtime key=`phase2/rosa-runtime/terraform.tfstate`, S3 `use_lockfile=true`, 암호화 | runtime backend 예제와 기존 경계. 다른 state key/lineage는 #35 기존 인계 원본으로 연결 |
| 삭제 보호 | 생성 기본 delete_protection=true. 최종 정리 창에서 승인된 코드로 해제→삭제→잔존 확인 | 생성 코드 + #38/#55 기존 정리 절차. 이 문서로 삭제 승인하지 않음 |

네트워크 계산은 위 VPC/Pod/Service/On-Prem `10.1.93.0/24`의 설계상 비중복만 검사한다. 현장 전체 route inventory와 중복 없음까지 실측했다고 표현하지 않는다. On-Prem↔AWS selector `/24 ↔ /16`은 transport 범위이며 DB 허용 source가 아니다.

### 2.2 용량·복구·운영 — 새 사양 권고

| 미정 영역 | FDS 권장안 | 이유·검증 시점 |
|---|---|---|
| 초기 앱 크기 | 기존 코드 유지: transaction-api 3개 + fds-engine 3개. Pod당 request 250m/256Mi, limit 500m/512Mi | 정상 합계 request **1.5 CPU/1536Mi**, limit **3 CPU/3072Mi**. 이미지/Rule/기능 계약을 바꾸지 않음 |
| rollout 여유 | 앱별 1개 surge를 고려한 8 Pod 예산: request **2 CPU/2048Mi**, limit **4 CPU/4096Mi** | **계산상 앱 예산**이며 namespace quota나 노드 allocatable 실측이 아님. 플랫폼·DaemonSet·시험 Pod는 별도 사용량으로 하영이 #38 기존 handoff에 더함 |
| N-1 확인 | worker 1대 불가 시 남은 2대의 allocatable에서 플랫폼 사용량을 제외하고 앱 request/배치 제약 충족 여부 확인 | 현재 1AZ/Relay1/NAT1의 다중 AZ HA/SLA 보장은 제안하지 않음. 기존 장애·복구 AC는 유지하며 무중단으로 낮춰 쓰거나 PASS 가정하지 않음 |
| Quota/LimitRange | 임의 수치를 먼저 강제하지 않고 위 request/limit·rollout budget을 입력으로 하영이 실제 플랫폼 여유에 맞춰 설정 여부 결정 | 공용 OCP quota를 ROSA로 복제하지 않음. 부족하면 workload/증설 중 영향이 작은 안을 변경결정으로 제시; 조용한 scale-out 금지 |
| 업그레이드 | 프로젝트 검증 회차는 고정 버전/source로 재현. 서비스가 요구하는 업데이트가 생기면 지원 조건·영향·검증 창을 Lead가 기록 | 자동 업데이트 불가/영구 동결을 가정하지 않음. 새 버전의 실제 지원·작업은 별도 |
| 복구 범위 | 앱은 검증된 이전 렌더/digest 복구, 최초 previous=NONE이면 STOP/readback/수동 정리 판단. 데이터 복구는 기존 DB 절차 | 앱 이미지 rollback으로 DB schema/data 복구를 주장하지 않음. 실제 재생성 예외와 최종 삭제 의무는 §1 유지 |
| 작업창 | 자원 준비·credential·생성/관측·복구·반출 여유를 포함해 산정. 기존 ROSA 약 6시간 가용 조건, VPN rev4.1 260분 후보/DB 예외 최대120분을 각각 유지 | 서로 다른 작업의 상한을 혼합하지 않음. 실제 날짜·시각·비중첩은 해당 실행 티켓에서만 확정 |

### 2.3 보안·권한·공급망

| 항목 | 설계 값/권장안 | 완료 근거·후속 |
|---|---|---|
| Namespace | `fds-app`=앱, `ci-cd`=배포 SA, `monitoring-api`=예약. `rosa-app`은 overlay 이름 | 기존 [namespace 코드][rosa-ns]. monitoring 업무/권한을 새 P0로 활성화하지 않음 |
| 앱 실행 | restricted-v2 호환, runAsNonRoot, 고정 runAsUser/GID 강제 없음, RuntimeDefault seccomp, 권한상승 금지, capability ALL drop, readOnlyRootFilesystem | 기존 [앱 소스][app-base]. 실제 UID/SCC/admission/Ready는 PG-03로 인계 |
| 배포 권한 | `ci-cd/fds-deployer`→`fds-app` Role, 앱 렌더 정확히 Deployment2/Service2/Route2. SA/NP/Secret/RBAC/delete/exec/cluster-scope 쓰기 제외 | 기존 [RBAC][rosa-rbac]·[배포 계약][app-contract]. Role이 허용하는 ConfigMap은 현재 앱 렌더 0개이며 자동 추가하지 않음 |
| 플랫폼 사전 자원 | 하영(named admin)이 SA2·앱 NP2·플랫폼 기본 정책·승인된 Secret 객체 생성. DB 값 생산·전달은 재환(#43/#47), 소비 검증은 권욱(#46) | 값 생산자와 cluster 객체 생성자를 분리. 기존 receipt에는 reference/name/UID/resourceVersion·필요한 지문/유효기간만 기록. Secret 원문 제외 |
| 외부 앱 | 같은 승인 host의 `/api`와 `/readyz` 두 Route만. edge TLS, HTTP→HTTPS Redirect, default apps 인증서. engine/metrics 공개 Route 없음 | 기존 [Route 코드][app-route]. router→Pod는 현재 HTTP8000이며 종단간 TLS라고 표현하지 않음. 외부 호출은 승인 시험 데이터·환경 범위 |
| 관리 API | public endpoint의 인증·CA 검증 유지. Runner direct. 기존 Runner/On-Prem DNS·LB·route 변경 없음 | #38 endpoint/CA/identity/RBAC handoff 후 #46 actual provider에서 확인. VPN을 API 관리의 필수 경로로 추가하지 않음 |
| Secret 저장 보호 | **권고:** HCP의 기본 etcd AES 보호와 EBS 암호화를 구분해 소비. 추가 customer-managed etcd KMS/FIPS는 이번 P0 제외 | [Red Hat HCP 공식 문서][hcp-kms]의 기본 etcd AES/선택 custom KMS 설명과 기존 worker EBS Encrypted readback 재사용. 하영이 #38 Full 보안 증적에 연결; 이 근거만으로 F08 전체 PASS 아님 |
| Secret 소비 | 앱은 승인된 Secret reference만, 앱 SA token automount=false. 배포 SA의 Secret 조회/수정 권한 없음. DB Secret은 `transaction-api-db-credentials`/`DATABASE_URL` 계약 | 재환이 DB principal·권한·유효기간·비공개 전달 경로를 제시→하영 SEC 확인/객체 생성→권욱 소비 검증. P1 credential 재사용 여부는 #47의 별도 실제 입력 판정이며 기본 미사용/미변경. 신규 DB 사용자·P1 암호 회전도 이 설계로 승인하지 않음. 저장 암호화가 적법한 소비자의 사용까지 막는다고 주장하지 않음 |
| Registry | Harbor Primary/P2 pull-only, 기존 CA JSON SHA `4d86507ecd81789e376669940f68b2dbb27f5989e6fd4315238c9f61a2401da4`. ECR 수동 A, 자동 mirror/전환 없음 | [D22 소비·전환/복귀](d22-lead-review.md). CA 재수집·current 이미지 재빌드 요구 없음 |
| Registry 실패 | 인증 만료/strict TLS 실패/digest 불일치면 신규 rollout STOP, 건강한 Pod 보존. A도 인증·실제 pull·digest가 확인됐을 때만 전환 | ECR은 이미지 공급 대안이며 VPN/DB를 복구하지 않음. D22 FINAL=PENDING_RUNTIME |
| IAM 운영 | 본인 MFA+담당 역할, D1 최대3시간 고정. 팀원 정책 관리 위임은 검증·반영된 범위만 소비 | 중앙 경유 축소 의도는 유지하되 **팀원 원문관리 위임 후보=NOT_APPLIED**를 완료로 바꾸지 않음. 실제 권한 수정·root 예외를 새로 부여하지 않음 |

## 3. Interface Register 채움안

아래는 **설계 계약**이다. 현재 승인이 있는 실행 범위와 앞으로 필요한 Runtime 증적을 함께 적고, 전체를 `APPROVED/PASS`로 치환하지 않는다. IF-20 번호는 OADP→S3에 보존한다.

| ID / 연결 | Producer → Consumer · 포트 | 담당·허용/전환 계약 | 인수 증적·남은 값 |
|---|---|---|---|
| IF-17 Hybrid Transit | On-Prem vpn-gw01 `.51` ↔ AWS Relay EIP · IKEv2/IPsec UDP500/4500 NAT-T | 설계 권욱, VPN 재환, AWS route/SG 하영. On-Prem initiator·explicit IKE ID. OCI 재전환·public SSH 없음. 승인 시험 창 ON→정리/원복; 상시24시간 ON 아님 | 최신 #37 C/D tunnel/selector/SA·허용/거부·복구·정리 원본. EIP/ENI 등 actual은 기존 최신 handoff 재사용 |
| IF-18 DB | ROSA transaction-api → db01 `10.1.93.55:5432` | 권욱 인수·원복, 재환 시험/앱, 하영 node/route/SG/NP. source 허용 단위는 private_a `10.20.10.0/24`(Relay nft·db01 rule·A2 pg_hba), 개별 node IP allowlist가 아님. 창 단위 A2 apply→E2E→rollback 원칙, 영구 유지 안은 채택하지 않음 | 같은 /24의 다른 ENI를 네트워크만으로 배제했다고 하지 않음. #37 C7 Pod/Node/IP/UID/imageID↔ENI·시각 대조 및 transaction-api 라벨/NP·DB 인증으로 식별, engine DENY·전체 VPC 금지. #37 TCP 예외와 #47 A2 별도 예외·원복 증적 구분 |
| IF-19 Image pull | ROSA **node image pull** → Harbor `10.1.93.54:443`; A는 실제 승인 ECR endpoint TCP443 | D22 Lead 권욱, trust/플랫폼 pull 하영, 이미지 공급 재환/권욱. IF-17 Transit·worker private_a route/SG·Relay 조건부 Harbor FORWARD·Harbor 반환 경로(#13)에 의존. P2 pull-only·strict TLS·immutable digest | 기존 D7/CA 재사용. Pod NP를 node pull 통제로 쓰지 않음. actual 인증 reference/expiry·허용 경로·cold-pull·갱신·전환/복귀는 후속. 승인 P2 인증·허용 증적 미연결이면 [CASE2/HOLD](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6258748604), P1 Robot 차용 안 함 |
| IF-20 Backup | OADP → S3 TCP443 | 하영. **P1 보류**, G5 이후 여력·지원 공급·안전 창·비용 판단 충족 시 재검토 | [#44 보류](https://github.com/321Team/fds-project-baseline/issues/44#issuecomment-6182867720). bucket/role/retention/restore actual 지금 생성하지 않음. Backup/Restore PASS 아님 |

IF-17/18의 Stage-A handoff는 승인 경로의 구현·실측 후 보완한다. [Stage-A 조건부 수용](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6207104552)의 `STAGE_A_READY=NO`를 전체 YES로 바꾸지 않는다. worker_db=0 초기 상태를 결함으로 되돌리지 않고 실제 DB 허용에 필요한 route/SG 변경을 한 회차에 맞춘다.

보조 연결(새 정본 IF 번호를 부여하지 않음):

| 연결 | 설계 계약 | 담당·확인 |
|---|---|---|
| Runner → API | 승인 actual API_URL의 scheme·host·port·CA 그대로 소비(현재 `https://api.fds-rosa-hcp.khht.p3.openshiftapps.com:443`). 단기 credential·제한 배포 SA, 승인6객체/동일 source·render·claim/checkpoint 결속 | 권욱 #46; 하영 identity/CA/권한·플랫폼 receipt; 재환 clean render. 일반 OCP 포트6443으로 치환하지 않음 |
| Client → Route → 앱 | TLS443→Ingress→transaction-api8000, 내부 API→engine8001. HTTP80은 Redirect. 외부 engine·9090/9091·catch-all 없음 | 재환 #43/#47, 하영 Router/NP 지원 |
| 앱 → DNS | 실제 openshift-dns로 UDP/TCP53/5353; 임의 인터넷 DNS 허용 아님 | 하영 플랫폼/재환 앱 NP 합산 대조 |
| 앱 → DB/Harbor | 승인 IF-18은 transaction-api의 `onprem-egress=true`만. 플랫폼03의 Harbor Pod egress 허용은 node pull 근거가 아니며 실제 필요한 Pod 소비가 없으면 최소화 | #7의 합산 정책/렌더 검토에서 확정. 앱은 probe용 `route-exposed=true`를 사용하지 않음 |

## 4. Decision·의존성·Gate

| 항목 | 현재 결정 / 조건 | 다음 책임 |
|---|---|---|
| D21 / #36→#35/#37 | AWS Relay FINAL, OCI 비선택. 기존 티켓명에 OCI가 남아 있어도 새 OCI 구축으로 해석하지 않음 | 하영 AWS 입력, 재환 VPN·회복 증적 |
| D22 / #42 | A 방향 확정, 생성 후 cold-pull·Basic Ready·전환/갱신·기존12출력으로 FINAL 판단 | 권욱, 하영/재환 기존 생산물 소비 |
| D23 / #40/#48/#120 | 추가 DNS 보류·OPEN 유지. actual public DNS는 #38에서 인계 | 권욱. P0가 실제 이름 해석에 막히는 변경이 생길 때만 재검토 |
| D26 / #41 | Operator 추가 공급 보류. G5 이후 여력/지원/필요가 있을 때 Direct/Mirror 선택 | [하영 보류 결정](https://github.com/321Team/fds-project-baseline/issues/41#issuecomment-6182867037). P0 선행조건으로 확대하지 않음 |
| D10 / D25 | D10의 과거 OCI Primary 표기는 후속 D21을 적용. D25의 backlog 복원·통합·조건부 티켓 기준 유지 | 기존 정본의 Decision ID를 재발급하지 않음. P1 보류를 취소/완료로 변경하지 않음 |
| #34 Freeze | 본 사양·IF·의존성·변경통제와 미확인 항목의 담당/시점을 검토 대상으로 배포한 뒤 Lead 결정 | 권욱. 하영/재환은 자기 영역의 차이만 확인; 모든 문서의 상시 이중 승인 절차를 새로 만들지 않음 |
| Create / G4 | #4의 해당 새 Plan·키트·가용 창·권한 조건으로만 Create 판단. 이후 #37 C/D·원복/G4 필수 증적 | 하영 생성/플랫폼, 재환 VPN, 권욱 G4. Full Freeze나 G4 PASS를 이번 작성으로 선언하지 않음 |
| #38 Basic→#42/#43→#46 | 플랫폼 identity/보안·pull→승인 Registry/host의 clean render→실제 verifier/provider/CLI→RUN-A 정상/RUN-B 차단 | 하영→재환→권욱. 구현 PR CI를 실제 배포 PASS로 승격하지 않음 |
| #47/#50→#49/#52/#55 | 실제 Hybrid E2E·실패/복구 결과를 인수표·산출물·Review·최종 정리에 연결 | 기존 Lead 유지. #52 참석/일정 미정값, P1 보류, 기존 AC 보존 |

## 5. 지금 닫을 항목과 생성 후 채울 항목

| 순서 | 담당 | 이번에 할 일 / 완료조건 | 단계 |
|---|---|---|---|
| 1 | **이권욱** | API443·source /24·A2 창 단위 원복 경계·Secret 분담과 하영의 EBS/etcd/IF-19 정정을 본 문서에 반영 | 설계 계약 보완. 아래 AC 연결과 문서 검사 결과로 Freeze 판단 가능 여부 확인 |
| 2 | 이하영 | [플랫폼 기술 입력](https://github.com/321Team/fds-project-baseline/pull/182#pullrequestreview-5558725574)의 비차단 정정을 소비. 실제 N-1/보안/권한·receipt는 #38에서 인계 | 기존 검토는 재사용, 자기 영역의 새 차이가 있을 때만 후속. 전체 시험/별도 견적 요구 없음 |
| 3 | 이재환 | [VPN·앱 기술 입력](https://github.com/321Team/fds-project-baseline/pull/182#pullrequestreview-5563073305)의 source·A2·Secret 차이를 소비 | 기존 검토는 재사용. Freeze 뒤 NETWORK.md CIDR 정합화는 재환 기존 소관. 실제 node/pull 결과를 지금 요구하지 않음 |
| 4 | **이권욱** | 본 보완 SHA·남는 위험·후속 슬롯을 확인하고 #34에서 최종 Freeze/변경통제 채택 여부 기록 | READY_FOR_LEAD_DECISION, 아직 최종 승인·병합·정본 발행 아님. 일반 설계 문서에 상시 전원 승인 Gate 추가 안 함 |
| 5 | 이하영 → 이재환 → 이권욱 | 수신한 URL/domain/cluster는 재사용. 나머지 CA/identity·node/ENI/Namespace UID·SCC·DB credential Secret 생성 경로/reference/expiry·actual node pull→clean render→#46 소비 | 후속 실측. 별도 미결값 합성·P1 credential 자동 재사용 금지 |
| 6 | **이권욱** | #39/G4·D22 Final·#46/Hybrid E2E·정본 및 인수 상태를 증거 단계별 갱신 | 실행/인수 결과가 생겼을 때만 |

**Freeze의 설계 미결과 Runtime 차단은 다르다.** 현재 actual host/UID 부재는 생성 후 인계 슬롯이다. 반면 #46에 이 값 없이 쓰기를 시도하거나, IF-18을 실제 승인 source/원복 없이 열려는 경우에는 해당 실행을 차단한다. 처음 확인된 drift만 수정하고 이미 받은 CA/D7/담당 지정/비중첩 확인을 재요구하지 않는다.

## 6. 실패·복구와 Phase 1 경계

| 발생 조건 | 영향 | 처리·재검증 |
|---|---|---|
| source/Plan/input hash·backend/lineage·대상 계정 불일치, 기존 오류 state 발견 | 잘못된 대상/기존 자원 손상 위험 | 해당 실행 HOLD, 원본 보존. state 삭제/강제 재Apply 금지. 정확 원인·변경분을 확인하고 동일 승인 조건을 다시 만족할 때 재개 |
| unknown 응답/부분 적용/credential 만료/claim 불명 | 중복 쓰기·실제 상태와 receipt 불일치 | 자동 재시도 금지, 실제 readback·checkpoint 대조. 새 유효 입력·사람의 범위 판단 후 재개 |
| DB source 불일치/동일 node의 다른 workload/관측 단절/원복 창 초과 위험 | 비인가 DB 접근 또는 추적성 훼손 | rev4.1 중단·원복 기준 사용. 실제 조건을 재확보한 해당 case만 재검증 |
| Registry/TLS/auth·digest 불일치 | cold-pull/rollout 실패 | 새 rollout STOP, 기존 정상 Pod 보존. 지원된 인증/승인 경로 복구 후 실패 case 재시험; A 미준비면 자동 전환 없음 |
| 플랫폼 용량/배치 부족 | Pending/eviction/업무 불안정 | 기존 노드/Pod 관측으로 요청량·배치 대조. 승인 없이 증설·보안 완화하지 않고 최소 변경안 검토 |

Phase 1 DB·pg_hba·영구 방화벽·NetworkManager·route·Harbor CA·공용 OCP·기존 Runner·DNS/LB·AC는 이 설계 작업에서 실제 변경하지 않는다. #37 `pre-apply`의 runtime route/firewall 예외는 TCP 사전 시험 전용이며 DB 로그인 허용/pg_hba 변경 승인이 아니다.

#47 A2는 별도 경계다. [고정 DB 코드][db-a2]의 `a2-apply`는 NM 영구 route·permanent firewall/reload·pg_hba hostssl을 실제 바꾸므로, 창 끝에 원복해도 **적용 중 P1 영구 설정 변경**이다. 설계는 영구 유지 대신 **창별 apply→E2E→동일 RUN receipt에 근거한 rollback**으로 정한다. 해당 창의 정확한 대상·새 RUN·코드 SHA·변경/원복·복구 대응·P1 영향이 별도로 승인된 경우에만 실행한다. #37 승인이나 이번 Freeze로 대체하지 않는다. 원복 완료 receipt의 재사용·drift 상태에서의 일괄 삭제/재Apply를 하지 않고 코드의 STOP/수동 판단을 따른다. 이 문서로 새 A2 예외나 상한을 발급하지 않으며 #37의 DB120분 상한을 A2 승인으로 전용하지 않는다.

새 Harbor Robot·allowlist/반환 경로 변경이 필요하면 baseline#13 소관의 대상·기간·복구/P1 기준선 영향 판단을 먼저 연결한다. 기존 CA·D7 digest를 재수집하거나 P1 Worker/Runner Robot을 임시 차용하지 않는다. 시험 접근권한은 증적 검토 완료까지 유지하는 기존 결정을 따르며, 새 정책 일괄 부여/분리 정책 재부착 승인은 아니다.

비용은 교육장 지원·자부담0·목표$400/중단$450/상한$500을 유지한다. 지정 비용 세션의 새 사용자 리포트만 권욱이 소비한다. 위 자원 유지안은 새 자원/비용 GO가 아니며 담당자에게 상세 단가표·중복 비용승인을 요구하지 않는다.

## 7. Freeze 판단에 남길 AC 연결

아래는 #34의 기존 AC/Exit Criteria에 대한 설계 근거다. 본문 체크박스·상태·정본은 자동 변경하지 않는다. 실제 실행값이 없는 항목은 설계가 아니라 해당 실행의 진입 조건이다.

| #34 기존 조건 | 이 검토본의 근거 / 최종 Lead 판단 입력 |
|---|---|
| On-Prem/AWS CIDR 중복 방지 | §2.1 VPC/Pod/Service/On-Prem 설계 비중복. 현장 전체 route inventory 실측과 구분 |
| Primary/Fallback 전환 조건 | §1·2.3 D21 Relay / D22 Harbor Primary·ECR 수동 A. TLS/auth/digest 실패 STOP, 준비되지 않은 A 자동전환 금지 |
| Producer/Consumer/Port/Owner/Acceptance | §3 IF-17~20·보조 연결. actual API443/source /24·node pull·A2 책임/원복 명시 |
| Ticket↔Source 연결 | §4·8의 고정 SHA와 각 책임 티켓, 관련 readback·검토 URL |
| 세 담당 검토 대상 배포 | PR182와 하영5558725574·재환5563073305 기술 입력, 이번 통합 정정. 검토 의견을 GitHub APPROVE로 바꾸지 않음 |
| OCI/IaC/VPN/ROSA/APP/CICD 의존성 | §4 및 [현재 인계](readiness-handoff-20261016.md). OCI 재개 아님, 실제 생성/Basic/Registry/Delivery 각 단계 분리 |
| D21~D23·D26 조건부 범위 | §1·4. D22 방향 확정/FINAL 후속, D23/D26 보류 유지. P1 우선순위 보류는 취소/완료 아님 |
| 변경 통제 기준 승인 | 아래 §8의 명시적 채택 대상. **최종 Lead Freeze 기록 전에는 승인 완료로 표시하지 않음** |

후속 슬롯의 종료 책임: #38 하영=actual identity/권한·UID/SCC/N-1·보안·pull 준비, #43 재환=승인 Registry/host의 clean render, #47 재환/하영=DB Secret 입력/생성·정확 A2 예외 요청, #46 권욱=실제 정상/실패차단·추적, #39 권욱=G4 남은 C/D/원복 판정, #42 권욱=D22 Runtime 최종. 이 값이 도착하기 전 해당 실행은 HOLD이며 설계 Freeze만으로 MET/PASS로 바꾸지 않는다.

## 8. 변경 통제·검증 기록

**권고:** Freeze 이후 변경은 기존 책임 티켓/PR에 `변경 전→후 / 이유 / 영향 interface·AC / source SHA / 필요한 delta 검증 / 실행 단계·창 / 원복 / Lead 판정`을 한 번 기록한다. 사소한 문구 수정·동일 사양의 actual ID 수신은 새 설계 승인 대기 없이 반영한다. CIDR·공개 범위·worker 용량·인증/권한 상한·Registry 방향·Phase1 영향·AC 변경은 해당 Lead의 실질 변경결정이 필요하다. 코드·실행 설정/증적 저장소는 기존 독립 리뷰 기준을 유지하고, 일반 설계 문서에 전원 서명을 추가하지 않는다. [기존 리뷰 권한 정책](../../../governance/REVIEW_AUTHORITY_POLICY.md) 적용.

작성 시 검토 근거:

- infra-terraform PR34 HEAD `f60a8031f9be15e651189dc98bbc4723df3d7316`: [runtime main.tf][tf-main], [variables][tf-vars], [backend][tf-backend]. 후보 코드이며 병합/실행 완료로 표시하지 않음.
- infra-rosa main `0e011ee6646d91b04e727d0ec09d49cac5607cf8`: Namespace/RBAC/NetworkPolicy의 실제 source 조회.
- fds-msa main `93800f09d2f5de61f6e2336771e62881f036c9ff`: 배포 계약·기계 계약·앱2종·Route·overlay source 조회.
- [D7 수신 기록](d22-lead-review.md#1016-1825-d7-원본-소비-완료), [#46 최신 인계](https://github.com/321Team/fds-project-baseline/issues/46#issuecomment-6218664174), [#37 rev4.1](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-6207763819) 재사용.
- [공개 아키텍처 PR11](https://github.com/321Team/fds-project-architecture/pull/11) HEAD `50ec51a589433d2e25bc0d4a9a503399bcde413d`은 별도 Draft 설명 자료다. 정본·실제 구축도·이번 Freeze 승인으로 대체하지 않는다. 본 후보 채택 후 필요한 도식 차이만 동기화한다.

10/19 보완은 [통합 리뷰5566547829](https://github.com/321Team/fds-project-baseline/pull/182#pullrequestreview-5566547829)의 API443/source/A2/Secret과 하영·재환 입력을 반영한다. MSA PR40 source `fe9e8277b9f8da485804a8742d5ec10200f22e9d`의 host 기록은 [기술 수용](https://github.com/321Team/fds-msa/pull/40#pullrequestreview-5566547370) 단계이며 아직 Runtime 아님. [cold-pull v5 수용](https://github.com/321Team/infra-rosa/issues/12#issuecomment-6258893270)과 [exact-zone 귀속 검토](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6258891664)는 각각 정적 키트/제한된 수동 귀속 근거이고 실행·삭제 GO가 아니다.

상태 구분: STATIC=문서/고정 source/주소·용량 계산 대조, MOCK=이번 문서 작업 신규 Runtime 모의시험 불요·기존 충분한 검증 재사용, CI=수정 HEAD의 실제 checks로 별도 확인, RUNTIME=이번 작업 미실행, REVIEW=기존 두 담당 기술 입력+작성자 통합 정정(자기 독립 승인 아님), MERGE=미수행, PUBLICATION=최종 Freeze/정본 미발행. 해시와 산술 검사는 동작/AC 성공 증거가 아니다.

[tf-main]: https://github.com/321Team/infra-terraform/blob/f60a8031f9be15e651189dc98bbc4723df3d7316/terraform/rosa-runtime/main.tf
[tf-vars]: https://github.com/321Team/infra-terraform/blob/f60a8031f9be15e651189dc98bbc4723df3d7316/terraform/rosa-runtime/variables.tf
[tf-backend]: https://github.com/321Team/infra-terraform/blob/f60a8031f9be15e651189dc98bbc4723df3d7316/terraform/rosa-runtime/backend.hcl.example
[rosa-ns]: https://github.com/321Team/infra-rosa/blob/0e011ee6646d91b04e727d0ec09d49cac5607cf8/platform/rbac/manifests/namespaces.yaml
[rosa-rbac]: https://github.com/321Team/infra-rosa/blob/0e011ee6646d91b04e727d0ec09d49cac5607cf8/platform/rbac/manifests/rbac.yaml
[app-contract]: https://github.com/321Team/fds-msa/blob/93800f09d2f5de61f6e2336771e62881f036c9ff/deploy/DELIVERY-CONTRACT-rosa.md
[app-base]: https://github.com/321Team/fds-msa/blob/93800f09d2f5de61f6e2336771e62881f036c9ff/deploy/base/transaction-api.yaml
[app-route]: https://github.com/321Team/fds-msa/blob/93800f09d2f5de61f6e2336771e62881f036c9ff/deploy/components/openshift/route.yaml
[hcp-kms]: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/install_clusters/rosa-hcp-creating-cluster-with-aws-kms-key
[db-a2]: https://github.com/321Team/infra-db/blob/57f050ef/ops/p2-hyb01-rosa-db01/db01-rosa.sh
