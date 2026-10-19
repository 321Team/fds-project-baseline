# P1-SEC-01 — 현재 관리·인수 스냅샷

기준 2026-10-19T19:25:19.982565+09:00. 미발행 정본 후보 / CODEX_ASSISTED. [GitHub 원본](https://github.com/321Team/fds-project-baseline/issues/19) · updated_at `2026-10-19T09:04:08Z` · body SHA256 `04ff69e4cc837cbd66baacf67b7ef5585e4bf7b31f01d10850a1c9ee1cde8f12`. 아래 속성표는 현행이며, 발행 v3.1.21 원본은 수정하지 않았다.

| Property | 현재 입력값 |
|---|---|
| Record ID | P1-SEC-01 |
| Phase | Phase 1 |
| Category | Security / Kubernetes |
| Type | Task |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-04 |
| End | 2026-09-21 |
| Calendar Days | 18 |
| Working Days | 10 |
| Lead | 이하영 |
| Support | 이권욱, 이재환 |
| Exit Criteria | PSA/SecurityContext/Default Deny/RBAC/HEP-GNP/Secretbox/LimitRange/Probe와 `.50/32→30080` 포함 Positive·Negative·Rollback Evidence PASS |
| Related Decision IDs | D12; D17; D18; D19; D27; D31; D34 |
| Related Risk IDs | RISK-06; RISK-07; RISK-08 |
| Source | Baseline/Ticket Pack v3.1.18; GitHub 321Team/fds-project-baseline#19; K8S PR 321Team/fds-project-baseline#2 097ddb5, 321Team/fds-project-baseline#3 merge 7d44afc, 321Team/fds-project-baseline#4 75d476e; audit/v3.1.18/k8s-intake-20260910.json; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 09-10 휴가 추가 후 기존 09-04~11 가용일은 4일. 권장 종료 09-21로 확장한 전체 계획창의 가용일은 10일이며 잔여 공수를 뜻하지 않는다. Runtime 검증은 플랫폼·앱 인수와 연계한다. 실제 상태·완료 판정은 유지한다. 세부 배정: Fast Track Plan 시트. |

실제 GitHub 종결 `2026-10-19T18:04:07+09:00` / `completed`. 계획 End와 구분한다. Cancelled는 구현 완료가 아니다. Done도 각 원 인수·한정 처분의 범위이며 기술 전체 PASS를 뜻하지 않는다.

## 현재 원 AC — 체크 상태 보존

**현행 인수 현황은 상단 AC 진행현황과 후속 확정 기록을 따른다.** AC01·AC03은 기존 MET/ACCEPTED이며 AC02·AC04·AC05·AC06 전체는 `[ ]`를 유지한다. 아래 9/23 시점 미실행·실패 표기는 최신 수용·보완과 구분하며, 이번 정합화는 새 인수·위험수용·Runtime 승인이 아니다.

- [x] PSA 위반 Pod 차단 — **MET / ACCEPTED**. [기존 Review Owner 판정6033026240](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-6033026240)의 PSA 위반 거부·version label·준수/위반 범위만 재사용한다.
- [ ] Allow 흐름 PASS / Deny 흐름 FAIL — **PARTIAL / NOT_VERIFIED 및 기존 행별 처분 유지**. CR126 WITHDRAWN/NO CHANGE로 원 AC를 보존한다. IF03/IF13A·IF12B·IF09·IF05C·IF06B의 후속 관측과 IF10 기존 인수를 연결하되 전체 AC02 인수·미충족 행의 #30 처분은 별도다. 철회된 MET6/RISK7/NOT_MET2 집계는 사용하지 않는다.
- [x] SA별 `kubectl auth can-i` Positive/Negative PASS — **MET / ACCEPTED**. [기존 Review Owner 판정6033026240](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-6033026240)의 합의 SA/권한 Matrix 범위를 재사용한다. 실제 Token 인증·만료/갱신·업무 변경 성공으로 확대하지 않는다.
- [ ] NodePort/9100/10250 HEP/GNP PASS — **전체 미충족·기존 한정 처분 유지**. 9/23 node-exporter 1/3 UP·kubelet/cadvisor6대 DOWN은 당시 이력이다. 이후144 방식B 누락6행 관측·207의 해당 시점23/23과10/18 MON7 회복을 각각 연결한다. CP3 기존 부팅 위험수용과 Worker3 조건부 수용은 별개이며 EARLY 직접 미측정·특정 차단 귀속 한계를 유지한다. #45 조치 전 pre-state/dry-run 원본 공백은 별도 Lead 처분 대기다.
- [ ] Secret encryption·backup·rotation·rollback PASS — **복합 AC05 전체 `[ ]` 유지**. [한정 통합 처분6205182638](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6205182638)에 따라 encryption·control03 1회 rollback·snapshot 격리 복원/health/정리 범위는 하위 MET, 예방 rotation은 NOT MET/RISK ACCEPTED다. 운영 DR 전체·복원본 Secret 복호화·APP 소비로 확대하지 않는다. 노출 키/DB credential 잔여는 별도 유지한다.
- [ ] Probe 장애 주입과 Endpoint 제외 PASS — **부분 관측 확보 / 전체 AC06 인수 대기**. 173 격리 exec 전이·177 실제6종 정의/Ready·223 실제 engine HTTP 실패→Endpoint 제외→kubelet 재시작→회복을 재사용한다. 관측기rc1·최초 HTTP 회복시각 미확정 한계를 보존하며 MON5종 대응 원본·인수 범위는 MON/SEC 판단으로 남긴다. 전부 NOT_RUN 또는 전수 장애 주입 필수로 바꾸지 않는다.

## 상태·원조건 추적

기존 승인·위험수용·미검증·Reviewer/Approver는 해당 GitHub 원문/댓글과 [Review 원조건 표](../REVIEW31_RESULTS_AND_DECISION_CARD.md)를 따른다. 상태 동기화가 원 AC를 완화하거나 미실행을 MET로 바꾸지 않는다.
