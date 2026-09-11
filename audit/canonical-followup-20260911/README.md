# 정본 무결성 후속 보완 후보 — 2026-09-11

상태: **IN PROGRESS / REVIEW CANDIDATE**. 운영 정본은 RELEASED v3.1.18이다.

## 착수 근거

사용자가 일정은 필수 기한이 아닌 유연한 계획이라고 명시하고 이하영 리뷰를 요청한 뒤, 차단사항이 없으면 착수하도록 지시했다.
PR #68의 정확한 HEAD `573c18877a5b710a04ee50dae59fedf4e3552aea`에 대한 [이하영 APPROVED 리뷰](https://github.com/321Team/fds-project-baseline/pull/68#pullrequestreview-5176621355)를 확인했다.
이 HEAD에서 현재 main `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`까지 ahead 6 / behind 0이다. PR #68의 코드는 이미 포함돼 있어 중복 병합 없이 superseded로 종결한다. 이 승인을 본 후보의 새 내용 승인으로 복제하지 않는다.

## 준비한 변경안

| 대상 경로 | 적용 후보 | 내용 |
|---|---|---|
| CURRENT.md | proposed/CURRENT.md | 실제 v18 게시시각·태그 대상·승인 링크를 기록하고 작성 당시 미게시 문구와 현재 상태를 분리 |
| governance/RELEASE_POLICY.md | proposed/governance/RELEASE_POLICY.md | WEB 필수 배포 및 동일 바이트 검증, 일정 유연성과 Gate 증적 요건의 분리 |
| governance/TICKET_SYNC_POLICY.md | proposed/governance/TICKET_SYNC_POLICY.md | 현행 v18·복원 완료 사실·계획 조정 원칙 반영 |
| D-ARC-01 / D-WBS-01 | intake.json | 복원된 17개 속성을 원문 그대로 고정하고 차기 Ticket Pack/Baseline 편입 입력으로 준비 |

`proposed-changes.patch`는 위 3개 파일의 실제 변경 diff다. `base-files.json`의 원본 Git blob SHA와 대상 파일이 일치할 때만 후속 통합 후보에 적용한다.
이 검토 PR은 제안 파일과 입력·검증 기록만 추가한다. 기존 v18의 CURRENT·정본·WBS·Tag·Release·Manifest·SHA256SUMS를 수정하지 않는다. v18 SHA256SUMS가 CURRENT와 정책까지 포함하므로 일부 파일만 덮어쓰고 예전 해시를 계속 사용하는 방식은 피한다.
차기 정본 통합 시 현재 승인된 데이터에서 WBS/Gantt·WEB·Release Notes·Manifest·SHA256SUMS·ZIP을 함께 생성하고 검증한다. 본 제안의 CURRENT는 v18 게시 사실에 대한 교정 입력이며 차기 버전 번호·상태로 그대로 복사하지 않는다.

## 확인 결과와 잔여

- 최신 운영 티켓 64건: 실제 Type 64건 설정, 실제 Milestone 44건 배정 / 20건 미확정. `intake.json`에 조회된 값을 기록했다.
- #59/#61의 원본 속성 미확인은 해소됐다. 배포된 v18의 과거 미확인 표시는 발행 스냅샷으로 보존하고 후속 편입 시 복원값으로 갱신한다.
- #59: 계획 Start/End 2026-08-24, Calendar/Working Days 3의 모순은 미해결. 실제 완료 서술은 2026-08-26이다. 임의로 계획 End를 8/26으로 바꾸지 않는다.
- #61: 복원된 계획 2026-08-24~26과 과거 원본의 완료일 8/26·8/28 혼재를 구분한다. 실제 완료일의 최종 확정은 근거 확인 대상이다.
- 20개 미배정 티켓은 추적 Milestone 선택 또는 의도적 미배정 근거가 필요하다. 일정 유연성만으로 일괄 배정·N/A 처리하지 않는다.
- #46의 Plan End 10/19와 G5 10/16은 조정 가능한 계획/연계 검토 항목이다. 정해진 날짜 준수 자체를 착수 차단 조건으로 삼지 않는다.
- OID/NTP/egress, IF-16, FUP-04/05, Stage A/LB-A-01 및 개별 Runtime 인수는 해당 책임 티켓에서 추적한다. 문서 보완 착수로 Gate·AC·Done을 변경하지 않는다.
- 배포본의 원본 해시 검증 결과는 2026-09-11 17:07 KST 감사 기준이다. 본 변경안의 검증 결과는 `validation.json`에 별도로 기록하며 CI/실서버 PASS를 주장하지 않는다.

## 리뷰 요청

이하영은 게시 상태 교정, WEB 필수 배포, 일정 유연성, 복원값 보존 및 미결 항목의 처리 경계를 검토한다.
확정 일정이나 미확인 실제 완료일을 새로 만들어 내지 않는다. 명시된 미결 사항은 후속 편입 범위를 정할 때 판단하며 비차단 준비 작업은 계속한다.
