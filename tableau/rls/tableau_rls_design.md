# Tableau Row-Level Security Design

## Pattern

1. Warehouse contains `security.user_client_access`.
2. Semantic views expose `client_key` and `region_key`.
3. Tableau data source joins or filters on entitlement table.
4. Tableau groups map to client access roles.

## Example Tableau Calculation

```text
[User Access Allowed] = [Client Key] IN [Entitled Client Keys]
```

## Governance Rules

- Never publish unrestricted PHI data sources to shared projects.
- Certify only semantic views that have passed KPI validation.
- Separate internal SIU dashboards from client-facing dashboards.
- Use extract encryption and refresh schedules approved by data owners.
