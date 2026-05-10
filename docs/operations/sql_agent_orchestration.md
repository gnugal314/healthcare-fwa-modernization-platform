# SQL Agent Orchestration

Recommended job sequence:

1. Run SSIS package to extract SQL Server source tables.
2. Load Bronze tables.
3. Execute Silver conformance stored procedures.
4. Execute Gold fact/dimension loads.
5. Run semantic validation SQL tests.
6. Trigger Tableau extract refresh or Airflow downstream job.
7. Write job status to `audit.pipeline_run_log`.
