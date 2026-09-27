# v3.1.21 Canonical Candidate

> **Status:** CANDIDATE / COLLECTING / NOT RELEASED  
> **Started:** 2026-09-27 KST  
> **Base canonical:** `docs-v3.1.20`  
> **Source main snapshot:** `2084182f97b593b3950194f44c071a88c0dfc4da`

이 브랜치는 v3.1.20 발행 이후의 정본 동기화 입력을 미리 수집하는 **후보 수집 지점**이다. 이 상태는 정본 승인·병합·Tag·Release 발행을 의미하지 않는다.

## 이번 사전 수집에 포함한 것

- v3.1.20 발행 후 main 및 관련 저장소의 Merged 변경 이력 수집.
- v3.1.20 발행 후 정정 기록에서 지정한 v3.1.21 이월 항목 수집.
- 현행 계획 입력 `DEC-P1-IMG-01`(#110)을 **To Do / 승인 대기 상태 그대로** 후보 데이터로 기록.
- `wbs/FDS_v3.1.21_WBS_and_Gantt_v1.0.xlsx` 후보 생성.
  - 2026-09-28 이재환: 개인 사정으로 인한 휴가
  - 2026-09-29 이하영: 채용설명회 및 직무테스트로 인한 휴가
  - 개인 부재 계산 범위를 Team Calendar 12행 → 14행으로 확장.
  - 기존 일정·Status·Lead/Support를 자동 변경하지 않음.
  - 영향 창: `DEC-P1-IMG-01`, `CR-P1-MON-01-01`, `CR-P1-MON-01-02`.

상세 수집 근거는 `audit/canonical-candidate-20260927/`을 따른다.

## 아직 정본 후보 완성으로 판정하지 않는 항목

다음은 이 PR에서 **수집/기록만** 하고 최종 정본 동기화 완료로 판정하지 않는다.

- Baseline / Ticket Pack / Description 전체 재생성 및 상호 대조
- v3.1.20 발행 후 정정 사항의 전체 반영
- Manifest / SHA256SUMS / Distribution ZIP / WEB snapshot 생성
- 필요 시 Architecture 재발행 사유 판정
- 전체 Workbook 수식 재계산 및 렌더링 기반 시각 QA
- GitHub Release Tag/Asset 발행 검증

열려 있는 구현·증적 PR은 병합 완료 입력으로 승격하지 않는다. 현재 제외 목록은 audit 기록의 **Open / excluded** 절을 따른다.

## Release gate

최종 v3.1.21 병합/발행 전에는 `governance/RELEASE_POLICY.md` §2~§6의 필수 산출물과 검증을 다시 수행해야 한다.
