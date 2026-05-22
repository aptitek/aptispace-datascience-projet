# Mon Projet Data Science
Étudiant(e) 1 : Dina Chaouki, Étudiant(e) 2 : Cécile Audrée
Demeuni, Étudiant(e) 3 : Aurélie Demure
2026-05-20

### Dashboard interactif

Le dashboard est visible sur ce lien : 

```bash
https://data-science-project-v8hxwnzwhtiperpwernkvr.streamlit.app/
```

Si le lien ne fonctionne pas, vous pouvez visualiser le dashboard localement.

Pour le lancer il faut se placer à la racine du projet puis exécuter :

```bash
pip install requirements.txt
streamlit run dashboard.py
```

L'application s'ouvre dans le navigateur à l'adresse locale :

```bash
http://localhost:8501
```


- [Introduction et Contexte Métier](#sec-intro)
  - [Contexte du Projet](#contexte-du-projet)
  - [Objectif Analytique](#objectif-analytique)
- [Acquisition et Préparation des Données (Data
  Wrangling)](#sec-wrangling)
  - [Chapitre 1 : Acquisition
    Multi-Sources](#chapitre-1--acquisition-multi-sources)
- [📥 Étape 1 : Acquisition des Données & Multi-Sources (Squelette
  Étudiant)](#inbox_tray-étape-1--acquisition-des-données--multi-sources-squelette-étudiant)
  - [Chapitre 2 : Nettoyage et Préparation
    (Wrangling)](#chapitre-2--nettoyage-et-préparation-wrangling)
- [🧹 Étape 2 : Préparation & Nettoyage de Données (Data Wrangling)
  (Squelette
  Étudiant)](#broom-étape-2--préparation--nettoyage-de-données-data-wrangling-squelette-étudiant)
  - [Nettoyage des séries](#nettoyage-des-séries)
- [Visualisation Multidimensionnelle (Insights)](#sec-viz)
  - [Chapitre 3 : Travaux Pratiques d’Exploration
    Visuelle](#chapitre-3--travaux-pratiques-dexploration-visuelle)
- [📊 Étape 4 : Visualisation Multidimensionnelle (Squelette
  Étudiant)](#bar_chart-étape-4--visualisation-multidimensionnelle-squelette-étudiant)
- [Analyse Exploratoire des Données (EDA)](#sec-eda)
  - [Chapitre 4 : Travaux Pratiques d’Exploration
    (EDA)](#chapitre-4--travaux-pratiques-dexploration-eda)
- [🔎 Étape 3 : Analyse Exploratoire des Données (EDA) (Squelette
  Étudiant)](#mag_right-étape-3--analyse-exploratoire-des-données-eda-squelette-étudiant)
- [Modélisation et Apprentissage](#sec-modelling)
  - [Chapitre 5 : Travaux Pratiques de Modélisation (ML &
    DL)](#chapitre-5--travaux-pratiques-de-modélisation-ml--dl)
- [🧠 Étape 5 : Modélisation (Machine Learning & Deep Learning)
  (Squelette
  Étudiant)](#brain-étape-5--modélisation-machine-learning--deep-learning-squelette-étudiant)
- [Évaluation Métrique et Validation](#sec-evaluation)
  - [Chapitre 6 : Travaux Pratiques d’Évaluation &
    Robustesse](#chapitre-6--travaux-pratiques-dévaluation--robustesse)
- [🧪 Étape 6 : Évaluation Métrique & Robustesse (Squelette
  Étudiant)](#test_tube-étape-6--évaluation-métrique--robustesse-squelette-étudiant)
- [Data Storytelling et Communication](#sec-storytelling)
  - [Chapitre 7 : Travaux Pratiques de
    Storytelling](#chapitre-7--travaux-pratiques-de-storytelling)
- [📢 Étape 7 : Data Storytelling & Communication (Squelette
  Étudiant)](#loudspeaker-étape-7--data-storytelling--communication-squelette-étudiant)
  - [Présentation des Résultats (Livrables
    Interactifs)](#présentation-des-résultats-livrables-interactifs)
- [Utilisation de l’Intelligence Artificielle](#sec-ai)
  - [Cartographie de l’utilisation de
    l’IA](#cartographie-de-lutilisation-de-lia)
  - [Principes de Rigueur et
    Responsabilité](#principes-de-rigueur-et-responsabilité)
- [Bibliographie](#bibliographie)

# Introduction et Contexte Métier

Ce projet s’inscrit dans une démarche d’analyse de données appliquée au
marché des ordinateurs portables. Le jeu de données utilisé contient
différentes caractéristiques techniques et commerciales de laptops,
telles que la marque, le type de machine, la taille de l’écran, le
processeur, la mémoire vive, le stockage, le système d’exploitation, le
poids et le prix.

L’objectif principal est d’étudier ces données afin de comprendre les
facteurs qui influencent le prix d’un ordinateur portable. Pour cela, le
projet suivra plusieurs étapes : le nettoyage des données, l’analyse
exploratoire, la visualisation, puis éventuellement la mise en place
d’un modèle prédictif permettant d’estimer le prix d’un ordinateur à
partir de ses caractéristiques.

## Contexte du Projet

Le marché des ordinateurs portables est très concurrentiel et propose
une grande variété de produits. Les prix peuvent varier fortement selon
les composants, la marque ou encore l’usage visé : bureautique, gaming,
professionnel, ultraportable, etc. Pour un consommateur, il n’est pas
toujours simple de comprendre quels éléments justifient réellement un
prix plus élevé.

Dans ce contexte, l’analyse quantitative du jeu de données permet
d’identifier les caractéristiques qui ont le plus d’impact sur le prix.
Elle peut aider à mieux comparer les produits, à comprendre les
tendances du marché et à faciliter la prise de décision. Par exemple, on
peut chercher à savoir si la quantité de RAM, la présence d’un SSD, la
gamme du processeur ou la résolution de l’écran influencent fortement le
prix.

Ce projet soulève donc une problématique métier concrète : comment
exploiter les caractéristiques techniques d’un ordinateur portable pour
comprendre et prédire son prix ? Cette analyse peut être utile à la fois
pour les consommateurs, les revendeurs ou les entreprises souhaitant
positionner leurs produits de manière plus pertinente.

## Objectif Analytique

*À rédiger par les étudiants — Pistes de réflexion :*

- *Quelles sont les variables cibles principales et la tâche globale de
  modélisation (classification, régression, clustering, etc.) ?*
- *Comment le couplage de données multi-sources et l’intégration de
  différents types de données (tabulaires, images, signaux, etc.)
  enrichissent-ils l’analyse ?*
- *Quels sont les livrables analytiques attendus pour répondre à votre
  problématique et guider les prises de décisions ?*

\[Rédiger votre paragraphe d’objectifs ici\]

------------------------------------------------------------------------

# Acquisition et Préparation des Données (Data Wrangling)

Le succès de tout projet de Data Science repose sur la qualité de la
préparation des données ([McKinney 2020](#ref-pandas2020)). Cette
section documente l’audit de qualité et les étapes de nettoyage
appliquées à vos jeux de données bruts.

## Chapitre 1 : Acquisition Multi-Sources

# 📥 Étape 1 : Acquisition des Données & Multi-Sources (Squelette Étudiant)

Cette étape correspond au premier chapitre du pipeline de Data Science.
L’objectif est d’identifier, d’importer et de consolider vos jeux de
données bruts issus de différentes sources (fichiers CSV locaux,
requêtes API, bases de données, etc.).

### 1. Initialisation de l’environnement

### 2. Chargement de la source de données principale

**À COMPLÉTER PAR L’ÉTUDIANT :** Chargez votre jeu de données principal
(par exemple un fichier CSV stocké dans `data/raw/`).

### 3. Intégration de données secondaires (Multi-Sources)

L’analyse se base uniquement sur le dataset principal. Nous n’avons pas
intégré de données secondaires.

### 4. Fusion des sources (Optionnel)

**À COMPLÉTER PAR L’ÉTUDIANT :** Associez vos différentes sources de
données en utilisant des jointures (`pd.merge`) pertinentes.

### 5. Consignation des données d’entrée brutes

Sauvegardez l’état brut de vos données d’entrée pour la suite du
pipeline.

## Chapitre 2 : Nettoyage et Préparation (Wrangling)

# 🧹 Étape 2 : Préparation & Nettoyage de Données (Data Wrangling) (Squelette Étudiant)

Cette étape correspond au deuxième chapitre du projet. L’objectif est
d’effectuer un audit de qualité de vos données brutes, puis de mettre en
œuvre un nettoyage rigoureux à l’aide de votre package personnalisé
`src.data_clean`.

### 1. Initialisation et imports

### 2. Chargement du dataset brut et Audit Initial

**À COMPLÉTER PAR L’ÉTUDIANT :** Chargez les données brutes et inspectez
la qualité du dataset (taux de valeurs manquantes, présence de doublons,
types erronés).

### 3. Uniformisation des Formats de Dates =\> pas de dates dans notre dataset

**À COMPLÉTER PAR L’ÉTUDIANT :** Uniformisez la colonne temporelle pour
la convertir dans un type datetime standardisé via votre module
`src.data_clean`.

### 4. Identification et Filtrage des Valeurs Aberrantes (Outliers)

**À COMPLÉTER PAR L’ÉTUDIANT :** Identifiez les anomalies physiques et
utilisez votre fonction `dc.handle_outliers` pour transformer ces
valeurs aberrantes en NaNs.

### 5. Imputation des valeurs manquantes

**À COMPLÉTER PAR L’ÉTUDIANT :** Appliquez des stratégies d’imputation
adaptées (interpolation temporelle, médiane, etc.) sur les valeurs
manquantes générées ou initiales.

## Nettoyage des séries

### 6. Sauvegarde des données propres

Enregistrez vos données de base nettoyées dans le répertoire
`data/processed/`.

------------------------------------------------------------------------

# Visualisation Multidimensionnelle (Insights)

Nous présentons ici les résultats visuels clés permettant de dégager des
insights exploitables pour les décideurs, en s’appuyant sur notre module
`src/utils_viz.py`.

## Chapitre 3 : Travaux Pratiques d’Exploration Visuelle

# 📊 Étape 4 : Visualisation Multidimensionnelle (Squelette Étudiant)

Cette étape correspond au quatrième chapitre du cours. L’objectif est de
concevoir des représentations visuelles premium pour identifier des
tendances et insights clés à l’aide de votre package personnalisé de
tracé `src.utils_viz`.

### 1. Préparation de l’environnement

### 2. Chargement du dataset enrichi

### 3. Tracés et analyses graphiques

#### A. Distribution des prix

#### B. Répartition des marques

#### C. Répartition des types d’ordinateurs

#### D. Matrice de corrélation

#### E. Prix moyen par marque

#### F. Relation poids / prix

#### G. Relation stockage / prix

------------------------------------------------------------------------

# Analyse Exploratoire des Données (EDA)

Dans cette section, nous analysons les relations statistiques
fondamentales qui régissent votre domaine d’étude au sein du jeu de
données.

## Chapitre 4 : Travaux Pratiques d’Exploration (EDA)

# 🔎 Étape 3 : Analyse Exploratoire des Données (EDA) (Squelette Étudiant)

Cette étape correspond au troisième chapitre du cours. L’objectif est
d’explorer et de résumer les propriétés statistiques fondamentales de
vos données et de réaliser du **Feature Engineering** pour enrichir vos
modèles.

### 1. Préparation de l’environnement

### 2. Chargement des données nettoyées

### 3. Statistiques Descriptives

**À COMPLÉTER PAR L’ÉTUDIANT :** Générez les résumés statistiques
globaux et par groupes/catégories de votre jeu de données.

### 4. Ingénierie de variables (Feature Engineering)

**À COMPLÉTER PAR L’ÉTUDIANT :** Appliquez la fonction
`feature_engineering` de `src.data_clean` pour extraire des indicateurs
temporels de base, et ajoutez d’autres variables dérivées complexes
adaptées à votre problématique.

### 5. Analyse des Corrélations

**À COMPLÉTER PAR L’ÉTUDIANT :** Analysez la matrice des corrélations
des caractéristiques numériques à l’aide de Pandas.

------------------------------------------------------------------------

# Modélisation et Apprentissage

Le pipeline complet intègre à la fois la branche analytique tabulaire
(Machine Learning) et la branche d’analyse visuelle ou de signaux
complexes (Deep Learning CNN) :

``` mermaid
graph TD
    A[Données Brutes Multi-Sources CSV/API] -->|Formatage & Alignement| B(data_clean.clean_dates)
    C[Données Externes Complémentaires] -->|Imputation & Interpolation| D(data_clean.impute_missing_values)
    B & D -->|Gestion Outliers| E[Jeu de données Propre & Fusionné]
    E -->|Extraction Temporelle/Caractéristiques| F[Feature Engineering]
    F -->|Splits Temporels ou Stratifiés| G[Modèle Machine Learning Tabulaire]
    H[Flux Multimédias Réels Images/Signaux] -->|Prétraitement d'images/signaux| I[Réseau Convolutif CNN TensorFlow]
    G -->|Prédictions de la Problématique Métier| J[Livrables & Aide à la Décision]
    I -->|Détection de Motifs Complexes| J
    
    style E fill:#e0f2fe,stroke:#0284c7,stroke-width:2px
    style J fill:#f0fdf4,stroke:#16a34a,stroke-width:2px
    style G fill:#fef3c7,stroke:#d97706,stroke-width:2px
    style I fill:#fef3c7,stroke:#d97706,stroke-width:2px
```

## Chapitre 5 : Travaux Pratiques de Modélisation (ML & DL)

# 🧠 Étape 5 : Modélisation (Machine Learning & Deep Learning) (Squelette Étudiant)

Cette étape correspond au cinquième chapitre du cours. L’objectif est
d’implémenter d’une part un modèle de Machine Learning tabulaire (ex:
RandomForest) et d’autre part un réseau de neurones convolutif (CNN)
sous TensorFlow pour traiter des images ou signaux complexes.

### 1. Préparation de l’environnement

### 2. Modélisation Tabulaire (Machine Learning)

**À COMPLÉTER PAR L’ÉTUDIANT :** Entraînez un modèle d’apprentissage
supervisé (ex: forêt aléatoire) sur les caractéristiques extraites de
votre jeu de données.

### 3. Modélisation Vision / Deep Learning (CNN & TensorFlow)

**À COMPLÉTER PAR L’ÉTUDIANT :** Pour des motifs complexes
(images/signaux), mettez en place un réseau convolutif (Conv2D, Pooling,
Dense) pour classifier ou enrichir vos prédictions.

------------------------------------------------------------------------

# Évaluation Métrique et Validation

## Chapitre 6 : Travaux Pratiques d’Évaluation & Robustesse

# 🧪 Étape 6 : Évaluation Métrique & Robustesse (Squelette Étudiant)

Cette étape correspond au sixième chapitre du cours. L’objectif est de
mettre en place un protocole d’évaluation rigoureux (splits d’évaluation
adaptés) et de calculer les métriques clés de performance pour valider
scientifiquement la qualité de vos modèles.

### 1. Préparation de l’environnement

### 2. Évaluation du modèle Tabulaire

**À COMPLÉTER PAR L’ÉTUDIANT :** Calculez et interprétez les métriques
d’erreur sur vos prédictions (MAE, RMSE, R²).

### 3. Protocole de Validation Croisée (Out-of-Fold / Chronologique)

**À COMPLÉTER PAR L’ÉTUDIANT :** Décrivez et codez (ou documentez) une
stratégie de validation croisée adaptée au comportement temporel de vos
données pour valider la robustesse de votre modèle sans fuite
d’information.

------------------------------------------------------------------------

# Data Storytelling et Communication

## Chapitre 7 : Travaux Pratiques de Storytelling

# 📢 Étape 7 : Data Storytelling & Communication (Squelette Étudiant)

Cette étape correspond au septième et dernier chapitre de data science.
L’objectif est de synthétiser vos résultats pour des profils métiers ou
décideurs et de proposer des visualisations interactives ou dynamiques
pour valoriser vos conclusions.

### 1. Préparation de l’environnement

### 2. Synthèse métier et Storytelling

**À COMPLÉTER PAR L’ÉTUDIANT :** Traduisez vos métriques techniques en
impacts stratégiques (par exemple, gains financiers, réduction de coûts,
amélioration de la sécurité, etc.).

<div id="plotly-21d25383-d98c-4a96-8973-7b94410be571"
style="width:100%; height:400px; background: white; border-radius: 8px;">

</div>

<script type="text/javascript">
  document.addEventListener("DOMContentLoaded", function() {
    if (typeof Plotly !== 'undefined') {
      Plotly.newPlot('plotly-21d25383-d98c-4a96-8973-7b94410be571', [{"type": "scatter", "x": [1, 2, 3], "y": [10, 15, 13], "mode": "lines+markers", "name": "Donn\u00e9es de Test"}], {"title": "Mon Graphique Plotly de Test"}, {"responsive": true});
    } else {
      console.error("Plotly library is not loaded.");
    }
  });
</script>

### 3. Visualisation Interactive (Plotly)

**À COMPLÉTER PAR L’ÉTUDIANT :** Générez un graphique interactif (par
exemple en utilisant Plotly ou des éléments OJS dans le document final)
pour permettre aux décideurs d’interagir dynamiquement avec vos données.

<div id="plotly-16d927b3-73fe-4d45-a3e0-7a0c1567991d"
style="width:100%; height:400px; background: white; border-radius: 8px;">

</div>

<script type="text/javascript">
  document.addEventListener("DOMContentLoaded", function() {
    if (typeof Plotly !== 'undefined') {
      Plotly.newPlot('plotly-16d927b3-73fe-4d45-a3e0-7a0c1567991d', [{"type": "scatter", "x": [1, 2, 3], "y": [10, 15, 13], "mode": "lines+markers", "name": "Donn\u00e9es de Test"}], {"title": "Mon Graphique Plotly de Test"}, {"responsive": true});
    } else {
      console.error("Plotly library is not loaded.");
    }
  });
</script>

## Présentation des Résultats (Livrables Interactifs)

<div class="panel-tabset">

### 📺 Diaporama de Soutenance (RevealJS)

Ci-dessous est intégré le squelette de votre diaporama de soutenance
RevealJS. Utilisez-le pour présenter votre démarche aux décideurs de
façon professionnelle.

<iframe src="slides.html" width="100%" height="500px" style="border: 1px solid #e2e8f0; border-radius: 8px; background: white;">

</iframe>

### 📊 Exemple de Dashboard Dynamique (OJS / Plotly)

Voici un exemple minimal de code montrant comment intégrer un graphique
dynamique contrôlé par un composant d’interface utilisateur en
Observable JS (OJS).

<div style="background: #f8fafc; padding: 1.5rem; border-radius: 8px; border: 1px solid #e2e8f0; margin-bottom: 1.5rem;">
  <div style="margin-bottom: 1rem; font-family: sans-serif;">
    <label for="selectedCategory-select" style="font-weight: 600; margin-right: 0.5rem; color: #1e293b;">Filtrer par Catégorie :</label>
    <select id="selectedCategory-select" style="padding: 0.5rem; border-radius: 4px; border: 1px solid #cbd5e1; background: white; color: #1e293b;">
      <option value="Toutes" selected>Toutes</option>
      <option value="A">A</option>
      <option value="B">B</option>
      <option value="C">C</option>
    </select>
  </div>
  
</div>

<script type="text/javascript">
  document.addEventListener("DOMContentLoaded", function() {
    const data = [
  {timestamp: "2026-05-18T00:00:00Z", value: 10.5, category: "A"},
  {timestamp: "2026-05-18T02:00:00Z", value: 12.1, category: "A"},
  {timestamp: "2026-05-18T04:00:00Z", value: 14.7, category: "A"},
  {timestamp: "2026-05-18T05:00:00Z", value: 15.2, category: "A"},
  {timestamp: "2026-05-18T06:00:00Z", value: 16.0, category: "B"},
  {timestamp: "2026-05-18T07:00:00Z", value: 18.3, category: "B"},
  {timestamp: "2026-05-18T09:00:00Z", value: 21.5, category: "B"},
  {timestamp: "2026-05-18T10:00:00Z", value: 22.0, category: "B"},
  {timestamp: "2026-05-18T12:00:00Z", value: 25.4, category: "C"},
  {timestamp: "2026-05-18T13:00:00Z", value: 26.1, category: "C"},
  {timestamp: "2026-05-18T15:00:00Z", value: 28.9, category: "C"},
  {timestamp: "2026-05-18T16:00:00Z", value: 30.2, category: "C"}
];

    function updatePlot(category) {
      if (typeof Plotly === 'undefined') {
        console.error("Plotly is not loaded");
        return;
      }
      // Boutons de sélection interactifs OJS
      // Données simulées réactives
      // Filtrage réactif de la donnée
      const filteredData = category === "Toutes" 
        ? data 
        : data.filter(d => d.category === category)
      // Tracé interactif avec la librairie Plotly
      Plotly.newPlot('dynamic-chart', [{
        x: filteredData.map(d => d.timestamp),
        y: filteredData.map(d => d.value),
        type: 'scatter',
        mode: 'lines+markers',
        marker: {color: '#1A73E8', size: 8},
        line: {shape: 'spline', color: '#1A73E8', width: 3}
      }], {
        title: 'Évolution Dynamique des Valeurs (Filtrée)',
        margin: {t: 50, b: 50, l: 50, r: 50},
        paper_bgcolor: 'rgba(0,0,0,0)',
        plot_bgcolor: 'rgba(0,0,0,0)',
        xaxis: {gridcolor: '#E5E7EB'},
        yaxis: {gridcolor: '#E5E7EB'}
      })
    }

    const select = document.getElementById("selectedCategory-select");
    if (select) {
      select.addEventListener("change", function(e) {
        updatePlot(e.target.value);
      });
      updatePlot(select.value);
    }
  });
</script>






</div>

------------------------------------------------------------------------

# Utilisation de l’Intelligence Artificielle

Dans une démarche de transparence scientifique et académique, cette
section détaille la manière dont les outils d’Intelligence Artificielle
(IA) générative ont été intégrés tout au long de la réalisation de ce
projet.

## Cartographie de l’utilisation de l’IA

| Outil d’IA | Cas d’usage (Pourquoi ?) | Méthode d’utilisation (Comment ?) | Rôle et Validation Humaine |
|:---|:---|:---|:---|
| **\[Outil d’IA\]** | *\[À compléter par les étudiants\]* | *\[À compléter par les étudiants\]* | *\[À compléter par les étudiants\]* |

## Principes de Rigueur et Responsabilité

1.  **Responsabilité intellectuelle** : L’équipe assume l’entière
    responsabilité des analyses, des choix de modèles et des conclusions
    présentées dans ce rapport.
2.  **Lutte contre les hallucinations** : Chaque suggestion technique a
    fait l’objet d’une validation empirique.
3.  **Protection des données** : Aucun jeu de données confidentiel ou
    sensible n’a été soumis à des modèles tiers en ligne.

------------------------------------------------------------------------

# Bibliographie

<div id="refs" class="references csl-bib-body hanging-indent">

<div id="ref-pandas2020" class="csl-entry">

McKinney, Wes. 2020. *Python for Data Analysis: Data Wrangling with
Pandas, NumPy, and IPython*. O’Reilly Media.

</div>

</div>

<script type="ojs-module-contents">
eyJjb250ZW50cyI6W119
</script>

<div id="exercise-loading-indicator"
class="exercise-loading-indicator d-none d-flex align-items-center gap-2">

<div id="exercise-loading-status" class="d-flex gap-2">

</div>

<div class="spinner-grow spinner-grow-sm">

</div>

</div>

<script type="vfs-file">
W10=
</script>
