# v3.1.21 발행 준비 증적

사용자 요청: 현시점 근거로 테스트 전략 검토, WBS 반영, 베이스라인 발행. 발행 승인은 받았으나 정책의 혼합 코드 독립 리뷰 및 실제 게시 조건을 면제한 것은 아니다.

산출물은 현 상태 snapshot이다. P1 Close/Architecture/Stage-A HOLD를 완료로 변경하지 않는다. 기존 78 Issue 원문은 snapshot.zip에 보존하고 body SHA와 current disposition을 canonical-records.json 및 Description에 연결한다. WBS Status/담당/날짜는 같은 properties로 생성한다. 미기재 속성은 미기재로 두고 기간은 날짜/달력에서 계산한 값으로 구분한다.

생성 규칙: UTF-8 LF 문서, JSON indent2, source body 문자열 원형 보존. 원문 body에는 원래 CRLF가 있을 수 있다. ZIP entry는 경로 정렬·고정 시각2026-01-01·고정 권한, manifest SHA256 순환을 피하기 위해 manifest 자체는 SHA256SUMS에만 등재. 배포 ZIP은 저장소의 build-canonical-package.py를 사용한다. SHA256SUMS/ZIP sidecar는 실제 byte에 대해 계산한다. 날짜는 KST.

WBS는 기존 9tab과 native WBS table을 편집해78row/10tab으로 갱신한다. Team Calendar/Fast Track Plan의 역사 자료 보존. Lead Workdays는 기존 휴일/개인부재 수식이며 공수 아님. Test Strategy TS01~16과 pre/post-create Gate를 추가했다. 수식 재계산, 오류 검색, export 후 independent cell/row/date/workday/conditional-format 검증과 이미지 확인을 수행한다. Native Excel 앱 실행은 하지 않았다.

후속 발행 순서: exact-head 독립 코드 리뷰 → 최신 HEAD/CI/미해결thread/산출물 일치 확인 → Lead 결정으로 reviewed PR 병합 → 별도 finalization PR로 CURRENT/버전상태/manifest/hash 갱신 → main의 최종화 SHA에 docs-v3.1.21 Tag → ZIP/sidecar/SHA256SUMS/독립 XLSX Asset → published byte 검증. 미실행 단계의 SHA/승인/게시 상태를 사전 채우지 않는다. 되돌림은 후보 변경 revert 또는 수정 commit이며 기존 v3.1.20 발행 bytes 보존.

## 발행 후 이월 항목 처리

2026-09-23 followup의 정정 DOCX를 동일 경로·바이트로 이번 Manifest/체크섬/ZIP에 포함했다. SHA256 04b8daf58efb4fdfb7947d6b4635c4be4e3bd237ec2b466daa70962bba777735. 문서 내부 v3.1.20은 역사 자료 식별이며 신규 v3.1.21 본문으로 오인하지 않는다. retrospectives/ 4개 파일은 참고 이력으로 체크섬 대상에 편입하되 AC로 자동 승격하지 않는다. 원본 v3.1.20 Tag/Release Asset은 변경하지 않는다.

CURRENT.md의 v3.1.20 Tag 대상 설명 정정과 v3.1.21 포인터/RELEASED 상태는 내용 병합 후 별도 최종화에서 수행한다. 기존 정본 내부의 역사적 CANDIDATE 표기는 현재 RELEASED 상태를 뒤집지 않는다.
