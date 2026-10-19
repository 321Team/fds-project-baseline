<!-- fds-canonical-live:v3.1.21 record-id:P2-OCI-01:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/P2-OCI-01.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 관련 추적 항목 **TS05**. 원본 AC와 각 항목의 환경·선행조건·중단/복구·증적 기준을 함께 적용한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:P2-OCI-01:end -->

<!-- d21-final-authority-20261003:v1:start -->
## 2026-10-03 D21 최종 권위 상태

> 이 블록이 아래 과거 `D21=PENDING` 기록보다 우선한다. #37 실제 Tunnel Acceptance와 #35 Apply는 별도 단계다.

- **D21 Decision:** FINAL
- **OCI Relay Primary:** **NO-GO — project suitability**
- **Selected single fallback / Transport Adapter:** **AWS EC2 + EIP self-managed Libreswan Relay**
- **Technical path feasibility:** PASS
  - education-site UDP/500·4500 packet arrival PASS
  - IKEv2 IKE_SA_INIT request/response PASS
  - NAT detection / UDP4500 transition PASS
  - IKE_AUTH request/response PASS
  - same logical exchange에서 Public source `121.160.42.93 -> 180.80.107.14` 변경 관측
- **NO-GO 의미:** OCI/Libreswan 기술 불가가 아님. AWS/ROSA가 목적지인 상황에서 OCI Primary는 On-Prem↔OCI + OCI↔AWS의 2-leg terminate/re-encrypt transit을 추가하여 provider-specific 상태·route·security·recovery 지점을 늘리므로 P0 R/I/T+Portability 목표에 부적합.
- **Selected adapter semantic contract:** On-Prem initiator / explicit IKE ID / dynamic public source / stable cloud endpoint / IKEv2+NAT-T.
- **Canonical final responder raw:** `d21-ike-observer-20261003T042646Z.log`, 8706 bytes, SHA256 `e5f754a3d66c6fe452605ff914a6294e87aa85bf6a345ec0fadb981f18745cb0`.
- **Pathcheck cleanup:** PASS.
- **Evidence repo publication:** PENDING.
- **Issue close:** HOLD until #34/#35/#37 exact handoff and evidence publication are linked.

### #35 / #37 Handoff
- adapter: `aws_ec2_eip_relay`
- Region/VPC: `ap-northeast-2 / 10.20.0.0/16`
- Relay subnet: `10.20.110.0/24`, `ap-northeast-2a / apne2-az1`
- Relay private IP: `10.20.110.10`
- instance/AMI: `t3.medium / ami-079a2667364cee804 / owner 125523088429`
- root: `gp3 40 GiB encrypted`
- EIP 1, auto public IPv4 off, source/destination check false
- public SSH deny, SSM/bootstrap management
- public ingress: UDP/500·4500 only; dynamic source 때문에 단일 /32을 권위 Source로 사용하지 않음
- selectors: `10.1.93.0/24 <-> 10.20.0.0/16`
- AWS route: `10.1.93.0/24 -> Relay ENI`
- On-Prem minimum return route: `db01 .55: 10.20.0.0/16 via 10.1.93.51`
- P0 single Relay SPOF accepted; #37 Done 전 rebuild/restart/rekey/recovery evidence 필수.
<!-- d21-final-authority-20261003:v1:end -->

<!-- phase2-execution-data-20261002:issue-36:v1:start -->
## 2026-10-02 Execution Data / Review Contract — #36

### Ownership
- **Execution/Decision Lead:** 이권욱
- 이권욱이 직접 실행·증적 생산한 건의 **독립 Evidence Review는 이하영/이재환 등 독립 Reviewer**가 수행한다.
- D21 Go/No-Go와 실제 #37 Tunnel Acceptance는 분리한다.

### W0 / Early Precheck — COMPLETE
- OCI Region: `ap-osaka-1`
- VCN/Subnet: `10.30.0.0/16` / `10.30.10.0/24`
- Relay: `fds-p2-oci-relay01`
- Shape: `VM.Standard.E5.Flex / 1 OCPU / 4 GB`
- Private/Public: `10.30.10.10` / Reserved `129.225.204.87`
- Source/Destination Check: disabled
- Oracle Linux 9.8 / SELinux Enforcing / firewalld active+enabled
- Libreswan 4.15 / local IPsec prerequisite + reboot persistence PASS
- Evidence PR #95: merged; W0 evidence publication 완료
- OCI native Budget: `fds-p2-oci-poc-budget`, SGD 50 MONTHLY, ACTUAL 50/80/100% alerts ACTIVE

