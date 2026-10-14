# O01 1차 세션 — AC07 원본 탐색과 오프라인 재현

2026-10-15 KST · CODEX_ASSISTED. 문서 Lead/자료 제공·결과 수신 이권욱. 수행 우선 후보 이재환, 보안 검토 지원 이하영. 실제 참여·시간과 AC07 작성/실행 직접 관여 여부는 미확인이다. 후보 수락 및 해당 대상의 제3자 요건을 확인한 뒤 수행자로 확정한다. 본 문서의 작성자 자체 점검을 그 사람의 실적으로 기입하지 않는다.

## 대상과 상태

- 입력 저장소: 321Team/fds-project-evidence.
- 고정 checkout: `43e26384ae422f2017f1e96e6c1bb5fe46d087d4`.
- 대상 폴더: `evidence/P1-CICD-01/ac07-native-runtime-20261014`.
- Manifest SHA256: `8ef7fa2bbadae05a526cd9890dd69d16915f227c7d549d883513996a0a22bfb2`.
- [증적231](https://github.com/321Team/fds-project-evidence/pull/231)은 [이하영의 증적 편입 승인](https://github.com/321Team/fds-project-evidence/pull/231#pullrequestreview-5518576437) 후 merge `72375108ec743455ae49c68b1398d211dcc1b669`로 병합됐다.
- [AC07 인수 결정](https://github.com/321Team/fds-project-baseline/issues/16#issuecomment-6171164664)은 별도 기록이다. 고정 README와 verifier가 출력하는 `RUNTIME_OBSERVED_EVIDENCE_REVIEW_PENDING`은 당시 상태다. 원본을 고치지 않고 이 후속 기록을 함께 읽는다.
- 1차 범위: 원본 경로 탐색 → 기존 판정기 로컬 실행 → Runbook의 대상·선행·중단·회수 설명 점검. 새 Runtime 및 전체 O01 인수는 별도다.

## 환경과 자료 전달

개인 검토 PC, 일반 사용자, Git와 Python 3.10 이상(표준 라이브러리만)을 사용한다. 서버 계정·kubeconfig·토큰은 필요하지 않다. 기존 저장소 권한으로 **새 검토 디렉터리**를 만들거나 이권욱이 제공한 고정 checkout을 사용한다. VM에 코드를 붙여 넣거나 서버로 접속하지 않는다.

새 폴더에 받을 때만 실행한다. 같은 이름의 기존 폴더가 있으면 다른 새 경로를 선택한다.

```text
git clone --no-checkout https://github.com/321Team/fds-project-evidence.git fds-evidence-o01-ac07
git -C fds-evidence-o01-ac07 config core.longpaths true
git -C fds-evidence-o01-ac07 checkout --detach 43e26384ae422f2017f1e96e6c1bb5fe46d087d4
```

각 명령이 실패하면 이후 명령을 실행하지 않는다. Windows는 짧은 디렉터리를 사용한다. 기존 폴더를 reset/clean하지 않는다. 전달된 복사본이면 Git HEAD, 대상 파일 누락/변경, Manifest를 먼저 대조하고 오류 시 제공자에게 돌려보낸다.

## 진행 순서와 정상 판정

30~45분은 준비 추정이다. 확인된 시작·종료 KST와 실제 소요 시간을 기록한다.

1. **입력 확인(약5분):** [결과 양식](O01_RESULT_TEMPLATE.md)을 증적 저장소 바깥의 새 결과 폴더로 복사한다. 수행자·사전 관여 여부·OS·Python·입력 SHA를 기록한다. 저장소 루트에서 아래 명령을 각각 실행한다.
   ```text
   git rev-parse HEAD
   git status --porcelain -- evidence/P1-CICD-01/ac07-native-runtime-20261014
   python --version
   ```
   HEAD가 고정 SHA이고 대상 status 출력이 비어 있어야 한다. 모든 종료 코드가0인지 확인한다.

2. **원본 탐색(약10분):** README의 순서를 따라 아래 항목에 대응하는 실제 파일과 설명을 결과 양식에 남긴다. 답만 복사하지 않고 원본을 직접 열어 확인한다.

   | 설명할 내용 | 원본 진입점(대상 폴더 기준) |
   |---|---|
   | 명령·시각·종료 코드 | `raw/native-execute.receipt.json` |
   | 실제 권한25건·GET2·한계 | `raw/native-execute.stdout` |
   | 코드8개·리뷰·병합 결속 | `raw/SOURCE_BINDING.json`, `references/pr82-reviews.json` |
   | 실패 수집과 성공 재조회 구분 | `raw/rbac-before/`, `raw/rbac-before-r2/` |
   | 앱·RBAC 전후와 회수 | `raw/POSTCHECK_SUMMARY.json`, `raw/cleanup-*`, `raw/WINDOW_RELEASE.json` |

3. **오프라인 판독(약5분):** `verify.py`와 이 파일이 읽는 `references/compare_scan_observations.py`를 확인한 뒤 저장소 루트에서 실행한다. `raw/*.py`는 실행하지 않는다.
   ```text
   python -I -B evidence/P1-CICD-01/ac07-native-runtime-20261014/verify.py
   ```
   stdout/stderr·종료 코드·실행 전후 KST를 별도 결과 폴더에 보존한다. PowerShell에서는 명령 직후 `$LASTEXITCODE`, POSIX shell에서는 `$?`를 기록한다. 정상은 rc0, `OFFLINE_CONSISTENCY=PASS`, manifest116·receipt20·source8·SSAR25(allow6/deny19)·GET2다. 출력의 과거 REVIEW_PENDING은 위 최신 승인/인수 기록과 함께 설명한다.

4. **Runbook 판독(약10분):** 기존 실제 대상 ansible01→control01/runner, source/CA/SA 결속, 1회 발급·비중첩 창·실패 중단·회수·점유 해제·AC08 미실행 경계를 원본에서 찾아 설명한다. 당시 명령/만료 시각은 이력이며 새 실행에 재사용하지 않는다. 권한 질의와 금지 행위 직접 실행을 구분한다.

5. **결과 제출(약5분):** 종료 후 대상 status가 계속 비어 있는지 확인하고 원본 로그·양식·문서 결함을 이권욱에게 인계한다. 인수 기록은 [DOC #24](https://github.com/321Team/fds-project-baseline/issues/24)에 실제 범위와 함께 연결한다.

## 중단·복구와 다음 단계

SHA/해시 불일치, 파일 누락, verifier rc≠0, 비밀 노출 가능성, 문서만으로 판단할 수 없는 명령이 있으면 해당 단계에서 중단한다. 로그를 보존하고 원본을 수정하거나 서버 재실행으로 대체하지 않는다. 로컬 판독만 수행하므로 서버 복구 작업은 없다. 잘못 생성한 결과도 자동 삭제·덮어쓰지 않고 별도 재회차로 남긴다.

원본 탐색과 오프라인 판독 성공은 **이번 세션 범위의 결과**다. [P1-DOC-01 AC](https://github.com/321Team/fds-project-baseline/blob/368e3595e4ca608c504a9557b750a5ce8439fab3/tickets/v3.1.21/descriptions/P1-DOC-01.md)의 핵심 Runbook 재현 전체·Critical 문서 결함0·Freeze를 자동 충족하지 않는다. 이권욱은 실제 결과를 기준으로 아직 재현하지 않은 핵심 범위와 문서 결함 처분을 정하고, 다음 대상 Probe223 또는 필요한 현장 범위를 별도로 고정한다.

