# Phase 2 Cloud Cost Policy — 2026-09-30 KST

## 1. 결정 상태

- Record ID: **DEC-P2-COST-01**
- 사용자 결정: **APPROVED — 2026-09-30 KST**
- 현행 정본: `docs-v3.1.20 / RELEASED`
- 차기 정본 후보: Draft PR #112 / `release/v3.1.21`
- Priority: **P0 cost/lifecycle control**
- 적용 범위: Phase 2에서 발생하는 프로젝트 귀속 Cloud/ROSA/AWS 유료 비용
- Native Decision Issue: **NOT CREATED — HUMAN APPLY REQUIRED**
- 이유: `governance/TICKET_SYNC_POLICY.md §5.1`에 따라 AI 도구가 Issue 본문을 신규 작성/문단 추가하지 않는다. 이 PR에서 Decision record와 본문 후보를 준비하고 관련 티켓에는 운영 코멘트로 연결한다.

이 결정은 예산 통제를 승인한 것이며, AWS/ROSA provisioning, 비용 발생, Runtime/Gate 승인 자체를 승인한 것은 아니다.

## 2. 승인 예산 정책

| 구간 | 기준 | 운영 규칙 |
|---|---:|---|
| Total Budget Ceiling | **$500** | 프로젝트 총 비용 상한. Credit/Promo 적용 여부와 별개로 프로젝트 귀속 gross spend 기준으로 관리 |
| Target Spend | **≤ $400** | 정상 목표 구간 |
| Target 초과 경계 | **$400** | 신규 P1/선택 실험 중단 또는 Deferred 우선, 잔여 P0 완료비용 재예측 |
| Operational Hard Stop | **$450** | 신규 유료 리소스 생성·확장 중단, 비필수 리소스 종료/삭제 및 비용 증가 억제 |
| Protected Reserve | **$50 ($450~$500)** | billing lag, 삭제/종료 지연, cleanup residual 등 불가피한 잔여 과금 대응 전용 |
| Absolute Ceiling | **$500** | 신규 소비 허용 기준이 아니라 초과 방지용 최종 상한 |

정책 표기:

> **Target Spend ≤ $400 / Operational Hard Stop $450 / Protected Reserve $50 / Total Ceiling $500**

## 3. 비용 산정 기준

비용 통제는 단순히 Billing 화면의 현재 숫자만 보지 않는다.

**Control Cost = Actual/Gross Project Spend + 확인 가능한 미반영·발생예상 비용**

Hard Stop 판정 시 다음을 포함한다.

- 이미 반영된 프로젝트 귀속 비용
- 실행 중 리소스의 청구 지연분 또는 아직 Billing 화면에 반영되지 않은 추정 발생분
- 삭제/종료 요청 후 실제 과금 종료가 확인되기 전까지의 잔여 비용
- Marketplace/서비스 비용이 Promo/Credit으로 상계되지 않더라도 프로젝트 귀속 비용이면 총예산에 포함

Credit, Promo, 교육기관 지원금 또는 환급은 **$500 Ceiling을 확대하는 근거로 사용하지 않는다.**

## 4. Threshold별 행동

### $0 ~ $400

- 승인된 P0 구현과 검증을 정상 수행한다.
- P1은 P0 일정/예산을 침해하지 않는 범위에서만 수행한다.
- 신규 장시간 리소스 또는 recreate 전 잔여 예상 비용을 확인한다.

### $400 도달 또는 초과 예상

- 신규 P1/선택 실험을 기본적으로 Deferred 한다.
- ROSA → APP → CI/CD → Hybrid → E2E → Documentation/Close의 P0 잔여 비용을 재예측한다.
- 현재 리소스 유지시간과 teardown 시점을 재확정한다.
- P0 완료에 필요하지 않은 유료 리소스는 종료한다.

### $450 도달 또는 Control Cost 기준 초과 예상

- **Operational Hard Stop 발동**.
- 신규 유료 리소스 생성, scale-out, recreate, 선택 시험을 중단한다.
- 비필수 실행을 종료하고 teardown/cleanup을 수행한다.
- Reserve를 새 기능 또는 일정 연장에 사용하지 않는다.
- 이미 발생한 비용·billing lag·cleanup residual만 Reserve에서 흡수한다.

### $450 ~ $500 Protected Reserve

- 정상 실행 예산이 아니다.
- 신규 기능/PoC/P1/재실험용 사용 금지.
- 불가피한 잔여 과금과 안전한 cleanup에만 사용한다.
- $500 초과가 예상되면 추가 소비를 허용하지 않고 미종결 기능은 Deferred/Known Issue로 전환한다.

## 5. Lifecycle 통제

