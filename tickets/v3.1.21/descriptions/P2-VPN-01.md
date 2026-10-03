# P2-VPN-01 — OCI Relay / AWS Site-to-Site VPN

Version: v3.1.21 CANDIDATE
Source: https://github.com/321Team/fds-project-baseline/issues/37
Updated at: 2026-10-03T10:59:20Z
Source body SHA256: `7995d4738f53b1bd8ab8bda4d841665178402695f51713fc841a8adba1f91f21`
GitHub: open / None
Current disposition: Source lifecycle/AC retained; no new acceptance by this publication.

| Property | Current source value |
|---|---|
| Record ID | P2-VPN-01 |
| Phase | Phase 2 |
| Category | Hybrid Network / VPN |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-12 |
| End | 2026-10-14 |
| Calendar Days | 3 |
| Working Days | 3 |
| Lead | 이재환 |
| Support | 이권욱 |
| Exit Criteria | 승인 Transit 경로의 Tunnel UP, On-Prem↔VPC Route, UDP 500/4500/IPsec, Source·승인 TCP Path 및 장애 Evidence 확보 |
| Related Decision IDs | D10; D21 |
| Related Risk IDs | RISK-04; RISK-10; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #37 snapshot 2026-09-10T02:09:49Z; 일정: docs-v3.1.20 WBS + 2026-09-22 재계획 + 2026-09-24 일정 정합화 |
| Schedule Note | #35 전체 완료를 기다리지 않고 10-08 Stage-A handoff(VPC/Subnet/Route/VPN 입력) 수신 후 10-12 착수한다. #35 Full과 #37 완료는 모두 10-14 G4 판정 전에 충족해야 한다. |

## Source checklist

- [ ] On-Prem/VPC CIDR 중복을 방지한다.
- [ ] UDP 500/4500과 NAT-T 조건을 검증한다.
- [ ] 필수 목적지·포트만 허용한다.
- [ ] Route 전파와 Static Route의 권위 Source를 명시한다.
- [ ] Tunnel 재협상 절차를 기록한다.
- [ ] 승인 Tunnel이 UP이다.
- [ ] On-Prem↔VPC 승인 TCP 경로가 성공한다.
- [ ] 미승인 경로가 차단된다.
- [ ] Tunnel 중단·복구가 Runbook대로 재현된다.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

<!-- p2-vpn-d21-handoff-20261003:v1:start -->
## 2026-10-03 D21 → P2-VPN-01 권위 Handoff

> 이 블록이 아래 과거 OCI Relay/AWS managed S2S 후보 서술보다 우선한다. #37 실제 Tunnel/Route/Positive/Negative/Recovery Runtime은 아직 미실행이다.

### Selected path
- Transport Adapter: **`aws_ec2_eip_relay`**
- OCI Relay: D21 기술 PoC/Portability reference로 보존, **Primary Transit으로 사용하지 않음**
- On-Prem Gateway: `vpn-gw01 10.1.93.51` — `LOCAL_GATEWAY_READY=PASS`
- Region/VPC: `ap-northeast-2 / 10.20.0.0/16`
- Relay subnet/AZ: `10.20.110.0/24 / ap-northeast-2a / apne2-az1`
- Relay private IP: `10.20.110.10`
- instance/AMI: `t3.medium / ami-079a2667364cee804 / owner 125523088429`
- EIP: 1; auto public IPv4 disabled
- ENI source/destination check: false
- public SSH: DENY; management SSM/bootstrap
- SELinux Enforcing / firewalld enabled 유지

### IKE semantic contract
- IKEv2 only
- On-Prem initiates
- cloud endpoint is stable EIP
- On-Prem public source may change during an exchange
- responder authenticates explicit IKE ID; source IP is not peer identity
- NAT-T UDP/4500 required
- public ingress at AWS adapter: UDP/500·4500 only; 단일 관측 /32에 의존하지 않음
- secret material is never stored in Git/Issue/Evidence/Terraform state

