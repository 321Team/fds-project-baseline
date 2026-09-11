# 다음 작업과 도입 상태

이 문서는 작업 순서와 조회 시점 기록이다. 현재 상태는 GitHub에서 재조회한다.

1. 공통 지침/검증기 Draft PR을 독립 검토하고 정확한 HEAD로 수동 병합한다.
2. 각 infra/evidence 저장소의 AGENTS 진입 지침은 공통 지침 병합 후 검토·병합한다.
   central main이 공통 파일을 제공하지 않으면 downstream에서 추측하여 진행하지 않는다.
3. CLOUD_SETUP의 Cloud 저장소 연결·정상 인증·지침 로딩을 실제 환경에서 확인한다.
   준비 문서/스크립트 생성과 Cloud 환경 설정 완료를 분리한다.
4. Work에서 다음 한 작업의 Task와 공통 receipt를 만들고 Codex에 인계한다.
5. 대표 3건의 실제 작업 시간·재작업을 측정하여 적용 범위를 결정한다.

## 2026-09-11 조회에서 확인한 의존 작업

| 대상 | 조회 당시 상태 | 다음 작업의 제한 |
|---|---|---|
| baseline docs-v3.1.18 | 발행, Tag 72599ae49342b0fb8dbd3d8ee60314afb9f907bb | 새 live 검사 필요 |
| baseline PR #68 | OPEN, release/v3.1.18-wbs-calendar 대상 | main 반영 내용과 PR 병합/속성 동기화 구분 |
| infra-kubernetes PR #2, #4 | OPEN | main 사양/코드인 것으로 가정 금지 |
| infra-cicd PR #2, #3 | OPEN | 모의 결과와 배포 가능 판정 구분 |
| fds-project-evidence PR #7 | OPEN | 제안한 매핑과 승인된 수신 Commit 구분 |
| P1-K8S/P1-HBR/P1-SEC/P1-CICD | 현장 Gate 잔여 | Codex 도입으로 자동 완료하지 않음 |

이 목록은 실시간 대시보드가 아니다. Ticket 64건의 source property는 기존
TICKET_SYNC_POLICY와 approved delta 절차에서만 동기화한다.