### D21에서 확정할 것
- OCI Relay를 Phase 2 VPN 경로로 실제 채택할지 Go/No-Go
- Trial-credit PoC 비용/cleanup 수용
- #37에 넘길 Relay endpoint의 사용 승인
- Project Close(2026-10-26) paid-resource cleanup 책임

### #37 Handoff
D21=GO인 경우 #37에 다음을 전달한다.
- Relay Public/Private IP
- VCN/Subnet CIDR
- NSG identity/current rule inventory
- Libreswan/runtime prerequisite evidence ref
- Cost/cleanup boundary
- 아직 미확정인 peer/selector/auth는 **#37/#35 입력 이후 확정**하며 이 티켓에서 추정하지 않는다.

### 현재 Checkpoint
`W0_PRECHECK=COMPLETE / EVIDENCE=MERGED / COST_GUARDRAIL=PASS / D21=PENDING / VPN_TUNNEL_RUNTIME=NOT_RUN`
<!-- phase2-execution-data-20261002:issue-36:v1:end -->

<!-- oci-current-status-20261002-w0:start -->
## 2026-10-02 KST — OCI W0 현재 진행상태 / Billing·Resource·Security Precheck 반영

### 실행 분류
- 실제 OCI Runtime을 사용한 **Early Precheck/PoC**이다.
- #33 Phase 2 공식 Start, D21 GO, P2-VPN-01 Runtime 또는 G4 PASS로 확대하지 않는다.
- D21 Go/No-Go는 **PENDING**.

### Account / Subscription / Promotion — CONFIRMED
OCI Console 직접 확인:
- Account banner: **Free Tier account**
- Trial: **Free Trial ACTIVE**
- Subscription: **Universal Credits / ACTIVE**
- Type: **Infrastructure**
- Start: **2026-10-01 UTC**
- Total commitment: **SGD 400.00**
- Days remaining: **29 / 30**
- Credit remaining: **SGD 399.91 (99%)**
- Credit used: **SGD 0.09**
- SKUs used: **2**
- Regions used: **1**
- Upgrade 링크가 표시되며 PAYG upgrade는 현재 관측되지 않음

판정:
- 현재 E5 사용은 Free Trial promotional credit 소비 범위로 관리한다.
- 실제 카드/계좌 out-of-pocket charge는 **현재 관측되지 않음**.
- Trial 종료/credit 소진/유료 upgrade 여부는 지속 비용 Gate로 관리한다.

### Usage API / Rate — COST VISIBILITY PASS
Usage API 조회 구간: **2026-10-02 00:00~06:00 UTC**
- Compute / Standard - E5: **SGD 0.03109275**
- Compute / Standard - E5 - Memory: **SGD 0.00829140**
- Compute gross 합계: **SGD 0.03938415**
- VCN / Outbound Data Transfer Zone 2: **SGD 0.0**
- CREDIT: empty
- ALLCREDIT: empty
  - credit adjustment row 부재로만 해석하며 promotion balance 판정에는 사용하지 않음

Subscription Rate Card(2026-10-01~10-30):
- Standard E5 OCPU: **SGD 0.0415 / OCPU-hour**
- Standard E5 Memory: **SGD 0.0028 / GB-hour**
- Relay 1 OCPU / 4 GB 명목 rate: **SGD 0.0527/hour**

### Native Budget / Alert Guardrail — RUNTIME PASS
초기 read-only 확인:
- `oci budgets budget budget list ...` → **0 rows / no error**
- 당시 Native Budget resource: **0개**

적용 결과:
- Budget: `fds-p2-oci-poc-budget`
- Amount: **SGD 50 / MONTHLY**
- TargetType: **COMPARTMENT**
- Target: `fds-p2-oci`
- State: **ACTIVE**
- exact `budget get` read-back: **PASS**
- Actual / Forecast: 생성 직후 조회에서는 `null`

