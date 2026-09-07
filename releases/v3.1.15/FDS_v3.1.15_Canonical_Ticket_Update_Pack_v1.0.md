# FDS v3.1.15 Canonical Ticket Update Pack v1.0

> **Purpose:** D35 Interface Contract Integrity / IF-11A 승인에 따른 Notion 속성·Description Upsert 정본  
> **Canonical Baseline:** FDS_Project_Implementation_Baseline_v3.1.15  
> **Upsert Key:** Record ID  
> **Rule:** 기존 Record를 갱신하며 동일 Record ID 신규 생성 금지
> **Description Rule:** 모든 Record는 `User/Technical Story → Scope(In/Out) → 핵심 요구사항 → Acceptance Criteria → 검증 및 증적 → Dependency → Decision/Risk Control → Review/Handoff → Completion Record` 순서를 유지한다.

---

# 1. MS-G0-01 — G0 Design Freeze

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | MS-G0-01 |
| Phase | Design |
| Category | Milestone / Design Freeze |
| Type | Milestone |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-26 |
| End | 2026-09-01 |
| Calendar Days | 7 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | D-ARC-01·D-NET-01·D-WBS-01·D-SEC-01 승인과 정본 Evidence를 확인하고 G0 FULL PASS 기록 확보 |
| Related Decision IDs | D17; D28; D32; D34; D35 |
| Related Risk IDs | RISK-05; RISK-07 |
| Source | FDS_Project_Implementation_Baseline_v3.1.15; D-SEC-01 Security Design Baseline v1.0; D35 |
| Schedule Note | 2026-09-01 D17/D34 승인으로 D-SEC-01과 G0를 FULL PASS / Done으로 종결했다. D35는 Interface 정합성 보정이며 G0를 재개방하지 않는다. G1/G2 Runtime Gate는 별도다. |

## Description

### 🎯 User Story

프로젝트 Gate Owner 이권욱으로서 Architecture·Network·WBS·Security 설계 동결을 Evidence로 승인하고, Runtime Gate와 구분된 G0 결과를 확정한다.

### 📌 Scope

#### In Scope

- D-ARC-01, D-NET-01, D-WBS-01, D-SEC-01 승인 확인
- D17/D34와 Baseline v3.1.15 연결; D35 정합성 보정 추적
- G0 FULL PASS 기록

#### Out of Scope

- G1/G2 Runtime 구현과 후속 티켓의 실제 PASS 판정

### 📋 핵심 요구사항

- [x] 설계 Ticket의 Lifecycle과 Gate Result를 분리한다.
- [x] 승인일·승인자·정본 Source를 동일하게 기록한다.

### ✅ Acceptance Criteria

- [x] 4개 Design Ticket Done
- [x] D17/D34 PASS
- [x] Baseline v3.1.15 RELEASED
- [x] G0 FULL PASS와 Lifecycle Done 동기화

### 🧪 Evidence

- Baseline v3.1.15
- D-SEC-01 Security Design Baseline v1.0
- D34 승인 기록
- `docs/evidence/MS-G0-01/`

### 🔗 Dependency

- Blocked By: 없음 — D17/D34 승인 완료
- Blocks / Next: G1 Infrastructure Ready, G2 Security / Feature Ready

### ⚖️ Decision / Risk Control

- Decision: D34에 따라 G0 FULL PASS를 확정한다.
- Risk Control: G0 종결을 G1/G2 Runtime 완료로 오인하지 않는다.

### 🔍 Review / Handoff

- Review Owner: 이하영, 이재환
- Handoff: 각 구현 티켓은 자체 Runtime Evidence로 별도 종결한다.

### 📝 Completion Record

- Result: FULL PASS
- Status: Done
- Completed Date: 2026-09-01
- Approver: 이권욱

---

# 2. P1-K8S-01 — kubeadm 3CP + 3Worker / Calico

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-K8S-01 |
| Phase | Phase 1 |
| Category | Kubernetes / Platform |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-08-27 |
| End | 2026-09-04 |
| Calendar Days | 9 |
| Working Days | 7 |
| Lead | 이하영 |
| Support | 이권욱 |
| Exit Criteria | LB Stage A 확인, 6개 Node firewalld OFF, containerd/kubelet·SELinux·identity·Port Matrix, BGP Disabled+VXLANCrossSubnet Calico, 6/6 Ready, CoreDNS, static local PV Evidence |
| Related Decision IDs | D01; D02; D05; D27; D31; D34; D35 |
| Related Risk IDs | RISK-02; RISK-03; RISK-04; RISK-07; RISK-14 |
| Source | Baseline v3.1.15; P1-K8S Preflight Review v1.1; D35 IF-11A Approval Record |
| Schedule Note | Gate 0 Preflight 실행은 가능하다. IF-11A 설계 승인은 완료됐으나 kubeadm init은 P1-LB Stage A `PASS / Listener Ready` Evidence 인수 전 **HOLD**다. 해제 후 firewalld OFF와 Calico 설치를 Console·Rollback 확보 후 순차 적용한다. |

