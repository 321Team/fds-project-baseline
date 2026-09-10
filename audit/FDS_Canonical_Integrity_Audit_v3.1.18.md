# FDS v3.1.18 후보 무결성 감사

> 2026-09-10 · CANDIDATE · 로컬 문서 정합성 검증

## 결과

| 항목 | 결과 |
|---|---|
| Record ID / 속성표 | 64건·중복 0·필수 17개 속성 모두 존재 |
| Record ID / 상태 / Lead / Support | 원본 스냅샷 대비 변경 0 |
| 계획 Start / End | 사용자 요청 기반 권장 계획창 24건, 전후 값과 원본 이력 보존 |
| Description 속성 vs canonical-records | 불일치 0 |
| 새 AC 체크·새 완료 판정 | 0 |
| 속성 변경 대장 | 174개 필드 차이, 누락 0 |
| WBS | 기존 8개 탭 보존 + Fast Track Plan 추가(9개), 일정관리 55건, 수식 2,209개, 수식 오류 0 |
| 기간 독립 재계산 | Python 달력 계산 vs Excel 결과 vs 티켓 속성: 불일치 0 |
| Gantt / Milestone·Decision | 권장 계획일 연결, 주말·공휴일·Lead 부재 막대 제외, 상태·대상 25건 표시 확인 |
| 표시 검수 | 최초 8개 탭 검수 후 이번 수정 영역·추가 Fast Track Plan 렌더 검수, 기존 차트 2개 보존 |
| 자원·주말·부재 | 54개 배정, 23인일(버퍼 1.5), 초과 배정·주말/부재 작업 0 |
| 기존 동기화 회귀 | 초기 후보 unittest 18/18 PASS 이력; 이번 동기화 코드 변경 없음 |
| Shell | 기존 배포/검증 스크립트 구문 검사 PASS |
| 체크섬·ZIP | SHA256SUMS 및 실제 후보 ZIP으로 기존 검증 스크립트 실행 |
| GitHub Actions / 게시 Release Asset | NOT RUN / 미발행 |
| 실서버 실행 / 실제 Issue 본문·속성 변경 | NOT RUN |

기계 판독 검증은 `v3.1.18/validation.json`, 재검증 명령은 `python3 scripts/verify-v18-candidate.py`다. 원본 본문 SHA-256은 `tickets/v3.1.18/canonical-records.json`에, 본문·댓글 원문은 `source-snapshot.json`에 고정했다. `updated_at`은 Issue 갱신 시각이며 본문만의 수정 시각을 뜻하지 않는다. 댓글 API가 시각을 반환하지 않은 항목은 null을 보존한다.

## 범위와 한계

- 이번 PASS는 정본 후보의 내부 일관성이다. 독립 Reviewer 승인·운영 Runtime PASS·Release 발행을 대신하지 않는다.
- #59/#61 원본 미확인, Milestone HOLD 20건, OID/NTP·DB 계약·FUP 인수 잔여는 변경 대장에 명시했다.
- P1-MON-02의 고도화 AC 상세화, K8S/ICR의 보호 전환 문구 교정은 후보 검토 사항이다. 실행·위험 수용을 승인하지 않았다.
- G1 과거 미달성 목표를 보존하고 09-17 목표를 권장한다. P1-MON-02의 기존 가용일 1일은 이력이며 MON-02/DR-02/HA-02 신규 구현 유예를 제안한다. 실제 잔여 공수는 미확인으로 일정 실현성은 PASS 판정 대상이 아니다.
- ZIP은 후보 검토용으로 생성했다. 정식 Tag 이후 독립 WBS Asset·ZIP·Sidecar·SHA256SUMS를 업로드하고 `--published` 검증을 통과해야 발행 완료다.
- 변경 전 v3.1.17 및 과거 버전은 원래 Git tree를 부모로 보존한다. 후보 WBS와 README 등 명시적 변경 외의 기존 정본 파일은 수정하지 않는다.

## 승인 경계