Alert Rule 최종 read-back:
- `fds-p2-oci-actual-50` — **ACTIVE / ACTUAL / PERCENTAGE / 50.0**
- `fds-p2-oci-actual-80` — **ACTIVE / ACTUAL / PERCENTAGE / 80.0**
- `fds-p2-oci-actual-100` — **ACTIVE / ACTUAL / PERCENTAGE / 100.0**
- 자동 stop/delete 동작: **없음** (알림 전용)

CLI 유의:
- 50/80 생성 시 `--wait-for-state ACTIVE` 후속 waiter에서 `TypeError: get_alert_rule() missing 1 required positional argument: 'alert_rule_id'` 재현.
- create 응답과 최종 list read-back에서 두 Rule 모두 ACTIVE였으므로 waiter 오류는 **NONBLOCKING CLI 후처리 defect**로 분리한다.
- 100% Rule은 waiter 없이 생성했고 최종 list에서 ACTIVE 확인.

판정:
- `BUDGET_GUARDRAIL_RUNTIME=PASS`
- Native Budget/Alert 구성은 완료.
- 프로젝트 전체 비용 정책(Target ≤$400 / Hard Stop $450 / Reserve $50 / Ceiling $500)을 대체하지 않으며 OCI PoC 조기경보용이다.

### Compute / Capacity — PASS
- Instance: `fds-p2-oci-relay01`
- Shape: `VM.Standard.E5.Flex`
- 1 OCPU / 4 GB
- State: **RUNNING**
- Oracle Linux 9.8
- Region/AD: `ap-osaka-1 / rBfb:AP-OSAKA-1-AD-1`
- E5 tenancy limits:
  - `standard-e5-core-count = 13`
  - `standard-e5-memory-count = 208`
- 현재 Relay 크기는 tenancy limit 내. 서비스 limit은 물리 host capacity 보장을 의미하지 않는다.

### Storage / Billable Resource Inventory — PASS
- Boot Volume: **47 GB / VPUs 10 / AVAILABLE**
- Additional Block Volume: **0개**
- NAT Gateway: **0개**
- Load Balancer: **0개**
- DRG: **0개**
- IPSec Connection: **0개**
- CPE: **0개**
- Reserved Public IP: `fds-p2-oci-relay-ip` / **ASSIGNED**
- VCN private DNS resolver/view/zones는 관측됨
- full compartment structured-search에서 별도 숨은 billable resource는 관측되지 않음
- 현 Usage API에서 유료 line은 E5 OCPU + Memory가 확인됨

### Network Runtime / Exposure — PASS
- VCN: `fds-p2-oci-vcn` / `10.30.0.0/16`
- Relay subnet: `fds-p2-oci-relay-subnet` / `10.30.10.0/24`
- Public IP allowed subnet
- IGW: `fds-p2-oci-igw` / AVAILABLE / enabled
- Route: `0.0.0.0/0 -> IGW`
- remote AWS/On-Prem prefix route: 아직 없음
- known CIDR overlap:
  - On-Prem `10.1.93.0/24`
  - AWS `10.20.0.0/16`
  - OCI `10.30.0.0/16`
  - 현재 알려진 범위에서 overlap 없음

Subnet Security List `fds-p2-oci-relay-sl`:
- ingress: **0**
- egress: stateful all -> `0.0.0.0/0`

Relay NSG `fds-p2-oci-relay-nsg`:
- 실제 VNIC attachment: **PASS**
- 현재 ingress 1건:
  - `168.138.35.119/32 -> TCP/22`
  - description: `TEMP Cloud Shell SSH P2-OCI-01`
- `0.0.0.0/0 -> TCP/22`: NSG에 없음
- UDP/500: 없음
- UDP/4500: 없음
- `skip-source-dest-check=true`: PASS
- VCN Default Security List의 broad SSH rule은 존재하나 relay subnet에는 custom SL만 연결되어 있어 relay 적용 rule로 계산하지 않는다.

### OS / Libreswan / Reboot Persistence — PASS
- SELinux: Enforcing
- firewalld: active/enabled
- Libreswan: 4.15
- ipsec.service: active/enabled
- `ip_forward=1`
- `rp_filter(all/default/enp0s5/ip_vti0/lo)=0`
- redirects=0
- Pluto UDP/500, UDP/4500 local listeners: PASS
- reboot persistence: PASS

