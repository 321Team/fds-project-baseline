# Project Schedule Replan — 2026-09-30 KST

## 1. 확정 입력

- **Project Close:** 2026-10-26(월) — 사용자 확정, 자동 연장 금지
- **Non-working:** 2026-10-05(월), 2026-10-09(금), 모든 토·일
- **Phase 1 Review / Close:** 2026-10-06(화)
- **Phase 2 Start:** 2026-10-07(수)
- Phase 2 사용 가능 작업일(10-07~10-26): **13일**
- 프로젝트 가치: 재현성 · 무결성 · 추적성
- 기존 P0/P1 재분류 및 P1 non-blocking 원칙 유지

2026-10-09는 한글날 법정공휴일이며, 10-05는 사용자 확정 비근무일로 프로젝트 캘린더에 반영한다. 공휴일/주말을 Working Days에서 제외한다.

## 2. Phase 1 마감 재배치

10-05 비근무로 인해 10-06 Review/Close 직전 작업일은 10-02(금)이다.

| Issue | 기존 | 변경 | Working | 의미 |
|---:|---|---|---:|---|
| #20 P1-E2E-01 | End 09-22 | **End 10-02** | 누적 16일 | 최종 회귀/증적 cutoff |
| #21 P1-DR-01 | End 09-21 | **End 10-02** | 누적 16일 | Restore 후 E2E/Runbook cutoff |
| #22 P1-HA-01 | End 09-21 | **End 10-02** | 누적 16일 | 잔여 HA 판정 cutoff |
| #24 P1-DOC-01 | End 09-22 | **End 10-02** | 누적 16일 | Review package freeze |
| #29 G3 | 09-22 | **10-02** | 1 | Review Ready |
| #119 APP CR | End TBD | **End 10-02** | 4 | AC 정정 Review cutoff |
| #31 Phase 1 Review | 10-06 | **유지** | 1 | Review |
| #30 Phase 1 Close Execution | 10-06 | **유지** | 1 | 보완/Sign-off |
| #32 Phase 1 Close | 10-06 | **유지** | 1 | Phase 1 종료 |

10-06에는 신규 대규모 구현을 배정하지 않는다. 10-02까지 미완료인 항목은 미검증을 PASS 처리하지 않고 Review에서 Known Issue/잔여 Action으로 판정한다.

## 3. Phase 2 P0 재계획

| Issue | 변경 일정 | Working Days | 비고 |
|---:|---|---:|---|
| #33 Phase 2 Start | **10-07** | 1 | Phase 1 Close 다음 작업일 |
| #34 Architecture Freeze | **10-07** | 1 | P0/P1·ROSA topology 동결 |
| #35 AWS/ROSA IaC | **10-07~10-14** | 5 | 10-09/주말 제외 |
| #36 OCI Go/No-Go | **10-07~10-08** | 2 | D21을 휴일 전 확정 |
| #37 VPN | **10-12~10-14** | 3 | D21 후 10-09/주말 건너뜀 |
| #39 G4 | **10-14** | 1 | IaC/VPN Runtime Gate |
| #38 ROSA Platform | **10-12~10-19** | 6 | VPN과 병행 가능한 platform 작업 포함 |
| #42 Registry Decision | **10-12~10-16** | 5 | P0 D22 |
| #43 App | **10-15~10-19** | 3 | ROSA/D22 소비 |
| #46 CI/CD | **10-19~10-20** | 2 | 일요일 10-18 제거 |
| #45 G5 | **10-20** | 1 | ROSA/App/CI Gate |
| #47 Hybrid Integration | **10-20~10-22** | 3 | DB/Registry |
| #50 E2E | **10-21~10-22** | 2 | final acceptance는 #47 승인상태 전제 |
| #53 G6 | **10-22** | 1 | Hybrid/E2E Gate |
| #49 Deliverable preparation | **10-19~10-23** | 5 | 실행과 병행해 as-built/evidence 정리 |
| #52 Review Schedule Decision | **10-22** | 1 | Review 10-23 고정 |
| #54 Deliverable Freeze | **10-23** | 1 | 신규 Scope 금지 |
| #56 Phase 2 Review | **10-23** | 1 | 금요일 |
| #55 Review/Close Execution | **10-23~10-26** | 2 | 10-24~25 주말 제외 |
| #57 Project Close | **10-26** | 1 | 확정 종료일 |

