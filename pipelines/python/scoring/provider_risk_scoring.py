from pathlib import Path
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

DATA = Path("data/gold")


def provider_features(claims: pd.DataFrame, detections: pd.DataFrame) -> pd.DataFrame:
    c = claims.groupby("provider_key").agg(
        claim_count=("claim_id", "nunique"),
        paid_amount=("paid_amount", "sum"),
        opioid_claim_rate=("is_opioid", "mean"),
        denied_rate=("claim_status", lambda s: (s == "Denied").mean()),
        high_dollar_rate=("paid_amount", lambda s: (s > s.quantile(.95)).mean()),
    ).reset_index()
    d = detections.groupby("provider_key").agg(
        detection_count=("detection_id", "nunique"),
        avg_detection_score=("risk_score", "mean"),
        suspected_exposure=("suspected_exposure_amount", "sum"),
    ).reset_index()
    return c.merge(d, on="provider_key", how="left").fillna(0)


def score_providers(features: pd.DataFrame) -> pd.DataFrame:
    cols = ["claim_count", "paid_amount", "opioid_claim_rate", "denied_rate", "high_dollar_rate", "detection_count", "avg_detection_score", "suspected_exposure"]
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(features[cols])
    weights = [0.10, 0.15, 0.15, 0.10, 0.15, 0.15, 0.15, 0.05]
    features = features.copy()
    features["provider_risk_score"] = (scaled * weights).sum(axis=1).round(4)
    features["risk_tier"] = pd.cut(features["provider_risk_score"], bins=[-1, .35, .65, 1], labels=["Low", "Medium", "High"])
    return features


def main():
    claims = pd.read_csv(DATA / "fact_claims.csv")
    detections = pd.read_csv(DATA / "fact_fraud_detection.csv")
    scored = score_providers(provider_features(claims, detections))
    scored.to_csv(DATA / "provider_risk_scores.csv", index=False)
    print("Provider risk scoring complete")

if __name__ == "__main__":
    main()
