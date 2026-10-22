# Phase 2 P1 미도입·미구현 잔여 대장

이 대장의 각 항목은 원 티켓의 기술 미완료와 향후 재개 책임을 보존한다. Close/Decision Done을 Runtime 성공이나 전체 프로젝트 완료율로 환산하지 않는다. 원 Risk/Known Issue/수용 이력의 ID는 변경하지 않으며 새 Risk 번호를 임의 발급하지 않는다.

## [P1-MON-02 / #25](https://github.com/321Team/fds-project-baseline/issues/25)

- 책임: **이재환**. 판단: 고도화 미구현 잔여로 제외 검토. 현재 승인: `LEAD_CONFIRMATION_PENDING`.
- 잔여·영향: Prometheus/Alertmanager HA·PDB/분산·장기보존·Dashboard/Alert 개선 및 장애/복구 시험 미완료. 기존 P0 관측·Observe→Metrics 대체 경로를 제거하지 않음.
- 확인/재개 조건: 현재 관측에 P0 필수 공백이 없는지, 기존 인계 이후 구현/자원 변화가 있는지 재환 확인.
- 일정: 이번 프로젝트 구현일/향후 재검토일 미배정. 무응답·P0 완료·잔여 자원 존재만으로 자동 재개하지 않음.
- 기술 상태: 기존 원본/인계의 범위만 재사용. 실제 새 설치·시험·복원·재생성·정리 성공을 선언하지 않음.
- 기존 근거: [기록](https://github.com/321Team/fds-project-baseline/issues/25#issuecomment-6256808772), [기록](https://github.com/321Team/fds-project-baseline/issues/25#issuecomment-6264971142)

## [P1-DR-02 / #26](https://github.com/321Team/fds-project-baseline/issues/26)

- 책임: **이하영**. 판단: 격리 Backup/Restore 미수행 잔여로 제외 검토. 현재 승인: `LEAD_CONFIRMATION_PENDING`.
- 잔여·영향: Harbor와 on-prem kubeadm etcd의 검증된 복원 보장 없음. 기존 다른 DB/DR 백업 성공을 본 AC로 대체하지 않으며 ROSA 관리형 etcd와 구분.
- 확인/재개 조건: 이전 수신 기록을 재사용. 이후 백업/격리 복원 시도·잔존 자원·P0 보호 영향만 하영 확인.
- 일정: 이번 프로젝트 구현일/향후 재검토일 미배정. 무응답·P0 완료·잔여 자원 존재만으로 자동 재개하지 않음.
- 기술 상태: 기존 원본/인계의 범위만 재사용. 실제 새 설치·시험·복원·재생성·정리 성공을 선언하지 않음.
- 기존 근거: [기록](https://github.com/321Team/fds-project-baseline/issues/26#issuecomment-6250018800), [기록](https://github.com/321Team/fds-project-baseline/issues/26#issuecomment-6264972567)

## [P1-HA-02 / #27](https://github.com/321Team/fds-project-baseline/issues/27)

- 책임: **이하영**. 판단: 추가 HA/장애 검증 미수행 잔여로 제외 검토. 현재 승인: `LEAD_CONFIRMATION_PENDING`.
- 잔여·영향: Rolling Update·PDB/TopologySpread·복구 E2E의 고유 미충족 AC 유지. 과거 CP 관측을 전체 HA 성공으로 승격하지 않음.
- 확인/재개 조건: 후속 시도/잔존 자원과 P0 기본 복구/가용성 영향만 하영 확인. 공용 OCP나 HCP 직접 장애 시험은 새로 하지 않음.
- 일정: 이번 프로젝트 구현일/향후 재검토일 미배정. 무응답·P0 완료·잔여 자원 존재만으로 자동 재개하지 않음.
- 기술 상태: 기존 원본/인계의 범위만 재사용. 실제 새 설치·시험·복원·재생성·정리 성공을 선언하지 않음.
- 기존 근거: [기록](https://github.com/321Team/fds-project-baseline/issues/27#issuecomment-6250019054), [기록](https://github.com/321Team/fds-project-baseline/issues/27#issuecomment-6264974122)

## [DEC-P2-DNS-01 / #40](https://github.com/321Team/fds-project-baseline/issues/40)

- 책임: **이권욱**. 판단: 이번 프로젝트 추가 Hybrid DNS 미도입 결정 확정. 현재 승인: `USER_CONFIRMED`.
- 잔여·영향: 기존 DB/Harbor IP·ROSA public API/Route DNS·엄격 TLS 경로 유지. Resolver/조건부 전달/새 Zone·53번 포트 정책은 도입하지 않음. 자동 endpoint 갱신·추가 양방향 DNS 시험 미구현 잔여.
- 확인/재개 조건: 이권욱 이번 직접 지시로 결정 확정. 미래 도입은 실제 필요·query path/권위·최소 권한·실패/복구 범위와 별도 재개 판단.
- 일정: 이번 프로젝트 구현일/향후 재검토일 미배정. 무응답·P0 완료·잔여 자원 존재만으로 자동 재개하지 않음.
- 기술 상태: 기존 원본/인계의 범위만 재사용. 실제 새 설치·시험·복원·재생성·정리 성공을 선언하지 않음.
- 기존 근거: [기록](https://github.com/321Team/fds-project-baseline/issues/40#issuecomment-6073998820), [기록](https://github.com/321Team/fds-project-baseline/issues/40#issuecomment-6150473837)

## [DEC-P2-OP-01 / #41](https://github.com/321Team/fds-project-baseline/issues/41)

- 책임: **이하영**. 판단: 추가 Operator Mirror 미도입/유예 결정 후보. 현재 승인: `LEAD_CONFIRMATION_PENDING`.
- 잔여·영향: 기존 승인 Catalog/Operator 소비 경로와 P0 보안은 유지. 새 oc-mirror/Harbor/Custom CatalogSource 공급망 보장은 하지 않음.
- 확인/재개 조건: 하영이 현재 공급 경로와 P0 필수 Package 영향을 확인하고 Direct 선택 또는 P1 범위 유예 중 실제 판정을 회신. 미회신을 Direct 확정으로 간주하지 않음.
- 일정: 이번 프로젝트 구현일/향후 재검토일 미배정. 무응답·P0 완료·잔여 자원 존재만으로 자동 재개하지 않음.
- 기술 상태: 기존 원본/인계의 범위만 재사용. 실제 새 설치·시험·복원·재생성·정리 성공을 선언하지 않음.
- 기존 근거: [기록](https://github.com/321Team/fds-project-baseline/issues/41#issuecomment-6099807120), [기록](https://github.com/321Team/fds-project-baseline/issues/41#issuecomment-6182867037)

## [P2-OADP-01 / #44](https://github.com/321Team/fds-project-baseline/issues/44)

- 책임: **이하영**. 판단: OADP/S3 도입 미수행 잔여로 제외 검토. 현재 승인: `LEAD_CONFIRMATION_PENDING`.
- 잔여·영향: OADP 기반 앱 Backup/Restore·S3 연계의 실제 복구 보장 없음. 클러스터 재생성·앱/DB 기존 필수 보호 AC는 그대로.
- 확인/재개 조건: 하영이 미착수 이후 Subscription/Backup/S3/IAM 관련 생성 유무와 잔존/정리 책임을 delta로 확인. 없음으로 합성하지 않음.
- 일정: 이번 프로젝트 구현일/향후 재검토일 미배정. 무응답·P0 완료·잔여 자원 존재만으로 자동 재개하지 않음.
- 기술 상태: 기존 원본/인계의 범위만 재사용. 실제 새 설치·시험·복원·재생성·정리 성공을 선언하지 않음.
- 기존 근거: [기록](https://github.com/321Team/fds-project-baseline/issues/44#issuecomment-5907064831), [기록](https://github.com/321Team/fds-project-baseline/issues/44#issuecomment-6182867720)

## [P2-DNS-01 / #48](https://github.com/321Team/fds-project-baseline/issues/48)

- 책임: **이권욱**. 판단: 이번 프로젝트 추가 Hybrid DNS 구현 범위 제외 확정. 현재 승인: `USER_CONFIRMED`.
- 잔여·영향: DNS 구현·양방향 Query/거부·장애 fallback Runtime은 미실행/인수 미충족으로 보존. #40의 기존 endpoint 유지 결정으로 조건부 구현을 수행하지 않음.
- 확인/재개 조건: 이권욱 이번 직접 지시로 제외 확정. Cancelled는 이번 구현 범위의 not_planned 종결이며 검토 자료·기술 도입 가능성 자체를 폐기한 뜻이 아님.
- 일정: 이번 프로젝트 구현일/향후 재검토일 미배정. 무응답·P0 완료·잔여 자원 존재만으로 자동 재개하지 않음.
- 기술 상태: 기존 원본/인계의 범위만 재사용. 실제 새 설치·시험·복원·재생성·정리 성공을 선언하지 않음.
- 기존 근거: [기록](https://github.com/321Team/fds-project-baseline/issues/48#issuecomment-5976876088), [기록](https://github.com/321Team/fds-project-baseline/issues/48#issuecomment-6150475259)

## [P2-OP-01 / #51](https://github.com/321Team/fds-project-baseline/issues/51)

- 책임: **이하영**. 판단: 조건부 Operator Mirror 구현 미수행 잔여로 제외 검토. 현재 승인: `LEAD_CONFIRMATION_PENDING`.
- 잔여·영향: ImageSet·Harbor mirror·Custom CatalogSource Ready/Package 조회·재생성 재현이 미검증. #41 실제 결정 전 Direct/N/A를 자동 확정하지 않음.
- 확인/재개 조건: 하영이 #41과 결합 판정하고 실제 mirror/cred/저장소·CatalogSource 잔존 여부 확인. 있으면 소유/정리 절차를 먼저 연결.
- 일정: 이번 프로젝트 구현일/향후 재검토일 미배정. 무응답·P0 완료·잔여 자원 존재만으로 자동 재개하지 않음.
- 기술 상태: 기존 원본/인계의 범위만 재사용. 실제 새 설치·시험·복원·재생성·정리 성공을 선언하지 않음.
- 기존 근거: [기록](https://github.com/321Team/fds-project-baseline/issues/51#issuecomment-5907195667), [기록](https://github.com/321Team/fds-project-baseline/issues/51#issuecomment-6182867389)

## [DEC-P2-RHOAI-01 / #95](https://github.com/321Team/fds-project-baseline/issues/95)

- 책임: **이하영**. 판단: 이번 프로젝트 RHOAI 미도입/유예 결정 후보. 현재 승인: `LEAD_CONFIRMATION_PENDING`.
- 잔여·영향: 과거 Lab precheck는 보존하되 ROSA AI Runtime/자원·지원·Entitlement·복구 인수 성공으로 확대하지 않음. AI Inference의 기존 Scope Out 유지.
- 확인/재개 조건: 하영이 이후 별도 설치/자원 변화와 P0 영향 확인 후 Decision 종결 판정. 10/27 이후 PoC는 별도 프로젝트/승인 범위.
- 일정: 이번 프로젝트 구현일/향후 재검토일 미배정. 무응답·P0 완료·잔여 자원 존재만으로 자동 재개하지 않음.
- 기술 상태: 기존 원본/인계의 범위만 재사용. 실제 새 설치·시험·복원·재생성·정리 성공을 선언하지 않음.
- 기존 근거: [기록](https://github.com/321Team/fds-project-baseline/issues/95#issuecomment-5907067523), [기록](https://github.com/321Team/fds-project-baseline/issues/95#issuecomment-6032524902)

## [DEC-P2-GITOPS-01 / #120](https://github.com/321Team/fds-project-baseline/issues/120)

- 책임: **이권욱**. 판단: 이번 프로젝트 추가 GitOps/Argo CD 미도입 결정 확정. 현재 승인: `USER_CONFIRMED`.
- 잔여·영향: 기존 #46 Runner direct ROSA Delivery Contract·Build/Test/Scan/Push 생산자/Runtime 소비자 경계 유지. Argo CD sync/drift/rollback/recreate 미구현 잔여.
- 확인/재개 조건: 이권욱 이번 직접 지시로 결정 확정. GitOps 재개는 기존 #46 변경 CR·namespace/RBAC·source/digest/sync/imageID 증적·복구·정리 범위를 별도 판단.
- 일정: 이번 프로젝트 구현일/향후 재검토일 미배정. 무응답·P0 완료·잔여 자원 존재만으로 자동 재개하지 않음.
- 기술 상태: 기존 원본/인계의 범위만 재사용. 실제 새 설치·시험·복원·재생성·정리 성공을 선언하지 않음.
- 기존 근거: [기록](https://github.com/321Team/fds-project-baseline/issues/120#issuecomment-5912507218), [기록](https://github.com/321Team/fds-project-baseline/issues/120#issuecomment-6150476545)

## [DEC-P2-COMP-01 / #121](https://github.com/321Team/fds-project-baseline/issues/121)

- 책임: **이하영**. 판단: 이번 프로젝트 Compliance Operator 미도입/유예 결정 후보. 현재 승인: `LEAD_CONFIRMATION_PENDING`.
- 잔여·영향: Operator Scan·Compliant/NonCompliant 처리·재실행/재생성 검증은 미수행 잔여. 기존 P0 Security/SCC/NP/TLS 검증과 발견 결함 처리는 계속 필수. 규제 준수 인증을 주장하지 않음.
- 확인/재개 조건: 하영이 이후 설치/scan/잔존 자원과 P0 필수 보안 영향 확인 후 Decision 종결 판정.
- 일정: 이번 프로젝트 구현일/향후 재검토일 미배정. 무응답·P0 완료·잔여 자원 존재만으로 자동 재개하지 않음.
- 기술 상태: 기존 원본/인계의 범위만 재사용. 실제 새 설치·시험·복원·재생성·정리 성공을 선언하지 않음.
- 기존 근거: [기록](https://github.com/321Team/fds-project-baseline/issues/121#issuecomment-5912511435), [기록](https://github.com/321Team/fds-project-baseline/issues/121#issuecomment-6182868066)