## Description

### 🎯 User Story

Kubernetes 담당자로서 3 Control Plane과 3 Worker의 kubeadm Cluster, Calico Network와 Monitoring Storage 기반을 제공한다.

### 📌 Scope

#### In Scope

- containerd/kubeadm/kubelet/kubectl
- 3CP+3Worker
- BGP Disabled + VXLANCrossSubnet + natOutgoing
- 6개 Node firewalld 비활성화
- CoreDNS/PSA Minor Handoff
- static local StorageClass/PV

#### Out of Scope

- Workload 보안 Manifest와 Application/Monitoring 배포
- 동적 Storage Provisioner 또는 NFS 도입

### 📋 핵심 요구사항

- [ ] LB Stage A Evidence 확인
- [x] IF-11A Node 6대→API LB 설계 승인 확인
- [ ] 6개 Node identity 중복 0
- [ ] SELinux Enforcing 유지
- [ ] UDP 4789 중심 Port Matrix, TCP 179/IPIP 기본 미허용
- [ ] MTU 후보 1450 실측 확정
- [ ] `WaitForFirstConsumer`, `Retain`, nodeAffinity local PV 제공
- [ ] P1-SEC의 Secret encryption 변경창 지원

### ✅ Acceptance Criteria

- [ ] CP3+Worker3 Ready
- [ ] etcd 3 Member Healthy
- [ ] Calico/CoreDNS 정상
- [ ] firewalld disabled/inactive 및 reboot 지속
- [ ] Pod/Service DNS와 Cross-node Pod 통신 PASS
- [ ] StorageClass/PV 준비 완료

### 🧪 Evidence

- `docs/evidence/P1-K8S-01/`
- Preflight/Runtime/Cluster Gate 및 SHA-256 Index

### 🔗 Dependency

- Blocked By Bootstrap: P1-LB-01 Stage A `PASS / Listener Ready` Evidence
- Blocks: P1-SEC/APP/MON Runtime, P1-LB Stage B

### ⚖️ Decision / Risk Control

- Decision: D34의 firewalld OFF, Calico BGP Disabled + VXLANCrossSubnet, static local PV를 적용한다.
- Risk Control: Console·Backup·canary·실측 MTU·CrossSubnet 회귀시험 후 확장하며 실패 시 승인된 VXLAN Always로 전환한다.

### 🔍 Review / Handoff

- Review Owner: 이권욱
- Handoff: PSA Minor·Storage·Calico 출력과 Platform Ready Evidence를 P1-SEC/P1-MON에 전달한다.

### 📝 Completion Record

- Result: TBD
- Status: To Do
- Completed Date: 미입력
- Reviewer / Approver: 미입력 — 입력 시 풀네임 사용

---

# 3. P1-SEC-01 — Kubernetes Security Controls

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-SEC-01 |
| Phase | Phase 1 |
| Category | Security / Kubernetes |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-04 |
| End | 2026-09-11 |
| Calendar Days | 8 |
| Working Days | 6 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | PSA/SecurityContext/Default Deny/RBAC/HEP-GNP/Secretbox/LimitRange/Probe와 `.50/32→30080` 포함 Positive·Negative·Rollback Evidence PASS |
| Related Decision IDs | D12; D17; D18; D19; D27; D31; D34 |
| Related Risk IDs | RISK-06; RISK-07; RISK-08 |
| Source | Baseline v3.1.15; D-SEC-01 Security Design Baseline v1.0; ICR v1.4 |
| Schedule Note | Manifest/Prework GO. Runtime은 P1-K8S Platform Ready 후 수행하고 실제 업무 Secret 생성 전에 secretbox를 적용한다. |

## Description

### 🎯 User Story

Kubernetes 보안 담당자로서 D-SEC-01 승인 설계를 Manifest와 Runtime Policy로 구현하고 최소권한과 기본차단을 증명한다.

### 📌 Scope

#### In Scope

- Namespace/PSA/version label
- SecurityContext/SA/RBAC
- Workload NetworkPolicy
- Calico named HEP/GNP 및 preDNAT NodePort
- Secretbox at-rest encryption
- LimitRange/Resource presence/Probe verification
- cicd-runner-sa Role/TokenRequest 정책

#### Out of Scope

- Self-hosted Runner 설치·GitHub 등록·Service·Workflow 운영
- Application 코드와 Monitoring Workload 자체 구현
- P2 Admission Policy·Image 서명 강제·KMS v2

### 📋 핵심 요구사항

