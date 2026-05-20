# 📊 06_evaluation.py — Évaluation du modèle ML

import os
import joblib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

print("📊 Évaluation du modèle démarrée")

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

evaluation_path = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "evaluation_predictions.csv"
)

# =====================================================
# 2. CHARGEMENT DATASET
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

X = df[features]
y = df[target]

# =====================================================
# 5. IMPUTATION SIMPLE
# =====================================================

X = X.fillna(X.median(numeric_only=True))

# =====================================================
# 6. CHARGEMENT MODÈLE
# =====================================================

if not os.path.exists(model_path):
    raise FileNotFoundError(
        f"❌ Modèle introuvable : {model_path}"
    )

model = joblib.load(model_path)

print("✔ Modèle chargé")

# =====================================================
# 7. PRÉDICTIONS
# =====================================================

y_pred = model.predict(X)

# =====================================================
# 8. MÉTRIQUES
# =====================================================

mae = mean_absolute_error(y, y_pred)

rmse = np.sqrt(mean_squared_error(y, y_pred))

r2 = r2_score(y, y_pred)

print("\n📈 MÉTRIQUES GLOBALES")

print(f"MAE  : {mae:,.2f} $")
print(f"RMSE : {rmse:,.2f} $")
print(f"R²   : {r2:.4f}")

# =====================================================
# 9. ERREURS
# =====================================================

errors = y - y_pred

print("\n📉 ANALYSE DES ERREURS")

print(f"Erreur moyenne : {errors.mean():,.2f}")
print(f"Erreur max     : {errors.max():,.2f}")
print(f"Erreur min     : {errors.min():,.2f}")

# =====================================================
# 10. VISUALISATION 1
# Réel vs Prédiction
# =====================================================

plt.figure(figsize=(8, 6))

plt.scatter(y, y_pred, alpha=0.6)

plt.xlabel("Prix Réel")
plt.ylabel("Prix Prédit")

plt.title("Prédictions vs Valeurs Réelles")

# ligne parfaite
min_val = min(y.min(), y_pred.min())
max_val = max(y.max(), y_pred.max())

plt.plot(
    [min_val, max_val],
    [min_val, max_val]
)

plt.tight_layout()
plt.show()

# =====================================================
# 11. VISUALISATION 2
# Histogramme des erreurs
# =====================================================

plt.figure(figsize=(8, 5))

plt.hist(errors, bins=30)

plt.xlabel("Erreur")
plt.ylabel("Fréquence")

plt.title("Distribution des erreurs")

plt.tight_layout()
plt.show()

# =====================================================
# 12. VISUALISATION 3
# Importance variables
# =====================================================

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=True
)

plt.figure(figsize=(8, 5))

plt.barh(
    importance["Feature"],
    importance["Importance"]
)

plt.xlabel("Importance")
plt.title("Importance des Variables")

plt.tight_layout()
plt.show()

# =====================================================
# 13. SAUVEGARDE DES PRÉDICTIONS
# =====================================================

results = pd.DataFrame({
    "Valeur_Reelle": y,
    "Valeur_Predite": y_pred,
    "Erreur": errors
})

results.to_csv(evaluation_path, index=False)

print(f"\n💾 Résultats sauvegardés : {evaluation_path}")

# =====================================================
# 14. INSIGHTS AUTOMATIQUES
# =====================================================

print("\n💡 INSIGHTS")

if r2 > 0.7:
    print("- Le modèle possède une bonne capacité prédictive.")

if mae < 25000:
    print("- L'erreur moyenne reste raisonnable pour des prix immobiliers.")

top_feature = importance.sort_values(
    by="Importance",
    ascending=False
).iloc[0]["Feature"]

print(f"- Variable la plus importante : {top_feature}")

print("\n🚀 Évaluation terminée avec succès")