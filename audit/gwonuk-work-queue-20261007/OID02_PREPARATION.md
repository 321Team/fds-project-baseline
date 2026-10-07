# OID-02 preloaded 보충안 준비 인계 — 2026-10-07

책임 티켓 [#14](https://github.com/321Team/fds-project-baseline/issues/14) / Review 입력 [#30](https://github.com/321Team/fds-project-baseline/issues/30). Owner 이하영, 추적·Review 준비 이권욱. CODEX_ASSISTED.

## 착수 범위

기존 preloaded 선택과 동일 승인 digest를 유지하는 보충안 준비를 우선 진행한다. 기존 [12:55 권고](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6030614541)와 [Owner 잔여 연결](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6031201210)을 하나의 제출 조건으로 묶었다. scheduling 제약 변경·새 egress·Risk Accepted를 채택한 결정이 아니다.

## 대상 고정

| 이미지 | 고정 상위 참조/digest | 보충안 대상 |
|---|---|---|
| kube-controllers | quay.io/calico/kube-controllers@sha256:df00967cbd6d88e1ff3123e1598895845622e2987928b4ebd9d8ac49aefe00c3 | control02, control03, worker01, worker02, worker03 |
| CoreDNS | registry.k8s.io/coredns/coredns:v1.14.2 / sha256:e7e6440cfd1e919280958f5b5a6ab2b184d385bba774c12ad2a9e1e4183f90d9 | worker01, worker02, worker03 |

[PR132](https://github.com/321Team/fds-project-evidence/pull/132) exact cbd2ba82df76a1e40c89fca776f1510e575026b9의 11:59~12:07 읽기 관측을 입력으로 쓴다. control01 cache는 현재 보존 원본 후보다. 과거 공급 출처를 복원한 것으로 표시하지 않는다. 빈 조회행은 특정 ref 미관측이며 호스트의 모든 content 부재를 뜻하지 않는다.

## 다음 제출의 필수 내용

1. 대상 ref·상위 index digest·linux/amd64 child manifest/config/layers와 실제 크기. CoreDNS 상위 index와 플랫폼 child를 구분하고, 전체 플랫폼/현재 플랫폼 보존 및 원래 ref의 digest 결속 방식을 명시한다.
2. 현재 Pod constraint·requests와 노드 조건·잔여 자원의 실효 대조. 기존 “6대 eligible”은 label/taint 후보6대로만 사용한다. 현재 캐시 complete는 해당 플랫폼 content 관측이다.
3. source 계정/권한·고정 경로, export 명령/RC·archive hash, 전달본 hash, 대상별 import·반입 ref/content 검증 계획. import/retag는 실행 승인이 확정되기 전 수행하지 않는다.
4. 1노드씩 진행, mismatch/정리 불명/health 변화의 STOP, 이번 추가 ref만 되돌리는 범위. 광역 content/layer 삭제·cache purge·운영 Pod delete/drain을 복구안에 넣지 않는다.
5. immutable source/목록/출처·실제 공급 결과가 확보된 뒤 renderer system_images path/hash와 OID02 완료조건2~5 연결. runtime-input.json을 미확정 값으로 바꾸지 않는다.

## 순서·성공·중단·복구

- 계획 준비: 이하영의 기존 control01/Ansible 접근 범위에서 입력 확인 → 위 구체안 제출 → 이권욱 #14/#30 Review 준비·해당 Lead의 실행 판단.
- 실행 사전조건: 검토된 정확한 source/명령·대상 노드·권한·경로·비중첩 변경창·현재 상태가 모두 고정돼야 한다. 새 계정/권한/네트워크 예외가 필요한 경우 이번 준비로 허용하지 않는다.
- 준비 완료: 8개 조합 모두의 입력/검증/STOP/복구 계획과 출처 한계가 제출된 상태. 준비 완료를 공급 RUNTIME PASS로 처리하지 않는다.
- 실행 성공: 승인된 창에서 실제 archive/ref/digest/content 검증과 정리·health 원본이 완료된 범위만 판정한다. import 성공만으로 Pod 시작/재Pull/재현성 전체를 주장하지 않는다.
- 현재 회차는 실행하지 않으므로 서버 원복 대상이 없다. 차기 실행안의 ref 단위 원복은 제출·검토 전이며 자동 실행하지 않는다.

## Due·Receiver·처분

- 기존 Due: 2026-10-07 유지.
- 최신 다음 초안 제출: **2026-10-07 18:00 KST**. Owner의 [14:38:23 정정6031725527](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6031725527)이 10/8 12:00을 대체했다. 이는 계획 제출 예정이며 Due 연장 또는 승인된 완료일이 아니다. 18:00 미제출이면 Owner가 사실과 이유를 먼저 기록한다.
- #30의 준비 자료 수신·검토는 기존 Lead 이권욱의 책임 범위다. 잔여 위험을 실제 인수할 Receiver/후속 완료조건과 APPROVED DEFERRED 여부는 별도 판정 전이다.
- OID02 전체 HOLD / OID03 HOLD / import·retag·Pod삭제·Drain·egress 미실행 / AC·Status·일정 변경 없음.

## 최신 Review 연결·수집 경로

- [#14 리뷰6031946801](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6031946801)와 [정정6032030166](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6032030166)을 함께 적용한다.18:00 제출에는 위 source/보존·export/전달 계획, 변경 노드·계정/권한·경로·STOP/추가ref복구 범위와 별도 변경창 GO 요청, 완료조건1~4의 목표 날짜 Due 제안을 담는다.18:00 자체를 완료 Due로 확정하지 않는다.
- 수집 경로는 **A. PR68 동일 승인HEAD 도구 / B. 기존 수동 읽기** 중 하나만 선택하고 첫 줄에 적는다. 같은 항목의 원본이 이미 있으면 그것을 인계하고 재수집하지 않는다. HBR과 같은 실행자이므로 창/세션 중복을 피한다.
- A의 코드 승인: c2f543a16754926c3dd2ecc35773ba09fe1df3a1에 이하영 [APPROVED5438296911](https://github.com/321Team/infra-kubernetes/pull/68#pullrequestreview-5438296911). source_commit_declared는 선언값이므로 실행 output의 collector_sha256을 검토된 도구 SHA256 5f3110ccd9fd3d3f0e7bacb0452baf4d96ff22c3f63369b0737ee47d93b9f8b6과 대조한다. 기존 ZIP SHA256은9564b58842d3af2ff5d479b6725eb809d9e9f2450d4c16c0e30af89c0c190202이며 전달 무결성이지 실행 성공 증거가 아니다.
- stderr 메타데이터 등 후속 의견은 비차단 권고다. 같은계정 기술 의견을 독립 승인으로 계상하지 않으며 수정 소스를 사용할 경우 새HEAD/해시와 해당 변경 검토를 연결한다. 현재 도구는 layer본문 무결성·과거 공급 출처·Pod현상·export/import를 검증하지 않는다.
- 현재 두 Workload의 Pod 위치·실효 constraint/자원을 읽기 원본으로 연결한다. 공급 완료 전 control01 drain/재부팅·두Workload Pod삭제/재시작을 사전 승인으로 묶는 관리 통제는 리뷰 제안이며 적용 완료로 표시하지 않는다. control01 집중에 따른 DNS/Calico 동시 중단 위험은 조건부 추정이고 시험 결과가 아니다.
- export/전달/반입한 바이트는 승인 digest 대조를 무결성 기준점으로 삼고 현재 cache의 과거 공급 출처 한계와 구분한다. 이 도구의 metadata/descriptor 일치만으로 layer본문 무결성을 선언하지 않는다. CoreDNS 실제Pod ref와 상위index/플랫폼child 해석은 반입 전후 확인안에 넣는다.
- P1 KNOWN ISSUE(Owner 이하영)+P0 예외 요청은 #30 Review 입력 권고이며 아직 처분 확정/위험수용이 아니다. Phase2(ROSA) 수신Ticket이 없는 상태에서 APPROVED DEFERRED로 기록하지 않는다. 원Due10/7과 제안 완료Due를 구분한다.
