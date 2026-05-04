import pandas as pd
from rapidfuzz import fuzz
import unicodedata


def normalize(text):
    if pd.isna(text):
        return ""

    text = str(text).lower()
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode("utf-8")
    return text.strip()


def find_duplicates(df, threshold=85):
    df = df.copy()

    # normalizar nomes
    df["name_norm"] = df["name"].apply(normalize)

    duplicates = []

    for city, group in df.groupby("customer_city"):

        names = group["name_norm"].tolist()
        indices = group.index.tolist()

        for i in range(len(names)):
            for j in range(i + 1, len(names)):

                score = fuzz.ratio(names[i], names[j])

                if score >= threshold:
                    duplicates.append({
                        "name_1": group.loc[indices[i], "name"],
                        "name_2": group.loc[indices[j], "name"],
                        "score": score,
                        "city": city
                    })

    return pd.DataFrame(duplicates)