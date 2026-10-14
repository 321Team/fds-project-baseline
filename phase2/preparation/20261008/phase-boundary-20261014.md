# Phase 1 보호와 Phase 2 준비 경계 — 2026-10-14

**현재 진입점:** [10:58 KST P0 13건·보류 3건 순차표](sequential-worklist-20261013.md#현재-작업-목록--1014-1058-kst-조회)와 [최신 PR75 HEAD/CI](evidence-handoff.md#1014-현재-인수표--기존-부분-완료와-미확인의-분리)를 따른다. 아래 `50f5f6e`의 122건 결과는 직전 검증 이력이다. PR75/167 병합 이후 PR80의 Git/Service/승인 입력 대조 후속과 문서 현행화를 진행했다. 이 작업의 실제 환경 미실행 경계는 유지한다.

이권욱 · CODEX_ASSISTED. 사용자 “phase 1 경계를 확실히 나눈 상태에서 권장 순서 대로 착수”에 따른 이번 작업 경계다. 팀 공용 정책·정본·AC를 바꾸지 않는다. Phase 1 Close 전의 기존 사전 준비 허용 범위를 공식 Phase 2 Start나 실제 환경 작업으로 확대하지 않는다.

## 작업 대상과 쓰기 범위

| 구분 | 이번에 하는 일 | 별도 실행·결정으로 남기는 일 |
|---|---|---|
| P1 코드·설정 | 기존 공급 결과/계약을 조회·참조 | tools/delivery·P1 workflow·Runner·DB/pg_hba·영구 방화벽/NM/route·Harbor CA/Robot·DNS/LB·공용 OCP 변경·시험·AC 인수 |
| P1 생산물 → P2 | TBS/Push/Deploy 원본의 source/RUN/수신 단계를 연결 | P1의 성공·token/claim·API/namespace UID·작업창을 P2 승인/identity로 복사 |
| P2 코드 | infra-cicd tools/phase2·docs/phase2의 오프라인 구현·시험, 병합된 PR75 이후 후속 Draft PR80 | 실제 API 요청·token 발급·IAM/RBAC 변경·운영 Runner 배치·Deploy·fence 해제 |
| P2 문서 | baseline phase2/preparation/20261008의 결정안·인수표·운영안, 병합된 PR167 이후 후속 문서 PR | 정본 발행·Issue AC/Status/담당/일정 변경·티켓 종결 |
| 자동 검증 | GitHub-hosted CI의 코드/문서 검사·합성 데이터·임시 로컬 파일 | self-hosted Runtime workflow_dispatch·실제 AWS/ROSA/DB/Harbor/공용 OCP 시험 |

기존 문서의 **P0/P1/P2는 우선순위**, **Phase 1/Phase 2는 프로젝트 단계**다. 예를 들어 “P1 조건부 Hybrid DNS”는 우선순위 설명이며 Phase 1 DNS 변경 허가가 아니다. 소비 namespace `fds-app`이라는 문자열도 P1/공용 OCP와 P2 ROSA가 같은 대상임을 뜻하지 않는다. `rosa-app`은 overlay다.

## 10/14 00:56 수행 이력 — 최신 결과는 위 현재 진입점 참조

| 순서 | 이번 진행 | 후속 담당·완료조건 |
|---|---|---|
| 1 #46 | PR75 `50f5f6ef8c35ccbad07fbaed47c021e60eb6db08`: 재시작 후 journal 읽기/체인·receipt 검사 CLI, 손상·partial·pending·live writer·FIFO 차단, 원본 보존 및 P1 공급 연결 | 실제 authorizer/target readback·fence 조정·배포 연결은 미완료. 하영 actual 플랫폼/권한, 재환 승인 이미지/clean render 입력 → 권욱 통합 구현·독립 리뷰 후 별도 Runtime |
| 2 #40/#48 | [권욱10/14 추가 Hybrid DNS 보류 결정](decision-packet.md#현재-d23-결정--추가-hybrid-dns-보류) 반영: D23=DEFERRED | Owner 권욱·기존10/16 점검 유지, #48 OPEN/구현 보류. 실제 API/Route값은 생산 인계 후 수용. DNS 전체 미사용·구현 취소가 아님 |
| 3 #42 | 기존 A/B·인증 갱신/전환/복귀 카드에 새 P1 Push 증적과 P2 credential 구분 연결 | 하영 P2 pull 인증·경로/재환 current·previous 입력 → 권욱 D22 선택. 기존 CA 자료 재요구 없음 |
| 4 #34/#39 | IAM v2·SSM 후속·N1 미실행·A3/태그 미확인을 인수표에 갱신 | 하영·재환의 actual 입력을 소비하여 권욱 Gate판정. 날짜 도래·PR병합만으로 G4 PASS 아님 |
| 5 #49/#54~57 | 공급 증적 편입과 운영 인수 구분, 누락 연결만 추적 | 생산자 기존 원본/리뷰를 #49 동일 candidate로 집계. Freeze/Review/삭제/Close 별도 |
| 6 #52 | 사용자 답변 “아직 미정—기존 제안 유지” 반영 | 10/23 14:00~15:30은 계속 제안. 사람의 참석/시간을 합성하지 않고 그 입력을 기다리는 동안 위 준비는 진행 |

PR75 Linux [p2-intake](https://github.com/321Team/infra-cicd/actions/runs/38424693689/job/115390890454)는122건 중111 PASS/11 SKIP, [source validate](https://github.com/321Team/infra-cicd/actions/runs/38424693676/job/115390890854)도 SUCCESS. 새 recovery 시험18건은 Linux17 PASS/Windows전용1 SKIP, 로컬 Windows9 PASS/POSIX9 SKIP이다. 실제 네트워크·TLS handshake·권한·ROSA 복구 인수가 아니다. 독립 REVIEW·MERGE·PUBLICATION 미완료.

## 현재 경계를 넘지 않고 닫을 수 없는 항목

**리뷰 절차:** [현행 정책](../../../governance/REVIEW_AUTHORITY_POLICY.md)에 따라 PR75 코드 변경은 독립 리뷰가 필요하고 PR167 문서 변경은 Lead 검토·병합 판단 대상이다. 문서 PR에 새 독립 승인 대기를 추가하지 않는다. 현재 PR75/167은 별도 검토 후 병합 완료다. 이번 후속 코드 PR80과 문서 변경은 Draft 검토본이며, 이번 요청에서 병합·정본 발행을 수행하지 않는다.

운영 배포의 권한/승인 검증과 실제 상태 대조는 신뢰된 actual 입력 없이 만들 수 없다. 기록 hash·형식검사·합성 Lease를 그 입력으로 대체하지 않는다. 준비 중 P1 설정 변경이 필요해 보이면 해당 접점의 원인·영향·최소 변경·복구 조건만 기록하고 현재 작업에서 실행하지 않는다.

비용은 교육장 리포트 기반 권욱 중앙 판단·지원확정/자부담0·400/450/500을 유지한다. 기존 ROSA Cost GO와 검증 종료까지 최소권한 유지 결정을 재사용하며, C2 Resolver/C3 ECR 추가비용·새 권한·분리 정책 재부착까지 승인하지 않는다. 10/13 종료한 자동 작업은 재개하지 않는다.
