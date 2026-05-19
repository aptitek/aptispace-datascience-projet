import os
import sys
import pandas as pd
import numpy as np

print("📥 Acquisition des données démarrée")

# =====================================================
# CHEMIN ABSOLU AUTOMATIQUE (FIX IMPORTANT)
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

main_data_path = os.path.join(BASE_DIR, "data", "raw", "train.csv")

print("📂 Chemin détecté :", main_data_path)

if not os.path.exists(main_data_path):
    raise FileNotFoundError(f"❌ Fichier introuvable : {main_data_path}")

# =====================================================
# CHARGEMENT DATASET
# =====================================================

df_main = pd.read_csv(main_data_path)

print(f"✔ Dataset chargé : {df_main.shape}")
print(df_main.head())
# Vérification sécurité
if not os.path.exists(main_data_path):
    raise FileNotFoundError(f"❌ Fichier introuvable : {main_data_path}")

df_main = pd.read_csv(main_data_path)

print(f"✔ Dataset chargé avec succès : {df_main.shape}")
print(df_main.head())

# =========================================================
# 3. DONNÉES SECONDAIRES (SIMULATION MULTI-SOURCES)
# =========================================================

categories_info = pd.DataFrame({
    'Neighborhood': ['CollgCr', 'Veenker', 'Crawfor', 'NoRidge', 'Mitchel'],
    'zone_type': ['Standard', 'Premium', 'Premium', 'Luxury', 'Standard'],
    'coef_multiplicateur': [1.0, 1.2, 1.3, 1.5, 1.1]
})

print("\n✔ Données secondaires créées")
print(categories_info.head())

# =========================================================
# 4. FUSION DES SOURCES
# =========================================================

# ⚠️ merge sécurisé (évite crash si colonne absente)
if 'Neighborhood' in df_main.columns:
    df_merged = pd.merge(df_main, categories_info, on='Neighborhood', how='left')
else:
    print("⚠️ Colonne 'Neighborhood' absente → fusion ignorée")
    df_merged = df_main.copy()

print(f"\n✔ Fusion terminée : {df_merged.shape}")
print(df_merged.head())

# =========================================================
# 5. SAUVEGARDE (BRUT FUSIONNÉ)
# =========================================================

output_path = '../data/processed/raw_merged.csv'
os.makedirs('../data/processed', exist_ok=True)

df_merged.to_csv(output_path, index=False)

print(f"\n💾 Données sauvegardées : {output_path}")
print("🚀 Acquisition terminée avec succès !")