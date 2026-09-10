<!-- fds-canonical-description:v3.1.18 record-id:P1-MON-01 -->
# P1-MON-01 — Kubernetes-Integrated Hybrid Monitoring 구축 및 검증

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-MON-01 |
| Phase | Phase 1 |
| Category | Monitoring / Observability |
| Type | Task |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-09-07 |
| End | 2026-09-11 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이재환 |
| Support | 이권욱 |
| Exit Criteria | Hybrid Monitoring의 Runtime Acceptance 14개와 필수 보조통제 2개, 구축·복구·Rollback Runbook 및 Support Review 증적 확보 |
| Related Decision IDs | D05; D14; D17; D19; D33; D34 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #17 snapshot 2026-09-10T04:01:45Z |
| Schedule Note | 이재환 09-04 개인 휴가로 실행 착수를 09-07로 이동한다. 사전 Metrics/Target 설계는 유지하고, 이권욱 지원 아래 K8S/APP 준비 후 통합한다. G2 09-11 목표 유지. |

## 현재 실행·검토 상태

담당자 9/10 보고는 임시 k3s/fds 사전 실증이다. kube-state-metrics, Alertmanager 수신, Dashboard 일부는 보고됐지만 Prometheus/Grafana의 monitoring-api 이전, 3종 PVC, Default Deny, node-exporter DaemonSet/monitoring-node, Prometheus SA/RBAC, monitor01 Blackbox/remote_write가 미완료다. 정본 Runtime NOT VERIFIED / In Progress. Acceptance는 Baseline §11.6의 14개와 필수 보조통제 2개를 구분한다.

