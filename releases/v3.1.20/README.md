# v3.1.20 — RELEASED / 발행 전 후보 이력 보존

> **현재 상태 정정 — 2026-09-30 KST**  
> `docs-v3.1.20`은 **2026-09-23 02:37:13 KST에 실제 발행된 현행 운영 정본**이다. 아래의 `CANDIDATE / COLLECTING / 정식 발행 보류` 표현은 2026-09-21~22 후보 수집 당시의 역사 기록이며 현재 배포 상태로 해석하지 않는다. 실제 발행 상태는 `CURRENT.md`와 GitHub Release API가 우선한다.  
> 이 정정은 v3.1.20 Tag/Asset/SHA256SUMS를 소급 변경하지 않는다. main-side 상태 설명의 정정은 차기 정본 후보 `release/v3.1.21` / Draft PR #112에서 추적한다.

## 후보 수집 당시 목적 — 역사 기록

이 브랜치는 v3.1.19 이후 발생하는 governance/tooling/티켓 변경분을 **정식 v3.1.20 발행 시점까지 모아두는 후보 수집 지점**이다. RELEASE_POLICY §2.3(완료 변경 요청의 정본 동기화) 대상이 쌓이면 이 브랜치 위에 반영하고, 정본 Lead가 실제 발행을 결정할 때 §2의 10개 필수 산출물(Baseline, WBS/Gantt, Ticket Pack, Release Notes, Manifest, SHA256SUMS, Architecture, Integrity Audit, ZIP, WEB 스냅샷)을 갖춰 완성한다.

## 2026-09-21 전수 감사 기준선 (착수 시점 스냅샷)

PR #86(`audit/canonical-followup-20260921/`)에서 수행한 전수 감사 결과:

