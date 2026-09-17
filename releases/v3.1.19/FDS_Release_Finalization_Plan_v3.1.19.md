# v3.1.19 발행 절차

현재 상태: CANDIDATE / REVIEW_PENDING. 사용자 배포 지시는 수신했다. 이하영의 최신 HEAD 독립 승인 전 병합·발행하지 않는다.

1. 최종 HEAD의 v19 verifier, SHA256SUMS, Workbook/ZIP 및 원본 보존 검증 결과를 리뷰한다.
2. 독립 APPROVED가 정확한 HEAD에 적용되고 차단 의견이 해소됐는지 재조회한 뒤 수동 병합한다.
3. CURRENT와 상태표를 v19 최종화 후보로 변경하고 내용 승인 HEAD·병합 SHA를 기록한다. 새 최종화 HEAD 독립 검토 후 병합한다.
4. 최종화 commit에 docs-v3.1.19 태그를 만들고 승인 SHA256SUMS로 ZIP을 재생성한다. ZIP·sidecar·SHA256SUMS·동일 WBS를 Release Asset으로 업로드한다.
5. 저장소·Manifest·SHA256SUMS·ZIP·독립 WBS Asset 해시를 대조한 뒤 Publish한다. Release API published_at·태그 commit·Asset digest를 재조회한다.
6. 티켓 Runtime/AC/Done은 자동 변경하지 않는다. 실패 시 v18 Release/태그/Asset을 유지하고 후보 상태로 복구한다.

복구: 잘못된 후보는 브랜치 수정으로 교정한다. 게시 전 Asset 오류는 Draft 내에서 수정·재검증한다. 이미 게시된 정본은 태그 강제 이동/과거 바이트 덮어쓰기 대신 별도 변경 통제로 정정한다.
