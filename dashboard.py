import joblib
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import streamlit as st

# =========================
# CONSTANTES
# =========================

INR_TO_EUR = 0.0089
MAE_INR = 9775
MAE_EUR = MAE_INR * INR_TO_EUR

COLORS = {
    "primary": "#2563eb",
    "primary_light": "#eff6ff",
    "accent": "#0ea5e9",
    "success": "#10b981",
    "warning": "#f59e0b",
    "danger": "#ef4444",
    "text": "#0f172a",
    "muted": "#64748b",
    "border": "#e2e8f0",
    "bg": "#f8fafc",
}

PLOTLY_COLORS = px.colors.qualitative.Set2

# ← size=13 ajouté ici
PLOTLY_LAYOUT = dict(
    font=dict(family="'DM Sans', sans-serif", color=COLORS["text"], size=13),
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    margin=dict(l=10, r=10, t=30, b=50),
    legend=dict(
        bgcolor="rgba(255,255,255,0.8)",
        bordercolor=COLORS["border"],
        borderwidth=1,
        font=dict(size=12),
    ),
)

# =========================
# CONFIGURATION STREAMLIT
# =========================

st.set_page_config(
    page_title="Estimateur de prix — Ordinateur portable",
    page_icon="💻",
    layout="wide",
)

st.markdown("""
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700;800&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<style>
    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif !important; }
    .block-container { padding: 1.5rem 3rem 4rem 3rem; max-width: 100%; }
    h1 { font-size: 2.4rem !important; font-weight: 800 !important; color: #0f172a !important; line-height: 1.1 !important; }
    h2 { font-size: 1.7rem !important; font-weight: 700 !important; color: #0f172a !important; }
    h3 { font-size: 1.3rem !important; font-weight: 700 !important; color: #0f172a !important; }
    .app-header { display: flex; align-items: flex-start; gap: 1rem; margin-top: 1rem; margin-bottom: 1.8rem; padding-bottom: 1.2rem; border-bottom: 2px solid #e2e8f0; }
    .app-header-icon { font-size: 2.6rem; line-height: 1; }
    .app-header-title { font-size: 2rem; font-weight: 800; color: #0f172a; margin: 0; line-height: 1.15; }
    .app-header-subtitle { font-size: 0.97rem; color: #64748b; margin: 0.2rem 0 0 0; font-weight: 400; }
    div[data-testid="stSelectbox"] label p,
    div[data-testid="stSlider"] label p,
    div[data-testid="stRadio"] label p,
    div[data-testid="stMultiSelect"] label p {
        font-size: 0.88rem !important; font-weight: 700 !important; color: #0f172a !important;
        text-transform: uppercase; letter-spacing: 0.04em;
    }
    .sim-section-title { font-size: 0.75rem; font-weight: 700; color: #2563eb; text-transform: uppercase; letter-spacing: 0.08em; margin: 1.2rem 0 0.6rem 0; padding-bottom: 0.4rem; border-bottom: 1px solid #dbeafe; }
    .sim-help { background: linear-gradient(135deg, #eff6ff, #f0fdf4); border-left: 3px solid #2563eb; border-radius: 8px; padding: 0.7rem 0.9rem; margin-bottom: 0.8rem; color: #475569; font-size: 0.9rem; line-height: 1.5; }
    .result-card { background: linear-gradient(135deg, #1d4ed8 0%, #0ea5e9 100%); border-radius: 16px; padding: 1.4rem 1.2rem; margin-top: 1rem; text-align: center; box-shadow: 0 8px 32px rgba(37,99,235,0.3); }
    .result-badge { display: inline-block; background: rgba(255,255,255,0.2); color: #fff; font-size: 0.72rem; font-weight: 700; letter-spacing: 0.1em; text-transform: uppercase; padding: 0.2rem 0.7rem; border-radius: 20px; margin-bottom: 0.6rem; }
    .result-value { font-size: 2.8rem; font-weight: 900; color: #ffffff; line-height: 1; font-family: 'DM Mono', monospace; }
    .result-range { font-size: 0.9rem; color: rgba(255,255,255,0.8); margin-top: 0.5rem; font-weight: 500; }
    .market-compare { background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 0.9rem 1rem; margin-top: 0.8rem; font-size: 0.9rem; color: #334155; }
    .market-compare b { color: #0f172a; }
    .badge-low  { background:#dcfce7; color:#15803d; border-radius:6px; padding:0.15rem 0.5rem; font-weight:700; font-size:0.82rem; }
    .badge-mid  { background:#fef9c3; color:#b45309; border-radius:6px; padding:0.15rem 0.5rem; font-weight:700; font-size:0.82rem; }
    .badge-high { background:#fee2e2; color:#b91c1c; border-radius:6px; padding:0.15rem 0.5rem; font-weight:700; font-size:0.82rem; }
    div[data-testid="stMetric"] { background: #ffffff; border: 1px solid #e2e8f0; padding: 1rem 1.1rem; border-radius: 14px; box-shadow: 0 1px 4px rgba(15,23,42,0.05); transition: box-shadow 0.2s; }
    div[data-testid="stMetric"]:hover { box-shadow: 0 4px 16px rgba(37,99,235,0.1); }
    div[data-testid="stMetricLabel"] { font-size: 0.8rem; color: #64748b; font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em; }
    div[data-testid="stMetricValue"] { font-size: 1.7rem; color: #0f172a; font-weight: 800; font-family: 'DM Mono', monospace; }
    .stButton > button { height: 3rem; font-size: 0.97rem; font-weight: 700; border-radius: 10px; background: linear-gradient(135deg, #2563eb, #0ea5e9) !important; color: white !important; border: none !important; letter-spacing: 0.02em; transition: opacity 0.2s, transform 0.1s; }
    .stButton > button:hover { opacity: 0.92; transform: translateY(-1px); }
    details summary { font-weight: 700 !important; font-size: 0.92rem !important; color: #0f172a !important; }
    .chart-title { font-size: 0.92rem; font-weight: 700; color: #0f172a; margin-bottom: 0.3rem; margin-top: 0.8rem; }
    .chart-subtitle { font-size: 0.8rem; color: #475569; margin-bottom: 0.2rem; }
    .divider { height: 1px; background: #e2e8f0; margin: 1rem 0; }
    [data-testid="stCaptionContainer"] { font-size: 0.82rem !important; color: #94a3b8 !important; }
</style>
""", unsafe_allow_html=True)


