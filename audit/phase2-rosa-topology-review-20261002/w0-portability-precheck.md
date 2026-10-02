# W0 Portability Precheck Plan — 2026-10-02 KST

## 1. 목적과 경계

- Record ID: **P2-PORTABILITY-W0-01**
- 대상: Phase 1 workload/security/delivery contract → Shared OCP → ROSA
- 목적: 유료 ROSA 생성 전에 PG-01/02/03/08의 제거 가능한 결함을 찾고 topology 결정 입력을 확보한다.
- 환경: **SHARED_OCP_LAB / namespace-local only**
- 결과 성격: **LAB-PRECHECK**. ROSA Runtime PASS 또는 G5 Acceptance로 승격하지 않는다.
- Cluster-wide SCC/CRD/ClusterRole/MachineConfig/Node 변경은 수행하지 않는다.
- 실제 Namespace는 승인된 Team Code 기반 `j1-<purpose>` / `j2-<purpose>` 규칙을 사용한다.

실행 전 반드시 고정할 입력:
- `PORT_NS`: 승인 Team Namespace
- transaction-api / fds-engine 승인 image digest
- Registry pull 경로와 namespace-local pull secret
- 테스트 manifest source SHA
- Shared OCP cluster/version

## 2. P0-PORT-01 — OpenShift UID/SCC 호환성

### 목적
현재 Phase 1 manifest의 `runAsUser: 10001`, `runAsGroup: 999` 고정이 OpenShift restricted-v2 정책에서 수용되는지 확인하고, custom SCC 없이 arbitrary UID로 실행 가능한지 검증한다.

### 수집
```bash
oc get ns "$PORT_NS" -o jsonpath='{.metadata.annotations.openshift\.io/sa\.scc\.uid-range}{"\n"}'
oc get ns "$PORT_NS" -o jsonpath='{.metadata.annotations.openshift\.io/sa\.scc\.supplemental-groups}{"\n"}'
oc auth can-i use scc/restricted-v2
```

### T1 — 현 Phase 1 고정 UID manifest admission
- 현재 고정 `runAsUser/runAsGroup` 값을 유지한 최소 Deployment를 `--dry-run=server`로 제출한다.
- PASS면 실제 SCC/namespace 범위와 일치 이유를 기록한다.
- REJECT면 오류 원문을 보존한다. **custom SCC 추가로 우회하지 않는다.**

### T2 — Portable security overlay
고정 UID/GID만 제거하고 다음은 유지한다.
- `runAsNonRoot: true`
- `allowPrivilegeEscalation: false`
- `readOnlyRootFilesystem: true`
- `seccompProfile: RuntimeDefault`
- `capabilities.drop: ["ALL"]`
- `hostNetwork/hostPID/hostIPC: false`

Namespace-local 실제 Pod를 기동해 다음을 확인한다.
```bash
oc -n "$PORT_NS" get pod -l app=transaction-api -o jsonpath='{range .items[*]}{.metadata.name}{"\t"}{.spec.securityContext.runAsUser}{"\t"}{.status.phase}{"\n"}{end}'
oc -n "$PORT_NS" exec deploy/transaction-api -- id
```

성공 기준:
- Pod Running/Ready
- 실제 UID가 root가 아님
- `/livez` 성공
- read-only rootfs + `/tmp` write가 필요한 경우 emptyDir로만 성공
- custom privileged SCC 불필요

## 3. P0-PORT-02 — Portable workload base

Phase 2용 권위 workload base를 별도 파일군으로 만들기 전 확인한다.

Base에 허용:
- Deployment
- ClusterIP Service
- ConfigMap/Secret **reference**
- ServiceAccount/RBAC
- standard NetworkPolicy
- probes/resources
- portable Pod SecurityContext

Base에서 제외:
- NodePort `30080`
- edge01 `10.1.93.50`
- db01 `10.1.93.55`
- monitoring/control-plane/worker 고정 IP
- OpenShift Route
- SCC binding
- AWS IAM/OIDC/EBS/ELB/NAT/VPN
- HCP/Classic topology 값

성공 기준:
- `kubectl` schema 기준 정적 유효
- Shared OCP에서 server-side dry-run 성공
- HCP/Classic 값 없이 동일 base 생성 가능

