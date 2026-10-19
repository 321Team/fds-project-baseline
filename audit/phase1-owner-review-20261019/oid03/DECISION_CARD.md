# OID03 자료 채택 경계 — 중앙 결정안
작성: 2026-10-19 KST. 판정: **자료 채택 문안 준비 완료 / 미채택·미게시 / OID03 전체 인수 미완료**.
추천: 지정 공유에 이미 보존된 정확 원본과 worker02 1종 사전검사를 현재 공급 참조자료로 채택한다. 새로운 검증을 반복하지 않고, 실제 설치·갱신·복구를 선택할 때만 필요한 입력의 차이를 연결한다.

## 원 기준과 결정 권한
정본 `979facb98de8ca1f1e2ce22f38b27ac3366f3fc3` Baseline 15.1 OID-03은 **사전 반입 또는 HTTPS Egress Destination·Owner·Expiry**, **미정의 Egress Permanent 허용 금지**, **이하영/이권욱 — 설치 실행 전**이다. 전체 신규 OS를 재설치해 성공해야 한다는 별도 OID03 시험 AC는 이 행에 없다.
같은 정본 Description의 원 AC18은 “Reboot 후 정책이 유지되고 재시험이 통과한다”, AC19는 “Rollback을 재현할 수 있다”이다. APP의 기존 20행 처분표를 재사용한다. RPM 보존·사전검사로 이 정책/경로 AC를 MET로 상향하거나, 반대로 전 노드 RPM 재설치를 새 필수조건으로 만들지 않는다.
기술 책임은 기존 이하영/이권욱, 보존 custodian은 이권욱이다. DOC의 기술 판독과 아래 제안은 실제 Lead 채택·위험수용·AC 변경이 아니다. 10/17 D01~D05 카드는 제안 이력으로만 사용하고 기존 Owner 확정으로 표시하지 않는다.

## 현재 충족·미충족·미확인
| 항목 | 현재 근거와 경계 |
|---|---|
| 공식 원본 보존 | 10/19 07:09:40 영수증: primary9 + worker02 직접 provider4 = RPM13개, 129,242,114B. 원본 복사20개(RPM13+공개키3+검증기록4)에 생성 README/CATALOG2개를 포함한 manifest22행·보존 영수증을 재사용. 이번 사본/RPM/키 재검사0 |
| 출처·정확 식별 | 보존 INTENT와 공표된 CATALOG 참조에 NEVRA·공식 URL·저장 상대경로·기록 SHA·목적이 연결됨. references/SOURCE_INDEX.json은 INTENT에서 추출한 읽기용 색인이며 공유 CATALOG를 새로 조회한 결과가 아님 |
| worker02 1종 사전검사 | 10/18 19:49:26~19:49:30, containerd.io-0:2.4.1-2.el10.x86_64. 실제 native parser·기존 key로 rpmkeys·설치 없는 `rpm -U --replacepkgs --test --noscripts --notriggers --noplugins` transaction 각 rc0. **이 결과 자체는 기존 중앙에서 한정 인수됨**; OID03 인수는 아님 |
| provider 가정 | 당시 설치된 bash/container-selinux/libseccomp/systemd exact4 원본 확보. 기존 의존 검사 및 transaction은 당시 worker02 설치 RPMDB를 소비. 새 OS 전이 의존물 closure와 모든 패키지/노드 transaction은 미입증 |
| 설치·복구 | 실제 reinstall·scriptlet/trigger/plugin 실행·서비스/데이터 복구 미수행. config/unit 내용 backup은 없음. hash·rpmdb main metadata 동일을 backup/전체 무결성으로 해석하지 않음 |
| 수령·보관 | 지정 공유 보존은 완료. 개별 사람 열람/수령·현재 ACL 감사·확정 단일 보존 종료일은 미확인. 기존 승인 인원 접근·프로젝트 종료까지 보존 조건 유지 |
| 공급 계약 채택 | 원본 참조·경로·provider 가정·갱신/실패/복구 경계의 아래 한정 문안은 채택 가능 후보. 기존 게시물도 “최종 채택/인수 별도”이므로 이번 DOC가 이를 승인했다고 기록하지 않음 |

## 추가 검증 없이 채택할 구체 문안
**출처/원본:** references/SOURCE_INDEX.json의 기록 식별값과 기존 공유 `CATALOG.json`을 공급 참조로 사용한다. Kubernetes v1.36 RPM 4종, Docker CentOS10 containerd 2종, CentOS Stream10 BaseOS primary3종·worker02 provider4종이다. 기록 SHA는 보존 당시 확인값이며 설치 당시 최초 provenance의 소급 증명은 아니다. 공개키 보관은 새 신뢰키 import 승인이 아니다.

