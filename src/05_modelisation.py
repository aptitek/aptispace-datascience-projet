# 🤖 05_modelisation.py — Modélisation ML House Prices
import os
import sys
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

print("🚀 Modélisation démarrée")

# =====================================================
# 1. CHARGEMENT DATA
# =====================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "processed", "cleaned_data_sample.csv")

df = pd.read_csv(data_path)
print(f"✔ Dataset chargé : {df.shape}")

# =====================================================
# 2. SÉLECTION DES FEATURES
# =====================================================
# Features numériques les plus corrélées avec SalePrice (validées par l'EDA)
features = [
    "GrLivArea",            # Surface habitable
    "OverallQual",          # Qualité globale du bien
    "HouseAge",             # Âge de la maison au moment de la vente
    "GarageCars",           # Capacité du garage
    "TotalBsmtSF",          # Surface du sous-sol
    "coef_multiplicateur"   # Coefficient zone (Standard/Premium/Luxury)
]
target = "SalePrice"

X = df[features]
y = df[target]

print(f"✔ Features sélectionnées : {features}")
print(f"✔ Target : {target}")

# =====================================================
# 3. TRAIN / TEST SPLIT
# =====================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,      # 20% pour le test
    random_state=42     # Reproductibilité
)

print(f"✔ Train : {X_train.shape} | Test : {X_test.shape}")

# =====================================================
# 4. ENTRAÎNEMENT RANDOM FOREST
# =====================================================
rf = RandomForestRegressor(
    n_estimators=200,       # 200 arbres dans la forêt
    max_depth=15,           # Profondeur max pour éviter l'overfitting
    random_state=42,
    n_jobs=-1               # Utilise tous les CPU
)

rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

print("✔ Modèle entraîné")

# =====================================================
# 5. ÉVALUATION DU MODÈLE
# =====================================================
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n📊 MÉTRIQUES")
print(f"MAE  : {mae:,.2f} $")
print(f"RMSE : {rmse:,.2f} $")
print(f"R²   : {r2:.4f}")

# =====================================================
# 6. FEATURE IMPORTANCE
# =====================================================
importance = pd.DataFrame({
    "feature": X.columns,
    "importance": rf.feature_importances_
}).sort_values(by="importance", ascending=False)

print("\n🔥 FEATURE IMPORTANCE")
print(importance.to_string(index=False))

print("\n🚀 Modélisation terminée avec succès")