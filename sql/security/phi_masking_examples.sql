-- Example SQL Server dynamic data masking patterns for PHI fields.
-- Review with privacy/security teams before use in production.

ALTER TABLE gold.dim_member
ALTER COLUMN masked_member_id ADD MASKED WITH (FUNCTION = 'partial(2,"XXXXXX",2)');

CREATE ROLE fwa_analytics_reader;
CREATE ROLE fwa_phi_privileged_reader;

GRANT SELECT ON SCHEMA::semantic TO fwa_analytics_reader;
GRANT SELECT ON SCHEMA::gold TO fwa_phi_privileged_reader;

-- Example row-level security predicate table.
CREATE TABLE security.user_client_access (
    user_name SYSNAME NOT NULL,
    client_key INT NOT NULL
);
GO

CREATE OR ALTER FUNCTION security.fn_client_access(@client_key INT)
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN SELECT 1 AS access_result
WHERE EXISTS (
    SELECT 1 FROM security.user_client_access a
    WHERE a.client_key = @client_key
      AND a.user_name = USER_NAME()
);
GO

CREATE SECURITY POLICY security.client_rls_policy
ADD FILTER PREDICATE security.fn_client_access(client_key) ON gold.fact_claims
WITH (STATE = ON);
