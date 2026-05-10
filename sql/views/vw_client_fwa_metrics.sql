CREATE OR ALTER VIEW semantic.vw_client_fwa_metrics AS
SELECT
    c.client_key,
    c.client_name,
    c.client_type,
    d.calendar_year,
    d.month_number,
    COUNT(DISTINCT fc.claim_id) AS total_claims,
    SUM(fc.paid_amount) AS total_paid_amount,
    COUNT(DISTINCT fd.detection_id) AS fraud_detection_events,
    SUM(fd.suspected_exposure_amount) AS suspected_fraud_exposure,
    SUM(ia.stopped_payment_amount) AS stopped_payment_savings,
    SUM(ia.recovered_amount) AS recovered_dollars,
    CAST(COUNT(DISTINCT fd.detection_id) AS DECIMAL(18,4)) / NULLIF(COUNT(DISTINCT fc.claim_id),0) * 1000 AS fraud_events_per_1000_claims
FROM gold.dim_client c
JOIN gold.fact_claims fc ON c.client_key = fc.client_key
JOIN gold.dim_date d ON fc.service_date_key = d.date_key
LEFT JOIN gold.fact_fraud_detection fd ON fc.claim_id = fd.claim_id
LEFT JOIN gold.fact_investigation_actions ia ON fd.detection_id = ia.detection_id
GROUP BY c.client_key, c.client_name, c.client_type, d.calendar_year, d.month_number;
