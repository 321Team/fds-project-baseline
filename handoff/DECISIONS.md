# 도입 결정 — 2026-09-11

근거: 사용자의 권장안 전체 적용 지시. 아래는 도입 방법이며 프로젝트의 기술 사양,
담당자, 일정, 기존 승인 권한을 새로 정하는 CR이 아니다.

| ID | 결정 | 적용 방식 |
|---|---|---|
| WC-01 | Cloud Codex 부분 도입 | 공용 교육장 PC는 웹 접속, 코드 작업은 클라우드 |
| WC-02 | Work에 PMO·판단·통합 검토 유지 | OPERATING_RULES 역할표 |
| WC-03 | GitHub를 공통 기준으로 사용 | 사양 lock + Task별 live context receipt |
| WC-04 | 명시적 인수인계 | AGENTS·WORK_START·DECISIONS·NEXT_ACTIONS·증적 참조 |
| WC-05 | Kit 재현성 보장 | 고정 파일 목록/Checksum/순서/시각으로 ZIP 생성 |
| WC-06 | 작업 단위 이관 | Task/Result 양식과 허용 경로·AC |
| WC-07 | 검증·실행·승인 분리 | STATIC/MOCK/CI/RUNTIME/REVIEW/MERGE/PUBLICATION |
| WC-08 | 이득 실측 후 범위 확대 | 3개 대표 작업 비교표; 현재 NOT_MEASURED |
| WC-09 | 기존 배포본 보존 | v3.1.18 141개 Git blob 그대로, 새 지침 별도 PR |
| WC-10 | 교육장 제약 유지 | 주말 교육장 작업 용량 0, 현장 Gate·기존 일정 유지 |

Cloud 환경 설치/권한 연결과 로그인/다운로드 흔적 제거는 PC·계정에서 확인해야 한다.
이 저장소에 문서를 추가한 사실만으로 해당 설정이 적용됐다고 표시하지 않는다.