**실제 보관 참조:** `\\10.1.93.150\HybridCloud과정공유디렉토리\07_프로젝트\제01조\01차 프로젝트\02 프로젝트 결과물\Phase1-OID03-offline-originals-20261019`.
내부 `rpm/pkg01.rpm~pkg09.rpm`, `rpm/provider01.rpm~provider04.rpm`, `keys/`, `records/`와 `README.md / CATALOG.json / RECEIPT.json / SHA256SUMS.txt`를 구분한다. 보존 manifest 기록 SHA는 `0107c96fa7a590c85c6abc0982786b7361d91c2d47aeb7ef8ce66bc886a74376`이다. 과거 서버 반입은 기존 svc_ansible 관리 전달 경로와 worker02 root 보호 경로를 사용했다. 경로의 현재 가용성·접근권한까지 새로 확인한 것은 아니다.

**대상/provider:** 현재 자료가 직접 뒷받침하는 최소 범위는 worker02의 같은 NEVRA containerd1종 및 당시 설치 provider4종이다. provider4종은 보관 원본이며 동시 재설치 대상으로 채택하지 않는다. containerd2.3.5 대상4대와 2.4.1 대상2대의 기존 구분을 보존한다. crictl archive/member 연결 및 OID02 공급208은 기존 범위로 재사용하고 이번 13RPM 묶음에 포함됐다고 하지 않는다.

**갱신:** 현 원본은 고정 참조로 보존한다. 실제 목적·노드·NEVRA/build/arch·의존 provider·설정/unit 또는 신뢰키가 달라지는 경우 그 차이에 필요한 공급물·검증·복구점만 별도 연결한다. latest 대체·버전 통일·영구 egress·키 자동 import를 허용하지 않는다. 실제 작업 목적이 없으면 운영 실행을 보류하고 계약 잔여를 유지한다.

**실패/중단:** 선택 회차에서 식별/해시/서명/parser/의존/파일 충돌 또는 시간 상한 불일치가 있으면 그 회차만 HOLD한다. 자동 retry·다음 노드 확대·검증/보안 통제 해제를 하지 않는다. 이번 기존 PASS 재실행을 완료조건으로 추가하지 않는다.

**복구:** 자료 보관만으로 실제 복구를 승인하지 않는다. 실제 변경이 필요한 회차에는 정확 같은 원본과 변경 직전 config/unit bytes·권한/SELinux가 보존된 보호 backup, 대상 Pod/PV·정책 영향, 콘솔·유한 중단/복귀 예산과 한정 절차가 먼저 필요하다. 실패 시 변경 대상만 검토된 backup/원본으로 복귀하며 package erase/kubeadm reset/살아 있는 runtime 덮어쓰기/전체 snapshot rollback으로 대체하지 않는다. 복귀 판정은 해당 NEVRA·config/unit·권한/SELinux·containerd/CRI·대상 Node/Pod/경로 회귀와 임시물 처분 receipt에 한정한다.

**보존 처분:** 기존 공유 보존 조건·custodian을 유지한다. 서버 사전검사 전달물의 “10/19 08:00 또는 결과 인수 중 먼저 검토”는 검토 트리거였고 자동삭제/영구보존 결정이 아니다. 공유 보존 완료가 서버 전달물 회수 완료를 뜻하지 않는다. 실제 회수·잔류 여부는 미확인으로 남긴다. 새 날짜나 무기한 위험수용을 부여하지 않는다.

## 원 AC와 잔여를 그대로 남기는 기록
1. OID03: 이 자료와 현재 공급 참조의 **한정 채택 결정 자체는 중앙 미실행**. 신규 OS 전이 의존물·선택하지 않은 갱신/실제 복구 계약 및 전체 OID03 인수는 미완료다. 현재 원본13종 부재·공유 미보존으로 되돌려 쓰지 않는다.
2. AC18/19: 기존 APP 행별 유효 결과/한정 처분/N/A를 재사용하되 최종 원 AC 판정은 별도다. 이 카드 작성은 후속 APP postboot 결과를 새로 검토하거나 #14 최신 전체 AC 표를 재작성하는 작업이 아니다.
3. 실제 reinstall/데이터 복구 미수행은 입증 범위의 한계다. 이 사실을 숨기거나 새 전 노드 재설치 의무로 바꾸지 않는다.
4. 후속 순서: 중앙이 이 문안의 한정 자료 채택 여부를 결정 → 채택한 정확 문안만 기존 책임 티켓에 기록 → 원 AC 미충족·미확인 행의 기존 처리로 연결. 이번 산출물은 첫 결정에 필요한 완성안까지이며 게시·채택·종결0이다.

## 추적 근거
- [정본 Baseline](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/baseline/FDS_Project_Implementation_Baseline_v3.1.21.md), [발행 Description](https://github.com/321Team/fds-project-baseline/blob/979facb98de8ca1f1e2ce22f38b27ac3366f3fc3/tickets/v3.1.21/descriptions/ICR-D-NET-01-01.md).
- [기존 사전검사](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6248973398), [공유 보존](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6255792476), [공급 경계 최종 채택 잔여](https://github.com/321Team/fds-project-baseline/issues/14#issuecomment-6251416965).
- 정확 입력 파일·hash·조회 시점은 PRIMARY_BINDING.json. 실제 argv는 references/NATIVE_SCOPE.json. 검증은 문서 결속과 경계 정합성만 수행했다.

