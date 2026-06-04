import pandas as pd
import unicodedata
from rapidfuzz import fuzz

def normalize(text):
    if pd.isna(text):
        return ""
    text = str(text).lower().strip()
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    return text

def find_duplicates(df: pd.DataFrame, threshold: int = 85) -> pd.DataFrame:
    df = df.copy()
    df["CITY_NORM"] = df["CITY"].apply(normalize)

    duplicates = []

    for state, group in df.groupby("STATE"):
        names = group["CITY_NORM"].tolist()
        indices = group.index.tolist()

        for i in range(len(names)):
            for j in range(i + 1, len(names)):
                score = fuzz.ratio(names[i], names[j])
                if score >= threshold:
                    duplicates.append({
                        "city_1": group.loc[indices[i], "CITY"],
                        "city_2": group.loc[indices[j], "CITY"],
                        "state": state,
                        "score": score
                    })

    return pd.DataFrame(duplicates)