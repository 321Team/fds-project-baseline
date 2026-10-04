<!-- fds-canonical-live:v3.1.21 record-id:D-NET-01:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/D-NET-01.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 해당 업무의 기존 AC·Exit Criteria와 실행/인수 구분을 유지한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:D-NET-01:end -->

<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/D-NET-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/D-NET-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 원 Network Freeze 종결 유지. 새 .56 관리/DNS/반환 경로·IF 변경을 A07/R05로 추적.

- .56 신규 할당·DNS ACL/ipset·ansible01 .10→.56:22·반환 .10/32 via .58을 #78/#74 변경과 현재 IF/Network As-built에 연결한다. 기존 Physical Node /24 반환 경로를 프록시 /32와 혼동하지 않는다.

**인계·관련 티켓:** [#14](https://github.com/321Team/fds-project-baseline/issues/14) · [#24](https://github.com/321Team/fds-project-baseline/issues/24) · [#78](https://github.com/321Team/fds-project-baseline/issues/78).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:D-NET-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:D-NET-01 -->
# D-NET-01 — Physical / Management Network Design Freeze

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

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
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #60 snapshot 2026-09-10T02:10:11Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 2026-08-26 실제 완료. 기존 계획보다 Closure가 1일 연장되었으나 Network Design/Implementation/Evidence를 포함해 DONE 처리. 후속 구축 범위는 P1-K8S-01 및 P1-DNS-01로 이관한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **Done / closed**. 원본 갱신 시각: `2026-09-10T02:10:11Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

D-NET-01 Done/2026-08-26 유지. 기존 종결 문서와 일부 8/28 보완 원본은 매핑 후보로 연결됐으나 FUP-04 최초 로그·Windows/VMware·관리 경로 전문은 잔여다. 8/28 자료를 8/26 최초 증적으로 소급하지 않는다.

근거: [Issue #60](https://github.com/321Team/fds-project-baseline/issues/60), Issue 갱신 시각 `2026-09-10T02:10:11Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

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
- Evidence Path: `321Team/fds-project-evidence:evidence/D-NET-01/`
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

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `275771afc8b23ae2f5172c2d9545ba329158541e96916a2269eed3810bcedeea`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:D-NET-01 -->
# D-NET-01 — Physical / Management Network Design Freeze

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
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
| Source | FDS_Network_Baseline_v2.3`, `FDS_Project_Implementation_Baseline_v3.1.2`, `D-NET-01_Closure_Report_v1.0`, `FDS_Notion_Network_Parameter_Patch_v1.2; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 2026-08-26 실제 완료. 기존 계획보다 Closure가 1일 연장되었으나 Network Design/Implementation/Evidence를 포함해 DONE 처리. 후속 구축 범위는 P1-K8S-01 및 P1-DNS-01로 이관한다. |

## 이관 기준 및 확인 사항

- 종결일 2026-08-26. 확보한 종결 Description과 Closed Register에 없는 계획·분류·담당 속성은 추정하지 않고 원본 미확인으로 표시했다. 본문 내 후속 티켓 상태·기술값은 당시 이력이며 현행 값은 v3.1.17 및 후속 변경 기록을 따른다.
- 17개 속성은 D-NET-01 입력본 v1.4에서 복원했다. Type=Task를 원문대로 보존하며 ID의 D 접두어만으로 Decision으로 바꾸지 않는다.
- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_Notion_Closed_Descriptions_D-ARC-01_D-NET-01_D-WBS-01_v1.2.md`
- `D-NET-01_Notion_Properties_Description_v1.4.md`

---

## Description — 보관 입력본

> 원본: `FDS_Notion_Closed_Descriptions_D-ARC-01_D-NET-01_D-WBS-01_v1.2.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

# 🎯 User Story

Network 담당자로서 8대 Windows/VMware 환경의 Physical Network와 Management Network를 설계·고정하고 실제 통신 결과로 검증한다.

이를 통해 프로젝트가 제어할 수 없는 현장 Gateway 조건에서도 Management Source IP를 보존하고, Kubernetes·DNS·CI/CD 등 후속 구축이 재해석 없이 사용할 수 있는 승인된 Network Baseline을 제공한다.

---

# 📌 Scope

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

# 📋 핵심 요구사항

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

# ✅ Acceptance Criteria

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

# 🧪 검증 및 증적

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

# 🔗 Dependency

- **Blocked By:** 없음 — 설계·현장 검증·Closure 완료
- **Blocks / Next:** `P1-K8S-01`, `P1-DNS-01`
- **Related Ticket:** `P1-LNX-01`, `P1-NET-01`
- **Milestone Contribution:** G0의 Architecture / Network / WBS 항목 중 Network `PASS`; G1 선행조건 제공

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** `D05`, `D13`, `D14`, `D15`, `D16`
- **Decision Control:** Bridged Endpoint, VMnet 분리, Physical Return Route, 내부 Source NAT 금지, 비관리 Gateway 및 Reserved / DO_NOT_USE 주소를 승인된 Network Baseline과 동일하게 유지한다.
- **Related Risk IDs:** `RISK-02`, `RISK-04`
- **Risk Control:** 신규 VM은 DAD/ARP/TCP 사전검증을 수행하고, 비관리 Gateway의 ICMP 응답만으로 PASS/FAIL을 판정하지 않는다. 승인된 Route와 실제 TCP 경로 및 Source Preservation을 함께 검증한다.
- **Change Control:** IP, CIDR, VMnet 역할, Route, NAT, Endpoint 또는 관련 인터페이스 변경은 D-NET / Interface Change Request와 영향도 검토 후 반영한다.

---

# 📝 Completion Record

- **Result:** `PASS`
- **Status:** `DONE`
- **Ticket Gate:** `CLOSED`
- **Exit Criteria:** Windows server01~08 PostBuild `FAIL=0`, VMnet0/VMnet1/VMnet8 분리, Physical Return Route via `10.1.93.58`, Source Preservation `PASS=6/FAIL=0`, Management VM 및 `mgmt-gw01` Verify `FAIL=0`, Closure Report 승인
- **Completed Date:** `2026-08-26`
- **Reviewer / Approver:** Network Baseline 및 Closure 승인 기록 참조
- **Closure Boundary:** 본 티켓의 종결은 Network 설계·검증 범위에 한한다. `D-SEC-01`은 별도 `IN PROGRESS / Lead 이하영`이며, G0 전체 상태는 `CONDITIONAL PASS`다.
- **Next:** `P1-K8S-01` / `P1-DNS-01`
````

</details>
