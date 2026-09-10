<!-- fds-canonical-description:v3.1.18 record-id:P1-DNS-01 -->
# P1-DNS-01 — Internal DNS Primary/Secondary

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | P1-DNS-01 |
| Phase | Phase 1 |
| Category | DNS / Supporting Service |
| Type | Task |
| Status | Done |
| Priority | P1 |
| Start | 2026-08-28 |
| End | 2026-09-03 |
| Calendar Days | 7 |
| Working Days | 5 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Primary/Secondary·TSIG·제한 Query/Recursion·Failover Evidence와 k8s-api-lb01 `.109` Resolver/ACL/IPSet 검증 및 Support Review 승인 |
| Related Decision IDs | D08; D09; D34; D35 |
| Related Risk IDs | RISK-02; RISK-04; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #12 snapshot 2026-09-10T02:09:19Z |
| Schedule Note | 기술 검증·Support Review·.109 ACL/Resolver/Failover Delta 확인 완료. 2026-09-03 Done 승인. |

## 현재 실행·검토 상태

기준 시점의 Done 상태와 기존 Acceptance를 유지한다. 이번 정본 정리에서는 서버 실행·새 Runtime 판정을 수행하지 않았다.

근거: [Issue #12](https://github.com/321Team/fds-project-baseline/issues/12), Issue 갱신 시각 `2026-09-10T02:09:19Z`. 댓글·승인 기록과 본문 보관본은 `../source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.

---

### User Story

인프라 담당자로서 승인된 P1 Host에 제한된 Primary/Secondary DNS와 Failover를 제공하고 k8s-api-lb01도 내부 DNS 정본을 사용하도록 한다.

### Scope

#### In Scope

- dns01/dns02, `fds.internal`, TSIG Transfer, 제한 Query/Recursion
- k8s-api-lb01 `.109` BIND ACL·firewalld IPSet·Resolver·Failover

#### Out of Scope

- Reverse/PTR, DNSSEC, 완전한 Authoritative/Recursive 분리, Hybrid DNS

### 핵심 요구사항

- [x] Primary/Secondary·TSIG·기존 Client Failover Technical PASS
- [x] dns01/dns02 ACL과 `fds-dns-clients` IPSet에 `.109` 반영
- [x] k8s-api-lb01 Resolver `.52→.53`, Search Domain `fds.internal`
- [x] `.109` 내부·외부 Query와 Primary 장애 Failover Technical Test
- [x] Management `.10/.20/.30` DNS 필요성·ACL OID-04 결정 — N/A 종결: v3.1.17 §15.1 OID-04 / IF-13M(D36)에 따라 P1 범위 제외, IF-13M 미구현 및 `.10` 제외 유지. 향후 도입은 Change Request 대상이다. 호스트별 ACL 구현·시험 PASS를 뜻하지 않는다.

### Acceptance Criteria

- [x] 원본 Evidence SHA-256 및 Support Review 승인 — DNS-AC-12/14/16 PASS (2026-09-03 승인본).
- [x] `.109` Positive Test PASS, 비승인 Source Negative Test 유지 — DNS-AC-06/10/11; DNS-NT-01/03; DNS-CR-05 PASS (2026-09-03 승인본).
- [x] Secret/TSIG 원문이 Evidence에 포함되지 않음 — DNS-AC-13 PASS (2026-09-03 승인본).

### 검증 및 증적

- `docs/evidence/P1-DNS-01/`
- 상세 Description: `P1-DNS-01_Notion_Description_v1.1.md`

### Dependency

- `.109` delta 실행 시점: P1-LB-01 Stage A
- Routing/SNAT 변경 시에만 D-NET-01 §15.2 ICR 발행

### Decision / Risk Control

- Decision: `.109`는 실제 LB VM Interface이므로 DNS Consumer로 허용한다.
- Risk Control: `/24` 전체가 아닌 `.109/32`만 추가하고 기존 monitor01 차단을 유지한다.

### Review / Handoff

- Review Owner: 이하영
- Handoff: ACL/IPSet·Resolver·Failover Evidence를 P1-LB와 P1-K8S에 전달한다.

### Completion Record

- Result: DNS 기능·보안·Failover·R2 Evidence Integrity·Runbook·Support Review PASS
- Status: Done
- Completed Date: 2026-09-03
- Reviewer / Approver: 이하영 / 이권욱 — Approved (2026-09-03)

## 승인본의 상세 Acceptance Criteria 보완

| ID | 완료 조건 | 현재 판정 |
|---|---|---|
| DNS-AC-01 | dns01 Primary와 dns02 Secondary가 활성화되고 부팅 시 자동 시작됨 | PASS |
| DNS-AC-02 | 승인된 13개 A Record가 양쪽 권한 서버에서 동일하게 응답함 | PASS |
| DNS-AC-03 | SOA Serial이 `2026090101`로 일치함 | PASS |
| DNS-AC-04 | Fresh HMAC-SHA256 TSIG Transfer가 성공하고 BADKEY/BADSIG가 없음 | PASS |
| DNS-AC-05 | 미인증 AXFR이 실패함 | PASS |
| DNS-AC-06 | 승인 Source만 Query/Recursion과 TCP/UDP 53에 접근할 수 있음 | PASS |
| DNS-AC-07 | `8.8.8.8` Forwarding과 `forward only` 외부 해석이 정상임 | PASS |
| DNS-AC-08 | Primary 중단 중 dns02가 내부·외부 해석을 지속함 | PASS |
| DNS-AC-09 | k8s-control01 Resolver Canary, Rollback, Reapply, Failover가 정상임 | PASS |
| DNS-AC-10 | k8s-api-lb01 `.109`의 ACL/IPSet, Resolver 및 Failover가 정상임 | PASS |
| DNS-AC-11 | monitor01의 직접 내부/재귀 질의가 차단됨 | PASS |
| DNS-AC-12 | 원본 11개, Sidecar 11개, Manifest 12개와 ZIP Sidecar가 검증됨 | PASS |
| DNS-AC-13 | Evidence에 TSIG Secret, Key Hash, 인증 AXFR MAC이 노출되지 않음 | PASS |
| DNS-AC-14 | v1.8 기반 R2가 정본 경로에 반영되고 ZIP SHA-256이 일치함 | PASS |
| DNS-AC-15 | 재실행 가능한 Runbook에 Subshell Guard와 상대 ZIP Sidecar 규칙이 반영됨 | PASS — v1.9 설치/Runbook/Canonical RC 0 |
| DNS-AC-16 | 이하영 Support Reviewer가 정본과 검증 결과를 승인함 | PASS — 2026-09-03 |
| DNS-AC-17 | 전체 6개 Node Resolver 전환의 소유 티켓, 일정, 검증 기준이 명시됨 | PASS |
| DNS-AC-18 | CoreDNS Source 관측과 ACL/ICR 분기 기준이 P1-K8S-01 Handoff로 명시됨 | PASS |

## 체크사항 보완 근거와 후속 작업 (2026-09-09)

- 상세 승인본: `P1-DNS-01_Notion_Description_v1.3_Review.md` (본문 v1.3-R5, 2026-09-03).
- 승인 기록: `P1-DNS-01_Support_Review_Approval_Record_20260903.md`. 이하영 회신만으로 승인을 추정한 것이 아니라 이권욱 Lead의 승인 완료 확정을 함께 기록한 문서다.
- R2 정본 ZIP: `P1-DNS-01-FRESH-20260902-R2.zip`; SHA-256 `e23d02a8422fdc4943ce2e255b5b087f0e58e5ad2a0439ddcf7d041276f315ab`. Raw TXT 11개, Sidecar 11개, Manifest 12개와 ZIP Sidecar 검증 PASS 기록을 대조했다.
- `.109` 증적: `lb/20260902T184256+0900_k8s_api_lb01_evidence.txt`, `failover/20260902T184144+0900_k8s_api_lb01_failover_evidence.txt`. 비승인 Source 증적: `monitor01/20260902T184303+0900_monitor01_negative.txt`.
- 전체 6개 Node Resolver 전환의 실행·멱등성 검증은 [CR-P1-ANS-01-01 #58](https://github.com/321Team/fds-project-baseline/issues/58) 소유다. DNS-AC-17의 PASS는 소유권·일정·검증 기준 Handoff에 대한 판정이다.
- CoreDNS Source 관측과 ACL/ICR 분기는 [P1-K8S-01 #10](https://github.com/321Team/fds-project-baseline/issues/10) 소유다. DNS-AC-18의 PASS는 Handoff 기준 문서화에 대한 판정이며 Runtime 완료를 뜻하지 않는다.
- OID-04는 [v3.1.17 정본 §15.1](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md)의 OID-04 및 IF-13M(D36) 행에 근거해 P1 N/A로 종결했다. 별도 호스트 허용 승인이나 Runtime PASS를 만들어 넣지 않았다.
