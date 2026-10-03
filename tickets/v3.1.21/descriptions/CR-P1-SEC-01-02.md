# CR-P1-SEC-01-02 — SEC-AC-02 Allow/Deny Matrix 범위를 소관 티켓 기준으로 정리

Version: v3.1.21 CANDIDATE
Source: https://github.com/321Team/fds-project-baseline/issues/126
Updated at: 2026-10-02T03:15:06Z
Source body SHA256: `81c6b48a5877fa7811d738224c668257fe0e2b720dc6e38a380f4b5d778c78a4`
GitHub: closed / not_planned
Current disposition: WITHDRAWN_NO_CHANGE

| Property | Current source value |
|---|---|
| Record ID | CR-P1-SEC-01-02 |
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
| Exit Criteria | #19 AC-02 범위 정리 결정 기록과 Review Owner 확인, 소관 티켓 AC 확인, #19 본문 AC 교체, 차기 정본 Ticket Pack 동기화 |
| Related Decision IDs | D17; D18; D34; D-SEC-01 |
| Related Risk IDs | RISK-06; RISK-07; RISK-08 |
| Source | #19 P1-SEC-01 본문·코멘트(2026-09-30 기준); FDS_Interface_Decision_CR_Register_v3.1.19; fds-project-evidence 병합본 |
| Schedule Note | 10-02(금)까지 Review 가능한 상태를 계획 목표로 한다. 코드·Runtime 정책 변경은 포함하지 않는다. |

## Source checklist

별도 checkbox 추출 없음. 아래 원문 Exit Criteria/계약을 따른다.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

<!-- cr-lifecycle-final-20261002:126:start -->
## 2026-10-02 Change Request 최종 Disposition

- **Disposition:** WITHDRAWN / NO CHANGE
- **Effective AC change:** 없음.
- **Original AC:** #19 SEC-AC-02 `Allow 흐름 PASS / Deny 흐름 FAIL` 원문 유지.
- **Evidence reuse:** 기존 병합 증적은 #19 판정에서 재사용하되 중복 Runtime은 요구하지 않는다.
- **Unmet flows:** 원 AC 기준 미충족은 `NOT MET / Known Issue`로 Close Review에 인계한다.
- **Aggregator proposal:** 철회됨. 별도 Matrix 변경을 정본에 반영하지 않는다.
<!-- cr-lifecycle-final-20261002:126:end -->

<!-- issue-enhancement-20261001:v1:start -->
## 2026-10-01 Interface Acceptance 계약 고도화

### 원칙
**Execution은 소관 티켓으로 분산할 수 있지만 SEC Acceptance 집계 책임은 제거하지 않는다.** 동일 Runtime/Evidence 재사용은 권장하되 Interface Register의 추적성은 유지한다.

### 필수 Aggregator Matrix
승인 전 각 Interface에 아래 필드를 채운다.

| 필드 | 요구 |
|---|---|
| Interface ID | IF-xx |
| Producer / Runtime Owner | 실제 시험 수행 티켓 |
| Acceptance Owner | 최종 판정 티켓 |
| Test Mode | RUNTIME / STATIC / POLICY / NOT-RUN-BY-DESIGN |
| Positive Evidence | PR/path/hash 또는 N/A 근거 |
| Negative Evidence | PR/path/hash 또는 위험상 미실행 근거 |
| Status | MET / NOT MET / RISK / DEFERRED |
| Close Dependency | #19 또는 소관 티켓 종결 영향 |

### 승인 Gate
- IF-09/10/13A/12C가 수신 티켓 AC에 실제 존재하는지 확인 전 이관 완료로 보지 않는다.
- 단순 링크만 있고 Acceptance Owner/Status가 없으면 #19/shared gate에 남긴다.
- #19 AC-02는 전체 Interface Register의 누락/상충 여부를 최종 집계한다.
<!-- issue-enhancement-20261001:v1:end -->

# CR-P1-SEC-01-02 — SEC-AC-02 Allow/Deny Matrix 범위를 소관 티켓 기준으로 정리

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | CR-P1-SEC-01-02 |
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
| Exit Criteria | #19 AC-02 범위 정리 결정 기록과 Review Owner 확인, 소관 티켓 AC 확인, #19 본문 AC 교체, 차기 정본 Ticket Pack 동기화 |
| Related Decision IDs | D17; D18; D34; D-SEC-01 |
| Related Risk IDs | RISK-06; RISK-07; RISK-08 |
| Source | #19 P1-SEC-01 본문·코멘트(2026-09-30 기준); FDS_Interface_Decision_CR_Register_v3.1.19; fds-project-evidence 병합본 |
| Schedule Note | 10-02(금)까지 Review 가능한 상태를 계획 목표로 한다. 코드·Runtime 정책 변경은 포함하지 않는다. |

## 변경 요청

