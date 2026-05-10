CREATE OR ALTER PROCEDURE gold.sp_load_fact_claims
    @ingestion_batch_id UNIQUEIDENTIFIER
AS
BEGIN
    SET NOCOUNT ON;

    INSERT INTO gold.fact_claims (
        claim_id, service_date_key, paid_date_key, provider_key, member_key, pharmacy_key,
        client_key, region_key, claim_type, diagnosis_code, procedure_code, ndc_code,
        drug_name, is_opioid, billed_amount, allowed_amount, paid_amount, denied_amount,
        claim_status, ingestion_batch_id
    )
    SELECT
        s.claim_id, s.service_date_key, s.paid_date_key, p.provider_key, m.member_key, ph.pharmacy_key,
        c.client_key, r.region_key, s.claim_type, s.diagnosis_code, s.procedure_code, s.ndc_code,
        s.drug_name, s.is_opioid, s.billed_amount, s.allowed_amount, s.paid_amount, s.denied_amount,
        s.claim_status, @ingestion_batch_id
    FROM silver.claims_conformed s
    JOIN gold.dim_provider p ON s.provider_id = p.provider_id AND p.is_current = 1
    JOIN gold.dim_member m ON s.member_id = m.member_id AND m.is_current = 1
    LEFT JOIN gold.dim_pharmacy ph ON s.pharmacy_id = ph.pharmacy_id AND ph.is_current = 1
    JOIN gold.dim_client c ON s.client_id = c.client_id
    JOIN gold.dim_region r ON s.region_id = r.region_key;
END;
