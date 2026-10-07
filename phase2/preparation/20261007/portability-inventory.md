# 이식성 소스 대조 결과

범위: latest main의 앱 reference snapshot, Kubernetes security 참고 manifest·NetworkPolicy·RBAC, infra-rosa의 기존 admission-only 도구를 읽었다.
판정: **STATIC 입력 분류 완료 / PORTABLE_BASE·PG03·ROSA Runtime 미판정**.

## 원본 성격부터 구분

- [fds-msa README](https://github.com/321Team/fds-msa/blob/0494ca279882d4e0cab24fb5a25a136a2e8f46c1/README.md)는 references/upstream/kubernetes를 **검토용 snapshot, 정본 배포 입력 아님**으로 명시한다.
- [#43 계약](https://github.com/321Team/fds-project-baseline/issues/43)은 Phase 1 YAML이 분산되어 있으므로 portable base/OpenShift overlay를 별도 고정하도록 한다.
- [02-securitycontext.yaml](https://github.com/321Team/infra-kubernetes/blob/c3057906a6a8427a4b315b7e544e063efe0fecf2/manifests/02-securitycontext.yaml)도 APP/MON 원본에 적용할 patch 참고자료라고 명시한다.
- 따라서 snapshot의 latest tag·과거 image digest·CPU/memory 숫자를 이번 P2 승인값으로 복사하지 않는다. 실제 승인 APP source·digest·resource는 #43 producer가 인계한다.

## 확인 사실과 준비 조치

| 원본 위치 | 정적 확인 사실 | 준비에 반영한 처리 / Runtime 재검증 |
|---|---|---|
| fds-msa reference의 두 Deployment | runAsUser=10001, fsGroup=10001, image :latest | reference만으로 최종 SecurityContext/image 선택 금지. 승인 digest의 arbitrary UID와 필요한 파일 쓰기를 실제 확인 |
| Kubernetes 02-securitycontext.yaml | runAsUser=10001/runAsGroup=999, non-root·RuntimeDefault·drop ALL·read-only rootfs | fixed UID만 제거하면 전체 이식성 PASS라는 결론 금지. custom/broad SCC 우회 없이 #38/#43 portable overlay 검증 |
| 같은 파일 | 업무8000/8001, metrics9091/9090, Service80→8000, Secret DATABASE_URL 참조 | 기존 업무/metrics/DB actor 계약을 유지. 실제 app manifest key/reference를 portable base에 연결 |
| [03-networkpolicy.yaml](https://github.com/321Team/infra-kubernetes/blob/c3057906a6a8427a4b315b7e544e063efe0fecf2/manifests/03-networkpolicy.yaml) | edge01 10.1.93.50/32 ingress·DB10.1.93.55/32 egress·kube-system/kube-dns DNS selector | On-Prem·CNI 관련 값이다. P2 Route/ingress·DNS·actual source adapter로 분리하고 범위 확대로 우회하지 않음 |
| 같은 파일 | API→engine8001 / API→DB5432; engine→DB 허용 없음 | P2에서도 DB actor=transaction-api 유지. engine에 DB credential/egress를 새로 주지 않음 |
| 같은 파일 monitoring 경로 | CP/worker 개별 IP, monitor01 10.250.10.30 | P0 앱 base와 full monitoring 이식 책임 분리. 이 값들을 ROSA node 정보로 복제하지 않음 |
| [06-rbac.yaml](https://github.com/321Team/infra-kubernetes/blob/c3057906a6a8427a4b315b7e544e063efe0fecf2/manifests/06-rbac.yaml) | 앱 SA token automount=false; Runner role은 두 named Deployment get/update/patch | 최소권한 intent를 P2로 연결. target namespace/SA/trust/credential는 #38/#46의 별도 실제 입력 |
| [infra-rosa W0](https://github.com/321Team/infra-rosa/blob/a37b10628cd59427c45dd28e2f6bd924891e1c54/precheck/portability/README.md) | 조회+server-side dry-run만 수행. 실제 Pod/Namespace/SCC 생성 없음. ENV=SHARED_OCP_LAB 또는 ROSA | 기존 Admission 검증기를 재구현하지 않음. 전제·환경 값 정합화 후 재사용; 실제 Running/Ready/imageID·filesystem·cleanup은 별도 LAB-PRECHECK 실측 |

## 준비 결과가 확정하는 범위

이번 산출물은 참고 source의 성격·고정값·이식 시 검증 지점을 분류했다. P1 manifest diff는 0이다.
승인된 P1 source와 실제 digest를 받은 뒤 #43에서 portable base와 OpenShift overlay를 구현한다.
DB/FDS 장애 기대결과는 [#119 Lead 승인](https://github.com/321Team/fds-project-baseline/issues/119#issuecomment-5928210700)과 최신 #15 AC를 소비한다.

## Lab 시험에 넘길 최소 입력

| 입력 | 생산 / 확인 |
|---|---|
| 실제 OCP cluster identity/version·API/context·허용 계정/권한 | 환경 제공 범위 확인 → #38 |
| Shared namespace·Quota/허용 범위·초기 상태·cleanup 책임 | Lab 실행 계획 |
| 승인 두 app digest·base/overlay SHA·resource·Secret key 참조 | #43 |
| 실제 target namespace·SCC·UID/GID 할당·trust/registry 경로 | #38/#42 |
| Running/Ready·health·imageID·RO filesystem·허용 volume 쓰기 관측 | LAB-PRECHECK |
| before/after resource inventory·cleanup·원본 명령/RC/log | 실행자 → 독립 증적 심사 |

Arbitrary UID 시험을 위해 앱 rebuild가 필요하면 새 SHA/digest의 변경 영향과 P1/P2 회귀를 연결한다. 현재 P1 이미지를 그 시험을 이유로 교체하지 않는다.

