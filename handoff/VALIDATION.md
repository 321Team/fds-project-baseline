# Work · Codex 공통 기준 도입 검증 — 2026-09-11

이 기록은 도입 후보의 로컬 검증이다. 독립 승인·main 병합·실제 Cloud 환경 설정·
교육장 Runtime 실행 완료를 뜻하지 않는다. 이 파일은 Kit에 포함하지 않아 Kit Hash의
자기참조를 피한다. 검토 대상 HEAD는 이 파일을 포함한 PR에서 확인한다.

| 검사 | 결과 | 근거/범위 |
|---|---|---|
| 기존 source 보존 | PASS | 원격 main 72599ae49342b0fb8dbd3d8ee60314afb9f907bb의 141개 blob와 로컬 SHA-1·SHA-256 일치; 기존 파일 diff 없음 |
| 공통 검증기·Kit 시험 | PASS | `python -m unittest discover -s tests -p 'test_shared_context.py' -v`, 14 tests |
| 발행본 무결성 | PASS, LOCAL | 기존 verify-canonical-release.sh, WBS/Gantt candidate 검사 포함 |
| 정본 ZIP 재생성 | PASS, LOCAL | 기존 builder로 v3.1.18 재생성; GitHub Release API가 제공한 ZIP SHA-256과 일치 |
| 인수인계 Kit 재현 | PASS, LOCAL | 16개 고정 입력 + Manifest, 두 ZIP의 SHA-256 동일 |
| 실제 GitHub 조회 사본 통합 검사 | PASS, SNAPSHOT_ONLY | 정상 연결된 Connector로 20개 API 경로를 조회; 공개 사양/승인/관련 상태 검증 |
| 오프라인 사본 실행 Gate 차단 | PASS | `check`가 SNAPSHOT_ONLY를 거절하고 exit 2 |
| gh live-mode 실행 | NOT_RUN | 현재 환경에 gh 없음; Fixture 시험을 실제 GitHub CLI 실행으로 표시하지 않음 |
| GitHub Actions | NOT_RUN at preparation | 이후 실제 Run URL/결론은 PR에서 별도 확인 |
| 사용자 Cloud 설정/세션 로딩 | UNVERIFIED | 사용자 계정의 Cloud 환경 설정 인터페이스에 접근하지 않음 |
| 교육장 Runtime | NOT_RUN | 실제 인프라 실행 없음 |
| 독립 REVIEW / MERGE | PENDING | 정확한 PR HEAD의 독립 검토·수동 병합 필요 |
| 성능 향상률 | NOT_MEASURED | 대표 3개 작업 비교 양식 준비; 수치 추정 없음 |

정본 ZIP SHA-256:
`a966bfef81adb0fba65b0d14e4f34c079fdaaaa5ca4888b802363160e21126f6`

인수인계 Kit SHA-256:
`3faf5ac95a54a69f6a3834921653e78a5cf7733977eafa73bf2f5876bb8c2c61`

GitHub 조회 완료 시각: `2026-09-11T03:46:06.043Z`.
SNAPSHOT_ONLY context_id:
`03e84272eb3075ae19800d89e58ac7dbe3f2af706cb40b7caa41bdab18097aa1`.
API 원문과 receipt는 개인/작업 데이터가 섞일 수 있어 배포 Kit와 Git 추적 대상에서 제외했다.
해당 context_id는 그 시점 Task의 관측 식별값이며 현재 상태 또는 승인 서명이 아니다.

시험은 Issue 본문/댓글, PR HEAD/Review, base HEAD, 새 Release/이동된 Tag/교체된 Asset,
배포 파일 변화, 검토 취소, 조회 중 변화, 페이지 누락, 인증 실패, 오래된 receipt,
변경된 Task, 잘못된 checkout, 허용 경로 밖 변경, Kit의 파일 변경/경로 탈출/중복/
symlink/출력 덮어쓰기를 차단하는 경우를 포함한다. 교육장 네트워크·서버 상태나
GitHub의 원자적 동시 편집 잠금은 시험/보장 범위가 아니다.

기존 CURRENT/README/UPSTREAM_LOCK의 과거 상태는 새 WORK_START에서 시점을 구분한다.
이 도입은 티켓 속성 동기화, PR #68 또는 기존 진행 PR의 상태 변경, Tag/Release 변경을 수행하지 않는다.