기존 PR #3·#68의 내용은 통합 후보에 포함한다. 기존 PR을 merge/close하지 않는다. 독립 리뷰·이권욱의 명시적 merge 승인 후 finalization과 Tag·Asset 검증을 진행한다. `CURRENT.md`는 v3.1.17을 유지한다. 배포 정책의 게시 Asset 검증은 발행 단계의 별도 필수 Gate이며 후보 ZIP 검증으로 대체할 수 없다.

## 09-10 휴가·ICR 추가 유입 검증

09-08 기록을 유지하고 09-10 부재를 추가했다. P1-SEC 기존 계획창 09-04~11에서 가용일 입력을 범위 밖으로 옮겼을 때 5일, 09-10으로 복원했을 때 4일을 확인했다. 이후 Fast Tracking 권장 End를 09-21로 바꾼 전체 계획창의 가용일은 10일이다. 이는 잔여 공수가 아니다. ICR 기존 End TBD와 실제 미완료 이력을 보존하고 권장 Plan End만 09-21로 제안한다. 상태·Lead/Support·AC·원본 스냅샷은 보존했다.

ICR 최초 추가 유입의 고정 원문은 `v3.1.18/followup-20260910.json`, 일정·배정·중간 판단은 `v3.1.18/fast-track-plan.json`이다. 당시 무결성 PASS / 완전성 PARTIAL / 운영 인수 HOLD는 과거 이력이다. 이후 Worker 보완 검증 및 PR #3 병합 결과는 아래 최신 편입으로 갱신한다.

## 09-10 K8S 최신 이력 후보 편입 검증

사용자의 권장안 후보 병합 요청에 따라 `infra-kubernetes` PR #2 `097ddb5`, PR #3 merge `7d44afc`, PR #4 `75d476e`와 baseline Issue #10/#14/#19를 고정했다. 고정 원문·메타데이터·본문 SHA-256·변경 전 후보 3개 레코드와 작업 2개는 `v3.1.18/k8s-intake-20260910.json`에 보존했다. Source·설명·Baseline·WBS·일정 권장안의 현재 요약을 동기화했다.

- Worker supplement 기술 PASS와 PR #3 병합을 반영했다. PR #2 현장 mock 37/37·읽기 전용 inspect 115건 및 PR #4 로컬 mock 74건은 원문에서 확인한 결과이며 이번 편입에서 실행한 시험이 아니다.
- 후보 부모 `e2992efa4e7e3659480fb209da874b01fa30dfb1` 대비 64개 레코드 중 K8S/ICR/SEC 3개만 갱신했다. 속성은 Source 3개만 변경했고, 상태·Lead/Support·일정·기존 AC 체크는 보존했다. Fast Track 배정 54개 중 작업 설명 2개만 갱신했다.
- WBS의 실제 문자값 변경은 17셀이다. 9개 탭·수식 2,209개·날짜·비대상 값·차트 2개 원본 XML·관계 대상·레이아웃·데이터 유효성·사용 서식을 비교해 보존을 확인했다. 내보내기 중 기존 OVERBOOKED 조건부 서식의 solid fill이 누락되는 현상을 같은 조건·색·글꼴로 복구했으며, 사용되지 않는 서식 항목 1개만 남는다.
- 수정된 WBS Source 3행·Sources & Change Log·Fast Track Plan을 렌더 검수했다. 후보 검증 스크립트 PASS, 수식 오류 0·속성/Description 불일치 0·새 AC 체크 0이다. 결과는 `v3.1.18/validation.json` 및 `v3.1.18/k8s-intake-validation.json`이다.
- NTP 승인 기준, CP2 잔존 상태에 따른 재개 절차, 최종 host 보호와 정적 Local PV 상세는 후속 확정 대상으로 유지한다. PR #2/#4의 최신 HEAD 독립 리뷰 및 운영 canary/join/인수는 완료로 표시하지 않았다.
- CA/CI-CD 및 외부 Monitoring·Notification의 별도 편입 요청은 이번 K8S 파일 통합 범위에 포함하지 않았다. 원본 스냅샷·기존 후속 이력·`CURRENT.md`는 바이트 단위로 보존했다.
