# Kafka Streaming Fraud Alert Architecture

```mermaid
flowchart LR
    A[Claims Adjudication Events] --> B[Kafka Topic: claims.raw]
    B --> C[Stream Enrichment]
    C --> D[Kafka Topic: claims.enriched]
    D --> E[Fraud Rules + ML Scoring]
    E --> F[Kafka Topic: fraud.alerts]
    F --> G[SIU Case Queue]
    F --> H[Real-Time Tableau / Operations Monitor]
    F --> I[Gold fact_fraud_detection]
```

## Example Streaming Patterns

- Duplicate claim within short time window
- Rapid claim submission bursts by provider or pharmacy
- Opioid fill velocity across multiple prescribers
- High-dollar outlier claim compared with provider peer group
- Geographic clustering by county and pharmacy chain
