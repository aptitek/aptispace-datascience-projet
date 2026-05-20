import pandas as pd
import numpy as np


def load_raw_data(path):
    return pd.read_csv(path)


def clean_dates(df, col):
    if col in df.columns:
        df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


def handle_outliers(df, cols, min_val, max_val):
    df = df.copy()
    for c in cols:
        if c in df.columns:
            df[c] = df[c].apply(lambda x: np.nan if x < min_val or x > max_val else x)
    return df


def impute_missing_values(df, cols, method="mean"):
    df = df.copy()

    for c in cols:
        if c not in df.columns:
            continue

        if method == "mean":
            df[c] = df[c].fillna(df[c].mean())

        elif method == "median":
            df[c] = df[c].fillna(df[c].median())

        elif method == "interpolate":
            df[c] = df[c].interpolate()

        elif method == "mode":
            df[c] = df[c].fillna(df[c].mode()[0])

    return df


def feature_engineering(df, date_col):
    df = df.copy()

    if date_col in df.columns:
        df["hour"] = df[date_col].dt.hour
        df["dayofweek"] = df[date_col].dt.dayofweek

    return df