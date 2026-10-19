# 이권욱 직접 결정 카드 — 최종 인수와 Gate 판정

기준 2026-10-19T18:53:07.358578+09:00. **권고는 아래 네 판정을 한 번에 한정 채택하는 것**이다. 아직 채택되지 않은 제안이며, 기존 U1/U2/HBR/DOC 결정의 재승인이 아니다.

| 결정 대상 | 권장 최종 판정 | 승인 범위 밖·미입증 보존 |
|---|---|---|
| ICR #14 | 원 AC20 대응표의 실제 기능·선택 정책·경로·복귀 근거와 기존 처분을 소비해 **조건부 최종 인수**. 최초 CP route/공급 provenance·직접 K/C CRI·미관측 monitor→Workload 행·전체 복구 completeness는 이름 붙인 근거 한계/KI로 남김 | 원 AC 전부 MET·과거 raw 복구·현재 GW 전체 NAT/listener/양성 흐름·무제한 복구 보장 아님. U1의 기존 Owner/10월26일 또는 선행 변경·재사용 트리거를 유지하며 새 기한/기술 PASS 없음 |
| Ansible #9 | source0d58598d·절대venv2.21.3의 **확인된 수동 opt-in·기존 두 엔진 격리CI/role 범위 조건부 최종 인수** | 외부/동적 caller·loader/.pth는 U2-B2 KI. 전역 RPM/PATH 교체·전 caller 전환·임의 새 역할/action 허용 아님. 기존 이권욱/10월26일 또는 새 caller·source/config/engine/Collection 변경·실제P2 재사용 전 재검토 유지 |
| G1 #18 | 원 Exit8묶음의 기존 기술 인수와 위 한계를 소비한 **준비도 조건부 수용** | 모듈 Closed 합산 자동PASS·미래 Push credential 유효성·전체 Ansible 업그레이드 성공 선언 아님 |
| G3 #29 | E2E/HA/DR/DOC 인수 및 아래의 **명시된 기존 Residual Risk 목록을 조건으로 Review Ready 조건부 수용** | 새 전환경 시스템Critical0/무조건PASS 아님. 문서Critical0과 별개. 실제Demo/Review/Action·#30 Signoff·#32전체Close·새 Release는 별도 |

기존 위험/한계의 유효 근거: [CP3·Worker3·복구4대·도구·OID02](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6205182638), [U1](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6259937834), [U2](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6261617347), [HBR 보관/Push](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6261947431), [SEC 최종 Source/목적지 미관측KI](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-6263349027), [APP/E2E D07·I01·E1/E2·부하/PG/HA 경계](https://github.com/321Team/fds-project-baseline/issues/20#issuecomment-6263244501), [MON D02·PF·IF06B](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6263609528), [DOC 선택 Freeze](https://github.com/321Team/fds-project-baseline/issues/24#issuecomment-6263765512). D07의 첫 재검토는 이미 완료했으며 새 구현Due를 만들지 않는다. CVSS 취약점 등급과 제품 결함 Critical은 서로 다른 분류다.

**G2는 직접 결정 대상이 아니다.** 이하영님의 [18:38 조건부 수용](https://github.com/321Team/fds-project-baseline/issues/23#issuecomment-6264221185)은 이미 실제 Lead 판정이다. 남은 것은 사용자 지시대로 Notion 대신 정본 후보에 결과를 실제 반영·대조하는 일이다. 현재 XLSX는 P1선택7건만 반영된 부분후보이므로 G2 추적 조건 완료/종결을 미리 쓰지 않는다.

미채택 시 ICR/Ansible/G1/G3는 OPEN을 유지하고, 원조건 가운데 실제로 추가 검증이 필요한 행만 특정한다. 새 전노드 재부팅·설치·역할185/CI/DNS canary/HA/DR 반복은 기본 대안이 아니다. 현재 승인 요청은 최종 인수/판정이며 서버 실행 승인이 아니다.

최종 판정 후: 정확한 네 기록·후속 책임·기존 재검토를 #30 및 각 티켓에 연결 → 정본 후보/WBS/Description 동일 반영 확인 → 종결 가능한 항목만 처리. 실제 Review/Demo와 전체 Signoff는 별도 단계로 계속한다.


## 실제 채택

사용자 회신 **네 항목 권장안 한정 채택**. 2026-10-19T18:59:05.136131+09:00 · [실제 중앙 결정](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6264594986)

G2 실제 Lead 수용은18:38, 기존원문6264221185를 재사용. 기존제안 상태와 실제채택은 이 절로 구분합니다.
