USE HealthcareFWA;
GO

CREATE OR ALTER VIEW semantic.vw_client_fwa_metrics AS
SELECT
    c.client_name,
    c.client_type,
    COUNT(fc.claim_key) AS total_claims,
    SUM(fc.billed_amount) AS total_billed_amount,
    SUM(fc.paid_amount) AS total_paid_amount,
    SUM(fc.denied_amount) AS total_denied_amount,
    SUM(fc.stopped_payment_amount) AS total_stopped_payment_amount,
    SUM(fc.recovered_amount) AS total_recovered_amount,
    AVG(fc.fraud_risk_score) AS avg_fraud_risk_score
FROM gold.fact_claims fc
LEFT JOIN gold.dim_client c
    ON fc.client_key = c.client_key
GROUP BY
    c.client_name,
    c.client_type;
GO

CREATE OR ALTER VIEW semantic.vw_provider_risk_summary AS
SELECT
    p.provider_npi,
    p.provider_name,
    p.provider_type,
    r.state,
    r.region_name,
    COUNT(fc.claim_key) AS total_claims,
    SUM(fc.paid_amount) AS total_paid_amount,
    SUM(fc.billed_amount) AS total_billed_amount,
    AVG(fc.fraud_risk_score) AS avg_fraud_risk_score,
    MAX(fc.fraud_risk_score) AS max_fraud_risk_score,
    SUM(fc.stopped_payment_amount) AS stopped_payment_amount,
    SUM(fc.recovered_amount) AS recovered_amount
FROM gold.fact_claims fc
LEFT JOIN gold.dim_provider p
    ON fc.provider_key = p.provider_key
LEFT JOIN gold.dim_region r
    ON fc.region_key = r.region_key
GROUP BY
    p.provider_npi,
    p.provider_name,
    p.provider_type,
    r.state,
    r.region_name;
GO

CREATE OR ALTER VIEW semantic.vw_geographic_exposure AS
SELECT
    r.region_name,
    r.state,
    r.city,
    r.latitude,
    r.longitude,
    COUNT(fc.claim_key) AS total_claims,
    SUM(fc.billed_amount) AS total_billed_amount,
    SUM(fc.paid_amount) AS total_paid_amount,
    SUM(fc.stopped_payment_amount) AS stopped_payment_amount,
    AVG(fc.fraud_risk_score) AS avg_fraud_risk_score
FROM gold.fact_claims fc
LEFT JOIN gold.dim_region r
    ON fc.region_key = r.region_key
GROUP BY
    r.region_name,
    r.state,
    r.city,
    r.latitude,
    r.longitude;
GO