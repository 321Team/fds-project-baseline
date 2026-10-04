# Phase 2 사전 작업 및 PR137 리뷰 후속 — 2026-10-04
AI usage: CODEX_ASSISTED. 조회 기준 2026-10-04 18:55~19:00 KST.
입력 PR137 HEAD: `36093a8640d045dea887d0e3d5b6817574851d96`.
현재 정본: CURRENT.md의 v3.1.21. 정본 발행과 P1 Close/Phase2 Start/Freeze는 별도다.
이번 범위: 기존 준비 코드·문서의 리뷰 보완. 담당·일정·AC·Status·Decision·권한을 변경하지 않는다.

## 1. 현재 판정과 우선순위
| 순서 | 필요한 사전 작업 | 이번 수행/다음 입력 | 상태 |
|---|---|---|---|
| 1 | PR137 미처리 리뷰 3건 | Runner 3안 비교, README sizing 참조 정렬, FQDN/CA 경로 코드 수정 | STATIC/MOCK 완료, 독립 재리뷰 대기 |
| 2 | #38 플랫폼 지원·용량 / #35 계정 준비 | exact supported HCP version/type, support/linkage, ELB role, named quotas, P1 live capacity | 원본 입력 대기; 기존 조회 collector 재작성 없음 |
| 3 | #34/#37/#40 관리 경로·필수 DNS subset | Runner→vpn-gw actual L3/next hop/source, DNS ACL·반환경로, source/selector 변경결정 | B1 HOLD |
| 4 | #42 D22 logical 계약 및 #43 image 입력 | P2 principal 분리·CA/endpoint 수용, build→scan→registry approved digest 연결 | 후보 준비됨, 사람 결정/producer 입력 대기 |
| 5 | #35/#34 비용 | 10-06 이후 사용자 텍스트로 한도·기간·누적·기준시각, 서울 총비용·teardown 입력 | null 유지, Cost GO 아님 |
| 6 | #32→#33→#34 실행 진입 | P1 Close 판정, Phase2 Start 조건, 권위 충돌·필수 설계입력 해소 | actual sign-off/Freeze 미확인·HOLD |
| 병행 | D21 final raw / 공개 이력·IAM 후속 | 기존 원본·독립 검토 및 소유자 결정 경로 연결 | 아래 잔여; 새 유료자원 생성 없음 |

#32 최신 조회 댓글은 10-06 Close 계획일이며 실제 Close 판정이 아니다. #33의 실행모델은 W0→W1 G4→W2 G5→W3 G6→10-23 teardown이다. Phase1 잔여를 완료로 표시하거나 P1 non-blocking 작업을 새 P0 조건으로 올리지 않는다.
Harbor consumer USER_READBACK(계약 §1.6) 및 Runner source 대조(§1.7)는 기존 작업으로 인정한다. 현재 CI Push adapter/authfile 격리는 기존 P1 구현 세션의 handoff를 소비하고 동일 작업을 중복 수행하지 않는다.

## 2. Runner 관리 경로 — B1 차단 및 세 대안
[Private 관리·DNS 계약](20261004-private-management-bidirectional-dns-contract.md)을 보완한다.
현재 Runner source가 기존 selector 밖이며 local routed next hop도 미확인이다. 문서 보완은 실제 도달성 해결이 아니다.

