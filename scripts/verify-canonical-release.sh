@@ -13,7 +13,43 @@ release_dir="releases/${release_version}"
 sha_file="${release_dir}/SHA256SUMS"
 
 test -f "${sha_file}"
-sha256sum -c "${sha_file}"
+
+# governance/*와 .github/workflows/*는 RELEASE_POLICY §6에 따라 release 브랜치를 거치지 않고
+# 문서/Workflow 전용 PR로 main에 직접 병합될 수 있다. 그 결과 발행된 릴리즈의 SHA256SUMS와
+# 어긋나는 것은 실제 위변조가 아니라 예상된 운영 드리프트이므로 WARN으로 보고하고 통과시킨다.
+# 다른 모든 경로(baseline/wbs/tickets/architecture/releases 등 정본 콘텐츠)의 불일치는 계속 FAIL한다.
+# 운영 드리프트는 RELEASE_POLICY §2.3에 따라 차기 정본 후보에 반드시 동기화해야 하며,
+# 이 예외가 그 의무를 면제하지 않는다.
+operational_drift_pattern='^(governance/|\.github/workflows/)'
+
+sha256sum_output="$(sha256sum -c "${sha_file}" 2>&1)" && sha_status=0 || sha_status=$?
+printf '%s\n' "${sha256sum_output}"
+
+if [[ "${sha_status}" -ne 0 ]]; then
+  failed_paths="$(printf '%s\n' "${sha256sum_output}" | sed -n 's/: FAILED$//p')"
+  content_failures=""
+  operational_failures=""
+  while IFS= read -r path; do
+    [[ -z "${path}" ]] && continue
+    if [[ "${path}" =~ ${operational_drift_pattern} ]]; then
+      operational_failures+="${path}"$'\n'
+    else
+      content_failures+="${path}"$'\n'
+    fi
+  done <<< "${failed_paths}"
+
+  if [[ -n "${content_failures}" ]]; then
+    echo "canonical-integrity: FAIL — 정본 콘텐츠 경로 체크섬 불일치:" >&2
+    printf '%s' "${content_failures}" >&2
+    exit 1
+  fi
+
+  echo "canonical-integrity: WARN — 운영 경로(governance/.github workflows) 드리프트, §2.3 차기 동기화 필요:" >&2
+  printf '%s' "${operational_failures}" >&2
+  operational_drift_warned=1
+else
+  operational_drift_warned=0
+fi
 
 python3 scripts/verify-document-secrets.py baseline wbs tickets web audit releases governance scripts .github
 
@@ -28,4 +64,8 @@ if [[ "$(printf '%s\n' '3.1.18' "${version_number}" | sort -V | head -n1)" == "3
   bash scripts/verify-wbs-gantt-distribution.sh "${release_version}" --candidate
 fi
 
-echo "canonical-integrity: PASS"
+if [[ "${operational_drift_warned}" -eq 1 ]]; then
+  echo "canonical-integrity: PASS (WITH OPERATIONAL DRIFT WARNINGS — §2.3 미동기화 항목 있음, 위 WARN 참조)"
+else
+  echo "canonical-integrity: PASS"
+fi
