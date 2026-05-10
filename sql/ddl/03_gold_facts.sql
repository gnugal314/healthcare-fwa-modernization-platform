CREATE TABLE gold.fact_claims (
    claim_key BIGINT IDENTITY(1,1) PRIMARY KEY,
    claim_id UNIQUEIDENTIFIER NOT NULL,
    service_date_key INT NOT NULL,
    paid_date_key INT NOT NULL,
    provider_key INT NOT NULL,
    member_key INT NOT NULL,
    pharmacy_key INT NULL,
    client_key INT NOT NULL,
    region_key INT NOT NULL,
    claim_type VARCHAR(30),
    diagnosis_code VARCHAR(20),
    procedure_code VARCHAR(20),
    ndc_code VARCHAR(20),
    drug_name VARCHAR(100),
    is_opioid BIT NOT NULL DEFAULT 0,
    billed_amount DECIMAL(18,2),
    allowed_amount DECIMAL(18,2),
    paid_amount DECIMAL(18,2),
    denied_amount DECIMAL(18,2),
    claim_status VARCHAR(30),
    ingestion_batch_id UNIQUEIDENTIFIER,
    created_at DATETIME2 DEFAULT SYSUTCDATETIME()
);

CREATE TABLE gold.fact_fraud_detection (
    detection_key BIGINT IDENTITY(1,1) PRIMARY KEY,
    detection_id UNIQUEIDENTIFIER NOT NULL,
    claim_id UNIQUEIDENTIFIER NULL,
    detection_date_key INT NOT NULL,
    provider_key INT NULL,
    member_key INT NULL,
    pharmacy_key INT NULL,
    client_key INT NOT NULL,
    region_key INT NOT NULL,
    scheme_key INT NOT NULL,
    risk_score DECIMAL(9,4),
    suspected_exposure_amount DECIMAL(18,2),
    detection_source VARCHAR(50),
    model_version VARCHAR(50),
    alert_status VARCHAR(50),
    created_at DATETIME2 DEFAULT SYSUTCDATETIME()
);

CREATE TABLE gold.fact_investigation_actions (
    action_key BIGINT IDENTITY(1,1) PRIMARY KEY,
    action_id UNIQUEIDENTIFIER NOT NULL,
    detection_id UNIQUEIDENTIFIER NOT NULL,
    action_date_key INT NOT NULL,
    investigator_team VARCHAR(100),
    action_type VARCHAR(100),
    action_status VARCHAR(50),
    stopped_payment_amount DECIMAL(18,2),
    recovered_amount DECIMAL(18,2),
    notes VARCHAR(1000),
    created_at DATETIME2 DEFAULT SYSUTCDATETIME()
);
