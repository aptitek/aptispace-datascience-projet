

import os
import sys
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

sys.path.append(os.path.abspath('..'))

from src import data_clean as dc

print("🧠 Modélisation démarrée")

# Chargement
df = pd.read_csv('../data/processed/cleaned_data_sample.csv')

# Conversion
df['YrSold'] = pd.to_datetime(df['YrSold'], format='%Y')

# Feature engineering
df_feat = dc.feature_engineering(df, 'YrSold')

# Features / target
features = [
    'GrLivArea',
    'TotalBsmtSF',
    'GarageArea',
    'OverallQual'
]

target = 'SalePrice'

# Train / test split
X_train = df_feat[features].iloc[:-200]
y_train = df_feat[target].iloc[:-200]

X_test = df_feat[features].iloc[-200:]
y_test = df_feat[target].iloc[-200:]

# Modèle
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)

# Prédictions
y_pred = rf_model.predict(X_test)

# Score
mae = mean_absolute_error(y_test, y_pred)

print(f"MAE : {mae:.2f}")

print("✅ Modélisation terminée")