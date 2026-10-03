# DEC-P1-IMG-01 — 1단계 애플리케이션 런타임 이미지 공급망 변경 결정

Version: v3.1.21 CANDIDATE
Source: https://github.com/321Team/fds-project-baseline/issues/110
Updated at: 2026-09-28T04:36:43Z
Source body SHA256: `a67095086501950e50620f6a6feb872ba09e0349687daf1c293a7b6050a07128`
GitHub: closed / completed
Current disposition: APPROVED_DECISION_ONLY; Delivery Runtime separate.

| Property | Current source value |
|---|---|
| Record ID | DEC-P1-IMG-01 |
| Phase | Phase 1 |
| Category | Application / Container Supply Chain / Security |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-27 |
| End | 2026-10-06 |
| Calendar Days | 10 |
| Working Days | 7 |
| Lead | 이재환 |
| Support | 이하영, 이권욱 |
| Exit Criteria | P1 애플리케이션 런타임 공급망 선택안, signed attestation 처리 방식, 운영 Dockerfile·Harbor·Kubernetes 후속 게이트 및 롤백 조건을 명시적으로 승인 |
| Related Decision IDs | D12; D17; D18; D19; D34; DEC-P1-TLS-01 |
| Related Risk IDs | RISK-06; RISK-07; RISK-08; RISK-09 |
| Source | Baseline v3.1.20; 승인 전 candidate validation HEAD `88b494c58d057303672cc1502021ab4655a4e916`; Source validation Run `36261976339`; attestation probe Run `36261976189`; 승인 구현 `321Team/fds-msa#9` HEAD `0bea0d4fa8ece5ecbf7aa5fd8f054fc24f5556cf`, merge `1c7f3651504097096c3a3fe4a86ac1973e169688` |
| Schedule Note | 기존 G2 계획일은 경과했다. 본 Decision은 2026-10-06 Phase 1 Review / Close 전 공급망 방향을 확정하기 위한 후속 게이트이며, 일정 입력만으로 승인 또는 런타임 완료 상태를 상향하지 않는다. |

## Source checklist

- [x] 런타임 공급망 방식이 하나로 결정된다.
- [x] P1에서 인정할 SBOM / provenance / lockfile / hash 증적 계약이 승인된다.
- [x] GitHub signed attestation의 P1 처리방식이 Option A/B/C 중 하나로 승인된다.
- [x] 운영 Dockerfile 전환 여부와 구현 담당자가 확정된다.
- [x] Harbor 반입 및 digest 검증 게이트가 승인된다.
- [x] Kubernetes dry-run/diff 및 런타임 smoke 선행조건이 승인된다.
- [x] 롤백 및 중단 조건이 승인된다.
- [x] 관련 P1-APP/HBR/CICD/SEC 티켓의 생산·소비 책임이 연결된다.

## Source body snapshot

아래 원문은 보관 문구와 과거 제안을 포함한다. 위 current disposition 및 원문의 최신 명시적 결정이 과거 제안보다 우선한다. 원문 수정·인수 상태 승격 없음.

# DEC-P1-IMG-01 — 1단계 애플리케이션 런타임 이미지 공급망 변경 결정

<!-- decision-complete-20260927:issue-110:start -->
## 최신 승인·완료 판정 — 2026-09-27 KST

**Decision 상태: APPROVED / DONE.**

- Review Owner `hayeounglee`가 DEC-01~04와 7개 중단 조건을 명시적으로 승인했다.
- Lead `supreme33-kr`의 추가 조건(담당 배정, SEC-04 기준 UID/GID `10001:999`, 2026-10-05 현장 전환 목표, smoke 실패 시 rollback, 2026-10-06 미완료 시 운영 전환만 후속 이관)도 Review Owner가 확인했다.
- 따라서 본 Decision의 Exit Criteria인 **공급망 선택·증적 계약·signed attestation 처리·후속 구현 Gate·롤백/중단 조건 승인**은 충족됐다.
- `fds-msa#9` Source 병합 및 이후 구현 PR 진행은 Decision 승인 후속 실행이며, 본 Decision 종료가 on-prem Test→Build→Scan, Harbor Push, Kubernetes Deploy 또는 P1 Delivery Runtime PASS를 뜻하지 않는다.
- 승인된 런타임 계정 계약은 후보 초기값 `65532`가 아니라 **SEC-04 manifest 기준 `runAsUser=10001 / runAsGroup=999`**이다.
- Native GitHub Issue Type은 REST 기준 아직 `type=null`이다. 정책 맵 보정 PR #111은 승인·병합됐으나 native type apply는 별도 메타데이터 후속이며, Decision 내용/승인 자체의 Exit Criteria에는 포함하지 않는다.

