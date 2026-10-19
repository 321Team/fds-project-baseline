문서 버전 **v3.1.22 / RELEASED after reviewed finalization merge**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# CR-P1-ANS-01-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/58) · updated_at `2026-10-09T13:06:18Z` · body SHA256 `871283ea4135116604a620feeb5cc67e0b455dd4cd7c6269d9501459fe678817`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | CR-P1-ANS-01-01 |
| Phase | Phase 1 |
| Category | Automation / DNS Client |
| Type | Change Request |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-04 |
| End | 2026-09-07 |
| Calendar Days | 4 |
| Working Days | 2 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Kubernetes 6개 Node의 DNS 전환, 검색 도메인·API FQDN/Short Name·외부 DNS·직접 질의·서비스 회귀·멱등성·Rollback·Evidence 무결성 및 Support Review 완료 |
| Related Decision IDs | D08; D09; D34; D35 |
| Related Risk IDs | RISK-02; RISK-04; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #58 snapshot 2026-09-09T12:14:54Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 2026-09-07 Runtime·멱등성·회귀·Rollback·무결성 증적과 이하영 승인 리뷰를 완료하고 이권욱 수동 승인으로 PR #1을 병합했다. GitHub Actions 실행은 0건이므로 CI PASS로 기록하지 않는다. v3.1.17의 `In Review` 표시는 발행 시점 스냅샷이며 다음 정본에서 `Done`으로 동기화한다. |

실제 GitHub 종결 `2026-09-09T18:52:36+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [x] `CR-DNS-AC-01` — 6개 Node의 DNS 순서가 `.52 → .53`이다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-02` — 6개 Node에 검색 도메인 `fds.internal`이 적용된다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-03` — `k8s-api.fds.internal`이 `.109`로 해석된다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-04` — Short Name `k8s-api`가 `.109`로 해석된다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-05` — 외부 DNS 해석이 정상이다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-06` — 승인 DNS 직접 질의가 정상이다. 결과: 12/12 PASS.
- [x] `CR-DNS-AC-07` — kubelet/containerd 서비스 회귀가 없다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-08` — 멱등성 결과가 `changed=0`, `failed=0`, `unreachable=0`이다. 결과: PASS.
- [x] `CR-DNS-AC-09` — Rollback 자료·절차·검증 결과가 확보됐다. 결과: PASS.
- [x] `CR-DNS-AC-10` — Evidence 원본·Index·SHA-256 무결성을 확인했다. 결과: PASS.
- [x] `CR-DNS-AC-11` — 이하영 Support Review가 승인됐다. 결과: `APPROVED`, 2026-09-07 11:13:58 KST.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
