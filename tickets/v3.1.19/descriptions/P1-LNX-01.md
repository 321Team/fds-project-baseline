# P1-LNX-01 — CentOS Stream 10 Linux / Network Baseline

> v3.1.19 CANDIDATE / NOT RELEASED · 2026-09-17 20:28 KST

## 현행 속성

| Property | 입력값 |
|---|---|
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
| Source | Baseline v3.1.19 CANDIDATE; GitHub #66 @ 2026-09-14T15:17:42Z; 원문 SHA256 aaaa46cb8d3a194ec754f793b45fce655113adab92ae6f1db28a94ad9b6735b7 |
| Schedule Note | 설계·사전구축 구간에서 2026-08-26 조기 완료. P1-LNX-01 완료판정은 Linux 필수조건과 Network Verify 기준이며 containerd/kubelet/kubeadm/API/Calico 동작은 포함하지 않는다. 해당 Role Check는 P1-K8S-01로 이관한다. |

## 상태와 인수 경계

현재 티켓 속성·AC·종결 이력을 수집했다. 이번 문서 통합에서 새로운 Runtime 시험이나 완료 승인을 수행하지 않았다.

- GitHub lifecycle: closed; Milestone: G1 Infrastructure Ready
- 일정은 조정 가능한 계획이며 실제 완료일·Gate 승인일과 구분한다.
- 원문·후속 댓글: [원본 티켓](https://github.com/321Team/fds-project-baseline/issues/66), [고정 수집본](../sources/issue-66.json).
- 상위 속성표는 이 후보의 현행 표다. 아래 원문은 수집 시점의 변경/승인/AC 이력이며 과거 버전 문구를 현재 발행 상태로 사용하지 않는다.

## 원문 보존

<details>
<summary>수집한 GitHub 본문 전체 — SHA256 aaaa46cb8d3a194ec754f793b45fce655113adab92ae6f1db28a94ad9b6735b7</summary>

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** Linux 원 종결 유지. NTP 정책·K8S 보호 전환은 후속 #14/#10/#19 ; A01/A02.

- 원 Linux 종결을 재개하지 않는다. 고정 NTP 정책/최종 보호 전환·K8S Runtime 인수는 #14/#10/#19에서 다룬다. 기존 시간 확인 PASS를 새 NTP 정책 승인으로 확장하지 않는다.

**인계·관련 티켓:** [#10](https://github.com/321Team/fds-project-baseline/issues/10) · [#14](https://github.com/321Team/fds-project-baseline/issues/14) · [#19](https://github.com/321Team/fds-project-baseline/issues/19).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P1-LNX-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P1-LNX-01 -->
# P1-LNX-01 — CentOS Stream 10 Linux / Network Baseline

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

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


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **Done / closed**. 원본 갱신 시각: `2026-09-10T02:10:15Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

P1-LNX-01 원 종결과 당시 PASS는 유지한다. FUP-04의 일부 원본 수신 한계 및 이후 Runtime drift 검증을 원 종결과 구분한다.

근거: [Issue #66](https://github.com/321Team/fds-project-baseline/issues/66), Issue 갱신 시각 `2026-09-10T02:10:15Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

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

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `a11bcdd6143b38bea709ffbb7b1c2ea20ecd2f26422b275721ddedc5b4066500`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P1-LNX-01 -->
# P1-LNX-01 — CentOS Stream 10 Linux / Network Baseline

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
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
| Source | FDS_Project_Implementation_Baseline_v3.1.2`, `FDS_Network_Baseline_v2.3`, `D-NET-01_Closure_Report_v1.0`, `P1-LNX-01 Network Apply/Test Kit; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 설계·사전구축 구간에서 2026-08-26 조기 완료. P1-LNX-01 완료판정은 Linux 필수조건과 Network Verify 기준이며 containerd/kubelet/kubeadm/API/Calico 동작은 포함하지 않는다. 해당 Role Check는 P1-K8S-01로 이관한다. |

## 이관 기준 및 확인 사항

- 2026-08-26 Linux/Network 종결 이력이다. 당시 Bootstrap DNS 8.8.8.8 기록은 현행 Resolver 지시가 아니며, 이후 P1-DNS-01 및 CR-P1-ANS-01-01의 승인 DNS .52/.53 전환이 우선한다.
- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `P1-LNX-01_Notion_Properties_Description_v1.4.md`

---

## Description — 보관 입력본

> 원본: `P1-LNX-01_Notion_Properties_Description_v1.4.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

# 🎯 User Story

Linux 운영자로서,  
Kubernetes 예정 Node에 공통 적용할 CentOS Stream 10 Linux 및 Network Baseline을 구축하고 검증하고자 한다.

이를 통해 P1-K8S-01이 OS·NIC·Route·MTU 오류를 재분석하지 않고 containerd, kubeadm, kubelet 및 Calico 구축에 집중할 수 있도록 한다.

---

# 📋 핵심 요구사항

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

# ✅ Acceptance Criteria

- [x] Kubernetes 예정 Node의 Linux 필수조건이 PASS다.
- [x] Kubernetes 예정 Node의 Network Verify 결과가 모두 `FAIL=0`이다.
- [x] IP / Prefix / MTU / Required Route가 Baseline과 일치한다.
- [x] Default Route가 필요한 Profile은 정확히 1개를 보유한다.
- [x] Default Route 금지 Profile은 Internet Route가 존재하지 않는다.
- [x] DO_NOT_USE IP가 Node에 할당되지 않았다.
- [x] Apply/Test 결과와 이전 상태 Backup 정보가 남아 있다.
- [x] Kubernetes Service Role Check 제외근거와 후속 이관 대상이 기록되었다.

---

# 📸 증적

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

# 🔗 Dependency

- **Blocked By:** D-NET-01 — DONE / CLOSED
- **Blocks / Next:** P1-K8S-01
- **Related Ticket:** P1-NET-01, P1-DNS-01
- **Milestone:** G1 Infrastructure Ready 선행 완료

> containerd, kubelet, kubeadm, Kubernetes API `6443`, Calico 및 Cluster Service 상태는 P1-LNX-01의 완료판정에서 제외한다.  
> 해당 항목은 P1-K8S-01의 Acceptance Criteria로 관리한다.  
> BIND Forward Zone과 내부 FQDN 전환은 P1-DNS-01에서 별도 수행한다.

---

# 📝 Final Result

- **Result:** PASS
- **Status:** DONE
- **Acceptance:** Linux 필수조건 PASS / Network Verify FAIL=0
- **Closed Basis Date:** 2026-08-26
- **Next:** P1-K8S-01 / P1-DNS-01
````

</details>


</details>
