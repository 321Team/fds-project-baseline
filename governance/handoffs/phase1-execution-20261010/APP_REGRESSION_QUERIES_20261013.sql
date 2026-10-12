-- Phase1 preparation only. Do not execute without explicit psql variables and confirmed read path.
-- Before: psql -X -v ON_ERROR_STOP=1 -v run_first=YYYYMMDDHHMM -v run_last=YYYYMMDDHHMM
-- The two bounds must be validated 12-digit KST minutes in one agreed window/date.
-- Preserve stdout/stderr, rc and time. The COUNT must be exactly zero before sending requests.
SELECT count(*) AS existing_rows_in_planned_run_window
FROM transactions
WHERE left(account_id, 7) = 'SIM_rg_'
  AND substring(account_id from 8 for 12) BETWEEN :'run_first' AND :'run_last'
  AND substring(account_id from 20 for 1) = '_';

-- After: separate invocation with actual meta.json RUN in -v run=YYYYMMDDHHMM.
-- Use psql -X -A -t -F '|' -v ON_ERROR_STOP=1; preserve the output as DB_LOG.
-- Execute before/after cards separately; this file is a template, not a combined script.
SELECT account_id, transaction_id, transaction_type, amount,
       fds_detected, fds_evaluation_skipped,
       coalesce((SELECT string_agg(r->>'rule_id', ',')
                 FROM jsonb_array_elements(fds_rules) r
                 WHERE (r->>'triggered')::bool), '-'), occurred_at
FROM transactions
WHERE left(account_id, length('SIM_rg_' || :'run' || '_')) = 'SIM_rg_' || :'run' || '_'
ORDER BY received_at;

-- Existing six PromQL queries, preserve actual timestamps/target set and response, not only summaries:
-- sum(transaction_save_success_total)
-- sum(transaction_save_failure_total)
-- sum(missing_client_ip_total)
-- sum(fds_evaluated_total)
-- sum by (rule_id)(fds_detected_total)
-- count(up{job=~"transaction-api|fds-engine"}==1)