- [ ] kube-system enforce Privileged, audit/warn Restricted
- [ ] CoreDNS 실제 Manifest dry-run
- [ ] monitoring-node 신규 Workload 생성 제한
- [ ] `.50/32→Worker:30080`만 preDNAT 허용
- [ ] Prometheus `nodes/metrics`와 `/metrics`만, `nodes/proxy`·Secret 금지
- [ ] Runner는 기존 2개 Deployment get/update/patch만 허용
- [ ] Secretbox key root-only, 3CP 동일 Config, etcd 원문 비노출

### ✅ Acceptance Criteria

- [ ] PSA 위반 Pod 차단
- [ ] Allow 흐름 PASS / Deny 흐름 FAIL
- [ ] SA별 `kubectl auth can-i` Positive/Negative PASS
- [ ] NodePort/9100/10250 HEP/GNP PASS
- [ ] Secret encryption·backup·rotation·rollback PASS
- [ ] Probe 장애 주입과 Endpoint 제외 PASS

### 🧪 Evidence

- `docs/evidence/P1-SEC-01/`
- 비밀정보는 fingerprint 또는 마스킹만 기록

### 🔗 Dependency

- Blocked By Runtime: P1-K8S Platform Ready
- Related: ICR-D-NET-01-01, P1-APP, P1-MON, P1-CICD

### ⚖️ Decision / Risk Control

- Decision: D17/D34와 D-SEC-01 v1.0을 구현 기준으로 사용한다.
- Risk Control: HEP/GNP는 Bootstrap Allow와 canary를 먼저 적용하고 Secretbox key는 Git/Evidence에서 제외한다. Deployment patch 우회 위험은 P1 Residual Risk로 유지한다.

### 🔍 Review / Handoff

- Review Owner: 이권욱, 이재환
- Handoff: SA/RBAC/TokenRequest 정책은 P1-CICD에, Probe·Resource 검증 결과는 P1-APP/P1-MON에 전달한다.

### 📝 Completion Record

- Result: TBD
- Status: To Do
- Completed Date: 미입력
- Reviewer / Approver: 미입력 — 입력 시 풀네임 사용

---

# 4. P1-APP-01 — transaction-api / fds-engine

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-APP-01 |
| Phase | Phase 1 |
| Category | Application / MSA |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-09-01 |
| End | 2026-09-09 |
| Calendar Days | 9 |
| Working Days | 7 |
| Lead | 이재환 |
| Support | 이하영 |
| Exit Criteria | 2개 Deployment/Service, 업무 8000/8001·metrics 9091/9090, `/livez`·`/readyz`, DB/FDS 장애정책, Resource, local endpoint topology, Contract/E2E Evidence |
| Related Decision IDs | D03; D04; D18; D27; D31; D34 |
| Related Risk IDs | RISK-07; RISK-09 |
| Source | Baseline v3.1.15; D-SEC-01 Security Design Baseline v1.0 |
| Schedule Note | Interface/Schema 개발은 진행한다. Kubernetes Runtime은 Platform Ready 후 수행한다. `externalTrafficPolicy: Local`에 맞춰 backend Worker의 local endpoint를 보장한다. |

## Description

### 🎯 User Story

애플리케이션 담당자로서 거래 처리와 FDS 판정을 독립 서비스로 구현하고, 업무·메트릭·상태 계약을 분리한다.

### 📌 Scope

#### In Scope

- transaction-api 8000 / metrics 9091
- fds-engine 8001 / metrics 9090
- `/livez`, `/readyz`
- Request/Limit 수치 측정
- Replica/topology/local endpoint

#### Out of Scope

- PSA/RBAC/NetworkPolicy/HostEndpoint 구현
- edge01 HAProxy 및 Kubernetes API LB 구성

### 📋 핵심 요구사항

- [ ] 업무 API와 metrics Listener/Service를 분리한다.
- [ ] 외부 DB 장애는 Readiness에 반영하되 Liveness 재시작 루프를 만들지 않는다.
- [ ] `externalTrafficPolicy: Local` 대상 Worker에 local endpoint를 보장한다.
- [ ] Workload별 Request/Limit을 부하 시험으로 확정한다.

### ✅ Acceptance Criteria

- [ ] 업무·메트릭 Port 분리
- [ ] DB/FDS 장애 시 `/readyz` 503와 Endpoint 제외
- [ ] 외부 DB 장애가 Liveness 재시작 루프를 만들지 않음
- [ ] 승인 Worker backend에 local endpoint 존재
- [ ] R01/R02/R04/R07와 DB 저장 PASS

### 🧪 Evidence

- `docs/evidence/P1-APP-01/`
- OpenAPI/Contract/Probe/Resource/Topology/E2E

### 🔗 Dependency

