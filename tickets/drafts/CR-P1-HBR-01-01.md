# CR-P1-HBR-01-01 — P1-HBR-01 종결 범위 조정 (핵심 요구 2건 이관·축소)

> PROPOSED / APPROVAL PENDING · 2026-09-30 KST · GitHub Issue 미생성(PR로 제안). 승인 전에는 P1-HBR-01의 Scope·AC·Status를 변경하지 않는다.

## 속성 (Issue 등록 시 사용)

| Property | 입력값 |
|---|---|
| Record ID | CR-P1-HBR-01-01 (번호는 등록 시 확정) |
| Phase | Phase 1 |
| Category | Registry / Scope Change Control |
| Type | Change Request (`type:change-request`) |
| Status | Proposed / Approval Pending |
| Priority | P0 (P1-HBR-01 종결의 선행 조건) |
| Lead | 이하영 (P1-HBR-01 Lead) |
| Support | 이권욱 (#16 Lead — CHG-02 인수 확인) |
| Target Ticket | [P1-HBR-01 #13](https://github.com/321Team/fds-project-baseline/issues/13) |
| Related | [#16 P1-CICD-01](https://github.com/321Team/fds-project-baseline/issues/16) · [#14 ICR-D-NET-01-01](https://github.com/321Team/fds-project-baseline/issues/14) · [#19 P1-SEC-01](https://github.com/321Team/fds-project-baseline/issues/19) · DEC-P1-IMG-01 |
| Related Decision IDs | D19; D-SEC-01; 2026-09-14 Robot 유한 30일 결정 ([코멘트](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5659049448)) |
| Approval | REVIEW_AUTHORITY_POLICY §1 — 코드 외 절차는 Lead 결정. 단 증적 저장소 PR은 독립 리뷰 유지 |

## 1. 변경 배경

#13의 종결 조건 중 두 가지는 HBR이 단독으로 충족할 수 없어, 다른 책임 티켓의 산출물을 기다리는 구조가 되었다. 나머지 요구사항의 Runtime 증적은 [fds-project-evidence PR #64](https://github.com/321Team/fds-project-evidence/pull/64)(OPEN)에 있으며 이 CR의 대상이 아니다.

- 이 CR은 **보안 통제를 완화하지 않는다.** TLS 검증 우회 금지, Worker Pull-only, Push DENY, 비승인 Source/CA/Credential DENY, 비밀정보 비노출은 그대로 유지한다.
- 이 CR은 기존 PASS/증적을 소급 인정하지 않는다. 승인 전 #13은 PASS 0 / NOT VERIFIED 상태가 유지된다.

## 1-1. 정당성 검토 결과

| 항목 | 판정 | 근거 |
|---|---|---|
| CHG-01 | 정당 | AC에 대응 항목 없음, Scope는 "결정 지원", #14가 이미 BLOCKED로 추적. 담당(이하영)·기한(K8S Gate 1 전) 불변 |
| CHG-02 | 조건부 정당 | CI Scan Digest 생산은 9/14 결정상 #16 담당. #16 Lead(이권욱)의 인수 확인 후 효력 |
| (제외) Robot 회전 | 변경하지 않음 | 9/14 결정이 인계/회전 검증을 구현·인수 항목으로 유지하고 credential 증적을 면제하지 않음. 기존 요구 유지 |

## 2. 변경 항목

### CHG-01 — OID-02 결정 요구를 HBR 핵심 요구에서 제외하고 #14로 이관

| 항목 | 내용 |
|---|---|
| 현행 | 핵심 요구 "OID-02를 P1-K8S Gate 1 전 결정" |
| 문제 | HBR AC 6개에 대응 항목이 없다. Scope는 "결정 **지원**"이다. OID-02(CP/Calico/system image source)는 K8S 게이트 항목이며 [#14](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5849779324)에서 `system_images.mode = BLOCKED / OID-02·03`으로 추적 중이다. |
| 변경 | HBR 요구를 "OID-02 결정 입력(Harbor 측 Pull 가능 여부·경로 옵션) 제공"으로 축소한다. 결정 자체와 Gate 판정은 #14가 추적한다. |
| 유지 | IF-10은 Worker만 허용. 결정 전 CP Source를 IF-10에 포함하지 않는다. |
| 종결 근거 | Harbor 측 옵션 제시 기록 1건(코멘트 링크). 결정 완료는 요구하지 않는다. |
| 병합된 증적 영향 | 없음 (evidence `main`에 OID-02 증적 없음) |

### CHG-02 — 4/4 Digest Traceability를 HBR AC에서 분리, Harbor 구간(3구간)으로 축소

| 항목 | 내용 |
|---|---|
| 현행 | 핵심 요구 "Trivy 결과와 배포 Digest 일치", AC "Image Digest·Scan 결과·Credential fingerprint Evidence 확보"(AC-05: CI Scan Digest → Harbor Artifact → Manifest `image@sha256` → Pod `imageID` 4/4) |
| 문제 | 첫 값(CI Scan Digest)은 #16이 생산한다. Run #5는 성공했으나 Push/Deploy가 NOT_EXECUTED이고 Run #5 증적은 [evidence PR #70](https://github.com/321Team/fds-project-evidence/pull/70)이 OPEN이다. HBR이 타 티켓 산출물 때문에 종결하지 못한다. |
| 변경 | HBR 인수 범위를 **Harbor 소유 구간**으로 한정한다: ① Harbor Artifact Digest ↔ Pod `imageID`(Worker 3대) ② Harbor Trivy Scanner 정상 동작 및 Harbor 스캔 결과 ③ Credential fingerprint. 4/4 전체 trace와 Rollback(이전 승인 Digest 복구)은 #16 / DEC-P1-IMG-01에서 종결한다. |
| 유지 | 2-way `LOCAL_DIGEST ↔ HARBOR_DIGEST`는 AC-05를 대체하지 않는다는 기존 원칙. HBR은 #16 산출물을 인수·검증하는 책임(기존 6차 리뷰 책임 경계)을 유지하되 종결 조건에서는 제외한다. |
| 효력 조건 | #16 Lead(이권욱)가 4/4 trace·Rollback 종결 책임 인수를 코멘트로 확인한 뒤 효력. 9/14 결정("4/4 추적에 연결")과 충돌하지 않도록 HBR은 Harbor 측 digest 대조·#16 산출물 인수 검증 책임을 유지한다: #16이 Scan/Manifest Digest 산출물을 제공하면 HBR Lead가 Harbor 측 값을 1회 대조해 #16에 코멘트로 회신한다(종결 조건은 아님). |
| 종결 근거 | 증적 PR #64 병합 + `PUSHED_DIGEST`가 manifest digest임을 확인(README가 config digest 가능성을 경고). |
| 병합된 증적 영향 | 없음 (HBR 증적은 PR #64 미병합. #16 증적은 그대로 #16 소관) |

### 부수 정리 — 본문 증적 목록에서 Rollback 제거

"검증 및 증적"의 `Rollback`은 CHG-02에 따라 #16 소관이므로 #13 목록에서 제외한다. Retention/GC는 기존대로 Optional / Non-blocking 유지.

## 3. 변경하지 않는 항목 (종결 조건으로 유지)

Robot 권한·회전·Secret 저장 경계(`robot$fds-ci` 60일 TTL·monitoring `admin` Secret 처리 포함) / TLS 1.2+·SAN·Chain / Runner `.20` 인증 Push·Pull / Worker 3대 Pull·Pod Start·Push DENY / 잘못된 CA·Credential·비승인 Source DENY / 실제 Source IP와 Host Firewall 일치(AC-04: 현재 `ACTUAL_SOURCE=NOT_VERIFIED`) / 비밀정보 평문 미포함.

## 4. 영향 분석

| 영역 | 영향 |
|---|---|
| 보안 | 통제 완화 없음. Robot 요구 전체 유지 |
| #16 CICD | 4/4 trace·Rollback 종결 책임이 명시적으로 #16으로 확정됨. Support 확인 필요 |
| #14 K8S | OID-02 결정 추적이 #14 단일 창구가 됨 |
| G1 Milestone | HBR 종결이 #16 산출물에 종속되지 않음 |
| 정본 | 승인 시 RELEASE_POLICY에 따라 다음 정본 후보에 동기화 (`P1-HBR-01` 핵심 요구·AC-05 문구) |

## 5. 승인 및 적용 절차

1. Lead(이하영) 승인 결정을 이 Issue 코멘트로 기록. #16 Lead(이권욱)의 CHG-02 인수 확인 1건.
2. 승인 후 #13 본문의 핵심 요구·AC-05·증적 목록을 변경 이력과 함께 갱신(원문 보존).
3. #14에 "OID-02 결정 입력 제공·결정 추적 — 담당 이하영, 기한 P1-K8S Gate 1 전"을 명시하고, #16에는 4/4 trace·Rollback 종결 및 HBR 대조 회신 절차를 링크 코멘트로 남긴다.
4. 증적 저장소 변경이 있으면 독립 리뷰 후 병합.

## 6. 롤백

승인 철회 시 #13 원문(SHA256 `8a5159fa6aecafdb1c61652bd0be2a234fa3b9792c53e910eeb39d6a17b400ff`)의 요구사항으로 복귀한다. 이 CR은 Runtime 변경을 포함하지 않는다.

## 7. 근거

- [#13 종합 대조 (2026-09-30)](https://github.com/321Team/fds-project-baseline/issues/13) 코멘트 전체
- [evidence PR #64](https://github.com/321Team/fds-project-evidence/pull/64) / [PR #70](https://github.com/321Team/fds-project-evidence/pull/70) — 둘 다 2026-09-30 조회 시점 OPEN
- [REVIEW_AUTHORITY_POLICY](../../governance/REVIEW_AUTHORITY_POLICY.md)
