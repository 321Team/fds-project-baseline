문서 버전 **v3.1.22 / CANDIDATE**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# P1-CICD-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/16) · updated_at `2026-10-16T07:44:26Z` · body SHA256 `a67524165c362ee9fdaa980ea812e355b7cce4092b5db603e9c9955c821b94ca`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P1-CICD-01 |
| Phase | Phase 1 |
| Category | CI/CD / Supply Chain |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-01 |
| End | 2026-09-18 |
| Calendar Days | 18 |
| Working Days | 14 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | GitHub→Runner→Test→Build→Trivy→Harbor→Kubernetes Deploy→Health/E2E 흐름과 실패 시 Deploy 차단 Evidence 확보; 승인 Digest와 이전 Digest 복구 추적 |
| Related Decision IDs | D03; D04; D19; D34; D35 |
| Related Risk IDs | RISK-06; RISK-08 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #16 snapshot 2026-09-10T02:09:24Z; Fast Tracking 일정 권장안 2026-09-10 / 사용자 재편성 요청; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | Runner/Workflow·Negative Gate 준비를 플랫폼 구축과 병행하고 승인된 플랫폼·Harbor가 준비된 뒤 배포한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

실제 GitHub 종결 `2026-10-15T19:47:58+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [x] CICD-AC-01: Runner 등록·Service 재시작 후 Online/Job 수신과 IF-08 실제 Run 증적이 있다.
  - [Run34960063214 Attempt2](https://github.com/321Team/infra-cicd/actions/runs/34960063214/attempts/2) / [Job104355893988 원본 로그](https://github.com/321Team/infra-cicd/actions/runs/34960063214/job/104355893988): RUN_ATTEMPT=2, JOB_RECEPTION=VERIFIED, BUILDER_ROOTLESS=VERIFIED. 원 실행은 9/15이며 새 실행하지 않았다.
- [ ] CICD-AC-02: Harbor 정상 Push와 Worker Pull/Pod Start, TLS·인증 음성시험이 대응된다.
  - CA 준비·공개 인계 실적은 보존하되 Harbor 적용/consumer trust·Worker3대·TLS/인증 음성시험 전체 증적은 미인수다.
- [ ] CICD-AC-03: 정상 Commit의 두 이미지 Test→Build→Scan→Push→Digest 갱신과 Health/E2E가 성공한다.
  - 앱#2 병합·앱 Lead 입력 회신은 수신했으나 repo/SHA 정합화·config 반영과 내부 Runner의 실제 Test→Build→Scan·Push·Health/E2E는 잔여다. [회신](https://github.com/321Team/infra-cicd/issues/11#issuecomment-5725640696).
- [ ] CICD-AC-04: 고의 Unit Test 실패 Run에서 Deploy가 skip/차단되고 대상 Deployment의 이미지가 유지된다.
  - 소스/Mock 통과와 실제 Unit 실패→Deploy 차단·대상 이미지 유지 시험은 구분한다. 후자 미실행.
- [x] CICD-AC-05: 취약점 Gate 실패와 스캐너 실행 오류를 각각 실패 처리하며 배포 이미지가 유지된다.
  - 2026-10-14 실제 두 실패 회차와 각 Deployment2/Pod6 이미지 유지 관측을 증적 PR229에 편입했다. 판정·고정 과거 이미지 시험 경계·독립 리뷰 및 Lead 인수 구분은 맨 위 AC05 기록을 따른다.
- [ ] CICD-AC-06: Commit→Run/Attempt→Image→Digest→Deployment/실제 Pod 증적을 역추적할 수 있다. 로컬 Image ID를 registry manifest Digest로 오인하지 않는다.
  - Runner/DB/공급 준비 Run 추적은 일부 존재. 실제 앱 Scan→Harbor→Deployment/Pod 전 구간 trace는 미확보다.
- [x] CICD-AC-07: 실제 Runner 자격증명으로 두 Deployment 권한은 허용되고, 임의 Deployment·create/delete·Secret·RBAC·exec 권한은 거부된다.
  - 2026-10-14 실제 Runner SSAR25건(허용6/거부19)·GET2 및 전후 상태/정리 확인. 증적 PR231 독립 리뷰·병합 후 AC07 충족 반영. 고정 질의 범위와 Lead 인수 구분은 맨 위 AC07 기록을 따른다.
- [x] CICD-AC-08: 만료 Token의 인증 실패 및 새 단기 Token으로 복구를 확인한다. 로그/Artifact/작업 디렉터리에 자격증명이 남지 않는다.
  - 2026-10-15 실제 GET200→만료401→새 Token200·종료 후 지정경로/프로세스 정리 관측, PR235 독립 편입·병합 근거로 충족. 범위와 Lead 인수 판단은 맨 위 AC08 기록을 따른다.
- [ ] CICD-AC-09: 승인 Digest와 승인자가 고정된 배포 기록, 재실행·동시 실행 통제, 이전 Digest 복구 결과가 있다.
  - 수동 승인 운영정책은 정의됨. 실제 승인 Digest 배포·재실행/동시 실행 통제·복구 결과는 미확보다.
- [ ] CICD-AC-10: 이하영의 독립 기술 리뷰와 이권욱의 최종 판정, 미해결 항목 및 정본 인계 기록이 있다.
  - 개별 코드 PR의 독립 리뷰·병합은 부분 실적. 전체 Delivery 인수·잔여 정리·정본 인계는 미완료. 적용 절차는 [9/18 현행 정책](https://github.com/321Team/infra-cicd/blob/ee039707db0a7ae980305f65ffb741d46b149015/docs/governance.md)에 따르며 동일 코드 Runtime에 반복 독립 승인을 새로 요구하지 않는다.

2026-09-15 후속 실행 대조로 CICD-AC-01의 Runtime 증적 충족을 확인했다. CICD-AC-02~10은 미완료이며 전체 인수 승인은 별도다. AC-01 판정은 로컬 상태만이 아니라 재시작 이후 실제 GitHub Job/로그를 근거로 한다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
