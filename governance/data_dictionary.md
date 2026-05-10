# Data Dictionary

| Field | Table | Description |
|---|---|---|
| `claim_id` | `fact_claims` | Synthetic claim identifier |
| `provider_key` | facts/dim_provider | Surrogate provider key |
| `member_key` | facts/dim_member | Surrogate member key |
| `pharmacy_key` | facts/dim_pharmacy | Surrogate pharmacy key |
| `risk_score` | `fact_fraud_detection` | Score from rules or ML model |
| `suspected_exposure_amount` | `fact_fraud_detection` | Estimated financial exposure |
| `stopped_payment_amount` | `fact_investigation_actions` | Prevented payment dollars |
| `recovered_amount` | `fact_investigation_actions` | Post-payment recovered dollars |
