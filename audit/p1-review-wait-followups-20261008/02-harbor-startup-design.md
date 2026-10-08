# 2. Harbor 자동기동·원복 설계안

HBR Lead 이하영 결정용 초안. 이권욱은 연계 준비를 수행한다. CODEX_ASSISTED.
근거: [baseline13 원인](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-6042409217),
[PR12](https://github.com/321Team/infra-harbor-trivy/pull/12), [PR13](https://github.com/321Team/infra-harbor-trivy/pull/13).

## 고정 사실과 권고

원본 /home/server08/harbor/docker-compose.yml SHA256은 0a84f57692268335eeedf45411e025d784e520bf749fa3501a3800cdfcb14ef0.
앱9개 syslog localhost:1514, log publish127.0.0.1:1514→10514, 10개 restart:always다.
10/7 daemon 오류는 앱9개 [::1]:1514 연결 거부이며 logger 준비 시각과 IPv4 재시도 여부까지 확정하지 않는다.
PR12는 주소9개 외 정규화 구성 불변, PR13은 상태 관측이다. 둘만으로 자동기동 보장은 없다.

**권고:** 주소 보완 후보의 효과와 남는 logger 준비 경합을 먼저 격리 환경에서 분리 검증한 후 기동 주체 변경 여부를 결정한다.
현재 운영에 새로운 시작기를 추가하거나 restart 정책을 바꾸지 않는다.
이 권고는 추가 현장 시험 GO가 아니다. 현장 Docker restart 시험은 별도 창·복구 조건으로 한 번만 계획한다.

| 선택안 | 적용 조건/범위 | 잔여와 선택 판단 |
|---|---|---|
| A. Docker restart 정책 유지 + 명시적 주소 override | 기존 정책을 보존하며 IPv4 주소만 일치 | 최소 변경 후보. 준비 순서 보장 없음; race가 남으면 실패로 기록하고 해결 완료 선언 금지 |
| B. 단일 host 관리 주체로 기동/재시작 책임 이관 | logger·앱별 Docker restart와 중복하지 않는 전체 소유권 전환 설계 필요 | logger→앱 준비·종료·복구를 제어하나 영향 큼. daemon/host 재시작·앱 crash까지 재검증할 때 선택 |
| C. Compose service_healthy만 추가 | 명시적 Compose up 경로 보완 | daemon 자체 restart의 순서 보장 해법으로 선택하지 않음 |

Docker는 host process manager와 Docker restart 정책의 중복 사용을 경고한다.
Compose 준비 대기는 healthcheck 조건에 의존하며 explicit Compose 작업과 daemon 자체 restart는 구분해야 한다.
[Docker restart 정책](https://docs.docker.com/engine/containers/start-containers-automatically/),
[Compose 시작 순서](https://docs.docker.com/compose/how-tos/startup-order/).

## B안을 선택할 경우의 구현 계약 — 아직 미확정/미구현

1. PREFLIGHT: source/Compose/image·volume·port·UID·guard 원본 고정, exclusive 실행과 복구 경로 확인.
2. LOGGER_START: logger 시작 책임이 하나인지 확인. 이미 기동 중이면 identity 확인 후 관측으로 이동.
3. LOGGER_READY: health와 loopback listener를 보조조건으로 확인. 실제 무민감 표식 수신/저장 기준은 Lead가 확정한다.
4. APPS_START: 기존 복구 B의 순서를 참고하되 현재 의존성을 재확인하고 ID별 한정 시작. 정해진 deadline 초과 시 다음 단계 중단.
5. VERIFY: 앱별 health, Runner TLS, 데이터·guard·image/volume/port 불변과 실제 로그 수신을 각각 확인.
6. FAIL: 실패 위치·rc·상태를 보존. 무한 restart/recreate 루프 금지; 허용된 복구만 실행.

총 timeout/재시도 상한, health 미정의 처리, log 수신 판정, 알림 수신자, crash 이후 재기동 책임,
정상 stop과 daemon restart 구별 및 운영 maintenance 진입/해제는 **OPEN_INPUT**이다.
현재 PR13의 healthy+LISTEN을 LOGGER_READY 최종 성공으로 사용하지 않는다.

## 적용·재생성·원복 경계

| 단계 | 구체 확인/보존 | 중단·복구 |
|---|---|---|
| 적용 전 | source SHA, Compose 원문/hash·권한, 실제10개 ID/image/mount/port/restart, guard, DB 상태 및 복구 접근 | drift/백업·접근 미확인 STOP |
| 생성 원본 | prepare가 생성 Compose를 덮으므로 명시적 override 소비 경로를 모든 start/recreate 절차에 연결 | prepare 실행 자체를 수정 적용으로 간주하지 않음; 원복 시 override 소비 경로도 원래대로 |
| 구성 반영 | 로그 설정 반영에는 대상 객체 재생성 영향 검토 필요. 이미지/볼륨/포트/DB는 같은 것으로 고정 | 일괄 down -v, 볼륨/이미지 삭제, 자동 pull 금지. ID 변경을 예상 변경으로 명시 |
| 새 기준선 | 재생성 후 새 ID를 등록, 그 뒤 daemon 시험 전후 동일 ID 확인 | 재생성 전 ID와 restart 후 ID를 혼용 금지 |
| 실패 복구 | 같은 실행의 원본 Compose/override 소비 방식·정책 복귀, 보존 이미지/볼륨으로 대상만 복원 | 구 원본 주소는 알려진 실패 위험이 있어 소스 복귀만으로 가용성 회복 완료 아님 |
| 복구 확인 | 필요한 경우 유효성 재확인한 수동 복구 B, 앱/TLS/guard/실제 로그 수신 | 수동 복구 성공은 자동기동 PASS가 아님. 새 실행 자동 반복 금지 |

이 단계는 검토 가능한 설계 초안까지다. 실제 up/recreate/restart/update/install 명령은 실행하지 않았으며
기동 주체가 확정되기 전에는 운영 unit이나 restart policy diff를 작성·적용하지 않는다.
