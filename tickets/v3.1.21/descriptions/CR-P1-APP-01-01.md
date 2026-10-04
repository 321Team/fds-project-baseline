# CR-P1-APP-01-01 — P1-APP-01 AC "DB/FDS 장애 시 /readyz 503" 문구 정정 — fds-engine fail-open 정합

Version: v3.1.21 CANDIDATE
Source: https://github.com/321Team/fds-project-baseline/issues/119
Updated at: 2026-10-01T12:11:06Z
Source body SHA256: `a5bd9c28dc6b26ee7187c20f760e31d2a675a3d52b853f6aadf6bb48afd17870`
GitHub: closed / completed
Current disposition: AC wording correction accepted / Done. DB outage readiness and engine failure fail-open separated.

| Property | Current source value |
|---|---|
| Record ID | CR-P1-APP-01-01 |
| Phase | Phase 1 |
| Category | Application / Acceptance Criteria |
| Type | Change Request |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-29 |
| End | 2026-10-02 |
| Calendar Days | 4 |
| Working Days | 4 |
| Lead | 이재환 |
| Support | 이하영 |
| Exit Criteria | #15 AC 문구 정정 결정 기록과 Review Owner·G3 확인, #15 본문 AC 교체, FDS 장애 fail-open Runtime 증적, 차기 정본 Ticket Pack 동기화 |
| Related Decision IDs | D18; D34; DEC-P1-FDS-01 |
| Related Risk IDs | RISK-07; RISK-09 |
| Source | #15 AC(v3.1.15 Ticket Update Pack~tickets/v3.1.19 P1-APP-01); evidence#66 GWONUK B2 2026-09-29; fds-msa main 5271e60; DEC-P1-FDS-01(#4) FDS-DAC-04 |
| Schedule Note | AC 문구 정정 CR을 10-02(금)까지 Review 가능한 상태로 만드는 것을 계획 목표로 한다. 10-05는 비근무일이며 10-06 Phase 1 Review 전에 승인/잔여판정을 완료한다. 코드·Runtime 정책 변경은 포함하지 않는다. |

## Source checklist

별도 checkbox 추출 없음. 아래 원문 Exit Criteria/계약을 따른다.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

<!-- issue-enhancement-20261001:v1:start -->
## 2026-10-01 실행·종결 계약 고도화

### Entry / Dependency
- Source of truth: #15 현행 AC, DEC-P1-FDS-01 FDS-DAC-04, evidence#66, fds-msa exact source SHA.
- 이 CR 승인 전 #15 AC 문구·체크 상태를 변경하지 않는다.
- Runtime 장애시험은 #15/#20의 현재 서비스 상태와 복구경로가 확인된 작업창에서만 수행한다.

### Runtime 성공·중단 기준
- 성공: DB 장애와 FDS 장애의 동작을 분리 판정하고, FDS 장애에서 transaction-api Ready 유지 + HTTP 201 + `fds_evaluation_skipped=true` + DB 저장을 원본 증적으로 확인.
- 즉시 중단: 거래 저장 실패, transaction-api Ready 상실, 복구 후 fds-engine replica/health 미복원, 예상 밖 restart 증가.
- 중단 시 CR 문구를 PASS로 올리지 않고 원상복구 후 `NOT MET / Known Issue`로 #30 Review에 이관한다.

### Evidence Contract
- host/cluster/namespace, 실행시각 KST, source SHA/image digest, 장애주입/복구 명령, RC, API 응답, DB row, metric delta, restartCount, 원본 로그/해시를 함께 보존한다.
- 합성 요약만으로 AC를 충족하지 않는다.

### Close / Handoff
- 승인 시 #15 AC를 정확히 교체하고 #20 A04와 동일 증적을 공유한다.
- 10-02까지 미완료면 삭제/완화하지 않고 10-06 #30에서 사실 상태로 분류한다.
<!-- issue-enhancement-20261001:v1:end -->

# CR-P1-APP-01-01 — P1-APP-01 AC "DB/FDS 장애 시 `/readyz` 503" 문구 정정

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | CR-P1-APP-01-01 |
| Phase | Phase 1 |
| Category | Application / Acceptance Criteria |
| Type | Change Request |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-29 |
| End | 2026-10-02 |
| Calendar Days | 4 |
| Working Days | 4 |
| Lead | 이재환 |
| Support | 이하영 |
| Exit Criteria | #15 AC 문구 정정 결정 기록과 Review Owner·G3 확인, #15 본문 AC 교체, FDS 장애 fail-open Runtime 증적, 차기 정본 Ticket Pack 동기화 |
| Related Decision IDs | D18; D34; DEC-P1-FDS-01 |
| Related Risk IDs | RISK-07; RISK-09 |
| Source | #15 AC(v3.1.15 Ticket Update Pack~tickets/v3.1.19 P1-APP-01); evidence#66 GWONUK B2 2026-09-29; fds-msa main 5271e60; DEC-P1-FDS-01(#4) FDS-DAC-04 |
| Schedule Note | AC 문구 정정 CR을 10-02(금)까지 Review 가능한 상태로 만드는 것을 계획 목표로 한다. 10-05는 비근무일이며 10-06 Phase 1 Review 전에 승인/잔여판정을 완료한다. 코드·Runtime 정책 변경은 포함하지 않는다. |