근거: [Issue #17](https://github.com/321Team/fds-project-baseline/issues/17), Issue 갱신 시각 `2026-09-10T04:01:45Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- [후속 기록](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-5612770657)

---

# Technical Story

모니터링 담당자로서 Kubernetes 내부의 Application·Cluster·Node 상태를 통합 관측하고 Grafana Dashboard와 Alertmanager를 통해 Review 가능한 운영 상태를 제공한다. 또한 Kubernetes 장애 시에도 `monitor01(.30)` 외부 Watchdog이 핵심 서비스 가용성과 Monitoring heartbeat 단절을 감지하도록 Hybrid Monitoring을 구축한다.

---

# Scope

## In Scope

- `monitoring-api`: Prometheus, Alertmanager, Grafana, kube-state-metrics 배포·Probe·Resource·PVC 구성
- `monitoring-node`: node-exporter DaemonSet 배포·Probe·Resource·Collector·read-only HostPath 구성
- Prometheus Target: Application, kube-state-metrics, node-exporter, kubelet, self
- Grafana P0 기본 View 3종: Application & FDS / Kubernetes Workload / Node & Monitoring Health
- Grafana Datasource와 Dashboard JSON의 Version-controlled Provisioning
- Test Alert의 Firing → Alertmanager 수신 → Resolved 전이
- Prometheus P0 목표 보존기간 15일과 `retention.size ≤ PVC 80%` 설정
- `monitor01(.30)` External Prometheus·Blackbox Exporter·TLS Reverse Proxy·제한 Remote Write 연계
- monitor01 Prometheus의 `--web.enable-remote-write-receiver` 활성화와 TLS Reverse Proxy 수신 Path 검증
- edge01 `.50:443` HTTPS Probe와 API LB `.109:6443` TCP Probe
- `fds_monitoring_heartbeat=1` 및 승인 self/target-health Metric의 HTTPS Remote Write
- IF-05, IF-05A, IF-05B, IF-06, IF-06A, IF-06B Runtime 검증
- Monitoring 전용 ServiceAccount·RBAC·NetworkPolicy·Host Firewall 통제의 공동 검증 및 Evidence
- 구축·운영·장애·복구·Rollback Runbook

## Out of Scope

- Application `/metrics`, `/readyz`, `/livez` 구현 — `P1-APP-01`
- Namespace/PSA/SecurityContext/NetworkPolicy/RBAC 기준 승인과 보안 Gate 소유 — `D-SEC-01`, `P1-SEC-01`
- Monitoring Image Registry·Robot Account·Trivy Gate 소유 — `P1-HBR-01`
- Runner 인증과 배포 Workflow 소유 — `P1-CICD-01`
- API LB 구축·Backend Health·Failover 소유 — `P1-LB-01`
- Prometheus 2 Replica, Alertmanager 3 Replica, PDB, TopologySpread, 고급 Dashboard/Alert, 장기 Metric 보존 — `P1-MON-02`
- Loki, SIEM, 장기 로그 보존
- Production 금융 규제 준수 또는 Production HA 적합성 주장

---

# 핵심 요구사항

## 1. Kubernetes 내부 배치

- [ ] `monitoring-api`에는 Prometheus, Alertmanager, Grafana, kube-state-metrics만 승인 범위로 배치한다.
- [ ] `monitoring-node`에는 node-exporter DaemonSet만 배치한다.
- [ ] Prometheus, Grafana, Alertmanager Service는 `ClusterIP`만 사용한다.
- [ ] Grafana 관리 접근은 승인 관리 단말의 `kubectl port-forward`만 허용한다.
- [ ] 모든 Image는 Harbor 승인 Repository의 Digest로 고정하고 Trivy 결과를 연결한다.

## 2. 보안 및 최소권한

- [ ] `monitoring-api` PSA Restricted와 `monitoring-node` 통제 예외를 적용한다.
- [ ] node-exporter Container는 `privileged=false`, `allowPrivilegeEscalation=false`, `seccomp=RuntimeDefault`, `capabilities.drop=ALL`을 유지한다.
- [ ] node-exporter HostPath는 전부 read-only이며 Kubernetes API RBAC를 부여하지 않는다.
- [ ] Prometheus와 kube-state-metrics RBAC는 승인된 읽기 Verb만 허용하고 Secret 읽기와 쓰기 Verb를 금지한다.
- [ ] Prometheus와 kube-state-metrics는 별도 ServiceAccount/ClusterRole을 사용하고 `nodes/proxy`를 금지한다.
- [ ] Grafana Anonymous Access, Sign-up, 기본 관리자 암호를 금지하고 자격정보를 Secret으로 관리한다.
- [ ] Default Deny 이후 필요한 Scrape, Datasource, Alert, Remote Write 경로만 허용한다.
- [ ] TCP 9100/10250은 Calico named HostEndpoint/GNP와 실제 Source 관측으로 검증한다.
- [ ] edge01을 통한 외부 `/metrics` 접근은 차단한다.

## 3. 저장·Dashboard·Alert

- [ ] Prometheus·Grafana·Alertmanager PVC와 Resource Request/Limit을 정의한다.
- [ ] P1-K8S가 제공한 static local StorageClass/PV가 `Bound`되고 `WaitForFirstConsumer`, `Retain`, nodeAffinity가 승인값과 일치한다.
- [ ] Prometheus 목표 보존기간 15일과 PVC 80% 상한을 적용한다.
- [ ] Datasource는 `http://prometheus.monitoring-api.svc:9090` Server-side Access로 Provisioning한다.
- [ ] P0 기본 Dashboard 3종과 기본 Alert Rule을 Source 관리한다.
- [ ] 외부 Plugin은 설치하지 않으며 필요 시 별도 승인·취약점 검토·Digest 고정을 수행한다.

## 4. 외부 Watchdog

- [ ] monitor01 `.30:443`은 Remote Write Path만 TLS Reverse Proxy로 수신한다.
- [ ] 프로젝트 Private CA가 서명한 monitor01 전용 Leaf와 IP SAN `.30`을 사용한다.
- [ ] Remote Write Payload는 heartbeat와 승인 self/target-health Metric으로 제한한다.
- [ ] 업무 Payload, 개인정보 Label, 전체 Application Metric 복제를 금지한다.
- [ ] `absent_over_time(fds_monitoring_heartbeat[5m])`로 단절을 탐지하고 복구 전이를 기록한다.
- [ ] IF-24 Alertmanager Webhook은 구성하지 않으며 Alertmanager는 외부 monitor01로 직접 송신하지 않는다.
- [ ] edge01 HTTPS와 API LB TCP Probe의 실패·복구를 외부 관점에서 기록한다.

---

# Acceptance Criteria

- [ ] App metrics `9091/9090`, kube-state-metrics, node-exporter, kubelet, Prometheus self Target이 모두 `UP`이다.
- [ ] 거래 호출 후 API/FDS/DB 저장 Metric과 Kubernetes/Node Metric 조회가 성공한다.
- [ ] Grafana 3개 기본 Dashboard가 Provisioning되고 Datasource Health가 PASS다.
- [ ] Grafana Service는 `ClusterIP`이며 Ingress·NodePort·LoadBalancer가 0건이다.
- [ ] 승인 관리 단말의 Port-forward는 성공하고 비승인 외부 접근은 실패한다.
- [ ] node-exporter의 PSA, Host Namespace, read-only HostPath, `privileged=false`, Image Digest, Collector Evidence를 확보한다.
- [ ] Prometheus·kube-state-metrics RBAC의 쓰기 Verb와 Secret 읽기 권한이 0건이다.
- [ ] NetworkPolicy Positive/Negative와 TCP 9100 Node Host Firewall Allowlist가 PASS다.
- [ ] edge01 `/metrics` 외부 접근은 403/404 또는 연결 차단되고 Cluster 내부 Scrape는 성공한다.
- [ ] Prometheus Pod 재시작 후 PVC 데이터와 Dashboard Query가 유지된다.
- [ ] Test Alert Firing → Alertmanager 수신 → Resolved 전이가 PASS다.
- [ ] In-cluster Prometheus 중단 후 monitor01이 5분 이내 heartbeat 단절을 감지하고 복구 후 정상 전환된다.
- [ ] edge01 HTTPS 또는 API LB TCP Probe 실패·복구 기록을 확보한다.
- [ ] Resource/PVC/Retention/Single-Replica Known Limitation과 구축·복구·Rollback 절차가 Runbook에 기록된다.
## 필수 보조통제 — 14개 Runtime Acceptance와 별도 집계

- [ ] kube-state-metrics Liveness `/livez:8080`, Readiness `/readyz:8081`과 각 Monitoring Component 공식 Probe가 PASS다.
- [ ] IF-06B Receiver flag, TLS/Auth, Payload Allowlist와 Return Route가 PASS이고 IF-24가 존재하지 않는다.

---

# 검증 및 증적

- Namespace/PSA Label, Deployment/StatefulSet/DaemonSet/Service/PVC 출력
- 적용 Image Digest와 Trivy 결과
- ServiceAccount/Role/ClusterRole/Binding YAML 및 `kubectl auth can-i` 결과
- NetworkPolicy와 Node Host Firewall 설정·Positive/Negative Test
- Prometheus Targets, PromQL 및 거래 전후 Metric
- Grafana Dashboard/Datasource Provisioning과 Health 캡처
- Alertmanager Firing/Resolved 캡처
- Remote Write Payload Allowlist, Private CA Trust, TLS/Auth 설정
- monitor01 Blackbox/Heartbeat Failure·Recovery 캡처
- Prometheus Restart/PVC Retention 결과
- Resource/PVC/Retention 확인 결과
- 구축·운영·장애·복구·Rollback Runbook
- Evidence Path: `docs/evidence/P1-MON-01/`

---

# Dependency

- **Blocked By (Runtime):** P1-K8S-01 Platform Ready, P1-APP-01 App `/metrics`·Service Ready, P1-SEC-01 Monitoring Security Control Apply, P1-LB-01 API LB `.109:6443` Ready
- **Decision / Control Prerequisite:** DEC-P1-MON-01/D33 Done, DEC-P1-TLS-01/D19 Done, D-SEC-01/D17/D34 Done
- **Blocks / Next:** P1-E2E-01, MS-G2-01, P1-MON-02, P1-DOC-01
- **Related Ticket:** P1-HBR-01, P1-CICD-01, P1-APP-01, P1-SEC-01, P1-LB-01
- **Milestone:** MS-G2-01 — Security / Feature Ready

---

# Interface

| ID | Source → Destination | Protocol / Port | 검증 |
|---|---|---|---|
| IF-05 | monitoring-api/Prometheus → transaction-api·fds-engine | TCP 9091/9090 | 업무 Port와 분리된 Target UP, App/FDS/DB Metric Query, edge01 `/metrics` DENY |
| IF-05A | monitoring-api/Grafana → Prometheus | TCP 9090 | Server-side Datasource Health PASS |
| IF-05B | monitoring-api/Prometheus → kube-state-metrics | TCP 8080 | Target UP, RBAC read-only |
| IF-05C | monitoring-api/Prometheus → Alertmanager | TCP 9093 | 내부 Alert Firing/Resolved, Default Deny Positive/Negative |
| IF-06 | monitoring-api/Prometheus → node-exporter·kubelet | TCP 9100/10250 HTTPS | Target UP, PSA Exception, Host Firewall, Auth Evidence |
| IF-06A | monitor01 `.30` → edge01 `.50` / API LB `.109` | TCP 443/6443 | Blackbox Failure/Recovery Evidence |
| IF-06B | monitoring-api/Prometheus → monitor01 `.30` | TCP 443 HTTPS | Payload Allowlist, TLS/Auth, 5분 이내 Heartbeat Loss Detection |

---

# Decision / Risk Control

- **Related Decision IDs:** D05, D14, D17, D19, D33, D34
- **Related Risk IDs:** RISK-04, RISK-07
- **Risk Control:** 비관리 Gateway와 Return Route는 ICMP 단독이 아닌 승인 TCP·Route·Source Evidence로 판정한다. Remote Write TLS는 D19 Trust를 사용하고, Default Deny·PSA·RBAC·Host Firewall은 D17/P1-SEC-01 통제와 함께 Positive/Negative Test한다.
- **Change Control:** Target, Port, Namespace, Exposure, Remote Write Payload, Retention, Collector, HostPath 또는 P0/P1 경계 변경은 D33과 Interface 영향도를 검토한 Change Request 없이 적용하지 않는다.

---

# Review / Handoff

- **이재환 / Lead:** Monitoring Manifest, Probe, Resource, PVC, Scrape, Dashboard, Alert, Watchdog 연계, Runtime Test와 Runbook 작성
- **이하영 / Security Reviewer·P1-SEC-01 Lead:** PSA, SecurityContext, RBAC, NetworkPolicy, Calico HEP/GNP, Secret encryption, Image/Exception 적합성 검토. WBS Support 변경 없이 관련 보안 티켓 책임으로 수행한다.
- **이권욱 / Support:** 단위 시험·영향성 Review, monitor01, Private CA/TLS 경로, API LB·edge01 Blackbox, Management Route, Interface와 Evidence 정합성 검토
- **P1-APP-01 Handoff:** Application `/metrics` Contract와 거래/FDS/DB Metric 제공
- **P1-HBR-01 Handoff:** 승인 Repository, Image Digest, Trivy 결과 제공
- **In Review 진입조건:** 14개 Acceptance 결과, Evidence Index, Known Issue, Recovery/Rollback Runbook을 제출하고 Support가 단위 시험과 영향성을 검토한다.

---

# Constraints / Known Limitation

- P0의 Prometheus, Alertmanager, Grafana 단일 Replica는 교육·PoC Known Limitation이다.
- P0 완료로 Production 금융 HA 또는 규제 준수를 주장하지 않는다.
- P1-MON-02는 P1-MON-01의 기본 Dashboard·기본 Alert·15일 Local Retention·Watchdog을 재구현하지 않는다.
- D-SEC-01/D17/D34 정본을 변경하려면 별도 Change Request와 영향도 검토가 필요하다.

---

# Rollback / Recovery

- 배포 전 Manifest·Config·Dashboard·Rule·Image Digest와 현재 Resource를 Backup 또는 Version Control로 보존한다.
- 장애 시 Monitoring Coverage 공백, Alert/Evidence 손실, IF-05/IF-06 및 Host Firewall 영향을 먼저 평가한다.
- Component 중지·복구, PVC 확인, Target 재등록, Alert Silence/복구, Watchdog 정상화 순서를 Runbook에 기록한다.
- node-exporter 예외 철회 시 DaemonSet과 TCP 9100 Allow Rule을 승인 절차로 제거하고 Coverage 공백을 Known Issue로 기록한다.
- monitor01의 과거 광범위 Node/Application Scrape는 승인 없이 복원하지 않는다.

---

# Completion Record / Done Definition

- **Result:** TBD
- **Status:** In Progress
- **Current Evidence State:** Design Fixed / Runtime Not Verified
- **Exit Criteria:** 14개 Runtime Acceptance 및 필수 보조통제 2개와 Evidence, Support 영향성 Review, 구축·운영·장애·복구·Rollback Runbook 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 이권욱·이하영·이재환 풀네임 사용
- **Done Definition:** Manifest 작성이나 Dashboard 화면만으로 Done 처리하지 않는다. 모든 Acceptance와 Evidence를 완료한 뒤 `In Review`로 제출하고 Support 검토와 승인 후에만 `Done`으로 전환한다.