### Selectors / routes
- protected selectors: `10.1.93.0/24 <-> 10.20.0.0/16`
- AWS route authority: Terraform, `10.1.93.0/24 -> Relay ENI`
- On-Prem minimum return route: `db01 10.1.93.55: 10.20.0.0/16 via 10.1.93.51`
- Harbor return route: D22가 On-Prem Harbor를 선택할 때만 추가

### D21 prerequisite already proven
- education-site UDP/500 and UDP/4500 packet arrival: PASS
- IKE_SA_INIT request/response: PASS
- NAT detection and UDP/4500 transition: PASS
- IKE_AUTH request/response: PASS
- dynamic public-source change inside one logical exchange: observed
- D21 pathcheck cleanup: PASS
- 이 결과는 #37 production Tunnel UP이 아님

### #37 acceptance remains
1. #35 Stage-A actual AWS resource IDs + exact Terraform source SHA handoff
2. AWS Relay bootstrap/config hash + secret boundary
3. approved Tunnel UP / IKE SA + Child/IPsec SA
4. VPC↔On-Prem route
5. approved TCP Positive
6. unauthorized Negative
7. restart/rekey/rebuild/reboot Recovery
8. raw evidence hashes + independent review

`D21_HANDOFF=CONFIRMED / LOCAL_GATEWAY_READY=PASS / AWS_RELAY_RESOURCE=NOT_CREATED / TUNNEL_RUNTIME=NOT_RUN / #37_DONE=NO`
<!-- p2-vpn-d21-handoff-20261003:v1:end -->

<!-- phase2-execution-data-20261002:issue-37:v1:start -->
## 2026-10-02 Execution Data / Review Contract — #37

### Ownership
- **Execution Lead / Runtime AC Acceptance:** 이재환
- **PMO/QA Review Owner:** 이권욱
- Code/Runbook/Evidence 독립 리뷰는 이권욱 우선. 작성/실행 충돌 시 다른 독립 Reviewer로 전환.
- 이하영은 #35 Producer이며 #37의 상시 Reviewer가 아니다.

### Confirmed pre-inputs
- OCI Relay private/public: `10.30.10.10` / `129.225.204.87`
- OCI VCN/Subnet: `10.30.0.0/16` / `10.30.10.0/24`
- OCI Relay source/destination check: disabled
- OCI NSG 현재 ingress: 관리용 Cloud Shell `168.138.35.119/32 -> TCP/22`만 확인; UDP 500/4500은 아직 미개방
- AWS Region: `ap-northeast-2`
- AWS project VPC design CIDR: `10.20.0.0/16`, 아직 NOT CREATED
- W0 기준 AWS VGW/CGW/VPN/TGW 기존 리소스: 0
- On-Prem/AWS/OCI known CIDR overlap 없음

### Entry blockers — 실제값 없으면 Tunnel 실행 금지
1. #36 D21 = GO
2. #35 `STAGE_A_READY=YES`
3. VPN attachment type/ID
4. AWS peer endpoint/CGW identity
5. Traffic selector(local/remote CIDR)
6. route authority(static/propagation)
7. IKE/IPsec proposal + auth 방식/Secret 취급
8. peer-specific NSG/firewalld source
9. reviewed Terraform/Runbook source SHA

### 최소보안
- peer 확정 전 OCI/AWS에 UDP 500/4500을 광범위하게 열지 않는다.
- 허용은 가능한 경우 peer exact IP(/32)과 승인 selector 기준으로 제한한다.
- PSK/credential 원문은 Issue/PR/Evidence에 기록하지 않는다.
- 현재 관리용 SSH rule과 VPN data-plane rule을 분리 추적한다.

### Runtime PASS
- IKE/IPsec SA + NAT-T 상태
- 승인 Route/selector 양방향
- 승인 TCP application path
- Source identity
- 비승인 Source/Port 차단
- tunnel down/recovery/rekey 또는 합의된 장애복구
- exact endpoint/config/source SHA/raw log/evidence ref