- v3.1.19 태그(`966fc5365874b1d259a9810fc876b57c3bfa0e08`, 2026-09-17 23:53:12Z) 이후 **종결된 GitHub Issue 0건**, **`status:done` 라벨을 가진 Open Issue 0건** — WBS/Ticket Pack/Baseline/Architecture 동기화 대상 없음.
- 실제 변경분은 governance/tooling 파일 한정:
  - `governance/GITHUB_IDENTITY_MAP.md`, `RELEASE_POLICY.md`, `TICKET_SYNC_POLICY.md` — 수정 (PR #80, #81)
  - `governance/REVIEW_AUTHORITY_POLICY.md` — 신규 (PR #80, #81에서 수정)
  - `.github/workflows/pr-review.yml` — 신규
  - `README.md` — 수정 (PR #80, #81, #84); v3.1.19 SHA256SUMS에 미등재라 체크섬 영향 없음
  - `.github/workflows/canonical-integrity.yml` — [PR #82](https://github.com/321Team/fds-project-baseline/pull/82) 병합 시 추가 drift 예정 (미병합)
- 각 파일의 등록 해시 대 현재 해시 비교는 `audit/canonical-followup-20260921/checksum-drift.json`(PR #86)을 기준으로 한다.

## 2026-09-22 재감사 (PR #82·#86·#88 병합 반영 후)

main HEAD `639811197242979416b69b3fab4808a52e9eca1e` 기준 재확인 결과:

- v3.1.19 태그 이후 **종결 Issue 여전히 0건**, **`status:done` 라벨 Open Issue 여전히 0건**(전체 Open 49건 라벨 재확인) — WBS/Ticket Pack/Baseline/Architecture 동기화 대상은 하루 전과 동일하게 없다.
- `releases/v3.1.19/SHA256SUMS` 대비 실제 drift 5건(로컬 sha256sum 재계산으로 확인):

| 경로 | 등록 해시(v3.1.19) | 현재 해시 |
|---|---|---|
| `governance/GITHUB_IDENTITY_MAP.md` | `162910ee...` | `be013eb1...` |
| `governance/RELEASE_POLICY.md` | `a8292a14...` | `cce6d6b0...` |
| `governance/TICKET_SYNC_POLICY.md` | `1fb3eb14...` | `53d7d1e7...` |
| `.github/workflows/canonical-integrity.yml` | `ff51d259...` | `8a28df47...` |
| `scripts/verify-canonical-release.sh` | (등재된 원본 해시) | `8ce9d4c4...` |

- SHA256SUMS에 아직 미등재된 신규 파일 2건(체크섬 검사 영향 없음, §2.3상 차기 후보에 추가 등재 필요):

| 경로 | 현재 해시 |
|---|---|
| `governance/REVIEW_AUTHORITY_POLICY.md` | `3a6a2eb8...` |
| `README.md` | `4e5bd6be...` |

`.github/workflows/pr-review.yml`(Gemini AI 리뷰 연동 시도, 중단됨)은 [PR #89](https://github.com/321Team/fds-project-baseline/pull/89)로 제거 진행 중이라 이 목록에서 제외한다.

- 원인: PR #80/#81(governance 정책 개정), PR #82(checkout SHA 고정), PR #88(WARN/FAIL 분리 로직). 전부 §2.4가 신설한 "운영 경로 드리프트" 범주이며 하드 FAIL 대상은 아니다.
- 결론: 하루 전 감사와 실질적으로 동일 — governance/tooling 드리프트만 누적되고 있고, 정식 발행을 지금 강행할 실익은 여전히 낮다.

## 2026-09-22 진행 중 티켓 사양 갱신 (Lead 이재환 요청, 미종결 진행 기록)

이 절은 §2.3 정본 동기화 기준(종결 Issue 또는 `status:done` 라벨)에는 아직 해당하지 않는다. 아래 티켓은 여전히 `In Progress`/`To Do` 상태이며 Baseline/WBS/Architecture 공식 동기화 대상이 아니다. 다만 Lead 이재환의 요청에 따라 v3.1.20 후보 수집 시점에 진행 상황과 발견된 사양 편차를 기록해 둔다.

### 체크리스트 갱신 (Gate2 실행테스트 근거, 이재환 직접 확인)

- [P1-APP-01 #15](https://github.com/321Team/fds-project-baseline/issues/15): "업무 API와 metrics Listener/Service를 분리한다", "업무·메트릭 Port 분리", "R01/R02/R04/R07와 DB 저장 PASS" 체크 — 정본 클러스터 실배포 기준 재검증(이슈 내 2026-09-22 코멘트 참고)
- [P1-DB-01 #11](https://github.com/321Team/fds-project-baseline/issues/11): "transaction-api 저장·조회가 성공한다" 체크
- [P1-E2E-01 #20](https://github.com/321Team/fds-project-baseline/issues/20): "정상 거래 E2E가 성공한다", "R01/R02/R04/R07 기대결과가 일치한다" 체크
- [P1-MON-01 #17](https://github.com/321Team/fds-project-baseline/issues/17): 핵심요구사항 §1 "Kubernetes 내부 배치" 중 3개("monitoring-api 배치 범위", "monitoring-node 배치 범위", "Service는 ClusterIP만 사용") + Acceptance Criteria "Grafana Service는 ClusterIP이며 Ingress·NodePort·LoadBalancer가 0건이다" 체크

각 항목은 티켓 자체 종결이 아니라 개별 체크리스트 항목 단위 확인이며, 티켓 Status·Result·Reviewer/Approver 등 종결 필드는 변경하지 않았다.

### 발견된 사양/구현 편차 (Known Limitation 후보 — 정본 사양 변경 아님)

- **Harbor 이미지 Digest 미고정**: P1-MON-01 사양은 "모든 Image는 Harbor 승인 Repository의 Digest로 고정"을 요구하나, 2026-09-22 실제 배포는 태그 기준(`10.1.93.54/fds/prometheus:latest` 등)으로 진행됐다. Digest 고정은 미완료로 남아 있다.
- **kubelet/node-exporter 크로스노드 스크레이프 실패**: Prometheus가 자신이 위치한 노드 외 나머지 노드의 kubelet(10250)/node-exporter(9100) Target에 도달하지 못한다(TLS SAN 오류·timeout 혼재). GNP가 Pod CIDR(10.244.0.0/16) 발신 트래픽의 노드 간 통과를 허용하는지 재검토가 필요하다. P1-MON-01 AC "App metrics·kube-state-metrics·node-exporter·kubelet·Prometheus self Target이 모두 UP이다" 미충족의 직접 사유다.

위 두 항목은 아직 Decision이나 Change Request로 승인되지 않은 관찰 사실이며, 이 기록 자체가 Baseline/Interface 정본 사양을 변경하지 않는다. 실제 정책 변경이 필요하면 별도 Change Request를 발행한다.

## 2026-09-22 Phase 2 일정 재계획 (Lead 결정)

Phase 1 지연으로 Phase 2 실제 착수(`MS-P2-START-01` #33)가 09-28 → **10-06**로 밀리면서, 정본 §2 일정 Baseline과의 정합을 위해 재계획했다. 프로젝트 최종 종료일 **10-23**(전체 작업 종결 요건), 발표일 **10-26**은 기존 정본 §2(Deliverable Freeze 10-23 / Phase 2 Review 10-23 오후 / Project Close 10-26)와 동일하여 변경하지 않았다.

- **방식**: 뒷단 고정(G6 Hybrid Integration Ready 10-22 ~ Project Close 10-26, 정본 §2 그대로 유지) + 앞단 압축(Phase 2 착수~G5, 원래 24일 → 새 16일, 압축비율 0.667). 전체 구간을 균등 비례압축하지 않고, 이미 확정된 뒷단 마일스톤은 그대로 두고 지연분(8일)만큼 앞단만 압축했다.
- **압축 예외 3건**: `DEC-P2-DNS-01`(#40, D23) · `DEC-P2-OP-01`(#41, D26) · `DEC-P2-REG-01`(#42, D22) — 정본 §14 Decision Register의 결정 시한(2026-10-16)이 이미 고정돼 있어 압축 대상에서 제외하고 원래 Start(10-12)/End(10-16)를 유지했다.
- **반영 대상**: #33~#57 Phase 2 티켓 24건 전체에 각 티켓 코멘트로 일정 갱신을 기록했다. 티켓 본문 속성표는 변경하지 않았다(정본 통합 시점에 일괄 반영 예정).
- 이 갱신은 §4.1(일정 유연성)에 따른 계획 목표 조정이며, 실제 착수·완료·Gate 승인·AC 상태를 변경하지 않는다.

## 후보 수집 당시 수행하지 않았던 것 — 역사 기록

- v3.1.19의 어떤 파일·Tag·SHA256SUMS·GitHub Release도 수정하지 않는다.
- WBS/Gantt·Ticket Pack·Baseline·Architecture 문서를 새로 만들거나 복사하지 않는다 (변경 사유가 없음).
- git tag 생성, GitHub Release 발행, Asset 업로드를 수행하지 않는다 — RELEASE_POLICY §6에 따라 "권한 있는 운영자"의 별도 결정·실행 사항이다.

## 후보 수집 당시 다음 조치 — 역사 기록

1. 이 브랜치를 유지하며 후속 governance/티켓 변경이 쌓이는지 관찰한다.
2. 실제 발행이 필요하다고 판단되는 시점에 §2 필수 산출물을 준비하고 이 PR을 갱신한다.
3. 그 전까지는 **Draft 상태를 유지**하며 병합·Tag·발행을 하지 않는다.
