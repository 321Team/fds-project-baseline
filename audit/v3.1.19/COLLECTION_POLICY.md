# v19 변경 수집 절차

## 대상과 권한

사용자는 v19 Draft PR 생성과 변경의 지속 수집을 요청했다. 수집 쓰기는 이 PR 브랜치의 `audit/v3.1.19/` 및 준비 중인 v19 후보 파일에 한정한다. 이 권한으로 main push, 기존 Release/태그/Asset 수정, 운영 티켓 자동 변경, PR 자동 병합·발행 또는 새 자동화를 수행하지 않는다.

GitHub의 fds-project-baseline 티켓·댓글·Decision/CR·PR #72 및 연결된 프로젝트 저장소(fds-project-evidence, infra-ansible, infra-kubernetes, infra-cicd, infra-harbor-trivy, infra-db)를 확인한다. baseline 자체의 수집 PR 업데이트는 새 소스 변경으로 다시 수집하지 않는다. 추가 저장소는 프로젝트의 명시적 연결 근거가 있을 때만 포함한다.

## 변경 감지 및 기록

1. 최초 snapshot과 가장 최근 `intake/updates/`의 출처 ID·updated_at·HEAD SHA·검토 ID·내용 해시를 기준으로 비교한다. 페이지네이션을 끝까지 처리한다.
2. 티켓 본문 변경뿐 아니라 신규 댓글·리뷰·Commit·병합도 확인한다. 소스 저장소의 default branch Commit도 검사해 PR 없는 승인 이력을 놓치지 않는다.
3. 원문 URL, 수집 시각, Record ID, 변경 전후 값, 승인자·승인 대상 HEAD·Merge Commit, 증적 경로/해시, 영향 산출물과 상태를 기록한다. 비밀 원문은 복제하지 않고 발견 위치와 차단 사유만 남긴다.
4. 승인·병합·사용자 지시가 확인된 범위는 APPROVED_INPUT, 제안·미승인·증적 미검증은 PENDING_REVIEW로 구분한다. 병합만으로 Runtime PASS 또는 Gate 승인을 만들지 않는다. 과거에 이미 v18에 반영된 자료를 신규 변경으로 중복 편입하지 않는다.
5. 실질 변경이 있을 때만 `intake/updates/<UTC timestamp>.json`과 필요한 요약을 추가한다. 수집 시각만 달라졌다는 이유로 Commit을 만들지 않는다. 부분 조회 실패는 수집 누락으로 기록하며 미존재·완료로 추정하지 않는다.
6. 기존 branch HEAD를 읽고 비강제 fast-forward로만 갱신한다. 사람이 변경한 파일은 보존하고 경합 시 재조회한다. 수집 파일 SHA-256 목록을 갱신하고 원격 바이트/Commit을 재검증한다.
7. PR 본문에는 최근 수집 시각, 승인 입력·검토 대기·발행 차단과 소스 링크를 간결하게 갱신한다. 의미 있는 변경·차단이 있을 때만 사용자에게 알리고 반복 통지는 피한다.

## 발행 준비와 종료

v19 전체 묶음의 Baseline·WBS/Gantt·WEB·Ticket Pack·Interface/Decision/CR·Release Notes·Manifest·SHA-256을 정합 검증한 뒤 최종 HEAD의 독립 리뷰를 받는다. 병합·발행은 별도 사용자 지시가 필요하다.

실제 docs-v3.1.19 Release 발행과 CURRENT 적용을 확인하면 수집을 종료하고 해당 자동화를 비활성화한다. 수집 PR이 병합·폐쇄됐으나 v19가 미발행이면 닫힌 브랜치에 쓰거나 새 PR을 만들지 말고 사용자에게 다음 수집 위치가 필요함을 알린다.
