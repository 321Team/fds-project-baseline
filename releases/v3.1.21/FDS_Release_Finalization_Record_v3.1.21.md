# v3.1.21 Finalization record

RELEASED after reviewed finalization merge. 사용자 이권욱의 배포 지시(2026-10-04 KST)에 따른 문서 전용 최종화다. PR112 내용 HEAD 4acd5a9af69ed7dcaa3cfc934ba8e4bd05b7c0d8, 내용 병합 bb3cd4f44932e932984beaba7f279bd4b7321c0b. [독립 승인](https://github.com/321Team/fds-project-baseline/pull/112#pullrequestreview-5403611452)은 해당 범위이며 이 문서가 승인 범위를 확장하지 않는다.

최종화 변경: CURRENT/README/핵심 문서/WEB/WBS 버전 상태 정리, 상속 §16 역사 표 주의, 과거 audit checksum/생성기 범위 명시, Manifest/SHA256SUMS/ZIP 재생성. WBS 수식·날짜·담당·Status/AC 등 원본 업무 데이터는 변경하지 않았다. 과거 candidate audit/Description은 당시 원문으로 보존한다.

PR112 CI 2건 SUCCESS. 최종화 CI는 최종화 PR exact HEAD에서 별도 확인한다. 이 문서에는 미래 commit SHA/게시 시각을 미리 기입하지 않는다. Tag docs-v3.1.21은 최종화 merge SHA에 생성하고 실제 Tag/Release API와 네 종류 Asset digest가 외부 게시 증적이다. 기존 v3.1.20 Tag/Assets 변경 없음.

배포 ZIP은 scripts/build-canonical-package.py의 경로 정렬·고정 timestamp/권한 규칙으로 생성. Manifest 자체는 SHA256SUMS에만 포함하여 순환을 피한다. ZIP sidecar는 외부에 둔다. 배포 후 ZIP/sidecar/SHA256SUMS/독립 WBS를 다운로드 또는 GitHub digest로 대조하고 --published CI를 확인한다. 로컬 gh/bash가 없어 실제 업로드는 사용자 로그인 GitHub UI에서 수행한다. 같은 네 파일/해시 통제를 유지하며 기존 검사기를 완화하지 않는다.

P1 Close/Architecture Freeze/Stage-A/D21 raw의 잔여는 그대로다. 이 발행은 실제 서버 적용·실행/AC 인수·티켓 종결을 뜻하지 않는다. 복구는 별도 문서 PR/새 버전이며 발행된 Tag/Asset을 덮어쓰지 않는다.
