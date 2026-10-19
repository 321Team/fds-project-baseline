# MON — D02 실제 수행 조건과 IF06B·Probe 판단 입력
대상 Owner: **이재환(MON Lead)**. Support 이권욱·보안 검토 이하영 유지. 기준 baseline main `acc513cf5c9f3e07e58d818a18e4b8fcf1e0cf70`의 [원 MON Description](https://github.com/321Team/fds-project-baseline/blob/acc513cf5c9f3e07e58d818a18e4b8fcf1e0cf70/tickets/v3.1.21/descriptions/P1-MON-01.md), [승인 Runbook466d29e9 §3/3.1](https://github.com/321Team/infra-monitoring/blob/466d29e995a1a7e97f3d8ed09015250282a34dfe/docs/RUNBOOK_P1_MON_01_20261002.md). **Owner 회신·최종 인수 미작성**.

## 재사용할 사실과 판단
- [D02 수행계획 인수6208668917](https://github.com/321Team/fds-project-baseline/issues/30#issuecomment-6208668917)·MON44 반영 완료. 수행계획을 재승인받지 않는다. edge HTTPS NOT_MET·HTTP 평문·자동 통보 공백과 기존 한정 조건을 유지한다.
- [10/18 재가동 후 미수행6255737394](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-6255737394)는 그대로다. 사유·정확 예정시각·하루 이상 접근불가는 미확인이다. MON7 Ready/23/23·중앙 HTTP를 본인 수행으로 바꾸지 않는다.
- [E1/E2 이번1회 수용6258576446](https://github.com/321Team/fds-project-baseline/issues/15#issuecomment-6258576446)은 완료 입력이다. API66.3초·engine 당시 실시간 NOT_PROVEN을 유지하고 정상 앱을 다시 재시작/시험하지 않는다.
- Grafana ‘없음—비상접속·접근 변경 모두 없음’ 사용자 회신은 기록 완료. 같은 사실을 다시 묻거나 회전/감사 성공으로 확대하지 않는다. 기존 C1 다섯 트리거·감사공백 처분·최종 인수 전 SEC 검토는 자기 범위로 유지한다.

## D02 — 승인된 실제 수행·미수행 기록 조건
| 상황 | 조건·정상 판정 |
|---|---|
| 일상/변경창 | 이재환이 근무일 시작·클러스터 변경창 전후·worker03/MON 이상 의심 시 monitor01 네 항목. 근무일 시작에는 server08(.29)의 edge /readyz도1회 |
| monitor01 네 항목 | heartbeat 수신15초 안팎·Watchdog에 HeartbeatMissing 없음·API LB probe_success=1·local/nginx 사용자 유닛 active2줄 |
| edge | 교육장 server08/10.1.93.29 기존 curl 셸→http://10.1.93.50/readyz HTTP200. HTTPS·POST·DB 시험으로 대체하지 않음 |
| 시연 직전 | 녹화·리허설·평가 일정 사전 공유와 해당 시각 콘솔/PC 접근이 전제. monitor01 네 항목+edge1회 모두 정상이어야 함. 정상이어도 #17에 KST 시각·결과 한 줄 |
| 부재/이상 | 본인이 기존 원격 경로로 확인. 불가하면 날짜·사유를 미수행 기록; 당일 기록도 불가하면 다음 근무일 시작에 명시. NoData/오류/오래된 표본/non200은 정상 아님. restart/reboot·설정 변경은 별도 권한/창 |
| 기존 적용 경계 | 시험·합성 데이터/실습망·10/26 P1 자원 회수까지. 회수 지연·하루 이상 확인 불가·감시/edge 구성·노출 변경·실제 데이터 유입 시 자동 연장 없이 기존 재검토 |

위는 기존 절차 연결이며 새 일정·현재 정상·실제 수행을 확정하지 않는다. 과거 미수행은 현재 점검으로 소급 해소하지 않는다.

## IF06B와 SEC MON5 — 기존 원본으로 판단할 잔여
[현재 #17](https://github.com/321Team/fds-project-baseline/issues/17)의 Receiver/TLS/Auth/allowlist/Return Route·IF24 부재 조건 유지.122 Source/401·151 정책 원본·[207](https://github.com/321Team/fds-project-evidence/pull/207) canary/구간 관측/회수는 자기 범위로 재사용한다. 특정 nft 규칙 유일 귀속·새 감사로그 검증을 일률 Gate로 추가하지 않는다.
**SEC MON5 완성 매핑은 미수신·연결 예정**([책임 #19](https://github.com/321Team/fds-project-baseline/issues/19), MON_PROBE_ORIGINAL_MAP_20261019_1223). 현재 FINAL_BINDING이 없으며 다른 Phase2 반환은 소비하지 않는다. Prometheus/Alertmanager/Grafana/KSM/node-exporter별 기존 실제 실패 전이→Endpoint 제외/복원 원본 또는 정확 미지정 범위를 연결해 이재환 MON 대응·이하영 SEC-AC06 판정으로 남긴다.
173 격리exec·177 정의/Ready·223 실제 engine HTTP는 기존 범위로 재사용한다. healthy/rollout은 실패 주입이 아니다. 전5종 재시험·startupProbe 신설·대표 시험 수를 미리 확정하지 않는다.
[증적 PR247](https://github.com/321Team/fds-project-evidence/pull/247), HEAD `46cc46da43ad1206821f3fa8a4d0807ee2913625`의 새 ICR 관리 Harbor GET은 curl28/HTTP000·연결0이다. source108 요청값을 실제 socket 관측으로 쓰거나 인증 RemoteWrite·postboot 정상 흐름·TLS 성공으로 확대하지 않는다.

## Owner 회신 빈양식 — 현재 미작성
- 검토자 / KST 시각 / 입력 버전: ______
- 미수행 날짜·사유 / 실제 수행한 경우의 시각·각 결과·#17 링크: ______
- 시연 직전 수행/미수행 기록(일정·접근 전제가 실제 있을 때): ______
- IF06B 수용 범위·정확 잔여 / SEC MON5 완성표 연결·미대응: ______
- MON 최종 판정·한계 / SEC에 연결할 원 요구: ______