- Blocked By Runtime: P1-K8S Platform Ready
- Related: P1-SEC-01, P1-DB-01, P1-LB-01, P1-CICD-01

### ⚖️ Decision / Risk Control

- Decision: D18/D34의 Port·Probe·local endpoint 계약을 적용한다.
- Risk Control: local endpoint가 없는 Worker는 edge01 backend에서 제외하고 Replica/Topology 실패를 별도 Evidence로 남긴다.

### 🔍 Review / Handoff

- Review Owner: 이하영
- Handoff: metrics·Probe·Resource·topology 결과를 P1-SEC/P1-MON/P1-CICD에 전달한다.

### 📝 Completion Record

- Result: TBD
- Status: In Progress
- Completed Date: 미입력
- Reviewer / Approver: 미입력 — 입력 시 풀네임 사용

---

# 5. P1-LB-01 — Kubernetes API Load Balancer

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-LB-01 |
| Phase | Phase 1 |
| Category | Infrastructure / Load Balancer |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-08-27 |
| End | 2026-09-03 |
| Calendar Days | 8 |
| Working Days | 6 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | IF-11/IF-11A/IF-06A Source Allowlist, `.109:6443→.102~.104:6443` Stage A Listener/Handoff와 Stage B Backend Health/API/Failover Evidence |
| Related Decision IDs | D02; D05; D27; D31; D34; D35 |
| Related Risk IDs | RISK-02; RISK-03; RISK-04 |
| Source | Baseline v3.1.15; P1-LB Stage A Guide v1.3; D35 IF-11A Approval Record |
| Schedule Note | IF-11A 설계 승인과 IF-06A 보존은 완료됐다. Node 6대·Runner Positive, ansible01 `.10` Negative, Listener/Rule/Hash/Handoff 전에는 Stage A와 P1-K8S Bootstrap을 해제하지 않는다. Application `.50→30080`은 별도 책임이다. |

## Description

### 🎯 User Story

인프라 담당자로서 단일 Kubernetes API Endpoint를 제공한다.

### 📌 Scope

#### In Scope

- `.109:6443` TLS pass-through
- CP `.102~.104:6443`
- IF-11 Runner `.20/32`, IF-11A Node 6대, IF-06A monitor01 `.30/32` Source Allowlist
- Stage A/Stage B Health/Failover

#### Out of Scope

- Application NodePort 30080 및 `externalTrafficPolicy: Local` 구현
- Kubernetes Node firewalld와 Calico HEP/GNP

### 📋 핵심 요구사항

- [x] IF-11A 설계 승인 및 IF-06A 보존 계약 확인
- [ ] IF-11/IF-11A/IF-06A `/32` Rule과 Zone-wide 6443 미개방을 검증한다.
- [ ] Node 6대·Runner Positive와 ansible01 `.10` Negative를 검증한다.
- [ ] HAProxy TCP health와 Control Plane backend를 검증한다.
- [ ] Stage A Listener Evidence를 P1-K8S Bootstrap 전에 전달한다.

### ✅ Acceptance Criteria

- [ ] Listener와 Source Allowlist PASS
- [ ] CP 3대 Backend 정상
- [ ] Backend 1대 장애 시 API 지속
- [ ] P1-K8S Bootstrap Handoff

### 🧪 Evidence

- HAProxy config validation, Listener/Allowlist, Backend health, failover, rollback
- `docs/evidence/P1-LB-01/`

### 🔗 Dependency

- Blocked By: P1-LNX-01/P1-NET-01/P1-ANS-01 Done Evidence
- Blocks: P1-K8S-01 kubeadm init, P1-LB Stage B

### ⚖️ Decision / Risk Control

- Decision: D27/D34에 따라 API LB와 Application NodePort 책임을 분리하고 D35에 따라 IF-11A 승인·IF-06A 보존을 적용한다.
- Risk Control: Stage A는 backend가 없어도 Listener만 검증하며 Stage B에서 API/failover를 최종 판정한다.

### 🔍 Review / Handoff

- Review Owner: 이하영
- Handoff: `.109:6443` Listener, Source Allowlist, Positive/Negative, SHA256/Commit Evidence를 P1-K8S에 전달한다.

### ⚠️ Scope Boundary

`externalTrafficPolicy: Local` Application NodePort 검증은 P1-APP/P1-SEC와 edge01 구성 담당이 수행한다.

### 📝 Completion Record

- Result: TBD
- Status: In Progress
- Completed Date: 미입력
- Reviewer / Approver: 미입력 — 입력 시 풀네임 사용

---

