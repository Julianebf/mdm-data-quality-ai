import pandas as pd
from sklearn.ensemble import IsolationForest


def detect_anomalies(df):
    df_num = df.select_dtypes(include="number").fillna(0)

    model = IsolationForest(contamination=0.01, random_state=42)
    df["anomaly"] = model.fit_predict(df_num)

    return df


if __name__ == "__main__":
    df = pd.read_csv("data/processed/master_table.csv")

    df = detect_anomalies(df)

    print(df["anomaly"].value_counts())

    # salvar resultado
    df.to_csv("data/processed/master_with_anomalies.csv", index=False)

    # ver exemplos de anomalias
    print("\nExemplos de anomalias:")
    print(df[df["anomaly"] == -1].head())