| 대안 | 영향·장점 | 필요한 입력·위험 | 선택 조건 |
|---|---|---|---|
| A. 기존 Runner + 좁은 관리 selector/route 추가 (권장 후보) | Runner·기존 delivery 위치 유지. source /32 보존과 기존 VPN 경로 활용 | local L3/next hop·양 peer 지원·cloud/local return·최소 SG/FORWARD·DNS 결정. 공통 Relay 장애에 관리도 의존 | actual routed path 확보 및 별도 네트워크 변경결정 수용 시 |
| B. 별도 관리 터널 | 업무 SA와 관리 selector/route의 변경·복구를 분리 가능 | 별도 endpoint/인증·키 수명/route·DNS·비용·운영 책임 필요. 같은 Relay/회선을 쓰면 물리 장애 독립성 없음 | A의 selector/장애 영향이 수용되지 않고 관리 채널 분리 효과를 입증할 때 |
| C. VPC 내부 Runner | private API로의 cloud 내부 관리 경로 구성 가능 | 새 compute/IAM/Runner registration/단기 credential·egress·증적 이전·비용. On-Prem Harbor push나 DB 경로는 별도이며 관리자의 DNS/접속도 자동 해결되지 않음 | 기존 위치 보존 제약을 정식 변경하고 A/B보다 비용·보안·운영 조건이 적합할 때 |

A를 우선 검토하는 이유는 기존 Runner 유지 intent와 변경량이다. actual L3 경로가 없으면 A를 강행하지 않고 B/C를 authority에 재검토한다.
성공 조건: 승인 source로 DNS→TLS 이름검증→인증/RBAC→대상 API/Route까지 확인하고 반환경로·negative·원복을 증적으로 연결. 승인 전 selector 확대/SNAT/route 변경은 하지 않는다.

## 3. README sizing 정합
현행 후보의 단일 참조는 [resource-fit §3](20261003-resource-fit-recommended-design.md)이다.
README의 과거 m5.2xlarge 비교값을 현행 3×m5.xlarge 후보 참조로 정렬했다. 승인 사양 변경이 아니다.
3대 합계 12vCPU/48GiB, 1대 상실 시 8vCPU/32GiB는 gross 사양일 뿐 schedulable capacity가 아니다.
supported offering/allocatable/platform requests/app surge/PDB·AZ·PVC 제약 검증 전 N-1 PASS·Cost GO 없음.

## 4. Harbor 도구 보완과 실제 검증
- HTTPS endpoint를 harbor.fds.internal로 고정, arbitrary host override/IP fallback 없음.
- --ca-file 필수 인자로 기존 공개 CA 파일 경로 지정. pinned SHA256 유지. credential 인자/환경변수 신설 없음.
- DNS/TLS 무자격 GET probe 후 hidden credential 입력. probe의 401/403은 TLS 도달성 확인 범위일 뿐 인증 성공 아님. authenticated 401/403은 기존대로 STOP.
- GET-only, redirect/proxy 차단, strict hostname/chain verification, secret/raw body 미저장 유지.
- 로컬 offline unittest 15/15 PASS: 기존10 + FQDN, bad CA 사전중단, missing CA, 임의 로컬 CA 경로/strict TLS, TLS/연결 실패 시 prompt 전 중단.
- 실제 DNS/Harbor API/Robot 인증/ROSA pull 미실행. 테스트의 PEM·HTTP 응답은 모의 입력이며 현장 증적이 아니다.
- 현재 SAN의 IP/FQDN 포함은 [D22 계약 §1.3](20261004-harbor-d22-input-contract.md)의 USER_READBACK을 소비. 새로운 인증서 원본 수신·재해시 또는 field 재시험 아님.
- 이미 확보된 Robot metadata 재수집 불필요. 향후 필요 시 [수정 실행 절차](../runbooks/20261004-harbor-robot-readonly.md)를 사용한다.

## 5. Freeze 전 비교·결정 잔여
새 리뷰의 비차단 권고는 기존 미확정 입력으로 연결한다.
- Relay+worker 동시 장애: 사전 캐시만으로 새 worker cold-pull 복구를 보장할 수 없다. 현 D22안은 자동 mirror/failover 없이 신규 rollout STOP 및 정상 workload/승인 digest 보존. mirror를 택하면 별도 저장·credential·동일 digest/provenance·비용 및 실제 pull 검증을 결정해야 한다.
- worker 전용 subnet안: Resolver/PrivateLink/LB ENI를 분리한 설계와 app별 DB 인증+NetworkPolicy의 조합을 source reconciliation 후보와 비교한다. subnet 안의 다른 주체 부재·NetworkPolicy 집행·DB identity·node pull 구분을 증명하기 전 subnet 전체 허용을 승인하지 않는다. 기존 CIDR/state 배치 변경은 후보일 뿐이다.
- 비용 초과 시 검토 순서(새 결정 제안): 불필요 idle 시간/잔존자원 정리 → 승인 P0를 보존한 실행창 재배치 → optional P1 소비 연기 → sizing/NAT/가용성 변경은 별도 결정. 미검증 감축으로 N-1/security AC를 낮추지 않는다. 금액/한도 미수신으로 절감액·허용 시간을 계산하지 않았다.

