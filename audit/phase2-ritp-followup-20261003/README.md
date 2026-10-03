# Phase 2 R/I/T/P follow-up / current source delta

기준: 2026-10-03T15:21:56.660+09:00. AI 사용: CODEX_ASSISTED.

CANDIDATE / COLLECTING / NOT RELEASED. 기존 전체 수집/정본 생성기는 변경하지 않았다. 이 회차는 지정 12 Issue와 6 PR의 비원자적 재수집이다. 14 repo/78 Issue 전체 재수집·WBS/Workbook/Description/ZIP regeneration 완료를 뜻하지 않는다.

- [current architecture candidate](https://github.com/321Team/fds-project-architecture/blob/1516a04f4103b75fa2a955b063dadb6589f99975/phase2/README.md), PR #8.
- D21 FINAL/aws_ec2_eip_relay, full Architecture Freeze HOLD.
- Terraform#2 refreshed HEAD dbd66f930760f159026ed5b833dd24fe22f0ca23: historical W0 superseded input, old body preserved.
- Terraform#3 ebfc56e25125784187e36a0c1dd2ca0463e82acd unchanged: previous author fmt/init/validate PASS; no resource blocks; CI checks0 ≠ PASS; plan/apply/runtime NOT RUN.
- infra-rosa#2 f5f0db1c50e83b7c9bb5242de9090fdd15cf5720: malformed input/source binding fixes + reproducible mock tests + arbitrary UID Runtime acceptance link. STATIC/MOCK PASS; CI/runtime NOT RUN; PG03 HOLD.
- evidence#104 feea4288f96d92c3e058d59d8dbf7f124c8bfdf8: two-parent main sync, main blobs 4395 unchanged and raw collection blobs4 unchanged. Registry exact main+1 manifest line. Local SHA256 checks: all3 items OK; collection manifest a38d157df07904e48d905f4d1a22b4ad41c16170c21c9e2d088528b6ef53f199. [evidence-layout run37102502442](https://github.com/321Team/fds-project-evidence/actions/runs/37102502442) SUCCESS at this exact HEAD. 독립 review/reapproval PENDING.
- D21 final responder expected 8706bytes/e5f754a3d66c6fe452605ff914a6294e87aa85bf6a345ec0fadb981f18745cb0; raw bytes/Phase-A/initiator/cleanup 미수신. intermediate bdcd9564...는 canonical 아님. Final publication HOLD.

## New dependency finding

Private API/Ingress이면 FQDN+TLS 검증에 필요한 DNS는 P0 subset이다. #40 전체 P1 scope/일정은 유지하면서 #34/#38 create gate에 최소 DNS dependency를 연결한다. Runner 10.250.10.20은 current selector 10.1.93.0/24 밖이다. 관리망 route/identity/selector 판단 전 SNAT 또는 selector 자동 확대 금지.

## Authority / Runtime contracts

B1 HCP 우선 비교 + Private API/Ingress는 권고 입력, 미승인. Exact version/quota/capacity/egress/DNS/access/cost 입력 부족으로 HOLD. HCP/Classic 앱 manifest 복제 없음.
B2 selectors ≠ app authorization; forwarding default deny, no inner NAT, DB5432 API만/engine deny, Harbor443은 D22 조건부, SG+host policy+platform policy+DB auth·stable source 결박.
B3 one observed IP 대신 approved failure-domain-stable source set, Node source collision은 app identity policy/DB auth로 통제. 재배치/교체/복구 후 검증.
B4 portable base + OpenShift overlay; nonroot/no escalation/RO rootfs/RuntimeDefault/drop ALL 유지. restricted-v2 arbitrary UID 실제 Running/Ready/health/filesystem/cleanup 필요. Admission PASS≠PG03 PASS.

## Source and integrity

[sources.json](sources.json)은 각 Issue 원문 body·comment body·updated_at과 PR 입력 HEAD/body를 보존한 source collection이다. Timestamp는 collection 범위의 상한이며 단일 atomic snapshot이 아니다. Own follow-up comments 8건을 exact read-back 대조했다. 초기 PR112 input HEAD5f3eaf6...는 수집 대상 기록이며 본 delta commit 뒤 PR HEAD는 갱신된다.

SHA256SUMS는 sources.json 바이트 무결성을 검증한다. Snapshot completeness/Runtime success를 뜻하지 않는다. 기존 Python scanner 자체를 실행하지 못해 해당 scanner의 5 pattern을 JS로 대조(findings0); 추가 AWS session key/GitHub PAT/private key 패턴도0. PSK-labelled long status의 heuristic match1은 credential 아닌 status 문자열로 판별했다. SECRET_REVIEW=STATIC_PATTERN_SCOPE_ONLY; 원본 증적에 적용한 scan 아님.

## Publication semantics

docs-v3.1.20 Release API draft=false/published_at=2026-09-22T17:37:13Z로 실제 게시 확인. Release text의 stale candidate 표현은 historical. CURRENT.md 후보에서 PUBLISHED와 v3.1.21 NOT_PUBLISHED를 구분하며 기존 release bytes/assets/hash는 변경하지 않았다.

## Remaining gates / owners

- #34 이권욱, #35/#38 이하영: actual account/ROSA supported input, Cost-to-Complete, topology/access/egress/DNS/management route decision.
- #35 이하영/#37 이재환: exact forwarding source tuple/SG/host policy/sourceSHA/IDs + positive-negative-recovery.
- #38 이하영/#43/#47 이재환: portable manifests/image/namespace and stable source arbitrary-UID Runtime.
- D21 producer 이권욱: final raw/cleanup authorized transfer; independent evidence reviewer 이하영/이재환 중 독립자.
- PR112 owner: 본 delta를 전체 regeneration input에 편입하고 WBS/문서/manifest/ZIP+검증을 수행. 이 회차는 전체 release set 생성 아님.

STATIC=bounded PASS / MOCK=ROSA input-contract PASS / CI=evidence104 exact-head SUCCESS, 그 외 재조회 / RUNTIME=NOT_RUN_BY_TASK / REVIEW=independent PENDING / MERGE=NOT_DONE / PUBLICATION=NOT_DONE.
