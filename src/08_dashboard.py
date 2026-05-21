"""
08_dashboard.py — Dashboard Interactif pour la Prédiction Immobilière

Tableau de bord Plotly Dash présentant les résultats du pipeline de Data Science :
analyse exploratoire, modèle prédictif RandomForest, et classification CNN.

Lancement : py -3.13 src/08_dashboard.py
Puis ouvrir dans le navigateur : http://127.0.0.1:8050
"""

import os
import joblib
import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html, Input, Output

# =====================================================
# 1. CHARGEMENT DES DONNÉES ET DU MODÈLE
# =====================================================
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(BASE_DIR, "data", "processed", "cleaned_data_sample.csv")
model_path = os.path.join(BASE_DIR, "models", "rf_house_prices.pkl")

df = pd.read_csv(data_path)
print(f"✔ Dataset chargé : {df.shape}")

if 'YearBuilt' in df.columns and 'YrSold' in df.columns:
    df['HouseAge'] = df['YrSold'] - df['YearBuilt']

model = joblib.load(model_path)
print(f"✔ Modèle chargé : {model_path}")

# =====================================================
# 2. CRÉATION DE L'APPLICATION DASH
# =====================================================
app = Dash(__name__)
app.title = "Dashboard Immobilier — Pipeline Data Science"

# =====================================================
# 3. KPIs PRINCIPAUX
# =====================================================
nb_biens = len(df)
prix_moyen = df['SalePrice'].mean()
prix_median = df['SalePrice'].median()
surface_moyenne = df['GrLivArea'].mean()

# =====================================================
# 4. STYLES RÉUTILISABLES
# =====================================================
CARD_STYLE = {
    'backgroundColor': 'white', 'padding': '20px',
    'borderRadius': '10px', 'marginBottom': '20px',
    'boxShadow': '0 2px 4px rgba(0,0,0,0.05)'
}

KPI_STYLE = {
    'backgroundColor': '#ecf0f1', 'padding': '20px',
    'borderRadius': '10px', 'flex': '1', 'margin': '10px',
    'textAlign': 'center'
}

SLIDER_STYLE = {'marginBottom': '25px'}