근거: Review Owner 승인 comment `5852885654`, 추가 조건 확인 comment `5855626610`, Lead 확정 comment `5856632297`.
<!-- decision-complete-20260927:issue-110:end -->

---


> **적용 기준:** `docs-v3.1.20` 및 이후 정식 변경결정  
> **발행일:** 2026-09-27 KST  
> **현재 상태:** 완료 / 승인 확정  
> **변경 경계:** Wolfi/apko 채택과 `fds-msa#9` Source 병합은 승인·완료됐다. 다만 이 Decision 완료는 on-prem Test→Build→Scan, Harbor Push, Kubernetes Deploy 또는 P1 Delivery Runtime PASS 완료를 의미하지 않는다.

## 요약

기존 Python 3.13 런타임 이미지 후보는 동일한 Trivy 보안 기준에서 HIGH 취약점 또는 공급망 정합성 문제로 차단됐다. 이에 보안 기준을 완화하지 않고 **Wolfi + apko 기반 Python 3.13 런타임 공급망 후보**를 검증했으며, 재현 빌드·고정 lockfile·SPDX SBOM·애플리케이션 기동 시험·Trivy `HIGH=0 / CRITICAL=0`을 모두 통과했다.

다만 GitHub private repository의 signed attestation 기능은 현재 321Team 조직 플랜에서 사용할 수 없는 것으로 실측됐다. 따라서 본 Decision은 **Wolfi/apko 공급망 채택 여부, P1에서 인정할 증적 계약, signed attestation 제약 처리 방식, 승인 후 Dockerfile→Harbor→Kubernetes 적용 순서**를 확정하기 위한 의사결정 티켓이다.

후보 기술 검증 이후 **Wolfi + apko Python 3.13 공급망 채택, P1 증적 계약, signed attestation Option A, 후속 구현 Gate 및 중단/롤백 조건이 승인됐다.** 운영 Dockerfile·Harbor·Kubernetes의 실제 실행과 Runtime 인수는 관련 Task에서 별도로 검증한다.

## 티켓 속성

| Property | 입력값 |
| --- | --- |
| Record ID | DEC-P1-IMG-01 |
| Phase | Phase 1 |
| Category | Application / Container Supply Chain / Security |
| Type | Decision |
| Status | Done |
| Priority | P0 |
| Start | 2026-09-27 |
| End | 2026-10-06 |
| Calendar Days | 10 |
| Working Days | 7 |
| Lead | 이재환 |
| Support | 이하영, 이권욱 |
| Review Owner | 이하영 |
| Milestone | G2 Security / Feature Ready |
| Exit Criteria | P1 애플리케이션 런타임 공급망 선택안, signed attestation 처리 방식, 운영 Dockerfile·Harbor·Kubernetes 후속 게이트 및 롤백 조건을 명시적으로 승인 |
| Related Tickets | P1-APP-01 #15; P1-HBR-01 #13; P1-CICD-01 #16; P1-SEC-01 #19 |
| Related PR | `321Team/fds-msa#9` |
| Related Decision IDs | D12; D17; D18; D19; D34; DEC-P1-TLS-01 |
| Related Risk IDs | RISK-06; RISK-07; RISK-08; RISK-09 |
| Evidence Path | `321Team/fds-project-evidence:evidence/DEC-P1-IMG-01/` |
| Source | Baseline v3.1.20; 승인 전 candidate validation HEAD `88b494c58d057303672cc1502021ab4655a4e916`; Source validation Run `36261976339`; attestation probe Run `36261976189`; 승인 구현 `321Team/fds-msa#9` HEAD `0bea0d4fa8ece5ecbf7aa5fd8f054fc24f5556cf`, merge `1c7f3651504097096c3a3fe4a86ac1973e169688` |
| Schedule Note | 기존 G2 계획일은 경과했다. 본 Decision은 2026-10-06 Phase 1 Review / Close 전 공급망 방향을 확정하기 위한 후속 게이트이며, 일정 입력만으로 승인 또는 런타임 완료 상태를 상향하지 않는다. |

## 사용자 스토리

