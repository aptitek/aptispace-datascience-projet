

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

sys.path.append(os.path.abspath('..'))

from src import data_clean as dc
from src import utils_viz as uv

uv.set_custom_style(theme='light')

print("📊 Visualisation démarrée")

# Chargement
df = pd.read_csv('../data/processed/cleaned_data_sample.csv')

# Conversion date
df['YrSold'] = pd.to_datetime(df['YrSold'], format='%Y')

# Feature engineering
df_feat = dc.feature_engineering(df, 'YrSold')

# A. Tendances
fig1 = uv.plot_generic_trends(
    df_feat,
    'YrSold',
    'SalePrice',
    group_col='Neighborhood'
)

plt.show()

# B. Corrélations
fig2 = uv.plot_correlation_matrix(
    df_feat,
    ['SalePrice', 'GrLivArea', 'TotalBsmtSF', 'GarageArea']
)

plt.show()

# C. Scatter plot
fig3 = uv.plot_bivariate_scatter(
    df_feat,
    'GrLivArea',
    'SalePrice',
    color_col='Neighborhood'
)

plt.show()

print("✅ Visualisations terminées")