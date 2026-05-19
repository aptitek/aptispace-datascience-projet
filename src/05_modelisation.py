
import os
import sys
import pandas as pd
import numpy as np


from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

sys.path.append(os.path.abspath('..'))
from src import data_clean as dc

print("🚀 Modélisation démarrée")

# =====================================================
# 1. CHARGEMENT DATA
# =====================================================

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "processed", "cleaned_data_sample.csv")

df = pd.read_csv(data_path)
print("✔ Dataset chargé :", df.shape)

# =====================================================
# 2. FEATURE ENGINEERING
# =====================================================

df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
df_feat = dc.feature_engineering(df, 'timestamp')

# fallback si dataset house prices (pas timestamp réel)
if 'hour' not in df_feat.columns:
    df_feat['hour'] = 12
if 'dayofweek' not in df_feat.columns:
    df_feat['dayofweek'] = 1

# =====================================================
# 3. FEATURES / TARGET
# =====================================================

target = "SalePrice" if "SalePrice" in df_feat.columns else "value"

features = [c for c in ["hour", "dayofweek"] if c in df_feat.columns]

X = df_feat[features]
y = df_feat[target]

# split chronologique simple
split = int(len(df_feat) * 0.8)
X_train, X_test = X.iloc[:split], X.iloc[split:]
y_train, y_test = y.iloc[:split], y.iloc[split:]

# =====================================================
# 4. RANDOM FOREST
# =====================================================

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)
y_pred = rf.predict(X_test)

# =====================================================
# 5. METRICS
# =====================================================

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n📊 METRICS")
print("MAE :", mae)
print("RMSE:", rmse)
print("R2  :", r2)

# =====================================================
# 6. FEATURE IMPORTANCE
# =====================================================

importance = pd.DataFrame({
    "feature": X.columns,
    "importance": rf.feature_importances_
}).sort_values(by="importance", ascending=False)

print("\n🔥 Feature Importance")
print(importance)

print("🚀 Modélisation terminée")