### Evidence — REVIEW / MERGE / PUBLICATION PASS
- Evidence PR: https://github.com/321Team/fds-project-evidence/pull/95
- reviewed exact HEAD: `1dca37a592c103a395c19fc09c73c48cc8714b13`
- independent APPROVED: `hayeounglee`, `supreme33-kr`
- evidence-layout Run #171: SUCCESS
- merge commit: `d2791df4af8107d3eb713b6dab2104668ff239ab`
- merged: **2026-10-02 14:37:02 KST**
- main raw/manifest re-read: PASS
- publication 범위는 local prerequisite + reboot persistence이며 tunnel/D21/G4를 의미하지 않음

### #35 / #37 Dependency
- #35 P2-IAC-01: open / assignee `hayeounglee`
- 최신 재확인 시 `infra-terraform` open PR: **0건**
- #35 Stage-A exact handoff는 아직 PENDING
- #37 P2-VPN-01은 local Relay substrate/evidence를 수신했으나 Entry는 기존대로 **D21 + #35 Stage-A exact handoff** 필요

### 임시 관리 경로
- Cloud Shell SSH allow: `168.138.35.119/32 -> TCP/22`
- D21/#35 handoff 대기 중 임시 유지
- D21 결정 또는 관리 작업 종료 시 제거하고 cleanup evidence를 남긴다.
- peer 확정 전 UDP 500/4500 외부 허용을 추가하지 않는다.

### 잔여 작업
1. #35 Stage-A: AWS Region/VPC/Subnet/Route/VPN attachment/state identity/plan/evidence 수신
2. D21 Go/No-Go 확정
3. peer Public IP / traffic selector / auth / IKE/NAT-T parameter 확정
4. IPsec/NAT-T/Route Runtime + approved ALLOW/unapproved DENY + failure/recovery
5. #37 P2-VPN-01 handoff
6. D21/관리 종료 후 임시 SSH /32 cleanup
7. Project close 이전 paid-resource teardown 재확인

### 현재 판정
`ACCOUNT_FREE_TRIAL=PASS / PROMO_BALANCE=PASS / COST_VISIBILITY=PASS / RESOURCE_INVENTORY=PASS / NETWORK_EXPOSURE=PASS / COMPUTE_LIMIT=PASS / OS_BASELINE=PASS / REBOOT_PERSISTENCE=PASS / EVIDENCE_PUBLICATION=PASS / BUDGET_CREATE=PASS / BUDGET_READBACK=PASS / ALERT50=PASS / ALERT80=PASS / ALERT100=PASS / BUDGET_GUARDRAIL_RUNTIME=PASS / ALERT_WAITER_CLI_ERROR=NONBLOCKING / IAC_STAGE_A=PENDING / TUNNEL_RUNTIME=NOT_RUN / D21=PENDING`
<!-- oci-current-status-20261002-w0:end -->

<!-- issue-execution-contract-20261001:v1:start -->
## 2026-10-01 OCI Go/No-Go Contract v1

### 판단 입력
- 인증/권한, Relay/Public Endpoint 가능성, IPsec/NAT-T/Route 제약, 일정·비용.
- 자동화/인증이 불안정하면 반복 시도 자체를 성공 근거로 사용하지 않는다.

### Decision
- **GO:** #37가 사용할 Endpoint/Route/권한이 실제 재현 가능하고 증적화 가능.
- **NO-GO:** OCI 경로가 일정/G4를 위협하거나 권한·네트워크 제약으로 재현 불가.
- **Fallback:** 승인된 AWS/대체 경로를 #34/#37에 명시하고 이유를 기록.

### Exit
결정에는 선택안, 실패한 경로, Owner, 비용/보안 영향, #37 입력값을 남긴다.
<!-- issue-execution-contract-20261001:v1:end -->

<!-- shared-ocp-boundary-ref-20261001:issue-36:start -->
## 2026-10-01 공용 OCP 경계 상속

본 티켓은 OCI Relay Go/No-Go이며 공용 OCP가 실행대상을 대체하지 않는다. OCP 관련 사전검증이 생기면 #34의 `SHARED_OCP_LAB` 경계를 상속하고 OCI/ROSA 실제 경로 판정과 분리한다.

