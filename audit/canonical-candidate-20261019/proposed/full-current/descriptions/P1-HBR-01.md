# P1-HBR-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/13) · updated_at `2026-10-19T09:04:16Z` · body SHA256 `b70bf46a22d42becd8950379877fe90b064c660dcd1b7a44340c1f65227fe0f9`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P1-HBR-01 |
| Phase | Phase 1 |
| Category | Registry / Supply Chain |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-31 |
| End | 2026-09-17 |
| Calendar Days | 18 |
| Working Days | 12 |
| Lead | 이하영 |
| Support | 이권욱 |
| Exit Criteria | harbor01 `.54:443`, Private CA Trust, 최소권한 Robot Account, IF-09 Runner Push·IF-10 Worker Pull/Pod Start, 비승인 Push/Pull DENY, Trivy/Digest/Evidence PASS |
| Related Decision IDs | D04; D17; D19; D35 |
| Related Risk IDs | RISK-04; RISK-06; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #13 snapshot 2026-09-10T03:15:50Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | Harbor 준비는 CP 후속과 병행하고 09-16 CI Scan Digest까지 4/4 대조 후 09-17 인수 목표다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

실제 GitHub 종결 `2026-10-19T18:04:15+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [x] Harbor Service/Health와 Certificate Chain PASS
  - 부분 준비: CA 발급·반입/키 일치. 정식 Service/Health·Certificate Chain의 실제 검증 증적은 미확인이다.
- [x] IF-09 Positive/Negative PASS
  - IF-09 실제 Runner Push/Pull·인증/비승인 음성시험 원본 미인수.
- [x] IF-10 Pull/Pod Start 및 Push DENY PASS
  - IF-10 Worker3대 Pull/Pod Start·Push DENY 원본 미인수.
- [ ] 실제 Source IP와 Host Firewall Allowlist 일치 — 부분 검증 완료, 최종 인수 HOLD(상단 최신 기록)
  - Route/allowlist의 설계·코드와 Harbor 도착지 관측 Source 일치의 실제 검증은 구분한다. 원본 미인수.
- [ ] Image Digest·Scan 결과·Credential fingerprint Evidence 확보
  - CI Scan Digest 생산은 #16, Harbor Artifact/Worker/배포 Digest 연결은 공동 확인. 4/4 trace·credential fingerprint 실행 증적 미확보.
- [x] 비밀정보 평문 미포함
  - PR2 코드 보완·승인은 확인. 해당 인수 증적 전체의 비밀정보 평문 비포함 여부를 확인한 기록은 미확보.

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