[#19](https://github.com/321Team/fds-project-baseline/issues/19) AC-02 `Allow 흐름 PASS / Deny 흐름 FAIL`의 "전체 Matrix"를 Interface Register의 1차 소관 기준으로 정리합니다. 흐름을 버리는 것이 아니라 **어느 티켓이 판정하는지 정하는 것**입니다.

| 흐름 | Register 소관 | 이 CR의 처리 |
|---|---|---|
| Workload→Node 9100/10250 Deny, `.50/32→Worker:30080`, Prometheus↔Node 9100/10250, 앱 NetworkPolicy, CP GNP 10250 | P1-SEC-01 | #19에서 판정 (증적 병합) |
| IF-12A CP↔etcd 2379/2380 | P1-K8S-01 / ICR / P1-SEC-01 | 기존 병합 증적을 #19에 연결해 판정. 아래 근거 참조 |
| IF-12B CP→Node:10250 | 동일 | 위와 동일(CP→Node OK와 workload-deny 8/8) |
| IF-12C VXLAN 4789 | P1-K8S-01 / ICR | P1-K8S-01(#10) 판정. 소관 티켓 증적 확인 필요 |
| IF-05/05A/05B/05C | P1-MON-01 / P1-SEC-01 | P1-MON-01(#17) Runtime 검증 범위(#17 본문에 IF-05~06B Runtime 검증 명시)에서 판정 |
| IF-09 | P1-HBR-01 / P1-CICD-01 | 해당 티켓에서 판정 |
| IF-10 | P1-HBR-01 / P1-K8S-01 | 해당 티켓에서 판정 |
| IF-13A | P1-K8S-01 / P1-SEC-01 / P1-APP-01 / P1-MON-01 | P1-K8S-01(#10)이 1차 |

## 변경 이유

1. **Negative 시험의 위험은 "승인 경로를 끊는 방식"에 한정됩니다.** [코멘트 #46](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5848266155)이 금지한 것은 etcd·kubelet-control·VXLAN을 실제로 끊는 시험입니다. 비승인 Source에서 접근해 막히는지 보는 시험은 안전하며, Register의 IF-12A 기준("비승인 Source DENY")도 이를 요구합니다.
2. **IF-12A의 Positive·Deny는 이미 병합된 증적에 있습니다.** evidence `P1-K8S-01/cp-reboot-20260927`(evidence#55)의 `reboot-cp02-after.txt` 정책 매트릭스: CP→`.103:2379/2380` OK, Worker 3대→`.103:2379/2380` TIMEOUT. CP 3대 재부팅 전후 매트릭스 20칸 바이트 동일. 다만 이 README는 "독립 검토 미완료"라고 적혀 있어 판정 사용은 Review Owner 확인이 필요합니다.
3. **Register상 IF-12A/B/C의 1차 소관은 P1-K8S-01입니다.** #19 AC가 이를 다시 요구하면 같은 흐름이 두 티켓의 AC에 이중으로 걸립니다.
4. **나머지 흐름은 각 1차 소관 티켓에 이미 검증 책임이 있습니다.** 다만 아래 "남는 작업"의 확인 전에는 이관을 확정하지 않습니다(`.50→30080`이 세 티켓 모두 Out of Scope로 남았던 공백 재발 방지).
5. **소관 흐름의 증적은 병합돼 있습니다.** evidence#49(workload-deny 재시험 8/8, 첫 회차 4 FAIL 이력 포함), evidence#54(CP GNP·Service after), evidence#79(MON NetworkPolicy 양성·음성), Gate2 네트워크 [9/9 보고](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5772355948).

## 남는 작업 (승인 전에 확인)

- IF-09/10/13A·IF-12C: 1차 소관 티켓(#13 HBR, #16 CICD, #10 K8S)의 AC에 해당 흐름이 실제로 있는지 확인. 없으면 그 티켓에 추가하거나 이 CR에서 해당 흐름을 #19에 남깁니다. IF-05 계열은 #17 본문에서 확인했습니다.
- evidence#55 원본과 IF-12A의 판정 연결에 대한 Review Owner 확인.

## 영향

| 대상 | 영향 |
|---|---|
| #19 AC-02 | 판정 대상이 위 표의 "#19에서 판정" + IF-12A/B 연결로 고정됨 |
| 소관 티켓 | IF-12C·05·09·10·13A의 판정이 해당 티켓 AC로 명시됨 |
| D-SEC-01 Interface Register | NOT TESTED 항목의 판정 티켓 표기 |
| 정본 | 승인되면 차기 정본 후보에 반영 |

## 이 CR이 하지 않는 것

- 다른 AC·핵심요구사항을 바꾸지 않습니다. PSA, HEP/GNP, RBAC can-i, Secret 암호화 최초 구성은 유지합니다.
- Runtime·코드·정책을 변경하지 않습니다.
- #19의 Status·AC 체크·Lead·일정을 이 CR로 바꾸지 않습니다. 결정 후 #19 본문 반영은 담당자가 별도로 합니다.

## 확인 요청

- 결정: SEC Lead 이하영 (REVIEW_AUTHORITY_POLICY §4 — Decision/CR 검토는 해당 Lead)
- @GWONUK, @supreme33-kr — Review Owner: 변경안과 위 "남는 작업" 확인

## Completion Record

- **Result:** WITHDRAWN_NO_CHANGE / ORIGINAL_AC_RETAINED
- **Status:** Done
- **Completed Date:** 2026-10-02
- **Reviewer / Approver:** 이하영 (Lead disposition), 이권욱 (Review Owner confirmation)

