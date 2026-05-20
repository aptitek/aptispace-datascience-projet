import streamlit as st
import pandas as pd
import numpy as np
import kagglehub
import os
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import shap

st.set_page_config(
    page_title="🏠 House Price AI",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 Smart House Price Prediction App")

st.markdown("""
Application intelligente qui permet :
- d’analyser les données immobilières
- de prédire le prix d’une maison
- d’expliquer les décisions du modèle
""")
@st.cache_data
def load_data():
    return pd.read_csv("data/raw/train.csv")

df = load_data()

df["TotalSF"] = df["GrLivArea"] + df["TotalBsmtSF"]
df["HouseAge"] = df["YrSold"] - df["YearBuilt"]
df["QualityScore"] = df["OverallQual"] * df["OverallCond"]

features = [
    "GrLivArea",
    "OverallQual",
    "GarageCars",
    "TotalBsmtSF",
    "YearBuilt",
    "TotalSF",
    "HouseAge",
    "QualityScore"
]

df_model = df[features + ["SalePrice"]].dropna()

X = df_model[features]
y = df_model["SalePrice"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

st.sidebar.header("🏠 Simulation maison")

surface = st.sidebar.slider("Surface habitable", 500, 4000, 1500)
quality = st.sidebar.slider("Qualité générale", 1, 10, 5)
garage = st.sidebar.slider("Garage cars", 0, 4, 2)
year = st.sidebar.slider("Année construction", 1900, 2020, 2000)

total_sf = surface * 1.2
age = 2026 - year
quality_score = quality * 5

input_data = pd.DataFrame([[
    surface,
    quality,
    garage,
    surface,
    year,
    total_sf,
    age,
    quality_score
]], columns=features)

prediction = model.predict(input_data)[0]

st.subheader("💰 Prix estimé")

st.metric(
    "Prix de la maison",
    f"{int(prediction):,} €"
)

st.subheader("📊 Distribution des prix")

fig, ax = plt.subplots()
ax.hist(df["SalePrice"], bins=50)
st.pyplot(fig)

st.subheader("📌 Importance des variables")

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
}).sort_values("Importance")

st.bar_chart(importance.set_index("Feature"))

explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test)

st.subheader("🔍 Explicabilité du modèle")
shap.summary_plot(shap_values, X_test, show=False)
fig = plt.gcf()
st.pyplot(fig)
plt.clf()