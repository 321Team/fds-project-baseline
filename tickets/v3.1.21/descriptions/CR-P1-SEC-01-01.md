# CR-P1-SEC-01-01 — SEC-AC-05 예방 rotation을 P1 NOT MET/RISK ACCEPTED로 기록 (backup·rollback은 P1 유지)

Version: v3.1.21 CANDIDATE
Source: https://github.com/321Team/fds-project-baseline/issues/125
Updated at: 2026-10-02T03:14:53Z
Source body SHA256: `121db8d858d45eb006ad554e3cb6e0a433695beaa926c40255c503cd85a9ed19`
GitHub: closed / completed
Current disposition: CHANGE_STRUCTURE_ACCEPTED; backup/rollback P1 required; preventive rotation NOT MET / RISK ACCEPTED.

| Property | Current source value |
|---|---|
| Record ID | CR-P1-SEC-01-01 |
| Phase | Phase 1 |
| Category | Security / Acceptance Criteria |
| Type | Change Request |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-30 |
| End | 2026-10-02 |
| Calendar Days | 미기재 |
| Working Days | 미기재 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | #19 AC-05 처리 결정 기록(backup·rollback P1 유지, 예방 rotation `NOT MET / RISK ACCEPTED`)과 Review Owner 확인, #19 본문/후보 정본 구조 동기화. backup·rollback Runtime 증적은 #19 실행 잔여로 분리 |
| Related Decision IDs | D17; D18; D34; D-SEC-01 |
| Related Risk IDs | RISK-06; RISK-07; RISK-08 |
| Source | #19 P1-SEC-01 본문·코멘트; [Review Owner 딥리뷰](https://github.com/321Team/fds-project-baseline/issues/125#issuecomment-5912559914)·[재딥리뷰](https://github.com/321Team/fds-project-baseline/issues/125#issuecomment-5928029691); fds-project-evidence `evidence/P1-SEC-01/` |
| Schedule Note | 10-02(금)까지 Review 가능한 상태를 계획 목표로 한다. 코드·Runtime 정책 변경은 포함하지 않는다. |

## Source checklist

별도 checkbox 추출 없음. 아래 원문 Exit Criteria/계약을 따른다.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

<!-- cr-lifecycle-final-20261002:125:start -->
## 2026-10-02 Change Request 최종 Disposition

- **Disposition:** CHANGE_STRUCTURE_ACCEPTED
- **Effective AC change:** AC 축소 없음. backup·rollback=P1 필수, preventive rotation=P1 `NOT MET / RISK ACCEPTED`.
- **Canonical candidate:** v3.1.21 candidate intake 유효.
- **CR lifecycle:** 완료. 이후 backup·rollback Runtime 증적은 #19 SEC-AC-05 실행 잔여로 추적한다.
- **Dependency on #128 lifecycle:** 없음. #128 철회 후에도 #10 원문과 #19/#125 구조에서 P1 요구가 보존된다.
- **Boundary:** 이 CR 종료는 #19 AC-05 PASS, Runtime 완료, Release/Publication을 의미하지 않는다.
<!-- cr-lifecycle-final-20261002:125:end -->

<!-- issue-enhancement-20261001:v1:start -->
## 2026-10-01 Change Control 계약 고도화

### 현재 Review Gate
본 CR의 Change Structure는 **Review Owner 승인 완료**다. Runtime AC 완료 여부는 #19에서 별도 추적한다. 일정·업무부담을 이유로 미검증 요구를 삭제하지 않는다.

| 항목 | P1 기본 처리 | P2 이관 허용조건 |
|---|---|---|
| Secretbox 최초 encryption/3CP config | P1 유지 | 해당 없음 |
| backup | **P1 유지 / 원본 증적 필요** | 단순 이관 금지 |
| rollback | **P1 유지가 기본** | 실제 Receiver Record/Owner/Window/성공조건/#19 close dependency가 승인된 경우에만 재검토 |
| 예방 rotation | `NOT MET / RISK ACCEPTED` 가능 | 실제 P2 Receiver가 생성된 경우만 이관 |
| 노출 키/DB credential | P1 Residual Risk로 별도 명시 | 예방 rotation과 합쳐서 삭제 금지 |

### Cross-CR Guard
- #128의 Secret 항목과 반드시 하나의 Change Matrix로 대조한다.
- 요구가 #125→#128→P2로 연속 이동해 P1/P2 양쪽에서 사라지는 상태를 금지한다.
- P2 KMS v2 수신 티켓이 실제 존재하지 않으면 `승계 완료`로 표현하지 않는다.

### Close Condition
승인 전에 최소한 `Requirement / Current Owner / Proposed Owner / Receiver Record / Evidence / Status / #19 Close 영향`을 채운다. 미충족이면 10-06 Review에서 `NOT MET / Residual Risk`로 남긴다.
<!-- issue-enhancement-20261001:v1:end -->