### Handoff
완료 시 #38/#47에 `endpoint + route + selector + security + evidence refs`를 고정 전달한다.

### 현재 Checkpoint
`OCI_SUBSTRATE=READY / AWS_STAGE_A=PENDING / D21=PENDING / VPN_RUNTIME=NOT_RUN / HANDOFF=NOT_READY`
<!-- phase2-execution-data-20261002:issue-37:v1:end -->

<!-- issue-execution-contract-20261001:v1:start -->
## 2026-10-01 VPN Execution Contract v1

### Entry
- #36 OCI Go/No-Go 결과 확정.
- #35 Stage-A의 VPC/Subnet/Route/VPN 입력을 exact evidence로 수신.

### Success
- Tunnel/SA 상태뿐 아니라 승인된 양방향 Route·Source IP·필수 Port 통신을 확인.
- 설정값과 실제 관측 경로가 일치해야 한다.
- #38/#47이 재사용할 endpoint/route/security 입력을 고정한다.

### Stop
- 광범위한 0.0.0.0/0 우회, 검증 목적의 보안통제 해제, 원인 미확인 route 확대 금지.
- #35 Full 미완료분이 G4에 영향 주면 G4에서 사실 상태로 차단한다.
<!-- issue-execution-contract-20261001:v1:end -->

<!-- shared-ocp-boundary-ref-20261001:issue-37:start -->
## 2026-10-01 공용 OCP 경계 상속

VPN 인수는 OCI/AWS Site-to-Site 실제 경로가 기준이다. 공용 OCP에서 가능한 연결성 확인은 Precheck로만 취급하고 VPN/G4 PASS 근거로 승격하지 않는다.

- Source of truth: #34 P2-ARC-01의 공용 OCP Multi-tenant 실행경계
- Scope/AC/Priority/Milestone/Review Authority 변경 없음.
<!-- shared-ocp-boundary-ref-20261001:issue-37:end -->



<!-- schedule-realign-20261001:issue-37:start -->
## 2026-10-01 일정·Dependency 정합화

- **Dependency split:** #37 착수조건은 #35의 10-08 Stage-A handoff이며, G4 완료조건은 #35 Full + #37 Full이다. 이 분리는 AC 축소가 아니라 선행 산출물의 소비시점을 명확히 하는 일정 제어다.

- Scope/AC/Priority/Milestone/Review Authority 변경 없음.
- 일정 조정은 재현성·무결성·추적성을 유지하면서 P0 동시 WIP와 선행조건 역전을 제거하기 위한 PMO 조정이다.
<!-- schedule-realign-20261001:issue-37:end -->
<!-- fds-oci-schedule:20260924:v1:start -->
## OCI 연계 일정 정합화 — 2026-09-24 KST

사용자 “일정 불일치부터 해소” 지시에 따라 일정 표시와 기간 계산을 정정했다. [2026-09-22 재계획](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-5779876610) 및 발행 docs-v3.1.20 WBS의 비근무일을 근거로 한다. 기존 10-06~10-09의 작업 가능일은 10-06·07·08의 3일이므로 **OCI 종료/D21 목표를 10-08로 통일**한다.

