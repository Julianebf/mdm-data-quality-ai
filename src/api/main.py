import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.ml.anomaly_detection import detect_anomalies
from src.quality.deduplication import find_duplicates
from src.quality.data_quality import quality_report

app = FastAPI(
    title="MDM Data Quality API — Brazil Cities",
    description="Plataforma de qualidade de dados cadastrais municipais com ML",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def load_master():
    return pd.read_csv("data/processed/master_table.csv")

@app.get("/", tags=["Status"])
def root():
    return {"message": "MDM Brazil Cities API rodando"}

@app.get("/qualidade", tags=["Qualidade"])
def get_qualidade():
    df = load_master()
    return quality_report(df)

@app.get("/anomalias", tags=["Anomalias"])
def get_anomalias(limit: int = 20):
    df = load_master()
    df = detect_anomalies(df)
    anomalias = df[df["anomaly"] == -1].sort_values("anomaly_score")
    return {
        "total": len(anomalias),
        "data": anomalias.head(limit).fillna("").to_dict(orient="records")
    }

@app.get("/anomalias/por-estado", tags=["Anomalias"])
def anomalias_por_estado():
    df = load_master()
    df = detect_anomalies(df)
    anomalias = df[df["anomaly"] == -1]
    por_estado = anomalias.groupby("STATE").size().reset_index(name="total")
    return por_estado.sort_values("total", ascending=False).to_dict(orient="records")

@app.get("/anomalias/estado/{state}", tags=["Anomalias"])
def anomalias_estado_detalhe(state: str):
    df = load_master()
    df = detect_anomalies(df)
    filtrado = df[(df["anomaly"] == -1) & (df["STATE"].str.upper() == state.upper())]
    return {
        "total": len(filtrado),
        "data": filtrado.sort_values("anomaly_score").fillna("").to_dict(orient="records")
    }

@app.get("/deduplicacao", tags=["Deduplicação"])
def get_deduplicacao(state: str = None, threshold: int = 85, limit: int = 20):
    df = load_master()

    if state:
        df = df[df["STATE"].str.upper() == state.upper()]

    duplicates = find_duplicates(df, threshold=threshold)

    return {
        "total": len(duplicates),
        "data": duplicates.head(limit).fillna("").to_dict(orient="records")
    }
@app.get("/cidades", tags=["Cidades"])
def get_cidades(state: str = None, limit: int = 50):
    df = load_master()
    if state:
        df = df[df["STATE"].str.upper() == state.upper()]
    return {
        "total": len(df),
        "data": df.head(limit).fillna("").to_dict(orient="records")
    }

@app.get("/cidades/{city}", tags=["Cidades"])
def get_cidade(city: str):
    df = load_master()
    result = df[df["CITY"].str.lower() == city.lower()]
    if result.empty:
        return {"error": "Cidade não encontrada"}
    return result.fillna("").to_dict(orient="records")[0]