# CR-P1-SEC-01-01 — SEC-AC-05 예방 rotation을 P1 `NOT MET / RISK ACCEPTED`로 기록 (backup·rollback은 P1 유지)

## 변경 이력

- 2026-10-01(개정): Review Owner 재딥리뷰(`DIRECTION=ACCEPTED / BODY=STALE_CONFLICT`)의 차단사항에 따라 본문을 최신 합의로 정정. **rollback의 P2 이관안을 철회하고 P1에 유지**, 예방 rotation은 P1에서 `NOT MET / RISK ACCEPTED`로 기록, P2 KMS v2는 실제 수신 Record가 생길 때만 후속으로 연결. 제목·변경 요청·영향·Exit Criteria를 모두 정정.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | CR-P1-SEC-01-01 |
| Phase | Phase 1 |
| Category | Security / Acceptance Criteria |
| Type | Change Request |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-30 |
| End | 2026-10-02 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | #19 AC-05 처리 결정 기록(backup·rollback P1 유지, 예방 rotation `NOT MET / RISK ACCEPTED`)과 Review Owner 확인, #19 본문/후보 정본 구조 동기화. backup·rollback Runtime 증적은 #19 실행 잔여로 분리 |
| Related Decision IDs | D17; D18; D34; D-SEC-01 |
| Related Risk IDs | RISK-06; RISK-07; RISK-08 |
| Source | #19 P1-SEC-01 본문·코멘트; [Review Owner 딥리뷰](https://github.com/321Team/fds-project-baseline/issues/125#issuecomment-5912559914)·[재딥리뷰](https://github.com/321Team/fds-project-baseline/issues/125#issuecomment-5928029691); fds-project-evidence `evidence/P1-SEC-01/` |
| Schedule Note | 10-02(금)까지 Review 가능한 상태를 계획 목표로 한다. 코드·Runtime 정책 변경은 포함하지 않는다. |

## 변경 요청

