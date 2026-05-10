# Lineage Documentation

```text
SQL Server claims source
  → SSIS extract batch_id
  → Bronze raw CSV/table
  → Silver conformed claims
  → Gold fact_claims
  → semantic.vw_client_fwa_metrics
  → Tableau Executive Summary Dashboard
  → Client subscription / portal access log
```

Each pipeline writes:

- batch ID
- source system/query
- row counts in/out
- rejected row counts
- hash totals for financial fields
- validation result
- execution timestamp
- actor/service account
