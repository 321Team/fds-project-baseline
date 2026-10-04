<!-- fds-canonical-live:v3.1.21 record-id:DEC-P1-MON-02:start -->
## 현행 정본 적용 — v3.1.21

- 정본: [docs-v3.1.21](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.21), 2026-10-04 14:49:12 KST 발행. 기준 커밋: `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3`.
- [이 티켓의 발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/DEC-P1-MON-02.md) · [Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md) · [WBS](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx).
- [테스트 전략](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tests/FDS_Test_Strategy_v3.1.21.md): 해당 업무의 기존 AC·Exit Criteria와 실행/인수 구분을 유지한다.
- 정본 Description은 2026-10-03 수집 시점 기록이다. 발행 후 실제 수행·검토·잔여·승인 변경은 아래 최신 운영 기록과 원본 증적을 따른다. 아래 과거 버전의 '현행/후보/미발행' 문구는 작성 당시 이력이다.
- 발행·동기화로 Status, AC 체크, 실제 완료일, 담당자, 일정, Runtime 승인 또는 종결을 상향하지 않는다. 신규 계획·사양 충돌은 별도 변경결정으로 정합화한다.
- 반영 근거: 사용자 '디스크립션 파일 반영과 이슈 본문 수정' 지시. AI 사용: CODEX_ASSISTED.
<!-- fds-canonical-live:v3.1.21 record-id:DEC-P1-MON-02:end -->

<!-- fds-status-sync:20260926 -->
## 현재 상태 동기화 — 2026-09-26 KST

- GitHub State: **Closed / Completed**
- 본문 Status: **Done**
- Label: `status:done`
- Decision 범위는 완료됐으며, P1-MON-01 route 형상/현장 반영 및 전체 Monitoring 인수는 별도 추적합니다.

# DEC-P1-MON-02 — Alertmanager Discord 제한 Egress·발송 범위·Secret Lifecycle 결정

## 속성

