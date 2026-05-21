import joblib
import pandas as pd
import plotly.express as px
import streamlit as st

# Configuration générale
st.set_page_config(
    page_title="Dashboard Laptop Price",
    page_icon="💻",
    layout="wide",
)

st.title("💻 Dashboard — Estimation du prix des laptops")

st.info("""
🎯 Objectif business : aider un client, un revendeur ou une entreprise à estimer rapidement si le prix d’un ordinateur portable est cohérent avec ses caractéristiques techniques.
""")

st.markdown("""
Aujourd’hui, le marché des ordinateurs portables est très difficile à lire pour un acheteur ou un revendeur. Deux ordinateurs peuvent sembler proches visuellement, mais avoir des prix très différents selon leur marque, leur processeur, leur RAM, leur stockage, leur carte graphique ou leur résolution d’écran.

Pour un client, cela peut entraîner une difficulté à savoir si un ordinateur est vendu à un prix juste. Pour un revendeur, cela peut rendre complexe la fixation d’un prix cohérent et compétitif.

Notre modèle répond à ce besoin en proposant une estimation automatique du prix d’un laptop à partir de ses caractéristiques techniques. L’objectif n’est pas de remplacer l’expertise humaine, mais de fournir un outil d’aide à la décision rapide, cohérent et basé sur les données.
            """)

st.markdown("""
Ce prototype combine deux approches :

1. **Comprendre le marché** grâce à des graphiques interactifs.
2. **Prédire le prix** d’un ordinateur portable à partir de ses caractéristiques.
""")

# Chargement des données
@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/cleaned_data_sample.csv")
    df["Price_EUR"] = df["Price"] * 0.0089
    return df

df = load_data()

# Chargement du modèle
@st.cache_resource
def load_model():
    model = joblib.load("models/random_forest_price_model.pkl")
    model_features = joblib.load("models/model_features.pkl")
    return model, model_features

model, model_features = load_model()

# Sidebar : filtres pour la partie descriptive
st.sidebar.header("Filtres d’exploration")

selected_companies = st.sidebar.multiselect(
    "Marques",
    options=sorted(df["Company"].dropna().unique()),
    default=sorted(df["Company"].dropna().unique()),
)

selected_types = st.sidebar.multiselect(
    "Types de laptop",
    options=sorted(df["TypeName"].dropna().unique()),
    default=sorted(df["TypeName"].dropna().unique()),
)

df_filtered = df[
    (df["Company"].isin(selected_companies)) &
    (df["TypeName"].isin(selected_types))
]

# Partie 1 : indicateurs clés
st.header("1. Vue d’ensemble du marché")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Nombre de laptops", len(df_filtered))
col2.metric("Prix moyen", f"{df_filtered['Price_EUR'].mean():,.0f} €")
col3.metric("Prix médian", f"{df_filtered['Price_EUR'].median():,.0f} €")
col4.metric("Prix max", f"{df_filtered['Price_EUR'].max():,.0f} €")

st.markdown("""
Ces indicateurs donnent une première vision du marché étudié : volume de données,
niveau moyen des prix et amplitude des valeurs observées.
""")

# Partie 2 : 
st.header("2. Les laptops professionnels et haut de gamme se distinguent nettement des modèles standards")

price_by_type = (
    df_filtered
    .groupby("TypeName", as_index=False)["Price_EUR"]
    .mean()
    .sort_values(by="Price_EUR", ascending=False)
)

fig_type = px.bar(
    price_by_type,
    x="TypeName",
    y="Price_EUR",
    title="Prix moyen des laptops par type d’ordinateur",
    labels={
        "TypeName": "Type d’ordinateur",
        "Price": "Prix moyen"
    }
)

st.plotly_chart(fig_type, width="stretch")

# Partie 3 : graphique descriptif
st.header("3. La marque influence fortement le positionnement prix")

price_by_company = (
    df_filtered
    .groupby("Company", as_index=False)["Price_EUR"]
    .mean()
    .sort_values(by="Price_EUR", ascending=False)
)

fig_company = px.bar(
    price_by_company,
    x="Company",
    y="Price_EUR",
    title="Prix moyen des laptops par marque",
    labels={
        "Company": "Marque",
        "Price_EUR": "Prix moyen",
    },
)

st.plotly_chart(fig_company, width='stretch')

# Partie 4 : graphique descriptif
st.header("4. Certaines caractéristiques techniques expliquent mieux les écarts de prix")

