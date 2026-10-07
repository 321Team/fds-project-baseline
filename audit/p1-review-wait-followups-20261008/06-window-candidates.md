# 6. 후속 작업창 후보·충돌 조건

CODEX_ASSISTED. **WINDOW=NOT_RESERVED**. 시각 도래나 오래된 idle 조회로 비중첩을 선언하지 않는다.
이 표는 새 일정·담당 배정이나 사용자의 다른 세션 실행을 중단시키는 명령이 아니다.

## 최신 충돌 입력

[SEC19 최신 기록6044114291](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-6044114291):
사용자가 기존10/10 제안보다 빠른 GWONUK Edge 전환을 지시했고, 실제 T0는 사전조건 후 고정한다.
edge01/server08 및 db01/server08 접근 확인이 준비돼 있으며 실제 인증/check/apply는 그 기록 시점 미실행이다.
따라서 과거의 “일정 결정 대기” 상태를 유지하지 않는다. 향후 변경은 실제 세션 기록을 다시 확인한다.
계획 관찰 C3 30분, T0+75분 전체상한/복구목표+90분은 해당 세션의 계획이며 새 창을 예약한 숫자가 아니다.

게시 직전 추가 확인: [6044215211](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-6044215211)에서
이전 대화형 인증 wrapper가 중단·철회되고 수정본은 MOCK3/3 후 현장 재확인 전으로 갱신됐다.
민감 입력 가능성이 있는 기존 출력은 해당 세션의 편입 제외 조치를 유지하며 여기서 조회/회수하지 않는다.
조기 실행 결정은 유지되지만 실제 인증/check/apply 완료로 취급하지 않는다. 이 세션은 인증 경로나 기존 wrapper를 실행하지 않는다.

| 후보 순서 | 작업/공유 자원 | 시작 조건 | 종료·복구 판정 |
|---|---|---|---|
| 지금 | 로컬 문서/입력 대조·GitHub CI(hosted) | 운영 호스트/Runner/클러스터 소비 없이 수행 | 결과/CI 기록, 다른 runtime 창 점유 없음 |
| 다음 짧은 후보 | worker02 DNS verify / ansible01·worker02·DNS/API | PR74 조건·정확한 입력·Edge 등 실제 종료/정리 확인 | 기존 timeout120초, rc/recap/상태·잔여 확인; 자동 재시도 없음 |
| HBR 입력 이후 | 새 Push / Runner·Harbor·Scan/저장소 | source/Robot/fresh 입력·승인·전용 창 | Push/원격 digest/credential 정리·Runner idle 확인 |
| Push 이후 | Deploy/Health/E2E/rollback / Runner·CP1·Workers·Harbor·APP/DB | 새 Push receipt, 최신 대상/원복·승인·비중첩 창 | result/journal/claim, 실제 APP/DB·Pod 상태 및 정리 확인 |
| 별도 영향 창 | Harbor 반영·재시작 시험 / Harbor·image Pull/Push 전체 | 설계/소스/백업·복구·중단 기준과 실행자 확정 | 서비스/TLS/guard·데이터·logger, 자동/수동 복구 구분 |

이는 조건부 권장 순서다. Harbor의 기존 가용성 위험을 수용할지 여부에 따라 Lead가
Push/Deploy보다 Harbor 수정을 먼저 배치할 수 있다. 현재 서비스 정상 여부도 실행 직전 재확인 대상이다.

## 창 확정용 입력 — 지금은 모두 미예약

- 해당 작업 source/Run/대상·실행자·연락/중단 책임, 시작시각과 실행/복구 상한.
- 선행 작업의 실제 END, 청소/복구 완료 및 기준선 정상 기록. 계획 END가 아니라 원본 결과 사용.
- 같은 Runner뿐 아니라 Harbor/Worker/API/DB/네트워크를 소비하는 수동 작업·다른 저장소 시험 확인.
- 작업별 기존 냉각/관찰 조건 적용. 과거 특정 창의 +10분을 전 작업의 새 공용 정책으로 확대하지 않음.
- 실패/연장 시 새 작업 시작을 막고 담당·잔여 상태 기록; 기존 시험 자동 재실행/취소 금지.

기존 10/8 00:05~03:30 APP 창은 종료 댓글로 이미 해제됐다. 이를 남은 시간의 새 Push/Deploy 허가로 재사용하지 않는다.
현재 Edge 조기 전환의 T0/정리 상태가 미확정이므로 서버 시험의 구체 시작시각을 이 표에 채우지 않았다.
