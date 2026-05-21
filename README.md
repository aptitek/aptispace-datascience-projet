# Mon Projet Data Science
Étudiant(e) 1 : celia merabet  
Étudiant(e) 2 : Abderrahmane Karim RAKEM   
Étudiant(e) 3 : BOUYABRI Mohamed

2026-05-18

- [Introduction et Contexte Métier](#sec-intro)
  - [Contexte du Projet](#contexte-du-projet)
  - [Objectif Analytique](#objectif-analytique)
- [Acquisition et Préparation des Données (Data Wrangling)](#sec-wrangling)
  - [Audit de Qualité](#audit-de-qualité)
  - [Algorithme de Nettoyage](#algorithme-de-nettoyage)
  - [Travaux Pratiques de Wrangling](#travaux-pratiques-de-wrangling)
- [🧹 Jalon 1 : Data Wrangling & Nettoyage (Squelette Étudiant)](#broom-jalon-1--data-wrangling--nettoyage-squelette-étudiant)
- [Analyse Exploratoire des Données (EDA)](#sec-eda)
  - [Statistiques Descriptives](#statistiques-descriptives)
  - [Ingénierie de Variables (Feature Engineering)](#ingénierie-de-variables-feature-engineering)
  - [Travaux Pratiques d'Exploration Visuelle (EDA)](#travaux-pratiques-dexploration-visuelle-eda)
- [📊 Jalon 1 : Analyse Exploratoire des Données (EDA) & Visualisation (Squelette Étudiant)](#bar_chart-jalon-1--analyse-exploratoire-des-données-eda--visualisation-squelette-étudiant)
- [Visualisation Multidimensionnelle (Insights)](#sec-viz)
  - [Profils et Distributions Caractéristiques](#profils-et-distributions-caractéristiques)
  - [Corrélations Globales](#corrélations-globales)
- [Modélisation et Apprentissage](#sec-modelling)
  - [Schéma Global du Pipeline de Données](#schéma-global-du-pipeline-de-données)
  - [Modélisation Tabulaire (Machine Learning)](#modélisation-tabulaire-machine-learning)
- [🧠 Jalon 2 : Modélisation Prédictive & Apprentissage (Squelette Étudiant)](#brain-jalon-2--modélisation-prédictive--apprentissage-squelette-étudiant)
  - [Modélisation Vision / Deep Learning (Analyse d'Images ou Signaux)](#modélisation-vision--deep-learning-analyse-dimages-ou-signaux)
- [📷 Jalon 2 : Brique de Vision par Ordinateur (CNN & TensorFlow) (Squelette Étudiant)](#camera-jalon-2--brique-de-vision-par-ordinateur-cnn--tensorflow-squelette-étudiant)
- [Évaluation Métrique et Validation](#sec-evaluation)
  - [Stratégie de Validation](#stratégie-de-validation)
  - [Résultats et Interprétation](#résultats-et-interprétation)
- [Data Storytelling et Communication](#sec-storytelling)
  - [Recommandations Stratégiques / Métier](#recommandations-stratégiques--métier)
  - [Limites et Perspectives](#limites-et-perspectives)
- [Bibliographie](#bibliographie)

# Introduction et Contexte Métier

[![](https://github.com/aptitek/aptispace-datascience-projet/actions/workflows/ci.yml/badge.svg)](https://github.com/aptitek/aptispace-datascience-projet/actions/workflows/ci.yml)

<<<<<<< HEAD
Ce projet de Data Science s’inscrit dans le domaine de l’analyse immobilière prédictive.
L’objectif est de comprendre et prédire les prix de biens immobiliers à partir de données hétérogènes.

Dans un marché immobilier complexe et non linéaire, les prix dépendent de nombreux facteurs :

caractéristiques physiques du bien
localisation géographique
qualité globale
facteurs visuels (images)

L’enjeu principal est donc de construire un pipeline complet de Data Science permettant :

d’explorer les données
de les nettoyer
de les analyser
de construire des modèles prédictifs
d’aider à la prise de décision

## Contexte du Projet

Ce projet vise à appliquer la Data Science au marché immobilier, domaine clé pour les investisseurs, agences et particuliers.

Les données utilisées combinent :

données tabulaires (surface, pièces, qualité)
données catégorielles (quartiers, type de bien)
données visuelles (images de logements)

📌 Le but est de modéliser un système intelligent capable de prédire les prix immobiliers de manière fiable.
=======
*À rédiger par les étudiants : Présentez ici le contexte global de votre projet, la problématique métier que vous cherchez à résoudre, les questions scientifiques soulevées et les opportunités d'aide à la décision sur la base de vos données.*

## Contexte du Projet

*À rédiger par les étudiants — Pistes de réflexion :* - *Quels sont les objectifs globaux et le domaine d'étude de votre projet ?* - *En quoi ce sujet de recherche est-il pertinent et stratégique ?* - *Pourquoi l'analyse quantitative de ce jeu de données est-elle indispensable pour répondre à votre problématique ?*

Ce projet s'inscrit dans une problématique de Data Science appliquée au marché immobilier, un domaine où l'analyse de données joue un rôle clé dans la prise de décision des particuliers, agences et investisseurs.

L'objectif général est de comprendre et prédire les prix des logements à partir de plusieurs sources de données :

caractéristiques tabulaires (surface, localisation, nombre de pièces, etc.),
données contextuelles issues de plateformes immobilières,
et éventuellement données visuelles (images de logements).

Dans un contexte de marché immobilier fortement hétérogène, les prix peuvent varier de manière importante en fonction de critères complexes et non linéaires. L'analyse quantitative permet donc de :

objectiver les facteurs influençant les prix,
détecter des patterns cachés dans les données,
et construire des modèles prédictifs fiables
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

## Dataset

- House Prices – Advanced Regression (Kaggle)
- https://www.kaggle.com/competitions/house-prices-advanced-regression-techniques

## Objectif Analytique

<<<<<<< HEAD
L’objectif principal est de construire un modèle de régression permettant de prédire le prix d’un bien immobilier (SalePrice).

Nous cherchons à :
=======
*À rédiger par les étudiants — Pistes de réflexion :* - *Quelles sont les variables cibles principales et la tâche globale de modélisation (classification, régression, clustering, etc.) ?* - *Comment le couplage de données multi-sources et l'intégration de différents types de données (tabulaires, images, signaux, etc.) enrichissent-ils l'analyse ?* - *Quels sont les livrables analytiques attendus pour répondre à votre problématique et guider les prises de décisions ?*

L'objectif principal du projet est de construire un modèle prédictif de régression capable d'estimer le prix d'un bien immobilier.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

prédire les prix de logements
identifier les variables les plus influentes
comparer plusieurs modèles ML
intégrer une approche Deep Learning (CNN)

<<<<<<< HEAD
📦 Approche multimodale :

tabulaire (ML classique)
images (CNN TensorFlow)

=======
prédire la variable cible : prix du logement
analyser les variables explicatives (surface, localisation, équipements…)
comparer plusieurs modèles de Machine Learning supervisé
intégrer, si possible, une dimension Deep Learning (CNN) sur des images de logements afin d'enrichir les prédictions

Le projet suit une approche multimodale, combinant :

données tabulaires structurées,
données non structurées (images),
et modèles d'apprentissage automatique avancés.

Les livrables attendus sont :

un pipeline complet de Data Science,
un modèle prédictif performant,
un dashboard interactif d'aide à la décision.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

------------------------------------------------------------------------

# Acquisition et Préparation des Données (Data Wrangling)

<<<<<<< HEAD
## Audit de Qualité

Lors de l’exploration initiale, plusieurs problèmes ont été identifiés :

valeurs manquantes dans plusieurs colonnes
incohérences de formats (dates, prix)
outliers extrêmes dans les prix immobiliers
variables catégorielles non normalisées
doublons issus de sources multiples

👉 Un nettoyage rigoureux est nécessaire pour garantir la qualité des modèles.

## Algorithme de Nettoyage

Le pipeline de nettoyage comprend :
=======
Le succès de tout projet de Data Science repose sur la qualité de la préparation des données ([McKinney 2020](#ref-pandas2020)). Cette section documente l'audit de qualité et les étapes de nettoyage appliquées à vos jeux de données bruts.

## Audit de Qualité

*À rédiger par les étudiants : Présentez un audit critique complet de vos fichiers de données brutes. Indiquez la liste des anomalies physiques et typologiques détectées (formats de dates hétérogènes, outliers physiques, taux de valeurs manquantes, etc.).*

Le dataset principal House Prices contient 1 460 biens immobiliers et 81 variables initiales. L'audit initial a permis d'identifier les anomalies suivantes :

Valeurs manquantes importantes : PoolQC (1 453 manquants sur 1 460, soit 99.5%), MiscFeature (1 406), Alley (1 369), Fence (1 179), MasVnrType (872), FireplaceQu (690). Ces colonnes sont quasi-vides et nécessitent une stratégie d'imputation adaptée.

Valeurs manquantes modérées : LotFrontage (259 manquants), GarageFinish, GarageCond, GarageYrBlt, GarageQual, GarageType (81 manquants chacun), BsmtExposure (38), BsmtQual (37).

Outliers sur la variable cible SalePrice : 61 valeurs aberrantes détectées aux percentiles extrêmes (1% et 99%), représentant des biens atypiques pouvant biaiser le modèle.

Aucun doublon détecté dans le dataset (0 lignes dupliquées).

Un jeu de données secondaire a été créé manuellement pour enrichir l'analyse, associant chaque quartier (Neighborhood) à une catégorie de zone (Standard, Premium, Luxury) et à un coefficient multiplicateur.

## Algorithme de Nettoyage

*À rédiger par les étudiants : Justifiez et détaillez l'enchaînement de vos opérations de traitement (uniformisation des dates, masquage des outliers, imputation, etc.). Faites référence aux fonctions correspondantes de votre module `src/data_clean.py`.*
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

Uniformisation des formats numériques
Conversion des dates en datetime standard
Imputation des valeurs manquantes :
médiane (numérique)
mode (catégoriel)
Traitement des outliers (IQR / clipping)
Encodage des variables catégorielles :
One-Hot Encoding
Label Encoding
Standardisation des variables numériques

<<<<<<< HEAD
Objectif : rendre les données exploitables pour le Machine Learning.

=======
### Fusion multi-sources :

Le dataset principal (1 460 lignes, 81 colonnes) a été fusionné avec le dataset secondaire de zones via une jointure sur la colonne Neighborhood, produisant un dataset enrichi de 83 colonnes.

### Traitement des valeurs manquantes :

imputation par médiane pour les variables numériques (LotFrontage, GarageYrBlt, MasVnrArea, etc.)
imputation par la valeur "Unknown" pour les variables catégorielles (Alley, PoolQC, Fence, MiscFeature, etc.)

### Gestion des outliers sur SalePrice :

suppression des valeurs extrêmes situées en dehors de l'intervalle [percentile 1%, percentile 99%], soit 61 biens atypiques remplacés par NaN puis réimpeutés par la médiane.

### Feature Engineering :
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

création de HouseAge = YrSold - YearBuilt pour capturer la dépréciation du bien
création de LogSalePrice = log(1 + SalePrice) pour normaliser la distribution asymétrique des prix
création de LogArea = log(1 + LotArea) pour normaliser la surface du terrain

## Travaux Pratiques de Wrangling

# 🧹 Jalon 1 : Data Wrangling & Nettoyage 

<<<<<<< HEAD
Ce notebook constitue la première étape du projet de Data Science. L’objectif est de transformer un jeu de données brut en un dataset propre, exploitable pour la modélisation. Cette étape est critique car elle conditionne directement la qualité des modèles prédictifs.
=======
Ce notebook correspond à la première étape du **Jalon 1**. L'objectif est d'importer le jeu de données brut (`data/raw/raw_data_sample.csv`), d'effectuer un audit de sa qualité (données manquantes, anomalies physiques, formats de dates hétérogènes) et de le nettoyer à l'aide de votre package personnalisé `src.data_clean`.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

### 1. Importation des packages et chargement des données

On commence par importer les librairies nécessaires ainsi que le dataset brut.

import os
import pandas as pd
import numpy as np

# Chargement du dataset brut
data_path = os.path.join("data", "raw", "raw_data_sample.csv")
df = pd.read_csv(data_path)

print("Dataset chargé :", df.shape)
df.head()


### 2. Audit initial des données

<<<<<<< HEAD
L’objectif ici est de comprendre la structure du dataset avant tout traitement.

# Dimensions
print("Dimensions :", df.shape)

# Types de données
print(df.dtypes)

# Valeurs manquantes
missing = df.isnull().mean() * 100
print("Taux de valeurs manquantes (%) :")
print(missing.sort_values(ascending=False))

# Doublons
print("Nombre de doublons :", df.duplicated().sum())

Observations attendues :

Présence possible de valeurs manquantes sur les variables numériques
Colonnes de type object nécessitant conversion
Doublons potentiels liés à la collecte multi-sources

### 3. Nettoyage et uniformisation des Dates

On standardise la colonne temporelle pour garantir une analyse cohérente.

from src.data_clean import clean_dates

df = clean_dates(df, column="timestamp")

print(df["timestamp"].dtype)

Objectif :

Uniformiser les formats de dates
Permettre des analyses temporelles fiables


### 4. Identification et Traitement des Outliers (Anomalies physiques)

On élimine les valeurs aberrantes dans la variable cible.

from src.data_clean import handle_outliers

df = handle_outliers(df, column="value", lower=0, upper=100)

print("Outliers traités")

 Objectif :

Supprimer les valeurs incohérentes
Stabiliser les distributions

### 5. Imputation des valeurs manquantes

On remplit les valeurs manquantes restantes.

from src.data_clean import impute_missing_values

df = impute_missing_values(df)

print("Valeurs manquantes traitées")

Stratégie :

Médiane pour variables numériques
Mode pour variables catégorielles


### 6. Sauvegarde des données propres

output_path = os.path.join("data", "processed", "cleaned_data_sample.csv")
df.to_csv(output_path, index=False)

print("Dataset nettoyé sauvegardé :", output_path)

=======
Le dataset brut contient 1 460 lignes et 81 colonnes. L'audit révèle 0 doublon et de nombreuses valeurs manquantes sur les variables liées au garage, à la cave et aux équipements optionnels (piscine, allée). Les colonnes PoolQC, MiscFeature et Alley sont quasi-vides (plus de 90% de valeurs manquantes).

### 3. Nettoyage et uniformisation des Dates

Le dataset House Prices ne contient pas de colonne timestamp. Les variables temporelles utilisées sont YearBuilt (année de construction) et YrSold (année de vente), toutes deux en format numérique et ne nécessitant pas de conversion.

### 4. Identification et Traitement des Outliers (Anomalies physiques)

61 outliers ont été détectés sur la variable SalePrice via la méthode des percentiles (1% - 99%). Ces valeurs extrêmes correspondent à des biens atypiques (très bon marché ou extrêmement chers) pouvant dégrader la qualité du modèle prédictif.

### 5. Imputation des valeurs manquantes

Les valeurs manquantes numériques ont été remplacées par la médiane de chaque colonne. Les valeurs manquantes catégorielles ont été remplacées par "Unknown" pour conserver toutes les lignes du dataset sans perte d'information.

### 6. Sauvegarde des données propres

Le DataFrame nettoyé (1 460 lignes, 85 colonnes après feature engineering) a été sauvegardé dans `data/processed/cleaned_data_sample.csv`.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

------------------------------------------------------------------------

# Analyse Exploratoire des Données (EDA)

Dans cette section, nous analysons les relations statistiques fondamentales qui régissent votre domaine d'étude au sein du jeu de données.

## Statistiques Descriptives

<<<<<<< HEAD
On analyse les tendances générales des données nettoyées.

df.describe()

Analyse :

Distribution des variables numériques
Détection de valeurs extrêmes résiduelles
Compréhension des ordres de grandeur

## Ingénierie de Variables (Feature Engineering)

L’objectif est de créer des variables plus informatives pour améliorer la performance des modèles.

 Exemples :

hour : extraction de l’heure depuis timestamp
dayofweek : capture des effets hebdomadaires
variables cycliques pour gérer la périodicité

 Impact :

Amélioration de la capacité prédictive
Capture des patterns temporels cachés
Réduction de la non-linéarité du problème

=======
*À rédiger par les étudiants : Présentez une vue d'ensemble descriptive rapide de vos variables nettoyées.*

Le dataset nettoyé contient 1 460 biens immobiliers et 85 variables (après feature engineering). Les statistiques descriptives de la variable cible SalePrice révèlent :

- Prix moyen : 179 914 $
- Prix médian : 163 000 $
- Écart-type : 73 992 $
- 61 outliers détectés et traités

La distribution des prix est asymétrique vers la droite, confirmant l'intérêt de la transformation logarithmique. L'analyse par zone de marché montre des écarts significatifs : les biens en zone FV (Floating Village Residential) atteignent un prix moyen de 214 014 $, contre seulement 82 768 $ en zone commerciale C(all).

## Ingénierie de Variables (Feature Engineering)

*À rédiger par les étudiants : Expliquez l'intérêt mathématique et l'impact sur les modèles prédictifs d'extraire des caractéristiques dérivées (ex: variables cycliques temporelles, ratios financiers, ratios physiques, etc.).*

Trois variables dérivées ont été créées pour enrichir le dataset :
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

HouseAge (âge du bien au moment de la vente) : calculée comme YrSold - YearBuilt. Cette variable capture la dépréciation naturelle du bien. Par exemple, un bien construit en 1985 et vendu en 2008 a un HouseAge de 23 ans.

LogSalePrice (transformation logarithmique du prix) : la distribution brute des prix étant fortement asymétrique, la transformation logarithmique la normalise et améliore la stabilité des modèles de régression.

LogArea (transformation logarithmique de la surface du terrain) : même logique que LogSalePrice, la surface du terrain présente une distribution très étalée vers les grandes valeurs.

Par ailleurs, un coefficient de zone (coef_multiplicateur) a été créé à partir de la variable Neighborhood, avec des coefficients variant de 1.0 (Standard) à 1.5 (Luxury).

## Travaux Pratiques d'Exploration Visuelle (EDA)

# 📊 Jalon 1 : Analyse Exploratoire des Données (EDA) & Visualisation (Squelette Étudiant)

<<<<<<< HEAD
## 1. Importation et configuration

import matplotlib.pyplot as plt
import seaborn as sns

from src.data_clean import feature_engineering
from src.utils_viz import (
    plot_generic_trends,
    plot_correlation_matrix,
    plot_bivariate_scatter
)
=======
Ce notebook est dédié à la découverte de relations clés et à l'analyse visuelle de nos données. À partir du jeu de données propre généré précédemment, nous allons enrichir nos variables explicatives et appeler les fonctions de notre module de visualisation `src.utils_viz` pour générer des graphiques professionnels.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712


### 2. Ingénierie de variables

<<<<<<< HEAD
df = feature_engineering(df, column="timestamp")
df.head()

=======
Les variables HouseAge et LogArea ont été créées à partir des variables brutes YearBuilt, YrSold et LotArea pour enrichir le dataset avec des caractéristiques plus informatives pour les modèles prédictifs.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

### 3. Visualisations Professionnelles

#### A. Distribution des prix de vente

<<<<<<< HEAD
plot_generic_trends(df, x="timestamp", y="value")

Insight :

Mise en évidence des variations temporelles globales

#### B. Matrice de corrélation multi-variables

plot_correlation_matrix(df[['value', 'hour', 'dayofweek']])

Insight :

Identification des relations linéaires entre variables
=======
La distribution des prix présente une asymétrie positive marquée avec un pic autour de 150 000 $. La longue queue vers la droite justifie l'utilisation d'une transformation logarithmique avant modélisation.

#### B. Matrice de corrélation multi-variables

Les corrélations les plus fortes avec SalePrice sont OverallQual (r = 0.808), LogArea (r = 0.704), GrLivArea (r = 0.703), GarageCars (r = 0.659) et TotalBsmtSF (r = 0.617).
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

#### C. Relation surface habitable / prix

<<<<<<< HEAD
plot_bivariate_scatter(df, x="hour", y="value", hue="dayofweek")

Insight :

Observation des comportements horaires différents selon les jours


### 4. Synthèse des observations clés

Résumé des insights :

Existence de patterns horaires significatifs
Variations hebdomadaires visibles
Corrélations faibles mais exploitables entre variables temporelles
=======
Le nuage de points Surface vs Prix révèle une relation positive claire : les grandes surfaces ont globalement des prix plus élevés, mais avec une forte dispersion indiquant que d'autres facteurs (qualité, localisation) jouent un rôle important.

### 4. Synthèse des observations clés

Les 5 insights majeurs identifiés lors de l'EDA sont les suivants :

La qualité de construction est le facteur le plus corrélé au prix (r = 0.808). Un bien noté 10/10 vaut en moyenne 4 fois plus qu'un bien noté 2/10.

La surface habitable est le deuxième facteur clé (r = 0.703). Chaque 100 sqft supplémentaires correspond en moyenne à une augmentation de prix de 10 000 $.

La localisation par zone de marché crée des écarts de prix significatifs : la zone FV affiche un prix moyen 2.6 fois supérieur à la zone commerciale C(all).

L'âge du bien a un impact négatif modéré sur le prix : les biens récents (HouseAge < 10 ans) valent en moyenne 30% de plus que les biens anciens (HouseAge > 50 ans).

La capacité du garage est fortement corrélée au prix (r = 0.659), reflétant le lien entre standing du bien et équipements associés.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

------------------------------------------------------------------------

# Visualisation Multidimensionnelle (Insights)

<<<<<<< HEAD
## Profils et distributions

 Les distributions montrent :

Une concentration autour de valeurs centrales
Quelques valeurs extrêmes résiduelles
Une variabilité modérée du signal

## Corrélations globales

Analyse :

Corrélation positive faible entre heure et valeur
Influence modérée du jour de la semaine
Structure globale non linéaire
=======
Nous présentons ici les résultats visuels clés permettant de dégager des insights exploitables pour les décideurs, en s'appuyant sur notre module `src/utils_viz.py`.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

## Profils et Distributions Caractéristiques

La distribution des prix de vente montre une asymétrie positive marquée avec un prix médian de 163 000 $ et un prix moyen de 179 914 $. L'écart entre moyenne et médiane (+16 914 $) confirme l'influence de quelques biens très chers sur la moyenne. Cette observation justifie l'utilisation de la médiane comme statistique de référence pour les estimations immobilières et l'application de la transformation logarithmique avant modélisation.

## Corrélations Globales

La matrice de corrélation révèle quatre variables numériques particulièrement prédictives du prix de vente : OverallQual (r = 0.808), GrLivArea (r = 0.703), GarageCars (r = 0.659) et TotalBsmtSF (r = 0.617). Ces quatre variables constituent le socle des features retenues pour le modèle RandomForest. On note également une forte corrélation entre GarageArea et GarageCars (r > 0.85), signe de multicolinéarité : nous avons retenu GarageCars comme variable plus interprétable.

------------------------------------------------------------------------

# Modélisation et Apprentissage

## Schéma Global du Pipeline de Données

<<<<<<< HEAD
Le pipeline de modélisation du projet repose sur une architecture hybride combinant :
=======
Le pipeline complet intègre à la fois la branche analytique tabulaire (Machine Learning) et la branche d'analyse visuelle ou de signaux complexes (Deep Learning CNN) : 
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

une branche tabulaire (Machine Learning supervisé) pour la prédiction des prix
une branche image (Deep Learning CNN) pour l’analyse visuelle des biens immobiliers

Cette approche multimodale permet de capturer à la fois les facteurs quantitatifs et qualitatifs influençant la valeur d’un bien.



```mermaid
graph TD

    A[Données Brutes Multi-Sources CSV / API] -->|Nettoyage dates| B[clean_dates()]
    C[Données Externes Complémentaires] -->|Imputation| D[impute_missing_values()]

    B --> E[Dataset Nettoyé]
    D --> E

    E --> F[Feature Engineering]
    F --> G[Dataset final structuré]

    G --> H[Train/Test Split]

    H --> I[Modèle ML Tabulaire<br/>RandomForest / XGBoost]
    H --> J[Prétraitement Images]

    J --> K[CNN TensorFlow / Keras]

    I --> L[Prédictions Prix Immobilier]
    K --> L

    L --> M[Aide à la Décision / Dashboard / Reporting]

    style E fill:#e0f2fe,stroke:#0284c7,stroke-width:2px
    style G fill:#fef3c7,stroke:#d97706,stroke-width:2px
    style I fill:#fde68a,stroke:#b45309,stroke-width:2px
    style K fill:#fde68a,stroke:#b45309,stroke-width:2px
    style M fill:#dcfce7,stroke:#16a34a,stroke-width:2px
```


## Modélisation Tabulaire (Machine Learning)

Objectif

Prédire le prix de vente des biens immobiliers à partir de variables structurées.

## Choix du modèle

Nous avons retenu un RandomForestRegressor pour plusieurs raisons :

robustesse face aux outliers et aux données bruitées
capacité à modéliser des relations non-linéaires complexes
bonne performance sans besoin de normalisation stricte
interprétabilité via l’importance des variables

## Variables explicatives utilisées

Les features sélectionnées sont :

GrLivArea : surface habitable
OverallQual : qualité globale du bien
HouseAge : ancienneté du logement
GarageCars : capacité du garage
TotalBsmtSF : surface du sous-sol
coef_multiplicateur : niveau de zone (standard / premium / luxe)


### Protocole d'apprentissage

Split : 80% entraînement / 20% test
random_state = 42 (reproductibilité)
200 arbres dans la forêt
profondeur max = 15

Objectif : limiter le surapprentissage tout en conservant une bonne capacité de généralisation.

### Résultats obtenus

MAE : 20 700 $
RMSE : 35 058 $
R² : 0.7334

 Interprétation :

Le modèle explique environ 73% de la variance des prix, ce qui constitue une performance solide pour un premier modèle de régression immobilière.

### Importance des variables

Classement des variables selon leur impact :

OverallQual → 57%
GrLivArea → 19%
TotalBsmtSF → 13%
HouseAge → 7%
GarageCars → 3%
coef_multiplicateur → < 1%

 Insight principal :

La qualité globale du bien (OverallQual) est le facteur dominant, bien plus influent que la surface seule. Cela montre que la perception qualitative prime sur les dimensions physiques dans la formation des prix immobiliers.

### Travaux Pratiques de Modélisation Tabulaire

# 🧠 Jalon 2 : Modélisation Prédictive & Apprentissage (Squelette Étudiant)

<<<<<<< HEAD
Dans ce notebook du Jalon 2, l’objectif est de mettre en place un pipeline complet d’apprentissage supervisé afin de prédire une variable cible (value) à partir de données structurées.

L’approche respecte une logique scientifique stricte afin d’éviter toute fuite de données (data leakage) et garantir la reproductibilité des résultats.
=======
Dans ce notebook du **Jalon 2**, l'objectif est d'implémenter un pipeline complet d'apprentissage supervisé pour prédire une variable cible (`SalePrice`) à l'aide de Scikit-Learn.

### 1. Préparation de l'environnement
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

### 2. Définition des variables et split train/test

<<<<<<< HEAD
Import des librairies nécessaires à la modélisation et à l’évaluation :

import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


### 2. Définition des variables et split chronologique

L’objectif est de séparer les données de manière temporelle afin de respecter la causalité.

# Exemple de features
features = ["hour", "dayofweek"]
target = "value"

df_ml = df[features + [target]].dropna()

# Split chronologique (important)
train_size = int(len(df_ml) * 0.8)

train = df_ml.iloc[:train_size]
test = df_ml.iloc[train_size:]

X_train = train[features]
y_train = train[target]

X_test = test[features]
y_test = test[target]

Pourquoi ?

éviter la fuite d’information future
simuler un cas réel de prédiction temporelle

### 3. Entraînement du modèle de Forêt Aléatoire

model = RandomForestRegressor(
    n_estimators=200,
    max_depth=15,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

### 4. Évaluation métrique

On évalue la performance du modèle avec trois métriques standards.

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("MAE :", mae)
print("RMSE :", rmse)
print("R² :", r2)

Interprétation :

MAE → erreur moyenne absolue
RMSE → pénalise les grosses erreurs
R² → qualité globale d’explication du modèle


### 5. Importance des variables explicatives

import pandas as pd

importance = pd.DataFrame({
    "feature": features,
    "importance": model.feature_importances_
}).sort_values(by="importance", ascending=False)

print(importance)

Insight :
Permet de comprendre quelles variables influencent le plus la prédiction.


## Modélisation Vision / Deep Learning (Analyse d’Images ou Signaux)

Objectif

Construire un modèle de Deep Learning capable de classifier des biens immobiliers en trois catégories :
=======
Les 6 features retenues sont GrLivArea, OverallQual, HouseAge, GarageCars, TotalBsmtSF et coef_multiplicateur. La cible est SalePrice. Le split 80/20 produit 1 168 observations en entraînement et 292 en test.

### 3. Entraînement du modèle de Forêt Aléatoire

Le RandomForestRegressor est entraîné avec 200 arbres, une profondeur maximale de 15 et n_jobs=-1 pour utiliser tous les cœurs CPU disponibles.

### 4. Évaluation métrique

MAE : 20 700 $ — RMSE : 35 058 $ — R² : 0.7334

### 5. Importance des variables explicatives

OverallQual domine avec 57% d'importance, suivi de GrLivArea (19%) et TotalBsmtSF (13%).

## Modélisation Vision / Deep Learning (Analyse d'Images ou Signaux)
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

économique
moyenne
luxe

à partir d’images uniquement.

## Dataset utilisé

Kaggle : House Prices and Images SoCal
15 000 images disponibles
échantillon utilisé : 1 000 images
taille : 128×128 pixels
normalisation : [0,1]

## Création des classes : 

Basé sur les quantiles :

< 280k → économique
280k – 550k → moyen

550k → luxe

<<<<<<< HEAD
 Objectif : équilibrer les classes pour éviter les biais.

## Architecture du CNN :
=======
### Architecture du CNN
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

Conv2D(32) → MaxPooling
Conv2D(64) → MaxPooling
Conv2D(128) → MaxPooling
Flatten
Dense(128, ReLU)
Dropout(0.3)
Dense(3, Softmax)

📌 Total : ~3.3M paramètres

## Entraînement

Optimiseur : Adam
Loss : sparse_categorical_crossentropy
Époques : 10
Batch size : 32
Validation split : 20%

Résultats :

Accuracy test : 52.5%
Baseline random : 33%
Gain : +58% vs hasard
Classe luxe : 67% précision

## Interprétation :
Le modèle détecte particulièrement bien les biens de luxe grâce à des signaux visuels forts (architecture, finition, jardin, etc.).

<<<<<<< HEAD
 Limites
=======
Le CNN identifie particulièrement bien les biens de luxe (67% de précision), ce qui démontre que l'aspect visuel capture efficacement le standing du bien.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

surapprentissage (86% train vs 52% test)
dataset trop petit
sensibilité au bruit des images

## Perspectives

augmentation des données
data augmentation (rotation, flip, zoom)
transfer learning (MobileNetV2 / ResNet50)
filtrage des images bruitées

<<<<<<< HEAD

=======
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712
### Travaux Pratiques de Vision par Ordinateur (CNN)

# 📷 Jalon 2 : Brique de Vision par Ordinateur (CNN & TensorFlow) (Squelette Étudiant)

<<<<<<< HEAD

## 1. Préparation

Import TensorFlow et préparation environnement :

import tensorflow as tf
from tensorflow.keras import layers, models

## 2.  Génération des images synthétiques

Dataset artificiel :

cercle vs rectangles
64×64 pixels

## 3. Split train/validation
from sklearn.model_selection import train_test_split
=======
Ce notebook est dédié à la brique d'analyse d'images du **Jalon 2**. L'objectif est de concevoir un Réseau de Neurones Convolutif (CNN) sous TensorFlow/Keras pour classifier les biens immobiliers en trois catégories de prix à partir de leurs photographies.

### 1. Préparation de l'environnement

### 2. Chargement des images

1 000 images de maisons californiennes issues du dataset SoCal ont été chargées, redimensionnées à 128x128 pixels et normalisées entre 0 et 1.

### 3. Split d'évaluation (Entraînement / Validation)

800 images pour l'entraînement et 200 images pour le test, avec stratification par catégorie de prix.

### 4. Conception de l'architecture du CNN

Réseau convolutif séquentiel Keras comprenant 3 blocs Conv2D + MaxPooling2D, une couche Flatten, un Dropout 30%, une Dense 128 et une sortie softmax à 3 neurones.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

X_train, X_val, y_train, y_val = train_test_split(
    X_images,
    y_labels,
    test_size=0.2,
    random_state=42
)

<<<<<<< HEAD
## 4.  Modèle CNN
model = models.Sequential([
    layers.Conv2D(32, (3,3), activation="relu", input_shape=(64,64,3)),
    layers.MaxPooling2D(),
=======
Le modèle est compilé avec Adam et sparse_categorical_crossentropy. Entraînement sur 10 époques. Accuracy finale : 52.5% sur le test set.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

    layers.Conv2D(64, (3,3), activation="relu"),
    layers.MaxPooling2D(),

    layers.Flatten(),
    layers.Dense(128, activation="relu"),
    layers.Dropout(0.3),
    layers.Dense(1, activation="sigmoid")
])


<<<<<<< HEAD
## 5.  Compilation & entraînement
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"]
)

model.fit(X_train, y_train, epochs=5, validation_data=(X_val, y_val))
=======
Le découpage d'évaluation retenu est un split aléatoire 80/20 (train/test) avec un random_state fixé à 42 pour garantir la reproductibilité des résultats.

Ce choix est adapté à la structure de nos données pour deux raisons. Premièrement, le dataset House Prices ne présente pas de structure temporelle stricte nécessitant un split chronologique : les transactions immobilières couvrent plusieurs années (2006-2010) sans dépendance séquentielle forte entre les observations. Deuxièmement, le split aléatoire garantit une distribution similaire des prix entre train et test, évitant ainsi les fuites de données.

Pour le modèle CNN, un split identique 80/20 a été appliqué sur les 1 000 images, avec stratification par catégorie de prix pour garantir une représentation équilibrée des trois classes dans chaque ensemble.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

## Évaluation et validation

<<<<<<< HEAD
Stratégie de validation :

La stratégie choisie dépend de la structure des données :

données temporelles → split chronologique
images → split stratifié
objectif → éviter toute fuite d’information
=======
*À rédiger par les étudiants : Complétez le tableau d'évaluation ci-dessous en reportant vos résultats de modélisation.*

| Modèle | Métrique 1 (MAE / Précision) | Métrique 2 (RMSE / F1-Score) | R² / Score (%) |
|---|---|---|---|
| Baseline (prédiction par la moyenne) | 57 543 $ | 73 992 $ | 0.00% |
| **Random Forest Regressor** | **20 700 $** | **35 058 $** | **73.34%** |
| **CNN Classification (3 classes)** | **Précision : 55%** | **F1-Score macro : 0.52** | **Accuracy : 52.5%** |

Le Random Forest Regressor surpasse largement la baseline en réduisant l'erreur absolue moyenne de 57 543 $ à 20 700 $, soit une réduction de 64%. Le R² de 0.73 indique que le modèle explique 73% de la variance des prix, ce qui constitue un résultat solide avec seulement 6 features.

Le CNN de classification atteint 52.5% d'accuracy sur 3 classes, soit 58% au-dessus du hasard pur (33%). Cette performance confirme que les caractéristiques visuelles des biens immobiliers contiennent des informations discriminantes, même si les features tabulaires restent dominantes pour la prédiction précise des prix.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

 Justification :

Cette approche garantit une évaluation réaliste des performances en conditions réelles.

## Résultats et interprétation

<<<<<<< HEAD
Modèle	Métrique 1	Métrique 2	Score
Baseline	MAE élevé	RMSE élevé	R² faible
Random Forest	MAE faible	RMSE moyen	R² ≈ 0.73
CNN	Accuracy 52.5%	Loss stable	+58% vs hasard

Interprétation :
=======
*À rédiger par les étudiants : Formulez des recommandations stratégiques, opérationnelles et innovantes basées sur vos découvertes analytiques et prédictives pour guider les décideurs.*

Sur la base des résultats analytiques et prédictifs obtenus, plusieurs recommandations peuvent guider les décideurs du secteur immobilier.

La qualité de construction est le levier principal du prix. Avec 57% d'importance dans le modèle RandomForest et une corrélation de 0.808 avec SalePrice, OverallQual est de loin le facteur le plus déterminant. Pour un investisseur ou un vendeur, améliorer la qualité perçue du bien (rénovations, matériaux haut de gamme) est le moyen le plus efficace d'augmenter sa valeur de vente.

La surface habitable reste un facteur clé mais secondaire. GrLivArea contribue à 19% de l'importance du modèle avec une corrélation de 0.703. L'agrandissement d'un bien peut significativement augmenter sa valeur, mais uniquement si la qualité de construction est maintenue.

La zone de marché impacte fortement les prix. Les biens en zone FV atteignent un prix moyen de 214 014 $ contre 82 768 $ en zone commerciale, soit un ratio de 2.6x. Pour un acheteur, privilégier une zone résidentielle de standing constitue le meilleur investissement à long terme.

Le dashboard interactif développé (src/08_dashboard.py) permet à tout décideur non technique de simuler instantanément l'impact de chaque caractéristique sur le prix de vente, facilitant ainsi la prise de décision en temps réel.
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

RF performant sur données tabulaires
CNN capture signaux visuels mais reste limité par les données

<<<<<<< HEAD
##  Data Storytelling

 Recommandations métier:

privilégier les modèles tabulaires pour estimation prix
utiliser CNN comme enrichissement qualitatif
intégrer des données géographiques plus fines

 Limites:

dataset limité
déséquilibre possible des features
CNN sous-entraîné

 Perspectives :

enrichir dataset
multimodal fusion (image + tabulaire)
modèles avancés (XGBoost + Transfer Learning)


## Conclusion

Cette approche montre que :

le Machine Learning tabulaire est le plus robuste pour la prédiction
le Deep Learning apporte une dimension complémentaire
la combinaison des deux ouvre la voie à une analyse multimodale complète
=======
*À rédiger par les étudiants : Identifiez honnêtement les biais ou limites de votre approche et proposez des pistes d'amélioration futures.*

Notre approche présente plusieurs limites identifiées de manière transparente.

Concernant le modèle tabulaire, le coefficient de zone (coef_multiplicateur) n'apporte qu'une contribution marginale de moins de 1%. Cette feature est trop grossière pour capturer la variabilité géographique réelle. Une amélioration consisterait à intégrer les coordonnées GPS des biens ou des données de prix au niveau du quartier.

Concernant le CNN, l'overfitting observé (86% d'accuracy en entraînement vs 52% en test) révèle un manque de données. Avec seulement 1 000 images, le modèle ne généralise pas suffisamment. Le recours au transfer learning (MobileNetV2, ResNet50) permettrait d'atteindre des performances nettement supérieures.

Concernant le dataset, il s'agit de données immobilières américaines datant de 2006-2010. Les modèles entraînés sur ces données ne sont pas directement transposables au marché immobilier actuel ou à d'autres régions géographiques sans re-entraînement.

Enfin, la combinaison des prédictions tabulaires et visuelles en un modèle hybride (ensemble learning) constitue une piste d'amélioration prometteuse pour des travaux futurs.

Ce document dynamique a été compilé en Quarto ([Team 2024](#ref-quarto2024)).
>>>>>>> a4e42e5e9dfc2a23819d7918bcc217144b95d712

------------------------------------------------------------------------

# Bibliographie

McKinney, Wes. 2020. *Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython*. O'Reilly Media.

Team, Quarto Development. 2024. "Quarto Dynamic Publishing System: Collaborative Scientific and Technical Publishing." https://quarto.org/.