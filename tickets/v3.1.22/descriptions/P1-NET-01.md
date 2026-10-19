문서 버전 **v3.1.22 / RELEASED after reviewed finalization merge**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# P1-NET-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/67) · updated_at `2026-10-09T13:06:34Z` · body SHA256 `f9af2a1aa0b4f7e11c0f6614fe026cf14650fd22b04a2e8ae7c0979a852723a4`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P1-NET-01 |
| Phase | Phase 1 |
| Category | Network / Connectivity Validation |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-27 |
| End | 2026-08-27 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Bridged Node 6대의 `/24`·Gateway·승인 통신 경로와 Physical/Management Return Route를 검증하고, Management Source Preservation `PASS=6`, `FAIL=0` 증적을 확보 |
| Related Decision IDs | D05; D13; D14; D15; D16 |
| Related Risk IDs | RISK-02; RISK-04 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #67 snapshot 2026-09-10T02:10:17Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 최초 계획은 2026-08-27 1일이었으나 D-NET-01 및 P1-LNX-01 통합 검증 증적이 2026-08-26 확보되어 조기 종결했다. Remaining Backlog에는 재등록하지 않고 Closed Ticket로 관리한다. |

실제 GitHub 종결 `2026-09-09T18:57:19+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [x] Bridged Node 6대의 Prefix가 모두 `/24`다.
- [x] Bridged Node 6대의 Default Gateway가 모두 `10.1.93.254`다.
- [x] Physical / Management Return Route가 `10.1.93.58` 경유로 정상 동작한다.
- [x] Node 간 승인 경로 통신이 정상이다.
- [x] `ansible01(10.250.10.10)`에서 접속할 때 Remote Observed Source가 `10.250.10.10`으로 유지된다.
- [x] Management Source Preservation 결과가 `PASS=6`, `FAIL=0`이다.
- [x] 관련 Linux Network Verify 결과가 `FAIL=0`이다.
- [x] 비관리 Gateway의 ICMP 응답 여부와 무관하게 Route / ARP / 승인 TCP 경로로 합격 근거를 확보했다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