애플리케이션 담당자로서 `transaction-api`와 `fds-engine`의 Python 3.13 런타임 이미지 공급망을 보안 게이트를 완화하지 않고 재현 가능한 방식으로 확정한다.

이를 통해 기존 distroless 계열 후보의 취약점 차단을 우회하지 않으면서 빌드 입력, lockfile, SBOM, provenance, Harbor 반입 및 Kubernetes 배포까지 동일한 추적 기준으로 연결한다.

## 범위

### 포함 범위

- P1 `transaction-api` / `fds-engine`의 builder/runtime 기반 이미지 계열 결정
- Python 3.13 런타임 공급망과 apko/Wolfi 적용 여부
- apko 설정과 저장소에 고정한 lockfile
- SPDX SBOM, project provenance, SHA256 검증
- Trivy `HIGH=0 / CRITICAL=0` 보안 게이트 유지
- GitHub signed attestation의 P1 적용 여부와 현재 조직 플랜 제약 처리
- 승인 후 운영 Dockerfile → Harbor → Kubernetes 단계별 적용 게이트
- 실패 시 중단 및 복구 기준

### 결정 당시 제외 범위 (승인 전)

아래 항목은 Decision 승인 전 단계의 변경 경계이며, 현재 승인·병합 상태를 나타내는 문구가 아니다.

- 승인 전 운영 Dockerfile 변경
- 승인 전 Harbor 푸시 또는 미러링
- 승인 전 Kubernetes 배포
- vulnerability ignore 또는 allowlist를 이용한 보안 게이트 우회
- SBOM 삭제 또는 scanner source 제한으로 취약점 0건을 만드는 조치
- P1-SEC-01에서 제외한 P2 Admission Policy / Image 서명 강제를 자동으로 P1 필수 AC로 확대하는 변경
- GitHub 조직 Billing Plan 변경 자체

## 배경 및 후보 검증

`fds-msa#9`에서 Python 3.13 런타임 후보를 동일한 HIGH/CRITICAL 기준으로 검증했다.

| 후보 | 결과 | 판정 |
| --- | --- | --- |
| `gcr.io/distroless/python3-debian13` | 두 서비스 HIGH22 / CRITICAL0 | 차단 |
| Red Hat Hardened Python 3.13 | embedded SBOM HIGH2 / CRITICAL0 | 차단 |
| `python:3.13-alpine` | embedded SBOM HIGH2 / CRITICAL0 | 차단 |
| distroless cc + CPython copy | shared-library / package metadata / SBOM inventory 정합 문제 | 보류 |
| Chainguard Python 3.13 / 3.13-dev | public control 정상, 특정 3.13 tag는 current anonymous input에서 `MANIFEST_UNKNOWN` | 사용 불가 |
| **Wolfi + apko** | 재현성, lock↔SBOM, smoke/livez, Trivy 0/0 | **기술 검증 통과** |

취약점 finding을 무시하거나 보안 게이트를 낮추지 않았다.

## 검증 완료한 Wolfi / apko 후보

### 승인 전 기술 후보 고정 입력 (Historical)

- `fds-msa` 정확 HEAD: `88b494c58d057303672cc1502021ab4655a4e916`
- apko 버전: `v1.4.4`
- apko release archive SHA256: `dbd9e8f416903b2d896497c51f3217259d03ecb45c997254cedca5274e8671db`
- builder 설정: `ci/apko/wolfi-python313-builder.apko.yaml`
- runtime 설정: `ci/apko/wolfi-python313-runtime.apko.yaml`
- builder/runtime apko lockfile: 저장소에 고정
- builder: Python 3.13 + pip + 빌드용 shell
- runtime: Python 3.13 + CA bundle + tzdata
- runtime UID: `65532` — **승인 전 기술 후보 값(Historical)**. 최종 승인 운영 계약은 `10001:999`이며, 후보 증적의 재현성을 위해 이 값은 해당 candidate HEAD의 이력으로 보존한다.
- runtime `apk-tools`: 미포함

### 정확 HEAD 기준 CI

- Source validation Run `36261976339`: **성공**
  - `validate`: 성공
  - `candidate-images-apko / validate`: 성공
  - 기존 `candidate-images`: 건너뜀 — PR #7 전용 유지
- Python 3.13 lock candidate Run `36261976104`: **성공**

### apko / 런타임 게이트

