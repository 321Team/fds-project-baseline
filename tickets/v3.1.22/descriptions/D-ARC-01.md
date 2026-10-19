문서 버전 **v3.1.22 / CANDIDATE**. 사용자 이권욱의 2026-10-19 정본 발행 지시에 따른다. PR191 내용 병합 `caa13c1839b31675794abd1ca9c1071376561643`와 실제 후속 인수·Signoff·Close를 입력으로 삼는다. 과거 입력 안의 후보/미발행·당시 미완료 표현은 당시 이력이며 현재 문서 상태는 이 절과 CURRENT/Release API를 따른다. 새 Runtime·서버·P2 실행·원 AC의 기술 MET 승격은 없다.

# D-ARC-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. v3.1.22 관리·인수 기록 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/59) · updated_at `2026-10-04T06:01:35Z` · body SHA256 `c5bc3af88a9d524449858cd3e18378598751cfb6d98b65089a1a83254125ff9e`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | D-ARC-01 |
| Phase | Design |
| Category | Design / Planning |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-08-24 |
| End | 2026-08-26 |
| Calendar Days | 3 |
| Working Days | 3 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | Logical / Physical Architecture v3.1.2 Freeze, MSA / CI-CD / Monitoring / Security 경계 확정, IP·배치 정합성 확인, Release / Freeze / 승인 메타데이터 반영 |
| Related Decision IDs | D01`~`D09`, `D12`~`D16 |
| Related Risk IDs | RISK-02`, `RISK-04`, `RISK-06`, `RISK-07`, `RISK-08`, `RISK-09 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #59 snapshot 2026-09-09T12:15:20Z; 2026-09-11 첨부 원본 속성 복원 D-ARC-01 (ZIP SHA-256: 5cb91902828ac0432493300632297a4703aaa98b7418b9cb1f0828bec68a1b5b); 2026-09-11 사용자 날짜 정정 — Issue #59 날짜 정정 기록 / PR #72 후속 편입; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 2026-08-26 Architecture 설계 동결 완료. 본 티켓의 종결은 Phase 1 논리·물리 구조와 Interface 경계의 승인을 의미하며 개별 구성요소의 구현 완료를 의미하지 않는다. 이후 구조·배치·IP·포트·보안 경계 변경은 Change Request와 영향도 검토 후 신규 버전에 반영한다. 2026-09-11 사용자 확인으로 계획 End를 2026-08-26으로 정정하여 3일 기간과 일치시켰다. |

실제 GitHub 종결 `2026-09-09T18:53:09+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [x] Logical Architecture v3.1.2에 External, Management, Physical FDS Network 및 Kubernetes 경계가 구분되어 있다.
- [x] Physical Architecture v3.1.2에 server01~08의 Windows Host IP와 주요 VM / Service 배치가 반영되어 있다.
- [x] Kubernetes 3CP + 3Worker, API LB, Harbor, PostgreSQL, Edge 및 DNS P1 배치가 두 Architecture 간에 일치한다.
- [x] `transaction-api` / `fds-engine` 2-Service MSA와 PostgreSQL 저장 흐름이 표현되어 있다.
- [x] GitHub Actions → Runner → Harbor → Kubernetes Deploy의 CI/CD 경계가 표현되어 있다.
- [x] Prometheus의 Infrastructure 및 Application / FDS Metrics 경로가 표현되어 있다.
- [x] Default Deny, Required Allowlist, RBAC, non-root 및 seccomp의 Security Boundary가 표현되어 있다.
- [x] Physical, Management, VMnet8 Subnet과 Return Route, Source Preservation, NAT 금지 및 IP 예외가 Network Baseline v2.3과 일치한다.
- [x] 두 Mermaid 원본에 `Release: v3.1.2`, `Freeze Ticket: D-ARC-01`, `Freeze Date: 2026-08-26`, `Status: APPROVED / DONE` 메타데이터가 기록되어 있다.
- [x] Implementation Baseline v3.1.3의 Configuration-controlled Deliverables와 Project Status Register에 D-ARC-01 종결 근거가 반영되어 있다.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
