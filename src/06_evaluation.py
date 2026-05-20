import os, sys
sys.path.append('/home/aptitek/Documents/Aptispace/datascience/lab/projet')

# Installation automatique des dépendances requises dans le noyau Jupyter actuel
# %pip install -r ../requirements.txt


import os
import sys
import pandas as pd
import numpy as np

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

sys.path.append(os.path.abspath('..'))
from src import data_clean as dc

print("Librairies prêtes pour l'évaluation des modèles !")


# Chargement des données et ré-entraînement rapide pour évaluation
df = pd.read_csv('../data/processed/cleaned_data_sample.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df_feat = dc.feature_engineering(df, 'timestamp')

features = ['hour', 'dayofweek']
target = 'value'

X_train = df_feat[features].iloc[:-4]
y_train = df_feat[target].iloc[:-4]
X_test = df_feat[features].iloc[-4:]
y_test = df_feat[target].iloc[-4:]

# Entraînement
from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=10, random_state=42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# TODO: Calculez MAE, RMSE et R² entre y_test et y_pred
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print(f"Test MAE  : {mae:.3f}")
print(f"Test RMSE : {rmse:.3f}")
print(f"Test R²   : {r2:.3f}")


# TODO: Proposer un script de K-Fold temporel (TimeSeriesSplit) ou de validation croisée classique
print("Protocole de validation documenté avec succès !")

