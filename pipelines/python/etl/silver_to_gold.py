from pathlib import Path
import pandas as pd

SILVER = Path("data/silver")
GOLD = Path("data/gold")


def calculate_claim_kpis(claims: pd.DataFrame) -> pd.DataFrame:
    claims = claims.copy()
    claims["net_exposure_amount"] = claims["paid_amount"] + claims["denied_amount"]
    claims["is_high_dollar_outlier"] = claims["paid_amount"] > claims["paid_amount"].quantile(.97)
    return claims


def main():
    GOLD.mkdir(parents=True, exist_ok=True)
    claims = pd.read_csv(SILVER / "fact_claims.csv")
    calculate_claim_kpis(claims).to_csv(GOLD / "fact_claims.csv", index=False)
    print("Silver to Gold complete")

if __name__ == "__main__":
    main()
