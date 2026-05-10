import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler


def train_anomaly_model(provider_features: pd.DataFrame):
    feature_cols = ["claim_count", "paid_amount", "opioid_claim_rate", "denied_rate", "high_dollar_rate"]
    x = StandardScaler().fit_transform(provider_features[feature_cols])
    model = IsolationForest(n_estimators=200, contamination=0.05, random_state=314)
    provider_features = provider_features.copy()
    provider_features["anomaly_flag"] = model.fit_predict(x)
    provider_features["anomaly_score"] = model.decision_function(x)
    return provider_features, model
