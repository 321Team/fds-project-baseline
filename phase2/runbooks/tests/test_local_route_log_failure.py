#!/usr/bin/env python3
"""Offline fault injection for local-route logging; never contacts a host."""
import os
from pathlib import Path
import subprocess
import tempfile

SCRIPT = Path(__file__).resolve().parents[1] / "collect-local-management-route.sh"

def run_case(mode, expected_rc, expected_state):
    with tempfile.TemporaryDirectory(prefix="route-log-test-") as name:
        root = Path(name)
        bindir = root / "bin"
        bindir.mkdir()
        ip = bindir / "ip"
        ip.write_text("""#!/bin/bash
if [[ "$*" == "-j -4 address show" ]]; then
  echo '[{"addr_info":[{"local":"10.250.10.20"}]}]'
elif [[ "${TEST_MODE:-}" == command_fail ]]; then
  exit 3
else
  echo 'MOCK local route metadata'
fi
""")
        ip.chmod(0o700)
        envfile = root / "fault-env"
        envfile.write_text("""printf() {
  case "${TEST_MODE:-}" in
    header) [[ "$1" == *COMMAND ]] && return 77;;
    rc) [[ "$1" == 'RC=%s\\n' ]] && return 77;;
    final) [[ "$1" == *NOT_PROVEN* ]] && return 77;;
  esac
  builtin printf "$@"
}
""")
        env = dict(os.environ, HOME=str(root), BASH_ENV=str(envfile),
                   TEST_MODE=mode, PATH=str(bindir)+os.pathsep+os.environ["PATH"])
        p = subprocess.run(["bash", str(SCRIPT), "runner"], env=env,
                           capture_output=True, text=True)
        assert p.returncode == expected_rc, (mode, p.returncode, p.stderr)
        assert expected_state in p.stdout+p.stderr, (mode, p.stdout, p.stderr)
        if mode in ("header", "rc", "final"):
            assert "STATE=CAPTURED_REVIEW_REQUIRED" not in p.stdout
            assert not list(root.glob("p2-local-route.*/SHA256SUMS"))
        else:
            dirs = list(root.glob("p2-local-route.*"))
            assert len(dirs) == 1
            subprocess.run(["sha256sum", "-c", "SHA256SUMS"], cwd=dirs[0],
                           check=True, capture_output=True)
            assert dirs[0].stat().st_mode & 0o777 == 0o700
            assert (dirs[0]/"local-route.txt").stat().st_mode & 0o777 == 0o600

if __name__ == "__main__":
    for case in (("normal",0,"CAPTURED_REVIEW_REQUIRED"),
                 ("command_fail",1,"PARTIAL_REVIEW_REQUIRED"),
                 ("header",2,"INCOMPLETE_LOG_WRITE"),
                 ("rc",2,"INCOMPLETE_LOG_WRITE"),
                 ("final",2,"INCOMPLETE_LOG_WRITE")):
        run_case(*case)
        print("PASS", case[0])
