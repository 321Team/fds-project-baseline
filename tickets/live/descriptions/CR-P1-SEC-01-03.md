<!-- fds-canonical-live:v3.1.21 record-id:CR-P1-SEC-01-03:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/CR-P1-SEC-01-03.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 해당 업무의 기존 AC·Exit Criteria와 실행/인수 구분을 유지한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:CR-P1-SEC-01-03:end -->

<!-- cr-lifecycle-final-20261002:127:start -->
## 2026-10-02 Change Request 최종 Disposition

- **Disposition:** REJECTED / NO CHANGE / OPTION A RETAINED
- **Effective AC change:** 없음.
- **Original AC:** B2 source-preservation은 SEC-AC-04/핵심요구4의 필수 하위조건으로 유지.
- **Accepted evidence:** clean immutable evidence #86은 Positive source-preservation 근거.
- **Boundary:** 비승인 Source Negative, evidence #58 claim 정리, Edge Cutover 및 SEC 전체 완료는 별도 잔여.
- **Canonical handling:** 변경 거절/기존 기준 유지 이력만 후보 정본에 남긴다.
<!-- cr-lifecycle-final-20261002:127:end -->

<!-- issue-enhancement-20261001:v1:start -->
## 2026-10-01 AC-04 종결 계약 고도화

### 현재 Review Gate
Review Owner 최신 판정은 **`BLOCK / AC_INTEGRITY_RISK`**다. 현재 기준에서는 선택 B를 승인안으로 간주하지 않으며, source-preservation은 AC-04 또는 이를 직접 차단하는 mandatory child gate에 남긴다.

### Required Path
1. infra-ansible #60 clean-rerun collector의 exact HEAD/CI/merge 확인
2. 복구 후 현재 형상에서 B2 source-preservation 재수집
3. `.50/32 → Worker:30080` 실제 L3 source identity와 allow/deny 결과 연결
4. evidence 독립 리뷰
5. #19 AC-04 판정

### Stop / Evidence Rule
- artifact quota, provenance 지연, 수집 편의성은 AC 제거 근거가 아니다.
- 비승인 Source Negative는 **현재 복구 후 형상**에서 확보해야 한다.
- tcpdump/collector 결과는 원본 PCAP/텍스트, host/time/interface/filter/RC/hash가 추적 가능해야 한다.

### Close
10-06까지 미완료여도 AC를 삭제하지 않고 `NOT MET / Known Issue`로 Close Review에 올린다. Edge cutover 역시 해당 gate가 해소되기 전 PASS로 올리지 않는다.
<!-- issue-enhancement-20261001:v1:end -->

# CR-P1-SEC-01-03 — B2 source-preservation(#63)의 AC-04 필수 여부 결정 요청

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | CR-P1-SEC-01-03 |
| Phase | Phase 1 |
| Category | Security / Acceptance Criteria |
| Type | Change Request |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-30 |
| End | 2026-10-02 |
| Calendar Days | 3 |
| Working Days | 3 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | Review Owner의 A/B 결정 기록, #19 AC-04·핵심요구 4 판정 범위 확정, 남는 작업 3건 완료 또는 이관, 차기 정본 Ticket Pack 동기화 |
| Related Decision IDs | D17; D18; D34; D-SEC-01 |
| Related Risk IDs | RISK-06; RISK-07; RISK-08 |
| Source | #19 P1-SEC-01 본문·코멘트(2026-09-30 기준); fds-project-evidence 병합본 evidence/P1-SEC-01/, evidence/P1-HA-01/; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 10-02(금)까지 Review 가능한 상태를 계획 목표로 한다. 코드·Runtime 정책 변경은 포함하지 않는다. |

## 결정 요청

