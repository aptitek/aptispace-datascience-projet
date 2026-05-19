# 🧹 02_wrangling.py — Data Wrangling & Nettoyage

import os
import sys
import pandas as pd
import numpy as np

print("🧹 Wrangling démarré")

# =====================================================
# 🔥 CHEMIN PROJET ROBUSTE
# =====================================================

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
# 4. OUTLIERS SUR VALUE
# =====================================================

if "value" in df.columns:
    df["value"] = df["value"].apply(
        lambda x: np.nan if (x < 0 or x > 100) else x
    )
    print("✔ Outliers traités (value)")

# =====================================================
# 5. IMPUTATION DES VALEURS MANQUANTES
# =====================================================

# zone_type
if "zone_type" in df.columns:
    df["zone_type"] = df["zone_type"].fillna("Unknown")

# coef_multiplicateur
if "coef_multiplicateur" in df.columns:
    df["coef_multiplicateur"] = df["coef_multiplicateur"].fillna(df["coef_multiplicateur"].median())

print("✔ Imputation améliorée terminée")

# =====================================================
# 6. SAUVEGARDE
# =====================================================

os.makedirs(os.path.dirname(processed_path), exist_ok=True)

df.to_csv(processed_path, index=False)

print(f"💾 Données nettoyées sauvegardées : {processed_path}")
print("🚀 Wrangling terminé avec succès !")