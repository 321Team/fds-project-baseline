# Phase 2 비공개 이전 기록 — 2026-10-04
AI usage: CODEX_ASSISTED. 저장 위치 교정이며 설계/코드 승인·정본 발행·Runtime 인수와 다르다.

## 현재 작업 위치
비공개 fds-project-baseline 브랜치 `docs/p2-private-migration-20261004`의 phase2/가 후속 작업 위치다.
공개 fds-project-architecture는 공개 가능한 구성도·설계 개요 용도로 유지한다.
실제 수집 원본은 비공개 fds-project-evidence의 기존 intake/review 절차로 편입한다.
collector는 현재 준비 도구로 함께 보존하며 향후 구현 저장소 귀속은 별도 변경으로 관리한다.

## 원본 보존
원본: fds-project-architecture PR8, commit `9ff3b32263ae1305fbd3a18781e633173a153452`.
최초 이전 시점의 20개 파일은 내용·경로·Git blob을 그대로 보존했다. mapping은 [migration-manifest.json](../audit/phase2-private-migration-20261004/migration-manifest.json)에 파일별 SHA256/byte size/source blob을 기록한다. 이후 리뷰 보완은 별도 commit diff로 추적하며 현재 HEAD의 20개 파일이 원본과 모두 같다고 주장하지 않는다. 최초 이전 manifest와 snapshot은 수정하지 않는다.
baseline parent: `8e870c4c551506afef816ef19b94b381994c6386`.
과거 설계 결정/상태/가격/링크는 당시 기록이며 이전이 이를 최신 승인으로 승격하지 않는다.
문서 속 architecture 고정 commit URL과 PR8 참조는 원본 provenance로 보존했다. 후속 실행파일은 이 비공개 PR의 동일 경로를 소비한다. 별도 링크 변경을 원본과 혼합하지 않았다.
원본 PR 본문/댓글/커밋 metadata는 audit 디렉터리에 private snapshot으로 보존한다. 리뷰 승인을 새 PR로 자동 이전하지 않는다.

## 실제 검증
- 20/20 source Git blob SHA 재계산 일치, UTF-8 파일 SHA256/size 기록.
- 상대 Markdown 파일 링크: missing 0 (외부 링크·anchor 유효성은 범위 제외).
- Python 4파일 AST 파싱 성공; offline unittest 21/21 PASS. AWS/Harbor 네트워크 호출은 mock.
- 공개 PR 커밋 42개의 변경 patch 확보, patch 누락 파일 0; 공개 댓글/리뷰 normalized 항목 20개와 PR 본문 확보.
- 현재 파일20 + commit file patches42 + 댓글20 + PR본문1 = 83 text units를 private-key header / GitHub token / AWS access-key ID / JWT 패턴으로 검사: 일치 0.
- 정형 패턴 검사이며 임의 비밀번호·opaque token 부재를 보증하지 않는다. 모든 Git ref/다른 PR/캐시/포크/타인 clone 검사는 미수행.
- 현재 자료의 내부 IP/CIDR·hostname·사용자/Robot·권한/만료·AWS account/role·운영 경로·보안 설계 및 사설 이슈 연결은 공개용 범위를 벗어나는 정보로 분류했다.
- public Root CERTIFICATE와 certificate fingerprint는 private key/credential로 분류하지 않는다. 실제 secret 노출 여부는 별도 판단한다.

## 공개 이력 잔여
비공개 이전 검증 후 PR8을 미병합 종료한다. 이는 현재 공개 논의를 중단하는 조치이며 기존 commit/PR diff/branch/댓글/캐시/복제본 삭제가 아니다.
이번 작업은 공개 repo visibility 변경, branch 삭제, force push/history rewrite, 댓글 삭제를 수행하지 않는다.
원본 저장소 전체에 대한 참조 영향·협업자 clone·PR cache 범위가 확정되기 전 광범위 이력 재작성을 실행하지 않는다.
필요한 후속 판단:
1. 현장 내부 상세에 대한 공개 허용/제거 범위를 저장소 owner가 확정.
2. 제거 대상 commit/ref/PR본문/댓글 위치 목록과 private 보존본을 연결.
3. 공개 목적을 유지할지, 제한적으로 비공개 전환할지와 외부 공유 링크 영향을 검토.
4. 정리 실행 시 기존 증적 source SHA와 새 SHA 대응·리뷰 영향 검증.
5. GitHub Support의 cache/PR ref 삭제는 민감정보 기준과 지원 범위에 따라 판단하며 삭제 가능성을 보장하지 않는다.
근거: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository

실제 credential 노출이 확인된 경우에만 해당 credential 폐기/rotation 대응을 연결한다.
내부 IP/계정 이름 공개만으로 모든 자격 회전을 완료조건에 추가하지 않는다.

## 다음 단계
비공개 PR 독립 코드/내용 리뷰. Freeze HOLD와 D22 final PENDING 유지.
consumer read-only 절차는 [준비 문서](runbooks/20261004-harbor-consumer-reference-readonly.md)에 있다. 이후 사용자 현장 출력 및 Runner source 대조는 [D22 입력 계약](reviews/20261004-harbor-d22-input-contract.md) §1.6~1.7을 따른다. 최초 이전 당시의 미실행 표기를 현재 상태로 사용하지 않는다.

## 이전 이후 사전 작업 리뷰 보완
[후속 기록](reviews/20261004-prework-review-followup.md)에 Runner 경로 3안, sizing 후보 정합, FQDN/CA 인자화와 시험, 공개 이력·IAM 후속을 연결한다. 공개 노출과 MFA/정책 약점의 확인·보완은 credential 유출 여부와 별개이며, 이번 코드/문서 수정으로 실제 계정 보완을 완료했다고 표시하지 않는다.
