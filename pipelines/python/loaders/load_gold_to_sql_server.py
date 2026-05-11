from pathlib import Path
import urllib.parse
import pandas as pd
from sqlalchemy import create_engine, text

SERVER = "localhost"
PORT = "1433"
DATABASE = "HealthcareFWA"
USERNAME = "sa"
PASSWORD = "FwaPlatform2026!"  # <-- replace this
DRIVER = "ODBC Driver 18 for SQL Server"

DATA_DIR = Path("data/gold")

TABLE_LOAD_ORDER = [
    ("dim_client", "dim_client.csv", "client_key"),
    ("dim_region", "dim_region.csv", "region_key"),
    ("dim_provider", "dim_provider.csv", "provider_key"),
    ("dim_member", "dim_member.csv", "member_key"),
    ("dim_pharmacy", "dim_pharmacy.csv", "pharmacy_key"),
    ("dim_fraud_scheme", "dim_fraud_scheme.csv", "scheme_key"),
    ("dim_date", "dim_date.csv", None),
    ("fact_claims", "fact_claims.csv", "claim_key"),
    ("fact_fraud_detection", "fact_fraud_detection.csv", "detection_key"),
    ("fact_investigation_actions", "fact_investigation_actions.csv", "action_key"),
]


def get_engine():
    connection_string = (
        f"DRIVER={{{DRIVER}}};"
        f"SERVER={SERVER},{PORT};"
        f"DATABASE={DATABASE};"
        f"UID={USERNAME};"
        f"PWD={PASSWORD};"
        f"TrustServerCertificate=yes;"
    )
    params = urllib.parse.quote_plus(connection_string)
    return create_engine(
        f"mssql+pyodbc:///?odbc_connect={params}",
        fast_executemany=True,
    )


def get_sql_columns(conn, table_name):
    result = conn.execute(
        text("""
            SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = 'gold'
              AND TABLE_NAME = :table_name
            ORDER BY ORDINAL_POSITION
        """),
        {"table_name": table_name},
    )
    return [row[0] for row in result]


def table_has_identity(conn, table_name):
    result = conn.execute(
        text("""
            SELECT COUNT(*) 
            FROM sys.identity_columns ic
            JOIN sys.tables t 
                ON ic.object_id = t.object_id
            JOIN sys.schemas s 
                ON t.schema_id = s.schema_id
            WHERE s.name = 'gold'
              AND t.name = :table_name
        """),
        {"table_name": table_name},
    )
    return result.scalar() > 0


def truncate_tables(conn):
    print("Clearing existing gold tables...")

    # Facts first, then dimensions because of FK dependencies
    delete_order = [
        "fact_investigation_actions",
        "fact_fraud_detection",
        "fact_claims",
        "dim_pharmacy",
        "dim_member",
        "dim_provider",
        "dim_fraud_scheme",
        "dim_date",
        "dim_region",
        "dim_client",
    ]

    for table_name in delete_order:
        conn.execute(text(f"DELETE FROM gold.{table_name};"))

    print("Existing data cleared.")


def load_table(conn, table_name, file_name, identity_key):
    file_path = DATA_DIR / file_name

    if not file_path.exists():
        print(f"Skipping gold.{table_name}: {file_path} not found")
        return

    print(f"Loading {file_path} into gold.{table_name}...")

    df = pd.read_csv(file_path)

    sql_columns = get_sql_columns(conn, table_name)

    # Keep only columns that actually exist in SQL Server
    df = df[[col for col in df.columns if col in sql_columns]]

    if df.empty:
        print(f"Skipping gold.{table_name}: no matching columns found")
        return

    has_identity = table_has_identity(conn, table_name)
    identity_insert_on = False

    try:
        if has_identity and identity_key and identity_key in df.columns:
            conn.execute(text(f"SET IDENTITY_INSERT gold.{table_name} ON;"))
            identity_insert_on = True

        df.to_sql(
            name=table_name,
            con=conn,
            schema="gold",
            if_exists="append",
            index=False,
            chunksize=500,
            method=None,
        )

        print(f"Loaded {len(df):,} rows into gold.{table_name}")

    finally:
        if identity_insert_on:
            conn.execute(text(f"SET IDENTITY_INSERT gold.{table_name} OFF;"))


def main():
    engine = get_engine()

    with engine.begin() as conn:
        truncate_tables(conn)

        for table_name, file_name, identity_key in TABLE_LOAD_ORDER:
            load_table(conn, table_name, file_name, identity_key)

    print("Gold load complete.")


if __name__ == "__main__":
    main()