USE HealthcareFWA;
GO

IF OBJECT_ID('bronze.raw_claims', 'U') IS NULL
CREATE TABLE bronze.raw_claims (
    raw_claim_id INT IDENTITY(1,1) PRIMARY KEY,
    source_system VARCHAR(100),
    source_file_name VARCHAR(255),
    load_batch_id UNIQUEIDENTIFIER DEFAULT NEWID(),
    raw_claim_number VARCHAR(100),
    raw_provider_npi VARCHAR(20),
    raw_member_id VARCHAR(100),
    raw_pharmacy_npi VARCHAR(20),
    raw_client_code VARCHAR(50),
    raw_service_date VARCHAR(50),
    raw_paid_amount VARCHAR(50),
    raw_billed_amount VARCHAR(50),
    raw_diagnosis_code VARCHAR(50),
    raw_procedure_code VARCHAR(50),
    raw_ndc_code VARCHAR(50),
    raw_claim_status VARCHAR(50),
    ingestion_timestamp DATETIME2 DEFAULT SYSUTCDATETIME()
);
GO