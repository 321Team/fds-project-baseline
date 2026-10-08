# Phase 1 리뷰 대기 중 후속 준비 — 2026-10-08

CODEX_ASSISTED. 사용자 이권욱의 여섯 후속 항목 착수 요청에 따른 **검토용 준비 자료**다.
정본은 CURRENT.md의 v3.1.21을 유지한다. 이 폴더는 실행 승인·정본 발행·Runtime 증적·AC 인수가 아니다.
조회 기준 시각과 PR HEAD는 [source-snapshot.json](source-snapshot.json)에 있다.
기존 리뷰 대상 브랜치·증적 원본은 수정하지 않았다. 새 코드/서비스/Runner/Secret 변경도 없다.

| 순서 | 실제 수행 | 산출물 | 남은 결정/실행 |
|---|---|---|---|
| 1 | PR147 APP 증적42파일 Git blob 동일성, PR65 입력26항목 대조 | [입력 대조](01-push-inputs.md), [결과 JSON](push-input-comparison.json) | 현재 HEAD 병합 판단은 리뷰 세션. 새 Push는 별도 조건 |
| 2 | 기존 오류·관리 원본·Docker 기준으로 주소/기동 책임/원복 분리 설계 | [Harbor 설계안](02-harbor-startup-design.md) | HBR Lead 기동 방식/timeout/영향 결정, 필요 소스 구현 |
| 3 | PR66/67 실제 계약의 필드4집합과 소비·생산 책임 연결 | [Deploy 입력안](03-deploy-preparation.md), [비실행 worksheet](deploy-input-worksheet.json) | 실제 Push receipt·최신 대상/원복·승인·작업창 |
| 4 | 구 운영 checkout/후보 엔진의 진입점·단계별 전환/복구 정리 | [Ansible 전환안](04-ansible-transition.md) | PR74 검토 후 제한된 DNS verify, role별 검증·전환 결정 |
| 5 | 소스·시험·증적·잔여를 구분한 문서 연결표 작성 | [증적 연결](05-evidence-index.md) | 독립 리뷰·편입·최종 인수. Freeze 미실행 |
| 6 | 조기 Edge 전환 최신 기록 반영, 충돌 자원·해제 조건 정리 | [작업창 후보](06-window-candidates.md) | 실제 T0/종료·정리와 담당자의 창 확정 |

## 검증·재현

입력 대조는 GitHub의 지정 commit tree와 blob을 조회하고 blob SHA1·tar SHA256 및
tar 내부 JSON 원문 SHA256을 대조했다. 결과 JSON에 전후 HEAD, 파일별 blob, 각 비교 결과가 있다.
원문 archive는 [지정 증적 HEAD](https://github.com/321Team/fds-project-evidence/tree/dbc5ce9ca5fa097b6016fcf989c8985ab19288be/evidence/P1-CICD-01/app-adc90410-run37642123031-20261008)에 보존한다.
계획 worksheet는 운영 입력 schema와 다르며 소비 코드에 전달하지 않는다.
필드 집합은 PR67의 deploy_plan.py에서 추출했고, 실제 승인 JSON이나 Push receipt를 합성하지 않았다.
SHA256SUMS는 이 폴더 문서/JSON의 바이트 검사용이며 인수 성공을 뜻하지 않는다.

이번 변경의 검증은 문서 링크·JSON·manifest·Git diff 정합성이다. 기존 프로그램 시험을 재실행하거나
이 폴더의 문서 검사를 새로운 Runtime/Deploy PASS로 집계하지 않는다.
현재 전체 진행 상태는 PREPARATION_COMPLETE_WITH_OPEN_INPUTS이며 운영 실행은 NOT_RUN이다.
