CREATE OR ALTER VIEW semantic.vw_provider_risk_summary AS
SELECT
    p.provider_key,
    p.npi,
    p.provider_name,
    p.specialty,
    r.state_code,
    r.county,
    COUNT(DISTINCT fc.claim_id) AS claim_count,
    SUM(fc.paid_amount) AS paid_amount,
    AVG(fd.risk_score) AS avg_risk_score,
    MAX(fd.risk_score) AS max_risk_score,
    SUM(fd.suspected_exposure_amount) AS suspected_exposure,
    SUM(CASE WHEN fc.is_opioid = 1 THEN 1 ELSE 0 END) AS opioid_claim_count,
    SUM(CASE WHEN fc.claim_status = 'Denied' THEN 1 ELSE 0 END) AS denied_claim_count
FROM gold.dim_provider p
LEFT JOIN gold.fact_claims fc ON p.provider_key = fc.provider_key
LEFT JOIN gold.fact_fraud_detection fd ON fc.claim_id = fd.claim_id
LEFT JOIN gold.dim_region r ON p.region_key = r.region_key
GROUP BY p.provider_key, p.npi, p.provider_name, p.specialty, r.state_code, r.county;
