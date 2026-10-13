# Phase 2 권욱 담당 선행 작업 — 순차 진행표

**10/14 01:35 결정 접수:** 권욱의 “보류”에 따라 [D23 추가 Hybrid DNS=DEFERRED](decision-packet.md#현재-d23-결정--추가-hybrid-dns-보류). 아래의 D23 PENDING은 앞선 검토 시점 이력이다. #48 OPEN·기존10/16 점검 유지, D22는 계속 PENDING. Phase 1 변경·실제 DNS 구현 없음.

## 10/14 별도 착수 — 현재 결과

[Phase 1 보호 경계와 순차 착수표](phase-boundary-20261014.md)를 현재 진입점으로 사용한다. 아래10/13 표는 당시 결과이며 같은 준비를 다시 만드는 작업 목록이 아니다.

1. #46: PR75 `50f5f6ef8c35ccbad07fbaed47c021e60eb6db08`에 오프라인 journal 재구성/검증 CLI·실패 모의시험·새 P1공급 연결을 추가했다. CI2SUCCESS, Linux122중111PASS/11SKIP. actual권한/대상 검증·운영배포·수동fence조정은 잔여이므로 현재 경계에서 더 진행하지 않고 다음 준비로 전환했다.
2. #40/#48: 기존 단일 DNS 권고안에 Phase1설정 보호·실제입력·Deferred/Cancelled 구분을 추가했다. 최종D23은 PENDING이다.
3. #42: 기존 A/B에 새 Push증적·P1 Push권한과 P2 pull권한 분리·만료/갱신 실패 중단·복구 수용조건을 연결했다. D22선택/실제전환은 PENDING이다.
4. #34/#39/#49: 최신 SSM부분완료·N1미실행·A3/태그actual미확인·새공급증적을 [현재 인수표](evidence-handoff.md)에 연결했다. 같은 원본 재제출·시험 반복을 요구하지 않는다.
5. #52/#54~57: 권욱의 “아직 미정—기존 제안 유지”를 [Review운영안](lifecycle-review-preparation.md)에 반영했다. 일정/참석확정·초대·실행·종결 없음.

새 실제 AWS/DB/Runner/OCP접속·권한/정책·Apply/Deploy/VPN B·자원변경 없이 준비 코드/문서만 진행했다. PR병합·독립승인·정본발행은 수행하지 않는다.

CODEX_ASSISTED. 2026-10-13 KST 작성. 기준 checkout `c5c854efe3572f65bb2ef7b23dd32b61b7291e8e`, 외부 PR 상태 17:48 KST, #52/#48 본문 재조회 18:01 KST. 이 문서는 정본·AC·담당자·일정을 변경하지 않는다. 최신 실행 여부는 각 원본을 재조회한다.

18:45 갱신: PR75 현재 HEAD와 PR214 충돌 해소·PR76/77/29 병합은 [증적 인계표의 추가 대조](evidence-handoff.md)에 연결했다. 최초 시점의 OPEN/이전 HEAD 표기를 현재 미처리 작업으로 다시 세지 않는다.

**진행 원칙:** 한 행이 외부 입력/리뷰에 막히면 현재 결과·남은 담당/완료조건을 남기고 다음 독립 행을 진행한다. 검증을 끝낸 동일 코드/증적은 새로운 변경이나 실패 근거가 있을 때만 재검증한다. 아래 “준비 완료”는 티켓 완료가 아니다.

| 순서·권욱 담당 티켓 | 이번 준비 결과 / 연결 | 다음 행동·담당자 | 실제 완료조건 |
|---|---|---|---|
| 1. #46 Delivery | [infra-cicd Draft PR75](https://github.com/321Team/infra-cicd/pull/75): 코어·TLS sender·영속 claim/checkpoint·생산자 bridge·연결 실패/복구 MOCK. HEAD `39fd173b4fd22e1ca2b4e430cc984ace01947bd1`, CI2 SUCCESS, 독립 리뷰0·미병합 | 코드 독립 검토 대기와 별개로 2번 진행. 플랫폼 실제 입력 이하영, 승인 Registry/digest·clean render 인계 이재환, 소비·검증 이권욱 | source/환경 identity·권한·승인 결속, 운영 수명주기·중단 후 수동 조정, 해당 SHA 리뷰와 별도 Runtime 조건. MOCK을 TLS handshake/배포 성공으로 사용하지 않음 |
| 2. #40/#48 D23 | [결정 문안·5개 소비 경로·Deferred 조건](decision-packet.md)의 10/13 보완 작성 | 이권욱이 기존 10/16 목표의 단일 선택 준비. 실제 API/Route는 #38/#43 입력 후 소비. 입력 대기 중 3번 진행 | D23 이유·범위·Owner/재검토 조건; Go이면 기존 Query/거부/복구 AC, IP 최종 선택이면 #48 Cancelled 근거. 이번 상태 변경 없음 |
| 3. #42 D22 | [기존 A/B·12출력에 인증/전환/복귀 카드 추가](d22-lead-review.md). CA 준비 입력 완료 재사용 | 이하영: 지원 pull 인증/경로; 이재환: Registry/image 원본; 이권욱: 소비 계약/비용/최종 선택. 실제값 대기 중 4번 진행 | 경로·인증·current/previous digest 및 생성 후 cold-pull→Basic Ready→D22 Final. ECR 생성/복사·Phase1 Robot 변경 별도 |
| 4. #34/#39 Architecture/G4 | [7개 Gate 입력에 최신 PR·수신 범위·잔여 연결](evidence-handoff.md) | #35 이하영·#37 이재환의 actual 원본/Lead 수용을 이권욱이 소비. 한 행 미결이어도 다른 행 검토 | 기존 G4 exact 입력·비용·Critical 잔여에 대한 실제 Lead 판정. PR29 승인·PR214 편입 승인만으로 PASS 아님 |
| 5. #49/#54 산출물/Freeze | [rolling 집계 4묶음과 결함 처리](evidence-handoff.md) | 생산자가 기존 원본에 누적, 이권욱은 변경분만 연결. 10/23 동일 candidate로 Freeze 검토 | P0 증적·승인된 As-built 차이·재현 가능한 IaC/runbook·Critical 문서 결함0. 정본 발행은 별도 |
| 6. #52/#55/#56/#57 Review/Close | [90분 시간안·역할·진행표·Action/정리 선후관계](lifecycle-review-preparation.md) | 이권욱이 단일 시각/필수 참석자·승인권자·Demo 방식을 조율; 현재 미확정 | #52 실제 확정/동기화, 10/23 #49→#54→#56→#55, 10/26 잔여/비용/sign-off→#57. 회의/종결 미실행 |

## 다른 담당 티켓을 기다리며 중복 작업하지 않을 항목

현재 1~6번은 전체를 직렬로 대기할 필요가 없다. 다음 준비 묶음은 병행하되 실제 Runtime은 각 승인된 대상·작업창·복구 조건을 먼저 확인한다.

| 병행 준비 묶음 | 지금 가능한 작업 | 실행/최종 판정 전에 기다릴 입력 |
|---|---|---|
| A. #35/#39 증적 연결 | PR214 충돌 해소 변경분 재검증과 G4 행 갱신 | 실제 편입 기록, 남은 IAM/VPN 원본·Lead 수용. 증적 편입만으로 G4 PASS 금지 |
| B. #46 Delivery | PR75 코드 독립 리뷰 준비와 운영 연결 설계 | 이하영 actual API/namespace UID/CA/host·권한 receipt, 이재환 current/previous digest·clean render, 정확한 실행창 |
| C. #40/#42 결정 | D23 선택 문안, D22 인증 갱신·전환·복귀 계약의 누락 필드 정리 | 각 결정에 필요한 실제 입력·Lead 판단. 미확정 값을 임의 확정하지 않음 |
| D. #49/#52/#55 문서·Review | 원본 연결 갱신, 시간/참석자·Demo 방식 조율안, Action 완료조건 | 실제 참석·시각 확정 및 G4/G5/G6 결과. 기존 문서 준비를 재작성하지 않음 |

위 병행 구분은 책임 티켓의 담당자를 바꾸지 않는다. 문서 전용 PR은 Lead 검토, 코드/증적 PR은 독립 리뷰라는 현행 정책을 적용하며 리뷰 요청과 실제 승인을 구분한다.

### 기존 결정·인수 대기를 유지하는 항목

| 티켓 | 지금의 권욱 선행 준비 범위 | 다시 작업하는 계기 |
|---|---|---|
| #33 Phase 2 Start | Phase1 Close·Known Issue/Approved Deferred 등 기존 진입조건 연결. 사전 문서 준비를 공식 Start로 표시하지 않음 | 기존 진입조건의 새 증적/결정 수신 |
| #36 D21 | OCI Primary NO-GO/AWS Relay 선택·PR161 원본 편입을 재사용 | 기존 기록의 실제 결함 또는 새 정식 변경결정. 새 OCI 시험 불필요 |
| #53 G6 | #47 exact handoff → #50 실제 E2E/회귀 결과 소비 순서와 인수표 재사용 | 실제 실행 SHA/RUN·결과 수신. Lab/합성 결과로 ROSA 인수 대체 금지 |
| #120 GitOps | G5 이후 여력 조건의 선택 항목으로 유지 | 해당 Lead의 Go/No-Go/Deferred 결정·실제 여력 확인. 지금 설치/권한 확대 없음 |

## 이번 변경의 단계와 복구

- STATIC: 기존 문서·Issue AC·PR 상태에 대한 자체 대조. 결과는 이 변경 PR의 검증란에 남긴다.
- MOCK/RUNTIME: 이번 문서 변경에서는 미실행. PR75의 기존 MOCK/CI는 그 source SHA와 한계 안에서만 인용한다.
- REVIEW/MERGE/PUBLICATION: 이 문서의 자체 검토, 실제 PR 리뷰, 병합, 정본 발행을 각각 기록한다. 작성자를 타인 독립 승인자로 표시하지 않는다.
- 실제 AWS/ROSA/DB/Runner/OCP 접속, token/IAM 변경, Apply/Deploy/VPN 단계 B, 자원 생성/삭제, 정본 발행·티켓 종결은 수행하지 않는다.
- Phase1 DB/pg_hba/영구 방화벽/NetworkManager/route/Harbor CA/Runner/DNS/LB/AC를 보존한다. 문서 복구는 해당 변경 커밋 revert이며 실행 환경 원복과 구분한다.
- 교육장 지원·자부담0·목표400/중단450/상한USD500, 중앙 비용 판단·검증 완료까지의 최소권한 유지 결정을 재사용한다. 현재 보고가 없으면 비용값/승인값을 합성하지 않는다.