## 4. P0-PORT-03 — OpenShift overlay

OpenShift overlay는 base를 대체하지 않고 추가/patch한다.

최소 대상:
- transaction-api 외부 노출: **ClusterIP base + OpenShift Route overlay**
- Namespace/Project target labels
- OpenShift UID/SCC 호환 security patch
- Registry pull secret reference
- target-specific NetworkPolicy CIDR

성공 기준:
- Route 삭제 시 base workload 자체는 유지
- HCP/Classic별 workload YAML 복제본을 만들지 않음
- overlay diff에 control-plane placement 값이 포함되지 않음

## 5. P0-PORT-04 — NetworkPolicy portability

W0에서 검증:
1. transaction-api → fds-engine TCP 8001 ALLOW
2. fds-engine → transaction-api 임의 역방향 신규 경로 DENY
3. DNS ALLOW
4. 미승인 namespace/pod → app DENY
5. monitoring 규칙은 P0 app 정책과 분리

ROSA에서만 최종 검증:
- transaction-api → On-Prem DB 5432
- ROSA source CIDR
- VPN/NACL/SG/OVN 결합
- Hybrid negative/recovery

주의: Kubernetes NetworkPolicy API가 동일해도 CNI 구현이 다르므로 Shared OCP PASS를 ROSA PASS로 승격하지 않는다.

## 6. P0-PORT-05 — RBAC / Delivery adapter

재사용:
- application ServiceAccount의 `automountServiceAccountToken: false`
- Runner는 기존 두 Deployment에 get/update/patch만 허용
- Secret read/create/delete/exec 금지

Phase 2 adapter:
- ROSA API endpoint
- target namespace
- short-lived credential/token
- approved registry/digest
- kubeconfig/context

성공 기준:
- build/scan 로직과 target deploy 로직 분리
- HCP/Classic 변경으로 Test/Build/Scan workflow가 바뀌지 않음
- target adapter만 교체 가능

## 7. P0-PORT-06 — Storage / Monitoring 경계

P0 application:
- 현재 business workload는 PVC를 필수 계약으로 사용하지 않으므로 topology blocker 아님.

P1/full-system monitoring:
- `fds-local-storage` / `k8s-worker03` local PV는 ROSA에 재사용 금지
- ROSA에서는 승인 CSI StorageClass 기반 PVC overlay 필요
- node-exporter hostNetwork/hostPID/hostPort/hostPath는 별도 managed-platform exception 검토

이 항목 때문에 P0 topology를 자동 HOLD하지 않지만, “전체 시스템 완전 이식 완료”로 표시하지 않는다.

## 8. PG-08 — IaC 계층 정적 Gate

`infra-terraform` / `infra-rosa`에 실제 코드가 생기기 전 설계 기준:

1. common network/interface inputs
2. AWS IAM/OIDC
3. ROSA topology-specific provisioning
4. cluster platform configuration
5. portable workload/overlay consumer

금지:
- HCP/Classic 분기가 application manifest 내부로 전파
- DB/Registry endpoint가 image에 하드코딩
- local-PV/Node hostname이 common module에 고정
- topology module이 application business config를 소유

검증:
- HCP↔Classic 변경 시 1,4,5 계층의 변경량을 diff로 산출
- topology-specific 변경은 주로 3 계층에 격리되는지 확인

## 9. Evidence Contract

각 시험은 다음을 남긴다.
- KST 시각
- Cluster/Version/Namespace
- source SHA / manifest SHA256
- 명령 / RC / stdout/stderr 원본
- admission result
- pod UID/GID/SCC(확인 가능한 범위)
- positive/negative test result
- cleanup 전/후 inventory
- 판정: PASS / FAIL / BLOCKED / NOT RUN

## 10. 현재 실행상태

- PLAN: **PREPARED**
- SHARED OCP RUNTIME: **NOT RUN**
- ROSA RUNTIME: **NOT RUN**
- PG-01: **HOLD**
- PG-02: **HOLD**
- PG-03: **HOLD**
- PG-08: **HOLD**
- topology: **UNDECIDED**