# 6. P1-MON-01 — Kubernetes-Integrated Hybrid Monitoring

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-MON-01 |
| Phase | Phase 1 |
| Category | Monitoring / Observability |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-09-04 |
| End | 2026-09-11 |
| Calendar Days | 8 |
| Working Days | 6 |
| Lead | 이재환 |
| Support | 이권욱 |
| Exit Criteria | In-cluster 5종 workload, static local PVC, Dashboard/Alert/Probe/Resource, IF-06B Receiver·Route·heartbeat와 16개 Acceptance Evidence |
| Related Decision IDs | D05; D14; D17; D19; D33; D34 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | Baseline v3.1.15; P1-MON Description v1.2; D33; D34; D35 |
| Schedule Note | Manifest 준비 GO. Runtime은 Platform/Storage/App/Security/IF-06B Route 준비 후 수행한다. IF-24는 P1 N/A다. |

## Description

### 🎯 Technical Story

Kubernetes 내부 모니터링과 외부 monitor01 Watchdog을 구축하여 Cluster 장애 시에도 heartbeat 단절을 탐지한다.

### 📌 Scope

#### In Scope

- Prometheus/Alertmanager/Grafana/KSM/node-exporter
- App metrics 9091/9090
- static local PVC와 15일/80% retention
- IF-06B 제한 Remote Write
- Blackbox edge/API Probe

#### Out of Scope

- IF-24 Alertmanager Webhook
- Monitoring HA, Loki/SIEM, 장기 외부 보존

### 📋 핵심 요구사항

- [ ] Monitoring Workload별 공식 UID/GID·Probe·Resource를 확정한다.
- [ ] static local PVC에 nodeAffinity·Retain·WaitForFirstConsumer를 사용한다.
- [ ] Grafana는 ClusterIP와 Server-side Prometheus Datasource만 사용한다.
- [ ] IF-06B는 승인 heartbeat/self metric만 전송한다.

### ✅ Acceptance Criteria

- [ ] Target/Dashboard/Alert/Probe PASS
- [ ] PVC restart persistence PASS
- [ ] KSM `/livez:8080`, `/readyz:8081` PASS
- [ ] IF-06B receiver flag/TLS/Auth/Payload/Route PASS
- [ ] 5분 heartbeat loss/recovery PASS
- [ ] IF-24 구성 0건

### 🧪 Evidence

- `docs/evidence/P1-MON-01/`

### 🔗 Dependency

- Blocked By Runtime: P1-K8S Storage/Platform, P1-APP metrics, P1-SEC controls, IF-06B Route/Receiver
- Blocks / Next: P1-E2E-01, P1-REV-01

### ⚖️ Decision / Risk Control

- Decision: D33/IF-06B를 유지하고 D34의 Storage·Probe·RBAC 경계를 적용한다.
- Risk Control: local PV는 비-HA Known Limitation이며 Route·TLS·Payload Allowlist 미확인 시 외부 연동을 Blocked로 유지한다.

### 🔍 Review / Handoff

- Review Owner: 이권욱
- Handoff: 9100/10250/IF-06B 실제 Source와 Target·Alert Evidence를 P1-SEC/ICR에 전달한다.

### 📝 Completion Record

- Result: TBD
- Status: In Progress
- Completed Date: 미입력
- Reviewer / Approver: 미입력 — 입력 시 풀네임 사용

---

# 7. P1-CICD-01 — GitHub Actions / Self-hosted Runner Delivery

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-CICD-01 |
| Phase | Phase 1 |
| Category | CI/CD / Supply Chain |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-01 |
| End | 2026-09-09 |
| Calendar Days | 9 |
| Working Days | 7 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Runner 설치·등록·Service 운영, Test/Trivy Gate, Harbor, 단기 Token, 승인 Digest patch, 이전 Digest rollback, Health/E2E Evidence |
| Related Decision IDs | D03; D04; D19; D34 |
| Related Risk IDs | RISK-06; RISK-08 |
| Source | Baseline v3.1.15; D-SEC-01 Security Design Baseline v1.0 |
| Schedule Note | P1-NET-01이 아닌 본 티켓이 Self-hosted Runner 설치·등록·Service·Workflow를 소유한다. P1-SEC은 SA/RBAC/TokenRequest 정책을 제공한다. |

## Description

### 🎯 User Story

자동화 담당자로서 Self-hosted Runner와 추적 가능한 Delivery Pipeline을 구축한다.

### 📌 Scope

#### In Scope

- Runner 설치·GitHub 등록·systemd/service 운영
- Workflow Test/Build/Trivy/Harbor
- 단기 Token 주입·만료·갱신
- 기존 Deployment의 승인 Digest patch
- 이전 승인 Digest rollback

#### Out of Scope

- Kubernetes SA/Role/RoleBinding/TokenRequest 정책 설계
- Harbor 자체 구축·Robot Account 발급·Trivy 서버 운영
- P2 Admission Policy·Image 서명 검증