# =====================================================
# 5. LAYOUT
# =====================================================
app.layout = html.Div([

    # ===== HEADER =====
    html.Div([
        html.H1("Dashboard Immobilier — House Prices",
                style={'color': '#2c3e50', 'marginBottom': '5px'}),
        html.P("Analyse prédictive du marché immobilier californien — Pipeline Data Science complet",
               style={'color': '#7f8c8d', 'fontSize': '16px', 'marginTop': '0'})
    ], style={'padding': '30px 50px 20px 50px', 'borderBottom': '2px solid #ecf0f1'}),

    # ===== SECTION 1 : KPIs =====
    html.Div([
        html.H2("Vue d'ensemble du marché", style={'color': '#2c3e50'}),
        html.Div([
            html.Div([
                html.H4("Biens analysés", style={'color': '#7f8c8d', 'fontSize': '14px'}),
                html.H2(f"{nb_biens:,}", style={'color': '#3498db', 'margin': '0'})
            ], style=KPI_STYLE),
            html.Div([
                html.H4("Prix moyen", style={'color': '#7f8c8d', 'fontSize': '14px'}),
                html.H2(f"${prix_moyen:,.0f}", style={'color': '#27ae60', 'margin': '0'})
            ], style=KPI_STYLE),
            html.Div([
                html.H4("Prix médian", style={'color': '#7f8c8d', 'fontSize': '14px'}),
                html.H2(f"${prix_median:,.0f}", style={'color': '#e67e22', 'margin': '0'})
            ], style=KPI_STYLE),
            html.Div([
                html.H4("Surface moyenne", style={'color': '#7f8c8d', 'fontSize': '14px'}),
                html.H2(f"{surface_moyenne:,.0f} sqft", style={'color': '#9b59b6', 'margin': '0'})
            ], style=KPI_STYLE),
        ], style={'display': 'flex', 'flexDirection': 'row'})
    ], style={'padding': '20px 50px'}),

    # ===== SECTION 2 : ANALYSE EXPLORATOIRE =====
    html.Div([
        html.H2("Analyse exploratoire", style={'color': '#2c3e50', 'marginTop': '40px'}),

        html.Div([
            html.H4("Distribution des prix de vente", style={'color': '#34495e'}),
            dcc.Graph(figure=px.histogram(
                df, x='SalePrice', nbins=50,
                labels={'SalePrice': 'Prix de vente ($)'},
                color_discrete_sequence=['#3498db']
            ).update_layout(plot_bgcolor='white', paper_bgcolor='white', showlegend=False))
        ], style=CARD_STYLE),

        html.Div([
            html.H4("Relation surface habitable / prix", style={'color': '#34495e'}),
            dcc.Graph(figure=px.scatter(
                df, x='GrLivArea', y='SalePrice',
                color='OverallQual', color_continuous_scale='Viridis',
                labels={'GrLivArea': 'Surface habitable (sqft)', 'SalePrice': 'Prix de vente ($)', 'OverallQual': 'Qualité'}
            ).update_layout(plot_bgcolor='white', paper_bgcolor='white'))
        ], style=CARD_STYLE),

        html.Div([
            html.H4("Prix selon la qualité globale du bien", style={'color': '#34495e'}),
            dcc.Graph(figure=px.box(
                df, x='OverallQual', y='SalePrice',
                labels={'OverallQual': 'Qualité globale (1=basse, 10=haute)', 'SalePrice': 'Prix de vente ($)'},
                color_discrete_sequence=['#27ae60']
            ).update_layout(plot_bgcolor='white', paper_bgcolor='white'))
        ], style=CARD_STYLE),
    ], style={'padding': '20px 50px'}),

    # ===== SECTION 3 : SIMULATEUR DE PRIX =====
    html.Div([
        html.H2("Simulateur de prix", style={'color': '#2c3e50', 'marginTop': '40px'}),
        html.P("Ajustez les caractéristiques du bien pour obtenir une estimation en temps réel.",
               style={'color': '#7f8c8d', 'marginBottom': '20px'}),

        html.Div([
            # Colonne gauche : les curseurs
            html.Div([
                html.Label("Surface habitable (sqft)", style={'fontWeight': 'bold'}),
                dcc.Slider(id='slider-grlivarea', min=500, max=5000, step=50,
                           value=1500, marks={500: '500', 2500: '2500', 5000: '5000'},
                           tooltip={'placement': 'bottom', 'always_visible': True}),
                html.Br(),

                html.Label("Qualité globale (1 à 10)", style={'fontWeight': 'bold'}),
                dcc.Slider(id='slider-qual', min=1, max=10, step=1, value=5,
                           marks={i: str(i) for i in range(1, 11)}),
                html.Br(),

                html.Label("Âge de la maison (années)", style={'fontWeight': 'bold'}),
                dcc.Slider(id='slider-age', min=0, max=150, step=1, value=30,
                           marks={0: '0', 75: '75', 150: '150'},
                           tooltip={'placement': 'bottom', 'always_visible': True}),
                html.Br(),

                html.Label("Capacité du garage (nb voitures)", style={'fontWeight': 'bold'}),
                dcc.Slider(id='slider-garage', min=0, max=4, step=1, value=2,
                           marks={i: str(i) for i in range(0, 5)}),
                html.Br(),

                html.Label("Surface du sous-sol (sqft)", style={'fontWeight': 'bold'}),
                dcc.Slider(id='slider-bsmt', min=0, max=3000, step=50, value=800,
                           marks={0: '0', 1500: '1500', 3000: '3000'},
                           tooltip={'placement': 'bottom', 'always_visible': True}),
                html.Br(),

                html.Label("Coefficient de zone", style={'fontWeight': 'bold'}),
                dcc.Slider(id='slider-coef', min=1.0, max=1.5, step=0.1, value=1.0,
                           marks={1.0: 'Standard', 1.2: 'Premium', 1.5: 'Luxury'}),
            ], style={'flex': '1', 'padding': '20px'}),

            # Colonne droite : le prix prédit
            html.Div([
                html.H4("Prix prédit", style={'color': '#7f8c8d', 'fontSize': '16px', 'marginBottom': '10px'}),
                html.H1(id='prix-predit', style={'color': '#27ae60', 'fontSize': '48px', 'margin': '0'}),
                html.P("Estimation basée sur le modèle RandomForest (R² = 0.73)",
                       style={'color': '#95a5a6', 'fontSize': '12px', 'marginTop': '15px'})
            ], style={
                'flex': '1', 'padding': '40px',
                'backgroundColor': '#ecf0f1', 'borderRadius': '10px',
                'textAlign': 'center', 'margin': '20px'
            })
        ], style={'display': 'flex', 'flexDirection': 'row'})
    ], style={'padding': '20px 50px'}),

], style={'fontFamily': 'Arial, sans-serif', 'backgroundColor': '#fafafa', 'minHeight': '100vh'})


# =====================================================
# 6. CALLBACK INTERACTIF — PRÉDICTION EN TEMPS RÉEL
# =====================================================
@app.callback(
    Output('prix-predit', 'children'),
    [
        Input('slider-grlivarea', 'value'),
        Input('slider-qual', 'value'),
        Input('slider-age', 'value'),
        Input('slider-garage', 'value'),
        Input('slider-bsmt', 'value'),
        Input('slider-coef', 'value'),
    ]
)

def predire_prix(grlivarea, qual, age, garage, bsmt, coef):
    # Créer un DataFrame avec les bons noms de colonnes (corrige le warning)
    features_df = pd.DataFrame(
        [[grlivarea, qual, age, garage, bsmt, coef]],
        columns=['GrLivArea', 'OverallQual', 'HouseAge', 'GarageCars', 'TotalBsmtSF', 'coef_multiplicateur']
    )
    prix = model.predict(features_df)[0]
    return f"${prix:,.0f}"

# =====================================================
# 7. LANCEMENT DU SERVEUR
# =====================================================
if __name__ == '__main__':
    print("\n🚀 Dashboard lancé !")
    print("📍 Ouvre dans ton navigateur : http://127.0.0.1:8050")
    print("⏹️  Pour arrêter le serveur : Ctrl + C\n")
    app.run(debug=True, port=8050)