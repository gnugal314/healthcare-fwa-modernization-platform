import hashlib
import pandas as pd


def mask_identifier(value: str, salt: str) -> str:
    return hashlib.sha256(f"{salt}:{value}".encode("utf-8")).hexdigest()[:16]


def mask_member_dataframe(df: pd.DataFrame, salt: str) -> pd.DataFrame:
    df = df.copy()
    df["masked_member_id"] = df["member_id"].astype(str).map(lambda x: "MBR-" + mask_identifier(x, salt))
    return df.drop(columns=[c for c in ["member_name", "ssn", "address"] if c in df.columns])
