# Dimensional Model

## Grain Definitions

| Table | Grain |
|---|---|
| `fact_claims` | One prescription/professional claim line |
| `fact_fraud_detection` | One fraud detection event per entity, scheme, and detection date |
| `fact_investigation_actions` | One SIU action per investigation event |

## Surrogate Keys

Every dimension uses integer surrogate keys. Source identifiers such as NPI, member ID, NCPDP, and client code are retained as alternate/business keys.

## Slowly Changing Dimensions

- `dim_provider`: SCD Type 2 for specialty, network status, and address changes.
- `dim_member`: Type 2 for plan/client/region changes.
- `dim_pharmacy`: Type 2 for ownership and chain changes.
- `dim_client`: Type 1 for descriptive updates unless contractual history is required.

## Star Schema

```mermaid
erDiagram
    dim_provider ||--o{ fact_claims : provider_key
    dim_member ||--o{ fact_claims : member_key
    dim_pharmacy ||--o{ fact_claims : pharmacy_key
    dim_client ||--o{ fact_claims : client_key
    dim_region ||--o{ fact_claims : region_key
    dim_date ||--o{ fact_claims : service_date_key
    dim_fraud_scheme ||--o{ fact_fraud_detection : scheme_key
    fact_claims ||--o{ fact_fraud_detection : claim_id
    fact_fraud_detection ||--o{ fact_investigation_actions : detection_id
```
