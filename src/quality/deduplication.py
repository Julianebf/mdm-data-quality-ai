from rapidfuzz import fuzz
import pandas as pd

def find_similar_names(df, threshold=85):
    results = []

    names = df["customer_id"].astype(str).tolist()

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            score = fuzz.ratio(names[i], names[j])

            if score > threshold:
                results.append((names[i], names[j], score))

    return results