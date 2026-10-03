# CR-P1-HBR-01-01 — P1-HBR-01 종결 범위 조정 (OID-02 결정 이관·AC-05 05A/05B 분리)

Version: v3.1.21 CANDIDATE
Source: https://github.com/321Team/fds-project-baseline/issues/130
Updated at: 2026-10-03T02:14:15Z
Source body SHA256: `750e03a2e6aa28f6c5a2f9acad1b62b0a91a3b63e6de0e085461c6a6a5d5d93d`
GitHub: closed / completed
Current disposition: CHG01_CHG02_ACCEPTED; OID02 owner/receiver retained; #16 produces 4/4 and rollback, #13 retains 05B acceptance.

| Property | Current source value |
|---|---|
| Record ID | CR-P1-HBR-01-01 |
| Phase | Phase 1 |
| Category | Registry / Scope Change Control |
| Type | Change Request |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-30 |
| End | 2026-10-02 |
| Calendar Days | 미기재 |
| Working Days | 미기재 |
| Lead | 이하영 |
| Support | 이권욱 (#16 Lead — AC-05B 인수 구조 확인) |
| Exit Criteria | #13 핵심 요구/AC-05 구조 조정 결정 기록, #14의 OID-02 완료조건/Owner/Due 명시, #16 Lead의 4/4 Review Run 산출물 제공 확인, #13 본문 교체 |
| Related Decision IDs | D19; D-SEC-01; [2026-09-14 Robot 유한 30일 결정](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5659049448) |
| Related Risk IDs | 미기재 |
| Source | [#13 종합 대조 코멘트(2026-09-30)](https://github.com/321Team/fds-project-baseline/issues/13); [Review Owner 딥리뷰](https://github.com/321Team/fds-project-baseline/issues/130#issuecomment-5912569914)·[교차검토](https://github.com/321Team/fds-project-baseline/issues/130#issuecomment-5912873005) |
| Schedule Note | 미기재 |

## Source checklist

별도 checkbox 추출 없음. 아래 원문 Exit Criteria/계약을 따른다.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

# CR-P1-HBR-01-01 — P1-HBR-01 종결 범위 조정 (OID-02 결정 이관 · AC-05 05A/05B 분리)

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | CR-P1-HBR-01-01 |
| Phase | Phase 1 |
| Category | Registry / Scope Change Control |
| Type | Change Request |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-30 |
| End | 2026-10-02 |
| Lead | 이하영 |
| Support | 이권욱 (#16 Lead — AC-05B 인수 구조 확인) |
| Exit Criteria | #13 핵심 요구/AC-05 구조 조정 결정 기록, #14의 OID-02 완료조건/Owner/Due 명시, #16 Lead의 4/4 Review Run 산출물 제공 확인, #13 본문 교체 |
| Related Decision IDs | D19; D-SEC-01; [2026-09-14 Robot 유한 30일 결정](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5659049448) |
| Source | [#13 종합 대조 코멘트(2026-09-30)](https://github.com/321Team/fds-project-baseline/issues/13); [Review Owner 딥리뷰](https://github.com/321Team/fds-project-baseline/issues/130#issuecomment-5912569914)·[교차검토](https://github.com/321Team/fds-project-baseline/issues/130#issuecomment-5912873005) |
| Related | [#13 P1-HBR-01](https://github.com/321Team/fds-project-baseline/issues/13) · [#16 P1-CICD-01](https://github.com/321Team/fds-project-baseline/issues/16) · [#14 ICR-D-NET-01-01](https://github.com/321Team/fds-project-baseline/issues/14) · DEC-P1-IMG-01 |

## 변경 이력

- 2026-09-30 최초 제안: CHG-01(OID-02 이관), CHG-02(4/4 Digest·Rollback을 #16로 이관해 HBR 종결 조건에서 제외)
- 2026-09-30 Review Owner 판정: CHG-01 **조건부 수용**, CHG-02 **HOLD**(HBR의 end-to-end 인수 Gate 제거는 추적성을 약화)
- **2026-10-01 개정(이 본문):** Review Owner 권고를 반영해 CHG-02를 "제외"에서 "**05A/05B 분리, HBR 인수 Gate 유지**"로 변경하고, CHG-01에 수용 조건 3개를 명시. 4/4 인수를 HBR 종결 조건에서 **빼지 않는다.**

## 변경 요청

[#13](https://github.com/321Team/fds-project-baseline/issues/13)의 종결 조건 중 OID-02 결정 추적 위치와 AC-05의 구조를 명확히 합니다.

| # | 현재 (#13 문구) | 변경안 |
|---|---|---|
| CHG-01 | 핵심 요구 "OID-02를 P1-K8S Gate 1 전 결정" | HBR 요구를 "OID-02 결정 **입력** 제공(Harbor 측 Pull 가능성·경로 옵션·CA/Robot 영향)"으로 명확화. 결정 자체와 Gate 판정은 [#14](https://github.com/321Team/fds-project-baseline/issues/14)가 추적. 담당(이하영)·기한(K8S Gate 1 전) 불변. IF-10은 Worker만 허용, 결정 전 CP Source를 IF-10에 포함하지 않음. **수용 조건:** ① #14가 OID-02 결정의 완료조건/Owner/Due를 명시 ② HBR은 Harbor 입력을 제공 ③ OID-02 미결정을 HBR이 임의 PASS로 해석하지 않음 |
| CHG-02 | AC-05 "CI Scan Digest → Harbor Artifact → Manifest `image@sha256` → Pod `imageID` 4/4" 단일 항목 | AC-05를 **두 단계로 분리하되 HBR 종결 조건은 유지**한다. **HBR-AC-05A:** Harbor Scanner / Artifact / Credential fingerprint / Worker imageID 구간 PASS. **HBR-AC-05B:** #16이 생산한 **동일 Review Run 4/4 trace package를 HBR가 인수·대조**하고 회신. Rollback 실행 산출물은 #16이 생산하고, Harbor Artifact / Worker 재기동 구간 결과를 HBR가 인수. 생산 책임은 #16, **end-to-end 인수 Gate는 #13에 유지** |
| 부수 | "검증 및 증적" 목록의 `Rollback` | 제외하지 않는다. #16 생산, HBR 인수 구간(Harbor/Worker 재기동)을 #13 목록에 유지 |

## 변경 이유

1. CHG-01: HBR AC 6개에 OID-02 결정에 대응하는 항목이 없고 Scope는 "결정 **지원**"입니다. OID-02(CP/Calico/system image source)는 K8S Gate 항목이며 [#14](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5849779324)에서 `system_images.mode = BLOCKED / OID-02·03`으로 이미 추적 중입니다.
2. CHG-02: 6차 리뷰의 책임 분리(#16 생산 / #13 인수·검증 / 공동 4/4 대조)와 "#16 의존성은 착수 차단이 아니라 #13 완료 차단"이라는 기존 설계는 의도된 cross-ticket acceptance gate입니다. 따라서 4/4를 HBR 종결에서 제외하는 것은 정당화되지 않으며, **구조를 05A/05B로 명확히 나누어 HBR가 자기 구간(05A)은 독립적으로 진행하고 05B는 #16 산출물 도착 후 인수**하도록 정리합니다.
3. 비용·일정 최적화는 #16과 #13이 **같은 Review Run 증적을 공유**하는 방식(동일 Run 재실행 없음)으로 해결합니다.

## 정당성 검토

| 항목 | 판정 | 근거 |
|---|---|---|
| CHG-01 | 조건부 수용 | Review Owner 판정: 책임 분리 자연스러움. #14의 Decision 완료조건/Owner/Due 명시와 PASS 임의 승격 금지가 조건 |
| CHG-02 | **개정 반영 후 재검토 요청** | 기존 "제외"안은 HOLD. 개정안은 Review Owner 권고 구조(05A/05B, HBR 인수 Gate 유지)를 그대로 따름 |
| (제외) Robot 회전 | 변경하지 않음 | 9/14 결정이 인계/회전 검증을 구현·인수 항목으로 유지 |

## 영향

| 대상 | 영향 |
|---|---|
| 보안 | 통제 완화 없음 |
| #16 CICD | 4/4 산출물(CI Scan Digest / Manifest / Rollback)을 같은 Review Run으로 제공. 05B 인수 시점은 산출물 도착 후 |
| #14 K8S | OID-02 결정의 완료조건/Owner/Due를 #14에 명시. 결정 추적의 단일 창구 |
| G1 Milestone | #13 종결은 05B(#16 산출물)에 계속 의존. 단 05A는 독립 진행 |
| 병합된 증적 | 영향 없음 |
| 정본 | 승인 시 RELEASE_POLICY에 따라 차기 정본 후보에 반영(`P1-HBR-01` 핵심 요구·AC-05 문구) |

## 이 CR이 하지 않는 것

- 보안 통제를 완화하지 않습니다. TLS 검증 우회 금지, Worker Pull-only, Push DENY, 비승인 Source/CA/Credential DENY, 비밀정보 비노출은 유지합니다.
- **4/4 Digest 인수와 Rollback 인수를 #13 종결 조건에서 제외하지 않습니다.** 구조만 05A/05B로 명확히 합니다.
- 기존 PASS/증적을 소급 인정하지 않습니다. Runtime을 변경하지 않습니다. #13의 Scope·AC·Status는 결정 전까지 바꾸지 않습니다.
- 롤백: 승인 철회 시 #13 원문(SHA256 `8a5159fa6aecafdb1c61652bd0be2a234fa3b9792c53e910eeb39d6a17b400ff`)의 요구로 복귀합니다.

## 확인 요청

- 결정: HBR Lead 이하영 (REVIEW_AUTHORITY_POLICY §4 — Decision/CR 검토는 해당 Lead)
- @GWONUK — Review Owner / #16 Lead: 개정된 CHG-01 수용 조건과 CHG-02(05A/05B 분리, HBR 인수 Gate 유지)가 권고 구조와 일치하는지 재검토 부탁드립니다.

## 적용 절차

1. Lead 결정을 이 Issue 코멘트로 기록하고 Review Owner의 재검토 확인 1건을 받습니다.
2. 승인 후 #13 본문의 핵심 요구·AC-05를 05A/05B로 갱신합니다(원문 보존, 변경 이력 포함).
3. #14에 "OID-02 결정 입력 제공·결정 추적 — 담당 이하영, 기한 P1-K8S Gate 1 전, 완료조건"을 명시하고, #16에는 같은 Review Run 4/4 산출물 제공 및 HBR 인수·대조 회신 절차를 링크 코멘트로 남깁니다.
4. 증적 저장소 변경이 있으면 독립 리뷰 후 병합합니다.

## Completion Record

- **Result:** ACCEPTED — CHG-01 OID-02 책임경계 및 CHG-02 HBR-AC-05A/05B 구조 수용
- **Status:** Done
- **Completed Date:** 2026-10-03
- **Lead / Approver:** 이하영
- **Review Owner:** 이권욱
- **Applied Records:** #13 CR effective block / #14 OID-02 Decision Contract / #16 Producer Contract
- **Runtime Boundary:** Harbor Push/Deploy/4/4/Rollback Runtime은 이 CR의 완료조건이 아니라 #13/#16의 미완료 AC로 유지