## 변경 요청

[#15](https://github.com/321Team/fds-project-baseline/issues/15) Acceptance Criteria 두 번째 줄을 두 줄로 나눕니다.

| 현재 | 변경안 |
|---|---|
| `DB/FDS 장애 시 /readyz 503와 Endpoint 제외` | ① `외부 DB 장애 시 transaction-api /readyz 503와 Endpoint 제외` |
| | ② `fds-engine 장애 시 transaction-api는 Ready를 유지하고 거래를 fail-open(fds_evaluation_skipped=true, HTTP 201)으로 저장` |

## 변경 이유

1. **현행 설계와 반대입니다.** transaction-api는 fds-engine 호출이 실패하면(connect 1s·read 2s 초과, 오류 응답) 거래를 저장하고 `fds_evaluation_skipped=true`로 기록합니다([계약 v1.0 §5 Option A 기본 채택](https://github.com/321Team/fds-msa/blob/5271e606eb6789c47f36241b8f1a38b61d49fb66/docs/transaction-api_fds-engine_contract_v1.0.md#L107-L114), [`fds_client.py`](https://github.com/321Team/fds-msa/blob/5271e606eb6789c47f36241b8f1a38b61d49fb66/transaction-api/app/fds_client.py#L1-L36), [`main.py` L73-89](https://github.com/321Team/fds-msa/blob/5271e606eb6789c47f36241b8f1a38b61d49fb66/transaction-api/app/main.py#L73-L89)). `/readyz`는 DB 연결만 확인합니다([`main.py` L40-49](https://github.com/321Team/fds-msa/blob/5271e606eb6789c47f36241b8f1a38b61d49fb66/transaction-api/app/main.py#L40-L49), [계약 §6](https://github.com/321Team/fds-msa/blob/5271e606eb6789c47f36241b8f1a38b61d49fb66/docs/transaction-api_fds-engine_contract_v1.0.md#L118-L122)). fds-engine `/readyz`는 외부 의존성이 없습니다([`fds-engine/app/main.py` L50-53](https://github.com/321Team/fds-msa/blob/5271e606eb6789c47f36241b8f1a38b61d49fb66/fds-engine/app/main.py#L50-L53)).
2. **문구대로 만들면 실패 정책이 바뀝니다.** fds-engine 장애 때 transaction-api `/readyz`가 503을 내면 transaction-api Pod 전부가 Endpoint에서 빠져 거래 접수가 멈춥니다. 사실상 fail-closed입니다. [DEC-P1-FDS-01(#4)](https://github.com/321Team/fds-project-baseline/issues/4) FDS-DAC-04는 "새 Fail-Open/Closed/Hold 정책을 선택하지 않음, 기존 실패 경로는 P1-APP-01/P1-E2E-01에서 확인"이고, 실패 정책 변경은 #4의 재검토 조건입니다.
3. **같은 티켓 안에서도 어긋납니다.** #15 핵심 요구사항은 "**외부 DB 장애**는 Readiness에 반영"으로 DB만 걸고, Exit Criteria는 "DB/FDS **장애정책**"입니다. AC만 "DB/FDS 장애 시 `/readyz` 503"입니다(v3.1.15 Ticket Update Pack부터 `tickets/v3.1.19/descriptions/P1-APP-01.md`까지 같은 문구).
4. **정식 변경 기록이 필요합니다.** [evidence#66 GWONUK B2](https://github.com/321Team/fds-project-evidence/pull/66)는 "Lead 해석만으로 승인된 AC를 축소할 수 없다, 정식 변경결정으로 FDS fail-open과 AC 문구를 정합화한 근거를 연결하라"고 했습니다. 그래서 [#15 AC 체크를 해제](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-5882975123)했고, 이 CR이 그 정식 변경 기록입니다. [REVIEW_AUTHORITY_POLICY §5](https://github.com/321Team/fds-project-baseline/blob/e603d0d0177081d6f60b823f66e3559911c56272/governance/REVIEW_AUTHORITY_POLICY.md)도 AC의 실질 변경은 해당 Lead가 Decision/CR에 이유·영향을 기록하고 정본에 인계하도록 합니다.

## 이 CR이 하지 않는 것

- fail-open을 새 정책으로 승인하지 않습니다. #4의 "현행 유지" 아래에서 AC 문구를 현행 동작에 맞출 뿐입니다.
- 코드·Probe·Deployment·Service를 바꾸지 않습니다.
- 다른 AC와 핵심 요구는 바꾸지 않습니다.

## 영향

| 대상 | 영향 |
|---|---|
| #15 AC | 5줄 → 6줄. ①은 [evidence#66](https://github.com/321Team/fds-project-evidence/pull/66)("DB 장애 부분 Runtime PASS")로 다시 판정할 수 있고, ②는 새 Runtime 증적이 필요합니다 |
| #20 | A04 "엔진 실패 fail-open 대조"에 ②의 증적을 연결할 수 있습니다 |
| #4 | FDS-DAC-04와 일치합니다(정책 변경 없음) |
| 정본 | 승인되면 차기 정본 후보 Ticket Pack의 P1-APP-01 AC에 반영합니다(RELEASE_POLICY: 승인된 CR은 다음 정본 후보에 동기화) |

## ② 검증 계획 (확인 뒤 별도 시험)

- 사전 기록: fds-engine 3 Pod·배치, Worker 3대 `/readyz` 200, `fds_evaluation_error_total` 현재값, transaction-api restartCount
- 장애 주입: `kubectl -n fds-app scale deploy/fds-engine --replicas=0` (약 2분, 팀 채팅 사전 공지)
- 관측: edge01 → Worker 3대 `/readyz` 1초 간격 200 유지(Endpoint 유지), `POST /api/v1/transactions` 1건(`SIM_fo15_<RUN>`, 10,000원 입금) → 201·`fds_evaluation_skipped=true`·`fds_detected=null`, DB 행 확인, `fds_evaluation_error_total` +1, restartCount 변화 0
- 복구: replicas 3, Worker당 1개 배치 확인(필요하면 #22와 같은 방식으로 재배치), POST 1건 → `fds_evaluation_skipped=false`
- 합격: 위 관측 모두. 결과는 증적 PR(archive 원본 포함)과 #15 코멘트로 올립니다.

## 확인 요청

- 결정: APP Lead 이재환 (REVIEW_AUTHORITY_POLICY §4 — Decision/CR 검토는 해당 Lead)
- @hayeounglee — #15 Support·Review Owner: 변경안 문구 확인
- @GWONUK — G3: evidence#66 B2의 "정식 변경결정" 요구를 이 CR이 충족하는지 확인

확인 전에는 #15 본문을 고치지 않고 AC도 체크하지 않습니다. 확인되면 #15 본문의 AC 줄 교체는 교체 본문 파일과 plan(전후 SHA)으로 담당자가 직접 반영합니다.

## Completion Record

- **Result:** 승인·완료. #15 AC 두 번째 줄을 ① 외부 DB 장애 `/readyz` 503, ② fds-engine 장애 fail-open으로 분리했고, 두 줄 모두 Runtime 증적으로 체크했다. 코드·Probe·Deployment·정책 변경은 없다.
- **Status:** Done
- **Completed Date:** 2026-10-01
- **Reviewer / Approver:** 이재환(APP Lead 승인), 이권욱(G3 수용 권고, evidence#90 독립 리뷰)

### Exit Criteria 대응

| 항목 | 상태 | 근거 |
|---|---|---|
| #15 AC 문구 정정 결정 기록과 확인 | 충족 | APP Lead 승인 [5928210700](https://github.com/321Team/fds-project-baseline/issues/119#issuecomment-5928210700), G3 수용 권고 [5922785388](https://github.com/321Team/fds-project-baseline/issues/119#issuecomment-5922785388). 이하영(#15 Support·Review Owner) 문구 확인 회신은 없었고, 10/1 회의 "대기 없이 진행" 결정에 따라 완료 처리한다. 이견이 접수되면 재검토한다 |
| #15 본문 AC 교체 | 충족 | [5928210968](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-5928210968), 본문 SHA `e9bbf654…` → `68d03d2f…` |
| FDS 장애 fail-open Runtime 증적 | 충족 | [evidence#90](https://github.com/321Team/fds-project-evidence/pull/90) 병합 `18797bd`, GWONUK APPROVED. #15 ② 체크 [5930827912](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-5930827912) |
| 외부 DB 장애 줄 재판정 | 충족 | [evidence#66](https://github.com/321Team/fds-project-evidence/pull/66) 병합 `e5ed3e9`. #15 ① 체크 [5931020429](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-5931020429) |
| 차기 정본 Ticket Pack 동기화 | 다음 정본 발행 때 처리 | RELEASE_POLICY에 따라 승인된 CR은 다음 정본 후보에 반영한다. 이번에는 발행하지 않았다 |

- Runtime 결과 요약: ② 장애 주입 73초(계획 약 2분), 장애 중 거래 HTTP 201·`fds_evaluation_skipped=true`·DB 저장, `/readyz` 200 유지, 복구 후 `skipped=false`. 편차와 한계는 증적 README에 기록했다.
- 이 CR의 완료는 #20 A04 판정, #17 검토, 정본 발행을 자동으로 완료하거나 승인하지 않는다.

