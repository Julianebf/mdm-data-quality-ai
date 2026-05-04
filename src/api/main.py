from fastapi import FastAPI
import pandas as pd

from src.ml.anomaly_detection import detect_anomalies
from src.quality.deduplication import find_duplicates

app = FastAPI(
    title="API de Qualidade de Dados MDM",
    description="Plataforma para análise de dados cadastrais com detecção de anomalias e deduplicação",
    version="1.0.0"
)

@app.get("/", tags=["Status"])
def root():
    return {"message": "API MDM rodando 🚀"}


@app.get("/anomalias", tags=["Detecção de Anomalias"])
def get_anomalias():
    df = pd.read_csv("data/processed/master_table.csv")
    df = detect_anomalies(df)

    anomalias = df[df["anomaly"] == -1]

    return {
        "total": len(anomalias),
        "data": anomalias.head(10).to_dict(orient="records")
    }


@app.get("/deduplicacao", tags=["Deduplicação"])
def get_deduplicacao():
    df = pd.read_csv("data/processed/master_table.csv")

    if "name" not in df.columns:
        df["name"] = df["customer_city"] + "_" + df.index.astype(str)

    duplicates = find_duplicates(df)

    return {
        "total": len(duplicates),
        "data": duplicates.head(10).to_dict(orient="records")
    }