<!-- fds-canonical-description:v3.1.18 record-id:D-NET-01 -->
# D-NET-01 — Physical / Management Network Design Freeze

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | D-NET-01 |
| Phase | Design |
| Category | Network / Infrastructure Design |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-24 |
| End | 2026-08-26 |
| Calendar Days | 3 |
| Working Days | 3 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Windows server01~08 PostBuild FAIL=0, VMnet0/VMnet1/VMnet8 분리, Physical Return Route via 10.1.93.58, Source Preservation PASS=6/FAIL=0, Management VM 및 mgmt-gw01 Verify FAIL=0, Closure Report 승인 |
| Related Decision IDs | D05 — Bridged Node / Service Endpoint`, `D13 — VMnet1/VMnet8 분리`, `D14 — Physical Return Route / Source NAT 금지`, `D15 — 10.1.93.254 프로젝트 비관리`, `D16 — Reserved / DO_NOT_USE IP |
| Related Risk IDs | RISK-02 — Bridged Multi-MAC 제한 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #60 snapshot 2026-09-10T02:10:11Z |
| Schedule Note | 2026-08-26 실제 완료. 기존 계획보다 Closure가 1일 연장되었으나 Network Design/Implementation/Evidence를 포함해 DONE 처리. 후속 구축 범위는 P1-K8S-01 및 P1-DNS-01로 이관한다. |

## 현재 실행·검토 상태

D-NET-01 Done/2026-08-26 유지. 기존 종결 문서와 일부 8/28 보완 원본은 매핑 후보로 연결됐으나 FUP-04 최초 로그·Windows/VMware·관리 경로 전문은 잔여다. 8/28 자료를 8/26 최초 증적으로 소급하지 않는다.