### 📋 핵심 요구사항

- [ ] 장기 static SA token 금지
- [ ] 관리자 발급 또는 신뢰 broker의 Token bootstrap 명시
- [ ] create/delete/Secret 접근 시도 차단
- [ ] Unit/Scan 실패 시 Deploy 미실행
- [ ] Image Digest와 Commit SHA 역추적

### ✅ Acceptance Criteria

- [ ] Runner Service reboot 지속
- [ ] 정상 Pipeline PASS
- [ ] Test/Trivy Negative Gate PASS
- [ ] Token 만료 후 재발급 절차 PASS
- [ ] 지정 Deployment patch만 허용
- [ ] 이전 Digest rollback PASS

### 🧪 Evidence

- `docs/evidence/P1-CICD-01/`
- Token/Secret 원문 저장 금지

### 🔗 Dependency

- Blocked By Runtime: P1-K8S, P1-HBR, P1-SEC SA/RBAC/TokenRequest
- Related: P1-APP-01, P1-E2E-01

### ⚖️ Decision / Risk Control

- Decision: P1-CICD가 Runner 설치·등록·Service·Workflow를 소유하고 P1-SEC이 Kubernetes 인증 정책을 제공한다.
- Risk Control: 장기 토큰을 금지하고 Token 만료·재발급, 지정 Deployment만 patch, 이전 승인 Digest rollback을 검증한다.

### 🔍 Review / Handoff

- Review Owner: 이하영
- Handoff: Workflow Run·Digest·Token 만료·Rollback Evidence를 P1-SEC/P1-E2E에 전달한다.

### 📝 Completion Record

- Result: TBD
- Status: To Do
- Completed Date: 미입력
- Reviewer / Approver: 미입력 — 입력 시 풀네임 사용

---

# 8. ICR-D-NET-01-01 — Kubernetes Node Host Firewall / Monitoring Route

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | ICR-D-NET-01-01 |
| Phase | Phase 1 |
| Category | Network / Interface Change Control |
| Type | Change Request |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-09-01 |
| End | TBD |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | 6개 Node firewalld OFF·HEP/GNP, 30080/9100/10250 최소 허용, Return Route·IF-06B, canary/reboot/rollback Evidence |
| Related Decision IDs | D17; D18; D33; D34; D35 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | Baseline v3.1.15; ICR v1.4; D35 |
| Schedule Note | Change 승인 완료. Phase 0 GO, Runtime은 LB Stage A·Calico Ready·Port Matrix·Source 관측 후 Conditional GO다. |

## Description

### 🎯 User Story

네트워크 변경 담당 이권욱으로서 Kubernetes 6개 Node의 Host Firewall과 IF-06B Return Route를 승인된 canary·rollback 절차로 변경한다.

### 📌 Scope

#### In Scope

- 6개 Node firewalld OFF와 named HEP/GNP
- NodePort 30080, node-exporter 9100, kubelet 10250 최소 허용
- mgmt-gw01 Return Route와 IF-06B 443

#### Out of Scope

- IF-24 Webhook, D-NET-01/P1-NET-01 재개, 미사용 Calico Port 일괄 허용

### 📋 핵심 요구사항

- [ ] Phase 0 관측·백업·Console·Rollback을 먼저 확보한다.
- [ ] 1개 Worker canary 후 Worker, Control Plane 순으로 확장한다.
- [ ] 실제 Source/Destination/Route를 tcpdump와 정책 hit로 확인한다.

### ✅ Acceptance Criteria

- [ ] 6개 Node firewalld disabled/inactive 및 reboot 지속
- [ ] HEP/GNP와 30080/9100/10250 Positive·Negative PASS
- [ ] IF-06B Return Route·TLS/Auth·heartbeat PASS
- [ ] canary·regression·rollback Evidence 승인

### 🧪 검증 및 증적

- 상세 Matrix·명령·Rollback·Evidence는 `ICR-D-NET-01-01_Kubernetes_Node_Host_Firewall_및_Monitoring_Route_변경요청_v1.4.md`를 정본으로 사용한다.

### 🔗 Dependency

- Phase 0: 즉시 GO
- Runtime: P1-LB Stage A, Calico Ready, Port Matrix, Source 관측 후 Conditional GO
- IF-06B: Return Route/Receiver/TLS 준비 전 Blocked

### ⚖️ Decision / Risk Control

- Decision: D34에 따라 6개 Node firewalld OFF + Calico HEP/GNP, IF-06B 유지로 확정한다.
- Risk Control: named HEP, Bootstrap Allow, canary, Console, 명시적 rollback을 사용한다.

### 🔍 Review / Handoff

- Review Owner: 이하영
- Monitoring Validation: 이재환
- Handoff: Host policy와 Route Evidence를 P1-K8S/P1-SEC/P1-MON에 전달한다.

