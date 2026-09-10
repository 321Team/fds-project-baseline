# FDS v3.1.18 후보 무결성 감사

> 2026-09-10 · CANDIDATE · 로컬 문서 정합성 검증

## 결과

| 항목 | 결과 |
|---|---|
| Record ID / 속성표 | 64건·중복 0·필수 17개 속성 모두 존재 |
| 상태 / Lead / Support / Start / End | 원본 스냅샷 대비 변경 0 |
| Description 속성 vs canonical-records | 불일치 0 |
| 새 AC 체크·새 완료 판정 | 0 |
| 속성 변경 대장 | Source 64 + 기타 보완 16 = 80, 누락 0 |
| WBS | 8개 탭 유지, 일정관리 55건, 수식 2,101개, 수식 오류 0 |
| 기간 독립 재계산 | Python 달력 계산 vs Excel 결과 vs 티켓 속성: 불일치 0 |
| Gantt / Milestone·Decision | 원본 일정 유지, 상태 연결·대상 25건 표시 확인 |
| 표시 검수 | 8개 탭 관련 영역 렌더·검수, 한글·추가 행·요약 차트 확인 |
| 기존 동기화 회귀 | unittest 18/18 PASS |
| Shell | 기존 배포/검증 스크립트 구문 검사 PASS |
| 체크섬·ZIP | SHA256SUMS 및 실제 후보 ZIP으로 기존 검증 스크립트 실행 |
| GitHub Actions / 게시 Release Asset | NOT RUN / 미발행 |
| 실서버 실행 / 실제 Issue 본문·속성 변경 | NOT RUN |

기계 판독 검증은 `v3.1.18/validation.json`, 재검증 명령은 `python3 scripts/verify-v18-candidate.py`다. 원본 본문 SHA-256은 `tickets/v3.1.18/canonical-records.json`에, 본문·댓글 원문은 `source-snapshot.json`에 고정했다. `updated_at`은 Issue 갱신 시각이며 본문만의 수정 시각을 뜻하지 않는다. 댓글 API가 시각을 반환하지 않은 항목은 null을 보존한다.

## 범위와 한계

- 이번 PASS는 정본 후보의 내부 일관성이다. 독립 Reviewer 승인·운영 Runtime PASS·Release 발행을 대신하지 않는다.
- #59/#61 원본 미확인, Milestone HOLD 20건, OID/NTP·DB 계약·FUP 인수 잔여는 변경 대장에 명시했다.
- P1-MON-02의 고도화 AC 상세화, K8S/ICR의 보호 전환 문구 교정은 후보 검토 사항이다. 실행·위험 수용을 승인하지 않았다.
- G1 과거 목표와 P1-MON-02 가용일 1일의 실행 가능성은 별도 Lead 판단 대상이다. 계획일을 바꿔 불일치를 숨기지 않는다.
- ZIP은 후보 검토용으로 생성했다. 정식 Tag 이후 독립 WBS Asset·ZIP·Sidecar·SHA256SUMS를 업로드하고 `--published` 검증을 통과해야 발행 완료다.
- 변경 전 v3.1.17 및 과거 버전은 원래 Git tree를 부모로 보존한다. 후보 WBS와 README 등 명시적 변경 외의 기존 정본 파일은 수정하지 않는다.

## 승인 경계

기존 PR #3·#68의 내용은 통합 후보에 포함한다. 기존 PR을 merge/close하지 않는다. 독립 리뷰·이권욱의 명시적 merge 승인 후 finalization과 Tag·Asset 검증을 진행한다. `CURRENT.md`는 v3.1.17을 유지한다. 배포 정책의 게시 Asset 검증은 발행 단계의 별도 필수 Gate이며 후보 ZIP 검증으로 대체할 수 없다.
