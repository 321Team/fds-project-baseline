# ICR-D-NET-01-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/14) · updated_at `2026-10-19T10:05:26Z` · body SHA256 `2da95da77c7004f39906dfa7b74fd1fcaf89c6fcbc4f10f37c23166f8a116f75`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | ICR-D-NET-01-01 |
| Phase | Phase 1 |
| Category | Network / Interface Change Control |
| Type | Change Request |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-01 |
| End | 2026-09-21 |
| Calendar Days | 21 |
| Working Days | 15 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | Kubernetes 6개 Node의 보호 공백 없는 firewalld→Calico named HEP/GNP 전환, 30080/9100/10250 최소 허용, 관리망 반환 경로와 IF-06B 정합화, Positive/Negative/Regression/Reboot/Rollback 및 무결성 Evidence 완료 |
| Related Decision IDs | D17; D18; D33; D34; D35 |
| Related Risk IDs | RISK-04; RISK-07 |
| Source | Baseline/Ticket Pack v3.1.18; GitHub #14; PR #2/#3/#4/#8 병합 기록; PR #9 b3f3374 승인·merge c08b798; CP1 최종 재적용·CP2 inspect·CNI 준비 및 p3dmjivl 실측 FAIL 증적. 원 정본 수집 이력: audit/v3.1.18/k8s-intake-20260910.json; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 09-21은 권장 Plan End이며 실제 종료일 확정이나 AC 완료가 아니다. 기존 End TBD 이력은 보존한다. CP→Worker·NTP·IF-16을 먼저, IF-06B·Negative/Reboot/Rollback·보호 인계를 후속 검증한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

실제 GitHub 종결 `2026-10-19T19:05:24+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

- [ ] `ICR-AC-01` — 6개 Node 변경 전 firewall/listener/route 설정과 SHA Evidence를 확보한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-02` — firewalld가 disabled/inactive이고 Calico Pod/Node 통신이 정상이다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-03` — named HEP/`expectedIPs`/Bootstrap Allow가 승인안과 일치한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-04` — `.50 → Worker:30080`은 허용되고 비승인 Source는 차단된다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-05` — Prometheus에서 Worker node-exporter 9100 Target이 `UP`이다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-06` — Prometheus에서 Worker kubelet 10250을 CA+SA로 인증한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-07` — 비승인 Workload의 9100/10250 접근이 차단된다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-08` — Control Plane의 logs/exec/port-forward가 정상이다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-09` — Worker에서 Harbor `.54:443` Pull과 Pod 시작이 성공한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-10` — Cockpit 9090이 노출되지 않는다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-11` — monitor01에서 Cluster Workload로 신규 Ingress를 시작할 수 없다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-12` — IF-06B Remote Write의 TLS/Auth/Payload Allowlist가 충족되고 비승인 Egress가 차단된다. 현재: **BLOCKED**.
- [ ] `ICR-AC-13` — edge/harbor/db에 `10.250.10.0/24 via .58`가 적용되고 `.30` route-get이 통과한다. 현재: **FAIL — DRIFT**.
- [ ] `ICR-AC-14` — Worker 3대에서 동일 경로 조회 회귀가 통과한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-15` — mgmt-gw IP Forward/Zone/Policy/NAT가 승인안과 일치하고 내부 SNAT가 없다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-16` — monitor01 `.30:443` Receiver/Protocol/TLS/Auth가 정본과 일치한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-17` — 패킷 관찰의 실제 Source와 양방향 Return Path가 정본과 일치한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-18` — Reboot 후 정책이 유지되고 재시험이 통과한다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-19` — Rollback을 재현할 수 있다. 현재: **NOT VERIFIED**.
- [ ] `ICR-AC-20` — Evidence에 평문 비밀정보가 없다. 현재: **NOT VERIFIED**.

---

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
