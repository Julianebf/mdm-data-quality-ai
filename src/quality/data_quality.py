import pandas as pd

def missing_values(df: pd.DataFrame) -> dict:
    missing = df.isnull().sum()
    return missing[missing > 0].to_dict()

def duplicate_rows(df: pd.DataFrame) -> int:
    return int(df.duplicated().sum())

def data_quality_score(df: pd.DataFrame) -> float:
    total_cells = df.shape[0] * df.shape[1]
    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()
    score = 100 - ((missing + duplicates) / total_cells * 100)
    return round(score, 2)

def quality_report(df: pd.DataFrame) -> dict:
    # Carrega o raw para medir qualidade real
    try:
        raw = pd.read_csv(
            "data/raw/BRAZIL_CITIES_REV2022.CSV",
            sep=",", encoding="utf-8", quotechar='"'
        )
        raw.columns = raw.columns.str.strip()
    except Exception:
        raw = df  # fallback pro processado

    return {
        "total_records": len(df),
        "total_columns": len(df.columns),
        "missing_values": missing_values(raw),
        "duplicate_rows": duplicate_rows(raw),
        "quality_score": data_quality_score(raw)
    }