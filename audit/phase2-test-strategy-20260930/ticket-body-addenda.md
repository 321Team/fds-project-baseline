# Ticket Addenda Candidate — P2-TEST-STRATEGY-01

> 사용자 승인: 2026-09-30 KST
> 상태: **CANDIDATE / HUMAN APPLY REQUIRED**
> Issue 본문 문단 추가는 TICKET_SYNC_POLICY §5.1에 따라 AI가 수행하지 않는다.
> 이 파일은 차기 정본/Ticket Pack/WBS 재생성과 담당자 수동 본문 반영의 입력이다.

## 공통 문구

Phase 2 P0 검증은 `W0 PRECHECK → W1 G4 → W2 G5 → W3 G6 → 10-23 CLOSE/TEARDOWN` Window로 운영한다. 제공 OCP/CI에서 제거 가능한 결함은 유료 ROSA에 반입하지 않으며, 실제 ROSA는 G4에 가까운 시점에 생성해 G5→G6를 동일 Cluster에서 연속 검증한다. $400 Target 이후 P1은 Deferred-first, $450은 신규 유료 Runtime Hard Stop이다. Full ROSA recreate는 P0 필수가 아니며 조건부 P1이다.

## #33 MS-P2-START-01
Phase 2 Start 시 #119 포함 Phase 1 Failure Contract의 승인/잔여판정, DEC-P2-COST-01, P0 Cost-aware Test Strategy를 인계 입력으로 확인한다. 이는 기존 Close/Start AC를 확대하지 않고 실행 준비 체크로 사용한다.

## #34 P2-ARC-01
Architecture Freeze에는 W0~W3 Runtime Window, ROSA Create Cost GO, 10-23 teardown 경계를 연결한다. 기존 Region/CIDR/D21~D26/Interface AC는 유지한다.

## #35 P2-IAC-01
ROSA 유료 Create 전에 fmt/validate/Plan Review와 비용발생 리소스/Destroy 전제를 고정한다. 재현성은 P0에서 re-plan drift 없음 + App redeploy + final teardown으로 증명하며 Full ROSA recreate를 자동 추가하지 않는다.

## #36 P2-OCI-01
D21은 10-08까지 Primary 또는 단일 Fallback으로 결정한다. 추가 조사로 전체 P2 유료 Runtime Window를 지연시키지 않는다. Fallback 비용/일정/보안 영향 기록은 기존 AC를 따른다.

## #37 P2-VPN-01
G4까지 승인 Transit의 Tunnel/Route/TCP 기본 path와 recovery 입력을 확보한다. ROSA를 먼저 장시간 기동한 상태에서 VPN 원인을 탐색하지 않는 것을 원칙으로 한다.

## #38 P2-ROSA-01
10-12부터 creation readiness 준비는 가능하되 실제 ROSA Create는 G4 근처로 최대한 늦춘다. W2/W3는 같은 Cluster를 사용하며 10-23 Final Evidence 후 teardown을 기본값으로 한다.

## #43 P2-APP-01
제공 OCP의 LAB-RUNTIME/PRECHECK는 OpenShift compatibility 선검증으로 소비할 수 있으나 ROSA Runtime PASS를 대체하지 않는다. ROSA에서는 Ready/Route/exposure/R01/R02/R04/R07 Smoke를 별도로 확보한다.

## #46 P2-CICD-01
기본 유료 Delivery Evidence는 RUN-A 정상 배포와 RUN-B Test/Scan 실패차단 두 종류로 집중한다. 동일 실패를 Source/Config 변경 없이 반복하지 않는다. #120 Go 전 Runner direct contract를 유지한다.

## #47 P2-HYB-01
10-20부터 Hybrid 기본 TCP/DB path 성공을 우선 확보한다. #50과 같은 Runtime Window에서 Negative/Failure/Recovery를 연속 실행하도록 준비한다.

## #50 P2-E2E-01
10-21에 정상/Rule/DB/Negative/Failure-Recovery 대부분을 수행하고 10-22는 Final Regression/Evidence 확정일로 사용한다. DB 장애와 fds-engine 장애 Expected Result는 #119 승인 결과를 구분해 적용한다.

## #49 P2-DOC-01
각 paid Window의 Source SHA/Runtime/Result/Evidence SHA/Control Cost/Resource Inventory/teardown을 Source→Runtime→Evidence→Cost chain으로 문서화한다.

## #55 P2-REV-01
Review에서 Window 준수, paid retest 근거, $400/$450 threshold, Full Recreate 미수행 근거 또는 별도 P1 결과, 10-23 teardown 상태를 검토한다.

## #57 MS-PROJECT-CLOSE-01
별도 승인 Demo 요구가 없으면 10-23 이후 ROSA를 유지하지 않는다. 10-26 Close는 Resource deletion, 잔여 Projected Cost, Known Issue/Deferred를 Evidence로 판정한다.

## #119 CR-P1-APP-01-01
Phase 2 E2E의 DB/FDS 장애 Expected Result가 이 CR의 승인 결과를 소비한다. 이 전략은 CR의 정책을 새로 승인하거나 AC를 변경하지 않는다.

## #120 / #121
GitOps/Compliance는 P1 non-blocking 유지. P0 결함, $400 초과 예상, G5/G6 일정 영향, 공급/권한 미확정 중 하나라도 있으면 Runtime 구현은 Deferred-first로 처리한다.

## 운영 코멘트 적용 후 snapshot

- #33: updated_at `2026-09-30T13:38:39Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/33#issuecomment-5912449502)
- #34: updated_at `2026-09-30T13:38:54Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-5912453444)
- #35: updated_at `2026-09-30T13:39:08Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5912457590)
- #36: updated_at `2026-09-30T13:39:24Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/36#issuecomment-5912462098)
- #37: updated_at `2026-09-30T13:39:38Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/37#issuecomment-5912466439)
- #38: updated_at `2026-09-30T13:39:52Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/38#issuecomment-5912470914)
- #43: updated_at `2026-09-30T13:40:06Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/43#issuecomment-5912475099)
- #46: updated_at `2026-09-30T13:40:21Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/46#issuecomment-5912479459)
- #47: updated_at `2026-09-30T13:40:36Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/47#issuecomment-5912483670)
- #50: updated_at `2026-09-30T13:40:50Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/50#issuecomment-5912487784)
- #49: updated_at `2026-09-30T13:41:04Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-5912491664)
- #55: updated_at `2026-09-30T13:41:18Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/55#issuecomment-5912495364)
- #57: updated_at `2026-09-30T13:41:33Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/57#issuecomment-5912499666)
- #119: updated_at `2026-09-30T13:41:47Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/119#issuecomment-5912503337)
- #120: updated_at `2026-09-30T13:42:00Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/120#issuecomment-5912507218)
- #121: updated_at `2026-09-30T13:42:16Z` — [strategy comment](https://github.com/321Team/fds-project-baseline/issues/121#issuecomment-5912511435)

본문 수동 반영 시 위 snapshot 이후 추가 변경이 없는지 다시 확인한다.
