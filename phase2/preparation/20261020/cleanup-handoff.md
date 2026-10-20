# #55 정리·Review·Close 인계

근거: [하영 회신](https://github.com/321Team/fds-project-baseline/issues/55#issuecomment-6291486761),
[재환 회신](https://github.com/321Team/fds-project-baseline/issues/55#issuecomment-6291990233), 2026-10-20 KST.
기존 계획의 확인된 누락과 의존관계만 보완한다. **실제 삭제/회수 GO는 이 문서에 포함하지 않는다.**

| 선행·순서 | 실행/생산 담당 → 소비·수용 | 완료 증거·실패 처리 |
|---|---|---|
| 1 시험·E2E 원본 보존 | 각 생산 Lead→권욱 | 원본·해시·RUN·실행/원복·검토 링크 수신. 창 A 증적 PR은 재환 담당, 기존3/3 원본 재제출 불필요 |
| 2 DB 소비 중지·W4/A2 원복 | 앱/Secret 소비중지 하영, db01 세션 확인·원복 재환, 장애 인수 권욱 | 10.20.0.0/16 소비 세션0 확인과 기존 동일 RUN 원복. A2는 현재 NOT_RUN. 세션 정리 지연 시 기존 STOP/원복 마감을 우선하고 시간 초과까지 DB 예외를 유지하지 않음 |
| 3 V9 양쪽 원복·최종 반출 | 재환·하영→권욱 | 양쪽 동일 RUN·기존 GO 수명 안에 원복/보고. **Relay 삭제 전에 V9**. DB 원복은 VPN 원복과 독립 확인 |
| 4 ROSA 소비/보존 종료→namespace·클러스터 삭제 | 하영→권욱 | Review 및 필요한 시험·증적 보존 종료 후, 실제 승인된 자원만. 삭제 exact absence 확인 후 다음 기반으로 진행 |
| 5 operator role/OIDC→전용 prereq IAM | 하영, 중앙 관련 권욱 | cluster 삭제·다른 소비자 없음 확인. 공용 backend/bootstrap/중앙 IAM/SSM 공용 문서는 기본 보존 |
| 6 Network/VPN/Relay 기반 정리 | 하영·재환 | 소비 의존성 해소·V9/반출 수신 후 actual Plan의 소유 자원만. 예상 밖 delete/replace/불명확 상태면 다음 기반 삭제 STOP |
| 7 vpn-gw01 bundle·RUN state 정리 | **재환** | 최종 V9·원본 반출/수신 뒤 남은 파일 정리·readback. Relay 파일은 해당 자원 최종 삭제와 연결. Libreswan package는 10/26 P1 자원 정리 단계와 구분하며 지금 별도 uninstall하지 않음 |
| 8 자격·전용 권한 최종 정리 | 각 발급/운영 Lead, 권욱 통합 | IAM 본인 access key0, 임시 cluster-admin 잔여0, VPN PSK/Relay·Harbor Robot/Source/Push 계정의 기존 범위별 회수·readback. Secret 삭제만으로 DB 자격 완전 회수라고 하지 않음 |

여러 소비자가 있으면 위 표는 자원별 의존 그래프에 적용한다. 무조건 직렬 실행하거나 이미 승인된 정리보다 만료를 늦추는 새 순서가 아니다.
검증 전용 권한은 시험·결함 재시험·원본 반출/검토 완료까지 유지하고 이후 정리한다. 필요한 운영 최소 권한은 별도 유지한다.
이는 새 포괄 권한 부여나 현재 분리된 정책 재부착 승인이 아니다.

삭제 실패·응답 유실·state 읽기 불가·미분류 잔존은 다음 기반 삭제를 중단한다. 기존 45분 읽기 재대조/인수안을 재사용하고,
state rm·force unlock·일괄 재destroy·유일 원본 폐기로 우회하지 않는다. 자원 삭제는 필요 시 재생성/보존 자료 복원이며 즉시 undo라고 하지 않는다.
비용은 지정 세션 중앙 추적, 승인 규모 유지에 새 비용 GO·시간별 상한을 추가하지 않는다. 실제 잔존/보안 수명·최종 정리 책임은 그대로다.

#55 Action 필드는 `출처·단계·Owner·Due(미정 허용)·완료조건·증거·수용 책임·상태`를 사용한다.
미발생 Action/Runtime 값을 채우지 않는다. 10/23 Review와 10/26 Close의 실제 Sign-off는 별도이며 준비 문서로 티켓을 닫지 않는다.
