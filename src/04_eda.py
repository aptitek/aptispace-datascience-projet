
import os
import sys
import pandas as pd
import numpy as np

print("🔎 EDA démarrée")



BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "processed", "cleaned_data_sample.csv")

print("📂 Chargement :", data_path)

if not os.path.exists(data_path):
    raise FileNotFoundError(f"❌ Fichier introuvable : {data_path}")

# =====================================================
# 1. CHARGEMENT
# =====================================================

df = pd.read_csv(data_path)

print("✔ Dataset chargé :", df.shape)

# =====================================================
# 2. FEATURE ENGINEERING MINIMUM
# =====================================================

if 'YearBuilt' in df.columns and 'YrSold' in df.columns:
    df['HouseAge'] = df['YrSold'] - df['YearBuilt']

df['LogSalePrice'] = np.log1p(df['SalePrice'])

# =====================================================
# 3. STATISTIQUES DESCRIPTIVES
# =====================================================

print("\n📊 STATISTIQUES DESCRIPTIVES (numériques)")
desc = df.describe().T
print(desc)

# Top insights automatiques
print("\n💡 INSIGHT AUTOMATIQUE :")
print(f"- Prix moyen : {df['SalePrice'].mean():,.0f}")
print(f"- Prix médian : {df['SalePrice'].median():,.0f}")
print(f"- Écart-type prix : {df['SalePrice'].std():,.0f}")

# =====================================================
# 4. ANALYSE DES VALEURS MANQUANTES
# =====================================================

print("\n❌ VALEURS MANQUANTES (TOP 10)")
missing = df.isnull().sum().sort_values(ascending=False).head(10)
print(missing)

# =====================================================
# 5. ANALYSE DES VARIABLES CATÉGORIELLES
# =====================================================

cat_cols = df.select_dtypes(include=["object", "string"]).columns

print("\n📦 VARIABLES CATÉGORIELLES (aperçu)")
for col in cat_cols[:5]:
    print(f"\n{col}")
    print(df[col].value_counts().head(5))

# =====================================================
# 6. CORRÉLATIONS IMPORTANTES
# =====================================================

num_df = df.select_dtypes(include=[np.number])

corr = num_df.corr()

print("\n📈 CORRÉLATIONS AVEC SALEPRICE")
print(corr['SalePrice'].sort_values(ascending=False).head(10))

# =====================================================
# 7. INSIGHTS AUTOMATIQUES
# =====================================================

print("\n💡 INSIGHTS CLÉS")

if 'GrLivArea' in df.columns:
    corr_area = df['SalePrice'].corr(df['GrLivArea'])
    print(f"- Corrélation Surface/Prix : {corr_area:.2f}")

if 'OverallQual' in df.columns:
    corr_qual = df['SalePrice'].corr(df['OverallQual'])
    print(f"- Corrélation Qualité/Prix : {corr_qual:.2f}")

if 'HouseAge' in df.columns:
    corr_age = df['SalePrice'].corr(df['HouseAge'])
    print(f"- Corrélation Âge/Prix : {corr_age:.2f}")

# =====================================================
# 8. OUTLIERS RAPIDES
# =====================================================

q1 = df['SalePrice'].quantile(0.01)
q99 = df['SalePrice'].quantile(0.99)

outliers = df[(df['SalePrice'] < q1) | (df['SalePrice'] > q99)]

print("\n🚨 OUTLIERS")
print(f"- Nombre d'outliers détectés : {len(outliers)}")

# =====================================================
# 9. EXPORT OPTIONNEL (TABLEAU POUR RAPPORT)
# =====================================================

output_path = os.path.join(BASE_DIR, "data", "processed", "eda_summary.csv")

desc.to_csv(output_path)

print(f"\n💾 Résumé EDA sauvegardé : {output_path}")

# =====================================================
# FIN
# =====================================================

print("\n🚀 EDA terminé avec succès")