# DEC-P2-COST-01 — Phase 2 Cloud Cost / Lifecycle Budget Control

> Decision input approved by user on 2026-09-30 KST.
> Candidate publication: PR #112 / release/v3.1.21.
> Native GitHub Issue creation requires human application under TICKET_SYNC_POLICY §5.1.

## Decision

**APPROVED**

- Total Budget Ceiling: **$500**
- Target Spend: **≤ $400**
- Operational Hard Stop: **$450**
- Protected Reserve: **$50 ($450~$500)**
- AWS/ROSA baseline Region: **Asia Pacific (Seoul) / `ap-northeast-2` — APPROVED 2026-10-02 KST**
- ROSA topology: **HCP vs Classic — PENDING Cost-to-Complete comparison**

## Interpretation

1. $400 이하를 정상 목표로 운영한다.
2. $400 도달 또는 초과 예상 시 P1/선택 실험을 Deferred 우선으로 전환하고 P0 잔여비용을 재예측한다.
3. $450은 신규 유료 소비의 Operational Hard Stop이다.
4. $450~$500은 신규 기능 예산이 아니라 billing lag, teardown delay, cleanup residual에 대비한 보호 Reserve다.
5. $500은 총 상한이며 Credit/Promo/지원금이 남더라도 확대하지 않는다.
6. Hard Stop은 단순 현재 청구액이 아니라 Actual/Gross + 확인 가능한 미반영/Projected cost를 기준으로 선제 적용한다.
7. Reserve를 P1 확장, 신규 PoC, 일정 연장 또는 정상 운영비로 전용하지 않는다.
8. Phase 2 AWS/ROSA 실행 기준 리전은 `ap-northeast-2`(Seoul)로 고정한다.
9. Region 결정은 HCP/Classic topology 승인으로 간주하지 않는다. 동일 workload/Runtime 조건의 Cost-to-Complete 비교와 prerequisite 확인 후 Cost GO에서 topology를 확정한다.

## Decision Boundary

이 결정은 비용/생명주기 통제 승인이다.

다음을 승인하지 않는다.

- AWS/ROSA 리소스 생성 자체
- ROSA HCP/Classic topology 선택 자체
- GitOps/Compliance 등 P1 기능 도입
- Runtime Acceptance
- Gate 통과
- Project Close
- $450 이상 신규 기능 소비

## Related Tickets

#34, #35, #37, #38, #42, #49, #55, #57

## Native ticket draft properties

| Property | Candidate value |
|---|---|
| Record ID | DEC-P2-COST-01 |
| Phase | Phase 2 |
| Category | Cloud / Cost / Lifecycle Governance |
| Type | Decision |
| Decision Result | APPROVED |
| Priority | P0 |
| Decision Date | 2026-09-30 |
| Owner | 이권욱 |
| Related Risk | RISK-11 및 Cloud cost/lifecycle 관련 위험 |
| Source | 2026-09-30 사용자 승인; PR #112 cost policy audit |
| Exit Criteria | $500 ceiling, ≤$400 target, $450 hard stop, $50 protected reserve와 threshold action/lifecycle/evidence rule이 정본 후보 및 관련 티켓에 연결됨 |

Status/Start/End/Milestone은 Native Issue 생성 시 최신 WBS/Project 카탈로그와 대조해 확정한다. 이 파일만으로 GitHub Issue가 생성되거나 정본 발행된 것으로 보지 않는다.
