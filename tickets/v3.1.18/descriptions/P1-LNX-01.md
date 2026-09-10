<!-- fds-canonical-description:v3.1.18 record-id:P1-LNX-01 -->
# P1-LNX-01 — CentOS Stream 10 Linux / Network Baseline

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-LNX-01 |
| Phase | Phase 1 |
| Category | Linux / Network Baseline |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-24 |
| End | 2026-08-26 |
| Calendar Days | 3 |
| Working Days | 3 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Kubernetes 예정 Node의 CentOS Stream 10 Linux 필수조건 PASS, Static Network/Route/MTU/DNS 기준 검증, Network Verify FAIL=0, Evidence 및 Rollback 정보 확보, Kubernetes Service Role Check는 P1-K8S-01로 이관 |
| Related Decision IDs | D01 — 3인 / 8 Server / CentOS 10`, `D05 — Bridged Node / Service Endpoint`, `D13 — VMnet1/VMnet8 분리`, `D14 — Physical Return Route / Source NAT 금지`, `D15 — Gateway 비관리 제약`, `D16 — Reserved / DO_NOT_USE IP |
| Related Risk IDs | RISK-02 — Bridged Multi-MAC 제한`, `RISK-03 — CentOS Stream 10 Kubernetes 조합 검증 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #66 snapshot 2026-09-10T02:10:15Z |
| Schedule Note | 설계·사전구축 구간에서 2026-08-26 조기 완료. P1-LNX-01 완료판정은 Linux 필수조건과 Network Verify 기준이며 containerd/kubelet/kubeadm/API/Calico 동작은 포함하지 않는다. 해당 Role Check는 P1-K8S-01로 이관한다. |

## 현재 실행·검토 상태

P1-LNX-01 원 종결과 당시 PASS는 유지한다. FUP-04의 일부 원본 수신 한계 및 이후 Runtime drift 검증을 원 종결과 구분한다.

근거: [Issue #66](https://github.com/321Team/fds-project-baseline/issues/66), Issue 갱신 시각 `2026-09-10T02:10:15Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.

---

# User Story

Linux 운영자로서,  
Kubernetes 예정 Node에 공통 적용할 CentOS Stream 10 Linux 및 Network Baseline을 구축하고 검증하고자 한다.

이를 통해 P1-K8S-01이 OS·NIC·Route·MTU 오류를 재분석하지 않고 containerd, kubeadm, kubelet 및 Calico 구축에 집중할 수 있도록 한다.

---

# 핵심 요구사항

- [x] Kubernetes 예정 Node에 CentOS Stream 10 Linux Baseline을 적용한다.
- [x] NetworkManager 기반 Static Network와 Hostname 기준을 적용한다.
- [x] Physical Network는 `10.1.93.0/24`, Gateway는 `10.1.93.254`를 사용한다.
- [x] Bootstrap DNS는 `8.8.8.8`, MTU는 `1500`을 사용한다.
- [x] VMnet1 `10.250.10.0/24`와 VMnet8 `192.168.10.0/24`의 역할을 분리한다.
- [x] 필요한 Static Route와 금지된 Default Route 조건을 검증한다.
- [x] `.100/.101/.106`은 DO_NOT_USE로 취급한다.
- [x] Network 적용 전 Backup과 Rollback 정보를 확보한다.
- [x] 검증 결과를 Node별 Evidence로 저장한다.

---

# Acceptance Criteria

- [x] Kubernetes 예정 Node의 Linux 필수조건이 PASS다.
- [x] Kubernetes 예정 Node의 Network Verify 결과가 모두 `FAIL=0`이다.
- [x] IP / Prefix / MTU / Required Route가 Baseline과 일치한다.
- [x] Default Route가 필요한 Profile은 정확히 1개를 보유한다.
- [x] Default Route 금지 Profile은 Internet Route가 존재하지 않는다.
- [x] DO_NOT_USE IP가 Node에 할당되지 않았다.
- [x] Apply/Test 결과와 이전 상태 Backup 정보가 남아 있다.
- [x] Kubernetes Service Role Check 제외근거와 후속 이관 대상이 기록되었다.

---

# 증적

- Kubernetes 예정 Node Linux Prerequisite 결과
- Node별 Network Verify Report
- `hostnamectl`
- `nmcli device status`
- `ip -br -4 address`
- `ip -4 route`
- `ip -4 neigh`
- MTU / DNS / Firewall 상태
- Network Apply Backup 및 Previous State
- Evidence Path: `/var/tmp/p1-lnx-01-network-evidence/`
- Project Evidence Path: `docs/evidence/P1-LNX-01/`

---

# Dependency

- **Blocked By:** D-NET-01 — DONE / CLOSED
- **Blocks / Next:** P1-K8S-01
- **Related Ticket:** P1-NET-01, P1-DNS-01
- **Milestone:** G1 Infrastructure Ready 선행 완료

> containerd, kubelet, kubeadm, Kubernetes API `6443`, Calico 및 Cluster Service 상태는 P1-LNX-01의 완료판정에서 제외한다.  
> 해당 항목은 P1-K8S-01의 Acceptance Criteria로 관리한다.  
> BIND Forward Zone과 내부 FQDN 전환은 P1-DNS-01에서 별도 수행한다.

---

# Final Result

- **Result:** PASS
- **Status:** DONE
- **Acceptance:** Linux 필수조건 PASS / Network Verify FAIL=0
- **Closed Basis Date:** 2026-08-26
- **Next:** P1-K8S-01 / P1-DNS-01
