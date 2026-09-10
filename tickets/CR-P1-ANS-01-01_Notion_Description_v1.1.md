<!-- fds-canonical-description:v3.1.18 record-id:CR-P1-ANS-01-01 -->
# CR-P1-ANS-01-01 — Ansible Kubernetes Node DNS Resolver 변경

> 정본 후보: v3.1.18 / CANDIDATE · 기준일 2026-09-10
> 독립 리뷰·최종 승인·발행 전에는 운영 정본 v3.1.17이 유효하다. 본 문서는 발행 후 Description 갱신용 후보이며 실제 Issue에는 아직 적용하지 않았다.

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

## 현재 실행·검토 상태

2026-09-07 CR 최종 승인·병합 완료. 승인 HEAD 507d8882a04f53640b07251bcc234b7d6ee81c09, merge 4f9bdb7c08704eebb3d1b294751e51b0721b6af4, AC 11/11은 당시 실행·Support 승인 기록에 근거한다. CI NOT RUN. FUP-01 원본 보완·독립 편입과 증적 PR #1 병합은 완료됐으며 Stage A 조건부 인수의 잔여 조건, Bootstrap 해제·Stage B는 별도다.

근거: [Issue #58](https://github.com/321Team/fds-project-baseline/issues/58), Issue 갱신 시각 `2026-09-09T12:14:54Z`. 댓글·승인 기록과 본문 보관본은 `v3.1.18/source-snapshot.json`에 보존하고 실제 Gate는 해당 증적·승인 범위로 판정한다.

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
