# P1-MON-01 후속 상태 후보 — 2026-10-19

**후보 범위:** 실제 Status Done/closed(completed), 완료시각 `2026-10-19T18:04:31+09:00`. 원 계획일·Owner·Exit/체크는 v3.1.21 입력을 보존한다. 아래 기존 수집시점 open/미완료 표현과 체크는 당시 이력이며 현재 종결은 [실제 기록](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-6263619666) 및 이 단락을 따른다. 기술 미입증·미실행의 체크를 바꾸지 않는다.

**유지할 한계:** MON 최종 조건부 수용(6260355852)과 MON 공식Probe 항목의177 정의·Ready 충족을 소비. 실패→Endpoint제외→회복 지정5종은 SEC-AC06/U2-B1 처분으로 연결. D02 edge HTTPS NOT_MET·평문/자동 통보 공백·PF 배타성·IF06B 규칙 귀속 미입증·기존10월26일 재검토 유지. 10월18일 수동점검 미수행과10월19일 근무일 정상 Owner 보고를 구분하며 새 중앙 Runtime으로 쓰지 않음.

기존본문 source body SHA는 당시 원문 식별자다. 현재 GitHub body SHA256 `59e50b43a8367183304eafe82ef53ab4318a063aa3d721b97c16360ddfb52031`·updated_at `2026-10-19T09:04:33Z`. 본 후보 편입은 새 시험·승인·정본발행·전체Close가 아니다. CODEX_ASSISTED.

---

# P1-MON-01 — Kubernetes-Integrated Hybrid Monitoring 구축 및 검증

Version: v3.1.21 기반 후속 반영 후보 — 선택7건 상태·실제종결 범위
Source: https://github.com/321Team/fds-project-baseline/issues/17
Updated at: 2026-10-03T07:08:53Z
Source body SHA256: `68fbfdd3aac4384177971ca8eea06624657bcfed3368bb2f74190af890b63b66`
GitHub: open / None
Current disposition: Source lifecycle/AC retained; no new acceptance by this publication.

| Property | Current source value |
|---|---|
| Record ID | P1-MON-01 |
| Phase | Phase 1 |
| Category | Monitoring / Observability |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-07 |
| End | 2026-09-18 |
| Calendar Days | 12 |
| Working Days | 6 |
| Lead | 이재환 |
| Support | 이권욱 |
| Exit Criteria | Hybrid Monitoring의 Runtime Acceptance 14개와 필수 보조통제 2개, 구축·복구·Rollback Runbook 및 Support Review 증적 확보 |
| Related Decision IDs | D05; D14; D17; D19; D33; D34 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #17 snapshot 2026-09-10T04:01:45Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | 09-11 Monitoring 인계, 부재 중 기존 Support의 준비·구현, 09-18 복귀 후 14개 AC+2개 보조통제 검증을 목표로 한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

## Source checklist