### Critical path

```text
10/06 Phase 1 Close
  ↓
10/07 P2 Start + Architecture
  ↓
10/07~14 IaC
10/07~08 D21
  ↓
10/12~14 VPN
  ↓
10/14 G4
  ↓
10/12~19 ROSA
10/12~16 Registry
  ↓
10/15~19 App
  ↓
10/19~20 CI/CD
  ↓
10/20 G5
  ↓
10/20~22 Hybrid
10/21~22 E2E
  ↓
10/22 G6
  ↓
10/23 Freeze + Review
  ↓
10/26 Project Close
```

## 4. P1 일정 보호

P1은 고정 구현일을 최소화한다.

### Decision only

- #40 Hybrid DNS Decision: **10-15~10-16 / 2일**
- #41 Operator Supply Chain Decision: **10-15~10-16 / 2일**
- #120 GitOps Decision: **10-15~10-16 / 2일**
- #121 Compliance Decision: **10-15~10-16 / 2일**

10-16까지 미결정이면 P0를 막지 않고 Deferred 처리한다.

### 구현일 미배정

- #25 Monitoring Enhancement
- #26 DR Enhancement
- #27 Resilience P1
- #44 OADP
- #48 Hybrid DNS implementation
- #51 Operator mirror implementation
- #95 RHOAI

P0 잔여 capacity가 있을 때만 착수한다. 10-26 이전 완료를 강제하지 않고 미착수 시 Deferred/N/A/Cancelled/Known Issue로 Close한다.

## 5. 일정 검수 결론

### 해소한 오류

1. 10-18(일)에 잡혀 있던 G5 / CI-CD / Hybrid start 제거
2. 10-11(일) ROSA start 제거
3. 10-09 공휴일을 Working Day에서 제외
4. 10-05 비근무 때문에 Phase 1 Review 전 실제 작업 cutoff를 10-02로 이동
5. Phase 1 Close와 Phase 2 Start가 같은 10-06이던 충돌을 해소
6. 10-26 Project Close를 확정값으로 고정
7. P1 구현이 P0 작업창을 잠식하지 않도록 고정 구현일 해제

### 남은 위험

- 10-07~10-26 Phase 2 실작업일은 13일뿐이다.
- #38/#43/#46이 10-20 G5의 핵심 압축구간이다.
- #47/#50은 10-22 G6 직전 3일에 집중된다.
- 따라서 새 P1 기능을 P0로 승격하거나 ROSA provisioning 지연이 발생하면 일정 여유가 거의 없다.
- 일정 보호를 위해 각 담당자 핵심 P0 WIP 1개 원칙을 유지한다.

## 6. 정본/WBS 동기화

**실제 Issue 일정:** 반영 완료.

**Draft PR #112:** 이 감사표와 machine-readable schedule을 정본 후보 입력으로 포함.

**후보 XLSX:** 기존 `audit/canonical-candidate-20260927/proposed/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx`는 이번 일정 변경 전 생성본이므로 **STALE / 재생성 대상**으로 취급한다. 바이너리 셀을 부분 패치해 Source와 Workbook이 갈라지게 하지 않고, 최신 Issue를 Source로 전체 WBS 재생성 시 반영한다.

정식 v3.1.21 발행 전에는 WBS/Baseline/Ticket Pack/Description/Manifest/SHA256SUMS/ZIP/WEB을 동일 일정 기준으로 다시 생성한다.
