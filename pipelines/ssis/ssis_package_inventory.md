# SSIS Package Inventory

| Package | Purpose | Source | Target |
|---|---|---|---|
| `ExtractClaims.dtsx` | Extract claims from SQL Server source | SQL Server | Bronze claims landing |
| `ExtractProviders.dtsx` | Extract provider reference data | SQL Server | Bronze provider landing |
| `LoadWarehouse.dtsx` | Execute Gold warehouse stored procedures | Silver tables | Gold dimensional model |

Store actual `.dtsx` files in this folder for enterprise deployment.
