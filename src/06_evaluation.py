

import os
import sys
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

sys.path.append(os.path.abspath('..'))

from src import data_clean as dc

print("📈 Évaluation démarrée")

# Chargement
df = pd.read_csv('../data/processed/cleaned_data_sample.csv')

# Conversion
df['YrSold'] = pd.to_datetime(df['YrSold'], format='%Y')

# Feature engineering
df_feat = dc.feature_engineering(df, 'YrSold')

features = [
    'GrLivArea',
    'TotalBsmtSF',
    'GarageArea',
    'OverallQual'
]

target = 'SalePrice'

# Split
X_train = df_feat[features].iloc[:-200]
y_train = df_feat[target].iloc[:-200]

X_test = df_feat[features].iloc[-200:]
y_test = df_feat[target].iloc[-200:]

# Modèle
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

r2 = r2_score(y_test, y_pred)

print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.2f}")

print("✅ Évaluation terminée")