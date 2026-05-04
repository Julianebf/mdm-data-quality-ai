import pandas as pd

def missing_values(df):
    return df.isnull().sum()

def duplicate_rows(df):
    return df.duplicated().sum()

def data_quality_score(df):
    total_cells = df.shape[0] * df.shape[1]
    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    score = 100 - ((missing + duplicates) / total_cells * 100)
    return round(score, 2)