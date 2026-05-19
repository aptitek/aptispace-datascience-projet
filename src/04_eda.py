

import os
import sys
import pandas as pd

sys.path.append(os.path.abspath('..'))

from src import data_clean as dc

print("🔎 EDA démarrée")

# Chargement
df = pd.read_csv('../data/processed/cleaned_data_sample.csv')

# Conversion
df['YrSold'] = pd.to_datetime(df['YrSold'], format='%Y')

# Statistiques
print(df.describe())

# Groupby
group_stats = df.groupby('Neighborhood')['SalePrice'].mean()

print("\nPrix moyen par quartier :")
print(group_stats)

# Feature engineering
df_feat = dc.feature_engineering(df, 'YrSold')

print(df_feat.head())

# Corrélations
correlations = df_feat[
    ['SalePrice', 'GrLivArea', 'TotalBsmtSF', 'GarageArea']
].corr()

print("\nMatrice de corrélation :")
print(correlations)

print("✅ EDA terminée")