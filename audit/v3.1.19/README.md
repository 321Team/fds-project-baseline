# v3.1.19 정본 발행 준비

상태: **COLLECTING / DRAFT / NOT RELEASED**

운영 정본은 v3.1.18이다. 이 브랜치는 v19를 발행하기 위한 변경 수집·통합 작업 공간이며 아직 배포 가능한 정본 묶음이 아니다.

- 기준 main: `58f72f78faa237cbdc9ceae6460d25407550c1a7` (PR #72 병합)
- 최초 수집: 2026-09-11T09:58:49.550Z
- 사용자 요청: v19 정본 발행 PR을 먼저 생성하고 이후 변경을 수시 수집한다.
- 검토 담당: 이하영 (`hayeounglee`). 최종 발행 판단: 이권욱. 과거 HEAD 승인은 후속 변경의 승인으로 복제하지 않는다.

## 초기 수집

- 승인된 PR #72의 게시 상태·WEB 배포 정책·일정 유연성 교정안.
- #59 Plan End 2026-08-26, #61 Completed Date 2026-08-26 확정, #46 Plan End 2026-10-16 및 기간 1일.
- 전체 64건의 현행 티켓 속성 및 Milestone 매핑. #25~27 구현 일정은 TBD이며 Phase 1 Close는 미결 사항 인계 추적이다.
- 관련 증적·Ansible·Kubernetes·CI/CD·Harbor·DB 저장소 6곳의 PR 메타데이터. 수집된 자료가 모두 신규 변경 또는 승인된 사양이라는 뜻은 아니다.

`intake/initial-snapshot.json`은 최초 입력 이력이다. 후속 갱신으로 덮어쓰지 않는다. `intake/repository-sources.json` 역시 최초 소스 카탈로그다. 변경이 있으면 `intake/updates/` 아래 별도 변경 기록을 추가하고 원문 URL·Commit·승인 범위와 출처 상태를 남긴다.

## 통합 및 발행 전 완료할 작업

- [ ] 승인 입력과 검토 대기 자료를 대조해 v19 반영 범위를 확정한다.
- [ ] Baseline·WBS/Gantt·Ticket Pack·개별 Description·Interface/Decision/CR·완료 이력을 동기화한다.
- [ ] GITHUB_MILESTONE_MAP을 64건 현행 매핑과 대조하고 수집 당시 미확정 수를 이력으로 구분한다.
- [ ] CURRENT·Release Policy·Ticket Sync Policy의 PR #72 제안을 v19 문맥으로 통합한다.
- [ ] WEB·편집 가능한 WBS/Gantt·Release Notes·Distribution Manifest·SHA-256·배포 ZIP 및 필요한 아키텍처를 같은 버전으로 생성한다.
- [ ] 이권욱 영문 표기 GU LEE, 일정·담당·Gate 및 수식·해시·비밀정보 노출을 검증한다.
- [ ] 이하영의 최종 HEAD 독립 리뷰와 이권욱의 병합·발행 승인을 확보한다.

## 수집 원칙

- 상세 절차는 `COLLECTION_POLICY.md`를 따른다. 자동 수집은 후보의 누적 기록만 갱신한다.
- 설계 승인, 코드 병합, 증적 편입, 실제 Runtime 인수와 Gate 통과를 구분한다.
- 일정은 조정 가능한 계획 목표이며 날짜 도래나 Milestone 배정으로 완료를 판정하지 않는다.
- Work/Codex의 개인 도구 운영 지침을 Claude Code 사용 팀원의 공통 의무로 편입하지 않는다. 철회된 공통 지침 PR은 제외 이력이다.
- 기존 v18 발행본·태그·Asset·SHA-256과 운영 CURRENT는 이 초기 수집에서 변경하지 않는다.
- 전체 배포 묶음이 아직 없으므로 본 PR의 병합·발행 준비 판정은 **NOT READY**다.

## 최신 수집 — 2026-09-11T10:31:50Z

[20260911T103150Z 기록](intake/updates/20260911T103150Z.json): 신규 CR #74 및 관련 댓글 1건을 검토 대기로 수집했다. 현재 티켓 65건, Milestone 64건 배정·#74 1건 미배정이다. 최초 snapshot의 64/64 집계는 당시 이력이다. 기존 64건은 변경되지 않았다. fds-msa 조회 404에 따른 배포 설정 대조 미확인을 별도로 기록했다.

#74의 예외 승인·담당·프록시·Secret/Runtime 근거가 미확정이므로 현행 사양으로 자동 편입하지 않는다. 기존 v18·운영 티켓은 변경하지 않았다.

## 최신 수집 — 2026-09-11T10:58:10Z

[20260911T105810Z 기록](intake/updates/20260911T105810Z.json): #74 속성·Scope 보완과 신규 #75, 티켓별 리뷰 #10/#13/#19 및 #17 롤업을 수집했다. 현재 66건, Record ID 66개 유일, Milestone 66/66이며 #74·#75의 native Type은 미반영이다.

두 CR의 G2는 추적용이다. 담당·계획·프록시 endpoint·변경권한·실제 selector·Secret/payload·Runtime과 기존 외부 미송신 계약 정합화가 남아 있으므로 발행 사양 승인으로 확대하지 않는다. WBS/Gantt·Ticket Pack·Interface/Decision/CR·전체 배포 묶음 편입도 대기다.

## 최신 수집 — 2026-09-11T11:34:47Z

[20260911T113447Z 기록](intake/updates/20260911T113447Z.json): #74·#75의 Lead 이하영·Support 이재환, Assignee `hayeounglee`, #74 Start 2026-09-11 및 두 건의 실제 GitHub Type `Change Request` 적용을 수집했다. 전체 66건, Record ID 66개 유일, Milestone 66/66, native Type 누락 0이다.

메타데이터 동기화와 실행 증적 수신 범위는 완료됐지만 두 CR의 변경안 승인·Runtime 인수는 완료되지 않았다. #74 endpoint·변경권한, #75 실제 selector·Secret/payload와 Positive/Negative/복구 증적, 기존 Decision/Interface 및 WBS/Gantt·Ticket Pack·전체 배포 묶음 편입은 계속 대기다.

## 2026-09-16 P1-CICD Trivy 운영안 사용자 채택 — 대상 한정 수집

[수집 기록](intake/updates/20260916T033933Z.json): 사용자 “권장안으로 정본 후보에 등록하고, 착수”에 따라 바이너리 버전/해시 통제 교체와 실제 이미지 Scan 전 DB 준비·검사, 기존 HIGH/CRITICAL 및 스캐너/DB 오류 Push·Deploy 차단 유지를 APPROVED_INPUT으로 수집했다.

592개 파일 참조 0·바이너리 해시 일치의 보완 증적을 검증했지만 외부 자동화 부재는 UNKNOWN이다. 코드 독립 리뷰·새 DB 경로 Runtime·실제 이미지 Delivery Gate는 잔여이며 기존 AC·역할·일정·진척도를 상향하지 않는다.

이번은 P1-CICD 입력에 한정한 수집이다. 기존 9/11의 티켓 수·다른 저장소 상태를 현재 전수 조사 결과로 재사용하지 않는다. v19 전체 묶음 NOT BUILT / 발행 NOT READY / 운영 정본 v3.1.18 유지.
