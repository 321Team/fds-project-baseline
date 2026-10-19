# K8S·Ansible·SEC — 새 NTP 증적과 원 AC 판단 입력
대상 Owner: **이하영(K8S/SEC Lead·Ansible 기존 검토자)**. 기준 baseline main `acc513cf5c9f3e07e58d818a18e4b8fcf1e0cf70`의 [원 K8S](https://github.com/321Team/fds-project-baseline/blob/acc513cf5c9f3e07e58d818a18e4b8fcf1e0cf70/tickets/v3.1.21/descriptions/P1-K8S-01.md)·[원 SEC Description](https://github.com/321Team/fds-project-baseline/blob/acc513cf5c9f3e07e58d818a18e4b8fcf1e0cf70/tickets/v3.1.21/descriptions/P1-SEC-01.md). **추가 Owner 회신·전체 인수 미작성**.

## 새 검토 대상 — NTP 정상6회 별도 증적
[PR247](https://github.com/321Team/fds-project-evidence/pull/247), 정확 HEAD `46cc46da43ad1206821f3fa8a4d0807ee2913625`, 이하영 formal review 요청 완료. NTP50+ICR17 파일·대장2행이며 이 문서는 새 NTP 정상6회 검토를 PR246과 구분한다.
정확 경로: [ntp-normal-series-20261019](https://github.com/321Team/fds-project-evidence/tree/46cc46da43ad1206821f3fa8a4d0807ee2913625/evidence/P1-K8S-01/ntp-normal-series-20261019). README·CENTRAL_READBACK·실제 source·원본/회차 입력·hash 목록을 소비한다. 회차 stdin은 실행 전 캡처가 아니라 동결 source·시각 영수증으로 사후 재구성해 actual dispatch SHA 일치를 대조한 자료다.
[확정 결정5697547621](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5697547621): offset≤100ms·60초간격6회, sync lost≥5분 FAIL·reboot 후5분 이내 재동기화. Description 보관 원문의 미승인 초안 표현보다 확정 결정·Baseline 현행 절을 우선한다.
10/19 **12:29:56~12:34:56 KST**,6대×6=36관측·chronyc72명령 rc0,host/machine/boot 유지. 노드별 간격60초 이상·span300.002954~300.004243초,Leap 전부Normal,최대|last_offset|0.40177ms·|system_time|0.155312ms. CP1은162.159.200.1,나머지5대는10.1.93.102 선택을 관측했다.
검토 범위는 **정상6회·현재 source·시계/원본 결속**이다. sync-loss/reboot NOT_TESTED·현행 egress/HEP/GNP 전체 승인 및 NTP 전체 AC 미확정을 유지한다. 이 두 원 조건은 기존 원본·처분과 대응한 뒤 정확 잔여만 판단하며 새 장애/재부팅을 자동 배정하지 않는다.

## 반복 확인 제외
- [PR246 정확 f51505cf6f6fe64aed2c22b5293bf39f9a1a0f0d의 APPROVED](https://github.com/321Team/fds-project-evidence/pull/246#pullrequestreview-5566591282)·CI1SUCCESS와 [중앙 소비6259177726](https://github.com/321Team/fds-project-evidence/pull/246#issuecomment-6259177726)를 재사용한다. 공유17 재열람·동일 승인·같은 byte 검사는 추가 회신 대상이 아니다. 리뷰 시각 표기 보완은 중앙의 별도 요청이며 재열람 Gate가 아니다. PR246 병합·#9 전체 인수를 이 문서로 판정하지 않는다.
- Ansible 역할185·PR87/243/244·paired6·OS-DNS·수동 caller09:46 채택·11:20 한정 metadata를 재사용. 전체 loader/.pth 미실행·미식별 외부/동적 caller 한계는 유지한다. 정상6회만으로 #9 종결·모든 caller 전환·전역 PATH/RPM 변경을 완료 처리하지 않는다.
- SEC-AC05 encryption/control03 rollback/격리 backup 하위MET·rotation NOT_MET/RISK_ACCEPTED·전체[ ]·한정 비차단 처분은 재승인 제외. Worker23 원본2개 사용자 보호보관·Grafana 없음·#25~27 인계기록 수신3완료도 재확인하지 않는다.

## SEC-AC04/06 — 기존 증적 판정 범위만 연결
| 원 요구 | 재사용·남은 판단 |
|---|---|
| AC04 named HEP/expectedIPs·preDNAT·canary/복구·승인/비승인 경로 | [144](https://github.com/321Team/fds-project-evidence/pull/144)의 첫 방식B Positive3/Negative9·[관측 수용6040616297](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-6040616297),#86 source-preservation·#99 유효 범위·현재 NodePort3 HTTP200을 대응. 실제 Source·Negative는 유지하고 특정 규칙 유일 귀속을 새 Gate로 추가하지 않음 |
| AC04 부팅 | CP3 기존 수용과 Worker3 10/16 조건부 수용을 분리 재사용. EARLY 직접 미측정/기술 한계를 steady-state 정상으로 대체하지 않음 |
| AC06 Probe/Endpoint 제외 | [173](https://github.com/321Team/fds-project-evidence/pull/173) 격리exec·[177](https://github.com/321Team/fds-project-evidence/pull/177) 정의/Ready·[223](https://github.com/321Team/fds-project-evidence/pull/223) engine HTTP 기존 범위 유지. MON5 완성표 미수신·연결 예정([MON 입력](02_MON_D02_IF06B_REVIEW.md)). healthy/재배치를 실패 주입으로 쓰지 않음 |
| 최종 경계 | [현재 #19](https://github.com/321Team/fds-project-baseline/issues/19)의 원 요구·미충족·기존 인수 유지. 추가 작업 필요 시 정확 부족 원 요구를 먼저 지정. 전체 NOT_RUN 환원·전수 Negative·전5종 재시험·새 Support 서명·Phase2 실행 추가 없음 |

## Owner 회신 빈양식 — 현재 미작성
- 검토자 / KST 시각 / NTP PR·정확 HEAD: ______
- 정상6회 판정·사후재구성 한계 / sync-loss·reboot 기존 자료 처분·정확 잔여: ______
- SEC-AC04 인수 범위·남는 원 요구·근거: ______
- SEC-AC06/MON5 완성표 연결·인수 범위·남는 원 요구: ______
- #9 선택 운영 범위·유지할 한계(수동 caller 채택 재승인 제외): ______

문서는 검토 입력이며 새 서버 조치·시험·실제 Owner 판단·AC/Status 상향·새 일정을 부여하지 않는다.

