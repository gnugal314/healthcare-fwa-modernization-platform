# Enterprise Modernization Blueprint

## 1. Understand the Business Domain

Healthcare Fraud, Waste, and Abuse analytics identifies suspicious claims, providers, pharmacies, members, and schemes that create avoidable financial exposure. Consumers of this platform include SIU investigators, Medicare/Medicaid reporting teams, commercial payer clients, employer groups, executives, compliance, and data governance teams.

## 2. Current-State Legacy Architecture

```text
SQL Server source tables
  → MS Access linked tables
  → Access queries + VBA/macros
  → Excel spreadsheets
  → Manual client distribution
```

## 3. Problems with Current State

- Business rules are trapped in Access queries and macros.
- Excel files create version-control and PHI distribution risk.
- KPI logic is duplicated across reports.
- Manual processes create SLA and operational risk.
- Lineage is weak; audit evidence requires manual reconstruction.
- Access does not support modern ML, streaming, CI/CD, or scalable governance.

## 4. Recommended Future-State Architecture

```text
SQL Server
  → SSIS/Python ingestion
  → Bronze landing
  → Silver conformance
  → Gold dimensional marts
  → Semantic views
  → Tableau certified data sources
  → Secure client distribution
```

## 5. Best Enterprise Microsoft-Centric Architecture

Use SQL Server/SSIS where they are strong: reliable extraction, relational storage, stored procedures, security, and SQL Agent orchestration. Use Python where Access/VBA becomes fragile: fraud scoring, synthetic data, anomaly detection, geospatial analysis, API movement, and automated testing.

## 6. Data Architecture Design Principles

- Governed by design
- Source-aligned Bronze retention
- Conformed Silver entity resolution
- Dimensional Gold analytics layer
- Reusable semantic views
- Automated validation and reconciliation
- Privacy-preserving client distribution

## 7. Data Warehouse Design

The warehouse should be optimized for fraud reporting and investigative analytics. It should support claims-level detail, provider/member/pharmacy relationship analysis, scheme trending, savings/recovery reporting, and client/region security filtering.

## 8. Fact Tables and Dimension Tables

Facts store measurable events. Dimensions store descriptive business context. Surrogate keys decouple analytics history from operational source IDs.

## 9. Star Schema Examples

`fact_claims` connects to `dim_provider`, `dim_member`, `dim_pharmacy`, `dim_client`, `dim_region`, and `dim_date`. Fraud events and investigations connect to the same conformed dimensions.

## 10. Bronze/Silver/Gold Medallion Architecture

Bronze is raw, Silver is cleaned and standardized, Gold is dimensional and KPI-ready. This separation improves traceability, auditability, and controlled business logic.

## 11. ETL/ELT Modernization Strategy

Start by extracting current Access logic into documented SQL and Python modules. Validate modern outputs against legacy Excel reports. Once reconciled, promote the semantic views as the system of record.

## 12. Recommended Tool Split

| Capability | Tool |
|---|---|
| SQL extraction | SSIS |
| Complex transformations | Python |
| Warehouse | SQL Server |
| Cross-platform orchestration | Airflow |
| Microsoft-native scheduling | SQL Agent |
| BI | Tableau |
| Code validation | GitHub Actions |

## 13. Why Python Matters

Python enables reproducible fraud analytics, data quality checks, ML scoring, synthetic data creation, and deployment automation while replacing fragile VBA logic with modular tested code.

## 14. Example Python Fraud Transformation Code

See `/pipelines/python/etl/silver_to_gold.py` and `/pipelines/python/scoring/provider_risk_scoring.py`.

## 15. KPI Layer Design

KPI logic belongs in semantic SQL views where it can be version controlled, tested, reused, and certified.

## 16. Example Healthcare Fraud KPIs

- Fraud dollar exposure
- Stopped payment savings
- Recovered dollars
- High-risk provider count
- Duplicate claim rate
- Suspicious opioid claim rate
- Provider risk score
- Geographic fraud concentration

## 17. Semantic Views

Semantic views hide physical model complexity and expose durable analytics contracts to Tableau and downstream clients.

## 18. Example SQL Semantic Views

See `/sql/views`.

## 19. Tableau Modernization

Tableau should consume certified data sources backed by semantic views. Avoid repeating business logic across workbooks.

## 20. Example Tableau Dashboards

See `/tableau/dashboards` for wireframes and dashboard specifications.

## 21. Client Distribution Modernization

Replace manual spreadsheet distribution with Tableau subscriptions, embedded portals, secure extracts, APIs, and audited delivery logs.