- 저장소 고정 lockfile 재생성 일치: **통과**
- builder 2회 재현 빌드 일치: **통과**
- runtime 2회 재현 빌드 일치: **통과**
- lockfile ↔ SPDX SBOM 정합성: **통과**
- Python `3.13.15`: **통과**
- tzdata `2026d` / `ZoneInfo("Asia/Seoul")`: **통과**
- transaction-api import smoke / `/livez`: **통과**
- fds-engine import smoke / `/livez`: **통과**
- transaction-api Trivy: **HIGH0 / CRITICAL0**
- fds-engine Trivy: **HIGH0 / CRITICAL0**
- `PROVENANCE.json`: 생성 완료
- evidence `SHA256SUMS`: **통과**

## 서명 증명(Attestation) 플랫폼 제약

GitHub 공식 `actions/attest@v4`를 private repository에서 실제 capability probe로 검증했다.

- Run: `36261976189`
- action commit: `1e69f48acb82d1966a394da916b4c1698aa569d6`
- 대상: 저장소에 고정한 apko builder/runtime lockfile
- 대상 SHA256 검증: 통과
- attestation 저장: **차단**
- GitHub 원문: `Feature not available for the 321Team organization. To enable this feature, please upgrade the billing plan, or make this repository public.`
- attestation ID / URL: 없음
- 판정: **현재 조직 플랜에서 사용 불가**

이는 Wolfi/apko 후보의 기술 실패가 아니라 현재 GitHub 조직 플랜 제약이다.

## 승인된 결정 항목

### DEC-01 — 런타임 공급망

P1 애플리케이션 런타임 기반 이미지를 기존 distroless Python 후보에서 **apko로 빌드한 Wolfi Python 3.13**으로 변경하는 것으로 승인했다.

### DEC-02 — P1 증적 계약

다음 항목을 P1 공급망의 공식 입력·검증 증적으로 인정한다. 단, 최종 Delivery Runtime 인수는 on-prem 검증과 별도로 구분한다.

- apko 설정
- 저장소 고정 apko lockfile
- 2회 재현 빌드 결과 일치
- SPDX SBOM
- project `PROVENANCE.json`
- evidence SHA256
- Trivy HIGH0 / CRITICAL0
- 애플리케이션 smoke / `/livez`

### DEC-03 — Signed Attestation 처리

- **Option A — 승인:** 현행 P1-SEC-01 범위를 유지하고 GitHub signed attestation 불가를 P1의 잔여 플랫폼 제약으로 기록한다. 이미지 서명 및 강제 정책은 P2 또는 별도 후속 Decision에서 처리한다.
- Option B: GitHub Enterprise Cloud 등 기능 사용이 가능한 조직 플랜을 확보한 뒤 signed attestation을 P1 병합/배포 선행조건으로 추가한다.
- Option C: 외부 cosign/Sigstore 또는 별도 signing-key lifecycle을 새로운 P1 변경으로 설계한다.

### DEC-04 — 승인 후 구현 게이트

승인 후 다음 순서로 진행한다.

1. 운영 Dockerfile을 승인된 apko/Wolfi 계약으로 전환
2. 정확 HEAD 기준 Source validation / apko Gate 재실행
3. 독립 코드 리뷰
4. Harbor 후보 이미지 푸시/미러링
5. Harbor manifest digest / Trivy 재확인
6. Kubernetes server-side dry-run / diff
7. 런타임 smoke 및 P1-APP/P1-SEC AC 연결

## 인수조건

- [x] 런타임 공급망 방식이 하나로 결정된다.
- [x] P1에서 인정할 SBOM / provenance / lockfile / hash 증적 계약이 승인된다.
- [x] GitHub signed attestation의 P1 처리방식이 Option A/B/C 중 하나로 승인된다.
- [x] 운영 Dockerfile 전환 여부와 구현 담당자가 확정된다.
- [x] Harbor 반입 및 digest 검증 게이트가 승인된다.
- [x] Kubernetes dry-run/diff 및 런타임 smoke 선행조건이 승인된다.
- [x] 롤백 및 중단 조건이 승인된다.
- [x] 관련 P1-APP/HBR/CICD/SEC 티켓의 생산·소비 책임이 연결된다.

## 검증 및 증적

- `321Team/fds-msa#9`
- Source validation Run `36261976339`
- Python 3.13 lock candidate Run `36261976104`
- Candidate attestation capability Run `36261976189`
- `fds-project-evidence:evidence/DEC-P1-IMG-01/` — 향후 정식 편입 위치
- 관련 Task: #15 / #13 / #16 / #19

