CREATE TABLE gold.dim_provider (
    provider_key INT IDENTITY(1,1) PRIMARY KEY,
    provider_id UNIQUEIDENTIFIER NOT NULL,
    npi VARCHAR(10) NOT NULL,
    provider_name VARCHAR(200) NOT NULL,
    specialty VARCHAR(100),
    provider_type VARCHAR(50),
    network_status VARCHAR(50),
    region_key INT,
    effective_start_date DATE NOT NULL,
    effective_end_date DATE NULL,
    is_current BIT NOT NULL DEFAULT 1
);

CREATE TABLE gold.dim_member (
    member_key INT IDENTITY(1,1) PRIMARY KEY,
    member_id UNIQUEIDENTIFIER NOT NULL,
    masked_member_id VARCHAR(64) NOT NULL,
    birth_year INT,
    gender VARCHAR(20),
    client_key INT,
    region_key INT,
    effective_start_date DATE NOT NULL,
    effective_end_date DATE NULL,
    is_current BIT NOT NULL DEFAULT 1
);

CREATE TABLE gold.dim_pharmacy (
    pharmacy_key INT IDENTITY(1,1) PRIMARY KEY,
    pharmacy_id UNIQUEIDENTIFIER NOT NULL,
    ncpdp_id VARCHAR(7) NOT NULL,
    pharmacy_name VARCHAR(200),
    chain_name VARCHAR(100),
    region_key INT,
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6),
    is_current BIT NOT NULL DEFAULT 1
);

CREATE TABLE gold.dim_client (
    client_key INT IDENTITY(1,1) PRIMARY KEY,
    client_id UNIQUEIDENTIFIER NOT NULL,
    client_name VARCHAR(200),
    client_type VARCHAR(50),
    market_segment VARCHAR(50)
);

CREATE TABLE gold.dim_region (
    region_key INT IDENTITY(1,1) PRIMARY KEY,
    state_code CHAR(2),
    county VARCHAR(100),
    market VARCHAR(100),
    latitude DECIMAL(9,6),
    longitude DECIMAL(9,6)
);

CREATE TABLE gold.dim_fraud_scheme (
    scheme_key INT IDENTITY(1,1) PRIMARY KEY,
    scheme_code VARCHAR(50),
    scheme_name VARCHAR(200),
    severity_level VARCHAR(20),
    description VARCHAR(1000)
);

CREATE TABLE gold.dim_date (
    date_key INT PRIMARY KEY,
    full_date DATE NOT NULL,
    calendar_year INT,
    calendar_quarter INT,
    month_number INT,
    month_name VARCHAR(20),
    week_of_year INT
);
