# 실제 HTTP Probe — 기존 성공 재사용과 남은 최소 범위

이권욱 / CODEX_ASSISTED · 2026-10-13 05:25 KST GitHub 원문 대조. [APP·HA 실행 카드](APP_HA_EXECUTION_CARD_20261013.md)의 잔여 Probe 항목을 좁힌 준비안이다. 새 Runtime 실행·AC 판정은 없다.

## 기존 증적을 유지할 범위

| 범위 | 확인한 원본과 실제 결과 | 이번 후속에서의 처리 |
|---|---|---|
| transaction-api DB 장애 | [증적66](https://github.com/321Team/fds-project-evidence/pull/66), merge `e5ed3e9ee094af2976dc491e401d0f8a106b5200`: 실제 HTTP503·Endpoint ready=false·liveness restart 변화 없음·복구 | 미실행으로 되돌리지 않는다. DB 전역 차단·DB 세션 종료를 Probe 공백 보완이라는 이유로 다시 필수화하지 않음 |
| FDS 장애 fail-open | [증적90](https://github.com/321Team/fds-project-evidence/pull/90), merge `18797bd1789d6ff90781dc242050538e89d709dc`: engine0 구간73초, API Ready200·HTTP201/skipped=true·DB 저장, 복구 후 skipped=false | [CR119 완료 결정](https://github.com/321Team/fds-project-baseline/issues/119)의 범위 유지. engine 전체0 재시험을 자동 추가하지 않음 |
| 격리 exec Probe | [증적173](https://github.com/321Team/fds-project-evidence/pull/173): 별도 Pod T0~T3·Endpoint 전이·restart0→1·UID 정리 | kubelet 기본 전이의 이미 확보한 증거. 실제 운영 이미지의 HTTP 실패 증거와 구분 |
| 실제6종 정의 | [증적177](https://github.com/321Team/fds-project-evidence/pull/177), merge `50f5742cde1ff19fbe607e6d9c4fb091f7ab338f`: Pod10 Ready, HTTP 정의·Endpoint 연결 | 상태/정의 관측으로 재사용. 누적 restart를 liveness 장애 성공으로 계산하지 않음 |
| 최종 후보 정상 listener | [APP27](https://github.com/321Team/fds-msa/pull/27), HEAD `affbc69beef9967f7977d09a6fec14f7fb6c0e94`: CI의 실제 앱 container TCP 검증·업무 metrics404/전용200 | 완료 CI를 반복하지 않음. 운영 경로·kubelet 실패/복구 결과로 확대하지 않음 |

중앙 [#19 현행 SEC-AC-06](https://github.com/321Team/fds-project-baseline/issues/19)은 격리 exec·정의/Ready를 이미 확보한 부분으로 유지하면서 실제 APP HTTP 등의 잔여 인수를 남긴다. 이 문서는 전체6종을 다시 실패시키거나 없는 startupProbe를 새 요구로 만들지 않는다. #119 완료를 #19 전체 완료로 확대하지도 않는다.

## 후보 변경 영향의 실제 대조

[정적 대조 결과](HTTP_PROBE_SOURCE_DELTA_20261013.json)는 APP27의 base `8eac4c982076e3c219840a13686b15c46879981f`→후보 `affbc69beef9967f7977d09a6fec14f7fb6c0e94`를 고정했다. [재현용 비교 코드](compare_http_probe_source.py)는 고정 Git blob을 읽고 AST/bytes만 대조하며 앱 함수를 실행하지 않는다.

- 두 앱의 `health`·`ready`·`evaluate`/`create_transaction` **6함수 AST 동일**. 본문에서 제거한 것은 업무 `/metrics` handler다.
- 두 `run.py`, transaction-api `db.py`·`fds_client.py` **4파일 bytes 동일**. listener 실행·DB 연결·FDS client의 해당 파일을 이번 PR이 바꾸지 않았다.
- 이 대조는 PR27 변경 영향에 한정한다.9/29·10/1 배포 바이너리 전체와 새 image의 동일성, dependency/image/환경의 동등성, Runtime 성공을 증명하지 않는다. 새 Push/Deploy receipt와 최종 형상·정상 회귀는 여전히 필요하다.

따라서 새 후보라는 이유만으로 DB 장애·engine 전체 정지·기존 exec시험을 모두 반복하는 안은 권하지 않는다. 실제 최종 image 또는 현장 동작이 해당 기존 경로와 달라졌다는 새 증거가 있으면 그 영향 행만 재검증한다.

## 권장 최소 후속: 실제 engine HTTP 한 사례를 먼저 구체화

기존6종 중 APP인 `fds-engine`의 **최종 image Pod1개**를 첫 후보로 권한다. DB 장애 시험으로 이미 관측한 transaction-api readiness와 구분해, 실제 engine HTTP 응답 불능→Ready/Endpoint 제외→kubelet liveness 재시작→복구의 원본을 얻는 범위다. 이 한 사례로 MON 나머지5종 또는 복합 AC 전체를 대표·완료 처리하지 않는다. 적용할 최소 범위와 잔여 인수의 대응은 기존 SEC/APP·MON 리뷰 범위에서 확인한다.

| 관측 단계 | 필요한 실제 증거 | 증거로 인정하지 않는 것 |
|---|---|---|
| 시작 | 최종 source/digest·Pod UID·containerID·node/boot·프로세스 식별, probe 설정, Ready/Endpoint true·restart 기준값 | 과거 Pod 이름·누적 restart값만 재사용 |
| readiness 실패 | 해당 HTTP probe 실패 원인, 같은 Pod Ready=false와 해당 Endpoint ready=false, 나머지 두 engine Ready 유지 | 프로세스가 이미 종료돼 자연 재시작된 결과를 HTTP 실패 주입으로 표시 |
| liveness 회수 | kubelet의 해당 UID/시각에 결속된 liveness failure·재시작 이벤트, 같은 Pod UID에서 containerID/restartCount 전이 | rollout/Eviction/강제 kill로 만든 재시작을 liveness 성공으로 표시 |
| 회복 | 같은 Pod의 실제 HTTP·Ready/Endpoint·engine3Ready, target 집합과 정상 업무 관측의 회복 | metadata 한 번의 Ready 또는 새 Pod로 대체된 상태만 확인 |

위 readiness·liveness 의미는 [Kubernetes1.36 공식 설명](https://v1-36.docs.kubernetes.io/docs/concepts/workloads/pods/probes/)과 대조했다. 실패 threshold와 grace는 조치 시점을 결정하지만 `period×threshold`만으로 실제 복귀의 절대 상한을 보장하지 않는다. 실행안에는 별도의 관측 중단·인수 기한이 필요하다.

### 실제 실행 전 남은 기술 입력

1. **정확한 주입·회수 경로:** 최종 container의 명령/프로세스 구성을 확인하고, 이전 Pod 이름이나 host PID가 교체됐을 때 다른 대상을 멈추거나 재개하지 않는 방식으로 고정한다. 현재는 프로세스 정지/재개 명령이나 새 실행기를 만들지 않았다. `kubectl exec` 전 GET 한 번만으로 검사 이후의 container 교체 경쟁이 없어졌다고 보지 않는다.
2. **중단·복구:** 주입은1개·1회, 나머지 engine2개 Ready 유지. 관측 불가·대상 교체·다른 앱/노드 이상·기한 초과면 다음 주입0회, 원본 보존 후 console 인수. 같은 container가 여전히 중단돼 있으면 그 정확한 대상을 재개하고, 이미 교체됐으면 과거 PID/새 container에 재개 명령을 보내지 않는다. 강제 삭제·권한/보안통제 완화는 자동 복구에 넣지 않는다.
3. **영향의 사전 합의:** 해당 engine의 업무8001과 metrics9090은 같은 프로세스다. 프로세스를 멈추는 방식을 선택하면 그 metrics도 끊기며, Endpoint 제외 전 일부 요청이 fail-open으로 저장될 수 있다. 업무 writer/회귀와 겹치지 않는 창, 그 의도한 영향 및 정확한 종료 기준을 새 회차 범위에 포함해야 한다. 기존 MON canary·새벽 Eviction 허용을 전용하지 않는다.
4. **최종 회귀와 순서:** 선택한 Probe 사례가 있다면 새 image Deploy/형상 확인 뒤 HA와는 별도 구간으로 수행하고, 서비스·MON·배치가 회복된 뒤 APP 거래 회귀를 마지막에 수행한다. Probe restart로 counter가 바뀐 구간과 회귀의 사전/사후 delta를 섞지 않는다.

이것은 실제 대상이 채워져야 명령·복귀를 확정할 수 있는 준비 항목이다. 새 image가 아직 배포되지 않은 상태에서 임의 container/PID를 채워 실행안을 READY로 표시하지 않는다. 현재 부족한 것은 또 하나의 포괄 승인이나 기존 코드 재리뷰가 아니라 **최종 대상·관측/회수 방법·한 회차의 영향/창**이다.

## 기록 상태

STATIC: 고정 source6함수·4파일 대조 완료. 기존 성공한 테스트는 재실행하지 않았다. RUNTIME(이번 heartbeat): 신규 서버 접속/파일 배치·exec·DB/서비스 변경·Probe fault0회. 이번 새 자료로 AC·Status·종결/위험수용을 바꾸지 않았다. 실제 실행이 필요해지면 위 입력을 채운 구체 카드의 한 번 검토로 모으며, 현재 대기 중인 Push 입력 검토의 추가 선행조건으로 넣지 않는다.
