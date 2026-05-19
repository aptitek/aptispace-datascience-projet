
import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("📊 Visualisation démarrée")


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "processed", "cleaned_data_sample.csv")

print("📂 Chargement :", data_path)

if not os.path.exists(data_path):
    raise FileNotFoundError(f"❌ Fichier introuvable : {data_path}")

# =====================================================
# 1. CHARGEMENT DATASET
# =====================================================

df = pd.read_csv(data_path)

# sécurité types
df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce') if 'timestamp' in df.columns else None

print("✔ Dataset chargé :", df.shape)

# =====================================================
# 2. FEATURE ENGINEERING (si pas déjà fait)
# =====================================================

if 'YearBuilt' in df.columns and 'YrSold' in df.columns:
    df['HouseAge'] = df['YrSold'] - df['YearBuilt']

# log price (très important pour analyse)
df['LogSalePrice'] = np.log1p(df['SalePrice'])

print("✔ Features créées")

# =====================================================
# STYLE GRAPHIQUE PRO
# =====================================================

sns.set_theme(style="whitegrid")

# =====================================================
# 3. A — EVOLUTION DES PRIX PAR SURFACE
# =====================================================

plt.figure(figsize=(10,6))

sns.scatterplot(
    data=df,
    x='GrLivArea',
    y='SalePrice',
    alpha=0.5
)

plt.title("Relation entre Surface habitable et Prix")
plt.xlabel("Surface habitable (GrLivArea)")
plt.ylabel("Prix de vente")
plt.show()

# 👉 INSIGHT
print("💡 INSIGHT: Les grandes surfaces ont globalement des prix plus élevés mais avec forte dispersion.")

# =====================================================
# 4. B — DISTRIBUTION DES PRIX
# =====================================================

plt.figure(figsize=(10,6))

sns.histplot(df['SalePrice'], kde=True, bins=40)

plt.title("Distribution des prix de vente")
plt.xlabel("SalePrice")
plt.ylabel("Fréquence")
plt.show()

print("💡 INSIGHT: Distribution asymétrique → transformation log recommandée.")

# =====================================================
# 5. C — PRIX PAR QUALITÉ GLOBALE
# =====================================================

if 'OverallQual' in df.columns:

    plt.figure(figsize=(10,6))

    sns.boxplot(
        data=df,
        x='OverallQual',
        y='SalePrice'
    )

    plt.title("Prix selon la qualité générale du bien")
    plt.show()

    print("💡 INSIGHT: La qualité est un facteur déterminant du prix.")

# =====================================================
# 6. D — CORRÉLATION HEATMAP
# =====================================================

plt.figure(figsize=(10,8))

num_cols = df.select_dtypes(include=[np.number])

corr = num_cols.corr()

sns.heatmap(corr, cmap="coolwarm", linewidths=0.5)

plt.title("Matrice de corrélation")
plt.show()

print("💡 INSIGHT: SalePrice fortement corrélé avec GrLivArea et OverallQual.")

# =====================================================
# 7. E — HOUSE AGE vs PRICE
# =====================================================

if 'HouseAge' in df.columns:

    plt.figure(figsize=(10,6))

    sns.scatterplot(
        data=df,
        x='HouseAge',
        y='SalePrice',
        alpha=0.5
    )

    plt.title("Impact de l'âge du bien sur le prix")
    plt.show()

    print("💡 INSIGHT: Les maisons récentes sont généralement plus chères.")


print("🚀 Visualisation terminée avec succès")