| Property | 입력값 |
|---|---|
| Record ID | DEC-P1-MON-02 |
| Phase | Phase 1 |
| Category | Monitoring / Alerting / Security / Egress |
| Type | Decision |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-26 |
| End | 2026-09-26 |
| Calendar Days | 1 |
| Working Days | 1 |
| Lead | 이권욱 |
| Support | 이하영, 이재환 |
| Exit Criteria | #75에서 승인된 Discord 제한 egress 범위, 발송 대상, Secret lifecycle, 실패·복구 인수 결과를 하나의 D-ID로 고정하고 #75/#17 및 v3.1.21 정본 인계 범위를 명시 |
| Related Decision IDs | DEC-P1-MON-01; DEC-P1-EGRESS-01 |
| Related Risk IDs | 미부여 — 정본 Risk Register 대조 후 부여 |
| Source | DEC-P1-EGRESS-01 #78; CR-P1-MON-01-02 #75; P1-MON-01 #17; 2026-09-26 Alertmanager Discord 제한 egress·발송·실패/복구 Runtime 인수 결과; 현행 발행 정본: docs-v3.1.21 (979facb98de8ca1f1e2ce22f38b27ac3366f3fc3); 수집 후 실행 기록은 본문 최신 증적 기준 |
| Schedule Note | 2026-09-26 단일일 Decision으로 종결. #75의 Runtime/AC 인수 결과를 정책으로 고정했으며 P1-MON-01 route 형상·현장 반영 및 전체 Monitoring 인수는 별도 추적한다. |
| Related | DEC-P1-MON-01, [DEC-P1-EGRESS-01 #78](https://github.com/321Team/fds-project-baseline/issues/78), [CR-P1-MON-01-02 #75](https://github.com/321Team/fds-project-baseline/issues/75), P1-MON-01 #17 |

## 결정 배경

DEC-P1-EGRESS-01 #78은 egress-proxy01의 배치·예약 IP·프록시 예외 원칙을 결정했다. 이후 #75에서 실제 Alertmanager NetworkPolicy, Secret, 허용/거부, Discord 발송 및 실패·복구 Runtime 검증까지 완료했다.

#75 종결 전, 구현 결과에서 확정된 운영 정책을 정본에 재사용할 수 있도록 별도 Decision ID로 고정한다. 이 Decision은 #78을 대체하지 않으며, #78의 프록시 배치 결정 위에 Alertmanager-specific 운영 정책을 추가한다.

## 최종 결정

### 1. Alertmanager 외부 Egress 경로
- Namespace: `monitoring-api`.
- 대상 workload selector: `app=alertmanager`.
- Discord 외부 송신은 **Alertmanager → egress-proxy01 `10.1.93.56:3128` → `discord.com:443` CONNECT** 경로만 허용한다.
- Alertmanager의 직접 Internet egress는 허용하지 않는다.
- 다른 Pod/서비스에 일반 프록시 사용 권한을 확대하지 않는다.
- DNS egress는 승인된 CoreDNS 경로의 UDP/TCP 53으로 제한한다.

### 2. Discord 발송 범위
최종 발송 대상은 다음으로 고정한다.
- `severity=critical`
- `alertname=FDSDetectionBurst` (warning)

그 밖의 warning/info 알림은 기본 `screen-only`로 유지한다.

근거: [MON Lead 이재환의 최종 보완 결정](https://github.com/321Team/fds-project-baseline/issues/75#issuecomment-5843243833). 구현 형상은 P1-MON-01의 Alertmanager route 범위에서 관리하며 #75 NetworkPolicy 종결조건으로 확대하지 않는다.

### 3. Discord Webhook Secret
- Secret 이름/역할: `discord-webhook`.
- Webhook URL은 Git, Issue/PR 댓글, 증적 원문에 기록하지 않는다.
- 확정 lifecycle 절차: `infra-monitoring/docs/ALERTMANAGER_SECRET_LIFECYCLE_REVIEW_20260924.md`.
- 생성·재발급: 이하영.
- 설정 인계·검증: 이재환.
- 노출, 담당 변경, 단계 인계가 발생하면 폐기·재발급한다.
- 실제 주기적 회전 시험은 #75 Exit Criteria에 포함하지 않지만, 이 결정으로 lifecycle 요구 자체를 면제하지 않는다.

근거: [#75 Secret 절차 정정·확정](https://github.com/321Team/fds-project-baseline/issues/75#issuecomment-5843147703).

### 4. 실패·복구 인수
전송 실패·복구는 범위 밖으로 유예하지 않고 실제 시험 결과를 인수 근거로 사용한다.

2026-09-26 17:25~17:32 KST:
- Squid 중지 → Alertmanager Discord 요청 실패 지표 증가 확인.
- Squid 복구 → 재전송 후 FIRING 도착.
- 이후 RESOLVED 도착.
- 실패 카운터는 누적값이므로 복구 후 0으로 돌아가는 것을 성공조건으로 사용하지 않는다.

근거: [#75 AC④ 실패·복구 PASS](https://github.com/321Team/fds-project-baseline/issues/75#issuecomment-5844673154).

### 5. 형상·Runtime 인수 경계
- `monitoring-api-dns-allow`는 저장소 소스와 현장 객체의 `kubectl diff rc=0`이 확인됐다. [근거](https://github.com/321Team/fds-project-baseline/issues/75#issuecomment-5843190278)
- #75 AC ①~④는 Lead가 충족 판정했다. [근거](https://github.com/321Team/fds-project-baseline/issues/75#issuecomment-5843216061)
- 본 Decision은 #75에서 이미 검증한 Runtime 결과를 기록하는 것이며, P1-MON-01 전체 AC 또는 G2 전체 PASS를 의미하지 않는다.
- Alertmanager route 형상화·현장 반영은 P1-MON-01에서 계속 관리한다.

## 비결정 / 범위 밖
- Alertmanager 외 다른 workload의 일반 Internet egress.
- 범용 egress proxy 제공.
- Discord 이외 신규 SaaS 목적지.
- Webhook URL 자체의 저장 또는 증적 편입.
- P1-MON-01 전체 Runtime 완료·티켓 종결.
- G2 전체 Gate 판정.

## 정본 인계
- 차기 정본 후보: v3.1.21.
- Decision Register에 `DEC-P1-MON-02`와 #75/#78 관계를 반영한다.
- 구현 티켓의 과거 이력과 실제 Runtime 결과를 본 Decision의 존재만으로 소급 변경하지 않는다.

## Completion Record
- Result: **Done — Discord 제한 egress 운영 정책과 발송 범위·Secret lifecycle·실패/복구 인수 기준 확정**
- Status: **Done**
- Completed Date: **2026-09-26 KST**
- Decision Owner: **이권욱**
- Supporting Decisions: 이하영(#75 Lead Runtime/AC), 이재환(MON Lead 발송 범위)
- Residual: P1-MON-01 route 형상/현장 반영 및 전체 Monitoring 인수는 별도 추적
