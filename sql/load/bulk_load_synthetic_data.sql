-- Example BULK INSERT patterns. Update file paths for your SQL Server host.
BULK INSERT gold.dim_client
FROM 'C:\fwa\data\synthetic\dim_client.csv'
WITH (FORMAT='CSV', FIRSTROW=2, FIELDTERMINATOR=',', ROWTERMINATOR='0x0a');

BULK INSERT gold.dim_region
FROM 'C:\fwa\data\synthetic\dim_region.csv'
WITH (FORMAT='CSV', FIRSTROW=2, FIELDTERMINATOR=',', ROWTERMINATOR='0x0a');

BULK INSERT gold.fact_claims
FROM 'C:\fwa\data\gold\fact_claims.csv'
WITH (FORMAT='CSV', FIRSTROW=2, FIELDTERMINATOR=',', ROWTERMINATOR='0x0a');
