# Interface / Decision / CR Register — v3.1.19

RELEASED / FINALIZATION.

## 승인 입력과 적용 경계

| 항목 | 반영한 값·결정 | 유지되는 경계 |
|---|---|---|
| PR #72 | v18 게시 사실·WEB 필수 배포·일정 유연성·#59/#61 08-26·#46 10-16·Milestone 배정 | 기존 v18 태그와 Asset 소급 변경 없음 |
| DEC-CAL-P1-01 #28 | 09-22 오후 평일 Review 일정 결정 Done | 실제 Review/G3/Close 승인 아님 |
| DEC-P1-EGRESS-01 #78 | server08 / egress-proxy01 / .56:3128, 2vCPU·2GiB·30GiB, .57 예비 유지 | #74 Squid·#75 NetworkPolicy/Secret Runtime 별도 |
| OID-01 | ansible01 10.250.10.10/32 + svc_ansible, 내부 SNAT 금지·기존 Return Route | HEP/GNP 실제 적용은 6/6 Ready 이후 별도 실행창 |
| Monitoring storage | worker03(.108), /home/fds-local-pv/{prometheus,grafana,alertmanager}; static local PV/WFFC/Retain/nodeAffinity | 단일 Worker non-HA, 경로·SELinux·공간 검증 및 Runtime 미완료 |
| PVC 초기값 | Prometheus 20Gi / Grafana 5Gi / Alertmanager 2Gi, Prometheus 15d·retention.size≤16GB | 사용률에 따른 조정 가능한 초기값 |
| NTP 결정 | control01 내부 chronyd, UDP123, offset≤100ms, 60초×6, sync lost≥5m FAIL, reboot≤5m 재동기화 | control01 upstream/time authority 미정; INPUT_INCOMPLETE/RUNTIME_HOLD |
| Harbor/CI 정책 | Worker pull-only 분리, Robot 유한 30일 결정·Never 미채택, Harbor Scanner 유지, HIGH/CRITICAL·Scanner/DB 오류 차단 | 실제 계정·소비자별 인수 별도 |
| Trivy 운영 | 검토 버전/SHA 고정·관리자 교체, Scan 전 DB 갱신 필요·유효성 검사, 오류 fail-closed | latest 자기 갱신·오래된 DB fallback·임의 유예기간 도입 없음 |
| ICR 단순화 | 기존 증적 재사용, 도구 qualification과 운영 보완 분리, 인수/영수증 연결 | 추가 VM 반복 시험·광역 허용·CP1/CP2/CP3 인수 예외 자동 승인 없음 |

