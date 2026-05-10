# Source-to-Target Mapping

| Source | Legacy Location | Modern Target | Transformation |
|---|---|---|---|
| Claims table | SQL Server / Access linked table | `bronze.claims_raw` → `gold.fact_claims` | Standardize status, dates, amounts, dimensions |
| Provider table | SQL Server | `gold.dim_provider` | SCD Type 2 provider attributes |
| Access fraud query | MS Access QueryDefs | `semantic.vw_provider_risk_summary` | Convert query logic to tested SQL view |
| Excel client report | Manual export | Tableau subscription / client portal | Use certified semantic views |