## 의존성

- **선행 차단:** Decision 승인 자체 외 기술 선행 차단 없음. 후보 기술 검증은 통과.
- **후속 실행 대상:** on-prem Test→Build→Scan, Harbor 후보 이미지 반입·digest 검증, Kubernetes dry-run/diff·애플리케이션 Runtime 검증.
- **관련 티켓:** P1-APP-01 #15, P1-HBR-01 #13, P1-CICD-01 #16, P1-SEC-01 #19.
- **Milestone 기여:** G2 Security / Feature Ready의 Application / Security / Delivery 잔여 연결.

## 결정 및 위험 통제

- Trivy `HIGH=0 / CRITICAL=0` 기준을 유지한다.
- vulnerability ignore / allowlist를 승인 우회 수단으로 사용하지 않는다.
- apko 도구 버전 및 release archive hash를 고정한다.
- builder/runtime lockfile을 저장소에 고정하고 재생성 일치를 검증한다.
- SPDX SBOM / provenance / SHA256 원본을 보존한다.
- 최종 승인 운영 runtime은 non-root UID/GID `10001:999`를 사용한다. `65532`는 승인 전 candidate 검증 이력으로만 보존한다.
- runtime에는 package manager를 포함하지 않는다.
- Harbor 푸시 / Kubernetes 배포는 Decision 승인 후 별도 게이트에서 수행한다.
- GitHub signed attestation 미지원 상태를 기술 검증 통과로 바꾸지 않고 별도 플랫폼 제약으로 기록한다.

## 롤백 및 중단 조건

승인 전 candidate 단계에서는 런타임/Harbor 변경이 없어 **PR #9 미통합 유지**가 롤백 경계였다. 현재 PR #9은 병합 완료이며, 실제 운영 전환의 rollback digest와 manifest는 후속 구현에서 고정한다.

후속 구현에서 다음 중 하나라도 발생하면 즉시 중단한다.

- 저장소 고정 lockfile 재생성 불일치
- apko reproducibility 실패
- 어느 서비스든 HIGH 또는 CRITICAL > 0
- smoke / `/livez` 실패
- Harbor manifest digest 불일치
- Kubernetes diff가 승인 범위를 초과
- 기존 P1-APP / P1-SEC 계약 회귀 발생

기존 distroless 후보는 보안 게이트를 통과하지 못했으므로 자동 롤백 대상으로 사용하지 않는다. 실제 운영 전환에 사용할 rollback digest와 manifest는 구현 단계에서 별도로 고정한다.

## 검토 및 인계

- **Lead:** 이재환
- **Support:** 이하영, 이권욱
- **Review Owner:** 이하영
- **Application:** #15 — 운영 Dockerfile/base-family 전환 및 애플리케이션 런타임 검증
- **Registry:** #13 — Harbor push/mirror, digest, registry-side Trivy
- **CI/CD:** #16 — 승인된 공급망/digest를 배포 게이트에 연결
- **Security:** #19 — HIGH0/CRITICAL0, SBOM/provenance, signing P1/P2 경계 검토

## 완료 기록

- 결과: **APPROVED — DEC-01~04 및 중단/롤백 조건 확정**
- 상태: **Done**
- 후보 기술 검증: **통과**
- Source validation: **통과**
- GitHub Signed Attestation: **Option A 승인 — 현재 조직 플랜 제약으로 P1 잔여 플랫폼 제약 기록**
- 공급망 채택: **Wolfi + apko Python 3.13 승인**
- 런타임 UID/GID 계약: **10001:999**
- 운영 Dockerfile/이미지 계약 Source: **PR #9 병합 완료 / on-prem Runtime 검증은 후속**
- Harbor Push: **후속 구현 범위 / 본 Decision 완료와 별도**
- Kubernetes Deploy: **후속 구현 범위 / 본 Decision 완료와 별도**
- PR #9 Merge: **완료 — merge `1c7f3651504097096c3a3fe4a86ac1973e169688`**
- 완료일: **2026-09-27 KST**
- Lead: **이재환(`supreme33-kr`)**
- Review Owner / 승인자: **이하영(`hayeounglee`)**
- 승인 근거: comment `5852885654`, 추가 조건 확인 `5855626610`, Lead 확정 `5856632297`
- 경계: **Decision 완료 ≠ Delivery Runtime PASS / Harbor Push / Kubernetes Deploy 완료**
