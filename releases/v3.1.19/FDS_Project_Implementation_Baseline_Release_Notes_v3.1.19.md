# FDS v3.1.19 Release Notes — 수집 초안

Status: **DRAFT / NOT RELEASED**
Base: v3.1.18

이 문서는 발행 준비를 위한 수집 초안이며 구현·검증·발행 완료 선언이 아니다.

## 승인 입력 — 통합 대기

| 입력 | 적용할 내용 | 근거 |
| --- | --- | --- |
| 게시·배포 정책 | CURRENT 게시 사실 교정, WEB 필수 배포, 일정 유연성 | [PR #72](https://github.com/321Team/fds-project-baseline/pull/72) |
| #59 / #61 | 계획 End 및 실제 완료일 2026-08-26 정정 | PR #72 approved-date-corrections.json |
| #46 | G5 목표 2026-10-16, 계획 기간 1일 | PR #72 및 실제 티켓 |
| Milestone | 64건 전체 매핑, 후속 19건의 근거·인계 조건 보존 | PR #72 댓글 5632352726, 5632473246 |

## 검토 대기·잔여

관련 저장소의 미병합 PR과 미검증 증적은 `audit/v3.1.19/intake/repository-sources.json`에서 추적한다. OID/NTP/egress, IF-16, FUP-04/05, Stage A/LB-A-01 및 개별 Runtime 인수는 책임 티켓의 실제 최신 근거로 판단한다.

## 발행 검증

전체 묶음: NOT BUILT. v19 발행 검증: NOT RUN. 기존 v18 정본을 유지한다.

## 2026-09-11T10:31:50Z 추가 수집 — 승인 사양 미편입

- 신규 [CR-P1-MON-01-01 #74](https://github.com/321Team/fds-project-baseline/issues/74): Alertmanager Discord 외부 송신 예외. **PENDING_REVIEW**.
- [infra-kubernetes #5 확인 댓글](https://github.com/321Team/infra-kubernetes/issues/5#issuecomment-5632931284): Worker 외부 연결 성공 보고는 원본 로그·해시 없는 보고이며 Pod/프록시 Runtime PASS를 뜻하지 않는다.
- 총 티켓 **65건 / Milestone 64건 배정 / 신규 #74 1건 미배정**. 기존 64건의 매핑 변경은 없다.
- 검토 필요: 기존 #17 외부 미송신 원칙과 Decision/Interface 정합화, Lead/Support·계획·프록시 배치·selector·Secret 수명주기. 네트워크 관리자 승인 불필요 주장은 별도 권한 근거로 확인해야 한다.
- fds-msa 조회 404로 실제 배포 라벨·설정 대조는 미확인. 저장소 미존재로 단정하지 않는다.
- 나머지 6개 관련 저장소 PR의 기존 HEAD·병합 상태 변경, 신규 PR 리뷰·Commit, 기준 시각 이후 default branch Commit은 미검출. 과거 리뷰 30개 PR의 조회 결과는 비교 기준으로 보존하며 신규 승인으로 취급하지 않는다.
- 상세: [수집 기록](../../audit/v3.1.19/intake/updates/20260911T103150Z.json). 수집 후보의 새 HEAD는 이하영의 독립 검토가 필요하며 병합·발행은 별도 승인 대상이다.

## 2026-09-11T10:58:10Z 추가 수집 — 두 Monitoring CR 추적 확장

- [CR-P1-MON-01-01 #74](https://github.com/321Team/fds-project-baseline/issues/74): 프록시 서버 구성으로 Scope 분리, 17개 속성·G2 추적 Milestone 반영. Lead/Support·계획일은 TBD, 내용은 PENDING_REVIEW, Runtime NOT VERIFIED.
- 신규 [CR-P1-MON-01-02 #75](https://github.com/321Team/fds-project-baseline/issues/75): #74 endpoint를 인수하는 NetworkPolicy·selector·Secret 통제. 17개 속성·G2 추적 Milestone 반영. Lead/Support·계획일은 TBD, 내용은 PENDING_REVIEW, Runtime NOT VERIFIED.
- 전체 **66건 / Record ID 66개 유일 / Milestone 66건 배정**. 실제 GitHub Type은 #74·#75 두 건 미반영이다. G2 배정은 추적용이며 P0/G2 필수 AC 또는 확정 End를 추가하지 않는다.
- 신규 리뷰 기록: [#10 K8S](https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5633333888) 운영 인수 HOLD, [#13 HBR](https://github.com/321Team/fds-project-baseline/issues/13#issuecomment-5633336598) HBR-01~06 Revision Required, [#19 SEC](https://github.com/321Team/fds-project-baseline/issues/19#issuecomment-5633339292) SEC-01~08 Revision Required. 이는 공식 PR APPROVED나 실행 승인으로 승격하지 않는다. [#17 롤업](https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-5633394060)도 같은 경계를 유지한다.
- 발행 전 차단: 두 CR의 native Type, 담당·계획, 프록시 endpoint/변경권한, 실제 selector/Secret/payload/Positive·Negative·복구 증적, 기존 외부 미송신 Decision·Interface 정합화 및 WBS/Ticket Pack/Release 묶음 편입.
- 연결 저장소 default HEAD·기존 PR 메타데이터·신규 공식 리뷰/Commit 변화는 미검출. fds-msa는 계속 404로 직접 대조하지 못했다.
- 상세: [수집 기록](../../audit/v3.1.19/intake/updates/20260911T105810Z.json). 새 후보 HEAD는 이하영의 독립 검토가 필요하다.

## 2026-09-11T11:34:47Z 추가 수집 — 두 CR 담당·Type 확정

- [CR-P1-MON-01-01 #74](https://github.com/321Team/fds-project-baseline/issues/74): Lead 이하영, Support 이재환, Start 2026-09-11, End/기간 TBD로 확정하고 Assignee를 `hayeounglee`로 적용했다.
- [CR-P1-MON-01-02 #75](https://github.com/321Team/fds-project-baseline/issues/75): Lead 이하영, Support 이재환, Start/End/기간 TBD와 #74 프록시 endpoint 선행조건을 유지하며 Assignee를 `hayeounglee`로 적용했다.
- 두 이슈의 실제 GitHub Issue Type은 `Change Request`(ID `864949231`)로 동기화됐다. [실행 증적 수신·검증 기록](https://github.com/321Team/fds-project-baseline/pull/73#issuecomment-5633784102)의 결과 SHA-256은 `c9c7b53028a5e2c72ac5ea2869844a84e0f5ace3c923ae175a5c2a6d4ba5b3b3`이다.
- 이 변경은 **USER_AUTHORIZED_OPERATIONAL_DELTA**다. 다만 두 CR의 기술 변경안은 계속 **PENDING_REVIEW**, 실제 적용·Runtime 인수는 **NOT VERIFIED**다. G2는 추적용이며 CR의 End 또는 Gate PASS를 뜻하지 않는다.
- 전체 **66건 / Record ID 66개 유일 / Milestone 66/66 / native Type 누락 0**. 프록시 endpoint·변경권한, 실제 selector·Secret/payload·허용/차단/복구 증적과 Decision/Interface 및 전체 v19 산출물 편입은 여전히 발행 전 검토 대상이다.
- 관련 7개 저장소의 default HEAD·기존 PR 메타데이터·신규 공식 PR 리뷰/Commit 변화는 미검출했다. PR #73 자체 수집 Commit·댓글·본문 갱신은 새 프로젝트 변경에서 제외했다.
- 상세: [수집 기록](../../audit/v3.1.19/intake/updates/20260911T113447Z.json). 새 후보 HEAD는 이하영의 독립 검토가 필요하다.
