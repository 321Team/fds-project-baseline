문서 버전 **v3.1.22 / RELEASED after reviewed finalization merge**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# D-NET-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/60) · updated_at `2026-10-04T06:01:55Z` · body SHA256 `ea2f55c13ab49552dbb9f47e40217a5ea40842f08e75a61c73d66748c30e86bf`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | D-NET-01 |
| Phase | Design |
| Category | Network / Infrastructure Design |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-24 |
| End | 2026-08-26 |
| Calendar Days | 3 |
| Working Days | 3 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Windows server01~08 PostBuild FAIL=0, VMnet0/VMnet1/VMnet8 분리, Physical Return Route via 10.1.93.58, Source Preservation PASS=6/FAIL=0, Management VM 및 mgmt-gw01 Verify FAIL=0, Closure Report 승인 |
| Related Decision IDs | D05 — Bridged Node / Service Endpoint`, `D13 — VMnet1/VMnet8 분리`, `D14 — Physical Return Route / Source NAT 금지`, `D15 — 10.1.93.254 프로젝트 비관리`, `D16 — Reserved / DO_NOT_USE IP |
| Related Risk IDs | RISK-02 — Bridged Multi-MAC 제한 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #60 snapshot 2026-09-10T02:10:11Z; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 2026-08-26 실제 완료. 기존 계획보다 Closure가 1일 연장되었으나 Network Design/Implementation/Evidence를 포함해 DONE 처리. 후속 구축 범위는 P1-K8S-01 및 P1-DNS-01로 이관한다. |

실제 GitHub 종결 `2026-09-09T18:53:40+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [x] Windows server01~08 PostBuild 결과가 모두 `FAIL=0`이다.
- [x] Kubernetes 예정 Node 6대의 Linux 필수조건이 PASS다.
- [x] Kubernetes 예정 Node 6대의 Network Verify가 모두 `FAIL=0`이다.
- [x] Physical Node 6대의 Management Return Route가 `10.1.93.58` 경유로 동작한다.
- [x] `ansible01(10.250.10.10)`에서 Physical Node로 접속할 때 Remote Observed Source가 원본 주소로 유지된다.
- [x] Management Source Preservation 결과가 `PASS=6`, `FAIL=0`이다.
- [x] `ansible01`, `cicd-runner01`, `monitor01` Network Verify가 모두 `FAIL=0`이다.
- [x] `mgmt-gw01` Verify 결과가 `FAIL=0`이다.
- [x] `FDS_Network_Baseline_v2.3`과 `D-NET-01_Closure_Report_v1.0`이 승인·보관되었다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
