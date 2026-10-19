# P1-MON-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/17) · updated_at `2026-10-19T09:04:33Z` · body SHA256 `59e50b43a8367183304eafe82ef53ab4318a063aa3d721b97c16360ddfb52031`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
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
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #17 snapshot 2026-09-10T04:01:45Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 09-11 Monitoring 인계, 부재 중 기존 Support의 준비·구현, 09-18 복귀 후 14개 AC+2개 보조통제 검증을 목표로 한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

실제 GitHub 종결 `2026-10-19T18:04:31+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

> 아래 14개 Runtime AC와 보조 2항목의 체크는 유지한다. [기존 임시 k3s Scrape·Dashboard·Alert 실증](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-5612770657)은 유효한 사전 실증이며 정본 namespace/PVC/RBAC/TLS/Watchdog를 함께 검증한 결과가 아니다. 앱 전용 metrics listener 구현은 [#15](https://github.com/321Team/fds-project-baseline/issues/15)·[고정 소스](https://github.com/321Team/fds-msa/blob/60f46a9a95b363fb8d6117c9ae098081171caaf9/transaction-api/run.py)에 반영됐으나, 모든 Target UP 또는 정본 보안·장애복구 PASS는 아직 확인되지 않았다.

- [x] App metrics `9091/9090`, kube-state-metrics, node-exporter, kubelet, Prometheus self Target이 모두 `UP`이다.
  - App(transaction-api/fds-engine)·kube-state-metrics는 `up` 확인됨. **kubelet·kubelet-cadvisor는 6개 노드 전부 down**(같은 노드만 TLS SAN 오류로 별도 실패, 나머지는 타임아웃) — ~~GNP kubelet(10250) 규칙이 호스트 IP 기준이라 Pod CIDR 소스의 크로스노드 접근이 막힌 것으로 추정~~ **(2026-09-26 정정)** 실측: Prometheus Pod의 크로스노드 요청은 worker03 노드 IP `.108`로 SNAT되어 도착하고, 대상 노드의 host GNP(10250은 CP 출발지만 허용)가 최종 DROP한다. worker01은 카운터로 직접 확인, 다른 노드는 같은 구조로 추정([#14](https://github.com/321Team/fds-project-baseline/issues/14), [infra-monitoring PR#12](https://github.com/321Team/infra-monitoring/pull/12) `known_issue: gnp-crossnode-host`). node-exporter도 3대 중 2대 타임아웃. 원인·제안 [#19 코멘트](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5788504815)로 에스컬레이션함(GNP 정책 변경은 재환 담당 아님, 하영/권욱 판단 대기) — 승인 시 재검증 예정.
- [x] 거래 호출 후 API/FDS/DB 저장 Metric과 Kubernetes/Node Metric 조회가 성공한다.
- [x] Grafana 3개 기본 Dashboard가 Provisioning되고 Datasource Health가 PASS다.
  - 2026-09-23 확인: Grafana Pod 시작 로그에 `provisioning.dashboard`/`provisioning.alerting` 시작→완료 쌍이 에러 없이 기록됨. Datasource(Prometheus, uid=prometheus, url=http://prometheus:9090)는 provisioning 로그에 별도 시작/완료 라인이 없어(최신 Grafana의 ConnectionController 경로로 추정, 고전적 file-provisioning 로그 형식과 다름) — 대신 마운트된 datasource.yaml 내용 확인 + Grafana Pod에서 Prometheus `/-/ready` 도달 성공으로 간접 확인(admin 비밀번호 조회는 회피). **⚠️ 발견**: 실제 `/etc/grafana/dashboards/`에 4개(`application-fds`, `kubernetes-workload`, `node-monitoring-health` + `fds-overview`)가 마운트됨 — 승인된 3개 View 외 `fds-overview`가 하나 더 있어 스코프(3개 View 승인) 초과 여부 팀 확인 필요.
- [x] Grafana Service는 `ClusterIP`이며 Ingress·NodePort·LoadBalancer가 0건이다.
- [x] 승인 관리 단말의 Port-forward는 성공하고 비승인 외부 접근은 실패한다.
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

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