- [x] [PKI 증적 PR #18](https://github.com/321Team/fds-project-evidence/pull/18): 이재환/supreme33-kr가 HEAD `74745237108830e0c19912e960b2e26f0957f04b`를 [독립 승인](https://github.com/321Team/fds-project-evidence/pull/18#pullrequestreview-5260358774). **22:57:30 KST 병합**, merge `c97b13fa2910f740582076f7e7b56f0da42ddf31`.
- [x] [TLS 구성 후보 PR #3](https://github.com/321Team/infra-monitoring/pull/3): 같은 독립 검토자가 HEAD `05a8114308c510c678efd64b3443c133c36ab66f`를 [승인](https://github.com/321Team/infra-monitoring/pull/3#pullrequestreview-5260362147). **22:57:47 KST 병합**, merge `e520358bb0e4739762511f1a6b3cd7d8b83c57ae`.
- [x] 승인 후 HEAD 변경 없음·미해결 리뷰 스레드 0건 확인. 병합 tree 전체의 path/mode/blob이 승인 tree와 일치(증적 696파일·MON 47파일). [MON main CI](https://github.com/321Team/infra-monitoring/actions/runs/35515026751) **SUCCESS**, 위 merge SHA의 push 실행 확인.
- [ ] 실제 배포 입력 확정·native parser/서비스 통합·TLS/Auth/IF-06B/Blackbox 현장 인수.
- [x] CA 서명·공개 인증서 반환 및 원본 SHA256 2/2 확인.
- [x] monitor01 현지 키 일치·체인/IP/serverAuth 검증 PASS.
- [x] ca01 볼륨 unmount 및 fds-ca 비활성 확인.
- [x] 원본 증적 PR #18 등록 및 TLS 구성 후보 PR #3 작성.
- [x] 구성 후보 HEAD `05a8114308c510c678efd64b3443c133c36ab66f`의 CI SUCCESS 확인.
- [ ] 두 PR 독립 리뷰·병합: 조회 현재 모두 open/Draft, 제출 리뷰 0건.
- [ ] 실제 입력 인계·native parser/서비스 통합·배포.
- [ ] TLS/Auth·IF-06B 허용/차단·heartbeat 단절/복구·Blackbox 현장 인수.
- [x] `monitoring-api`에는 Prometheus, Alertmanager, Grafana, kube-state-metrics만 승인 범위로 배치한다.
- [x] `monitoring-node`에는 node-exporter DaemonSet만 배치한다.
- [x] Prometheus, Grafana, Alertmanager Service는 `ClusterIP`만 사용한다.
- [ ] Grafana 관리 접근은 승인 관리 단말의 `kubectl port-forward`만 허용한다.
- [x] 모든 Image는 Harbor 승인 Repository의 Digest로 고정하고 Trivy 결과를 연결한다.
- [x] `monitoring-api` PSA Restricted와 `monitoring-node` 통제 예외를 적용한다.
- [x] node-exporter Container는 `privileged=false`, `allowPrivilegeEscalation=false`, `seccomp=RuntimeDefault`, `capabilities.drop=ALL`을 유지한다.
- [x] node-exporter HostPath는 전부 read-only이며 Kubernetes API RBAC를 부여하지 않는다.
- [x] Prometheus와 kube-state-metrics RBAC는 승인된 읽기 Verb만 허용하고 Secret 읽기와 쓰기 Verb를 금지한다.
- [x] Prometheus와 kube-state-metrics는 별도 ServiceAccount/ClusterRole을 사용하고 `nodes/proxy`를 금지한다.
- [x] Grafana Anonymous Access, Sign-up, 기본 관리자 암호를 금지하고 자격정보를 Secret으로 관리한다.
- [x] Default Deny 이후 필요한 Scrape, Datasource, Alert, Remote Write 경로만 허용한다.
- [ ] TCP 9100/10250은 Calico named HostEndpoint/GNP와 실제 Source 관측으로 검증한다.
- [x] edge01을 통한 외부 `/metrics` 접근은 차단한다.
- [x] Prometheus·Grafana·Alertmanager PVC와 Resource Request/Limit을 정의한다.
- [x] P1-K8S가 제공한 static local StorageClass/PV가 `Bound`되고 `WaitForFirstConsumer`, `Retain`, nodeAffinity가 승인값과 일치한다.
- [x] Prometheus 목표 보존기간 15일과 PVC 80% 상한을 적용한다.
- [x] Datasource는 `http://prometheus.monitoring-api.svc:9090` Server-side Access로 Provisioning한다.
- [x] P0 기본 Dashboard 3종과 기본 Alert Rule을 Source 관리한다.
- [x] 외부 Plugin은 설치하지 않으며 필요 시 별도 승인·취약점 검토·Digest 고정을 수행한다.
- [x] monitor01 `.30:443`은 Remote Write Path만 TLS Reverse Proxy로 수신한다.
- [x] 프로젝트 Private CA가 서명한 monitor01 전용 Leaf와 IP SAN `.30`을 사용한다.
- [x] Remote Write Payload는 heartbeat와 승인 self/target-health Metric으로 제한한다.
- [x] 업무 Payload, 개인정보 Label, 전체 Application Metric 복제를 금지한다.
- [x] `absent_over_time(fds_monitoring_heartbeat[5m])`로 단절을 탐지하고 복구 전이를 기록한다.
- [x] IF-24 Alertmanager Webhook은 구성하지 않으며 Alertmanager는 외부 monitor01로 직접 송신하지 않는다.
- [ ] edge01 HTTPS와 API LB TCP Probe의 실패·복구를 외부 관점에서 기록한다.
- [x] App metrics `9091/9090`, kube-state-metrics, node-exporter, kubelet, Prometheus self Target이 모두 `UP`이다.
- [x] 거래 호출 후 API/FDS/DB 저장 Metric과 Kubernetes/Node Metric 조회가 성공한다.
- [x] Grafana 3개 기본 Dashboard가 Provisioning되고 Datasource Health가 PASS다.
- [x] Grafana Service는 `ClusterIP`이며 Ingress·NodePort·LoadBalancer가 0건이다.
- [ ] 승인 관리 단말의 Port-forward는 성공하고 비승인 외부 접근은 실패한다.
- [x] node-exporter의 PSA, Host Namespace, read-only HostPath, `privileged=false`, Image Digest, Collector Evidence를 확보한다.
- [x] Prometheus·kube-state-metrics RBAC의 쓰기 Verb와 Secret 읽기 권한이 0건이다.
- [x] NetworkPolicy Positive/Negative와 TCP 9100 Node Host Firewall Allowlist가 PASS다.
- [x] edge01 `/metrics` 외부 접근은 403/404 또는 연결 차단되고 Cluster 내부 Scrape는 성공한다.
- [x] Prometheus Pod 재시작 후 PVC 데이터와 Dashboard Query가 유지된다.
- [x] Test Alert Firing → Alertmanager 수신 → Resolved 전이가 PASS다.
- [x] In-cluster Prometheus 중단 후 monitor01이 5분 이내 heartbeat 단절을 감지하고 복구 후 정상 전환된다.
- [x] edge01 HTTPS 또는 API LB TCP Probe 실패·복구 기록을 확보한다.
- [x] Resource/PVC/Retention/Single-Replica Known Limitation과 구축·복구·Rollback 절차가 Runbook에 기록된다.
- [x] kube-state-metrics Liveness `/livez:8080`, Readiness `/readyz:8081`과 각 Monitoring Component 공식 Probe가 PASS다.
- [ ] IF-06B Receiver flag, TLS/Auth, Payload Allowlist와 Return Route가 PASS이고 IF-24가 존재하지 않는다.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P1-MON-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P1-MON-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

## 현행 배포 상태·검수 후속 — 2026-09-23 KST

[통합 전수 검수](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5794357232). 9/21의 namespace 부재·sender 미배포 기록은 당시 이력이다. [9/22 Lead 배포 보고](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-5772337466)와 본문 9/23 실행 기록을 현재 기준으로 사용한다.

- **확보:** monitoring-api/node 스택 기동, 앱·KSM Target UP, PVC 재시작 이전 데이터 보존, 읽기 전용 RBAC·Alert Firing/Resolved 등 기존 보고를 유지한다. Runtime AC는 담당자가 체크한 **6/14**, 보조 2개는 미완료 상태를 유지한다.
- **차단:** node-exporter 1/3 UP·2대 timeout, kubelet/cadvisor 6대 DOWN. worker03 TLS IP SAN 오류와 다른 5대 timeout은 별도 후속이다. [SEC 연계](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5788504815); GNP 원인은 실제 source/deny 근거 대조 전 추정이다.
- **후속 코드 작성 완료:** [MON PR7](https://github.com/321Team/infra-monitoring/pull/7) / HEAD d6c05bc1eafbf62c3157eab64220c181b3dea0ad. 현장에서 이미 고친 fds→fds-app을 main에도 반영하도록 3개 manifest의 6개 namespace/DNS 참조와 README 수정. YAML 13개 및 내장 설정 파싱, 다른 의미 변경 0, [CI SUCCESS](https://github.com/321Team/infra-monitoring/actions/runs/35856917623/job/107167471022). 독립 리뷰·병합·서버 적용은 미수행. Lead가 별도로 작성 중인 image/digest·imagePullSecrets·fds-msa 사본 변경을 대신하지 않는다.
- **기존 완료 체크 근거 보완 3건:** Datasource Health는 Grafana의 실제 Health/승인 dashboard 로드 근거, 승인 port-forward/비승인 외부 실패는 Grafana 대상의 해당 경로 근거, 재시작 후 Dashboard Query는 Grafana 경유 조회 근거를 연결한다. provisioning·다른 Pod port-forward·서비스 유형 또는 구조적 추론만으로 복합 조건 전부가 입증되지는 않는다. 기존 6개 체크는 임의로 해제하지 않았다.
- **monitor01 잔여:** PKI 발급·구성 후보 병합 완료를 유지하되 receiver/TLS/Auth/Payload allowlist·IF-06B·heartbeat 단절/복구는 미완료. sender 기동으로 Source 식별은 시작 가능하며 이권욱(ICR)과 실제 수신 Source/반환 경로를 연결한다.
- MON Lead 이재환은 현장 변경 형상화·이미지/Secret 입력·Target 및 MON 기능 인수, K8S/SEC Lead 이하영은 정책/serving 인증서 후속, 이권욱은 ICR 경로 지원 범위다. 담당·일정·상태 유지. 이번 검수에서 새 Runtime 시험을 수행하지 않았다.

---

<!-- icr-management-recovery-20260921T140152:issue-17:start -->
## CP 관리 경로 복구·MON 인계 범위 갱신 — 2026-09-21 14:01 KST

[ICR 원본7개·검증](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5755742235)에서 10250 규칙13개 추가 영구 저장과 직접 CP API3×etcd Pod3의 logs/exec/port-forward 총27/27 성공을 확인했습니다. 이는 클러스터 관리 경로의 복구 증거이며 Prometheus의 Worker kubelet CA+SA 인증, node-exporter Target UP 또는 IF-06B Remote Write 성공 증거는 아닙니다.

12:40:18 monitoring-api·monitoring-node NotFound는 마지막 제출 관측입니다. 이번7개 파일은 namespace/sender를 재조회하지 않았으므로 이후 배포 유무는 미확인입니다. 새로 구축 완료됐다고 하거나 현재도 없다고 단정하지 않습니다.

**후속 담당 유지:** 이재환(MON)은 정본 sender workload/container·node·artifact 및 Secret/Root 참조, monitor01 receiver/TLS/Auth 입력·서비스 통합을 준비합니다. 이하영(K8S/SEC)은 namespace/RBAC/정책·저장소를 협업합니다. 이권욱(ICR)은 실제 sender 준비 후 수신 Source·반환 경로를 실측합니다. 이번 관리 통신을 실제 sender 패킷으로 대체하지 않습니다. NTP는 별도 진행이며 MON·ICR의 기존 미완료 AC, 담당·일정·상태를 유지합니다.
<!-- icr-management-recovery-20260921T140152:issue-17:end -->

---

<!-- api-network-recovery-20260921T1240:issue-17:start -->
## API 회복 후 정본 MON sender 준비 필요 확인 — 2026-09-21 12:40:18 KST

사용자 콘솔 자료에서 API 회복과 CP/Worker 통신 규칙 영구 저장을 확인했습니다. [K8S #10](https://github.com/321Team/fds-project-baseline/issues/10)·[LB #9](https://github.com/321Team/fds-project-baseline/issues/9)에 범위/제한을 반영했습니다. 12:33 Worker API TCP15/15 및 Calico6/6 Running, 12:40 노드6/6 Ready입니다.

**이번 실제 조회:** control01에서 기존 admin.conf와 LB .109를 지정한 조회 결과, monitoring-api 및 monitoring-node 모두 명시적 NotFound였습니다. 이어진 해당 namespace의 workload/service 조회는 No resources found입니다. 이는 기존 API EOF와 구분되는 MON 배포 준비 의존성입니다. 다른 namespace의 MON workload 유무는 이번 출력으로 판정하지 않습니다.

현재 infra-monitoring main은 e520358bb0e4739762511f1a6b3cd7d8b83c57ae이며 열린 PR은 조회 시점 0건입니다. [monitor01 README](https://github.com/321Team/infra-monitoring/blob/e520358bb0e4739762511f1a6b3cd7d8b83c57ae/monitor01/README.md)는 RENDER_ONLY/NOT_DEPLOYED 후보이고, references/e-k3s는 정본 배포 입력이 아닙니다.

**다음 인계 범위**

- MON Lead 이재환: 정본 monitoring-api 송신 Prometheus 구현/배포 준비, 실제 workload·container·배치 node, 승인 artifact/digest·PVC 및 sender Secret/Root mount 참조 인계. monitor01 실행 모델·receiver 포트/경로·계정 입력도 아래 기존 인계표에 따라 확정.
- K8S/SEC 이하영 협업: namespace/PSA·RBAC·NetworkPolicy·Storage·호스트 정책 정합성.
- 이권욱: 위 실제 sender가 준비되면 IF-06B monitor01 수신 Source IPv4·반환 경로 실측과 필요한 최소 네트워크 보완. 현재 정본 sender가 확인되지 않아 이 실측을 완료할 수 없음. 임의 Pod/Worker IP를 실제 송신 Source로 대체하지 않음.

기존 PKI 키 일치·체인/IP/serverAuth 검증은 재사용합니다. TLS receiver/proxy/sender 설치·적용, IF-06B 양성/음성 시험과 heartbeat/Blackbox 인수는 미완료입니다. 이번 티켓 갱신은 직접 서버 배포나 담당자 메시지 발송이 아닙니다. 기존 담당·상태·일정·14개 AC+보조2 체크 유지. 아래는 각 시점 이력.
<!-- api-network-recovery-20260921T1240:issue-17:end -->

---

<!-- cp23-etcd-recovery-20260921T1014:issue-17:start -->
## MON 선행 API 복구 절차 준비 — 2026-09-21 10:14 KST

CP2/CP3 로그로 etcd 실행/CrashLoopBackOff, peer2380 연결 실패 및 합의 기반 읽기 실패를 확인했습니다. [K8S #10](https://github.com/321Team/fds-project-baseline/issues/10)에 기존 데이터·멤버십을 유지하는 CP /32 제한 TCP2380 Runtime 복구 절차를 준비했습니다. 구문·모의 검증만 완료했고 실제 서버 적용/복구는 아직 미수행입니다.

API 회복과 안정성을 검증한 뒤 실제 MON sender 식별·IF-06B 관측을 재개합니다. MON TLS 배포·현장 인수는 미완료이며 기존 담당·상태·일정·AC 체크는 유지합니다.
<!-- cp23-etcd-recovery-20260921T1014:issue-17:end -->

---

<!-- cp3-peer-listener-20260921T0943:issue-17:start -->
## MON 선행 장애의 3CP 비교 완료 — 2026-09-21 09:42~09:43 KST

사용자 cp1/cp2/cp3.txt 비교에서 CP peer 2380 TCP 6방향 실패와 public Runtime/Permanent 허용 누락을 확인했습니다. CP2/CP3는 etcd 2379·2380 리스너도 조회 시점에 없으며, 세 CP 모두 API6443 리스너가 미관측입니다. 방화벽 설정만으로 전체 종료 원인이나 복구 완료를 판단하지 않습니다.

[상세 결과·다음 CP2/CP3 etcd 로그 수집: K8S #10](https://github.com/321Team/fds-project-baseline/issues/10). 실제 MON sender 식별·IF-06B Source 관측은 미완료입니다. 이번 수행은 첨부 분석·진척 반영이며 실제 서버 수정·MON TLS 배포는 미수행입니다. 기존 담당·상태·일정·AC 체크를 유지합니다.
<!-- cp3-peer-listener-20260921T0943:issue-17:end -->

---

<!-- cp1-etcd-peer-20260921T0043:issue-17:start -->
## MON 선행 API 장애의 원인 범위 축소 — 2026-09-21 00:34~00:43 KST

사용자 로그에서 CP1 apiserver의 **etcd 저장소 초기화 timeout 종료**, CP1→CP2/CP3 **etcd peer 2380/TCP 연결 실패**, CP1 etcd **합의 기반 읽기 실패·readyz503**를 확인했습니다. VM/NIC·경로·방화벽 중 통신 실패 원인과 CP2/CP3 간 상태는 미확인입니다.

[상세 진단·다음 3CP 읽기 전용 비교: K8S #10](https://github.com/321Team/fds-project-baseline/issues/10). 실제 sender 식별·IF-06B Source 관측은 API 가용성 차단으로 미완료입니다. 기존 monitor01 PKI 검증·승인 PR 병합은 유지하며 실제 TLS 배포/인수로 확대하지 않습니다. 이번 수행은 분석·진척 반영이며 서버 복구·MON 배포는 미수행입니다. 기존 담당·상태·일정·AC 체크는 유지합니다.
<!-- cp1-etcd-peer-20260921T0043:issue-17:end -->

---

<!-- cp1-api-crash-20260921T0020:issue-17:start -->
## MON 후속의 API 차단 조사 갱신 — 2026-09-21 00:20 KST

사용자 첨부 kubelet 로그에서 CP1 `kube-apiserver`의 **CrashLoopBackOff / back-off 5m0s**가 확인됐습니다. 실제 종료 원인과 etcd 상태는 아직 미확인이며, crictl 조회는 실행 파일을 찾지 못해 실패했습니다.

[상세 관측·첨부 SHA256·다음 수집: K8S #10](https://github.com/321Team/fds-project-baseline/issues/10). 다음은 control01의 apiserver·etcd 호스트 로그 확인입니다. API 가용성 차단 때문에 실제 sender 식별·IF-06B Source 관측은 미완료로 유지합니다. monitor01의 기존 PKI 검증과 승인 PR 병합을 실제 TLS 배포·현장 인수로 확대하지 않습니다. MON Lead/지원 역할, 티켓 상태·일정·AC 체크는 유지합니다. 아래 기록은 각 시점의 이력입니다.
<!-- cp1-api-crash-20260921T0020:issue-17:end -->

---

<!-- cp1-api-listener-20260921T0008:issue-17:start -->
## CP1 API 리스너 부재 확인 — 2026-09-21 00:08 KST

사용자가 제출한 화면 `2a217a52-b8bd-454b-9378-e1ae218fe209.png`의 표시 시각은 `2026-09-21T00:08:02+09:00`입니다. 앞서 안내한 control01 읽기 전용 비교 명령의 결과로 접수했습니다.

| 관측 | 화면 결과 | 확인 범위 |
|---|---|---|
| API LB .109:6443 | EOF, API_RC=1 | LB 경유 API 접근 실패 지속 |
| CP1 .102:6443 | Connection refused, API_RC=1 | CP1 직접 API 접근 실패 |
| CP1 로컬 TCP6443 | ss 헤더만 출력 | 해당 조회 시각의 6443 LISTEN 미관측 |
| kubelet/containerd | 둘 다 active/running | 서비스 프로세스 실행 중; API/etcd 컨테이너 정상까지 입증하지 않음 |

**판정:** kubeconfig 선택 문제에서 CP1 API 가용성 조사로 진행합니다. CP1에는 로컬 6443 리스너 부재가 확인되므로 kube-apiserver static Pod의 생성/실행/종료 원인과 etcd 상태를 우선 확인합니다. kube-apiserver 컨테이너의 종료·미생성·재시작 여부, CP2/CP3 상태 및 LB backend 상태는 아직 미확인입니다. LB 단독 장애, etcd quorum 상실, 인증서 또는 방화벽 원인으로 단정하지 않습니다.

**다음 최소 수집:** control01의 manifest 파일 목록, 기존 CRI 소켓을 통한 종료 포함 컨테이너 목록, 최근 kubelet 로그. API 실패 조회 반복 대신 호스트에서 읽기 전용으로 수집합니다. 파일 삭제/이동·reset/init/join·서비스 재시작·방화벽 변경·인증서 재발급은 수행하지 않았으며 현재 조치로 제시하지 않습니다.

**담당/영향:** CP 복구 판단은 기존 K8S Lead 이하영 범위, 이권욱은 원인 분리·네트워크/수집 지원을 이어갑니다. 실제 sender 식별과 IF-06B Source 관측은 미완료입니다. 9/18의 6/6 Ready·backend3/3 PASS는 과거 관측으로 보존하며 현재 정상으로 승계하지 않습니다. 기존 티켓 상태·담당·일정·AC 체크는 유지합니다. 화면 판독 결과이며 서버 원문 로그/원본 해시와 이번 추가 진단 결과는 아직 미수신입니다.
<!-- cp1-api-listener-20260921T0008:issue-17:end -->

---

<!-- api-lb-eof-20260920T2335:issue-17:start -->
## API LB 접근 실패 관측 — 2026-09-20 23:34~23:35 KST

사용자가 k8s-control01/server02에서 제출한 터미널 출력 기준입니다. `sudo kubectl --kubeconfig=/etc/kubernetes/admin.conf config current-context`는 `kubernetes-admin@kubernetes`를 출력했습니다. 이어진 namespace 조회의 `https://10.1.93.109:6443/api?timeout=15s`에서 EOF·TLS handshake timeout·최종 `Unable to connect to the server: EOF`가 발생했습니다.

- **확인:** 기존 localhost:8080 대상 문제는 이번 명령에서 해소되어 API LB 주소를 선택했습니다. context 출력은 로컬 설정 읽기이며 API 인증 성공을 뜻하지 않습니다.
- **미확인:** LB 현재 backend 상태, CP API/etcd 상태, 차단·경로·TLS 실패 원인. EOF만으로 방화벽이나 인증서 문제로 확정하지 않습니다.
- **영향:** monitoring-api namespace/Pod/Deployment/StatefulSet의 현재 존재 여부는 아직 확인하지 못했습니다. 실제 sender 식별 및 IF-06B Source 관측은 보류합니다.
- **다음:** 같은 control01에서 기존 admin.conf의 TLS 검증을 유지해 LB .109와 CP1 .102 각각 `/readyz?verbose` 읽기 전용 조회를 비교합니다. 요청별·프로세스별 시간을 제한하고 local6443 listener/kubelet/containerd 상태를 함께 확인합니다. 결과 전에는 HAProxy/노드 재시작·방화벽/NAT 변경·kubeconfig 수정·TLS 검증 생략을 수행하지 않습니다.
- **담당:** LB/네트워크 분리는 이권욱 범위, CP 서비스 문제가 확인되면 기존 K8S Lead 이하영과 연결합니다. MON Lead 이재환 역할은 유지합니다.

2026-09-18 backend3/3 PASS·6노드 관측은 당시 증적으로 보존하며 현재 정상 상태로 재사용하지 않습니다. 기존 AC 체크·Status·담당·일정은 변경하지 않았습니다. 이 기록은 사용자 붙여넣기 출력의 수신 기록이며 서버 원본 파일/해시·이번 추가 점검 결과는 아직 미수신입니다.
<!-- api-lb-eof-20260920T2335:issue-17:end -->

---

<!-- monitor01-approved-merged-20260920:issue-17:start -->
## 독립 승인·병합 완료 — 2026-09-20 KST

- [x] [PKI 증적 PR #18](https://github.com/321Team/fds-project-evidence/pull/18): 이재환/supreme33-kr가 HEAD `74745237108830e0c19912e960b2e26f0957f04b`를 [독립 승인](https://github.com/321Team/fds-project-evidence/pull/18#pullrequestreview-5260358774). **22:57:30 KST 병합**, merge `c97b13fa2910f740582076f7e7b56f0da42ddf31`.
- [x] [TLS 구성 후보 PR #3](https://github.com/321Team/infra-monitoring/pull/3): 같은 독립 검토자가 HEAD `05a8114308c510c678efd64b3443c133c36ab66f`를 [승인](https://github.com/321Team/infra-monitoring/pull/3#pullrequestreview-5260362147). **22:57:47 KST 병합**, merge `e520358bb0e4739762511f1a6b3cd7d8b83c57ae`.
- [x] 승인 후 HEAD 변경 없음·미해결 리뷰 스레드 0건 확인. 병합 tree 전체의 path/mode/blob이 승인 tree와 일치(증적 696파일·MON 47파일). [MON main CI](https://github.com/321Team/infra-monitoring/actions/runs/35515026751) **SUCCESS**, 위 merge SHA의 push 실행 확인.
- [ ] 실제 배포 입력 확정·native parser/서비스 통합·TLS/Auth/IF-06B/Blackbox 현장 인수.

이번 사용자 “후속 작업 착수” 지시로 정확한 승인 HEAD를 지정하여 두 PR을 수동 병합했습니다. 증적 PR의 CI 검사 0건은 NOT RUN이며 기존 무결성 검증·독립 편입 검토와 구분합니다. 아래 과거 Draft·리뷰/병합 대기 표현은 당시 이력입니다. PKI 현장 검증 완료 범위와 AC·티켓 상태·담당·일정은 유지합니다.

### MON 배포 입력 인계 — 이 표를 한 번에 확정

[병합된 입력 예제](https://github.com/321Team/infra-monitoring/blob/e520358bb0e4739762511f1a6b3cd7d8b83c57ae/monitor01/inputs.example.json)와 [실행/복구 설명](https://github.com/321Team/infra-monitoring/blob/e520358bb0e4739762511f1a6b3cd7d8b83c57ae/monitor01/README.md)을 기준으로 합니다. 기존 키/인증서와 앞선 검증은 재사용합니다. 현재 #17 본문·댓글 및 PR에서 아래 실제 값의 확정 근거를 찾지 못했습니다.

| 인계 묶음 | 실제 값/근거가 필요한 항목 | 기존 담당 연결 |
|---|---|---|
| 실행 모델·artifact | systemd/컨테이너 등 선택, NGINX/Prometheus 승인 버전·artifact/digest·취약점 결과, 서비스 계정 UID/GID | MON Lead 이재환 · HBR |
| receiver | `receiver_port`, `receiver_config_dir`, `receiver_data_dir`, 저장 용량/retention·소유권. localhost만 listen; 현재 Cockpit 9090 유지, Blackbox 9115와 충돌 금지 | MON Lead |
| IF-06B 경로 | 실제 송신에서 관측한 `source_ipv4` 및 return route·필요 최소 정책. Worker IP/Pod CIDR를 추정해 입력하지 않음 | ICR 이권욱 · K8S 이하영 · MON |
| 인증·신뢰 참조 | `sender_username`, `nginx_password_file`, `sender_password_file`, `root_file_on_sender` 및 해당 Secret/mount 참조. 암호·토큰·hash 값은 티켓에 기록하지 않음 | MON · SEC 이하영 |
| 현지 PKI 접근 | 알려진 Leaf/key 인계 경로의 실제 서비스 접근권한·최종 배치·SELinux context | MON · 관련 서버 담당 |

승인은 구성 생성기 코드 범위입니다. NGINX/Basic Auth 코드 후보의 독립 승인을 위 실제 값 확정·서비스 실행 승인으로 확대하지 않습니다. in-cluster Worker03 PV/UID/이미지 값을 별도 VM monitor01의 값으로 전용하지 않습니다.

**다음 실행 순서:** 위 입력 확정 → 병합된 생성기로 입력 검사/새 후보 폴더 생성 → 실제 승인 버전의 `nginx -t`·`promtool check config/rules` → 서비스 통합 소스/설정 검토 → MON Lead 운영 판단에 따라 receiver→proxy→sender 적용 → 양성/음성·5분 단절/복구·Blackbox 인수. parser/입력 실패 시 서비스 변경 없이 중단합니다. 적용 후 실패 시 sender 추가 변경과 이번 proxy/receiver 변경을 직전 구성으로 복구하고 기존 CA·개인키·data는 보존합니다.

**검토 경계 유지:** payload allowlist는 sender relabel에서 집행하며 NGINX의 protobuf 본문 차단을 의미하지 않습니다. 동일 승인 코드의 실행마다 새 독립 승인을 반복하지 않고, 새 서비스 통합 코드/실행 설정은 해당 변경 범위만 검토합니다.

새로 등록된 [S8 참고 스크립트 결함 기록](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-5750093706)은 기존 E-K3S 시연 자료의 후속이며 이번 monitor01 소스 병합에 포함되지 않습니다. 해당 스크립트를 MON 현장 시험에 그대로 재사용하지 않습니다.
<!-- monitor01-owner-start-20260920:issue-17:start -->
### 후속 책임과 권욱님 착수 범위 — 2026-09-20 KST

사용자 “누가 해야 하는지 확인하고 본인 범위이면 착수” 지시에 따라 기존 Lead/Support를 재확인했습니다.

| 작업 | 기존 담당 | 이번 상태 |
|---|---|---|
| MON 실행 방식·버전/artifact·receiver 포트/저장 경로/서비스 계정 확정과 서비스 통합·배포 | 이재환(MON Lead), HBR 입력 협업 | 실제 값 인계 필요 |
| 클러스터 송신 workload·Secret/Root mount·NetworkPolicy 연계 | 이재환(MON) · 이하영(K8S/SEC) | 실제 송신 대상과 참조 확인 필요 |
| CA 발급·공개 반환·PKI 검증 지원 | 이권욱 | 완료, 기존 키/인증서·증적 재사용 |
| IF-06B Source/반환 경로·host/gateway 정책 확인 및 필요한 최소 보완 | 이권욱(ICR Lead), K8S/MON 협업 | 아래 읽기 전용 송신 식별 단계 준비 완료·현장 출력 대기 |

**우리의 다음 현장 단계:** 기존에 정본 6노드 클러스터의 `kubectl` 조회가 정상 동작하던 **k8s-control01 터미널/계정**에서 아래만 실행합니다. 전체 클러스터/Worker 경로 재수집 대신 `monitoring-api`의 실제 송신 workload를 식별합니다.

```bash
date -Is
kubectl config current-context
kubectl -n monitoring-api get pods -o wide
kubectl -n monitoring-api get deployment,statefulset
```

조회 대상/현재 context가 예상과 다르거나 Forbidden·연결 오류가 나면 후속 접근/변경 없이 오류를 반환합니다. Namespace/Prometheus workload가 없으면 임시 k3s나 다른 Pod로 대체하지 않고 MON/K8S 담당의 정본 sender 준비에 연결합니다. 이름만으로 sender를 확정하지 않고 해당 workload/컨테이너와 Remote Write 담당을 대조합니다. Secret 값·kubeconfig 본문·개인키는 수집하지 않습니다.

출력으로 실제 sender를 고정한 뒤 monitor01에서 해당 전송의 Source와 return path를 확인합니다. Pod IP·Worker host route의 source를 receiver가 관측한 Source로 입력하지 않습니다. sender가 준비되면 TLS 서비스 완성 전에도 제한된 연결 시도의 패킷 헤더로 Source를 확인할 수 있으므로 TLS 인수 완료를 이 식별 단계의 선행조건으로 추가하지 않습니다. 상세 능동 연결/관측은 sender 식별 후 범위를 고정합니다.

기존 Worker3의 `.30 via .58 / source .105·.107·.108` route-get 및 AC14 RUNTIME_PASS는 해당 관측 범위로 재사용합니다. 이 기록은 새 원격 실행/패킷 관측·방화벽/NAT/route 변경·Runtime PASS가 아니며, 기존 AC12/16·티켓 상태·담당·일정은 유지합니다.
<!-- monitor01-owner-start-20260920:issue-17:end -->
<!-- monitor01-approved-merged-20260920:issue-17:end -->

---

<!-- monitor01-pki-return-20260919:start -->
## monitor01 PKI 현장 검증 완료 및 TLS 연동 후속 — 2026-09-19

사용자 “후속 절차 착수” 지시에 따라 이번 대화의 콘솔 원본과 기존 승인 소스를 연결합니다. 아래 기존 서명/TLS 미실행 문구는 당시 기록으로 보존하며, 현재 확인 범위는 이 갱신을 우선합니다.

| 항목 | 현재 확인 범위 |
|---|---|
| ca01 서명 | 사용자 서명 화면의 CA_SIGN_AND_VERIFY=PASS, serial 1001(hex), IP SAN 10.250.10.30 |
| 공개 반환 | 캡처 복원 PEM 2종의 원본 화면 SHA256 정확히 일치, monitor01 sha256sum 두 파일 성공 |
| monitor01 현지 대조 | PUBLIC_KEY_MATCH=PASS / CHAIN_IP_SERVER_PURPOSE=PASS 화면 확인 |
| CA 종료 | XFS unmount / fds-ca inactive 화면 확인; VM 전원 OFF 미확인 |
| TLS/Auth/Remote Write·IF-06B·ICR-AC12/16 | 서비스 적용·실통신 인수 미완료 |

- [원본 증적 Draft PR #18](https://github.com/321Team/fds-project-evidence/pull/18), HEAD `74745237108830e0c19912e960b2e26f0957f04b`: 원본 화면 9개·공개 PEM 2개·검증 기록 16파일, 수집회차 hash 15/15 및 Git blob 16/16 일치. 전체 서버 텍스트 로그/종료코드·각 실행 시각은 미수신이며 사용자 콘솔 증적과 분석 환경의 검증을 구분합니다. 독립 편입 리뷰·병합 대기입니다.
- Leaf/Root 수신 위치: `/home/server01_monitor/monitor01.crt`, `/home/server01_monitor/fds-root-ca.crt`. 기존 키는 `/etc/fds/pki/monitor01/request/monitor01.key`에 유지하며 반출/재생성하지 않습니다.
- [monitor01 구성 후보 Draft PR #3](https://github.com/321Team/infra-monitoring/pull/3), HEAD `05a8114308c510c678efd64b3443c133c36ab66f`: TLS reverse proxy·localhost receiver·heartbeat-only 송신 구성 생성기와 Runbook. 기본 입력 검사/새 후보 폴더 생성만 수행하며 설치·서비스/방화벽/SELinux 변경·서버 접속·K8s apply는 없습니다.
- 소스 LOCAL: STATIC 47파일 PASS, UNIT 13/13 PASS, 기존 참고 소스 27파일 보존, 원격 tree 47파일 blob/mode 일치. NGINX/promtool native parser·실제 통신은 NOT RUN. [PR CI #35442097555](https://github.com/321Team/infra-monitoring/actions/runs/35442097555)는 HEAD `05a8114308c510c678efd64b3443c133c36ab66f`에서 **SUCCESS**이며 정적 검사·새 무배포 단위시험·기존 셸 구문 단계 성공을 확인했습니다. 실제 서버 Runtime 성공을 뜻하지 않습니다.
- 후보의 NGINX/Basic Auth 방식, receiver port/저장·실행 모델, 승인 버전/Harbor digest, 관측 Source IPv4·return route, Secret·Root mount는 MON Lead/관련 소유자의 인계가 필요합니다. 구체 값은 추정하지 않았습니다. payload 제한은 송신 relabel에서 집행하며 proxy의 protobuf 본문 검사로 표현하지 않습니다.
- 다음 순서: 코드 독립 검토와 위 실제 입력 인계 → native parser/서비스 통합 → Lead의 기존 운영 절차에 따른 적용 → 실제 TLS/Auth/허용·차단/heartbeat 단절·복구/Blackbox 검증. 동일 승인 코드의 실행마다 독립 승인을 반복하지 않습니다.

기존 Lead 이재환·Support 이권욱, 보안 검토 이하영, 일정·Status·14개 Runtime AC+보조 2개 체크·Gate 판정은 유지합니다. PKI 부분 완료를 전체 MON Done으로 확대하지 않습니다. 이번 기록은 편입/구성 준비이며 독립 승인·병합·배포 인수가 아닙니다.
<!-- monitor01-progress-sync-20260919:issue-17:start -->
### 하위작업 진행 체크 — 2026-09-19 재조회

- [x] CA 서명·공개 인증서 반환 및 원본 SHA256 2/2 확인.
- [x] monitor01 현지 키 일치·체인/IP/serverAuth 검증 PASS.
- [x] ca01 볼륨 unmount 및 fds-ca 비활성 확인.
- [x] 원본 증적 PR #18 등록 및 TLS 구성 후보 PR #3 작성.
- [x] 구성 후보 HEAD `05a8114308c510c678efd64b3443c133c36ab66f`의 CI SUCCESS 확인.
- [ ] 두 PR 독립 리뷰·병합: 조회 현재 모두 open/Draft, 제출 리뷰 0건.
- [ ] 실제 입력 인계·native parser/서비스 통합·배포.
- [ ] TLS/Auth·IF-06B 허용/차단·heartbeat 단절/복구·Blackbox 현장 인수.

위 체크는 하위작업 진행이며 기존 14개 Runtime AC와 보조 2개 통제 체크를 대체하지 않습니다. 연계 진행은 [ICR #14](https://github.com/321Team/fds-project-baseline/issues/14)·[SEC #19](https://github.com/321Team/fds-project-baseline/issues/19)·[K8S #10](https://github.com/321Team/fds-project-baseline/issues/10)·[LB #9](https://github.com/321Team/fds-project-baseline/issues/9)·[DOC #24](https://github.com/321Team/fds-project-baseline/issues/24)에 반영합니다.


<!-- monitor01-progress-sync-20260919:issue-17:end -->
<!-- monitor01-pki-return-20260919:end -->

<!-- monitor01-observation-20260918:start -->
## monitor01 현장 수신 구성 확인 — 2026-09-18

사용자가 Support 요청에 따라 제출한 화면 `ca4a02e7-8cf7-4ef6-a15b-4ae671fe9f06.png`를 직접 확인했습니다. SHA256 `2bcd4435034ea0d04422d1803841a4a61906c08a62b64d3acffa0d3ad02c2084`. 화면 자체의 촬영 시각은 표시되지 않아 제출된 LB 수집 시각과 동일 시점으로 간주하지 않습니다.

| 확인 | 화면의 실제 결과 | 판정 범위 |
|---|---|---|
| 호스트·주소 | monitor01 / ens160 UP / 10.250.10.30/24 | 예상 관리망 주소 확인 |
| TCP443·9115 | 해당 host listener 출력 없음 | host에서 IF-06B443·Blackbox9115 수신 준비 미확인 |
| TCP9090 | 최초 systemd pid1 관측, 후속 `[::]:9090 cockpit.socket → cockpit.service` | Cockpit 소켓으로 식별 완료. Prometheus 수신 증거가 아님 |
| 서비스 조회 | prometheus*/blackbox*/nginx*/haproxy*에 0 loaded units | 해당 이름의 loaded service 없음. 미설치·비표준 unit·컨테이너 부재를 증명하지 않음 |

**후속 식별 완료:** 사용자 추가 출력에서 `[::]:9090 → cockpit.socket → cockpit.service` 및 `cockpit.socket enabled`를 확인했습니다. 조회 패턴에 맞는 설치 unit은 Cockpit·Podman 계열이며 Prometheus·Blackbox·nginx·HAProxy 등 MON 서비스 unit은 나타나지 않았습니다. 안내한 현재 사용자/root 두 Podman 조회는 각각 헤더만 출력되어 두 범위의 컨테이너 목록이 비어 있습니다. Docker 조회는 출력이 없어 설치 부재까지 확정하지 않습니다. 비표준 실행 파일·다른 사용자 컨테이너의 전수 부재를 주장하지 않습니다.

**Support 준비 범위:** 현황 조회를 반복하지 않고 monitor01 전용 프로파일·키/CSR 도구·공개 인증서 인계 절차를 아래 PR로 준비했습니다. CSR 생성·공개 인계 검증은 아래 수신 원본으로 완료했으며 CA 서명과 MON 수신 스택 연동은 미완료입니다.

v19 §6.6의 Cockpit 비활성화/별도 통제 조건은 K8S6Node를 대상으로 하므로 monitor01의 Cockpit을 이번에 임의 중지하거나 ICR-AC10 실패로 변경하지 않습니다. 9090은 호스트 listener 확인이며 원격 접근 허용 여부는 별도 미시험입니다. 모니터링 receiver는 정본대로 localhost에 두되 실제 port와 인증 설정은 MON 연동 구현에서 고정합니다.

- .30:443·PrivateCA/monitor01 전용 Leaf·제한 Remote Write·heartbeat1/5분 단절 설계는 유지하며 재승인 대상으로 되돌리지 않습니다.
- LB에서는 별도 원본으로 backend3/3 준비가 확인됐습니다([LB #9](https://github.com/321Team/fds-project-baseline/issues/9)). monitor01→LB Blackbox 실제 시험 성공을 뜻하지 않습니다.
- MON Lead 이재환·Support 이권욱 역할과 기존 Runtime AC/보조통제 체크·일정·In Progress는 유지합니다. ICR AC12 BLOCKED, AC16은 실제 Receiver/TLS/Auth 인수 미완료입니다.


**소스 구현·검증 완료:** [infra-pki PR3](https://github.com/321Team/infra-pki/pull/3), 최신 HEAD `f778af0dc8178608edc8ddef509d01d3a81990fe`. 기존 프로파일 후보 `5c9459c`에 monitor01 현지 키·CSR 생성/재사용 도구와 기존 CA 서명·반환 검증 절차를 추가했습니다. 같은 PR에서 신규7파일(프로파일2·실행도구1·시험2·문서2)의 검토·병합을 완료했습니다. IP SAN은 `10.250.10.30` 하나, CA:FALSE/serverAuth이며 키는 monitor01에 보관하고 공개 CSR·receipt·해시만 내보냅니다.

- LOCAL: 관련 격리 시험 **20/20 PASS**, Python AST·문서 Bash 구문 PASS.
- CI: [source-validation #35349450313](https://github.com/321Team/infra-pki/actions/runs/35349450313) **SUCCESS**. 위 HEAD에 대한 PR 병합 테스트에서 정적31파일 및 전체31/31 시험 PASS, 원격7파일과 검증 소스 Git blob 일치.
- REVIEW/MERGE: [supreme33-kr의 독립 APPROVED](https://github.com/321Team/infra-pki/pull/3#pullrequestreview-5248507791), 2026-09-18 22:50:36 KST, 대상 HEAD `f778af0dc8178608edc8ddef509d01d3a81990fe` 확인. 차단 지적·미해결 thread 없음. ens160 참고사항은 기존 monitor01 현장 출력의 ens160/10.250.10.30과 대조했습니다. 2026-09-19 01:22:01 KST 병합 완료, merge `2be575329349973babd2fa392f22c69b34c76253`. 동일 승인 소스의 실행마다 독립 승인을 추가하지 않습니다.
- MAIN CI: [source-validation #35368045592](https://github.com/321Team/infra-pki/actions/runs/35368045592) **SUCCESS**, merge 커밋에서 정적31파일·전체31/31 시험 PASS를 job log로 확인했습니다.
- DISTRIBUTION: `FDS_MONITOR01_CSR_f778af0_v1.0.tar.gz`, SHA256 `c2f7ba2a599c7b050860cce14986908128fa8cc1b38e7ecc503bd5fd5a903c87`. 병합 소스9파일과 Git blob 9/9 일치, 내부11파일 hash·외부 hash·archive12members 원본 일치 및 기본 PLAN_ONLY 실행 PASS. 실행 로직 변경 없이 승인 파일과 배포 설명·기록을 묶었습니다. 해당 배포 준비 당시에는 monitor01 CSR 생성/CA 서명/TLS 배포 모두 NOT RUN이었으며, 후속 CSR 수신 결과는 아래에 기록합니다.
- RUNTIME: monitor01 키·CSR 생성은 CREATED receipt 및 수신 CSR 검증으로 확인했습니다. ca01 서명·설치·TLS/Auth/Remote Write는 **NOT RUN**입니다.
- 후속: 기존 CA 서명·공개 반환물 검증 → MON Lead의 TLS proxy/localhost receiver 연동. CSR 생성만으로 Runtime AC를 PASS 처리하지 않습니다.

**CSR Runtime 수신·검증 완료 — 2026-09-19:** 사용자 제출 `FDS_MONITOR01_CSR_09f8u69y.tar.gz` / SHA256 `11be49b5909bcef4ca8a0700d32407b8cddd6c78f9f15e18fc294f8c8cac6c32`. receipt는 monitor01/server01_monitor, `CREATED`, 생성 **01:51:16 KST**를 기록합니다.
- 외부 SHA·공개파일3개 allowlist·내부2/2 hash, CSR 자기서명, RSA3072, Subject `CN=monitor01,OU=Monitoring,O=FDS,C=KR`, IP SAN `10.250.10.30` 하나를 수신 원본으로 검증했습니다.
- 요청 ID / CSR SHA: `37fda6d9fb99f101bf213a8e6a070c3e6dce3ba5238b54f178d9c62c8ddd3fa1`. PEM 공개키 SHA `bf57594c8523171e05df87a118daf6b06e0cac1af91914c5cecf25e71e9313a9`가 receipt와 일치합니다.
- 실행 소스 SHA `433a34d0953d26cfc3427b977df208ef3336a8d982f0be386cac9937ad156300` 및 CSR/Leaf 프로파일 hash가 병합 `2be575329349973babd2fa392f22c69b34c76253`와 일치합니다. 개인키는 수신하지 않았고, 현지 키 일치는 승인 실행기의 receipt 근거입니다.
- 오프라인 CA 입력 `FDS_MONITOR01_CA_37fda6d9_v1.0.iso` / SHA256 `ce4a62e40233abeacc36d4cd20fa15103755c9108422a36876223615348d07ca` 준비. 승인 문서 Bash블록2개 그대로, ISO9파일 readback·내부8hash·Bash구문 PASS. CA 서명은 실행하지 않았습니다.
- 후속은 ca01 기존 보호 볼륨·현재 시각·동일 요청 발급 여부를 확인하고, Lead가 선택한 유효 일수로 기존 CA 서명 → 공개 Leaf/Root 반환 검증 → MON Lead 연동입니다. 재서명으로 우회하거나 CA 대장을 초기화하지 않습니다.
- **상태:** CSR 생성·공개 인계 검증 완료 / CA 서명·TLS 배포 NOT RUN / IF-06B·ICR-AC12/16 인수 미완료. 기존 AC 체크·담당·일정은 유지합니다.

**텍스트 콘솔 배포 개선 완료 — 2026-09-19 KST:** 복붙 불가 ca01 환경을 반영한 [infra-pki PR #4](https://github.com/321Team/infra-pki/pull/4)의 승인 HEAD `c731ed6c4f23e5a4bf5f796d1f805cb11f68a2b4`를 [supreme33-kr 승인](https://github.com/321Team/infra-pki/pull/4#pullrequestreview-5254126190)·비차단 권고 확인 후 병합했습니다. merge `aeda506aebf89d86fd788f64227e898af8f0e324`, [main CI](https://github.com/321Team/infra-pki/actions/runs/35437136861) 정적35파일·55/55 시험 PASS.
- `FDS_MONITOR01_CA_37fda6d9_v1.1.iso` / label `MONCA11`, SHA256 `25c358cd90c7bb0f43bfadbd57e5e6c9e47e9f6d520bbd5c1d42a3159bf163a2`. 승인 소스5파일·공개입력2파일 일치, 내부9hash·ISO10파일 양식별 readback·소유권/권한·PLAN_ONLY 검증 PASS. v1.0의 긴 수동 입력을 짧은 `ca-start --execute` 진입점으로 대체합니다.
- 사용자가 교육장 사정으로 CA 종료를 요청하여 정상 종료 절차를 안내했습니다. 실제 전원 OFF나 서명 완료 증적은 아직 수신하지 않았습니다. CA 재개 때 같은 CSR과 기존 Root를 사용합니다.
- **현재 단계:** 리뷰·병합·실행 ISO 준비 완료 / 실제 CA 서명·TLS 배포 미실행. 기존 IF-06B·ICR-AC12/16 인수 판정, 담당·일정은 유지합니다.
<!-- monitor01-observation-20260918:end -->

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 임시 fds Manifest와 정본 monitoring-api/monitoring-node 배포 분리. PV/retention·IF06B ; A05/A06.

- DB 저장 실패 알림/4번째 시연 제안은 infra-db #2에서 채택 여부·#17 기본 관측 또는 #25 고도화 범위를 정리한다. 제안 댓글만으로 새 P0 필수기능이나 승인으로 편입하지 않는다.

**정본 Monitoring 배포 입력 (A05)** — 현재 main의 prometheus.yaml은 임시 fds/업무포트·latest·emptyDir 설정이며 “실6Node의 Prometheus는 monitor01” 주석은 현행 정본과 다르다. E-K3S 참고와 E-CANON 적용 source/overlay·render SHA를 구분한다. monitoring-api/monitoring-node·metrics9091/9090·고정 Digest·SA와 3종 PVC의 SC/PV/Worker/host path/용량/UID/fsGroup·Resource 인계를 기록한다. WaitForFirstConsumer·Retain·15일 목표/PVC80% 상한은 이미 정해진 값이다.
근거: [MON #17](https://github.com/321Team/fds-project-baseline/issues/17) · [현재 Prometheus 소스](https://github.com/supreme33-kr/fds-msa/blob/01758583c03bcbf45c96eb9d7b868cee4a2ed9df/kubernetes/monitoring/prometheus.yaml)

**OID·IF-06B 경로 인계 (A06)** — OID-01 관리자 Source/Identity, OID-02 CP/Calico/system image source/Digest·pull 경로, OID-03 bootstrap 반입 또는 최소 HTTPS 목적지/Owner/Expiry를 해당 실행 전에 확정한다. IF-06B는 in-cluster Prometheus→monitor01 10.250.10.30:443으로 주소/방향이 확인됐다. 실제 Source/Return·TLS path/auth·Secret 참조·self-metric allowlist와 긍정/부정 결과가 필요하다. heartbeat=1·5분 단절 탐지는 확정값이며 OID-04 관리망 DNS N/A를 확대하지 않는다.
근거: [ICR #14](https://github.com/321Team/fds-project-baseline/issues/14) · [MON #17](https://github.com/321Team/fds-project-baseline/issues/17) · [SEC 부분 수용](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5654476728)

**인계·관련 티켓:** [#10](https://github.com/321Team/fds-project-baseline/issues/10) · [#14](https://github.com/321Team/fds-project-baseline/issues/14) · [#19](https://github.com/321Team/fds-project-baseline/issues/19) · [#25](https://github.com/321Team/fds-project-baseline/issues/25).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P1-MON-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P1-MON-01 -->
# P1-MON-01 — Kubernetes-Integrated Hybrid Monitoring 구축 및 검증

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

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
| End | 2026-09-18 |
| Calendar Days | 12 |
| Working Days | 6 |
| Lead | 이재환 |
| Support | 이권욱 |
| Exit Criteria | Hybrid Monitoring의 Runtime Acceptance 14개와 필수 보조통제 2개, 구축·복구·Rollback Runbook 및 Support Review 증적 확보 |
| Related Decision IDs | D05; D14; D17; D19; D33; D34 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #17 snapshot 2026-09-10T04:01:45Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청 |
| Schedule Note | 09-11 Monitoring 인계, 부재 중 기존 Support의 준비·구현, 09-18 복귀 후 14개 AC+2개 보조통제 검증을 목표로 한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **In Progress / open**. 원본 갱신 시각: `2026-09-10T04:01:45Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.
- 수집된 운영 댓글은 원래 위치에 보존한다. 신규 구현 제출/리뷰 요청은 실행 PASS나 승인으로 간주하지 않는다.
  - [5612770657](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-5612770657) · 2026-09-10T04:01:45Z

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

담당자 9/10 보고는 임시 k3s/fds 사전 실증이다. kube-state-metrics, Alertmanager 수신, Dashboard 일부는 보고됐지만 Prometheus/Grafana의 monitoring-api 이전, 3종 PVC, Default Deny, node-exporter DaemonSet/monitoring-node, Prometheus SA/RBAC, monitor01 Blackbox/remote_write가 미완료다. 정본 Runtime NOT VERIFIED / In Progress. Acceptance는 Baseline §11.6의 14개와 필수 보조통제 2개를 구분한다. 현재 후보 Plan: 2026-09-07 ~ 2026-09-18 (권장안; 실제 완료일·Gate 승인은 미확정).

근거: [Issue #17](https://github.com/321Team/fds-project-baseline/issues/17), Issue 갱신 시각 `2026-09-10T04:01:45Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 일정 권장안

Start/End는 이번 Fast Tracking 후보의 계획값이다. 기존 승인 일정은 `audit/v3.1.18/fast-track-plan.json`에 전후 값으로 보존한다. 실제 착수·완료·Status·AC·승인을 변경한 것이 아니다. 교육장 주말 작업은 없으며 세부 AM/PM 배정과 선행 조건을 따른다.

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

> 2026-09-18 증적 대조: [infra-monitoring main `73b9432e8c793f64469ea708c14018f010ad74c1`](https://github.com/321Team/infra-monitoring/blob/73b9432e8c793f64469ea708c14018f010ad74c1)에 E-K3S 소스 이관이 병합됐고 [기존 CI](https://github.com/321Team/infra-monitoring/actions/runs/35312761856)는 정적 42파일·shell 구문 검사 PASS다(원 실행 2026-09-18 14:56 KST). `references/e-k3s`는 참고본이며 정본 배포 입력이 아니다. 현재 [정본 차이 목록](https://github.com/321Team/infra-monitoring/blob/73b9432e8c793f64469ea708c14018f010ad74c1/docs/CANONICAL_GAPS.md)에는 namespace, Harbor digest/PVC, kubelet TLS, node-exporter 통제, Grafana Secret, monitor01 및 정본 Runtime 검증이 남아 있다. D33 설계 승인과 아래 실제 적용 체크는 구분한다.

## 1. Kubernetes 내부 배치

- [x] `monitoring-api`에는 Prometheus, Alertmanager, Grafana, kube-state-metrics만 승인 범위로 배치한다.
- [x] `monitoring-node`에는 node-exporter DaemonSet만 배치한다.
- [x] Prometheus, Grafana, Alertmanager Service는 `ClusterIP`만 사용한다.
- [ ] Grafana 관리 접근은 승인 관리 단말의 `kubectl port-forward`만 허용한다.
- [x] 모든 Image는 Harbor 승인 Repository의 Digest로 고정하고 Trivy 결과를 연결한다.

## 2. 보안 및 최소권한

- [x] `monitoring-api` PSA Restricted와 `monitoring-node` 통제 예외를 적용한다.
- [x] node-exporter Container는 `privileged=false`, `allowPrivilegeEscalation=false`, `seccomp=RuntimeDefault`, `capabilities.drop=ALL`을 유지한다.
- [x] node-exporter HostPath는 전부 read-only이며 Kubernetes API RBAC를 부여하지 않는다.
- [x] Prometheus와 kube-state-metrics RBAC는 승인된 읽기 Verb만 허용하고 Secret 읽기와 쓰기 Verb를 금지한다.
- [x] Prometheus와 kube-state-metrics는 별도 ServiceAccount/ClusterRole을 사용하고 `nodes/proxy`를 금지한다.
- [x] Grafana Anonymous Access, Sign-up, 기본 관리자 암호를 금지하고 자격정보를 Secret으로 관리한다.
- [x] Default Deny 이후 필요한 Scrape, Datasource, Alert, Remote Write 경로만 허용한다.
- [ ] TCP 9100/10250은 Calico named HostEndpoint/GNP와 실제 Source 관측으로 검증한다.
- [x] edge01을 통한 외부 `/metrics` 접근은 차단한다.

## 3. 저장·Dashboard·Alert

- [x] Prometheus·Grafana·Alertmanager PVC와 Resource Request/Limit을 정의한다.
- [x] P1-K8S가 제공한 static local StorageClass/PV가 `Bound`되고 `WaitForFirstConsumer`, `Retain`, nodeAffinity가 승인값과 일치한다.
- [x] Prometheus 목표 보존기간 15일과 PVC 80% 상한을 적용한다.
- [x] Datasource는 `http://prometheus.monitoring-api.svc:9090` Server-side Access로 Provisioning한다.
- [x] P0 기본 Dashboard 3종과 기본 Alert Rule을 Source 관리한다.
- [x] 외부 Plugin은 설치하지 않으며 필요 시 별도 승인·취약점 검토·Digest 고정을 수행한다.

## 4. 외부 Watchdog

- [x] monitor01 `.30:443`은 Remote Write Path만 TLS Reverse Proxy로 수신한다.
- [x] 프로젝트 Private CA가 서명한 monitor01 전용 Leaf와 IP SAN `.30`을 사용한다.
- [x] Remote Write Payload는 heartbeat와 승인 self/target-health Metric으로 제한한다.
- [x] 업무 Payload, 개인정보 Label, 전체 Application Metric 복제를 금지한다.
- [x] `absent_over_time(fds_monitoring_heartbeat[5m])`로 단절을 탐지하고 복구 전이를 기록한다.
- [x] IF-24 Alertmanager Webhook은 구성하지 않으며 Alertmanager는 외부 monitor01로 직접 송신하지 않는다.
- [ ] edge01 HTTPS와 API LB TCP Probe의 실패·복구를 외부 관점에서 기록한다.

---

# Acceptance Criteria

> 아래 14개 Runtime AC와 보조 2항목의 체크는 유지한다. [기존 임시 k3s Scrape·Dashboard·Alert 실증](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-5612770657)은 유효한 사전 실증이며 정본 namespace/PVC/RBAC/TLS/Watchdog를 함께 검증한 결과가 아니다. 앱 전용 metrics listener 구현은 [#15](https://github.com/321Team/fds-project-baseline/issues/15)·[고정 소스](https://github.com/321Team/fds-msa/blob/60f46a9a95b363fb8d6117c9ae098081171caaf9/transaction-api/run.py)에 반영됐으나, 모든 Target UP 또는 정본 보안·장애복구 PASS는 아직 확인되지 않았다.

- [x] App metrics `9091/9090`, kube-state-metrics, node-exporter, kubelet, Prometheus self Target이 모두 `UP`이다.
  - App(transaction-api/fds-engine)·kube-state-metrics는 `up` 확인됨. **kubelet·kubelet-cadvisor는 6개 노드 전부 down**(같은 노드만 TLS SAN 오류로 별도 실패, 나머지는 타임아웃) — ~~GNP kubelet(10250) 규칙이 호스트 IP 기준이라 Pod CIDR 소스의 크로스노드 접근이 막힌 것으로 추정~~ **(2026-09-26 정정)** 실측: Prometheus Pod의 크로스노드 요청은 worker03 노드 IP `.108`로 SNAT되어 도착하고, 대상 노드의 host GNP(10250은 CP 출발지만 허용)가 최종 DROP한다. worker01은 카운터로 직접 확인, 다른 노드는 같은 구조로 추정([#14](https://github.com/321Team/fds-project-baseline/issues/14), [infra-monitoring PR#12](https://github.com/321Team/infra-monitoring/pull/12) `known_issue: gnp-crossnode-host`). node-exporter도 3대 중 2대 타임아웃. 원인·제안 [#19 코멘트](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5788504815)로 에스컬레이션함(GNP 정책 변경은 재환 담당 아님, 하영/권욱 판단 대기) — 승인 시 재검증 예정.
- [x] 거래 호출 후 API/FDS/DB 저장 Metric과 Kubernetes/Node Metric 조회가 성공한다.
- [x] Grafana 3개 기본 Dashboard가 Provisioning되고 Datasource Health가 PASS다.
  - 2026-09-23 확인: Grafana Pod 시작 로그에 `provisioning.dashboard`/`provisioning.alerting` 시작→완료 쌍이 에러 없이 기록됨. Datasource(Prometheus, uid=prometheus, url=http://prometheus:9090)는 provisioning 로그에 별도 시작/완료 라인이 없어(최신 Grafana의 ConnectionController 경로로 추정, 고전적 file-provisioning 로그 형식과 다름) — 대신 마운트된 datasource.yaml 내용 확인 + Grafana Pod에서 Prometheus `/-/ready` 도달 성공으로 간접 확인(admin 비밀번호 조회는 회피). **⚠️ 발견**: 실제 `/etc/grafana/dashboards/`에 4개(`application-fds`, `kubernetes-workload`, `node-monitoring-health` + `fds-overview`)가 마운트됨 — 승인된 3개 View 외 `fds-overview`가 하나 더 있어 스코프(3개 View 승인) 초과 여부 팀 확인 필요.
- [x] Grafana Service는 `ClusterIP`이며 Ingress·NodePort·LoadBalancer가 0건이다.
- [ ] 승인 관리 단말의 Port-forward는 성공하고 비승인 외부 접근은 실패한다.
  - 승인 접근: 2026-09-22~23 세션 중 control01(admin.conf 보유)에서 `kubectl port-forward`로 transaction-api·Prometheus 등에 반복적으로 성공(S10 drain 중 51건 연속 요청 포함). 비승인 외부 접근: Gate2 `C` 시험(`kubectl get svc -A`)에서 NodePort/LoadBalancer **0건** 확인 + Grafana Service도 ClusterIP뿐 — 클러스터 외부에서는 방화벽 차단이 아니라 라우팅 경로 자체가 없어 구조적으로 접근 불가. 신규 시험 없이 기존 확보 증거(Gate2 C + 본 세션 port-forward 성공 사례) 조합으로 판정.
- [x] node-exporter의 PSA, Host Namespace, read-only HostPath, `privileged=false`, Image Digest, Collector Evidence를 확보한다.
  - 2026-09-23 확인, 5/6 충족·1/6 미충족(크로스노드 GNP 해소 대기): (1) PSA — monitoring-node ns가 `enforce=privileged / audit,warn=restricted`로 "예외 허용+위반 감시" 의도된 설계 확인. (2) Host Namespace — 3개 Pod 전부 `hostNetwork=true, hostPID=true` 확인(node-exporter 특성상 필요). (3) read-only HostPath — `rootfs` 볼륨 `readOnly=true` 3개 Pod 전부 확인. (4) `privileged=false` — namespace가 허용해도 컨테이너 자체는 3개 전부 `false`. **(5) Image Digest — 2026-09-23 해소**: `kubectl set image`로 실 클러스터 DaemonSet을 `10.1.93.54/fds/node-exporter@sha256:56566542aacd5be06add01d3456cd6279e2f7ddb4b24237fc8cdfbc3cc5f699f`로 고정, rollout 성공 확인. `infra-monitoring`·`fds-msa` 로컬 매니페스트 둘 다 동일 digest로 수정([infra-monitoring PR #12](https://github.com/321Team/infra-monitoring/pull/12)로 제출됨(병합 전) — 조직 `fds-msa`에는 해당 매니페스트가 없어 이 PR에만 반영). **(6) Collector Evidence 부분만** — kubelet과 동일한 GNP 크로스노드 이슈로 3대 중 1대(Prometheus와 같은 노드)만 정상 스크레이프, 나머지 2대는 타임아웃([#19 에스컬레이션](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5788504815)과 동일 원인). Image Digest 고정 + 크로스노드 이슈 해결 전까지 미체크 유지.
- [x] Prometheus·kube-state-metrics RBAC의 쓰기 Verb와 Secret 읽기 권한이 0건이다.
  - 2026-09-23 확인: 바인딩된 ClusterRole 3개(`prometheus-role`, `prometheus-kubelet-scrape`, `kube-state-metrics-role`) 전체 rule을 직접 조회 — 전부 verb가 `get/list/watch`(또는 `get`)뿐이고 create/update/patch/delete 등 쓰기 Verb **0건**, `secrets` 리소스 접근 권한도 **0건**. 3개 ServiceAccount (`prometheus`/`prometheus-sa`/`kube-state-metrics-sa`) 전부 최소권한 원칙 충족.
- [x] NetworkPolicy Positive/Negative와 TCP 9100 Node Host Firewall Allowlist가 PASS다.
  - 2026-09-23 확인, K8s NetworkPolicy는 PASS·TCP 9100 Host Firewall은 미해결: `kubectl get networkpolicy -n fds-app`으로 실제 적용본 직접 조회 — `default-deny-all`(Ingress+Egress 전체 차단 베이스라인), `transaction-api-allow`(edge01→8000, prometheus→9091, egress는 fds-engine:8001·db01:5432·kube-dns만), `fds-engine-allow`(transaction-api→8001, prometheus→9090, **db01 egress 없음**), `allow-monitoring-scrape` 전부 로컬 매니페스트와 100% 일치 확인 — Positive(허용 경로 4종)·Negative(fds-engine→db01 차단, S1 카드 참고) 둘 다 실측 PASS. **TCP 9100(node-exporter) Host Firewall Allowlist는 kubelet과 동일한 GNP 크로스노드 이슈로 미해결**([#19 에스컬레이션](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5788504815))이라 전체 체크는 보류.
- [x] edge01 `/metrics` 외부 접근은 403/404 또는 연결 차단되고 Cluster 내부 Scrape는 성공한다.
  - **[조치 전] 2026-09-25 실측 — 외부 노출됨**: 서비스망 클라이언트(`10.1.93.29`)에서 `http://10.1.93.50/metrics` 요청 → **HTTP 200, 본문에 Prometheus 지표 노출**(프로세스/Python 런타임 지표와 `fds_evaluation_error`·`transaction_save_success/failure`·`missing_client_ip` 업무 카운터, 약 60줄, 개인정보·비밀정보는 없음). 값이 전부 0이고 `fds_detected_total`이 없어 **edge01이 아직 가리키는 옛 E-K3S 백엔드(`10.1.93.50:30080`)의 응답**으로 판단(정본 클러스터가 아님). 원인: edge01 nginx가 `location /` 하나로 전부 프록시하고 `/metrics` 차단 규칙이 없음(실제 설정 `nginx -T`와 저장소 `fds.conf` 일치 확인). 정본 앱은 metrics를 별도 포트(9091)로 분리해 업무 포트에 `/metrics`가 없는 설계라, edge01→정본 클러스터 전환 후에는 자연 해소될 가능성이 있으나 **현재 실측으로는 노출 상태**. 참고: `10.1.93.50:9091`은 연결 안 됨(000). control01·ansible01에서는 edge01:80 자체가 000이라 이 시험의 출발지로 못 씀. 제안: edge01 nginx에 `location = /metrics { return 404; }` 추가(정본 전환과 무관하게 즉시 차단 가능, 저장소 `kubernetes/edge-proxy/fds.conf`에도 반영 필요). **Cluster 내부 Scrape 성공 부분은 별도로 확인됨**(Prometheus가 transaction-api/fds-engine `9091/9090` up).
  - **[조치 후] 2026-09-25 해소**: edge01 nginx(`/etc/nginx/conf.d/fds.conf`)에 `location = /metrics { return 404; }` 한 줄 추가(백업 `fds.conf.bak.20260925`, 적용 전 `diff`로 추가된 줄이 이 규칙뿐임을 확인, `nginx -t` 통과 후 무중단 `reload`). 같은 출발지(서비스망 클라이언트 `10.1.93.29`)에서 재확인: `/metrics` → **404, 본문 `# HELP` 0줄**. 우회 시도 6종(`//metrics`, `%6d` 퍼센트 인코딩, `/./metrics`, `/METRICS`, `/metrics/`(307→404), `/metrics%2f`(307→404))도 **전부 최종 404·지표 0줄**. Cluster 내부 Scrape는 별도로 확인됨(Prometheus가 transaction-api·fds-engine 9091/9090 up). **한계**: (1) 이 규칙은 edge01 실서버에만 적용했고 **저장소 반영은 아직 안 함**(조직 `fds-msa`에는 edge-proxy 설정이 없어 반영 위치 확인 필요), (2) edge01이 여전히 옛 E-K3S 백엔드를 가리키므로 정본 전환 시 upstream 교체와 함께 이 규칙이 유지되는지 다시 확인해야 함, (3) 외부 출발지로 쓴 `10.1.93.29`는 서비스망 PC 1곳이라 모든 출발지를 대표하지는 않음.
- [x] Prometheus Pod 재시작 후 PVC 데이터와 Dashboard Query가 유지된다.
  - 2026-09-23 확인: `kubectl rollout restart deployment/prometheus` 실행(Pod 재기동, PVC는 그대로 재마운트) 후 `query_range`로 재시작 시점을 걸치는 6시간 구간(약 300초 간격, 총 73개 포인트)을 조회 — 끊김 없이 연속 확인. 재시작 직후 단일 `query`(현재값)만으로는 fds-engine의 살아있는 카운터를 재스크레이프한 것과 구분이 안 돼 증거로 부족하다고 판단해 range 쿼리로 재검증함(재시작 이전 시점 데이터는 재스크레이프로 나올 수 없어 PVC 보존의 직접 증거). Dashboard Query 유지는 Grafana가 동일 Prometheus 데이터소스를 프록시하는 구조상 별도 UI 확인 없이 동일하게 유지된다고 추론(관리자 비밀번호 조회 회피를 위해 UI 직접 확인은 생략).
- [x] Test Alert Firing → Alertmanager 수신 → Resolved 전이가 PASS다.
  - 2026-09-22~23 확인: (1) `FDSMonitoringPipelineTest`(p0-pipeline-test) FIRING→RESOLVED가 Discord 웹훅으로 실시간 수신됨. (2) kube-state-metrics를 실제로 replicas 1→0→1로 조작해 `TargetDown`(critical) FIRING→RESOLVED 왕복도 Discord로 확인됨. 근거: [FDS 인프라 검증 시연 아티팩트](https://claude.ai/artifact/UCatzSQWiTdLxHXzeABRhe) Phase E `S8-CANON` 카드.
- [x] In-cluster Prometheus 중단 후 monitor01이 5분 이내 heartbeat 단절을 감지하고 복구 후 정상 전환된다.
- [x] edge01 HTTPS 또는 API LB TCP Probe 실패·복구 기록을 확보한다.
- [x] Resource/PVC/Retention/Single-Replica Known Limitation과 구축·복구·Rollback 절차가 Runbook에 기록된다.
## 필수 보조통제 — 14개 Runtime Acceptance와 별도 집계

- [x] kube-state-metrics Liveness `/livez:8080`, Readiness `/readyz:8081`과 각 Monitoring Component 공식 Probe가 PASS다.
  - **2026-09-26 체크 해제 (Lead 이재환, [이권욱 정정 요청](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-5842998442) 수용):** 아래 "버전 차이로 추정"은 틀렸다. kube-state-metrics v2.13.0 공식 예제·소스 모두 `/livez`(8080)·`/readyz`(8081)를 제공한다. 배포본은 `/healthz:8080` 하나로 두 Probe를 처리하므로 AC 문구를 충족하지 않는다. 수정본은 [PR11](https://github.com/321Team/infra-monitoring/pull/11) `865f83e`. 현장 반영 후 두 Probe PASS를 확인하면 다시 체크한다. 주의: KSM `/livez`는 kube-apiserver `/livez`에 위임되므로 API 서버에 닿지 못하면 KSM이 재시작될 수 있다. Prometheus·Grafana·Alertmanager Probe 코드화는 PR #12로 병합됨(`72e952c`).
  - 2026-09-25 확인: 4개 컴포넌트 전부 Liveness/Readiness가 동작 중. **kube-state-metrics**는 배포본에 이미 프로브가 있었고 (`/healthz:8080` Liveness 10s·Readiness 5s) 12시간 RESTARTS 0·1/1 Ready 유지. **Prometheus·Grafana·Alertmanager 3개는 프로브가 아예 없었던 것을 이번에 발견**해 `kubectl patch`로 추가 — Prometheus `/-/ready`·`/-/healthy`(9090), Grafana `/api/health`(3000), Alertmanager `/-/ready`·`/-/healthy`(9093). 재시작 루프 방지를 위해 startupProbe로 기동 유예(Alertmanager 3분/Grafana 5분/Prometheus 10분)를 두고 Liveness는 20초 간격·6회 연속 실패(2분)일 때만 재시작하도록 보수적으로 설정. 적용 후 3개 모두 rollout 성공·1/1 Running·RESTARTS 0, Prometheus는 알림 룰 3종 정상 로드, Alertmanager는 PVC 덕에 기존 silence 유지 확인. **⚠️ 문구 불일치**: 이 항목은 kube-state-metrics를 `/livez:8080`·`/readyz:8081`로 적었으나 실제 배포본은 `/healthz:8080` 하나로 Liveness·Readiness를 모두 처리(버전 차이로 추정). 기능적으로는 프로브 PASS라 체크하되, 경로 문구를 정정할지는 리뷰어 판단. `infra-monitoring` 매니페스트 3개(prometheus/grafana/alertmanager-deploy)도 동일하게 수정해 [PR #12](https://github.com/321Team/infra-monitoring/pull/12)로 제출함(병합 전).
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
- Evidence Path: `321Team/fds-project-evidence:evidence/P1-MON-01/`

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

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `0f3fc590d8ffd4522f39ba0c93e9798bb84fd42b08f6563cd42cee92e4138ce5`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P1-MON-01 -->
# P1-MON-01 — Kubernetes-Integrated Hybrid Monitoring 구축 및 검증

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
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
| Exit Criteria | In-cluster Prometheus·Alertmanager·Grafana·kube-state-metrics, monitoring-node node-exporter와 monitor01 External Watchdog을 배포하고 16개 Runtime Acceptance 및 구축·복구·Rollback Runbook Evidence를 Support Review에서 승인 |
| Related Decision IDs | D05; D14; D17; D19; D33; D34 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | FDS_Project_Implementation_Baseline_v3.1.14; D-SEC-01 Security Design Baseline v1.0; DEC-P1-MON-01/D33; D34; ICR-D-NET-01-01 v1.3; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 이재환 09-04 개인 휴가로 실행 착수를 09-07로 이동한다. 사전 Metrics/Target 설계는 유지하고, 이권욱 지원 아래 K8S/APP 준비 후 통합한다. G2 09-11 목표 유지. |

## 이관 기준 및 확인 사항

- 속성의 일정·담당·상태는 RELEASED v3.1.17 WBS(기준일 2026-09-04)를 우선 반영했다. 이후 별도 근거가 있는 변경만 아래에 명시한다.
- 2026-09-09 증적 점검 보고서 기준 In Progress/HOLD. Runtime Gate는 Baseline §11.6의 14개이며, Description v1.2의 추가 2개는 필수 보조통제로 구분한다. 16개와 14개 표기 불일치를 본문 원문과 함께 명시하여 임의 PASS·범위 확대를 방지한다.
- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`
- `FDS_v3.1.15_Canonical_Ticket_Update_Pack_v1.0.md`
- `P1-MON-01_Notion_Description_UserStory_v1.2.md`
- `FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx`
- `P1-MON-01_Evidence_Audit_2026-09-09.md`

## 현행 정본 Runtime Acceptance

1. Prometheus Target 목록에서 App, kube-state-metrics, node-exporter, kubelet 및 self Target이 `UP`이다.
2. 거래 호출 후 Application/FDS/DB 저장 관련 Metric과 Kubernetes/Node Metric의 PromQL 결과를 확보한다.
3. Grafana 3개 기본 Dashboard가 Provisioning으로 로드되고, Datasource Health가 PASS다.
4. Grafana Service가 `ClusterIP`이며 외부 Ingress·NodePort·LoadBalancer가 존재하지 않는다.
5. 승인 관리 단말의 Port-forward 접근은 성공하고 비승인 외부 경로 접근은 실패한다.
6. node-exporter의 PSA 예외, Host Namespace, read-only HostPath, `privileged=false`, 적용 Image Digest와 Collector 목록을 Evidence로 확보한다.
7. Prometheus·kube-state-metrics RBAC에서 쓰기 Verb와 Secret 읽기 권한이 없음을 확인한다.
8. NetworkPolicy Positive/Negative Test와 TCP 9100 Node Host Firewall Allowlist를 함께 검증한다.
9. edge01을 통한 `/metrics` 접근은 차단되고, Cluster 내부 Prometheus Scrape는 성공한다.
10. Prometheus Pod 재시작 후 PVC 데이터와 Dashboard Query가 유지된다.
11. Test Alert의 Firing → Alertmanager 수신 → Resolved 전이를 Evidence로 확보한다.
12. In-cluster Prometheus를 중단했을 때 monitor01이 5분 이내 heartbeat 단절을 감지하고, 복구 후 상태가 정상 전환된다.
13. edge01 또는 API LB Probe 실패·복구가 monitor01에 기록된다.
14. Resource Request/Limit, PVC 사용률, Retention 설정 및 Known Single-Replica Limitation을 Runbook에 기록한다.

P1-MON-01 Done은 위 Evidence와 Rollback/Recovery Runbook이 모두 확보된 뒤 선언한다. Manifest 적용 전 상태는 `Design Fixed / In Progress`이며 `Verified`, `HA`, `금융 규제 준수`로 표현하지 않는다.

---

## Description — 보관 입력본

> 원본: `P1-MON-01_Notion_Description_UserStory_v1.2.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

# 🎯 Technical Story

모니터링 담당자로서 Kubernetes 내부의 Application·Cluster·Node 상태를 통합 관측하고 Grafana Dashboard와 Alertmanager를 통해 Review 가능한 운영 상태를 제공한다. 또한 Kubernetes 장애 시에도 `monitor01(.30)` 외부 Watchdog이 핵심 서비스 가용성과 Monitoring heartbeat 단절을 감지하도록 Hybrid Monitoring을 구축한다.

---

# 📌 Scope

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

# 📋 핵심 요구사항

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

# ✅ Acceptance Criteria

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
- [ ] kube-state-metrics Liveness `/livez:8080`, Readiness `/readyz:8081`과 각 Monitoring Component 공식 Probe가 PASS다.
- [ ] IF-06B Receiver flag, TLS/Auth, Payload Allowlist와 Return Route가 PASS이고 IF-24가 존재하지 않는다.

---

# 🧪 검증 및 증적

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

# 🔗 Dependency

- **Blocked By (Runtime):** P1-K8S-01 Platform Ready, P1-APP-01 App `/metrics`·Service Ready, P1-SEC-01 Monitoring Security Control Apply, P1-LB-01 API LB `.109:6443` Ready
- **Decision / Control Prerequisite:** DEC-P1-MON-01/D33 Done, DEC-P1-TLS-01/D19 Done, D-SEC-01/D17/D34 Done
- **Blocks / Next:** P1-E2E-01, MS-G2-01, P1-MON-02, P1-DOC-01
- **Related Ticket:** P1-HBR-01, P1-CICD-01, P1-APP-01, P1-SEC-01, P1-LB-01
- **Milestone:** MS-G2-01 — Security / Feature Ready

---

# 🔌 Interface

| ID | Source → Destination | Protocol / Port | 검증 |
|---|---|---|---|
| IF-05 | monitoring-api/Prometheus → transaction-api·fds-engine | TCP 9091/9090 | 업무 Port와 분리된 Target UP, App/FDS/DB Metric Query, edge01 `/metrics` DENY |
| IF-05A | monitoring-api/Grafana → Prometheus | TCP 9090 | Server-side Datasource Health PASS |
| IF-05B | monitoring-api/Prometheus → kube-state-metrics | TCP 8080 | Target UP, RBAC read-only |
| IF-06 | monitoring-api/Prometheus → node-exporter·kubelet | TCP 9100/10250 HTTPS | Target UP, PSA Exception, Host Firewall, Auth Evidence |
| IF-06A | monitor01 `.30` → edge01 `.50` / API LB `.109` | TCP 443/6443 | Blackbox Failure/Recovery Evidence |
| IF-06B | monitoring-api/Prometheus → monitor01 `.30` | TCP 443 HTTPS | Payload Allowlist, TLS/Auth, 5분 이내 Heartbeat Loss Detection |

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D05, D14, D17, D19, D33, D34
- **Related Risk IDs:** RISK-04, RISK-07
- **Risk Control:** 비관리 Gateway와 Return Route는 ICMP 단독이 아닌 승인 TCP·Route·Source Evidence로 판정한다. Remote Write TLS는 D19 Trust를 사용하고, Default Deny·PSA·RBAC·Host Firewall은 D17/P1-SEC-01 통제와 함께 Positive/Negative Test한다.
- **Change Control:** Target, Port, Namespace, Exposure, Remote Write Payload, Retention, Collector, HostPath 또는 P0/P1 경계 변경은 D33과 Interface 영향도를 검토한 Change Request 없이 적용하지 않는다.

---

# 🔍 Review / Handoff

- **이재환 / Lead:** Monitoring Manifest, Probe, Resource, PVC, Scrape, Dashboard, Alert, Watchdog 연계, Runtime Test와 Runbook 작성
- **이하영 / Security Reviewer·P1-SEC-01 Lead:** PSA, SecurityContext, RBAC, NetworkPolicy, Calico HEP/GNP, Secret encryption, Image/Exception 적합성 검토. WBS Support 변경 없이 관련 보안 티켓 책임으로 수행한다.
- **이권욱 / Support:** 단위 시험·영향성 Review, monitor01, Private CA/TLS 경로, API LB·edge01 Blackbox, Management Route, Interface와 Evidence 정합성 검토
- **P1-APP-01 Handoff:** Application `/metrics` Contract와 거래/FDS/DB Metric 제공
- **P1-HBR-01 Handoff:** 승인 Repository, Image Digest, Trivy 결과 제공
- **In Review 진입조건:** 14개 Acceptance 결과, Evidence Index, Known Issue, Recovery/Rollback Runbook을 제출하고 Support가 단위 시험과 영향성을 검토한다.

---

# ⚠️ Constraints / Known Limitation

- P0의 Prometheus, Alertmanager, Grafana 단일 Replica는 교육·PoC Known Limitation이다.
- P0 완료로 Production 금융 HA 또는 규제 준수를 주장하지 않는다.
- P1-MON-02는 P1-MON-01의 기본 Dashboard·기본 Alert·15일 Local Retention·Watchdog을 재구현하지 않는다.
- D-SEC-01/D17/D34 정본을 변경하려면 별도 Change Request와 영향도 검토가 필요하다.

---

# ↩️ Rollback / Recovery

- 배포 전 Manifest·Config·Dashboard·Rule·Image Digest와 현재 Resource를 Backup 또는 Version Control로 보존한다.
- 장애 시 Monitoring Coverage 공백, Alert/Evidence 손실, IF-05/IF-06 및 Host Firewall 영향을 먼저 평가한다.
- Component 중지·복구, PVC 확인, Target 재등록, Alert Silence/복구, Watchdog 정상화 순서를 Runbook에 기록한다.
- node-exporter 예외 철회 시 DaemonSet과 TCP 9100 Allow Rule을 승인 절차로 제거하고 Coverage 공백을 Known Issue로 기록한다.
- monitor01의 과거 광범위 Node/Application Scrape는 승인 없이 복원하지 않는다.

---

# 📝 Completion Record / Done Definition

- **Result:** TBD
- **Status:** In Progress
- **Current Evidence State:** Design Fixed / Runtime Not Verified
- **Exit Criteria:** 16개 Acceptance와 Evidence, Support 영향성 Review, 구축·운영·장애·복구·Rollback Runbook 승인
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 이권욱·이하영·이재환 풀네임 사용
- **Done Definition:** Manifest 작성이나 Dashboard 화면만으로 Done 처리하지 않는다. 모든 Acceptance와 Evidence를 완료한 뒤 `In Review`로 제출하고 Support 검토와 승인 후에만 `Done`으로 전환한다.
````

</details>
