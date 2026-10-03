# CR-P1-ANS-01-01 — Ansible Kubernetes Node DNS Resolver 변경

Version: v3.1.21 CANDIDATE
Source: https://github.com/321Team/fds-project-baseline/issues/58
Updated at: 2026-09-14T15:17:06Z
Source body SHA256: `78d737be847179ed25742e3d64f00164ec4dba42d4b6433e35f13e716ab15361`
GitHub: closed / completed
Current disposition: Source lifecycle/AC retained; no new acceptance by this publication.

| Property | Current source value |
|---|---|
| Record ID | CR-P1-ANS-01-01 |
| Phase | Phase 1 |
| Category | Automation / DNS Client |
| Type | Change Request |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-04 |
| End | 2026-09-07 |
| Calendar Days | 4 |
| Working Days | 2 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Kubernetes 6개 Node의 DNS 전환, 검색 도메인·API FQDN/Short Name·외부 DNS·직접 질의·서비스 회귀·멱등성·Rollback·Evidence 무결성 및 Support Review 완료 |
| Related Decision IDs | D08; D09; D34; D35 |
| Related Risk IDs | RISK-02; RISK-04; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #58 snapshot 2026-09-09T12:14:54Z |
| Schedule Note | 2026-09-07 Runtime·멱등성·회귀·Rollback·무결성 증적과 이하영 승인 리뷰를 완료하고 이권욱 수동 승인으로 PR #1을 병합했다. GitHub Actions 실행은 0건이므로 CI PASS로 기록하지 않는다. v3.1.17의 `In Review` 표시는 발행 시점 스냅샷이며 다음 정본에서 `Done`으로 동기화한다. |

## Source checklist

- [x] Kubernetes 6개 Node의 DNS Server를 `.52 → .53` 순서로 적용한다.
- [x] 검색 도메인 `fds.internal`을 적용한다.
- [x] NetworkManager의 자동 DNS 덮어쓰기를 차단한다.
- [x] FQDN, Short Name, 외부 DNS 및 승인 DNS 직접 질의를 검증한다.
- [x] kubelet/containerd 서비스 회귀가 없음을 확인한다.
- [x] Apply와 Check Mode의 실행 결과를 분리해 기록한다.
- [x] 반복 실행 시 `changed=0`, `failed=0`, `unreachable=0`을 확인한다.
- [x] Rollback 절차와 Evidence Index·SHA256SUMS를 남긴다.
- [x] 고정 HEAD에 대한 독립 리뷰와 Lead 수동 승인 후 병합한다.
- [x] `CR-DNS-AC-01` — 6개 Node의 DNS 순서가 `.52 → .53`이다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-02` — 6개 Node에 검색 도메인 `fds.internal`이 적용된다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-03` — `k8s-api.fds.internal`이 `.109`로 해석된다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-04` — Short Name `k8s-api`가 `.109`로 해석된다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-05` — 외부 DNS 해석이 정상이다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-06` — 승인 DNS 직접 질의가 정상이다. 결과: 12/12 PASS.
- [x] `CR-DNS-AC-07` — kubelet/containerd 서비스 회귀가 없다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-08` — 멱등성 결과가 `changed=0`, `failed=0`, `unreachable=0`이다. 결과: PASS.
- [x] `CR-DNS-AC-09` — Rollback 자료·절차·검증 결과가 확보됐다. 결과: PASS.
- [x] `CR-DNS-AC-10` — Evidence 원본·Index·SHA-256 무결성을 확인했다. 결과: PASS.
- [x] `CR-DNS-AC-11` — 이하영 Support Review가 승인됐다. 결과: `APPROVED`, 2026-09-07 11:13:58 KST.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

<!-- fds-spec-audit:20260914:v1:start -->
## 사양·기록 전수 점검 후속 — 2026-09-14 점검 반영

사용자 “각 티켓에 내용 갱신” 지시에 따른 기록 보완. 재대조: `2026-09-14T15:11:45+00:00`. 발행 [docs-v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18)과 후속 결정·현재 Issue/PR를 기준으로 한다.

