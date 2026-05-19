# 🧹 02_wrangling.py — Data Wrangling & Nettoyage

import os
import sys
import pandas as pd
import numpy as np

print("🧹 Wrangling démarré")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw_path = os.path.join(BASE_DIR, "data", "processed", "data_merged.csv")
processed_path = os.path.join(BASE_DIR, "data", "processed", "cleaned_data_sample.csv")

print("📂 Dataset source :", raw_path)

if not os.path.exists(raw_path):
    raise FileNotFoundError(f"❌ Fichier introuvable : {raw_path}")

# =====================================================
# 1. CHARGEMENT
# =====================================================

df = pd.read_csv(raw_path)

print(f"✔ Dataset chargé : {df.shape}")

# =====================================================
# 2. AUDIT QUALITÉ
# =====================================================

print("\n📊 INFO DATASET")
print(df.info())

print("\n❌ VALEURS MANQUANTES")
print(df.isnull().sum())

print("\n🔁 DOUBLONS")
print(df.duplicated().sum())

# =====================================================
# 3. NETTOYAGE DES DATES (si colonne existe)
# =====================================================

if "timestamp" in df.columns:
    df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
    print("✔ Dates converties")

# =====================================================
# 4. OUTLIERS SUR TARGET (SalePrice)
# =====================================================

if "SalePrice" in df.columns:
    q1 = df["SalePrice"].quantile(0.01)
    q99 = df["SalePrice"].quantile(0.99)

    df.loc[
        (df["SalePrice"] < q1) | (df["SalePrice"] > q99),
        "SalePrice"
    ] = np.nan

    print("✔ Outliers traités sur SalePrice (1% trimming)")

# =====================================================
# 5. IMPUTATION DES VALEURS MANQUANTES
# =====================================================

# categorical fill
cat_cols = df.select_dtypes(include="object").columns
for col in cat_cols:
    df[col] = df[col].fillna("Unknown")

# numeric fill
num_cols = df.select_dtypes(include=[np.number]).columns
for col in num_cols:
    df[col] = df[col].fillna(df[col].median())

print("✔ Imputation améliorée terminée")

# =====================================================
# 6. FEATURE ENGINEERING SIMPLE (BON BONUS PROJET)
# =====================================================

if "YrSold" in df.columns and "YearBuilt" in df.columns:
    df["HouseAge"] = df["YrSold"] - df["YearBuilt"]

if "SalePrice" in df.columns:
    df["LogSalePrice"] = np.log1p(df["SalePrice"])

print("✔ Feature engineering ajouté")

# =====================================================
# 7. SAUVEGARDE
# =====================================================

os.makedirs(os.path.dirname(processed_path), exist_ok=True)

df.to_csv(processed_path, index=False)

print(f"💾 Données nettoyées sauvegardées : {processed_path}")
print("🚀 Wrangling terminé avec succès !")