[#19](https://github.com/321Team/fds-project-baseline/issues/19) AC-04와 핵심요구 4(`.50/32→Worker:30080`만 preDNAT 허용)의 판정에 다음을 **필수로 포함할지** Review Owner의 결정을 요청합니다.

- evidence#63 tcpdump L3 source-preservation과 `infra-ansible#60` 이후 clean immutable B2 재수집

| 선택 | 내용 |
|---|---|
| A | 필수 유지. #60 CI 성공 → merge → 재수집 → 독립 리뷰를 거쳐야 AC-04 종결 |
| **B (권장)** | SEC AC 판정과 분리하고 D18·edge cutover Gate에서만 관리. AC-04는 아래 "판정 근거"로 종결 |

## 이 요청의 근거 — 그리고 기존 결정과의 관계

- [Review Owner #79](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5863858466)는 tcpdump 방식을 "**AC 완화가 아니라 증적 수단 대체**"로 수용했습니다. 즉 현재는 AC 증적으로 취급합니다. B는 이 결정을 바꾸는 것이므로 Review Owner의 명시적 결정이 필요합니다.
- [#83](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5883374181)은 edge upstream 이관의 선행조건을 SEC 전체 잔여로 넓히지 말라는 내용입니다. 이 CR의 근거가 아니며, edge cutover Gate(`EDGE_CUTOVER=HOLD`, #63/#60 경로)는 이 CR과 무관하게 그대로 유지합니다.
- B를 권하는 이유: (1) AC 본문은 `.50/32` preDNAT Allow/Deny까지이고 source-preservation은 D18 항목입니다. (2) #63 차단 원인은 collector 한 줄 수정의 provenance이고 재수집은 GitHub artifact quota로 막혀 있어([#88](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5902810972), [#90](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5911391929)) 보안 통제와 무관한 인프라 지연입니다.

## 판정 근거 (B 선택 시)

- Positive: `P1-HA-01`(evidence#57, 병합) — edge01→Worker `.105/.107/.108` `:30080/readyz` 200, 최종 Service 형상(2026-09-27 19:13 KST Final E2E). evidence#58(edge01 CONNECTED)은 OPEN·CHANGES_REQUESTED 상태.
- Deny: GNP `nodeport-30080-allow` spec(병합, `received-20260926T034804Z/20-gnp-nodeport-30080-allow.yaml`).
- 32085: 최종 Service spec으로 listener 부재 확인 — evidence#54 `b2-svc-after.yaml`(병합), Review Owner [#64](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5854584683)가 이 방식을 인정.

## 남는 작업 (A/B 어느 쪽이든 필요)

1. **비승인 Source → 30080 Negative 원본 연결.** 현재는 코멘트뿐이고, 그것도 Service 복구 전 형상에서 수행한 결과입니다. [#83](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5883374181) 4번이 요구합니다. 복구 후 형상에서 1회 재수집해 evidence에 편입합니다.
2. **evidence#58 병합.** CHANGES_REQUESTED 해소 필요.
3. **P1-HA-01(evidence#57)이 판정에 쓰일 수 있는지 Review Owner 확인.** 이 README는 "edge는 `/readyz`로 정상 Worker를 고른다"는 가정의 모사이며 업무 API 연속 요청은 하지 않았다고 명시합니다.

## 영향

| 대상 | 영향 |
|---|---|
| #19 AC-04·핵심요구 4 | B 선택 시 source-preservation 제외, 위 근거·남는 작업으로 판정 |
| edge01 upstream 이관 | 영향 없음. HOLD와 Gate 유지 |
| evidence#63 / infra-ansible#60 | B 선택 시 SEC AC와 별개 트랙(D18·edge cutover) |

## 이 CR이 하지 않는 것

- 다른 AC·핵심요구사항을 바꾸지 않습니다. PSA, HEP/GNP, RBAC can-i, Secret 암호화 최초 구성은 유지합니다.
- Runtime·코드·정책을 변경하지 않습니다.
- #19의 Status·AC 체크·Lead·일정을 이 CR로 바꾸지 않습니다. 결정 후 #19 본문 반영은 담당자가 별도로 합니다.

## 확인 요청

- 결정: SEC Lead 이하영 (REVIEW_AUTHORITY_POLICY §4 — Decision/CR 검토는 해당 Lead)
- @GWONUK, @supreme33-kr — Review Owner: A/B 결정과 위 "남는 작업" 확인

## Completion Record

- **Result:** REJECTED_NO_CHANGE / OPTION_A_RETAINED
- **Status:** Done
- **Completed Date:** 2026-10-02
- **Reviewer / Approver:** 이하영 (Lead disposition), 이권욱 (Review Owner confirmation)
