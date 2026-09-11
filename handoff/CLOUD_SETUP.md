# Cloud Codex와 공용 PC 운영

현재 저장소에 구현한 것은 공통 지침과 검증 도구다. 사용자의 실제 Cloud 환경 및
교육장 Windows 설정은 아직 확인하지 않았으며 UNVERIFIED다.

## Cloud 환경에서 확인할 항목

1. 본인 계정으로 Codex의 GitHub 연결과 허용 저장소를 확인한다. 필요한 Private
   저장소만 선택하고 기존 팀 역할·승인 권한을 유지한다.
2. 작업 저장소와 `321Team/fds-project-baseline`을 읽을 수 있어야 한다.
   시작 시 baseline main의 WORK_START/AGENTS/lock을 읽고 해당 main Commit을 기록한다.
   이미 시작된 세션의 지침이 바뀌면 새 세션으로 로딩한다.
3. Python 3.10 이상과 표준 라이브러리로 공통 검증/Kit 시험을 실행한다.
   기존 WBS 검증에는 기존 프로젝트의 openpyxl 의존성이 추가로 필요하다.
4. live 검증에는 정상 인증된 `gh api`의 읽기 권한과 api.github.com 접근이 필요하다.
   Cloud의 저장소 clone 권한이 `gh` 로그인까지 제공한다고 가정하지 않는다.
   없는 경우 환경의 정식 인증 절차로 구성한다. Connector 토큰 추출·복사로 우회하지 않는다.
5. Cloud GitHub 접근과 증적 읽기가 검증되면 Task/receipt를 만들고 check를 실행한다.
   `capture --api-export` 성공은 live check 성공을 대체하지 않는다.
6. 네트워크를 최소 범위로 허용한다. 이 도입에는 교육장 관리망, SSH, kubeconfig,
   CA 개인키, 서버 자격증명이 필요하지 않다. 실제 Runtime은 기존 현장 실행 절차를 따른다.

```bash
python --version
python -m unittest discover -s tests -p 'test_shared_context.py'
python scripts/shared_context.py --help
```

Cloud UI의 저장소 연결·실행 기록 URL, 사용 모델, 지침 Commit, 인증된 읽기 검사 결과를
첫 인계 Result에 기록한다. 설치/권한 변경 완료 표시는 실제 성공 증적을 확보한 뒤 한다.

## 교육장 PC

- 평일/주말 공용 Windows 계정은 개인 계정 격리가 아니다. SecretFolder는 폴더 숨김/
  접근 제한의 보조 수단으로 유지하며 암호화 저장소로 취급하지 않는다.
- 가능하면 개인 Windows 표준 계정을 사용한다. 같은 관리자 계정을 공유하는 현 상태에서는
  중요한 개인 원본·저장소·장기 인증정보를 PC에 내려받지 않는 Cloud 중심 운영을 적용한다.
- 웹 접속은 개인 세션으로 사용하고 브라우저 동기화·비밀번호 저장·로그인 유지를 끈다.
  종료 시 로그아웃, 모든 개인 세션 창 종료, 생성된 다운로드·휴지통 파일을 정리한다.
  시크릿 창은 다운로드 파일 삭제나 기기 관리자에 대한 격리를 보장하지 않는다.
- 교육장에는 그날 승인된 실행 Kit만 전달한다. 원본 증적은 기존 통제 경로로 수집하고
  수신 Commit/Hash로 연결한다. 개인 외장 저장소가 필요하면 기관이 허용한 암호화 방식을 쓴다.
- 주말반 점유 시간의 교육장 작업 용량은 기존 결정대로 0이다. Cloud 작업 가능 여부가
  현장 일정/AC 변경을 뜻하지 않는다.

참고: [OHSoft SecretFolder](https://ohsoft.net/kor/secretfolder.php),
[Codex Cloud 환경](https://learn.chatgpt.com/docs/environments/cloud-environment),
[AGENTS 지침](https://learn.chatgpt.com/docs/agent-configuration/agents-md).