**이 티켓의 점검 결과:** DNS resolver 변경 종결 유지. 신규 프록시 DNS는 #74/#78 별도 변경 ; A07.

**인계·관련 티켓:** [#12](https://github.com/321Team/fds-project-baseline/issues/12) · [#65](https://github.com/321Team/fds-project-baseline/issues/65) · [#74](https://github.com/321Team/fds-project-baseline/issues/74) · [#78](https://github.com/321Team/fds-project-baseline/issues/78).

점검 항목 A01~A07/R01~R06의 전체 대응은 [P1-DOC-01 #24](https://github.com/321Team/fds-project-baseline/issues/24)에서 추적한다. 미완료 티켓의 기록/시험값은 해당 실행·인수 전에 확정할 후속이며, 유예·조건부 P1/P2 항목을 현재 P0 차단으로 추가하지 않는다.

이번 내용 갱신은 기존 AC 체크·Status·Lead/Support·계획 일정·사람의 승인/종결을 변경하지 않는다. 아래 작성 당시의 미병합·검토대기 표현은 위 최신 확인 및 연결된 근거와 구분한다. 기존 본문·보관 원문·댓글은 보존한다.
<!-- fds-spec-audit:20260914:v1:end -->

---

<!-- fds-milestone-assignment:2026-09-11 issue:58 -->
## 대표 Milestone 배정 — 2026-09-11

- **추적 Milestone:** G1 Infrastructure Ready (GitHub #2)
- **배정 성격:** 완료 이력 · 이권욱 사용자 지시에 따른 대표 추적 항목 지정.
- **배정 근거:** Ansible DNS Resolver 변경의 승인·병합 이력을 G1 인프라 선행 변경으로 연결한다. infra-ansible PR #1 병합 Commit 4f9bdb7c08704eebb3d1b294751e51b0721b6af4 확인. Stage A 잔여 조건·Bootstrap 해제·Stage B 승인은 별도다.
- **출처:** [발행 정본에 보존된 종결·승인 이력](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json) · [승인·병합 PR](https://github.com/321Team/infra-ansible/pull/1)
- **일정 원칙:** 일정은 고정된 필수 기한이 아닌 조정 가능한 계획 목표다. 선행조건과 영향 확인 후 유연하게 조정하며, 실제 완료일·승인·Runtime 증적 요건과 구분한다.
- **적용 범위:** 대표 Milestone 연결과 이 근거 기록. 기존 상태·완료 사실·AC·담당·티켓 Start/End 및 Gate 요건을 유지한다.

---

<!-- fds-notion-migration:2026-09-09 record-id:CR-P1-ANS-01-01 -->
<!-- fds-canonical-description:v3.1.18 record-id:CR-P1-ANS-01-01 -->
# CR-P1-ANS-01-01 — Ansible Kubernetes Node DNS Resolver 변경

> 적용 기준: [발행 정본 v3.1.18](https://github.com/321Team/fds-project-baseline/releases/tag/docs-v3.1.18) · 2026-09-11 11:23:47 KST 게시.
> 승인 소스: `72599ae49342b0fb8dbd3d8ee60314afb9f907bb`. 문서의 작성 당시 후보·미발행·이전 상태 표현은 이력이며, 현재 적용 기준은 이 머리말과 최신 운영 기록을 따른다. 계획 갱신으로 실제 AC·승인·종결을 상향하지 않는다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | CR-P1-ANS-01-01 |
| Phase | Phase 1 |
| Category | Automation / DNS Client |
| Type | Change Request |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-04 |
| End | 2026-09-07 |
| Calendar Days | 4 |
| Working Days | 2 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Kubernetes 6개 Node의 DNS 전환, 검색 도메인·API FQDN/Short Name·외부 DNS·직접 질의·서비스 회귀·멱등성·Rollback·Evidence 무결성 및 Support Review 완료 |
| Related Decision IDs | D08; D09; D34; D35 |
| Related Risk IDs | RISK-02; RISK-04; RISK-07 |
| Source | Baseline v3.1.18; Ticket Pack v3.1.18; GitHub #58 snapshot 2026-09-09T12:14:54Z |
| Schedule Note | 2026-09-07 Runtime·멱등성·회귀·Rollback·무결성 증적과 이하영 승인 리뷰를 완료하고 이권욱 수동 승인으로 PR #1을 병합했다. GitHub Actions 실행은 0건이므로 CI PASS로 기록하지 않는다. v3.1.17의 `In Review` 표시는 발행 시점 스냅샷이며 다음 정본에서 `Done`으로 동기화한다. |


## 최신 운영 기록의 보존

- 이관 직전 Issue 상태: **Done / closed**. 원본 갱신 시각: `2026-09-09T12:14:54Z`.
- 담당·라벨·실제 Type·Milestone·댓글·AC 판정은 이 Description 단계에서 변경하지 않는다.
- 현행 설계·Scope·계획은 상단 v3.1.18을 따른다. 아래 원문 보관의 과거 사양·상태를 현재 값으로 다시 적용하지 않는다.

## 정본에 반영된 실행·검토 상태 — 작성 시점 기록

2026-09-07 CR 최종 승인·병합 완료. 승인 HEAD 507d8882a04f53640b07251bcc234b7d6ee81c09, merge 4f9bdb7c08704eebb3d1b294751e51b0721b6af4, AC 11/11은 당시 실행·Support 승인 기록에 근거한다. CI NOT RUN. FUP-01 원본 보완·독립 편입과 증적 PR #1 병합은 완료됐으며 Stage A 조건부 인수의 잔여 조건, Bootstrap 해제·Stage B는 별도다.

근거: [Issue #58](https://github.com/321Team/fds-project-baseline/issues/58), Issue 갱신 시각 `2026-09-09T12:14:54Z`. 댓글·승인 기록과 본문 보관본은 [정본 수집 원문](https://github.com/321Team/fds-project-baseline/blob/72599ae49342b0fb8dbd3d8ee60314afb9f907bb/tickets/v3.1.18/source-snapshot.json)에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

## 적용 기준

- Baseline v3.1.18의 현행 설계·Interface·Gate와 아래 Scope/Acceptance를 함께 적용한다.
- 이력의 당시 PASS·Done은 원래 범위에 한정한다. 후속 Runtime 또는 승인자를 새로 생성하지 않는다.
- 이 티켓은 종결 이력이다. 과거 구성 설명은 해당 종결 범위를 설명하며 현재 배포 명령으로 사용하지 않는다. 후속 설계 변경은 Baseline의 현행 절과 책임 티켓을 따른다.

---

### User Story

인프라 자동화 담당자로서 Ansible을 통해 Kubernetes 6개 Node의 DNS Client 설정을 승인된 DNS 이중화 구성으로 일관되게 전환한다. 이를 통해 반복 실행 시 불필요한 변경이 발생하지 않도록 하고, 장애 발생 시 재현 가능한 Rollback과 검증 가능한 Evidence를 확보한다.

---

### Scope

#### In Scope

- Kubernetes Control Plane 3대와 Worker 3대의 Resolver 전환
- DNS Server `.52 → .53` 순서 및 `fds.internal` 검색 도메인 적용
- `k8s-api.fds.internal` 및 `k8s-api` 해석 검증
- 외부 DNS와 승인 DNS 직접 질의 검증
- kubelet/containerd 회귀 점검
- Apply, Check Mode, 멱등성, Rollback 및 SHA-256 Evidence 관리
- 독립 Support Review와 Lead 수동 승인·병합

#### Out of Scope

- Kubernetes API 인증 성공 판정
- P1-LB-01 Stage B Backend UP, Failover/Recovery 판정
- kubeadm init/join 착수 승인
- ICR-D-NET-01-01의 Calico HostEndpoint/GNP 및 관리망 반환 경로 변경

---

### 핵심 요구사항

- [x] Kubernetes 6개 Node의 DNS Server를 `.52 → .53` 순서로 적용한다.
- [x] 검색 도메인 `fds.internal`을 적용한다.
- [x] NetworkManager의 자동 DNS 덮어쓰기를 차단한다.
- [x] FQDN, Short Name, 외부 DNS 및 승인 DNS 직접 질의를 검증한다.
- [x] kubelet/containerd 서비스 회귀가 없음을 확인한다.
- [x] Apply와 Check Mode의 실행 결과를 분리해 기록한다.
- [x] 반복 실행 시 `changed=0`, `failed=0`, `unreachable=0`을 확인한다.
- [x] Rollback 절차와 Evidence Index·SHA256SUMS를 남긴다.
- [x] 고정 HEAD에 대한 독립 리뷰와 Lead 수동 승인 후 병합한다.

---

### Acceptance Criteria

- [x] `CR-DNS-AC-01` — 6개 Node의 DNS 순서가 `.52 → .53`이다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-02` — 6개 Node에 검색 도메인 `fds.internal`이 적용된다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-03` — `k8s-api.fds.internal`이 `.109`로 해석된다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-04` — Short Name `k8s-api`가 `.109`로 해석된다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-05` — 외부 DNS 해석이 정상이다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-06` — 승인 DNS 직접 질의가 정상이다. 결과: 12/12 PASS.
- [x] `CR-DNS-AC-07` — kubelet/containerd 서비스 회귀가 없다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-08` — 멱등성 결과가 `changed=0`, `failed=0`, `unreachable=0`이다. 결과: PASS.
- [x] `CR-DNS-AC-09` — Rollback 자료·절차·검증 결과가 확보됐다. 결과: PASS.
- [x] `CR-DNS-AC-10` — Evidence 원본·Index·SHA-256 무결성을 확인했다. 결과: PASS.
- [x] `CR-DNS-AC-11` — 이하영 Support Review가 승인됐다. 결과: `APPROVED`, 2026-09-07 11:13:58 KST.

---

### 검증 및 증적

- 저장소: `321Team/infra-ansible`
- Pull Request: [PR #1](https://github.com/321Team/infra-ansible/pull/1)
- 승인 대상 HEAD: [`507d8882a04f53640b07251bcc234b7d6ee81c09`](https://github.com/321Team/infra-ansible/commit/507d8882a04f53640b07251bcc234b7d6ee81c09)
- 병합 Commit: [`4f9bdb7c08704eebb3d1b294751e51b0721b6af4`](https://github.com/321Team/infra-ansible/commit/4f9bdb7c08704eebb3d1b294751e51b0721b6af4)
- 병합 시각: 2026-09-07 15:02:55 KST
- GitHub Actions/Commit Status: 실행 0건 — **NOT RUN**, CI PASS로 간주하지 않음
- Control Plane Apply: 2/2, `changed=4`, 실패 0
- Control Plane Idempotency: 2/2, `changed=0`, 실패 0
- Worker Apply: 3/3, `changed=4`, 실패 0
- Worker Idempotency: 3/3, `changed=0`, 실패 0
- Corrected Check Mode API Check: 5/5 실행, `changed=0`
- 6개 Node 최종 재검증: 6/6, `changed=0`, 실패 0
- 승인 DNS 직접 질의: 12/12
- Kubernetes API Listener 전·후: 6/6
- 외부 DNS: 6/6
- kubelet/containerd 회귀 없음: 6/6

| Evidence 대상 | SHA-256 |
|---|---|
| `EVIDENCE_INDEX` | `6f5568d805a5d7f43130d2fdca2ba631358f4f8be23e1f7d0799ae8243c7db1e` |
| `SHA256SUMS` | `05de9ba6b22d36ef8fc67bdf3dd8c6629c3e334fbb61620a265a46acdbfd4115` |
| 6개 Node 최종 로그 | `18cbda0fc7d91ebf58c89c230dccabaf9ad8239305856da03067210582194e83` |
| 무결성 로그 | `35a320650312e343764a5d7eecfe70c42bafcf43c8043a422d920030a20dee14` |
| 재최종화 기록 | `db7da7eae13c1b07e6b073003a23229e76f3a86f6903a66ac9a2cf522f84395d` |

> 원시 Runtime Evidence는 `ansible01`에서 생성되어 Git 추적 제외 대상으로 관리된다. 이번 판정은 PR에 고정된 해시 기록과 독립 승인 리뷰를 근거로 하며, 이번 검토에서 원시 파일 자체를 다시 실행하거나 재수집하지 않았다.

---

### Dependency

- 선행 기준: P1-DNS-01 승인 DNS 구성과 D08/D09 DNS 결정
- 연동 기준: P1-LB-01 Stage A Listener와 API Endpoint `.109:6443`
- 후속 영향: P1-K8S-01의 kubeadm Bootstrap 전 DNS 선행조건 제공
- 통제 사항: 본 CR의 완료만으로 P1-LB-01 Stage B, Kubernetes API 인증 또는 kubeadm init/join을 승인하지 않는다.

---

### Decision / Risk Control

- `D08`, `D09`: DNS Server 순서와 `fds.internal` 해석 기준을 유지한다.
- `D34`, `D35`: 설계 승인과 Runtime 상태를 분리하고 Interface 정본을 준수한다.
- `RISK-02`: 단일 DNS 또는 Resolver Drift 위험을 이중 DNS와 멱등성 검증으로 통제한다.
- `RISK-04`: 네트워크 경로 오판을 FQDN/Short Name/직접 질의/외부 DNS 검증으로 통제한다.
- `RISK-07`: 증적 누락과 상태 과대판정을 Evidence Index, SHA-256 및 독립 리뷰로 통제한다.
- GitHub Actions가 실행되지 않았으므로 CI PASS를 주장하지 않는다.

---

### Review / Handoff

- Reviewer: 이하영 (`hayeounglee`)
- Review 결과: `APPROVED`
- Review 시각: 2026-09-07 11:13:58 KST
- Review 대상: HEAD `507d8882a04f53640b07251bcc234b7d6ee81c09`
- 최종 수동 승인: 이권욱
- 병합 결과: 2026-09-07 15:02:55 KST, Merge Commit `4f9bdb7c08704eebb3d1b294751e51b0721b6af4`
- 후속 Handoff: P1-K8S-01은 별도 Gate와 실제 Runtime 조건을 확인한 후 착수한다.

---

### Completion Record

- Acceptance 11/11: **충족**
- Runtime Evidence 및 SHA-256: **충족**
- 독립 Reviewer 승인: **충족**
- Lead 수동 승인: **충족**
- 승인 HEAD 병합: **충족**
- 비밀정보를 Git에 포함하지 않는 Evidence 관리: **충족 기록 확인**
- GitHub Actions CI: **NOT RUN** — 별도 PASS 주장 없음
- 최종 판정: **Done**
- 완료일: **2026-09-07**

`CR-P1-ANS-01-01` 완료는 Kubernetes API 인증, P1-LB-01 Stage B, kubeadm init/join 또는 ICR Runtime 완료를 의미하지 않는다.

다음 정본 발행 시 Baseline Project Status Register, WBS/Gantt, Canonical Ticket Pack, `docs/change/CR-P1-ANS-01-01.md`, Release Notes, Manifest, SHA256SUMS, Audit 및 WEB을 `Done` 상태로 동기화한다. WBS/Gantt는 내용 변경 여부와 관계없이 ZIP 및 독립 Release Asset에 포함한다.

## 갱신 전 원문 보관

<details>
<summary>이전 본문·승인·검토·AC 이력 원문 — 당시 기록</summary>

원문 SHA-256: `1a6e1d8181675b046b1504b7b5af1fa5142596b0092948361526163c84eb289e`. 원문은 아래 문자 그대로 보존하며 현재 속성표로 사용하지 않는다.

````text
<!-- fds-notion-migration:2026-09-09 record-id:CR-P1-ANS-01-01 -->
# CR-P1-ANS-01-01 — Ansible Kubernetes Node DNS Resolver 변경

> 이관일: 2026-09-09 · 정본 및 보관 Notion 입력본 기준. Notion 실시간 원문·댓글·첨부의 완전 복제를 확인한 결과는 아니다.

## Notion 데이터 속성

| Property | 입력값 |
|---|---|
| Record ID | CR-P1-ANS-01-01 |
| Phase | Phase 1 |
| Category | Automation / DNS Client |
| Type | Change Request |
| Status | Done |
| Priority | P1 |
| Start | 2026-09-04 |
| End | 2026-09-07 |
| Calendar Days | 4 |
| Working Days | 2 |
| Lead | 이권욱 |
| Support | 이하영 |
| Exit Criteria | Kubernetes 6개 Node의 DNS 전환, 검색 도메인·API FQDN/Short Name·외부 DNS·직접 질의·서비스 회귀·멱등성·Rollback·Evidence 무결성 및 Support Review 완료 |
| Related Decision IDs | D08; D09; D34; D35 |
| Related Risk IDs | RISK-02; RISK-04; RISK-07 |
| Source | FDS_Project_Implementation_Baseline_v3.1.17.md`; `FDS_v3.1.17_Canonical_Ticket_Update_Pack_v1.0.md`; `321Team/infra-ansible` PR #1; HEAD `507d8882a04f53640b07251bcc234b7d6ee81c09`; Merge `4f9bdb7c08704eebb3d1b294751e51b0721b6af4; 이관 대조: Baseline/WBS v3.1.17 (commit 2d93395a0e19ea67e5be199d7183a7edbaa6cf4c) |
| Schedule Note | 2026-09-07 Runtime·멱등성·회귀·Rollback·무결성 증적과 이하영 승인 리뷰를 완료하고 이권욱 수동 승인으로 PR #1을 병합했다. GitHub Actions 실행은 0건이므로 CI PASS로 기록하지 않는다. v3.1.17의 `In Review` 표시는 발행 시점 스냅샷이며 다음 정본에서 `Done`으로 동기화한다. |

## 이관 기준 및 확인 사항

- 2026-09-08 Notion 배포안의 속성·본문을 반영했다. 원 정본 v3.1.17은 소급 변경하지 않는다.
- 2026-09-09 GitHub 재조회: infra-ansible PR #1 merged=true, merge SHA 4f9bdb7c08704eebb3d1b294751e51b0721b6af4. 기존 완료 기록을 이관하며 신규 Runtime 검증/승인을 생성하지 않는다.
- [현행 정본 v3.1.17](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/baseline/FDS_Project_Implementation_Baseline_v3.1.17.md) · [정본 WBS](https://github.com/321Team/fds-project-baseline/blob/2d93395a0e19ea67e5be199d7183a7edbaa6cf4c/wbs/FDS_v3.1.17_WBS_and_Gantt_v1.0.xlsx).
- 본문은 아래에 적힌 원본 버전의 기록이다. 위 속성·후속 승인과 다른 과거 상태는 현재 판정으로 사용하지 않는다. 이관 자체로 미실행 AC를 체크하거나 새 승인을 부여하지 않는다.
- Lead/Support의 풀네임은 본문 속성으로 보존한다. GitHub 계정 대응이 확인되지 않은 사람에게 자동 배정하지 않았다.

## 원본 및 변경 출처

- `CR-P1-ANS-01-01_ICR-D-NET-01-01_Notion_배포안_2026-09-08.md`

---

## Description — 보관 입력본

> 원본: `CR-P1-ANS-01-01_ICR-D-NET-01-01_Notion_배포안_2026-09-08.md`. 원본의 완료/미완료 체크와 당시 이력을 보존했다.

### 🎯 User Story

인프라 자동화 담당자로서 Ansible을 통해 Kubernetes 6개 Node의 DNS Client 설정을 승인된 DNS 이중화 구성으로 일관되게 전환한다. 이를 통해 반복 실행 시 불필요한 변경이 발생하지 않도록 하고, 장애 발생 시 재현 가능한 Rollback과 검증 가능한 Evidence를 확보한다.

---

### 📌 Scope

#### In Scope

- Kubernetes Control Plane 3대와 Worker 3대의 Resolver 전환
- DNS Server `.52 → .53` 순서 및 `fds.internal` 검색 도메인 적용
- `k8s-api.fds.internal` 및 `k8s-api` 해석 검증
- 외부 DNS와 승인 DNS 직접 질의 검증
- kubelet/containerd 회귀 점검
- Apply, Check Mode, 멱등성, Rollback 및 SHA-256 Evidence 관리
- 독립 Support Review와 Lead 수동 승인·병합

#### Out of Scope

- Kubernetes API 인증 성공 판정
- P1-LB-01 Stage B Backend UP, Failover/Recovery 판정
- kubeadm init/join 착수 승인
- ICR-D-NET-01-01의 Calico HostEndpoint/GNP 및 관리망 반환 경로 변경

---

### 📋 핵심 요구사항

- [x] Kubernetes 6개 Node의 DNS Server를 `.52 → .53` 순서로 적용한다.
- [x] 검색 도메인 `fds.internal`을 적용한다.
- [x] NetworkManager의 자동 DNS 덮어쓰기를 차단한다.
- [x] FQDN, Short Name, 외부 DNS 및 승인 DNS 직접 질의를 검증한다.
- [x] kubelet/containerd 서비스 회귀가 없음을 확인한다.
- [x] Apply와 Check Mode의 실행 결과를 분리해 기록한다.
- [x] 반복 실행 시 `changed=0`, `failed=0`, `unreachable=0`을 확인한다.
- [x] Rollback 절차와 Evidence Index·SHA256SUMS를 남긴다.
- [x] 고정 HEAD에 대한 독립 리뷰와 Lead 수동 승인 후 병합한다.

---

### ✅ Acceptance Criteria

- [x] `CR-DNS-AC-01` — 6개 Node의 DNS 순서가 `.52 → .53`이다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-02` — 6개 Node에 검색 도메인 `fds.internal`이 적용된다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-03` — `k8s-api.fds.internal`이 `.109`로 해석된다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-04` — Short Name `k8s-api`가 `.109`로 해석된다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-05` — 외부 DNS 해석이 정상이다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-06` — 승인 DNS 직접 질의가 정상이다. 결과: 12/12 PASS.
- [x] `CR-DNS-AC-07` — kubelet/containerd 서비스 회귀가 없다. 결과: 6/6 PASS.
- [x] `CR-DNS-AC-08` — 멱등성 결과가 `changed=0`, `failed=0`, `unreachable=0`이다. 결과: PASS.
- [x] `CR-DNS-AC-09` — Rollback 자료·절차·검증 결과가 확보됐다. 결과: PASS.
- [x] `CR-DNS-AC-10` — Evidence 원본·Index·SHA-256 무결성을 확인했다. 결과: PASS.
- [x] `CR-DNS-AC-11` — 이하영 Support Review가 승인됐다. 결과: `APPROVED`, 2026-09-07 11:13:58 KST.

---

### 🧪 검증 및 증적

- 저장소: `321Team/infra-ansible`
- Pull Request: [PR #1](https://github.com/321Team/infra-ansible/pull/1)
- 승인 대상 HEAD: [`507d8882a04f53640b07251bcc234b7d6ee81c09`](https://github.com/321Team/infra-ansible/commit/507d8882a04f53640b07251bcc234b7d6ee81c09)
- 병합 Commit: [`4f9bdb7c08704eebb3d1b294751e51b0721b6af4`](https://github.com/321Team/infra-ansible/commit/4f9bdb7c08704eebb3d1b294751e51b0721b6af4)
- 병합 시각: 2026-09-07 15:02:55 KST
- GitHub Actions/Commit Status: 실행 0건 — **NOT RUN**, CI PASS로 간주하지 않음
- Control Plane Apply: 2/2, `changed=4`, 실패 0
- Control Plane Idempotency: 2/2, `changed=0`, 실패 0
- Worker Apply: 3/3, `changed=4`, 실패 0
- Worker Idempotency: 3/3, `changed=0`, 실패 0
- Corrected Check Mode API Check: 5/5 실행, `changed=0`
- 6개 Node 최종 재검증: 6/6, `changed=0`, 실패 0
- 승인 DNS 직접 질의: 12/12
- Kubernetes API Listener 전·후: 6/6
- 외부 DNS: 6/6
- kubelet/containerd 회귀 없음: 6/6

| Evidence 대상 | SHA-256 |
|---|---|
| `EVIDENCE_INDEX` | `6f5568d805a5d7f43130d2fdca2ba631358f4f8be23e1f7d0799ae8243c7db1e` |
| `SHA256SUMS` | `05de9ba6b22d36ef8fc67bdf3dd8c6629c3e334fbb61620a265a46acdbfd4115` |
| 6개 Node 최종 로그 | `18cbda0fc7d91ebf58c89c230dccabaf9ad8239305856da03067210582194e83` |
| 무결성 로그 | `35a320650312e343764a5d7eecfe70c42bafcf43c8043a422d920030a20dee14` |
| 재최종화 기록 | `db7da7eae13c1b07e6b073003a23229e76f3a86f6903a66ac9a2cf522f84395d` |

> 원시 Runtime Evidence는 `ansible01`에서 생성되어 Git 추적 제외 대상으로 관리된다. 이번 판정은 PR에 고정된 해시 기록과 독립 승인 리뷰를 근거로 하며, 이번 검토에서 원시 파일 자체를 다시 실행하거나 재수집하지 않았다.

---

### 🔗 Dependency

- 선행 기준: P1-DNS-01 승인 DNS 구성과 D08/D09 DNS 결정
- 연동 기준: P1-LB-01 Stage A Listener와 API Endpoint `.109:6443`
- 후속 영향: P1-K8S-01의 kubeadm Bootstrap 전 DNS 선행조건 제공
- 통제 사항: 본 CR의 완료만으로 P1-LB-01 Stage B, Kubernetes API 인증 또는 kubeadm init/join을 승인하지 않는다.

---

### ⚖️ Decision / Risk Control

- `D08`, `D09`: DNS Server 순서와 `fds.internal` 해석 기준을 유지한다.
- `D34`, `D35`: 설계 승인과 Runtime 상태를 분리하고 Interface 정본을 준수한다.
- `RISK-02`: 단일 DNS 또는 Resolver Drift 위험을 이중 DNS와 멱등성 검증으로 통제한다.
- `RISK-04`: 네트워크 경로 오판을 FQDN/Short Name/직접 질의/외부 DNS 검증으로 통제한다.
- `RISK-07`: 증적 누락과 상태 과대판정을 Evidence Index, SHA-256 및 독립 리뷰로 통제한다.
- GitHub Actions가 실행되지 않았으므로 CI PASS를 주장하지 않는다.

---

### 🤝 Review / Handoff

- Reviewer: 이하영 (`hayeounglee`)
- Review 결과: `APPROVED`
- Review 시각: 2026-09-07 11:13:58 KST
- Review 대상: HEAD `507d8882a04f53640b07251bcc234b7d6ee81c09`
- 최종 수동 승인: 이권욱
- 병합 결과: 2026-09-07 15:02:55 KST, Merge Commit `4f9bdb7c08704eebb3d1b294751e51b0721b6af4`
- 후속 Handoff: P1-K8S-01은 별도 Gate와 실제 Runtime 조건을 확인한 후 착수한다.

---

### 🏁 Completion Record

- Acceptance 11/11: **충족**
- Runtime Evidence 및 SHA-256: **충족**
- 독립 Reviewer 승인: **충족**
- Lead 수동 승인: **충족**
- 승인 HEAD 병합: **충족**
- 비밀정보를 Git에 포함하지 않는 Evidence 관리: **충족 기록 확인**
- GitHub Actions CI: **NOT RUN** — 별도 PASS 주장 없음
- 최종 판정: **Done**
- 완료일: **2026-09-07**

`CR-P1-ANS-01-01` 완료는 Kubernetes API 인증, P1-LB-01 Stage B, kubeadm init/join 또는 ICR Runtime 완료를 의미하지 않는다.

다음 정본 발행 시 Baseline Project Status Register, WBS/Gantt, Canonical Ticket Pack, `docs/change/CR-P1-ANS-01-01.md`, Release Notes, Manifest, SHA256SUMS, Audit 및 WEB을 `Done` 상태로 동기화한다. WBS/Gantt는 내용 변경 여부와 관계없이 ZIP 및 독립 Release Asset에 포함한다.
````

</details>

