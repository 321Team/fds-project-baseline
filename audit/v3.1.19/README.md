# v3.1.19 통합 후보

상태: CONTENT_APPROVED_MERGED / FINALIZATION_REVIEW_PENDING / NOT_PUBLISHED.
리뷰어: 이하영 (`hayeounglee`). 내용 PR #73 승인·병합 완료. 최종화 HEAD 독립 승인이 필요하다.
운영 정본: 실제 발행 v3.1.18 (2026-09-11 11:23:47 KST).

67개 티켓/Description, 67개 대표 Milestone, 58개 WBS/Gantt 일정관리 레코드를 통합했다. 계획은 유연한 목표이며 AC·Runtime·Gate 상태를 임의 상향하지 않았다.

- `integration/source-index.json`: 현재 원본 수집 범위
- `integration/property-delta.json`: 기존 v18 이후 속성 차이
- `integration/repository-status.json`: 연결된 10개 저장소의 66개 PR 관측
- `integration/verification.json`: 로컬 정합성 검증
- `integration/review-response.md`: 리뷰 의견별 조치
- `integration/history/`: 수집 단계 README·Release Notes·체크섬·PR 본문 원문
- `intake/`: 이전 승인 입력·증적·변경 수집을 원본 그대로 보존
- `../../../releases/v3.1.19/`: 배포 구성 및 최종화 절차 (저장소 루트 기준 releases/v3.1.19)

ZIP은 Git 이력에 반복 저장하지 않고 검토된 SHA256SUMS로 결정적으로 생성한다. 정식 발행 시 Release Asset으로 제공한다. 후보 ZIP의 SHA-256과 검증 결과는 PR에 기록한다.

새 수집으로 HEAD가 변경되면 문서·WBS·Manifest·체크섬·ZIP을 재생성하고 해당 HEAD 검토를 다시 받는다. 기존 자동 수집만으로 병합·발행하지 않는다.

최종화 검증: `finalization-validation.json`, 배포 기록: `releases/v3.1.19/FDS_Release_Finalization_Record_v3.1.19.md`. 과거 수집 상태는 역사적 원문이다.
