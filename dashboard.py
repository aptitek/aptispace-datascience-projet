import joblib
import pandas as pd
import plotly.express as px
import streamlit as st

INR_TO_EUR = 0.0089

# Erreur moyenne du modèle, récupérée depuis l'évaluation
MAE_INR = 9775
MAE_EUR = MAE_INR * INR_TO_EUR

# Configuration générale
st.set_page_config(
    page_title="Dashboard Laptop Price",
    page_icon="💻",
    layout="wide",
)

st.title("💻 Dashboard — Estimation du prix des laptops")

st.info("""
Objectif : Aider un client, un revendeur ou une entreprise à estimer si le prix d’un laptop est cohérent avec ses caractéristiques.
""")

st.success(
    "Conclusion principale : le type d’ordinateur, la marque et les caractéristiques techniques "
    "permettent d’estimer un prix cohérent. Le modèle peut donc servir de base à un outil "
    "d’aide à l’achat ou à la revente."
)

tab_market, tab_analysis, tab_prediction, tab_conclusion = st.tabs([
    "📊 Vue marché",
    "🔎 Analyse des prix",
    "🔮 Simulateur",
    "🎯 Conclusion"
])

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

with st.sidebar.expander("Filtres d’exploration", expanded=True):
    selected_companies = st.multiselect(
        "Marques",
        options=sorted(df["Company"].dropna().unique()),
        default=sorted(df["Company"].dropna().unique()),
    )

    selected_types = st.multiselect(
        "Types de laptop",
        options=sorted(df["TypeName"].dropna().unique()),
        default=sorted(df["TypeName"].dropna().unique()),
    )

df_filtered = df[
    (df["Company"].isin(selected_companies)) &
    (df["TypeName"].isin(selected_types))
]

# Partie 1 : indicateurs clés
with tab_market:
  st.header("Vue d’ensemble du marché")
  st.markdown("<br><br>", unsafe_allow_html=True)

  col1, col2, col3, col4 = st.columns(4)

  col1.metric("Nombre de laptops", len(df_filtered))
  col2.metric("Prix moyen", f"{df_filtered['Price_EUR'].mean():,.0f} €")
  col3.metric("Prix médian", f"{df_filtered['Price_EUR'].median():,.0f} €")
  col4.metric("Prix max", f"{df_filtered['Price_EUR'].max():,.0f} €")

  st.markdown("<br><br>", unsafe_allow_html=True)

  st.markdown("""
  Ces indicateurs donnent une première vision du marché étudié : volume de données,
  niveau moyen des prix et amplitude des valeurs observées.
  """)

# Partie 2 : 
with tab_analysis:
  st.header("1. Segments de marché : les modèles premium se démarquent")

  st.info(
      "Les Workstations et les modèles Gaming se positionnent sur les prix les plus élevés. "
      "Les Netbooks et Notebooks restent les segments les plus accessibles."
  )


  type_order = (
      df_filtered
      .groupby("TypeName")["Price_EUR"]
      .median()
      .sort_values(ascending=False)
      .index
      .tolist()
  )

  fig_box_type = px.box(
      df_filtered,
      x="TypeName",
      y="Price_EUR",
      color="TypeName",
      category_orders={"TypeName": type_order},
      title="Distribution des prix par segment",
      labels={
          "TypeName": "Type d’ordinateur",
          "Price_EUR": "Prix (€)"
      }
  )

  fig_box_type.update_layout(
      xaxis_tickangle=-30,
      showlegend=False,
      height=520,
      margin=dict(l=20, r=20, t=60, b=80)
  )

  st.plotly_chart(fig_box_type, use_container_width=True)


  #  graphique descriptif
  st.header("2. La marque influence fortement le positionnement prix")

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

  #  graphique descriptif
  st.header("3. Certaines caractéristiques techniques expliquent mieux les écarts de prix")

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

# Partie 3 : simulateur de prédiction
with tab_prediction:
  st.header("Simulateur de prix")

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
      # Le modèle prédit en roupies car il a été entraîné sur Price
      predicted_price_inr = model.predict(input_encoded)[0]

      # Conversion en euros pour l'affichage
      predicted_price_eur = predicted_price_inr * INR_TO_EUR

      # Fourchette indicative basée sur l'erreur moyenne du modèle
      lower_price_eur = max(0, predicted_price_eur - MAE_EUR)
      upper_price_eur = predicted_price_eur + MAE_EUR

      st.success(f"Prix estimé : {predicted_price_eur:,.0f} €")

      st.info(
          f"Fourchette indicative : entre {lower_price_eur:,.0f} € "
          f"et {upper_price_eur:,.0f} €"
      )

      st.caption(
          f"Cette fourchette est basée sur l'erreur moyenne du modèle "
          f"MAE ≈ {MAE_EUR:,.0f} €, soit {MAE_INR:,.0f} ₹."
      )

      st.markdown("""
  Le modèle fournit une estimation du prix, mais cette valeur reste une prédiction.
  Pour communiquer cette incertitude, le dashboard affiche également une fourchette indicative basée sur l'erreur moyenne observée lors de l'évaluation du modèle.
      """)

# Conclusion
with tab_conclusion:
    st.header("Conclusion business")

    st.markdown("""
    Ce dashboard montre que le prix d’un ordinateur portable dépend d’une combinaison de facteurs techniques et commerciaux : type d'ordinateur, marque, RAM, processeur, résolution et stockage.

    La partie exploratoire permet de comprendre les différences de prix entre les segments du marché. 

    Le simulateur transforme ensuite le modèle Random Forest en outil concret : l’utilisateur peut saisir les caractéristiques d’un laptop et obtenir une estimation de prix, accompagnée d’une fourchette indicative pour tenir compte de l’incertitude du modèle.

    Ce prototype pourrait donc être financé pour devenir un outil d’aide à la décision destiné aux acheteurs, revendeurs ou entreprises souhaitant évaluer rapidement si le prix d’un laptop est cohérent avec ses caractéristiques.
    """)

    st.info(
        "Action recommandée : poursuivre le développement du modèle avec davantage de données récentes (les données datant de 3 ans), puis l’intégrer dans une interface utilisateur complète."
    )