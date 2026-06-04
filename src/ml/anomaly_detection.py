import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

FEATURES = [
    "ESTIMATED_POP", "AREA", "IDHM", "GDP_CAPITA",
    "GVA_TOTAL", "HOTELS", "Cars", "COMP_TOT"
]

def detect_anomalies(df: pd.DataFrame, contamination: float = 0.05) -> pd.DataFrame:
    df = df.copy()

    data = df[FEATURES].copy()
    data = data.fillna(data.median())

    scaler = StandardScaler()
    scaled = scaler.fit_transform(data)

    model = IsolationForest(contamination=contamination, random_state=42)
    df["anomaly"] = model.fit_predict(scaled)
    df["anomaly_score"] = model.decision_function(scaled).round(4)

    return df