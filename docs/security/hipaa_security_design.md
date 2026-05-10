# Security + HIPAA Governance Design

## Controls

- Minimum necessary access by role and client assignment
- Encryption in transit and at rest
- PHI masking/tokenization where detail is not required
- SQL Server roles and Tableau groups
- Row-level security by client and region
- Audit logs for extracts, dashboard access, and file delivery
- Data retention policies and secure deletion
- Break-glass access with approval and logging

## Secure Client Isolation

Client-facing dashboards must filter by `client_key`, use dedicated Tableau groups, and avoid exposing row-level PHI unless contractually authorized and approved.