# =========================
# CHARGEMENT DES DONNÉES
# =========================

@st.cache_data
def load_data():
    df = pd.read_csv("data/processed/cleaned_data_sample.csv")
    df["Price_EUR"] = df["Price"] * INR_TO_EUR
    return df


@st.cache_resource
def load_model():
    model = joblib.load("models/random_forest_price_model.pkl")
    model_features = joblib.load("models/model_features.pkl")
    label_encoders = joblib.load("models/label_encoders.pkl")
    return model, model_features, label_encoders


df = load_data()
model, model_features, label_encoders = load_model()


# =========================
# HEADER
# =========================

st.markdown("""
<div class="app-header">
    <div class="app-header-icon">💻</div>
    <div>
        <div class="app-header-title">Estimateur de prix — Ordinateur portable</div>
        <div class="app-header-subtitle">
            Estimez le prix d'un ordinateur à partir de ses caractéristiques et positionnez-le par rapport au marché.
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# =========================
# LAYOUT PRINCIPAL
# =========================

left_col, right_col = st.columns([0.78, 2.22], gap="large")


# ============================================================
# COLONNE GAUCHE — SIMULATEUR
# ============================================================

with left_col:
    with st.container(border=True):
        st.markdown("### 💰 Simulateur de prix")
        st.markdown("""
        <div class="sim-help">
            Renseignez les caractéristiques du ordinateur. Le modèle Random Forest
            estime un prix cohérent avec les données du marché observé.
        </div>
        """, unsafe_allow_html=True)

        st.markdown('<div class="sim-section-title">Profil</div>', unsafe_allow_html=True)

        company = st.selectbox("Marque", options=sorted(df["Company"].dropna().astype(str).unique()))
        type_name = st.selectbox("Type d'ordinateur", options=sorted(df["TypeName"].dropna().astype(str).unique()))
        op_sys = st.selectbox("Système d'exploitation", options=sorted(df["OpSys"].dropna().astype(str).unique()))
        cpu_gamme = st.selectbox("Gamme CPU", options=sorted(df["Cpu_Gamme"].dropna().astype(str).unique()))

        st.markdown('<div class="sim-section-title">Caractéristiques techniques</div>', unsafe_allow_html=True)

        c1, c2 = st.columns(2)
        with c1:
            ram = st.slider("RAM (Go)", min_value=2, max_value=64, value=8, step=2)
        with c2:
            total_memory_gb = st.slider("Stockage (Go)", min_value=32, max_value=4000, value=512, step=32)

        c3, c4 = st.columns(2)
        with c3:
            inches = st.slider("Écran (pouces)", min_value=10.0, max_value=20.0, value=15.6, step=0.1)
        with c4:
            cpu_freq = st.slider("Fréq. CPU (GHz)", min_value=0.5, max_value=5.0, value=2.5, step=0.1)

        c5, c6 = st.columns(2)
        with c5:
            res_width = st.slider("Résol. largeur", min_value=800, max_value=4000, value=1920, step=100)
        with c6:
            res_height = st.slider("Résol. hauteur", min_value=600, max_value=2500, value=1080, step=100)

        default_weight = round(float(df["weight_kg"].median()), 1)
        weight_kg = st.slider("Poids (kg)", min_value=0.5, max_value=5.0, value=default_weight, step=0.1)

        st.markdown('<div class="sim-section-title">Options</div>', unsafe_allow_html=True)

        oc1, oc2, oc3 = st.columns(3)
        with oc1:
            has_ssd_label = st.radio("SSD", options=["Oui", "Non"], horizontal=False)
        with oc2:
            has_hdd_label = st.radio("HDD", options=["Oui", "Non"], horizontal=False)
        with oc3:
            is_ips_label = st.radio("Écran IPS", options=["Oui", "Non"], horizontal=False)

        gpu_brand = st.selectbox("Carte graphique", options=["Intel", "Nvidia", "AMD", "Autre"])

        has_ssd = 1 if has_ssd_label == "Oui" else 0
        has_hdd = 1 if has_hdd_label == "Oui" else 0
        is_ips = 1 if is_ips_label == "Oui" else 0
        has_intel_gpu = 1 if gpu_brand == "Intel" else 0
        has_nvidia_gpu = 1 if gpu_brand == "Nvidia" else 0
        has_amd_gpu = 1 if gpu_brand == "AMD" else 0

        input_data = pd.DataFrame([{
            "Company": company, "TypeName": type_name, "OpSys": op_sys,
            "Cpu_Gamme": cpu_gamme, "Inches": inches, "Ram": ram,
            "Cpu_Frequence_GHz": cpu_freq, "weight_kg": weight_kg,
            "total_memory_gb": total_memory_gb, "Res_Width": res_width,
            "Res_Height": res_height, "has_ssd": has_ssd, "has_hdd": has_hdd,
            "has_intel_gpu": has_intel_gpu, "has_nvidia_gpu": has_nvidia_gpu,
            "has_amd_gpu": has_amd_gpu, "Is_IPS": is_ips,
        }])

        input_encoded = input_data.copy()
        for col, encoder in label_encoders.items():
            if col in input_encoded.columns:
                try:
                    input_encoded[f"{col}_enc"] = np.asarray(
                        encoder.transform(input_encoded[col].astype(str)), dtype=np.int64
                    )
                except ValueError:
                    st.error(f"Valeur inconnue pour '{col}'.")
                    st.stop()

        input_encoded = input_encoded.drop(columns=list(label_encoders.keys()), errors="ignore")
        input_encoded = input_encoded.reindex(columns=model_features, fill_value=0)

        if st.button("💰 Estimer le prix", type="primary", use_container_width=True):
            predicted_price_inr = model.predict(input_encoded)[0]
            predicted_price_eur = predicted_price_inr * INR_TO_EUR
            lower_eur = max(0, predicted_price_eur - MAE_EUR)
            upper_eur = predicted_price_eur + MAE_EUR

            st.markdown(f"""
            <div class="result-card">
                <div class="result-badge">Prix estimé</div>
                <div class="result-value">{predicted_price_eur:,.0f} €</div>
                <div class="result-range">Fourchette · {lower_eur:,.0f} € — {upper_eur:,.0f} €</div>
            </div>
            """, unsafe_allow_html=True)

            median_market = df["Price_EUR"].median()
            pct = (predicted_price_eur - median_market) / median_market * 100

            if pct < -15:
                badge = '<span class="badge-low">Entrée de gamme</span>'
                position_txt = f"En dessous de la médiane marché de {abs(pct):.0f}%"
            elif pct > 30:
                badge = '<span class="badge-high">Premium</span>'
                position_txt = f"Au-dessus de la médiane marché de {pct:.0f}%"
            else:
                badge = '<span class="badge-mid">Milieu de gamme</span>'
                position_txt = f"Dans la moyenne du marché (écart : {pct:+.0f}%)"

            st.markdown(f"""
            <div class="market-compare">
                Positionnement {badge}<br>
                <span style="color:#64748b; font-size:0.85rem">{position_txt} · Médiane marché : {median_market:,.0f} €</span>
            </div>
            """, unsafe_allow_html=True)

            st.caption(f"Erreur moyenne du modèle (MAE) ≈ {MAE_EUR:,.0f} € · Random Forest entraîné sur {len(df):,} ordinateurs")


# ============================================================
# COLONNE DROITE — MARCHÉ
# ============================================================

with right_col:
    st.markdown("### 📊 Marché de référence")

    with st.expander("🔎 Filtres du marché", expanded=True):
        fc1, fc2 = st.columns(2)
        with fc1:
            selected_companies = st.multiselect(
                "Marques",
                options=sorted(df["Company"].dropna().astype(str).unique()),
                default=[],
                placeholder="Toutes les marques",
            )
        with fc2:
            selected_types = st.multiselect(
                "Types d'ordinateurs",
                options=sorted(df["TypeName"].dropna().astype(str).unique()),
                default=[],
                placeholder="Tous les types",
            )

    df_filtered = df.copy()
    if selected_companies:
        df_filtered = df_filtered[df_filtered["Company"].astype(str).isin(selected_companies)]
    if selected_types:
        df_filtered = df_filtered[df_filtered["TypeName"].astype(str).isin(selected_types)]

    if df_filtered.empty:
        st.warning("Aucune donnée ne correspond aux filtres sélectionnés.")
        st.stop()

    # ── KPIs ──
    k1, k2, k3, k4, k5 = st.columns(5)
    with k1:
        st.metric("Ordinateurs", f"{len(df_filtered):,}".replace(",", "\u202f"))
    with k2:
        st.metric("Prix moyen", f"{df_filtered['Price_EUR'].mean():,.0f} €")
    with k3:
        st.metric("Prix médian", f"{df_filtered['Price_EUR'].median():,.0f} €")
    with k4:
        st.metric("Prix min", f"{df_filtered['Price_EUR'].min():,.0f} €")
    with k5:
        st.metric("Prix max", f"{df_filtered['Price_EUR'].max():,.0f} €")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ── Ligne 1 : distribution + boxplot ──
    row1_l, row1_r = st.columns(2)

    with row1_l:
        st.markdown('<div class="chart-title">Distribution des prix</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-subtitle">Répartition par tranche de prix</div>', unsafe_allow_html=True)
        fig_hist = px.histogram(
            df_filtered, x="Price_EUR", nbins=40,
            color_discrete_sequence=[COLORS["primary"]],
            labels={"Price_EUR": "Prix (€)"},
        )
        fig_hist.update_traces(marker_line_width=0, opacity=0.85,
                            hovertemplate="Prix : %{x:.0f} €<br>Nb. ordinateurs : %{y}<extra></extra>")
        fig_hist.update_layout(**PLOTLY_LAYOUT, height=260,
                            xaxis=dict(showgrid=False),
                            yaxis=dict(showgrid=True, gridcolor="#f1f5f9", title="Nb. ordinateurs"))
        st.plotly_chart(fig_hist, use_container_width=True)

    with row1_r:
        st.markdown('<div class="chart-title">Prix par segment</div>', unsafe_allow_html=True)
        st.markdown("""<div class="chart-subtitle">Médiane et dispersion par type d'ordinateur</div>""", unsafe_allow_html=True)
        type_order = (
            df_filtered.groupby("TypeName")["Price_EUR"]
            .median().sort_values(ascending=False).index.tolist()
        )
        fig_box = px.box(
            df_filtered, x="TypeName", y="Price_EUR",
            color="TypeName",
            category_orders={"TypeName": type_order},
            color_discrete_sequence=PLOTLY_COLORS,
            labels={"TypeName": "", "Price_EUR": "Prix (€)"},
        )
        fig_box.update_traces(
            hovertemplate="<b>%{x}</b><br>Prix : %{y:.0f} €<extra></extra>"
        )
        fig_box.update_layout(**PLOTLY_LAYOUT, showlegend=False, height=260,
                            xaxis_tickangle=-30,
                            yaxis=dict(showgrid=True, gridcolor="#f1f5f9", title="", tickformat=",.0f"))
  
        st.plotly_chart(fig_box, use_container_width=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # ── Ligne 2 : heatmap + scatter ──
    row2_l, row2_r = st.columns(2)

    with row2_l:
        st.markdown('<div class="chart-title">Heatmap prix moyen · Marque × Type</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-subtitle">Plus la case est foncée, plus le prix moyen est élevé</div>', unsafe_allow_html=True)

        top_companies = (
            df_filtered.groupby("Company")["Price_EUR"]
            .mean().nlargest(8).index.tolist()
        )
        heatmap_df = (
            df_filtered[df_filtered["Company"].isin(top_companies)]
            .groupby(["Company", "TypeName"])["Price_EUR"]
            .mean().reset_index()
            .pivot(index="Company", columns="TypeName", values="Price_EUR")
        )

        z_vals = heatmap_df.values.astype(float)
        z_min = np.nanmin(z_vals)
        z_max = np.nanmax(z_vals)

        fig_heat = go.Figure(data=go.Heatmap(
            z=z_vals,
            x=heatmap_df.columns.tolist(),
            y=heatmap_df.index.tolist(),
            colorscale=[[0, "#eff6ff"], [0.5, "#60a5fa"], [1, "#1d4ed8"]],
            hovertemplate="<b>%{y}</b> · %{x}<br>Prix moyen : %{z:.0f} €<extra></extra>",
            texttemplate="",
            showscale=False,
        ))

        # Annotation case par case avec couleur adaptée à la luminosité
        for i, company in enumerate(heatmap_df.index):
            for j, typ in enumerate(heatmap_df.columns):
                val = heatmap_df.loc[company, typ]
                if pd.notna(val):
                    ratio = (val - z_min) / (z_max - z_min + 1e-9)
                    txt_color = "white" if ratio > 0.4 else "#1e3a5f"
                    fig_heat.add_annotation(
                        x=typ, y=company,
                        text=f"{val:,.0f} €",
                        showarrow=False,
                        font=dict(size=12, color=txt_color, family="'DM Sans', sans-serif"),
                        xref="x", yref="y",
                    )

        fig_heat.update_layout(**PLOTLY_LAYOUT, height=300,
                            xaxis=dict(tickangle=-30, tickfont=dict(size=12)),
                            yaxis=dict(tickfont=dict(size=12)))
        st.plotly_chart(fig_heat, use_container_width=True)

    with row2_r:
        st.markdown('<div class="chart-title">Facteur technique / prix</div>', unsafe_allow_html=True)
        available_features = [
            col for col in ["Ram", "Cpu_Frequence_GHz", "total_memory_gb",
                            "Inches", "weight_kg", "Res_Width", "Res_Height"]
            if col in df_filtered.columns
        ]
        feature_labels = {
            "Ram": "RAM (Go)", "Cpu_Frequence_GHz": "Fréquence CPU (GHz)",
            "Res_Width": "Résolution largeur", "Res_Height": "Résolution hauteur",
            "Inches": "Taille écran (po)", "weight_kg": "Poids (kg)",
            "total_memory_gb": "Stockage total (Go)",
        }
        selected_feature = st.selectbox(
            "Variable",
            available_features,
            format_func=lambda x: feature_labels.get(x, x),
            label_visibility="collapsed",
        )
        fig_scatter = px.scatter(
            df_filtered, x=selected_feature, y="Price_EUR",
            color="TypeName",
            color_discrete_sequence=PLOTLY_COLORS,
            trendline="ols",
            trendline_scope="overall",
            trendline_color_override="#94a3b8",
            opacity=0.65,
            labels={
                selected_feature: feature_labels.get(selected_feature, selected_feature),
                "Price_EUR": "Prix (€)", "TypeName": "Type",
            },
        )
        fig_scatter.for_each_trace(
            lambda t: t.update(name="Tendance générale") if t.name == "Overall Trendline" else t
        )
        fig_scatter.update_traces(
            hovertemplate="<b>%{fullData.name}</b><br>" + feature_labels.get(selected_feature, selected_feature) + " : %{x}<br>Prix : %{y:.0f} €<extra></extra>"
        )
        fig_scatter.update_layout(**PLOTLY_LAYOUT, height=300,
                                yaxis=dict(showgrid=True, gridcolor="#f1f5f9"))
        st.plotly_chart(fig_scatter, use_container_width=True)

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


    # ── Ligne 3 : Top marques + RAM vs prix médian ──
    row3_l, row3_r = st.columns(2)

    with row3_l:
        st.markdown('<div class="chart-title">Top 8 marques · Prix moyen</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-subtitle">Marques triées par prix moyen décroissant</div>', unsafe_allow_html=True)
        price_by_company = (
            df_filtered.groupby("Company", as_index=False)
            .agg(Prix_moyen=("Price_EUR", "mean"), Nb=("Price_EUR", "count"))
            .sort_values("Prix_moyen", ascending=False).head(8)
        )
        fig_bar = px.bar(
            price_by_company, x="Company", y="Prix_moyen",
            color="Prix_moyen",
            color_continuous_scale=["#bfdbfe", "#1d4ed8"],
            labels={"Company": "", "Prix_moyen": "Prix moyen (€)", "Nb": "Nb ordinateurs"},
            hover_data=["Nb"],
            text="Prix_moyen",
        )
        fig_bar.update_traces(texttemplate="%{text:.0f} €", textposition="outside",
                            textfont_size=11, marker_line_width=0,
                             hovertemplate="<b>%{x}</b><br>Prix moyen : %{y:.0f} €<extra></extra>")
        fig_bar.update_layout(**PLOTLY_LAYOUT, height=270,
                            showlegend=False, coloraxis_showscale=False,
                            xaxis_tickangle=-30,
                            yaxis=dict(showgrid=True, gridcolor="#f1f5f9"))
        st.plotly_chart(fig_bar, use_container_width=True)

    with row3_r:
        st.markdown('<div class="chart-title">RAM vs prix médian</div>', unsafe_allow_html=True)
        st.markdown('<div class="chart-subtitle">Impact de la mémoire vive sur le prix</div>', unsafe_allow_html=True)
        ram_price = (
            df_filtered.groupby("Ram")["Price_EUR"]
            .agg(Prix_median=("median"), Nb_ordinateurs=("count"))
            .reset_index()
            .sort_values("Ram")
        )
        fig_ram = px.area(
            ram_price, x="Ram", y="Prix_median",
            color_discrete_sequence=[COLORS["primary"]],
            labels={"Ram": "RAM (Go)", "Prix_median": "Prix médian (€)"},
            markers=True,
            custom_data=["Nb_ordinateurs"],
        )
        fig_ram.update_traces(
            fill="tozeroy",
            fillcolor="rgba(37,99,235,0.08)",
            line=dict(color=COLORS["primary"], width=2.5),
            marker=dict(size=7, color=COLORS["primary"]),
            hovertemplate=(
                "<b>RAM : %{x} Go</b><br>"
                "Prix médian : %{y:.0f} €<br>"
                "Nb. ordinateurs : %{customdata[0]}<br>"
                "<extra></extra>"
            ),
        )
        fig_ram.update_layout(**PLOTLY_LAYOUT, height=270,
                            xaxis=dict(showgrid=False),
                            yaxis=dict(showgrid=True, gridcolor="#f1f5f9"))
        st.plotly_chart(fig_ram, use_container_width=True)

    st.caption(
        f"Données : {len(df):,} ordinateurs portables · Modèle : Random Forest · MAE ≈ {MAE_EUR:,.0f} € · "
        "Les graphiques servent de contexte marché pour interpréter l'estimation."
    )