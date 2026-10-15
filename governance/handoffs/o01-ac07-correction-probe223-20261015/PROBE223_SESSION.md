# O01 후속 후보 — Probe223 원본 탐색과 오프라인 판독

2026-10-15 KST · 자료 준비·결과 검수 이권욱 · CODEX_ASSISTED. 이재환이 10:37:44~10:39:05 KST에 기존 참여자 재확인으로 수행한 결과를 수신·검토했다. 아래 절차는 해당 회차의 판독 기준이며, 후속 서버 작업이나 새 장애 주입 승인이 아니다.

## 목적과 입력

AC07과 다른 실패·회복 사례에서 제3자가 Runbook의 경로·근거·한계를 설명할 수 있는지 확인한다. 대상은 [Probe223 고정 증적](https://github.com/321Team/fds-project-evidence/tree/43e26384ae422f2017f1e96e6c1bb5fe46d087d4/evidence/P1-K8S-01/http-probe-runtime-20261014T0950)이다. 과거 실제 장애를 로컬 자료로 판독하는 세션이며 새 장애를 재현하는 작업이 아니다.

- 저장소 / 고정 checkout: fds-project-evidence / `43e26384ae422f2017f1e96e6c1bb5fe46d087d4`.
- 폴더: `evidence/P1-K8S-01/http-probe-runtime-20261014T0950`.
- Manifest SHA256: `46d41a1a733caec603209280f4277e3f41592070d14f47ecd6f030fb4b08e8fe`.
- 원본108파일 + SHA256SUMS = 총109파일.
- 실행 코드: [K8S PR86](https://github.com/321Team/infra-kubernetes/pull/86), 검토 HEAD `d53ce00f318785b97577d41c07d8309ff581c2a8`, merge `e60e022333a51a9a1690649ef170c0bda92ad9b9`.
- 증적: [PR223](https://github.com/321Team/fds-project-evidence/pull/223), 검토 HEAD `e2d6d5aa4a09bec034ecfe33171ea1a2fe608adc`, [이재환 승인](https://github.com/321Team/fds-project-evidence/pull/223#pullrequestreview-5511991541), merge `ddd1e38c1c07d7d0dd99281df8e619c317db764b`.

이재환은 코드·증적 리뷰에서 판정기를 이미 실행했다. 그 사람이 다시 수행하면 기존 참여 이력과 재확인 성격을 명시한다. 다른 후보는 코드 작성·실행·리뷰 관여 범위를 본인이 확인하고 참여 수락 후 시작한다. 이는 새 AC/결격 정책을 만들기 위한 조건이 아니라 실제 재현 이력을 정확히 구분하기 위한 기록이다.

## 환경과 순서

개인 검토 PC의 일반 사용자, Git, Python3.10 이상(표준 라이브러리), 고정 checkout을 사용한다. 서버 계정·SSH·kubectl·토큰·kubeconfig는 필요하지 않다. 예상30~45분은 준비 추정이며 일정 확정이 아니다.

1. **기존 입력 재사용:** AC07에서 사용한 checkout이 있으면 새 clone 없이 HEAD와 대상 상태를 확인한다. 없으면 PR174의 새 checkout 안내를 이용한다. reset/clean으로 기존 작업을 지우지 않는다.
2. 저장소 루트에서 아래 명령을 각각 실행하고 명령·rc·원본 출력을 새 결과 폴더에 보존한다. 결과 폴더는 저장소 밖에서 새로 만든다.
   ```text
   git rev-parse HEAD
   git status --porcelain -- evidence/P1-K8S-01/http-probe-runtime-20261014T0950
   python --version
   ```
   HEAD는 위40자리 SHA, status는 빈 출력, 각 rc는0이어야 한다. Windows에서는 다음으로 Manifest 해시도 확인한다.
   ```powershell
   Get-FileHash -Algorithm SHA256 -LiteralPath evidence/P1-K8S-01/http-probe-runtime-20261014T0950/SHA256SUMS
   ```
   `verify_result.py`는 Manifest 전체 검사를 하지 않는다. 입력 HEAD·Git 상태·Manifest 해시 확인을 생략하지 않는다. Git 추적이 없는 복사본이면 이 절차로 확인 완료 처리하지 말고 제공자에게 고정 입력 검증을 요청한다.
3. README와 아래 원본을 직접 열어 결과 양식에 실제 경로·필드·설명을 적는다. 작성자 사전검증 답을 복사해 수행 결과로 쓰지 않는다.

   | 설명할 내용 | 원본 진입점 |
   |---|---|
   | 실행 계정·명령·시각·rc | apply-once/receipt.json, remote-originals/input.json, remote-originals/events.jsonl |
   | STOP1·CONT0과 원 프로세스 종료 | remote-originals/events.jsonl, remote-originals/engine_stop.py(열람만) |
   | Ready/Endpoint·liveness·동일 Pod 재시작 | observer.jsonl, app-state/stdout.json, final-app-state/stdout.json |
   | 실패 관측과 회복 보충 | worker-http.receipt.json, worker-http.stderr, worker-http.jsonl, http-recovery/stdout.json |
   | MON·영향 범위·회복 | mon-during/stdout.json, mon-stable/stdout.json, recovery-edge/stdout.json |
   | 실행기 공급·수신 바이트와 리뷰 | remote-originals-receipt/stdout.json, GITHUB_MERGE_REVIEW_RECEIPT.json, 위 PR86·223 |

4. `verify_result.py` 전체와 의존성을 읽는다. 이 파일은 표준 라이브러리로 기존 파일만 읽고 stdout을 출력한다. 저장소 루트에서 아래 **검증기만** 실행한다.
   ```text
   python -I -B evidence/P1-K8S-01/http-probe-runtime-20261014T0950/verify_result.py evidence/P1-K8S-01/http-probe-runtime-20261014T0950
   ```
   실행 전후 KST, 명령 직후 종료 코드, stdout/stderr를 저장한다. PowerShell에서는 `$LASTEXITCODE`, POSIX에서는 `$?`를 다음 명령 전에 기록한다. `apply_once.py`, `verify_and_stage.py`, `engine_stop.py` 및 관측·서버 수집기는 실행하지 않는다.
5. 정상은 rc0, stderr없음, `HTTP_PROBE_RUNTIME_PASS_WITH_RECORDED_OBSERVATION_LIMITS`다. STOP1·CONT0, 같은 Pod UID·restart1, 비대상restart0, 관측300·오류0, HTTP/MON60초 회복을 한계와 함께 설명한다. 이 출력의 RUNTIME은 과거 사건의 판독 결과이며 이번 세션은 OFFLINE이다.
6. 아래 한계를 설명하고 종료 후 대상 git status가 계속 비어 있는지 확인한다. [결과 양식](PROBE223_RESULT_TEMPLATE.md)에 실제 값·문서 결함을 기록해 이권욱에게 인계한다.

## 판독 시 유지할 한계

- control01 직접 Pod HTTP는 주입 전부터 timeout이었으므로 장애 성공의 근거로 쓰지 않는다. worker02 실제 HTTP와 control01 API 관측을 구분한다.
- worker HTTP/process 수집기는 원 PID 종료 경쟁으로 rc1을 기록했다. 실패 원본을 보존하고 별도60초 회복 관측을 읽는다. 실제 HTTP 최초 회복 시각은 확정하지 않는다.
- kubelet journal은 No entries다. 원인 연결은 같은 Pod UID의 Kubernetes liveness/Killing 이벤트를 근거로 한다.
- 관측기·회복 보충은 당시 pure observer 범위이고 독립 코드 리뷰가 수행됐다고 바꾸지 않는다.
- 고정 출력의 evidence review PENDING은 PR223 승인·병합 이전 값이다. final_APP/DB/W4 등은 해당 회차 당시 범위다. 최신 타 티켓 상태나 최종 인수로 확대하지 않는다.


## 시각 기준과 호스트 간 비교 한계

2026-10-15 재확인에서 제기한 경미 후보 P1의 판독 보완이다. 아래 값은 evidence `43e26384`의 봉인 원본을 그대로 읽었다.

| 기록 | 원본 시각 | 기준·해석 |
|---|---|---|
| `apply-once/receipt.json`의 `finished_at_kst` | 2026-10-14 09:52:03.669644+09:00 | Windows 조정측의 SSH 호출 수신 완료 기록으로 해석. `route`의 ansible01은 SSH 중계 경로이며 시계 출처를 뜻하지 않음 |
| `remote-originals/events.jsonl`의 `ORIGINAL_EXIT_OBSERVED_NOT_PROBE_PASS` | 2026-10-14 00:52:04.267843+00:00 (09:52:04.267843 KST) | worker02 실행기가 원 PID 종료를 관측한 기록 |
| 두 값의 차이 | worker02 이벤트 − receipt 종료 = +0.598199초 | 서로 다른 시계의 표시값 차이. 실제 인과 순서·전송 지연·정확한 clock offset으로 해석하지 않음 |

receipt 원본의 `command`는 `C:/Windows/System32/OpenSSH/ssh.exe`이고, 기존 로컬 `read_transport.py`의 `datetime.now(...)`는 outer SSH 호출 전후에 실행된다. 따라서 제출 양식의 “ansible01 기록”은 조정 PC 측 receipt와 구분해야 한다. 검토에 사용한 로컬 보조 소스의 경로·SHA256은 SOURCE_INDEX에 기록했다. 이 보조 소스는 Probe223 봉인 Manifest에 결속된 파일이 아니다. 현재 남아있는 수집 구조를 설명하는 보조 자료이며, 이 해시만으로 당시 실행된 보조 소스와의 바이트 동일성을 입증하지 않는다. 정확한 조정 PC 식별과 당시 양측 동기화 상태·오차 상한은 이 자료에서 확정하지 않는다. `cluster/stdout.json`의 control01과 `edge/stdout.json`·`recovery-edge/stdout.json`의 edge01 chrony 기록은 존재하지만, 비교 대상인 Windows 조정 PC와 worker02의 동시점 오차를 입증하는 자료는 아니다.

“호스트 간 초 단위 오차가 있다”는 확정 문구나 임의의 허용 오차를 추가하지 않는다. 시계 차이는 가능한 설명이며 원인은 미확인이다. UTC↔KST 변환만으로 호스트 시계 차이가 보정되지는 않는다. 원본 시각·Manifest는 그대로 보존한다.

같은 worker02 실행기의 `STOP_SENT` → `ORIGINAL_EXIT_OBSERVED_NOT_PROBE_PASS` 간 차이는 wall clock 81.785631초, monotonic 약81.785639초다. 기록 순서와 같은 호스트의 경과값을 함께 읽을 수 있지만 이를 다른 호스트 시각의 동기화 증거로 확대하지 않는다.

기존 verifier는 apply-once receipt의 rc를 검사하지만 receipt 종료와 worker02 종료 이벤트의 선후를 비교하지 않는다. 수신 verifier 출력은 고정 입력의 기존 오프라인 판정과 일치한다. 따라서 이번 문서 보완은 해당 범위의 결과 접수를 차단하지 않으며, 전역 정밀 시각 정합성이 검증됐다는 뜻도 아니다. 정확한 호스트 간 선후·지연을 요구하는 별도 검증이 필요하면 동시점 동기화/offset 증적부터 확보해야 한다. 현재 서버 시계를 조회해 과거 상태를 소급 입증하거나, 이번 판독을 이유로 장애를 재주입하지 않는다.

## 중단·복구와 완료 범위

SHA/Manifest 불일치, 파일 누락·변경, verifier rc≠0, 비밀값 노출 우려, 설명할 수 없는 명령이 있으면 중단하고 실패 원본을 보존한다. 원본을 고치거나 새 서버 시험으로 대체하지 않는다. 로컬 읽기만 수행하므로 서버 복구는 없다. 결과 파일을 잘못 만들었으면 기존 것을 덮어쓰지 않고 새 결과 회차로 다시 남긴다.

이 세션 결과가 정상이어도 핵심 현장 검증 전체·O01 전체 인수·Critical 문서 결함0·DOC Freeze는 별도다. 작성자 사전검증과 실제 수행자 결과를 분리한다.
