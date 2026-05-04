import pandas as pd
from rapidfuzz import fuzz

df = pd.read_csv("data/processed/master_table.csv")

df["name"] = df["customer_city"].astype(str) + "_" + df.index.astype(str)


df.loc[0, "name"] = "Joao Silva"
df.loc[1, "name"] = "João Silva"

def find_duplicates(df, threshold=85):
    results = []
    names = df["name"].tolist()

    for i in range(len(names)):
        for j in range(i + 1, len(names)):
            score = fuzz.ratio(names[i], names[j])

            if score > threshold:
                results.append((names[i], names[j], score))

    return results

duplicates = find_duplicates(df, threshold=80)

print("Duplicados encontrados:")
for d in duplicates[:10]:
    print(d)