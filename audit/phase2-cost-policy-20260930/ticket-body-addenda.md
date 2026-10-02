# Issue Body Addenda Candidate — DEC-P2-COST-01

> 기준: 2026-09-30 KST 사용자 승인
> 상태: **CANDIDATE / HUMAN APPLY REQUIRED**
> TICKET_SYNC_POLICY §5.1에 따라 AI가 기존 Issue 본문 절/문단을 직접 추가하지 않는다.
> 관련 티켓에는 별도 운영 코멘트를 남기며, 아래 블록은 차기 수동 본문 반영/정본 재생성용 후보이다.

## 공통 정책 문구

> Phase 2 Cloud Cost 정책은 `Target ≤ $400 / Operational Hard Stop $450 / Protected Reserve $50 / Total Ceiling $500`으로 적용한다. AWS/ROSA 기준 리전은 **Asia Pacific (Seoul) / `ap-northeast-2`**로 고정한다. $400 도달 또는 초과 예상 시 신규 P1/선택 실험은 Deferred 우선, $450은 신규 유료 소비 Hard Stop이다. $450~$500은 billing lag·teardown delay·cleanup residual 전용 Reserve이며 신규 기능 예산으로 사용하지 않는다. 판정은 단순 현재 Billing 수치가 아니라 Actual/Gross + 확인 가능한 미반영/Projected cost를 포함한다. Region 확정은 HCP/Classic topology 또는 provisioning 승인으로 확대하지 않는다.

## #34 P2-ARC-01

- Architecture Freeze 입력에 Cost/Lifecycle control을 추가한다.
- ROSA/AWS 자원 생성·유지·삭제 창이 $400/$450/$500 threshold와 충돌하지 않도록 설계한다.
- 비용 정책은 D21~D26 및 P0/P1 우선순위를 변경하지 않는다.
- AWS/ROSA Region/AZ 설계 입력은 `ap-northeast-2`를 기준으로 동결하고, HCP/Classic은 Cost GO까지 미확정으로 유지한다.

## #35 P2-IAC-01

- Terraform Plan/Apply 전 비용 발생 리소스와 예상 유지시간을 기록한다.
- Create → Verify → Destroy 재현성을 유지하고 Destroy 결과와 실제 리소스 소멸을 구분한다.
- $450 Hard Stop 발동 시 신규 create/recreate/scale-out을 중단하고 cleanup을 우선한다.
- Terraform AWS provider/ROSA 입력은 `ap-northeast-2`를 기준으로 준비하되 topology·instance type/count는 Cost GO 전 임의 확정하지 않는다.

## #37 P2-VPN-01

- AWS Site-to-Site VPN 측 Region 입력은 `ap-northeast-2`를 기준으로 한다.
- OCI 측 기존 결정/리전과 터널 Runtime 상태는 별도 선행조건·증적으로 유지하며, 이번 Region 결정만으로 VPN Runtime PASS를 상향하지 않는다.
- VPN 시간당/데이터 전송 등 프로젝트 귀속 비용은 Cost-to-Complete 입력에 포함한다.

## #38 P2-ROSA-01

- ROSA Cluster lifecycle을 비용 정책에 연결한다.
- 장기 24x7 유지가 기본값이 아니며 P0 Runtime 검증 창에 맞춰 최소 유지한다.
- $400 이후 P1 실험은 Deferred 우선, $450에서는 신규 비용 증가를 중단한다.
- ROSA 생성 Region은 `ap-northeast-2`로 고정한다. HCP/Classic은 동일 workload/Runtime Cost-to-Complete 비교와 quota/prerequisite 확인 후 별도 Cost GO에서 확정한다.

## #42 DEC-P2-REG-01

- Registry 선택 시 ROSA/AWS 프로젝트 귀속 Registry/Storage/Transfer 등 유료 비용을 동일 $500 Ceiling에 포함한다.
- 무료/credit 여부만으로 별도 예산으로 분리하지 않는다.
- Cloud Registry를 선택하는 경우 AWS 측 Region 비용/전송 입력은 `ap-northeast-2` 기준으로 산정한다.

## #49 P2-DOC-01

- 최종 산출물에 Budget policy, Actual/Control Cost, 유료 resource inventory, cleanup 결과와 Deferred 항목을 남긴다.
- Reserve 사용이 있었다면 금액·원인·불가피성을 구분한다.

## #55 P2-REV-01

- Phase 2 Review에서 비용 threshold 준수, running resource, teardown 상태, 잔여 projected charge를 검토한다.
- $500 초과 예상 잔여가 있으면 Project Close 전에 Action/Known Issue로 명시한다.

## #57 MS-PROJECT-CLOSE-01

- 기존 Cloud Resource/Cost Exit Criteria에 DEC-P2-COST-01 준수 여부를 연결한다.
- Close는 삭제 명령 실행만으로 판정하지 않고 실제 resource inventory와 잔여 비용 위험을 확인한다.

## 적용 전 Issue snapshot

비용정책 운영 코멘트 적용 후 최신 snapshot:

- #34: updated_at `2026-09-30T13:12:04Z` — [P2-ARC-01] Hybrid / OCI / AWS / ROSA Architecture Freeze — [운영 코멘트](https://github.com/321Team/fds-project-baseline/issues/34#issuecomment-5912002564)
- #35: updated_at `2026-09-30T13:12:14Z` — [P2-IAC-01] AWS / ROSA Terraform IaC — [운영 코멘트](https://github.com/321Team/fds-project-baseline/issues/35#issuecomment-5912005719)
- #38: updated_at `2026-09-30T13:12:24Z` — [P2-ROSA-01] ROSA Platform / Security — [운영 코멘트](https://github.com/321Team/fds-project-baseline/issues/38#issuecomment-5912008823)
- #42: updated_at `2026-09-30T13:12:41Z` — [DEC-P2-REG-01] ROSA Image Registry Source Decision — [운영 코멘트](https://github.com/321Team/fds-project-baseline/issues/42#issuecomment-5912013508)
- #49: updated_at `2026-09-30T13:12:52Z` — [P2-DOC-01] Cloud / Hybrid Deliverable Freeze — [운영 코멘트](https://github.com/321Team/fds-project-baseline/issues/49#issuecomment-5912016585)
- #55: updated_at `2026-09-30T13:13:01Z` — [P2-REV-01] Phase 2 Review / Project Close Execution — [운영 코멘트](https://github.com/321Team/fds-project-baseline/issues/55#issuecomment-5912019416)
- #57: updated_at `2026-09-30T13:13:11Z` — [MS-PROJECT-CLOSE-01] Project Close — [운영 코멘트](https://github.com/321Team/fds-project-baseline/issues/57#issuecomment-5912022066)

적용 시점에 updated_at이 변경됐으면 최신 원문과 승인 변경을 다시 대조한다.
