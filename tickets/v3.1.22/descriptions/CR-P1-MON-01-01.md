문서 버전 **v3.1.22 / RELEASED after reviewed finalization merge**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# CR-P1-MON-01-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/74) · updated_at `2026-10-09T13:06:37Z` · body SHA256 `8032fb1c24b43f0cf168b86dc332d14e3c1526d4570e3b884aab73bbd270bb22`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | CR-P1-MON-01-01 |
| Phase | Phase 1 |
| Category | Monitoring / Alerting Egress Change Control |
| Type | Change Request |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-11 |
| End | 2026-10-06 |
| Calendar Days | TBD — Start/End 확정 후 산정 |
| Working Days | TBD — 계획일·가용일 확정 후 산정, 교육장 주말 작업 0 |
| Lead | 이하영 |
| Support | 이재환 |
| Exit Criteria | discord.com 아웃바운드 확인, 프록시 전용 VM 확정, Squid/Nginx 구성 및 discord.com allowlist 적용, 고정 IP·포트를 [Issue B(#75)](https://github.com/321Team/fds-project-baseline/issues/75)에 전달 |
| Related Decision IDs | D17; D33; D34; D35 — 현행 영향 기준. 신규 CR 승인·신규 D-ID/Interface ID는 미확정 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | [발행 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18), 승인 SHA 72599ae49342b0fb8dbd3d8ee60314afb9f907bb; [P1-MON-01 #17](https://github.com/321Team/fds-project-baseline/issues/17); [방식·책임 논의 infra-kubernetes #5](https://github.com/321Team/infra-kubernetes/issues/5); [현황 보고 5632931284](https://github.com/321Team/infra-kubernetes/issues/5#issuecomment-5632931284); [후속 CR #75](https://github.com/321Team/fds-project-baseline/issues/75); 사용자 2026-09-11 속성 보완·추적 요청 및 담당·일정 확정 지시(공통 Lead 이하영/Support 이재환, #74 Start 2026-09-11·End TBD, #75 프록시 서버 선행으로 Start/End TBD); 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | Lead 이하영·Support 이재환, Start 2026-09-11·End TBD. 프록시 배치와 고정 scheme/host/IP/port를 확정하여 #75에 인계한다. 종료일은 후속 계획에서 확정한다. 교육장 주말 작업은 배정하지 않는다. G2는 추적용 분류이며 기존 P0/G2 Acceptance에 필수 조건을 자동 추가하지 않는다. |

실제 GitHub 종결 `2026-09-26T11:29:06+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

원 AC/Exit 및 상세 변경결정은 [현재 원문](https://github.com/321Team/fds-project-baseline/issues/74)을 따른다. 이 후보는 AC를 재작성하지 않는다.

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