- **이 티켓의 계획:** 2026-10-08 ~ 2026-10-13 · 달력 6일 / 작업 3일. 10-08~10-13 계획. P2-OCI-01·P2-IAC-01 선행조건 충족 전에는 준비 작업만 수행하고 경로 적용은 선행조건 충족 후 착수한다. OCI No-Go 시 D21에서 승인된 Fallback만 사용한다.
- **연계 목표:** Phase 2 착수/설계 10-06, D21 10-08, IaC 10-06~13, VPN 준비 10-08~13, G4 10-13. VPN 적용은 기존 선행조건 충족 후이며, IaC 완료 목표와 G4가 같은 날이므로 실제 적용·검증 작업창 확보를 확인해야 한다.
- 아래 이전 정본 머리말·마일스톤 배정·보관 원문의 과거 일정은 이력이다. 현행 계획 일정은 이 정정과 갱신한 티켓 속성표를 따른다. [정정 근거 및 차기 정본 반영안](https://github.com/321Team/fds-project-baseline/blob/docs/oci-schedule-align-20260924/audit/oci-schedule-20260924/README.md).
- 계획 정정이며 OCI 도입 승인, D21 판정 완료, G4 통과를 뜻하지 않는다. 발행 정본 편입은 별도이며 상태·AC·담당·기존 선행조건은 유지한다.
- 동기화 잔여: #36의 별도 Target date는 10-09→10-08, GitHub Milestone #7 기한/현행 설명은 09-28→10-06, #8은 10-08→10-13 갱신이 필요하다. 현재 연결은 해당 필드 쓰기를 제공하지 않아 본문 갱신과 구분해 추적한다.
<!-- fds-oci-schedule:20260924:v1:end -->

---

<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P2-VPN-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P2-VPN-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 계획 단계. 승인 Transit·UDP500/4500/NAT-T·Source/Route와 복구 결과를 확정안에 연결.

**인계·관련 티켓:** [#35](https://github.com/321Team/fds-project-baseline/issues/35) · [#36](https://github.com/321Team/fds-project-baseline/issues/36) · [#38](https://github.com/321Team/fds-project-baseline/issues/38).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-notion-migration:2026-09-09 record-id:P2-VPN-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P2-VPN-01 -->
# P2-VPN-01 — OCI Relay / AWS Site-to-Site VPN

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-VPN-01 |
| Phase | Phase 2 |
| Category | Hybrid Network / VPN |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-12 |
| End | 2026-10-14 |
| Calendar Days | 3 |
| Working Days | 3 |
| Lead | 이재환 |
| Support | 이권욱 |
| Exit Criteria | 승인 Transit 경로의 Tunnel UP, On-Prem↔VPC Route, UDP 500/4500/IPsec, Source·승인 TCP Path 및 장애 Evidence 확보 |
| Related Decision IDs | D10; D21 |
| Related Risk IDs | RISK-04; RISK-10; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #37 snapshot 2026-09-10T02:09:49Z; 일정: docs-v3.1.20 WBS + 2026-09-22 재계획 + 2026-09-24 일정 정합화 |
| Schedule Note | #35 전체 완료를 기다리지 않고 10-08 Stage-A handoff(VPC/Subnet/Route/VPN 입력) 수신 후 10-12 착수한다. #35 Full과 #37 완료는 모두 10-14 G4 판정 전에 충족해야 한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-10T02:09:49Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #37](https://github.com/321Team/fds-project-baseline/issues/37), Issue 갱신 시각 `2026-09-10T02:09:49Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Hybrid Network 담당자로서 On-Prem과 AWS VPC 사이의 승인된 암호화 경로를 구축한다. 이를 통해 ROSA가 On-Prem DB와 필요한 서비스에 최소 포트로 접근한다.

---

# Scope

## In Scope

- vpn-gw01 `.51`
- OCI/Fallback Relay
- AWS S2S VPN
- Route
- Firewall
- Tunnel/Fail Test

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] On-Prem/VPC CIDR 중복을 방지한다.
- [ ] UDP 500/4500과 NAT-T 조건을 검증한다.
- [ ] 필수 목적지·포트만 허용한다.
- [ ] Route 전파와 Static Route의 권위 Source를 명시한다.
- [ ] Tunnel 재협상 절차를 기록한다.

---

# Acceptance Criteria

- [ ] 승인 Tunnel이 UP이다.
- [ ] On-Prem↔VPC 승인 TCP 경로가 성공한다.
- [ ] 미승인 경로가 차단된다.
- [ ] Tunnel 중단·복구가 Runbook대로 재현된다.

---

# 검증 및 증적

- Tunnel Status
- Route Tables
- Firewall/Security Group
- TCP/Source Test
- Failure/Recovery Log
- Evidence Path: `321Team/fds-project-evidence:evidence/P2-VPN-01/`

---

# Dependency

- **Blocked By:** P2-OCI-01; P2-IAC-01 Stage-A handoff
- **Blocks / Next:** P2-ROSA-01, P2-HYB-01
- **Related Ticket:** P2-E2E-01
- **Milestone:** G4 Cloud / VPN Ready

---

# Decision / Risk Control

- **Related Decision IDs:** D10; D21
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-04; RISK-10; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** 승인 Transit 경로의 Tunnel UP, On-Prem↔VPC Route, UDP 500/4500/IPsec, Source·승인 TCP Path 및 장애 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `14173d143f1eea5dc4bba86a9ea78c21ef53db02cd33d62741ce7ce604b5f8d9`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P2-VPN-01 -->
# P2-VPN-01 — OCI Relay / AWS Site-to-Site VPN

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P2-VPN-01 |
| Phase | Phase 2 |
| Category | Hybrid Network / VPN |
| Type | Task |
| Status | To Do |
| Priority | P0 |
| Start | 2026-10-01 |
| End | 2026-10-08 |
| Calendar Days | 8 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | 승인 Transit 경로의 Tunnel UP, On-Prem↔VPC Route, UDP 500/4500/IPsec, Source·승인 TCP Path 및 장애 Evidence 확보 |
| Related Decision IDs | D10; D21 |
| Related Risk IDs | RISK-04; RISK-10; RISK-12 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Phase1_Logical_Architecture_v3.1.2; Phase 2 OCI/AWS/ROSA Design; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 10-05는 비근무일이다. OCI No-Go 시 D21에서 승인된 Fallback만 사용한다. |

## 이관 기준 및 확인 사항

- 속성의 일정·담당·상태는 RELEASED v3.1.17 WBS(기준일 2026-09-04)를 우선 반영했다. 이후 별도 근거가 있는 변경만 아래에 명시한다.
- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`
- `FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx`

---

## Description — 보관 입력본

> 원본: `FDS_Notion_Remaining_Backlog_Manual_v1.9.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

# 🎯 User Story

Hybrid Network 담당자로서 On-Prem과 AWS VPC 사이의 승인된 암호화 경로를 구축한다. 이를 통해 ROSA가 On-Prem DB와 필요한 서비스에 최소 포트로 접근한다.

---

# 📌 Scope

## In Scope

- vpn-gw01 `.51`
- OCI/Fallback Relay
- AWS S2S VPN
- Route
- Firewall
- Tunnel/Fail Test

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 📋 핵심 요구사항

- [ ] On-Prem/VPC CIDR 중복을 방지한다.
- [ ] UDP 500/4500과 NAT-T 조건을 검증한다.
- [ ] 필수 목적지·포트만 허용한다.
- [ ] Route 전파와 Static Route의 권위 Source를 명시한다.
- [ ] Tunnel 재협상 절차를 기록한다.

---

# ✅ Acceptance Criteria

- [ ] 승인 Tunnel이 UP이다.
- [ ] On-Prem↔VPC 승인 TCP 경로가 성공한다.
- [ ] 미승인 경로가 차단된다.
- [ ] Tunnel 중단·복구가 Runbook대로 재현된다.

---

# 🧪 검증 및 증적

- Tunnel Status
- Route Tables
- Firewall/Security Group
- TCP/Source Test
- Failure/Recovery Log
- Evidence Path: `docs/evidence/P2-VPN-01/`

---

# 🔗 Dependency

- **Blocked By:** P2-OCI-01, P2-IAC-01
- **Blocks / Next:** P2-ROSA-01, P2-HYB-01
- **Related Ticket:** P2-E2E-01
- **Milestone:** G4 Cloud / VPN Ready

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D10; D21
- **Decision Control:** 관련 Decision Register를 준수하며 신규 의사결정이 발생하면 별도 Decision 레코드를 발행한다.
- **Related Risk IDs:** RISK-04; RISK-10; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** 승인 Transit 경로의 Tunnel UP, On-Prem↔VPC Route, UDP 500/4500/IPsec, Source·승인 TCP Path 및 장애 Evidence 확보
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>