근거: [Issue #60](https://github.com/321Team/fds-project-baseline/issues/60), Issue 갱신 시각 `2026-09-10T02:10:11Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.

---

# User Story

Network 담당자로서 8대 Windows/VMware 환경의 Physical Network와 Management Network를 설계·고정하고 실제 통신 결과로 검증한다.

이를 통해 프로젝트가 제어할 수 없는 현장 Gateway 조건에서도 Management Source IP를 보존하고, Kubernetes·DNS·CI/CD 등 후속 구축이 재해석 없이 사용할 수 있는 승인된 Network Baseline을 제공한다.

---

# Scope

## In Scope

- Physical LAN, Windows Host Fixed IP 및 FDS VM IPAM 확정
- VMware `VMnet0` / `VMnet1` / `VMnet8` 역할과 Subnet 분리
- `mgmt-gw01` Dual NIC, IP Forwarding, Physical Return Route 구성
- 내부 Source NAT 금지 및 외부 목적지 조건부 Masquerade 경계 확정
- Management Source Preservation 검증
- Bootstrap DNS, MTU, Reserved / DO_NOT_USE 주소 확정
- Windows server01~08, Kubernetes 예정 Node, Management VM, `mgmt-gw01` 검증 및 Closure Evidence 확보

## Out of Scope

- containerd, kubelet, kubeadm, Kubernetes API Server 및 Calico 구성 — `P1-K8S-01`로 이관
- BIND Primary/Secondary 및 `fds.internal` Forward Zone 구현 — `P1-DNS-01`로 이관
- Reverse Zone / PTR — `N/A — Out of Scope`
- 현장 Gateway `10.1.93.254`의 설정 변경 또는 관리권 확보

---

# 핵심 요구사항

- [x] Physical LAN을 `10.1.93.0/24`, Gateway를 `10.1.93.254`로 확정한다.
- [x] Bootstrap DNS를 `8.8.8.8`, MTU를 `1500`으로 확정한다.
- [x] `VMnet0`은 `Automatic`이 아니라 실제 Windows `이더넷` Adapter에 명시적으로 Bridged 연결한다.
- [x] `VMnet1`은 `10.250.10.0/24` Host-only, VMware DHCP Off로 구성한다.
- [x] server01의 VMnet1 Host Adapter는 `10.250.10.254/24`로 고정하고 Default Route를 두지 않는다.
- [x] `VMnet8`은 `192.168.10.0/24` NAT로 분리하고 FDS VM NIC 연결을 금지한다.
- [x] `mgmt-gw01`은 Physical `10.1.93.58/24`와 Management `10.250.10.1/24`를 사용한다.
- [x] 모든 Physical FDS VM에 `10.250.10.0/24 via 10.1.93.58` 반환 경로를 구성한다.
- [x] 내부 목적지에는 Source NAT를 금지하고 외부 인터넷 목적지에만 조건부 Masquerade를 허용한다.
- [x] `.56/.57/.59`는 Reserved, `.100/.101/.106`은 DO_NOT_USE로 관리한다.
- [x] Pod `10.244.0.0/16`, Service `10.96.0.0/12`, AWS VPC `10.20.0.0/16`의 비중복을 확인한다.

---

# Acceptance Criteria

- [x] Windows server01~08 PostBuild 결과가 모두 `FAIL=0`이다.
- [x] Kubernetes 예정 Node 6대의 Linux 필수조건이 PASS다.
- [x] Kubernetes 예정 Node 6대의 Network Verify가 모두 `FAIL=0`이다.
- [x] Physical Node 6대의 Management Return Route가 `10.1.93.58` 경유로 동작한다.
- [x] `ansible01(10.250.10.10)`에서 Physical Node로 접속할 때 Remote Observed Source가 원본 주소로 유지된다.
- [x] Management Source Preservation 결과가 `PASS=6`, `FAIL=0`이다.
- [x] `ansible01`, `cicd-runner01`, `monitor01` Network Verify가 모두 `FAIL=0`이다.
- [x] `mgmt-gw01` Verify 결과가 `FAIL=0`이다.
- [x] `FDS_Network_Baseline_v2.3`과 `D-NET-01_Closure_Report_v1.0`이 승인·보관되었다.

---

# 검증 및 증적

- `01_Windows_PostBuild_server01-08`
- `02_VMware_Virtual_Network_Editor`
- `03_Linux_Node_Network_Verify`
- `04_K8s_Linux_Prerequisites`
- `05_Physical_Return_Route`
- `06_Source_Preservation_PASS6`
- `07_Management_VM_Verify`
- `08_mgmt-gw01_Verify`
- `09_DO_NOT_USE_IP_Exception`
- `10_D-NET-01_Closure`
- Evidence Path: `docs/evidence/D-NET-01/`
- Configuration Baseline: `FDS_Network_Baseline_v2.3`
- Closure Record: `D-NET-01_Closure_Report_v1.0`

---

# Dependency

- **Blocked By:** 없음 — 설계·현장 검증·Closure 완료
- **Blocks / Next:** `P1-K8S-01`, `P1-DNS-01`
- **Related Ticket:** `P1-LNX-01`, `P1-NET-01`
- **Milestone Contribution:** G0의 Architecture / Network / WBS 항목 중 Network `PASS`; G1 선행조건 제공

---

# Decision / Risk Control

- **Related Decision IDs:** `D05`, `D13`, `D14`, `D15`, `D16`
- **Decision Control:** Bridged Endpoint, VMnet 분리, Physical Return Route, 내부 Source NAT 금지, 비관리 Gateway 및 Reserved / DO_NOT_USE 주소를 승인된 Network Baseline과 동일하게 유지한다.
- **Related Risk IDs:** `RISK-02`, `RISK-04`
- **Risk Control:** 신규 VM은 DAD/ARP/TCP 사전검증을 수행하고, 비관리 Gateway의 ICMP 응답만으로 PASS/FAIL을 판정하지 않는다. 승인된 Route와 실제 TCP 경로 및 Source Preservation을 함께 검증한다.
- **Change Control:** IP, CIDR, VMnet 역할, Route, NAT, Endpoint 또는 관련 인터페이스 변경은 D-NET / Interface Change Request와 영향도 검토 후 반영한다.

---

# Completion Record

- **Result:** `PASS`
- **Status:** `DONE`
- **Ticket Gate:** `CLOSED`
- **Exit Criteria:** Windows server01~08 PostBuild `FAIL=0`, VMnet0/VMnet1/VMnet8 분리, Physical Return Route via `10.1.93.58`, Source Preservation `PASS=6/FAIL=0`, Management VM 및 `mgmt-gw01` Verify `FAIL=0`, Closure Report 승인
- **Completed Date:** `2026-08-26`
- **Reviewer / Approver:** Network Baseline 및 Closure 승인 기록 참조
- **Closure Boundary:** 본 티켓의 종결은 Network 설계·검증 범위에 한한다. `D-SEC-01`은 별도 `IN PROGRESS / Lead 이하영`이며, G0 전체 상태는 `CONDITIONAL PASS`다.
- **Next:** `P1-K8S-01` / `P1-DNS-01`
