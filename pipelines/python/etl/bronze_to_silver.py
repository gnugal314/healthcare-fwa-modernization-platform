from pathlib import Path
import pandas as pd

BRONZE = Path("data/bronze")
SILVER = Path("data/silver")


def standardize_claims(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["claim_status"] = df["claim_status"].str.strip().str.title()
    df["paid_amount"] = df["paid_amount"].fillna(0).clip(lower=0)
    df["denied_amount"] = df["denied_amount"].fillna(0).clip(lower=0)
    df = df.drop_duplicates(subset=["claim_id"], keep="first")
    return df


def main():
    SILVER.mkdir(parents=True, exist_ok=True)
    claims = pd.read_csv(BRONZE / "fact_claims.csv")
    standardize_claims(claims).to_csv(SILVER / "fact_claims.csv", index=False)
    print("Bronze to Silver complete")

if __name__ == "__main__":
    main()