근거: [PR72](https://github.com/321Team/fds-project-baseline/pull/72), [#28](https://github.com/321Team/fds-project-baseline/issues/28), [#78](https://github.com/321Team/fds-project-baseline/issues/78), [Lead 결정](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5697547621), [Harbor 결정](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5659049448), [CI 결정](https://github.com/321Team/fds-project-baseline/issues/16#issuecomment-5659051242). 세부 수집 문서 및 원문은 audit/v3.1.19/intake와 tickets/v3.1.19/sources에 보존한다.

## 승인·관측·보류 분류

APPROVED_INPUT은 확인된 사용자/Lead 결정의 명시 범위만 뜻한다. GitHub의 Merged는 코드 편입 사실이며 Runtime 인수가 아니다. PENDING_REVIEW/INPUT_INCOMPLETE 및 합성 시험·제출 영수증 검증은 그대로 표시한다. GitHub ticket lifecycle과 원문 체크상태를 보존했으며 이번 작업에서 운영 AC를 새로 체크하지 않았다. 새 D/IF 순번은 임의 발급하지 않고 DEC-P1-EGRESS-01·CR Record ID로 추적한다.

## Decision / CR lifecycle

| Record | Status | Milestone | Exit Criteria | Source |
|---|---|---|---|---|
| DEC-P1-FDS-01 | Done | G2 Security / Feature Ready | 현행 탐지·기록 유지, 신규 보류·운영 기능 미도입, 실패 정책·계약 소유권, G2 영향 없음 및 후속 검증·재검토 조건 기록 | https://github.com/321Team/fds-project-baseline/issues/4 |
| DEC-P1-TXN-01 | Done | G2 Security / Feature Ready | 기존 계약 유지 선택, 신규 상태/API·Migration 변경 유예, #4/#6과 정책·표현 소유권 및 기존 구현 정합성 후속 기록 | https://github.com/321Team/fds-project-baseline/issues/5 |
| DEC-P1-ADMIN-01 | Done | G2 Security / Feature Ready | 프론트엔드 배치 제외, 합성 데이터·최소 노출 원칙, 5개 검토 축 적용/유예, 기존 접근 통제 재사용 및 후속 시나리오 인계 기록 | https://github.com/321Team/fds-project-baseline/issues/6 |
| D-SEC-01 | Done | G0 Design Freeze | 승인권자 지정, D-SEC-01 검토 범위·산출물·Exit Criteria 승인, P1-SEC-01과의 경계 승인, 요구사항과 검증 증적 연결 후 Done 판정 | https://github.com/321Team/fds-project-baseline/issues/7 |
| ICR-D-NET-01-01 | In Progress | G2 Security / Feature Ready | Kubernetes 6개 Node의 보호 공백 없는 firewalld→Calico named HEP/GNP 전환, 30080/9100/10250 최소 허용, 관리망 반환 경로와 IF-06B 정합화, Positive/Negative/Regression/Reboot/Rollback 및 무결성 Evidence 완료 | https://github.com/321Team/fds-project-baseline/issues/14 |
| DEC-CAL-P1-01 | Done | Phase 1 Review | 09-20 일요일 Review 유지 또는 영업일 재배치, 참석자·승인권자·시간·대체일을 확정하고 WBS/Calendar 동기화 | https://github.com/321Team/fds-project-baseline/issues/28 |
| P2-OCI-01 | To Do | G4 Cloud / VPN Ready | OCI Relay 가능성·권한·Public Endpoint·IPsec/NAT-T·Route를 검증하고 Primary 또는 승인 Fallback 경로를 선택 | https://github.com/321Team/fds-project-baseline/issues/36 |
| DEC-P2-DNS-01 | To Do | G5 ROSA Application Ready | P0 IP Endpoint 유지 또는 Hybrid DNS P1 적용을 확정하고 Resolver/Forwarding/Zone/Route/테스트·Cancelled 결정 근거를 승인 | https://github.com/321Team/fds-project-baseline/issues/40 |
| DEC-P2-OP-01 | To Do | G5 ROSA Application Ready | ROSA Operator 공급망을 Direct Catalog 또는 oc-mirror/Harbor/Custom CatalogSource 중 하나로 결정하고 구현·N/A 기준 승인 | https://github.com/321Team/fds-project-baseline/issues/41 |
| DEC-P2-REG-01 | To Do | G5 ROSA Application Ready | ROSA Image Source를 On-Prem Harbor 또는 승인 Cloud Registry로 확정하고 Route·TLS·Credential·비용·Fallback을 승인 | https://github.com/321Team/fds-project-baseline/issues/42 |
| DEC-CAL-P2-01 | To Do | Phase 2 Review | 10-24 토요일 Review 유지 또는 영업일 재배치, 참석자·승인권자·시간·Project Close 영향도를 확정하고 WBS 동기화 | https://github.com/321Team/fds-project-baseline/issues/52 |
| CR-P1-ANS-01-01 | Done | G1 Infrastructure Ready | Kubernetes 6개 Node의 DNS 전환, 검색 도메인·API FQDN/Short Name·외부 DNS·직접 질의·서비스 회귀·멱등성·Rollback·Evidence 무결성 및 Support Review 완료 | https://github.com/321Team/fds-project-baseline/issues/58 |
| DEC-P1-ENTRY-01 | Done | G2 Security / Feature Ready | edge01→transaction-api 노출 방식을 Ingress/Reverse Proxy/NodePort 후보 중 확정하고 Port·Health Check·Firewall·NetworkPolicy 변경을 승인 | https://github.com/321Team/fds-project-baseline/issues/62 |
| DEC-P1-MON-01 | Done | G0 Design Freeze | Grafana 포함 Kubernetes 내부 관측 Stack, node-exporter 통제 예외, monitor01 외부 Watchdog, IF-05/IF-06 계열, 보안·Rollback·후속 구현 책임을 D33으로 승인하고 Baseline·Architecture·Addendum·Release Notes를 발행 | https://github.com/321Team/fds-project-baseline/issues/63 |
| DEC-P1-TLS-01 | Done | G1 Infrastructure Ready | Harbor와 edge01의 인증서 발급·SAN·CA Trust 배포·갱신·Rollback 방식을 확정하고 Consumer별 검증방법 승인 | https://github.com/321Team/fds-project-baseline/issues/64 |
| CR-P1-MON-01-01 | In Progress | G2 Security / Feature Ready | discord.com 아웃바운드 확인, 프록시 전용 VM 확정, Squid/Nginx 구성 및 discord.com allowlist 적용, 고정 IP·포트를 [Issue B(#75)](https://github.com/321Team/fds-project-baseline/issues/75)에 전달 | https://github.com/321Team/fds-project-baseline/issues/74 |
| CR-P1-MON-01-02 | In Progress | G2 Security / Feature Ready | Alertmanager 전용 NetworkPolicy(Egress) 작성·적용, podSelector 라벨 확정, Secret 주입·회전·폐기 절차 확정, 검증(허용/차단/알림 전송) 완료 및 Support Review 완료 | https://github.com/321Team/fds-project-baseline/issues/75 |
| DEC-P1-EGRESS-01 | Done | G2 Security / Feature Ready | 배치·예외 정책 기록, 예약 IP/자산 충돌 확인, 자원 영향 검토, #74/#75 구현·인계 조건 연결 | https://github.com/321Team/fds-project-baseline/issues/78 |

## 계승 Interface 계약

## 15.1 Interface Contract Register

v19 추가/구체화: IF-07의 관리 Source/identity는 .10/32 + svc_ansible이다. Alertmanager→egress-proxy01 .56:3128→discord.com:443 CONNECT는 DEC-P1-EGRESS-01과 #74/#75에 한정한다. 실제 client Source·selector·Secret·발송/거부/복구 인수는 미완료다. 다른 Pod 일반 인터넷 egress로 확대하지 않는다. 기존 IF-24 퇴역·IF-06B 계약은 유지한다.


`Design State=FROZEN`은 Endpoint/Protocol/Port/Owner/Acceptance의 설계 확정을 의미한다. `Runtime State=PASS`만 실제 구현·시험 완료를 의미한다. `PROVISIONAL` 또는 `DECISION REQUIRED`는 Allowlist·Manifest·방화벽 Permanent 반영 근거로 사용할 수 없다.

| ID | Source → Destination | Protocol / Port | Contract / Purpose | Owner | Implementing Ticket | Acceptance | Design State | Runtime State — 2026-09-04 |
|---|---|---|---|---|---|---|---|---|
| IF-01 | Client → edge01 `.50` | TCP 80/443 | External Service Entry | 이권욱 / 이재환 | P1-APP-01 / TLS 후속 구현 | Health, 80→443, 승인 Transaction 요청 | FROZEN | NOT TESTED |
| IF-02 | edge01 `.50/32` → Worker `.105/.107/.108` | TCP 30080 | HAProxy → 제한 NodePort | 이권욱 / 이하영 | P1-APP-01 / P1-SEC-01 / ICR | `/readyz`, Source `.50/32` Positive, 기타 Source Negative | FROZEN | NOT TESTED |
| IF-02A | transaction-api Service → Pod | TCP 80 → 8000 | ClusterIP Service Routing | 이재환 | P1-APP-01 | `/readyz`, `/livez`, Positive/Negative API | FROZEN | NOT TESTED |
| IF-03 | transaction-api → fds-engine | TCP 8001 | Internal REST Rule Evaluation | 이재환 | P1-APP-01 / P1-SEC-01 | R01/R02/R04/R07 Contract 및 비승인 Egress DENY | FROZEN | NOT TESTED |
| IF-04 | transaction-api → db01 `.55` | TCP 5432 | Transaction/FDS Result Persistence | 이재환 | P1-DB-01 / P1-APP-01 / P1-SEC-01 | Migration, Save/Query, Source 확인, fds-engine→DB DENY | FROZEN | IN PROGRESS |
| IF-05 | `monitoring-api/Prometheus` → transaction-api/fds-engine | TCP 9091/9090 | 분리된 Cluster 내부 `/metrics` Scrape | 이재환 | P1-APP-01 / P1-MON-01 / P1-SEC-01 | Target UP, Metric Query, edge01 `/metrics` DENY | FROZEN — D34 | NOT TESTED |
| IF-05A | `monitoring-api/Grafana` → Prometheus | TCP 9090 | Server-side Datasource Query | 이재환 | P1-MON-01 / P1-SEC-01 | Datasource Health, Grafana ClusterIP only | FROZEN — D33 | NOT TESTED |
| IF-05B | `monitoring-api/Prometheus` → kube-state-metrics | TCP 8080 | Object State Metrics | 이재환 / 이하영 | P1-MON-01 / P1-SEC-01 | Target UP, RBAC read-only | FROZEN — D33 | NOT TESTED |
| IF-05C | `monitoring-api/Prometheus` → Alertmanager | TCP 9093 | Alert Delivery | 이재환 / 이하영 | P1-MON-01 / P1-SEC-01 | Test Alert Firing→Resolved, Default Deny Positive/Negative | FROZEN — D35 | NOT TESTED |
| IF-06 | `monitoring-api/Prometheus` → node-exporter/kubelet | TCP 9100/10250 HTTPS | Node/Kubelet Metrics | 이재환 / 이하영 | P1-MON-01 / P1-SEC-01 / ICR | 실제 Source/SNAT, Target UP, CA/SA Auth, 비승인 Workload DENY | FROZEN — D33/D35 | SOURCE OBSERVATION PENDING |
| IF-06A | monitor01 `.30/32` → edge01 `.50` / API LB `.109` | TCP 443/6443 | External HTTPS/TCP Blackbox Probe | 이권욱 / 이재환 | P1-MON-01 / P1-LB-01 | LB `.30/32` Allowlist, Failure/Recovery Probe | FROZEN — D33/D35 | NOT TESTED |
| IF-06B | `monitoring-api/Prometheus` → monitor01 `.30` | TCP 443 HTTPS | 제한 Heartbeat/Self Metric Remote Write | 이재환 / 이하영 | P1-MON-01 / P1-SEC-01 / ICR | 5분 이내 Loss Detection, TLS/Auth, Payload Allowlist, Return Path | FROZEN — D33 | BLOCKED — ROUTE/RECEIVER/SOURCE |
| IF-07 | ansible01 `.10` → K8s Node `.102/.103/.104/.105/.107/.108` | TCP 22 | OS/Node Configuration | 이권욱 | P1-ANS-01 / P1-K8S-01 | SSH `PASS=6`, Source `.10`, 멱등성 | FROZEN — D35 scope correction | PASS=6 / DRIFT CHECK REQUIRED |
| IF-08 | runner `.20` → GitHub | TCP 443 | SCM / Workflow Outbound Session | 이권욱 | P1-CICD-01 | Clone/Workflow Poll 또는 승인 API | FROZEN | NOT TESTED |
| IF-09 | runner `.20` → harbor01 `.54` | TCP 443 | Image Push | 이권욱 / 이하영 | P1-HBR-01 / P1-CICD-01 | CA Trust, Authenticated Push, Source `.20` | FROZEN | NOT TESTED |
| IF-10 | Worker `.105/.107/.108` → harbor01 `.54` | TCP 443 | Workload Image Pull | 이하영 | P1-HBR-01 / P1-K8S-01 | CA Trust, Pull/Pod Start, Push DENY | FROZEN | NOT TESTED |
| IF-11 | runner `.20/32` → API LB `.109` | TCP 6443 | Kubernetes Deploy | 이권욱 / 이하영 | P1-LB-01 / P1-CICD-01 | Source `.20`, Authenticated API/Deploy | FROZEN | STAGE A TCP POSITIVE PASS / AUTHENTICATED DEPLOY PENDING |
| IF-11A | K8s Node `.102/.103/.104/.105/.107/.108/32` → API LB `.109` | TCP 6443 | kubeadm init/join 및 안정된 Control Plane Endpoint | 이권욱 / 이하영 | P1-LB-01 / P1-K8S-01 | Node 6대 Positive, 실제 Source, 비승인 Source Negative | FROZEN / APPROVED — D35 | STAGE A NODE POSITIVE 6/6 PASS; `.10` NEGATIVE PASS |
| IF-12 | API LB `.109/32` → CP `.102/.103/.104` | TCP 6443 | Kubernetes API HA | 이권욱 / 이하영 | P1-LB-01 / P1-K8S-01 | Pre-bootstrap Route, Backend Health, Auth API, Failover/Recovery | FROZEN | PREBOOTSTRAP REACHABILITY PASS / STAGE B PENDING |
| IF-12A | CP `.102/.103/.104` 상호 및 kube-apiserver → etcd | TCP 2379~2380 | etcd Client/Peer | 이하영 / 이권욱 | P1-K8S-01 / ICR / P1-SEC-01 | Listener, CP 상호 Positive, 비승인 Source DENY, Cluster Health | FROZEN — D35 | NOT TESTED |
| IF-12B | Control Plane `.102/.103/.104` → Node 6대 | TCP 10250 HTTPS | kubelet API for cluster operation | 이하영 / 이권욱 | P1-K8S-01 / ICR / P1-SEC-01 | CA/Auth, logs/exec/port-forward, 비승인 Source DENY | FROZEN — D35 | NOT TESTED |
| IF-12C | K8s Node `.102/.103/.104/.105/.107/.108` 상호 | UDP 4789 Bidirectional | Calico VXLANCrossSubnet Dataplane | 이하영 / 이권욱 | P1-K8S-01 / ICR | Cross-node Pod 통신, MTU, Reboot, TCP179·IP Protocol4 미허용 확인 | FROZEN — D35 | NOT TESTED |
| IF-13 | Physical Service/Node `.50/.51/.52/.53/.54/.55/.102/.103/.104/.105/.107/.108/.109` → dns01 `.52`, dns02 `.53` | UDP/TCP 53 | `fds.internal` Resolution / Recursion | 이권욱 | P1-DNS-01 | Known/Unknown/External Query, ACL/IPSet, 비승인 Source DENY | FROZEN — D35 source enumeration | PASS / SUPPORT REVIEW CLOSED — 2026-09-03 |
| IF-13A | Approved Kubernetes Workload → CoreDNS | UDP/TCP 53 | `cluster.local` 및 승인 Egress DNS | 이하영 | P1-K8S-01 / P1-SEC-01 / P1-APP-01 / P1-MON-01 | Pod DNS, Default Deny Positive/Negative, 비-DNS Egress DENY | FROZEN — D35 | NOT TESTED |
| IF-13M | Management `.10/.20/.30` → dns01 `.52`, dns02 `.53` | UDP/TCP 53 | Management Resolver | 이권욱 | P1-DNS-01 | Source별 필요성·ACL·Positive/Negative | P1 N/A / FUTURE CHANGE CONTROL — D36 | NOT IMPLEMENTED; `.10` EXCLUDED |
| IF-14 | dns01 `.52` → dns02 `.53` | TCP 53 + TSIG | Restricted Zone Transfer | 이권욱 | P1-DNS-01 | Authorized AXFR/IXFR, Unauthorized DENY | FROZEN | PASS / SUPPORT REVIEW CLOSED — 2026-09-03 |
| IF-15 | dns01/dns02 → `8.8.8.8` | UDP/TCP 53 | External Forwarding | 이권욱 | P1-DNS-01 | `forward only`, External Query, Other Node Direct Query DENY | FROZEN | PASS / SUPPORT REVIEW CLOSED — 2026-09-03 |
| IF-16 | Physical FDS VM → mgmt-gw01 `.58` | L3 Static Route | `10.250.10.0/24 via 10.1.93.58`, 내부 SNAT 금지 | 이권욱 | ICR-D-NET-01-01 | Route, 양방향 Source Preservation, Reboot/Regression | FROZEN | DRIFT — edge/harbor/db REMEDIATION PENDING |
| IF-17 | vpn-gw01 `.51` → OCI 및 OCI → AWS VPN | UDP 500/4500; IPsec | Hybrid Transit 후보 | 이권욱 | P2-ARC-01 / P2-VPN-01 | Peer별 Endpoint, Tunnel, Route, Approved TCP Path | PROVISIONAL — D21 PENDING | NOT TESTED |
| IF-18 | ROSA → db01 `.55` | TCP 5432 | Hybrid Persistence 후보 | 이권욱 / 이재환 | P2-ARC-01 / P2-HYB-01 | Source CIDR/SG/Route, DB ACL, Hybrid E2E | PROVISIONAL — D21 PENDING | NOT TESTED |
| IF-19 | ROSA → harbor01 `.54` | TCP 443 | Optional Image Pull 후보 | 이하영 | DEC-P2-REG-01 / P2-HYB-01 | D22 선택, Source/Trust, Pull 또는 N/A | PROVISIONAL — D22 PENDING | NOT TESTED |
| IF-20 | OADP → S3 | TCP 443 | Backup Object Storage 후보 | 이하영 | P2-DR / OADP 후속 티켓 | Endpoint/Region/Bucket/Auth, Backup/Restore | PROVISIONAL — P2 DESIGN PENDING | NOT TESTED |

### 15.1.1 Alias / Supersession Register

| 과거/로컬 ID | 처리 | Canonical Contract |
|---|---|---|
| ICR v1.3 IF-21 | MERGED / 신규 Interface 아님 | IF-02 edge01→Worker:30080 |
| ICR v1.3 IF-22 | MERGED / 신규 Interface 아님 | IF-06 Prometheus→node-exporter:9100 |
| ICR v1.3 IF-23 Prometheus 부분 | MERGED | IF-06 Prometheus→kubelet:10250 |
| ICR v1.3 IF-23 Control Plane 부분 | SPLIT / CANONICALIZED | IF-12B Control Plane→Node:10250 |
| IF-24 Alertmanager→monitor01 Webhook | RETIRED / P1 N/A | IF-06B Prometheus→monitor01 Remote Write만 유지 |
| D-NET v2.3 monitor01→CP/Worker:9100/10250 | SUPERSEDED BY D33/D34/D35 | IF-06, IF-06A, IF-06B 사용; monitor01→Cluster workload 신규 Ingress DENY |

### 15.1.2 Open Interface Decisions

| Item | 미확정 내용 | 현재 통제 | Owner / Due |
|---|---|---|---|
| OID-01 Approved Admin → API LB | Grafana port-forward/운영 kubectl의 정확한 Source IP 및 Identity | IF-11 Runner만 허용; 별도 Admin Rule 적용 금지 | 이하영 / 이권욱 — P1-MON Runtime 전 |
| OID-02 Control Plane/System Image Registry | CP·Calico·kube-system Image를 Harbor에서 Pull할지 외부 Registry를 사용할지 | IF-10은 Worker만 허용 | 이하영 — P1-K8S Gate 1 전 |
| OID-03 Bootstrap Package/Registry Egress | 사전 반입 또는 HTTPS Egress Destination·Owner·Expiry | 미정의 Egress Permanent 허용 금지 | 이하영 / 이권욱 — 설치 실행 전 |
| OID-04 Management DNS | `.10/.20/.30`의 P1 DNS 사용 여부 | P1 범위 N/A로 종결; IF-13M 미구현 및 `.10` 제외 유지, 도입 시 Change Request | Closed by P1-DNS-01 Done — 2026-09-03 |

## 15.2 Interface Change Control

- Endpoint, Port, Protocol, Payload, Authentication 또는 Owner 변경은 Interface Change Request 대상이다.
- `FROZEN/APPROVED`는 설계 계약 상태이고 `PASS/FAIL/NOT TESTED`는 Runtime Evidence 상태다. 설계 승인만으로 Listener Ready·Bootstrap Release·Gate PASS를 선언하지 않는다.
- 중복 ID는 신규 구현 규칙으로 사용하지 않고 15.1.1의 Alias/Supersession Mapping을 통해 Canonical ID 하나에만 Evidence를 연결한다.
- 변경 전 Producer/Consumer, Network Allowlist, NetworkPolicy, Monitoring, Test Case 영향을 검토한다.
- 변경 후 Positive/Negative/Regression 결과와 Source/Configuration Version을 Evidence에 연결한다.
- 미정의 인터페이스는 기본 차단하며 임시 허용은 Owner, Expiry, 제거 조건을 기록한다.

---


배포 상태의 효력과 작성 시점은 `FDS_Release_Finalization_Record_v3.1.19.md` 및 CURRENT를 따른다.