available_features = [
    "Ram",
    "Cpu_Frequence_GHz",
    "Res_Width",
    "Res_Height",
    "Inches",
]

available_features = [col for col in available_features if col in df.columns]

selected_feature = st.selectbox(
    "Choisir une caractéristique à comparer avec le prix",
    available_features,
)

hover_columns = [
    col for col in ["Company", "TypeName", "Cpu_Gamme", "has_ssd"]
    if col in df_filtered.columns
]

fig_scatter = px.scatter(
    df_filtered,
    x=selected_feature,
    y="Price_EUR",
    color="Company",
    hover_data=hover_columns,
    title=f"Relation entre {selected_feature} et le prix",
    labels={
        selected_feature: selected_feature,
        "Price_EUR": "Prix",
        "Company": "Marque",
    },
)

st.plotly_chart(fig_scatter, width='stretch')

st.markdown("""
Cette partie permet de comprendre les tendances présentes dans les données.
Elle justifie l’intérêt d’un modèle prédictif : le prix n’est pas aléatoire,
il dépend de plusieurs caractéristiques techniques et commerciales.
""")

# Partie 5 : simulateur de prédiction
st.header("5. Simulateur de prix")

st.markdown("""
Saisissez les caractéristiques d’un laptop pour obtenir une estimation automatique du prix.
""")

col_left, col_right = st.columns(2)

with col_left:
    company = st.selectbox(
        "Marque",
        options=sorted(df["Company"].dropna().unique()),
    )

    type_name = st.selectbox(
        "Type de laptop",
        options=sorted(df["TypeName"].dropna().unique()),
    )

    cpu_gamme = st.selectbox(
        "Gamme CPU",
        options=sorted(df["Cpu_Gamme"].dropna().unique()) if "Cpu_Gamme" in df.columns else ["Unknown"],
    )

    ram = st.number_input(
        "RAM en Go",
        min_value=2,
        max_value=64,
        value=8,
        step=2,
    )

with col_right:
    inches = st.number_input(
        "Taille écran en pouces",
        min_value=10.0,
        max_value=20.0,
        value=15.6,
        step=0.1,
    )

    cpu_freq = st.number_input(
        "Fréquence CPU en GHz",
        min_value=0.5,
        max_value=5.0,
        value=2.5,
        step=0.1,
    )

    res_width = st.number_input(
        "Résolution largeur",
        min_value=800,
        max_value=4000,
        value=1920,
        step=100,
    )

    res_height = st.number_input(
        "Résolution hauteur",
        min_value=600,
        max_value=2500,
        value=1080,
        step=100,
    )

has_ssd_label = st.radio(
    "Présence d’un SSD",
    options=["Oui", "Non"],
    horizontal=True,
)

has_ssd = 1 if has_ssd_label == "Oui" else 0

# Construction de la ligne utilisateur
input_data = pd.DataFrame([{
    "Company": company,
    "TypeName": type_name,
    "Cpu_Gamme": cpu_gamme,
    "Ram": ram,
    "Inches": inches,
    "Cpu_Frequence_GHz": cpu_freq,
    "Res_Width": res_width,
    "Res_Height": res_height,
    "has_ssd": has_ssd,
}])

# Encodage des variables catégorielles
input_encoded = pd.get_dummies(input_data)

# Alignement avec les colonnes du modèle
input_encoded = input_encoded.reindex(columns=model_features, fill_value=0)

if st.button("Estimer le prix"):
    predicted_price_inr = model.predict(input_encoded)[0]
    predicted_price_eur = predicted_price_inr * 0.0089

    st.success(f"Prix estimé : {predicted_price_eur:,.0f} €")

    st.markdown("""
    Cette estimation est produite à partir du modèle Random Forest entraîné sur les données disponibles.
    Elle doit être interprétée comme une aide à la décision, et non comme un prix exact garanti.
    """)

# Conclusion
st.header("5. Conclusion business")

st.markdown("""
Ce dashboard montre l’intérêt concret du modèle.

La partie descriptive permet de comprendre les tendances du marché, tandis que
le simulateur de prix transforme le modèle en prototype utilisable.

Ce modèle peut permettre de développer un outil d'aide à la décision utile pour plusieurs profils :
- un client qui veut véririer si un laptop est vendu à un prix cohérent ;
- un revendeur qui souhaite fixer des prix compétitifs ;
- une entreprise qui doit acheter ou renouveler un parc informatique ;
- une plateforme de vente qui peut proposer une estimation automatique de prix.
""")