## 6. 공개 이전 리뷰 후속 — 완료로 표시하지 않는 항목
[독립 보조 리뷰](https://github.com/321Team/fds-project-baseline/pull/137#pullrequestreview-5404973855)는 최초 이전20/20 범위만 확인했고 새 코드·설계는 제외했다.
- MFA 미등록으로 기록됐던 두 사용자 현재 등록/Assume 상태, MFA 없는 장치 해제·삭제 Deny의 현재 적용, 장기 access key 0개 상태는 실제 원본 재확인이 필요하다. 사용자별 본인 조치·계정 정책 담당의 검토된 bootstrap 경로를 사용한다. 이번 요청을 IAM 쓰기 승인으로 확대하지 않는다.
- 공개 저장소의 의사결정 주체는 repository/org owner 권한 보유자다. 정확 개인 신원·실행 기한은 미확정이므로 이권욱 또는 타 팀원으로 임의 배정하지 않는다.
- 순서: private snapshot 확인 → 권한 보유자의 현재 branch 삭제 판단 → 공개 목적/외부 링크 영향과 visibility 결정 → 공개 유지 시 GitHub Support 대상 검토. branch 삭제만으로 PR refs/commit/cache/clone 제거 완료가 아니다.
- 리뷰 작성자 supreme33-kr가 제안한 자신의 공개 리뷰2건 정리는 원문 보존 확인 뒤 작성자 본인 수행 대상이다. 이번 세션이 타인 리뷰를 수정하거나 그 사람의 완료를 대신 기록하지 않는다.
- 이 항목은 실제 credential 유출 유무와 별개인 공개 상세·보안 약점 후속이며 전 credential 일괄 rotation 요구로 확대하지 않는다.
- 최초 migration manifest/snapshot은 불변. 이후 코드/문서 diff와 해당 최초 byte-identical 판정을 구분한다.

## 7. 검증 경계와 재리뷰
STATIC=위 코드·문서 변경 범위 확인. MOCK=Harbor collector 15/15.
CI=이번 작성 단계 미확인(0건이면 NOT_RUN). RUNTIME/CREATE/APPLY=NOT_RUN.
INDEPENDENT_REVIEW=PENDING / D22_FINAL=PENDING / ARCHITECTURE_FREEZE=HOLD / MERGE=NOT_RUN.
새 코드 변경으로 기존 이전 무결성 리뷰를 코드 승인으로 승계하지 않는다. 로컬시험은 strict TLS 실제 handshake/계정 지원/실제 credential 검증을 대신하지 않는다.

근거:
- [PR137 미처리3건](https://github.com/321Team/fds-project-baseline/pull/137#issuecomment-5978011937)
- [#32 Close 계획](https://github.com/321Team/fds-project-baseline/issues/32#issuecomment-5793206233), [#33 실행모델](https://github.com/321Team/fds-project-baseline/issues/33#issuecomment-5912449502)
- [#34 관리/DNS](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-5976875946), [#35 준비검증](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5977270867), [#38 capacity](https://github.com/321Team/fds-project-baseline/issues/38#issuecomment-5977086566)
- [#43 image handoff](https://github.com/321Team/fds-project-baseline/issues/43#issuecomment-5977008279), [D22 현재 패킷](20261004-d22-decision-and-input-packet.md)