### 📝 Completion Record

- Result: Approved Change / Runtime Pending
- Status: In Progress
- Completed Date: 미입력
- Reviewer: 이하영
- Approver: 이권욱

---

# 9. P1-DNS-01 — Internal DNS Primary/Secondary

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-DNS-01 |
| Phase | Phase 1 |
| Category | DNS / Supporting Service |
| Type | Task |
| Status | In Review |
| Priority | P1 |
| Start | 2026-08-28 |
| End | 2026-09-07 |
| Calendar Days | 11 |
| Working Days | 7 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Primary/Secondary·TSIG·제한 Query/Recursion·Failover Evidence와 k8s-api-lb01 `.109` Resolver/ACL/IPSet 검증 및 Support Review 승인 |
| Related Decision IDs | D08; D09; D34; D35 |
| Related Risk IDs | RISK-02; RISK-04; RISK-07 |
| Source | Baseline v3.1.15; P1-DNS Description v1.1; P1-DNS Evidence Package v1.0; P1-LB Guide v1.3; D35 |
| Schedule Note | `.109` ACL/IPSet·Resolver delta를 포함해 Technical PASS이며 Support Review 대기다. Management `.10/.20/.30`의 DNS 사용은 OID-04 결정 전 미구현이고 현재 `.10` 제외를 유지한다. |

## Description

### 🎯 User Story

인프라 담당자로서 승인된 P1 Host에 제한된 Primary/Secondary DNS와 Failover를 제공하고 k8s-api-lb01도 내부 DNS 정본을 사용하도록 한다.

### 📌 Scope

#### In Scope

- dns01/dns02, `fds.internal`, TSIG Transfer, 제한 Query/Recursion
- k8s-api-lb01 `.109` BIND ACL·firewalld IPSet·Resolver·Failover

#### Out of Scope

- Reverse/PTR, DNSSEC, 완전한 Authoritative/Recursive 분리, Hybrid DNS

### 📋 핵심 요구사항

- [x] Primary/Secondary·TSIG·기존 Client Failover Technical PASS
- [x] dns01/dns02 ACL과 `fds-dns-clients` IPSet에 `.109` 반영
- [x] k8s-api-lb01 Resolver `.52→.53`, Search Domain `fds.internal`
- [x] `.109` 내부·외부 Query와 Primary 장애 Failover Technical Test
- [ ] Management `.10/.20/.30` DNS 필요성·ACL OID-04 결정

### ✅ Acceptance Criteria

- [ ] 원본 Evidence SHA-256 및 Support Review 승인
- [ ] `.109` Positive Test PASS, 비승인 Source Negative Test 유지
- [ ] Secret/TSIG 원문이 Evidence에 포함되지 않음

### 🧪 검증 및 증적

- `docs/evidence/P1-DNS-01/`
- 상세 Description: `P1-DNS-01_Notion_Description_v1.1.md`

### 🔗 Dependency

- `.109` delta 실행 시점: P1-LB-01 Stage A
- Routing/SNAT 변경 시에만 D-NET-01 §15.2 ICR 발행

### ⚖️ Decision / Risk Control

- Decision: `.109`는 실제 LB VM Interface이므로 DNS Consumer로 허용한다.
- Risk Control: `/24` 전체가 아닌 `.109/32`만 추가하고 기존 monitor01 차단을 유지한다.

### 🔍 Review / Handoff

- Review Owner: 이하영
- Handoff: ACL/IPSet·Resolver·Failover Evidence를 P1-LB와 P1-K8S에 전달한다.

### 📝 Completion Record

- Result: Technical PASS / Support Review Pending
- Status: In Review
- Completed Date: 미입력
- Reviewer / Approver: 미입력 — 입력 시 풀네임 사용

---

# 10. P1-HBR-01 — Harbor / Trivy Registry

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P1-HBR-01 |
| Phase | Phase 1 |
| Category | Registry / Container Security |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | TBD |
| End | TBD — G1 Runtime 일정에 연동 |
| Calendar Days | TBD |
| Working Days | TBD |
| Lead | 이하영 |
| Support | 이권욱 |
| Exit Criteria | harbor01 `.54:443`, Private CA Trust, 최소권한 Robot Account, IF-09 Runner Push·IF-10 Worker Pull/Pod Start, 비승인 Push/Pull DENY, Trivy/Digest/Evidence PASS |
| Related Decision IDs | D04; D17; D19; D35 |
| Related Risk IDs | RISK-04; RISK-06; RISK-07 |
| Source | Baseline v3.1.15; DEC-P1-TLS-01/D19; D-SEC-01 Security Design Baseline v1.0; D35 |
| Schedule Note | IF-09·IF-10 Runtime은 미검증이다. P1-K8S Gate 1 전 OID-02 Control Plane/System Image Registry Source를 결정하며, 결정 전 IF-10 Worker 범위를 CP로 임의 확장하지 않는다. |

