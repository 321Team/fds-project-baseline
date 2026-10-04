# v3.1.21 Issue body synchronization

78개 Issue 본문과 운영 Description 동기화. 사용자 명시적 본문 수정 지시로 수행했다. AI 사용: CODEX_ASSISTED.

변경: 상단 정본 적용 블록과 최초 현행 Source 행만 변경. TS01~16 중 원본 책임/소비자 매핑에 해당하는 항목을 연결했다. 기존 본문·보관 원문·마커·체크박스는 Source 행 외 바이트 그대로다. 상태·제목·담당·라벨·Milestone은 쓰기 요청에서 제외하고 재조회 불변을 검증했다.

각 건 updated_at와 본문을 쓰기 직전 대조하고 쓰기 직후 전체 본문 일치를 확인했다. 상세 SHA256/변경 행/시각은 [results.json](results.json). 변경 전 원문은 기존 이슈 편집 이력과 별도 로컬 감사 ZIP에 보존한다. 이 결과는 비원자적 수집이며 이후 사용자 편집은 덮어쓰지 않는다.

동결된 release·manifest·체크섬·기존 Description은 수정하지 않았다. 운영 파일은 [tickets/live](../../tickets/live/README.md)에 있다.
