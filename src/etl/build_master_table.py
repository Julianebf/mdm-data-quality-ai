import pandas as pd

def load_data():
    df = pd.read_csv(
        "data/raw/BRAZIL_CITIES_REV2022.CSV",
        sep=",",
        encoding="utf-8",
        quotechar='"'
    )
    df.columns = df.columns.str.strip()
    return df

def build_master():
    df = load_data()

    cols = [
        "CITY", "STATE", "CAPITAL", "ESTIMATED_POP", "AREA",
        "IDHM", "IDHM_Renda", "IDHM_Longevidade", "IDHM_Educacao",
        "GDP_CAPITA", "GDP", "GVA_AGROPEC", "GVA_INDUSTRY", "GVA_SERVICES",
        "GVA_PUBLIC", "GVA_TOTAL", "RURAL_URBAN", "LONG", "LAT", "ALT",
        "HOTELS", "BEDS", "Cars", "Motorcycles", "POST_OFFICES",
        "FIXED_PHONES", "PAY_TV", "COMP_TOT"
    ]
    df = df[cols].copy()

    df["CITY"] = df["CITY"].str.strip().str.title()
    df["STATE"] = df["STATE"].str.strip().str.upper()

    num_cols = [c for c in cols if c not in ["CITY", "STATE", "CAPITAL", "RURAL_URBAN"]]
    for c in num_cols:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    df.to_csv("data/processed/master_table.csv", index=False)
    print(f"Master table salva. Shape: {df.shape}")
    return df

if __name__ == "__main__":
    build_master()