- 24x7 장기 실행을 기본값으로 두지 않는다.
- Create → Verify → Destroy 경로를 IaC로 재현 가능하게 유지한다.
- 실제 통합 Cluster는 P0 검증 창에 맞춰 최소 기간만 유지한다.
- Project Close 전에 프로젝트 귀속 Cloud resource inventory와 teardown 상태를 확인한다.
- 삭제 요청 자체가 비용 종료 증적은 아니다. 실제 리소스 상태와 Billing/Cost inventory를 별도로 확인한다.
- 비용 통제를 위해 보안 통제, 증적 요건 또는 승인된 AC를 임의로 약화하지 않는다.

## 6. 티켓 영향

- #34 P2-ARC-01: Architecture Freeze에 Budget/Lifecycle control을 P0 설계 입력으로 추가
- #35 P2-IAC-01: Terraform Plan/Apply/Destroy와 비용 발생 리소스 inventory를 정책에 연결
- #38 P2-ROSA-01: ROSA 생성·유지·삭제 시간을 Cost threshold와 연결
- #42 DEC-P2-REG-01: Registry 선택 시 프로젝트 귀속 유료 비용을 동일 Ceiling에 포함
- #49 P2-DOC-01: 최종 문서에 Actual/Control Cost, cleanup, Deferred 사유 기록
- #55 P2-REV-01: Project Close Review에서 Cost inventory와 threshold 준수 검토
- #57 MS-PROJECT-CLOSE-01: Cloud Resource/Cost 및 teardown 잔여를 Close 조건으로 확인

비용 정책은 P0 기능 범위를 확대하지 않는다. $400 경계는 P1을 자동 삭제하는 규칙이 아니라 **기본 Deferred 우선순위**다.

## 7. 검증 및 증적 원칙

최소 기록:

- 기준 시각(KST)
- AWS/ROSA Account/Project 식별 정보(Secret 제외)
- Actual/Gross spend
- 미반영/Projected 또는 계산한 잔여 비용
- 실행 중 유료 리소스 inventory
- Create/Destroy 시각
- cleanup 상태
- Hard Stop 발동 여부와 후속 Action

Billing screenshot 단독보다 원본 Cost/Resource export 또는 CLI/API 결과를 우선한다. Secret, 계정 토큰, Access Key는 증적에 포함하지 않는다.

## 8. 상태 구분

- POLICY DECISION: **APPROVED**
- ISSUE PUBLICATION: **NOT CREATED / HUMAN APPLY REQUIRED**
- CANDIDATE PR: **APPLIED**
- CLOUD RUNTIME: **NOT RUN**
- COST MEASUREMENT: **NOT RUN**
- REVIEW: **NOT DONE**
- MERGE/PUBLICATION: **NOT DONE**


## 9. 실제 GitHub 운영 반영

TICKET_SYNC_POLICY §5.1의 본문 직접 수정 금지를 준수하면서, 다음 관련 티켓에는 승인된 비용정책을 **Issue comment**로 실제 연결했다.

- #34 — [comment](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-5912002564)
- #35 — [comment](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5912005719)
- #38 — [comment](https://github.com/321Team/fds-project-baseline/issues/38#issuecomment-5912008823)
- #42 — [comment](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-5912013508)
- #49 — [comment](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-5912016585)
- #55 — [comment](https://github.com/321Team/fds-project-baseline/issues/55#issuecomment-5912019416)
- #57 — [comment](https://github.com/321Team/fds-project-baseline/issues/57#issuecomment-5912022066)

- 기존 Issue body/title/state/label은 이번 비용정책 반영으로 수정하지 않았다.
- Native `DEC-P2-COST-01` Issue는 아직 생성하지 않았다.
- 차기 정본에서 Decision record와 관련 ticket description을 재생성할 때 이 감사 기록과 코멘트를 입력으로 사용한다.


## 10. Cost-aware Test Strategy 연계

사용자 승인에 따라 비용정책의 실행 전략을 `P2-TEST-STRATEGY-01`로 연결한다.

- W0 PRECHECK: Local/CI/제공 OCP에서 유료 ROSA 반입 전 결함 제거
- W1 G4: D21/IaC/IAM-OIDC/VPN/Registry/Cost GO
- W2 G5: 실제 ROSA Platform→App→Runner Delivery
- W3 G6: 동일 ROSA에서 Hybrid→E2E→Failure/Recovery→Regression
- 10-23: Final Evidence/Cost/Resource Inventory 후 teardown 기본값
- $400 초과 예상: P1/선택 시험 Deferred-first
- $450 이상 예상: 신규 paid Runtime/Create/Recreate Hard Stop
- Full ROSA recreate: P0 필수 아님 / 조건부 P1

상세: `../phase2-test-strategy-20260930/README.md`

이 연계는 DEC-P2-COST-01의 $400/$450/$500 기준을 변경하지 않는다.
