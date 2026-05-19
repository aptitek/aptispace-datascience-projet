
import os
import pandas as pd
import numpy as np

print("📥 Acquisition des données démarrée")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

raw_data_path = os.path.join(BASE_DIR, "data", "raw", "train.csv")
processed_path = os.path.join(BASE_DIR, "data", "processed", "raw_merged.csv")

print("📂 Chemin détecté :", raw_data_path)

if not os.path.exists(raw_data_path):
    raise FileNotFoundError(f"❌ Fichier introuvable : {raw_data_path}")

# =====================================================
# 1. CHARGEMENT DATASET PRINCIPAL
# =====================================================

df_main = pd.read_csv(raw_data_path)

print("✔ Dataset chargé :", df_main.shape)
print(df_main.head())

# =====================================================
# 2. CRÉATION DONNÉES SECONDAIRES (FEATURE EXTERNE)
# =====================================================

# 👉 mapping propre basé sur Neighborhood
zone_map = {
    'CollgCr': 'Standard',
    'Veenker': 'Premium',
    'Crawfor': 'Premium',
    'NoRidge': 'Luxury',
    'Mitchel': 'Standard'
}

categories_info = df_main[['Neighborhood']].drop_duplicates().copy()

# 👉 IMPORTANT : fallback = mode (pas NaN)
categories_info['zone_type'] = categories_info['Neighborhood'].apply(
    lambda x: zone_map.get(x, 'Standard')
)

coef_map = {
    'Standard': 1.0,
    'Premium': 1.2,
    'Luxury': 1.5
}

categories_info['coef_multiplicateur'] = categories_info['zone_type'].map(coef_map)

# 👉 sécurité finale
categories_info['coef_multiplicateur'] = categories_info['coef_multiplicateur'].fillna(1.0)
print("✔ Données secondaires créées")
print(categories_info.head())

# =====================================================
# 3. FUSION DES DONNÉES
# =====================================================

df_merged = df_main.merge(categories_info, on='Neighborhood', how='left')

print("✔ Fusion terminée :", df_merged.shape)
print(df_merged.head())

# =====================================================
# 4. SAUVEGARDE
# =====================================================

os.makedirs(os.path.dirname(processed_path), exist_ok=True)

df_merged.to_csv(processed_path, index=False)

print(f"💾 Données sauvegardées : {processed_path}")
print("🚀 Acquisition terminée avec succès !")