## Description

### 🎯 User Story

Registry 담당자 이하영으로서 Private CA로 보호된 Harbor/Trivy와 최소권한 계정을 제공해 Runner의 승인 Image Push와 Worker의 검증된 Pull/Pod Start를 보장한다.

### 📌 Scope

#### In Scope

- harbor01 `10.1.93.54:443`, 서비스 전용 Leaf 인증서와 Consumer CA Trust
- CI/CD Push+Pull Robot Account와 Worker Pull-only Credential 분리
- IF-09 `runner .20 → harbor01 .54:443` Positive/Negative
- IF-10 `Worker .105/.107/.108 → harbor01 .54:443` Pull/Pod Start와 Push DENY
- Trivy 결과, Image Digest Pinning, Credential 회전·마스킹 Evidence
- OID-02 CP/Calico/kube-system Image Registry Source 결정 지원

#### Out of Scope

- Harbor HA와 실제 Backup/Restore — P1-DR-02
- P2 ROSA Image Source — D22/P2 Decision
- 결정 전 Control Plane Source를 IF-10에 임의 포함

### 📋 핵심 요구사항

- [ ] TLS 1.2 이상, hostname/SAN/Chain 검증과 우회 금지
- [ ] Runner `.20` Source 보존 및 인증 Push/Pull PASS
- [ ] Worker 3대 Pull/Pod Start PASS와 Push DENY
- [ ] 비승인 Source·잘못된 CA·잘못된 Credential DENY
- [ ] Robot Account 권한·회전·Secret 저장 경계 준수
- [ ] Trivy 결과와 배포 Digest 일치
- [ ] OID-02를 P1-K8S Gate 1 전 결정

### ✅ Acceptance Criteria

- [ ] Harbor Service/Health와 Certificate Chain PASS
- [ ] IF-09 Positive/Negative PASS
- [ ] IF-10 Pull/Pod Start 및 Push DENY PASS
- [ ] 실제 Source IP와 Host Firewall Allowlist 일치
- [ ] Image Digest·Scan 결과·Credential fingerprint Evidence 확보
- [ ] 비밀정보 평문 미포함

### 🧪 검증 및 증적

- `docs/evidence/P1-HBR-01/`
- TLS Chain/SAN, Login, Push/Pull, Trivy, Digest, Negative, Rotation, Rollback 및 `99_SHA256SUMS.txt`

### 🔗 Dependency

- Blocked By Runtime: Network/Linux 기반, D19 Private CA; Worker Pull은 P1-K8S Node 준비
- Blocks / Next: P1-CICD-01 Delivery, P1-K8S/APP/MON Image Pull, G1 Infrastructure Ready
- Related: P1-SEC-01 Credential/RBAC, P1-DR-02 Harbor Restore

### ⚖️ Decision / Risk Control

- Decision: D19의 Private Root CA + Harbor 전용 Leaf + Consumer CA Trust를 구현한다.
- Risk Control: `insecure`/검증 우회를 금지하고 Push·Pull Identity를 분리한다. OID-02 전에는 CP Source를 허용하지 않는다.

### 🔍 Review / Handoff

- Review Owner: 이권욱
- Handoff: CA Bundle, Repository, Robot Account Scope, Digest와 Pull 예시를 P1-K8S/P1-CICD/P1-APP/P1-MON에 전달한다.

### 📝 Completion Record

- Result: TBD
- Status: To Do
- Completed Date: 미입력
- Reviewer / Approver: 미입력 — 입력 시 풀네임 사용

---

# Release Note

- 2026-09-02 / v1.0: D35 Interface 전수점검과 IF-11A 승인 반영. P1-LB Stage A Runtime 조건, P1-K8S Bootstrap HOLD, IF-06A 보존, P1-DNS `.109` Technical PASS/OID-04, P1-HBR-01 복원을 동기화했다.

# Upsert 검증

- [ ] Record ID 중복 0
- [ ] 허용 Lifecycle 값만 사용
- [ ] Lead/Support 풀네임 일치
- [ ] Source가 v3.1.15로 갱신
- [ ] D35 영향 티켓의 Description과 Exit Criteria 동기화
- [ ] 기존 D-NET-01/P1-NET-01 Done/Closed 유지
- [ ] IF-11A Design Approved와 Stage A Runtime Pending 상태 분리
- [ ] IF-06A monitor01 `.30/32` Rule 보존 및 Negative Test 제외
- [ ] P1-HBR-01 신규 생성이 아니라 Record ID 기반 복원/Upsert
- [ ] 비밀정보 미포함
