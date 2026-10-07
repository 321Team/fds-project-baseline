# D22 Harbor Robot metadata read-only capture

Source contract: [Harbor v2.13.1 API](https://github.com/goharbor/harbor/blob/v2.13.1/api/v2.0/swagger.yaml), GET /robots, Robot/RobotPermission/Access schemas.

## Execution-location prerequisite — 2026-10-05 review follow-up
Runner→DNS52/53 failures were recorded in baseline #37 comments5980791972/5980821721. Until DNS allowance and name resolution at the actual execution location are confirmed, do not run this collector on Runner expecting success. Confirm harbor.fds.internal resolution through the approved DNS path at the chosen execution location. Do not bypass with /etc/hosts, IP URL, disabled TLS, or an unapproved DNS change. Existing successful metadata need not be collected again. This note does not declare that the DNS issue remains unresolved in every environment; consume later evidence if available.

## Run on cicd-runner01

Save [harbor-robot-readonly.py](harbor-robot-readonly.py) as
/home/server01_cicd-runner/harbor-robot-readonly.py using GitHub Raw/download and your existing file transfer method.
Requires Python 3, an interactive terminal, and existing DNS resolution for harbor.fds.internal. Pass the existing public Root CA PEM path explicitly with --ca-file; the expected PEM SHA256 remains pinned in code. No hosts override or DNS configuration change is included.

```bash
if python3 /home/server01_cicd-runner/harbor-robot-readonly.py --ca-file "$HOME/.config/containers/certs.d/10.1.93.54/ca.crt"; then
  printf 'D22_ROBOT_EXIT_CODE=0\n'
else
  d22_robot_rc=$?
  printf 'D22_ROBOT_EXIT_CODE=%s\n터미널은 유지됩니다.\n' "$d22_robot_rc"
fi
```

Use an existing Harbor account that can read the relevant Robot metadata. Enter its password or OIDC CLI secret only at the hidden prompt; do not paste it into chat. This does not ask for either target Robot secret. No account creation, credential rotation, permission changes, POST/PUT/PATCH/DELETE, login/pull/push tests.

The wrapper reports the child exit code without changing parent shell options; its final shell status is not the collector status. Run the complete if block.

## Output and interpretation

Output directory: ~/d22-robot-ro-<random>, mode 0700; files mode 0600:
- robot-metadata.json: allowlisted metadata for exact names robot$worker and robot$push.
- SHA256SUMS: checksum of that JSON file.

Share the printed metadata and READONLY_CAPTURE / D22_ROBOT_EXIT_CODE lines. No raw API body, password, authorization header, description, or secret field is written. Console JSON escapes control characters.

CAPTURED_REVIEW_REQUIRED means both names were captured, not that privilege/expiry policy passed.
PARTIAL_MISSING_TARGETS (exit 2) means missing or not visible to the account; not proof of global absence. HTTP 401/403 stops; use the existing access process, do not create grants for this script.

expires_at is preserved as the API integer; positive values also have a KST rendering. Zero/negative values remain explicit without guessing their meaning. disable, duration, permission kind/namespace/resource/action/effect are preserved. Omitted effect is null, not inferred allow. Compare actual project permissions and expiry with the input contract after capture.

HTTPS connects to harbor.fds.internal and verifies its FQDN SAN using only pinned CA bytes. The example CA storage directory retains the existing IP name; this does not change the HTTPS endpoint or container runtime trust. Ambient proxies and redirects are disabled. An unauthenticated GET probe checks DNS/TLS before the credential prompt; 200/401/403 only allow that preflight to continue. Authenticated 401/403 still stops. DNS/TLS failure has no IP/insecure fallback. GET list pagination is bounded to 100 data pages plus an empty-page check; repeated IDs and malformed metadata stop capture. Results are not an atomic snapshot if accounts change while paging.

The 2026-10-04 field USER_READBACK in the D22 contract §1.3 reports IP and FQDN SANs. This is not a new live certificate verification by this collector. Existing captured Robot metadata need not be collected again solely because this preparation tool changed. On failure preserve the STOP/exit status, resolve the existing DNS/CA access prerequisite, and rerun only when needed; no server change or rollback is part of this read-only command.

## Validation

10 local offline unittest cases passed on 2026-10-04: pagination and secret omission; missing targets; duplicate IDs; invalid JSON; missing fields; wrong scalar types; disabled/expired metadata; negative expiry; redirects; safe 401/403 diagnostics. No live Harbor API call performed by the author.
Run: python3 -m unittest discover -s phase2/runbooks -p test_harbor_robot_readonly.py

Revision follow-up: 15 local offline tests PASS (the original 10 plus FQDN endpoint, bad/missing CA, explicit CA path with strict TLS, and connection failure before credential input). Tests use mocks and do not establish live DNS/TLS/API success. Code review pending; Phase 2 Freeze HOLD remains. This collector supplies metadata evidence only.