- Source of truth: #34 P2-ARC-01의 공용 OCP Multi-tenant 실행경계
- Scope/AC/Priority/Milestone/Review Authority 변경 없음.
<!-- shared-ocp-boundary-ref-20261001:issue-36:end -->

<!-- fds-oci-schedule:20260924:v1:start -->
## OCI 연계 일정 정합화 — 2026-09-24 KST

사용자 “일정 불일치부터 해소” 지시에 따라 일정 표시와 기간 계산을 정정했다. [2026-09-22 재계획](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-5779876206) 및 발행 docs-v3.1.20 WBS의 비근무일을 근거로 한다. 기존 10-06~10-09의 작업 가능일은 10-06·07·08의 3일이므로 **OCI 종료/D21 목표를 10-08로 통일**한다.

- **이 티켓의 계획:** 2026-10-06 ~ 2026-10-08 · 달력 3일 / 작업 3일. D21 목표는 10-08이다. 10-09 비근무일 제외 후에도 가용 작업일은 3일이다. No-Go 시 Vendor Endpoint→AWS EC2+EIP Relay→Overlay 순으로 승인된 단일 Fallback을 선택한다.
- **연계 목표:** Phase 2 착수/설계 10-06, D21 10-08, IaC 10-06~13, VPN 준비 10-08~13, G4 10-13. VPN 적용은 기존 선행조건 충족 후이며, IaC 완료 목표와 G4가 같은 날이므로 실제 적용·검증 작업창 확보를 확인해야 한다.
- 아래 이전 정본 머리말·마일스톤 배정·보관 원문의 과거 일정은 이력이다. 현행 계획 일정은 이 정정과 갱신한 티켓 속성표를 따른다. [정정 근거 및 차기 정본 반영안](https://github.com/321Team/fds-project-baseline/blob/docs/oci-schedule-align-20260924/audit/oci-schedule-20260924/README.md).
- 계획 정정이며 OCI 도입 승인, D21 판정 완료, G4 통과를 뜻하지 않는다. 발행 정본 편입은 별도이며 상태·AC·담당·기존 선행조건은 유지한다.
- 동기화 잔여: #36의 별도 Target date는 10-09→10-08, GitHub Milestone #7 기한/현행 설명은 09-28→10-06, #8은 10-08→10-13 갱신이 필요하다. 현재 연결은 해당 필드 쓰기를 제공하지 않아 본문 갱신과 구분해 추적한다.
<!-- fds-oci-schedule:20260924:v1:end -->

---

<!-- fds-evidence-path:20260923:v1:start -->
## 증적 경로 일괄 변경 — 2026-09-23

사용자 지시(“티켓에 대한 내용은 fds-project-evidence로 일괄 변경”)에 따라 현행 본문의 Evidence Path를 증적 저장소 [`321Team/fds-project-evidence`](https://github.com/321Team/fds-project-evidence)로 변경했다. 경로 구조는 기존 편입 관례(`evidence/<Record ID>/`)를 따른다.

- 변경 전: `docs/evidence/P2-OCI-01/` → 변경 후: `321Team/fds-project-evidence` `evidence/P2-OCI-01/`
- 이 변경은 증적 보관 위치의 지정이다. 해당 경로에 증적이 편입됐거나 AC가 충족됐다는 뜻이 아니다. 편입은 증적 저장소 PR의 독립 리뷰([EVIDENCE_POLICY](https://github.com/321Team/fds-project-evidence/blob/main/governance/EVIDENCE_POLICY.md))로 별도 판단한다.
- Status·AC 체크·Lead/Support·일정·승인/종결은 변경하지 않았다. 아래 `<details>` 보관 원문과 서버 수집 경로 표기는 당시 기록으로 그대로 둔다.
- 정본(Ticket Pack) 반영은 차기 정본 후보에서 처리한다. 발행 docs-v3.1.20의 기존 경로 문구는 이력이다.
<!-- fds-evidence-path:20260923:v1:end -->

---

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** 계획 단계. OCI Go/No-Go 및 단일 Fallback·비용/일정/보안 승인 기록. 체크포인트와 완료일 구분.

**인계·관련 티켓:** [#35](https://github.com/321Team/fds-project-baseline/issues/35) · [#37](https://github.com/321Team/fds-project-baseline/issues/37).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-milestone-assignment:2026-09-11 issue:36 -->
## 대표 Milestone 배정 — 2026-09-11

- **추적 Milestone:** G4 Cloud / VPN Ready (GitHub #8)
- **배정 성격:** P2 잠정 계획 · 이권욱 사용자 지시에 따른 대표 추적 항목 지정.
- **배정 근거:** WBS 2026-09-28~10-02 OCI Go/No-Go와 후속 VPN 구축 관계에 따라 G4에 연결한다. 티켓의 10-02 의사결정 체크포인트는 유지하며 G4 날짜로 대체하지 않는다.
- **출처:** [발행 정본 v3.1.18 WBS](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/wbs/FDS_v3.1.18_WBS_and_Gantt_v1.0.xlsx)
- **일정 원칙:** 일정은 고정된 필수 기한이 아닌 조정 가능한 계획 목표다. 선행조건과 영향 확인 후 유연하게 조정하며, 실제 완료일·승인·Runtime 증적 요건과 구분한다.
- **적용 범위:** 대표 Milestone 연결과 이 근거 기록. 기존 상태·완료 사실·AC·담당·티켓 Start/End 및 Gate 요건을 유지한다.

---

<!-- fds-notion-migration:2026-09-09 record-id:P2-OCI-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:P2-OCI-01 -->
# P2-OCI-01 — OCI Relay Go / No-Go

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P2-OCI-01 |
| Phase | Phase 2 |
| Category | Milestone / Hybrid Network |
| Type | Decision |
| Status | In Progress |
| Priority | P0 |
| Start | 2026-10-07 |
| End | 2026-10-08 |
| Calendar Days | 2 |
| Working Days | 2 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | OCI Relay 가능성·권한·Public Endpoint·IPsec/NAT-T·Route를 검증하고 Primary 또는 승인 Fallback 경로를 선택 |
| Related Decision IDs | D10; D21 |
| Related Risk IDs | RISK-10; RISK-12 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #36 snapshot 2026-09-09T12:07:26Z; 일정: docs-v3.1.20 WBS + 2026-09-22 재계획 + 2026-09-24 일정 정합화; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | D21 결정창 10-07~10-08 유지. 교육장 UDP/500·4500 경로 관측 → return/NAT-T/IKE 검증 → 보안 노출·return-route·SPOF 판단 → Transport Adapter 선택을 거쳐 #34 최종 Freeze 및 #35 Stage-A에 인계한다. 경로 관측/Decision 미완료 시 D21 OPEN과 후속 HOLD를 유지한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **To Do / open**. 원본 갱신 시각: `2026-09-09T12:07:26Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

기준 시점의 To Do 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #36](https://github.com/321Team/fds-project-baseline/issues/36), Issue 갱신 시각 `2026-09-09T12:07:26Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.

---

# User Story

Hybrid Network 담당자로서 OCI Relay를 Primary Transit으로 사용할 수 있는지 조기에 판정한다. 이를 통해 실패 가능성이 큰 경로를 G4 직전까지 끌고 가지 않고 대체경로를 통제한다.

---

# Scope

## In Scope

- OCI 권한/Endpoint
- IPsec/NAT-T
- Route
- AWS VPN 연계 가능성
- Fallback 비교
- Go/No-Go 승인

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 핵심 요구사항

- [ ] 필요 계정·권한·Quota를 확인한다.
- [ ] Public Endpoint와 NAT 조건을 검증한다.
- [ ] On-Prem/AWS CIDR 중복을 확인한다.
- [ ] Fallback별 비용·일정·보안 영향을 기록한다.

---

# Acceptance Criteria

- [ ] OCI Primary의 실행 가능 여부가 증적으로 판정된다.
- [ ] Go 또는 단일 Fallback이 승인된다.
- [ ] P2-VPN-01과 P2-IAC-01 입력값이 확정된다.
- [ ] 미결 전제와 Owner/Due가 0건이다.

---

# 검증 및 증적

- OCI/AWS 권한·리소스 확인
- Endpoint/Route Test
- Fallback 비교표
- Decision D21
- 갱신 Architecture/WBS
- Evidence Path: `321Team/fds-project-evidence:evidence/P2-OCI-01/`

---

# Dependency

- **Blocked By:** MS-P1-CLOSE-01
- **Blocks / Next:** P2-VPN-01
- **Related Ticket:** P2-IAC-01
- **Milestone:** OCI Go/No-Go — 2026-10-08 (계획 체크포인트; 판정 Pending)

---

# Decision / Risk Control

- **Related Decision IDs:** D10; D21
- **Decision Control:** D21 결과로 Primary/Fallback과 비용·일정 영향도를 승인한다.
- **Related Risk IDs:** RISK-10; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** OCI Relay 가능성·권한·Public Endpoint·IPsec/NAT-T·Route를 검증하고 Primary 또는 승인 Fallback 경로를 선택
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `25fa85700fabf55d1988551283ccbfc3edeb3514646e3400da22b0b81b32048d`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:P2-OCI-01 -->
# P2-OCI-01 — OCI Relay Go / No-Go

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | P2-OCI-01 |
| Phase | Phase 2 |
| Category | Milestone / Hybrid Network |
| Type | Decision |
| Status | To Do |
| Priority | P0 |
| Start | 2026-09-28 |
| End | 2026-10-02 |
| Calendar Days | 5 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | OCI Relay 가능성·권한·Public Endpoint·IPsec/NAT-T·Route를 검증하고 Primary 또는 승인 Fallback 경로를 선택 |
| Related Decision IDs | D10; D21 |
| Related Risk IDs | RISK-10; RISK-12 |
| Source | FDS_Project_Implementation_Baseline_v3.1.12; FDS_Phase1_Logical_Architecture_v3.1.2; Phase 2 OCI/AWS/ROSA Design; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 10-02 Go/No-Go를 넘기지 않는다. No-Go 시 Vendor Endpoint→AWS EC2+EIP Relay→Overlay 순으로 승인된 Fallback을 선택한다. |

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

Hybrid Network 담당자로서 OCI Relay를 Primary Transit으로 사용할 수 있는지 조기에 판정한다. 이를 통해 실패 가능성이 큰 경로를 G4 직전까지 끌고 가지 않고 대체경로를 통제한다.

---

# 📌 Scope

## In Scope

- OCI 권한/Endpoint
- IPsec/NAT-T
- Route
- AWS VPN 연계 가능성
- Fallback 비교
- Go/No-Go 승인

## Out of Scope

- 명시되지 않은 P1/P2 기능과 Scope Out 기능은 본 티켓에서 구현하지 않는다.

---

# 📋 핵심 요구사항

- [ ] 필요 계정·권한·Quota를 확인한다.
- [ ] Public Endpoint와 NAT 조건을 검증한다.
- [ ] On-Prem/AWS CIDR 중복을 확인한다.
- [ ] Fallback별 비용·일정·보안 영향을 기록한다.

---

# ✅ Acceptance Criteria

- [ ] OCI Primary의 실행 가능 여부가 증적으로 판정된다.
- [ ] Go 또는 단일 Fallback이 승인된다.
- [ ] P2-VPN-01과 P2-IAC-01 입력값이 확정된다.
- [ ] 미결 전제와 Owner/Due가 0건이다.

---

# 🧪 검증 및 증적

- OCI/AWS 권한·리소스 확인
- Endpoint/Route Test
- Fallback 비교표
- Decision D21
- 갱신 Architecture/WBS
- Evidence Path: `docs/evidence/P2-OCI-01/`

---

# 🔗 Dependency

- **Blocked By:** MS-P1-CLOSE-01
- **Blocks / Next:** P2-VPN-01
- **Related Ticket:** P2-IAC-01
- **Milestone:** OCI Go/No-Go — 2026-10-02

---

# ⚖️ Decision / Risk Control

- **Related Decision IDs:** D10; D21
- **Decision Control:** D21 결과로 Primary/Fallback과 비용·일정 영향도를 승인한다.
- **Related Risk IDs:** RISK-10; RISK-12
- **Risk Control:** 관련 Risk의 예방·탐지·복구 통제를 Acceptance와 Evidence에 연결한다.

---

# 📝 Completion Record

- **Result:** TBD
- **Status:** To Do
- **Exit Criteria:** OCI Relay 가능성·권한·Public Endpoint·IPsec/NAT-T·Route를 검증하고 Primary 또는 승인 Fallback 경로를 선택
- **Completed Date:** 미입력
- **Reviewer / Approver:** 미입력 — 입력 시 풀네임 사용
````

</details>
