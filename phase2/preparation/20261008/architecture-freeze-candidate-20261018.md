# #34 Architecture Freeze — 통합 사양 검토안

기준 시각: 2026-10-18 00:32 KST. Lead: 이권욱. 기술 입력: 이하영(#35/#38), 이재환(#37/#43/#47). AI 사용: CODEX_ASSISTED.

**판정: 권욱 담당 설계 통합·권장값 작성 완료 / DESIGN_FREEZE=CANDIDATE.** 기존 결정과 코드에 있는 값을 먼저 채웠다. 아래 `권고`는 이번 제안이며 승인 완료나 실행값이 아니다. `후속 실측`은 생성·해당 시험 후 채울 값이다. 실제 endpoint·UID가 아직 없다는 이유로 설계 선택 전체를 다시 미결로 돌리지 않는다. 이 문서는 tfvars, 적용 manifest, 새 GO 또는 발행 정본이 아니다.

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

적용 상태의 스냅샷: [Plan v9/Apply v6.1 검토](https://github.com/321Team/infra-rosa/issues/4#issuecomment-6235578516)는 새 Plan 수집 GO이며 새 Create GO가 아니다. 해당 실행 승인은 #4의 최신 정확한 Plan/시간/조건으로만 판단한다. 설계 문서로 과거 GO를 연장하지 않는다.

## 2. 고정할 구성과 권장 상세

### 2.1 네트워크·ROSA·데이터

| 항목 | 채운 사양 | 분류·담당 |
|---|---|---|
| AWS 범위 | 계정 `774055931866`, 서울 `ap-northeast-2`, VPC `10.20.0.0/16` | 기존 결정 / 이하영 |
| 기존 subnet 4개 | private_a `10.20.10.0/24`(2a/apne2-az1), private_b `10.20.20.0/24`(2b/apne2-az2), private_c `10.20.30.0/24`(2c/apne2-az3), public_transport_a `10.20.110.0/24`(2a/apne2-az1) | 기존 D21 배치. b/c 보유를 worker 3-AZ 배치로 해석하지 않음 |
| ROSA 제출 subnet | worker=private_a, public Ingress용=public_transport_a. public b/c 신설 없음 | 기존 결정 + 생성 코드 / 이하영 |
| Transit / egress | Relay `10.20.110.10`, t3.medium, encrypted gp3 40GiB, EIP 1. 일반 인터넷 egress NAT 1은 Relay와 역할 분리 | 기존 결정. 단일 Relay/NAT 장애 위험 유지 |
| Cluster | ROSA HCP, 이름 `fds-rosa-hcp`, 버전 `4.22.17`, public API / public default Ingress | 기존 결정. 생성 직전 지원성·실제 Plan 판정은 기존 #4 키트 |
| Worker | pool `workers`, m5.xlarge ×3, root gp3 300GiB/대, IMDSv2 required, autoscaling=false, auto_repair=true | 생성 코드. single-AZ는 worker 배치 설명이며 managed control-plane 배치를 의미하지 않음 |
| 교체 설정 | worker pool max_surge=1 / max_unavailable=0. 실제 용량·quota·IP 여유는 기존 precheck 소비 | 생성 코드. 이 설정만으로 무중단이나 실제 Ready 수를 보장하지 않음 |
| 내부 주소 | Pod `10.128.0.0/14`, Service `172.30.0.0/16`, host prefix `/23` | 생성 코드 값을 설계 계약으로 채택 **권고**. 코드/Plan/승인 계약 일치 확인 후 Freeze |
| 관리·업무 주소 | API actual URL/CA와 실제 default Ingress domain 사용. 앱 host는 `fds-api.<실제 default Ingress domain>` **권고** | 실제 domain/인증서 범위를 하영이 인계한 뒤 재환이 두 Route 공통 host로 고정. 지금 placeholder를 승인값으로 바꾸지 않음 |
| 데이터 위치 | 업무 DB는 기존 db01 `10.1.93.55:5432`. 앱 2종은 stateless, 초기 P2 앱 PVC·새 DB 없음 | 기존 앱 계약. DB 전환·credential/ACL은 #37/#47의 승인 범위 |
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
| 플랫폼 사전 자원 | named admin이 SA2·앱 NP2와 플랫폼 기본 정책·승인 Secret reference 준비. 배포 SA와 분리 | 기존 receipt에 name/UID/hash/resourceVersion만 기록. Secret 값은 제외 |
| 외부 앱 | 같은 승인 host의 `/api`와 `/readyz` 두 Route만. edge TLS, HTTP→HTTPS Redirect, default apps 인증서. engine/metrics 공개 Route 없음 | 기존 [Route 코드][app-route]. router→Pod는 현재 HTTP8000이며 종단간 TLS라고 표현하지 않음. 외부 호출은 승인 시험 데이터·환경 범위 |
| 관리 API | public endpoint의 인증·CA 검증 유지. Runner direct. 기존 Runner/On-Prem DNS·LB·route 변경 없음 | #38 endpoint/CA/identity/RBAC handoff 후 #46 actual provider에서 확인. VPN을 API 관리의 필수 경로로 추가하지 않음 |
| Secret 저장 보호 | **권고:** HCP 기본 etcd 암호화와 AWS 관리 EBS 암호화를 사용하고 추가 customer-managed KMS/FIPS 도입은 이번 P0에서 제외 | [Red Hat HCP 공식 문서][hcp-kms]의 default 범위 근거. EBS 암호화와 etcd 보호는 구분. 하영이 생성 옵션/지원 근거를 #38 Full 보안 항목에 연결; 실제 적용 확인 전 F08 PASS 아님 |
| Secret 소비 | 앱은 승인된 Secret reference만, 앱 SA token automount=false. 배포 SA의 Secret 조회/수정 권한 없음. 원문은 비공개 전달·보존 | 기존 코드. 권한을 가진 사람/워크로드의 Secret 사용까지 저장 암호화가 막는다는 주장은 하지 않음 |
| Registry | Harbor Primary/P2 pull-only, 기존 CA JSON SHA `4d86507ecd81789e376669940f68b2dbb27f5989e6fd4315238c9f61a2401da4`. ECR 수동 A, 자동 mirror/전환 없음 | [D22 소비·전환/복귀](d22-lead-review.md). CA 재수집·current 이미지 재빌드 요구 없음 |
| Registry 실패 | 인증 만료/strict TLS 실패/digest 불일치면 신규 rollout STOP, 건강한 Pod 보존. A도 인증·실제 pull·digest가 확인됐을 때만 전환 | ECR은 이미지 공급 대안이며 VPN/DB를 복구하지 않음. D22 FINAL=PENDING_RUNTIME |
| IAM 운영 | 본인 MFA+담당 역할, D1 최대3시간 고정. 팀원 정책 관리 위임은 검증·반영된 범위만 소비 | 중앙 경유 축소 의도는 유지하되 **팀원 원문관리 위임 후보=NOT_APPLIED**를 완료로 바꾸지 않음. 실제 권한 수정·root 예외를 새로 부여하지 않음 |

## 3. Interface Register 채움안

아래는 **설계 계약**이다. 현재 승인이 있는 실행 범위와 앞으로 필요한 Runtime 증적을 함께 적고, 전체를 `APPROVED/PASS`로 치환하지 않는다. IF-20 번호는 OADP→S3에 보존한다.

| ID / 연결 | Producer → Consumer · 포트 | 담당·허용/전환 계약 | 인수 증적·남은 값 |
|---|---|---|---|
| IF-17 Hybrid Transit | On-Prem vpn-gw01 `.51` ↔ AWS Relay EIP · IKEv2/IPsec UDP500/4500 NAT-T | 설계 권욱, VPN 재환, AWS route/SG 하영. On-Prem initiator·explicit IKE ID. OCI 재전환·public SSH 없음. 승인 시험 창 ON→정리/원복; 상시24시간 ON 아님 | 최신 #37 C/D tunnel/selector/SA·허용/거부·복구·정리 원본. EIP/ENI 등 actual은 기존 최신 handoff 재사용 |
| IF-18 DB | ROSA transaction-api → db01 `10.1.93.55:5432` | 권욱 인수·원복, 재환 시험/앱, 하영 node/route/SG/NP. 실제 승인 node-source 집합과 앱 라벨/NP·DB credential로 제한. engine DENY. 전체 VPC 허용 금지 | #37 C7 Pod/Node/IP/UID/imageID↔ENI·서버 관측 결속, positive/negative·time window·rollback. SNAT 이후 패킷만으로 Pod 정체성 입증했다고 하지 않음 |
| IF-19 Image pull | ROSA **node image pull** → Harbor `10.1.93.54:443`; A는 실제 승인 ECR endpoint TCP443 | D22 Lead 권욱, trust/플랫폼 pull 하영, 이미지 공급 재환/권욱. P2 pull-only·strict TLS·immutable digest. Pod NP와 node pull 통제를 혼동하지 않음 | 기존 D7 current 원문 재사용. actual 인증 reference/expiry·경로·cold-pull·갱신·전환/복귀. 재환은 확정 registry host만 렌더에 반영 |
| IF-20 Backup | OADP → S3 TCP443 | 하영. **P1 보류**, G5 이후 여력·지원 공급·안전 창·비용 판단 충족 시 재검토 | [#44 보류](https://github.com/321Team/fds-project-baseline/issues/44#issuecomment-6182867720). bucket/role/retention/restore actual 지금 생성하지 않음. Backup/Restore PASS 아님 |

IF-17/18의 Stage-A handoff는 승인 경로의 구현·실측 후 보완한다. [Stage-A 조건부 수용](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-6207104552)의 `STAGE_A_READY=NO`를 전체 YES로 바꾸지 않는다. worker_db=0 초기 상태를 결함으로 되돌리지 않고 실제 DB 허용에 필요한 route/SG 변경을 한 회차에 맞춘다.

보조 연결(새 정본 IF 번호를 부여하지 않음):

| 연결 | 설계 계약 | 담당·확인 |
|---|---|---|
| Runner → API | actual public API:6443/CA, 단기 credential, 제한된 배포 SA. 승인된6객체/동일 source·render·claim/checkpoint 결속 | 권욱 #46; 하영 플랫폼 receipt; 재환 clean render |
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
| 1 | **이권욱** | 기존 결정 충돌 정리, 위 사양·Interface·의존성·변경통제 작성. 문서 검증 후 검토본 제공 | 이번 작성 완료 |
| 2 | 이하영 | Pod/Service CIDR·host prefix·managed Secret 보호·N-1/rollout 예산·state 소유가 고정 생성 코드/플랫폼 지원과 맞는지 **차이만** 확인 | Freeze 기술 입력. 새로운 전체 시험/별도 견적 요구 없음 |
| 3 | 이재환 | IF-17/18 조건이 rev4.1/C7과 일치하는지, 앱 replicas/resources/포트/host 규칙·Secret 생산 책임이 #43/#47과 맞는지 **차이만** 확인 | Freeze 기술 입력. 실제 node/Pull 결과를 지금 요구하지 않음 |
| 4 | **이권욱** | 기술 차이 해소 후 채택값/남는 위험/문서 SHA/시점을 #34에 기록해 Freeze 판단 | 아직 미승인. 코드·증적 독립 리뷰와 문서 Lead 판단은 기존 정책 적용 |
| 5 | 이하영 → 이재환 → 이권욱 | 생성 후 URL/domain/CA·cluster/node/ENI/Namespace UID·SCC·Secret reference/expiry·actual node pull을 한 번 인계→clean render→#46 소비 | 후속 실측. 빈값 합성 금지 |
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

Phase 1 DB·pg_hba·영구 방화벽·NetworkManager·route·Harbor CA·공용 OCP·기존 Runner·DNS/LB·AC는 이 설계 작업의 변경 대상이 아니다. #37에서 별도로 승인된 DB runtime 예외만 정확한 대상·시간·원복 범위로 소비한다. 시험 접근권한은 증적 검토 완료까지 유지하는 기존 결정을 따르며, 새 정책 일괄 부여/분리 정책 재부착 승인은 아니다.

비용은 교육장 지원·자부담0·목표$400/중단$450/상한$500을 유지한다. 지정 비용 세션의 새 사용자 리포트만 권욱이 소비한다. 위 자원 유지안은 새 자원/비용 GO가 아니며 담당자에게 상세 단가표·중복 비용승인을 요구하지 않는다.

## 7. 변경 통제·검증 기록

**권고:** Freeze 이후 변경은 기존 책임 티켓/PR에 `변경 전→후 / 이유 / 영향 interface·AC / source SHA / 필요한 delta 검증 / 실행 단계·창 / 원복 / Lead 판정`을 한 번 기록한다. 사소한 문구 수정·동일 사양의 actual ID 수신은 새 설계 승인 대기 없이 반영한다. CIDR·공개 범위·worker 용량·인증/권한 상한·Registry 방향·Phase1 영향·AC 변경은 해당 Lead의 실질 변경결정이 필요하다. 코드·실행 설정/증적 저장소는 기존 독립 리뷰 기준을 유지하고, 일반 설계 문서에 전원 서명을 추가하지 않는다. [기존 리뷰 권한 정책](../../../governance/REVIEW_AUTHORITY_POLICY.md) 적용.

작성 시 검토 근거:

- infra-terraform PR34 HEAD `f60a8031f9be15e651189dc98bbc4723df3d7316`: [runtime main.tf][tf-main], [variables][tf-vars], [backend][tf-backend]. 후보 코드이며 병합/실행 완료로 표시하지 않음.
- infra-rosa main `0e011ee6646d91b04e727d0ec09d49cac5607cf8`: Namespace/RBAC/NetworkPolicy의 실제 source 조회.
- fds-msa main `93800f09d2f5de61f6e2336771e62881f036c9ff`: 배포 계약·기계 계약·앱2종·Route·overlay source 조회.
- [D7 수신 기록](d22-lead-review.md#1016-1825-d7-원본-소비-완료), [#46 최신 인계](https://github.com/321Team/fds-project-baseline/issues/46#issuecomment-6218664174), [#37 rev4.1](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-6207763819) 재사용.
- [공개 아키텍처 PR11](https://github.com/321Team/fds-project-architecture/pull/11) HEAD `50ec51a589433d2e25bc0d4a9a503399bcde413d`은 별도 Draft 설명 자료다. 정본·실제 구축도·이번 Freeze 승인으로 대체하지 않는다. 본 후보 채택 후 필요한 도식 차이만 동기화한다.

상태 구분: STATIC=문서/고정 source/주소·용량 계산 대조, MOCK=이번 문서 작업에는 새 실행 시험 없음, CI=이 PR의 실제 checks로 별도 기록, RUNTIME=이번 작업 미실행, REVIEW=작성자 자체 검토·기술 차이 확인 대기, MERGE=미수행, PUBLICATION=정본 미발행. 해시와 산술 검사는 동작/AC 성공 증거가 아니다.

[tf-main]: https://github.com/321Team/infra-terraform/blob/f60a8031f9be15e651189dc98bbc4723df3d7316/terraform/rosa-runtime/main.tf
[tf-vars]: https://github.com/321Team/infra-terraform/blob/f60a8031f9be15e651189dc98bbc4723df3d7316/terraform/rosa-runtime/variables.tf
[tf-backend]: https://github.com/321Team/infra-terraform/blob/f60a8031f9be15e651189dc98bbc4723df3d7316/terraform/rosa-runtime/backend.hcl.example
[rosa-ns]: https://github.com/321Team/infra-rosa/blob/0e011ee6646d91b04e727d0ec09d49cac5607cf8/platform/rbac/manifests/namespaces.yaml
[rosa-rbac]: https://github.com/321Team/infra-rosa/blob/0e011ee6646d91b04e727d0ec09d49cac5607cf8/platform/rbac/manifests/rbac.yaml
[app-contract]: https://github.com/321Team/fds-msa/blob/93800f09d2f5de61f6e2336771e62881f036c9ff/deploy/DELIVERY-CONTRACT-rosa.md
[app-base]: https://github.com/321Team/fds-msa/blob/93800f09d2f5de61f6e2336771e62881f036c9ff/deploy/base/transaction-api.yaml
[app-route]: https://github.com/321Team/fds-msa/blob/93800f09d2f5de61f6e2336771e62881f036c9ff/deploy/components/openshift/route.yaml
[hcp-kms]: https://docs.redhat.com/en/documentation/red_hat_openshift_service_on_aws/4/html/install_clusters/rosa-hcp-creating-cluster-with-aws-kms-key
