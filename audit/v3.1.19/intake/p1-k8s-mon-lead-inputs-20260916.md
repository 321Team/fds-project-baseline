# P1-K8S / P1-MON 운영 입력 — Lead 결정 정본 후보

상태: **APPROVED_INPUT / LEAD_DECISION_CONFIRMED / RUNTIME_SEPARATE / PR7_IMPLEMENTATION_PENDING**.
정본 상태: v3.1.19 후보 수집, NOT RELEASED. 운영 정본은 v3.1.18 유지.

## 수집 근거

2026-09-16 사용자 요청에 따라 P1-K8S-01, ICR-D-NET-01-01, P1-MON-01 및
infra-kubernetes PR #7의 최신 의견을 재검토했다.

주요 원문:
- P1-K8S-01 Lead Decision: https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5697547621
- P1-K8S 병행 입력: https://github.com/321Team/fds-project-baseline/issues/10#issuecomment-5696866432
- ICR NTP 요청: https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-5697384866
- P1-MON Storage 인계: https://github.com/321Team/fds-project-baseline/issues/17#issuecomment-5696869601
- Monitoring Lead Storage 의견: https://github.com/321Team/infra-kubernetes/pull/7#issuecomment-5697415810
- Worker NIC 의견: https://github.com/321Team/infra-kubernetes/pull/7#issuecomment-5697260887
- OID-01 의견: https://github.com/321Team/infra-kubernetes/pull/7#issuecomment-5697293093
- 구현 PR: https://github.com/321Team/infra-kubernetes/pull/7

## 정본 후보로 수용하는 승인 입력

### OID-01 관리 Source / Identity

- Management Source: `ansible01 10.250.10.10/32`
- Identity: `svc_ansible`
- Destination: Kubernetes Node TCP/22
- 내부 FDS 목적지 Source NAT 금지
- Return Route: `10.250.10.0/24 via 10.1.93.58`
- HEP의 SSH 허용은 승인 관리 Source에 한정
- 실제 HEP/GNP 적용은 3CP+3Worker Ready / 6/6 join 완료 후 별도 실행 승인으로 진행

이 입력은 기존 IF-07 및 Management Source Preservation 계약의 구체화이며 Runtime PASS를 생성하지 않는다.

### Monitoring static local Storage

- designated Storage Worker: `k8s-worker03 (10.1.93.108)`
- host path:
  - `/home/fds-local-pv/prometheus`
  - `/home/fds-local-pv/grafana`
  - `/home/fds-local-pv/alertmanager`
- 기존 정본 통제 유지:
  - `kubernetes.io/no-provisioner`
  - `WaitForFirstConsumer`
  - `Retain`
  - `PersistentVolume.spec.nodeAffinity`
  - 단일 지정 Worker non-HA Known Limitation
- 최종 적용 전 free-space, 경로 충돌, owner/mode, SELinux persistent fcontext/restorecon 재검증

사용자 제출 `server07_worker03.txt`의 SHA-256은
`d7bef0ef1c413dd7e85a221fe8db1563de2b48f2aae4bf4a0e23b812df12287a`이다.
제출본에서 worker03 `/home` XFS 가용량은 약 163G로 확인됐다.
이 원본은 현재 GitHub evidence 저장소에 편입된 파일이 아니므로 Runtime Evidence Archive로 표현하지 않는다.

### Monitoring PVC 초기 sizing

Lead가 다음 값을 **CONFIG_DEFAULT_CANDIDATE**로 채택했다.

| Component | PVC | 비고 |
|---|---:|---|
| Prometheus | 20Gi | `retention.time=15d`, `retention.size<=16GB` |
| Grafana | 5Gi | 상태/Provisioning |
| Alertmanager | 2Gi | Silence/notification 상태 |

합계 27Gi. 실제 cardinality, scrape interval, PVC 사용률에 따라 후속 조정 가능하며 불변 Architecture 값으로 취급하지 않는다.

## 승인됐으나 추가 입력이 필요한 NTP

Lead는 dns01/dns02 Relay 제안을 기각하고 다음을 결정했다.

- K8S Node NTP Source: `control01` 단일 내부 chronyd
- 내부 UDP/123만 사용, 신규 외부 egress 없음
- offset 100ms 이내
- 60초 간격 × 6회
- sync lost 5분 이상 지속 시 FAIL
- reboot 후 5분 이내 재동기화

다만 `control01` 자체가 동기화할 **upstream/time authority와 해당 egress/복구 계약**은 위 결정 원문에 정의되지 않았다.
따라서 `control01` downstream source 선택과 수치 AC는 승인 입력으로 수집하되,
실제 NTP 형상 및 HEP/GNP UDP/123 규칙의 최종 확정은 upstream source가 확인될 때까지
`INPUT_INCOMPLETE / RUNTIME_HOLD`로 유지한다. 단일 Source는 HA로 표현하지 않는다.

## Worker HEP NIC

`ens160`은 Worker01~03의 기본 interface 후보로 의견이 등록돼 있고 적용 직전
IP/route/NetworkManager binding 불일치 시 STOP 조건이 있다.
그러나 Kubernetes/SEC Lead의 #10 최종 Decision에는 NIC 값이 포함되지 않았다.
따라서 v19에서는 `ens160`을 **AS_BUILT_CANDIDATE / OWNER_CONFIRMATION_PENDING**으로 수집하고
불변 정본값으로 승격하지 않는다. 실제 적용창의 read-only 실측 결과를 최종 입력으로 사용한다.

## infra-kubernetes PR #7 구현 상태

정본 후보 입력과 코드 승인은 분리한다.

- DNS egress `.52/.53` 제한은 수정되어 CLOSED_STATIC 후보.
- 9091/9090 metrics 계약, Grafana port-forward-only 방향, image identity placeholder는 최신 수정에서 정본 방향으로 복귀했다.
- Monitoring StorageClass/PV/PVC 구현이 추가됐다.
- P1-APP 전용 metrics listener는 `supreme33-kr/fds-msa#5`로 병합됐으며 작성자 제출 Runtime/pytest 결과가 있다.
- 그러나 PR #7의 기존 SEC-01/02/07/08 코드·증적 오류 경로는 최신 manifest 중심 커밋으로 해소됐다는 근거가 없다.
- 최신 Lead NTP 결정은 Bootstrap GNP에 아직 반영되지 않았고, control01 upstream도 미정이다.
- 최신 HEAD 독립 승인, CI, 실제 Runtime 인수는 별도 확인 대상이다.

따라서 PR #7 자체는 **PENDING_REVIEW / NOT_APPROVED_INPUT**으로 유지하며,
이 문서의 승인 입력 수집을 PR #7 병합·Runtime 승인으로 해석하지 않는다.

## 발행 경계

이 수집은 Baseline/Ticket Pack/Interface/Decision/Release Notes 전체 통합 완료가 아니다.
v3.1.19 최종 HEAD 독립 리뷰와 이권욱의 병합·발행 승인이 별도로 필요하다.