[#19](https://github.com/321Team/fds-project-baseline/issues/19) AC-05 `Secret encryption·backup·rotation·rollback PASS`는 **문구를 유지**하고, 항목별 P1 처리를 다음과 같이 기록한다. AC를 줄이지 않으며, 이 CR은 rotation을 PASS로 올리지 않는다.

| 항목 | P1 처리 | 상태 |
|---|---|---|
| Secret encryption·3CP 동일 Config·etcd 원문 비노출 | **P1 유지** | 증적 있음(`evidence/P1-SEC-01/received-20260924T081821Z/`, `received-20260926T034804Z/`) |
| backup | **P1 유지** | 원본 증적 **없음**(필요) |
| **rollback**(잘못된 암호화 구성 변경에서 되돌릴 수 있는지의 복구성 검증) | **P1 유지** (`ROLLBACK_P1_REQUIRED`) | 증적 **없음**(필요). 이관안 철회 |
| 예방 rotation(회전 스크립트 실행, 새 키 load/복호화) | P1에서 **`NOT MET / RISK ACCEPTED`** 로 기록. 실행하지 않는다 | Lead 수용(9/26 합의) |
| P2 KMS v2에서의 실제 key rotation·compromise 후 교체 시험 | **후속(조건부)**: 수신 Record ID·Owner·Window(W0~W3)·성공조건·Evidence path가 확정된 경우에만 연결. "P2 이관"을 완료 증빙으로 쓰지 않는다(`P2_RECEIVER_REQUIRED`) | **수신 Record 현재 없음(TBD)** |
| 노출된 키·DB 비밀번호(Gate2 중 CP shell history 노출) | **P1 Residual Risk로 별도 수용**(예방 rotation과 합쳐 삭제하지 않음) | 아래 변경 이유 4 |

## 변경 이유

1. **예방 rotation은 이미 P1에서 실행하지 않기로 합의됐다.** SEC Lead [결정](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5848034498)과 Review Owner [회신](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5846722659)(실행 스킵에는 이견 없음, `NOT MET / RISK ACCEPTED`). 이 CR은 그 기록 방식을 정리한다.
2. **rollback은 키 회전 기능이 아니다.** 잘못된 암호화 구성 변경에서 되돌릴 수 있다는 복구성 검증이므로 P1의 무결성·운영 복구 가치와 직접 연결된다. 따라서 rotation과 함께 P2로 보내지 않고 P1에 유지한다(Review Owner 의견 수용).
3. **미충족을 AC 삭제 근거로 쓰지 않는다.** "이 AC 때문에 티켓이 미충족으로 남는다"는 사실은 AC 축소 근거가 될 수 없다(Review Owner). rotation은 `NOT MET / RISK ACCEPTED`로 남기고 충족으로 올리지 않는다.
4. **노출된 키는 예방 rotation과 성격이 다르다.** 노출 통로는 CP shell history. 확인: control02/03 history 필터링·잔여 0건(2026-09-22 Gate2 기록), control01 `current_key_lines=0`·`enc_key_assign_lines=0`(`received-20260926T034804Z/40-control01-history-check.txt`, 병합). 키 자체를 바꾸지는 않았으므로 "노출 가능성이 남은 채 수용"임을 명시한다. DB 비밀번호는 담당자 진술로 회전 완료가 남아 있으나 시각·방법 증적은 없다.
5. **P2 승계를 확정으로 쓰지 않는다.** 실제 P2 KMS v2 수신 Record가 현재 확인되지 않으므로 `P2 승계`를 effective change로 기록하지 않는다.

## 남는 작업 (이 CR로 사라지지 않음)

- **backup 증적 1건:** encryption-config 백업(root-only 보관)과 복원 가능 확인. 현재 원본 없음.
- **rollback 검증 증적 1건:** 잘못된 암호화 구성 변경에서의 복구 절차 검증. 현재 원본 없음. (회전 스크립트는 [infra-kubernetes PR7](https://github.com/321Team/infra-kubernetes/pull/7)로 코드만 병합, 기존 B1~B4 잔여)
- **노출 건 잔여 리스크**를 #19 Residual Risk에 명시(승인자 이하영, 재검토 조건: P2 KMS v2 수신 Record 생성 또는 별도 CR).
- P2 수신 Record가 생길 때만 후속 연결. 생기기 전에는 `승계 완료`로 표현하지 않는다.

## Cross-CR 연결 — #128과의 통합 Change Matrix

요구가 #125 → #128 → P2로 연속 이동해 P1/P2 양쪽에서 사라지는 일을 막기 위해 [#128](https://github.com/321Team/fds-project-baseline/issues/128)과 하나의 Change Matrix에서 함께 승인한다.

| 요구 | 개정 전 | **개정 후(이 본문)** | #128 | 합성 결과 |
|---|---|---|---|---|
| Secretbox 최초 구성 | P1 | P1 유지 | #10은 '최초 구성 지원'으로 한정, 나머지는 #19 | P1 유지 |
| backup | P1(증적 필요) | P1 유지(증적 필요) | #19로 연결 | **P1 필수·미충족, 사라지지 않음** |
| rollback | P2로 이관안 | **P1 유지** | #19로 연결 | **P1 필수·미충족, 사라지지 않음** |
| 예방 rotation | P2로 이관안 | **P1 `NOT MET / RISK ACCEPTED`** | #19로 연결 | **P1 기록으로 남음**(미충족·수용). 사라지지 않음 |
| P2 KMS v2 실제 회전·교체 시험 | 승계 | 조건부 후속(수신 Record 없음) | 해당 없음 | 수신 Record 생성 전에는 승계 미표기 |
| 노출 키·DB 비밀번호 | 별도 수용 | P1 Residual Risk 유지 | 해당 없음 | 유지 |

합성 결과 P1 요구가 사라지는 항목이 없다. rotation은 미충족·수용으로 **P1에 기록**되고, backup·rollback은 P1 필수로 남는다.

## 영향

| 대상 | 영향 |
|---|---|
| #19 AC-05 | **문구 유지.** backup·rollback은 P1 증적 필요, rotation은 `NOT MET / RISK ACCEPTED`. AC-05 충족 처리 아님 |
| #19 핵심요구 7·Exit Criteria | rollback 항목 유지. 예방 rotation 항목만 `NOT MET / RISK ACCEPTED` 표기 |
| D-SEC-01 | "회전은 P2" 문구로 바꾸지 않는다. rotation `NOT MET / RISK ACCEPTED`와 정합하는 문구 여부는 **결정 필요(TBD)** |
| P2 KMS v2 | 실제 수신 Record 생성 시에만 후속 연결 |
| #128 | 통합 Change Matrix로 함께 승인 |
| 정본 | 승인되면 차기 정본 후보 Ticket Pack에 반영 |

## 이 CR이 하지 않는 것

- rotation을 PASS로 올리거나 #19 AC-05를 충족 처리하지 않는다.
- 다른 AC·핵심요구(PSA, HEP/GNP, RBAC can-i, Secret 암호화 최초 구성)를 바꾸지 않는다.
- Runtime·코드·정책을 변경하지 않는다.
- #19의 Status·AC 체크·Lead·일정을 바꾸지 않는다. **#19 본문은 이 개정본 승인 후 담당자가 별도로 바꾼다.**

## 확인 요청

- 결정: SEC Lead 이하영 (REVIEW_AUTHORITY_POLICY §4 — Decision/CR 검토는 해당 Lead)
- @GWONUK, @supreme33-kr — Review Owner: 개정본과 #128 통합 Change Matrix 확인

## Completion Record

- **Result:** CHANGE_STRUCTURE_ACCEPTED / CANONICAL_CANDIDATE_INTAKE_VALID / RUNTIME_AC_OPEN
- **Status:** Done
- **Completed Date:** 2026-10-02
- **Reviewer / Approver:** 이하영 (Lead / Change decision), 이권욱 (Review Owner)

