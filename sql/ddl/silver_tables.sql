USE HealthcareFWA;
GO

IF OBJECT_ID('silver.claims_clean', 'U') IS NULL
CREATE TABLE silver.claims_clean (
    claim_id BIGINT IDENTITY(1,1) PRIMARY KEY,
    claim_number VARCHAR(100) NOT NULL,
    provider_npi VARCHAR(20),
    member_id VARCHAR(100),
    pharmacy_npi VARCHAR(20),
    client_code VARCHAR(50),
    service_date DATE,
    paid_amount DECIMAL(18,2),
    billed_amount DECIMAL(18,2),
    diagnosis_code VARCHAR(50),
    procedure_code VARCHAR(50),
    ndc_code VARCHAR(50),
    claim_status VARCHAR(50),
    data_quality_status VARCHAR(50),
    load_batch_id UNIQUEIDENTIFIER,
    created_timestamp DATETIME2 DEFAULT SYSUTCDATETIME()
);
GO