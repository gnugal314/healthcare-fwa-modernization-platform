CREATE OR ALTER VIEW semantic.vw_geographic_exposure AS
SELECT
    r.region_key,
    r.state_code,
    r.county,
    r.market,
    r.latitude,
    r.longitude,
    COUNT(DISTINCT fd.detection_id) AS fraud_events,
    SUM(fd.suspected_exposure_amount) AS suspected_exposure,
    AVG(fd.risk_score) AS avg_risk_score,
    COUNT(DISTINCT fc.provider_key) AS impacted_provider_count,
    COUNT(DISTINCT fc.member_key) AS impacted_member_count
FROM gold.dim_region r
LEFT JOIN gold.fact_claims fc ON r.region_key = fc.region_key
LEFT JOIN gold.fact_fraud_detection fd ON fc.claim_id = fd.claim_id
GROUP BY r.region_key, r.state_code, r.county, r.market, r.latitude, r.longitude;