## 22. Old Workflow vs Modern Workflow

| Old | Modern |
|---|---|
| Access query | Versioned SQL/Python |
| Macro export | Orchestrated pipeline |
| Manual Excel | Governed dashboard/subscription |
| Local logic | Semantic layer |
| Manual QA | Automated data quality |

## 23. Future-State Delivery Options

- Tableau Server dashboards
- Tableau subscriptions
- Embedded analytics in client portal
- Secure SFTP/API extracts
- Executive PDF packs

## 24. Tableau Server Architecture

Use projects for domain separation, certified data sources for governed metrics, groups for RBAC, and subscriptions for scheduled delivery.

## 25. Embedded Analytics Architecture

Embed Tableau dashboards in a secure payer/client portal using trusted authentication and passing client context to enforce row-level security.

## 26. Scheduled PDF Reporting Architecture

Airflow or SQL Agent triggers data refresh, validates KPI outputs, refreshes extracts, and sends controlled Tableau subscriptions.

## 27. Security and Compliance

Security design includes PHI minimization, encryption, RBAC, RLS, audit logs, approval workflows, and client isolation.

## 28. HIPAA Considerations

Analytics environments containing PHI should follow minimum necessary access, controlled disclosures, user access reviews, encryption, audit logs, and retention controls.

## 29. PHI Masking Examples

See `/sql/security/phi_masking_examples.sql` and `/pipelines/python/etl/mask_phi.py`.

## 30. Row-Level Security

RLS filters records by client, region, and role so users only see authorized populations.

## 31. Tableau Row-Level Security Examples

See `/tableau/rls/tableau_rls_design.md`.

## 32. Auditability and Lineage

Each pipeline should write batch ID, source file/query, row counts, hash totals, DQ results, user, and execution timestamp.

## 33. Automation Orchestration Workflows

Use dependency-aware orchestration from ingestion through dashboard refresh.

## 34. SQL Agent Orchestration

SQL Agent can schedule SSIS packages, stored procedures, and SQL validations for Microsoft-centered deployments.

## 35. Airflow Orchestration

Airflow coordinates SQL, Python, DQ, ML scoring, and Tableau refresh APIs across environments.

## 36. CI/CD Pipelines

CI/CD validates Python tests, SQL linting, DQ config, and package build before deploy.

## 37. GitHub Actions Examples

See `/ci_cd/github_actions/ci.yml`.

## 38. Data Quality Validation

Validate row counts, duplicates, referential integrity, null constraints, metric ranges, and historical trend variance.

## 39. Great Expectations Examples

See `/tests/data_quality/great_expectations_claims.yml`.

## 40. Advanced Feature Enhancements

ML risk scoring, streaming fraud alerts, graph analytics, geospatial hot spot detection, and near-real-time dashboards.

## 41. Machine Learning Fraud Detection

Use supervised models when labeled outcomes exist and anomaly detection when labels are sparse.

## 42. Provider Risk Scoring

Risk score features include claim velocity, high-dollar rate, opioid rate, denial rate, duplicate rate, and peer-group outlier position.

## 43. Anomaly Detection

Isolation Forest, robust z-scores, and time-series baselines can flag unusual claim patterns before monthly reporting.

## 44. Real-Time Streaming Detection

Claim events can be evaluated in near-real time to identify bursts, duplicate submissions, and high-risk provider/pharmacy patterns.

## 45. Kafka Architecture

Kafka topics separate raw claim events, enriched events, fraud alerts, and investigation action events.

## 46. Geospatial Fraud Analytics

Latitude/longitude, county, state, and market dimensions support heatmaps, regional clustering, and suspicious concentration detection.

## 47. Migration Strategy

Migrate by domain/report family, not by technology component only. Keep legacy and modern outputs running in parallel until validated.

## 48. Phase-by-Phase Modernization Roadmap

See `/docs/migration/roadmap.md`.

## 49. Recommended Final Architecture

The recommended architecture is a SQL Server-centered dimensional warehouse with SSIS/Python ingestion, semantic SQL views, Tableau Server certified data sources, governed client delivery, ML scoring, and auditable orchestration.

## 50. Problem vs Modern Solution Comparison Table

| Current Problem | Modern Solution |
|---|---|
| Access logic is opaque | Versioned SQL/Python with documentation |
| Excel distribution is risky | Secure Tableau/portal delivery |
| Manual refresh | Airflow/SQL Agent orchestration |
| No metric consistency | Semantic KPI views |
| Weak audit evidence | Batch logs, lineage, DQ results |
| Limited fraud intelligence | ML scoring and streaming alerts |
