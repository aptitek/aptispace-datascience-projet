# 🤖 05_modelisation.py — Modélisation ML PRO

import os
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.impute import SimpleImputer
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

print("🚀 Modélisation démarrée")

# =====================================================
# 1. CHEMINS
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "cleaned_data_sample.csv"
)

model_path = os.path.join(
    BASE_DIR,
    "models",
    "random_forest_model.pkl"
)

os.makedirs(os.path.dirname(model_path), exist_ok=True)

# =====================================================
# 2. CHARGEMENT DATA
# =====================================================

df = pd.read_csv(data_path)

print(f"✔ Dataset chargé : {df.shape}")

# =====================================================
# 3. FEATURE ENGINEERING
# =====================================================

if "YrSold" in df.columns and "YearBuilt" in df.columns:
    df["HouseAge"] = df["YrSold"] - df["YearBuilt"]

# =====================================================
# 4. FEATURES / TARGET
# =====================================================

features = [
    "GrLivArea",
    "OverallQual",
    "HouseAge",
    "GarageCars",
    "TotalBsmtSF",
    "coef_multiplicateur"
]

target = "SalePrice"

# Vérification colonnes
missing_cols = [c for c in features if c not in df.columns]

if missing_cols:
    raise Exception(f"Colonnes manquantes : {missing_cols}")

X = df[features]
y = df[target]

print("\n✔ Features utilisées :")
print(features)

# =====================================================
# 5. GESTION DES NaN
# =====================================================

imputer = SimpleImputer(strategy="median")

X = pd.DataFrame(
    imputer.fit_transform(X),
    columns=X.columns
)

print("✔ Valeurs manquantes imputées")

# =====================================================
# 6. SPLIT TRAIN / TEST
# =====================================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print(f"✔ Train : {X_train.shape}")
print(f"✔ Test  : {X_test.shape}")

# =====================================================
# 7. RANDOM FOREST
# =====================================================

rf = RandomForestRegressor(
    n_estimators=300,
    max_depth=20,
    min_samples_split=5,
    random_state=42,
    n_jobs=-1
)

rf.fit(X_train, y_train)

print("✔ Random Forest entraîné")

# =====================================================
# 8. PRÉDICTIONS
# =====================================================

y_pred = rf.predict(X_test)

# =====================================================
# 9. MÉTRIQUES
# =====================================================

mae = mean_absolute_error(y_test, y_pred)

rmse = np.sqrt(mean_squared_error(y_test, y_pred))

r2 = r2_score(y_test, y_pred)

print("\n📊 MÉTRIQUES FINALES")
print(f"MAE  : {mae:,.2f} $")
print(f"RMSE : {rmse:,.2f} $")
print(f"R²   : {r2:.4f}")

# =====================================================
# 10. VALIDATION CROISÉE
# =====================================================

cv_scores = cross_val_score(
    rf,
    X,
    y,
    cv=5,
    scoring="r2"
)

print("\n📈 VALIDATION CROISÉE")
print("Scores R² :", cv_scores)
print("R² moyen  :", cv_scores.mean())

# =====================================================
# 11. FEATURE IMPORTANCE
# =====================================================

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n🔥 IMPORTANCE DES VARIABLES")
print(importance)

# =====================================================
# 12. VISUALISATION IMPORTANCE
# =====================================================

plt.figure(figsize=(10, 6))

plt.barh(
    importance["Feature"],
    importance["Importance"]
)

plt.xlabel("Importance")
plt.ylabel("Variables")
plt.title("Importance des Variables")

plt.tight_layout()

plt.show()

# =====================================================
# 13. SAUVEGARDE MODÈLE
# =====================================================

joblib.dump(rf, model_path)

print(f"\n💾 Modèle sauvegardé : {model_path}")

print("\n🚀 Modélisation terminée avec succès")

# =====================================================
# 7. SAUVEGARDE DU MODÈLE
# =====================================================
import joblib

output_dir = os.path.join(BASE_DIR, "models")
os.makedirs(output_dir, exist_ok=True)
model_path = os.path.join(output_dir, "rf_house_prices.pkl")
joblib.dump(rf, model_path)
print(f"\n💾 Modèle sauvegardé : {model_path}")