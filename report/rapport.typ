// Some definitions presupposed by pandoc's typst output.
#let blockquote(body) = [
  #set text( size: 0.92em )
  #block(inset: (left: 1.5em, top: 0.2em, bottom: 0.2em))[#body]
]

#let horizontalrule = [
  #line(start: (25%,0%), end: (75%,0%))
]

#let endnote(num, contents) = [
  #stack(dir: ltr, spacing: 3pt, super[#num], contents)
]

#show terms: it => {
  it.children
    .map(child => [
      #strong[#child.term]
      #block(inset: (left: 1.5em, top: -0.4em))[#child.description]
      ])
    .join()
}

// Some quarto-specific definitions.

#show raw.where(block: true): block.with(
    fill: luma(230), 
    width: 100%, 
    inset: 8pt, 
    radius: 2pt
  )

#let block_with_new_content(old_block, new_content) = {
  let d = (:)
  let fields = old_block.fields()
  fields.remove("body")
  if fields.at("below", default: none) != none {
    // TODO: this is a hack because below is a "synthesized element"
    // according to the experts in the typst discord...
    fields.below = fields.below.amount
  }
  return block.with(..fields)(new_content)
}

#let empty(v) = {
  if type(v) == "string" {
    // two dollar signs here because we're technically inside
    // a Pandoc template :grimace:
    v.matches(regex("^\\s*$")).at(0, default: none) != none
  } else if type(v) == "content" {
    if v.at("text", default: none) != none {
      return empty(v.text)
    }
    for child in v.at("children", default: ()) {
      if not empty(child) {
        return false
      }
    }
    return true
  }

}

#show figure: it => {
  if type(it.kind) != "string" {
    return it
  }
  let kind_match = it.kind.matches(regex("^quarto-callout-(.*)")).at(0, default: none)
  if kind_match == none {
    return it
  }
  let kind = kind_match.captures.at(0, default: "other")
  kind = upper(kind.first()) + kind.slice(1)
  // now we pull apart the callout and reassemble it with the crossref name and counter

  // when we cleanup pandoc's emitted code to avoid spaces this will have to change
  let old_callout = it.body.children.at(1).body.children.at(1)
  let old_title_block = old_callout.body.children.at(0)
  let old_title = old_title_block.body.body.children.at(2)

  // TODO use custom separator if available
  let new_title = if empty(old_title) {
    [#kind #it.counter.display()]
  } else {
    [#kind #it.counter.display(): #old_title]
  }

  let new_title_block = block_with_new_content(
    old_title_block, 
    block_with_new_content(
      old_title_block.body, 
      old_title_block.body.body.children.at(0) +
      old_title_block.body.body.children.at(1) +
      new_title))

  block_with_new_content(old_callout,
    new_title_block +
    old_callout.body.children.at(1))
}

#show ref: it => locate(loc => {
  let target = query(it.target, loc).first()
  if it.at("supplement", default: none) == none {
    it
    return
  }

  let sup = it.supplement.text.matches(regex("^45127368-afa1-446a-820f-fc64c546b2c5%(.*)")).at(0, default: none)
  if sup != none {
    let parent_id = sup.captures.first()
    let parent_figure = query(label(parent_id), loc).first()
    let parent_location = parent_figure.location()

    let counters = numbering(
      parent_figure.at("numbering"), 
      ..parent_figure.at("counter").at(parent_location))
      
    let subcounter = numbering(
      target.at("numbering"),
      ..target.at("counter").at(target.location()))
    
    // NOTE there's a nonbreaking space in the block below
    link(target.location(), [#parent_figure.at("supplement") #counters#subcounter])
  } else {
    it
  }
})

// 2023-10-09: #fa-icon("fa-info") is not working, so we'll eval "#fa-info()" instead
#let callout(body: [], title: "Callout", background_color: rgb("#dddddd"), icon: none, icon_color: black) = {
  block(
    breakable: false, 
    fill: background_color, 
    stroke: (paint: icon_color, thickness: 0.5pt, cap: "round"), 
    width: 100%, 
    radius: 2pt,
    block(
      inset: 1pt,
      width: 100%, 
      below: 0pt, 
      block(
        fill: background_color, 
        width: 100%, 
        inset: 8pt)[#text(icon_color, weight: 900)[#icon] #title]) +
      block(
        inset: 1pt, 
        width: 100%, 
        block(fill: white, width: 100%, inset: 8pt, body)))
}



#let article(
  title: none,
  authors: none,
  date: none,
  abstract: none,
  cols: 1,
  margin: (x: 1.25in, y: 1.25in),
  paper: "us-letter",
  lang: "en",
  region: "US",
  font: (),
  fontsize: 11pt,
  sectionnumbering: none,
  toc: false,
  toc_title: none,
  toc_depth: none,
  doc,
) = {
  set page(
    paper: paper,
    margin: margin,
    numbering: "1",
  )
  set par(justify: true)
  set text(lang: lang,
           region: region,
           font: font,
           size: fontsize)
  set heading(numbering: sectionnumbering)

  if title != none {
    align(center)[#block(inset: 2em)[
      #text(weight: "bold", size: 1.5em)[#title]
    ]]
  }

  if authors != none {
    let count = authors.len()
    let ncols = calc.min(count, 3)
    grid(
      columns: (1fr,) * ncols,
      row-gutter: 1.5em,
      ..authors.map(author =>
          align(center)[
            #author.name \
            #author.affiliation \
            #author.email
          ]
      )
    )
  }

  if date != none {
    align(center)[#block(inset: 1em)[
      #date
    ]]
  }

  if abstract != none {
    block(inset: 2em)[
    #text(weight: "semibold")[Abstract] #h(1em) #abstract
    ]
  }

  if toc {
    let title = if toc_title == none {
      auto
    } else {
      toc_title
    }
    block(above: 0em, below: 2em)[
    #outline(
      title: toc_title,
      depth: toc_depth
    );
    ]
  }

  if cols == 1 {
    doc
  } else {
    columns(cols, doc)
  }
}
#show: doc => article(
  title: [Mon Projet Data Science],
  authors: (
    ( name: [Étudiant\(e) 1 : \[Insérer Prénom Nom\]],
      affiliation: [],
      email: [] ),
    ( name: [Étudiant\(e) 2 : \[Insérer Prénom Nom\]],
      affiliation: [],
      email: [] ),
    ( name: [Étudiant\(e) 3 : \[Insérer Prénom Nom\]],
      affiliation: [],
      email: [] ),
    ),
  date: [2026-05-18],
  sectionnumbering: "1.1.a",
  toc: true,
  toc_title: [Table of contents],
  toc_depth: 3,
  cols: 1,
  doc,
)


= Introduction et Contexte Métier
<sec-intro>
#figure([
#link("https://github.com/aptitek/aptispace-datascience-projet/actions/workflows/ci.yml")[#box(width: 154.5pt, image("https://github.com/aptitek/aptispace-datascience-projet/actions/workflows/ci.yml/badge.svg"));]
], caption: figure.caption(
position: bottom, 
[
CI Compilation Pipeline
]), 
kind: "quarto-float-fig", 
supplement: "Figure", 
)


#emph[À rédiger par les étudiants : Présentez ici le contexte global de votre projet, la problématique métier que vous cherchez à résoudre, les questions scientifiques soulevées et les opportunités d’aide à la décision sur la base de vos données.]

== Contexte du Projet
<contexte-du-projet>
#emph[À rédiger par les étudiants — Pistes de réflexion :] - #emph[Quels sont les objectifs globaux et le domaine d’étude de votre projet ?] - #emph[En quoi ce sujet de recherche est-il pertinent et stratégique ?] - #emph[Pourquoi l’analyse quantitative de ce jeu de données est-elle indispensable pour répondre à votre problématique ?]

\[Rédiger votre paragraphe de contexte ici\]

== Objectif Analytique
<objectif-analytique>
#emph[À rédiger par les étudiants — Pistes de réflexion :] - #emph[Quelles sont les variables cibles principales et la tâche globale de modélisation \(classification, régression, clustering, etc.) ?] - #emph[Comment le couplage de données multi-sources et l’intégration de différents types de données \(tabulaires, images, signaux, etc.) enrichissent-ils l’analyse ?] - #emph[Quels sont les livrables analytiques attendus pour répondre à votre problématique et guider les prises de décisions ?]

\[Rédiger votre paragraphe d’objectifs ici\]

#horizontalrule

= Acquisition et Préparation des Données \(Data Wrangling)
<sec-wrangling>
Le succès de tout projet de Data Science repose sur la qualité de la préparation des données #cite(<pandas2020>);. Cette section documente l’audit de qualité et les étapes de nettoyage appliquées à vos jeux de données bruts.

== Audit de Qualité
<audit-de-qualité>
#emph[À rédiger par les étudiants : Présentez un audit critique complet de vos fichiers de données brutes. Indiquez la liste des anomalies physiques et typologiques détectées \(formats de dates hétérogènes, outliers physiques, taux de valeurs manquantes, etc.).]

\[Rédiger votre audit de données ici\]

== Algorithme de Nettoyage
<algorithme-de-nettoyage>
#emph[À rédiger par les étudiants : Justifiez et détaillez l’enchaînement de vos opérations de traitement \(uniformisation des dates, masquage des outliers, imputation, etc.). Faites référence aux fonctions correspondantes de votre module `src/data_clean.py`.]

\[Rédiger la justification méthodologique ici\]

== Travaux Pratiques de Wrangling
<travaux-pratiques-de-wrangling>
= 🧹 Jalon 1 : Data Wrangling & Nettoyage \(Squelette Étudiant)
<jalon-1-data-wrangling-nettoyage-squelette-étudiant>
Ce notebook correspond à la première étape du #strong[Jalon 1];. L’objectif est d’importer le jeu de données brut \(`data/raw/raw_data_sample.csv`), d’effectuer un audit de sa qualité \(données manquantes, anomalies physiques, formats de dates hétérogènes) et de le nettoyer à l’aide de votre package personnalisé `src.data_clean`.

=== 1. Importation des packages et chargement des données
<importation-des-packages-et-chargement-des-données>
=== 2. Audit initial des données
<audit-initial-des-données>
#strong[À faire par l’étudiant :] Explorez le dataset brut pour évaluer sa structure : - Quelles sont les dimensions du dataset ? - Quels sont les types de données par colonne ? - Reste-t-il des valeurs nulles ? Quel est le taux de valeurs manquantes par variable ? - Y a-t-il des doublons ?

=== 3. Nettoyage et uniformisation des Dates
<nettoyage-et-uniformisation-des-dates>
#strong[À faire par l’étudiant :] Appliquez la fonction `clean_dates` de votre module `src.data_clean` pour convertir la colonne `timestamp` en type Datetime uniforme.

=== 4. Identification et Traitement des Outliers \(Anomalies physiques)
<identification-et-traitement-des-outliers-anomalies-physiques>
#strong[À faire par l’étudiant :] Analysez les valeurs de la colonne `value` et appliquez votre fonction `handle_outliers` pour filtrer les valeurs physiques aberrantes \(inférieures à 0 ou supérieures à 100).

=== 5. Imputation des valeurs manquantes
<imputation-des-valeurs-manquantes>
#strong[À faire par l’étudiant :] Appliquez la fonction `impute_missing_values` pour remplir les NaNs issus du chargement initial ou du nettoyage des anomalies.

=== 6. Sauvegarde des données propres
<sauvegarde-des-données-propres>
Enregistrez votre DataFrame nettoyé dans `data/processed/cleaned_data_sample.csv`.

#horizontalrule

= Analyse Exploratoire des Données \(EDA)
<sec-eda>
Dans cette section, nous analysons les relations statistiques fondamentales qui régissent votre domaine d’étude au sein du jeu de données.

== Statistiques Descriptives
<statistiques-descriptives>
#emph[À rédiger par les étudiants : Présentez une vue d’ensemble descriptive rapide de vos variables nettoyées.]

\[Rédiger les statistiques descriptives ici\]

== Ingénierie de Variables \(Feature Engineering)
<ingénierie-de-variables-feature-engineering>
#emph[À rédiger par les étudiants : Expliquez l’intérêt mathématique et l’impact sur les modèles prédictifs d’extraire des caractéristiques dérivées \(ex: variables cycliques temporelles, ratios financiers, ratios physiques, etc.).]

\[Rédiger votre explication de l’ingénierie de variables ici\]

== Travaux Pratiques d’Exploration Visuelle \(EDA)
<travaux-pratiques-dexploration-visuelle-eda>
= 📊 Jalon 1 : Analyse Exploratoire des Données \(EDA) & Visualisation \(Squelette Étudiant)
<jalon-1-analyse-exploratoire-des-données-eda-visualisation-squelette-étudiant>
Ce notebook est dédié à la découverte de relations clés et à l’analyse visuelle de nos données. À partir du jeu de données propre généré précédemment, nous allons enrichir nos variables explicatives et appeler les fonctions de notre module de visualisation `src.utils_viz` pour générer des graphiques professionnels.

=== 1. Importation des packages et configuration du style
<importation-des-packages-et-configuration-du-style>
=== 2. Ingénierie de variables temporelles
<ingénierie-de-variables-temporelles>
#strong[À faire par l’étudiant :] Appliquez la fonction `feature_engineering` de `src.data_clean` pour enrichir votre DataFrame en caractéristiques de temps classiques \(heures, jours de la semaine).

=== 3. Visualisations Professionnelles
<visualisations-professionnelles>
==== A. Profils d’évolution et tendances
<a.-profils-dévolution-et-tendances>
#strong[À faire par l’étudiant :] Appliquez la fonction `plot_generic_trends` de votre module `src.utils_viz` pour tracer l’évolution de la valeur par rapport au temps.

==== B. Matrice de corrélation multi-variables
<b.-matrice-de-corrélation-multi-variables>
#strong[À faire par l’étudiant :] Appliquez la fonction `plot_correlation_matrix` de votre module `src.utils_viz` pour calculer et afficher graphiquement la carte thermique des corrélations sur les colonnes `['value', 'hour', 'dayofweek']`.

==== C. Nuage de points bivarié
<c.-nuage-de-points-bivarié>
#strong[À faire par l’étudiant :] Générez un nuage de points de la relation heure vs valeur en colorant les points selon la variable `dayofweek`, en utilisant votre fonction `plot_bivariate_scatter`.

=== 4. Synthèse des observations clés
<synthèse-des-observations-clés>
Sur la base de vos figures, listez les #strong[insights majeurs] observés sur le comportement de vos variables.

#horizontalrule

= Visualisation Multidimensionnelle \(Insights)
<sec-viz>
Nous présentons ici les résultats visuels clés permettant de dégager des insights exploitables pour les décideurs, en s’appuyant sur notre module `src/utils_viz.py`.

#emph[À rédiger par les étudiants : Présentez et commentez en détail vos 3 à 5 insights majeurs découverts lors de l’exploration descriptive visuelle. Intégrez et justifiez les figures clés générées.]

== Profils et Distributions Caractéristiques
<profils-et-distributions-caractéristiques>
```python
#| label: fig-distribution-density
#| fig-cap: "Distribution ou profils caractéristiques de vos variables clés."
#| echo: false
# TODO: Utiliser vos fonctions personnalisées de votre module pour tracer la figure
```

\[Commenter la figure et décrire vos observations ici\]

== Corrélations Globales
<corrélations-globales>
```python
#| label: fig-correlation
#| fig-cap: "Matrice de corrélation de Spearman ou de Pearson entre variables."
#| echo: false
# TODO: Utiliser uv.plot_correlation_matrix() de votre module pour tracer la figure
```

\[Commenter la figure et décrire vos observations ici\]

#horizontalrule

= Modélisation et Apprentissage
<sec-modelling>
== Schéma Global du Pipeline de Données
<schéma-global-du-pipeline-de-données>
Le pipeline complet intègre à la fois la branche analytique tabulaire \(Machine Learning) et la branche d’analyse visuelle ou de signaux complexes \(Deep Learning CNN) :

```mermaid
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

== Modélisation Tabulaire \(Machine Learning)
<modélisation-tabulaire-machine-learning>
#emph[À rédiger par les étudiants : Expliquez le choix de vos algorithmes d’apprentissage \(supervisé ou non supervisé) et décrivez l’importance des variables explicatives.]

\[Détailler votre modélisation ici\]

=== Travaux Pratiques de Modélisation Tabulaire
<travaux-pratiques-de-modélisation-tabulaire>
= 🧠 Jalon 2 : Modélisation Prédictive & Apprentissage \(Squelette Étudiant)
<jalon-2-modélisation-prédictive-apprentissage-squelette-étudiant>
Dans ce notebook du #strong[Jalon 2];, l’objectif est d’implémenter un pipeline complet d’apprentissage supervisé pour prédire une variable cible \(`value`) à l’aide de Scikit-Learn.

Vous devrez mettre en œuvre une stratégie de découpage train/test chronologique pour respecter la causalité temporelle.

=== 1. Préparation de l’environnement
<préparation-de-lenvironnement>
=== 2. Définition des variables et split chronologique
<définition-des-variables-et-split-chronologique>
#strong[À faire par l’étudiant :] - Identifiez vos colonnes prédictives \(`features`) et la colonne cible \(`value`). - Séparez chronologiquement vos données en ensembles d’entraînement \(`Train`) et de test \(`Test`). N’utilisez pas de split aléatoire !

=== 3. Entraînement du modèle de Forêt Aléatoire
<entraînement-du-modèle-de-forêt-aléatoire>
#strong[À faire par l’étudiant :] - Instanciez et entraînez un modèle `RandomForestRegressor`. - Générez les prédictions `y_pred` sur l’ensemble de test.

=== 4. Évaluation métrique
<évaluation-métrique>
#strong[À faire par l’étudiant :] Calculez et affichez les scores d’évaluation requis : - #strong[MAE] \(Mean Absolute Error) - #strong[RMSE] \(Root Mean Squared Error) - #strong[R²] \(Coefficient de détermination)

=== 5. Importance des variables explicatives
<importance-des-variables-explicatives>
#strong[À faire par l’étudiant :] Extrayez et affichez l’importance relative de chaque caractéristique prédictive.

== Modélisation Vision / Deep Learning \(Analyse d’Images ou Signaux)
<modélisation-vision-deep-learning-analyse-dimages-ou-signaux>
#emph[À rédiger par les étudiants : Expliquez l’intérêt de la brique de Deep Learning \(images, signaux ou traitement de données structurées complexes) pour classifier ou enrichir vos prédictions. Détaillez l’architecture de votre réseau de neurones convolutif \(CNN) conçu sous TensorFlow/Keras \(conv, pooling, dense, dropout, activation) et commentez les courbes d’apprentissage obtenues.]

\[Détailler votre architecture CNN et analyse ici\]

=== Travaux Pratiques de Vision par Ordinateur \(CNN)
<travaux-pratiques-de-vision-par-ordinateur-cnn>
= 📷 Jalon 2 : Brique de Vision par Ordinateur \(CNN & TensorFlow) \(Squelette Étudiant)
<jalon-2-brique-de-vision-par-ordinateur-cnn-tensorflow-squelette-étudiant>
Ce notebook est dédié à la brique d’analyse d’images du #strong[Jalon 2];. L’objectif est de concevoir un Réseau de Neurones Convolutif \(CNN) sous TensorFlow/Keras pour classifier des motifs géométriques simples \(Classe 0: Cercle vs Classe 1: Multiples Rectangles).

=== 1. Préparation de l’environnement
<préparation-de-lenvironnement-1>
=== 2. Génération du jeu d’images synthétiques
<génération-du-jeu-dimages-synthétiques>
Pour travailler de manière autonome sans importer de lourdes bases d’images externes, cette fonction utilitaire génère des images simulées en $64 times 64$ pixels de formes simples \(Cercle vs Rectangles).

=== 3. Split d’évaluation \(Entraînement / Validation)
<split-dévaluation-entraînement-validation>
#strong[À faire par l’étudiant :] Divisez vos données d’images `X_images` et `y_labels` en $80 %$ pour l’entraînement et $20 %$ pour la validation.

=== 4. Conception de l’architecture du CNN
<conception-de-larchitecture-du-cnn>
#strong[À faire par l’étudiant :] Instanciez un réseau convolutif séquentiel Keras comprenant des couches `Conv2D`, `MaxPooling2D`, `Flatten`, `Dense` et un `Dropout` pour classifier nos deux formes géométriques.

=== 5. Compilation et Entraînement
<compilation-et-entraînement>
#strong[À faire par l’étudiant :] - Compilez le modèle avec l’optimiseur `'adam'` et la fonction de perte binaire. - Entraînez votre CNN sur environ 5 époques.

#horizontalrule

= Évaluation Métrique et Validation
<sec-evaluation>
== Stratégie de Validation
<stratégie-de-validation>
#emph[À rédiger par les étudiants : Expliquez pourquoi le découpage d’évaluation choisi \(ex: validation temporelle, stratifiée ou par groupe) est adapté à la structure de vos données pour éviter les fuites de données.]

\[Rédiger la section de validation ici\]

== Résultats et Interprétation
<résultats-et-interprétation>
#emph[À rédiger par les étudiants : Complétez le tableau d’évaluation ci-dessous en reportant vos résultats de modélisation.]

#figure(
align(center)[#table(
  columns: 4,
  align: (col, row) => (auto,auto,auto,auto,).at(col),
  inset: 6pt,
  [Modèle], [Métrique 1 \(ex: MAE / Précision)], [Métrique 2 \(ex: RMSE / F1-Score)], [R² / Score \(%)],
  [Baseline \(ex: Naïve / Moyenne)],
  [\[À compléter\]],
  [\[À compléter\]],
  [\[À compléter\]],
  [#strong[Modèle Choisi];],
  [#strong[\[À compléter\]];],
  [#strong[\[À compléter\]];],
  [#strong[\[À compléter\]];],
)]
)

\[Interpréter et comparer les métriques d’erreur calculées ici\]

#horizontalrule

= Data Storytelling et Communication
<sec-storytelling>
== Recommandations Stratégiques / Métier
<recommandations-stratégiques-métier>
#emph[À rédiger par les étudiants : Formulez des recommandations stratégiques, opérationnelles et innovantes basées sur vos découvertes analytiques et prédictives pour guider les décideurs.]

\[Rédiger vos recommandations ici\]

== Limites et Perspectives
<limites-et-perspectives>
#emph[À rédiger par les étudiants : Identifiez honnêtement les biais ou limites de votre approche et proposez des pistes d’amélioration futures \(ex: intégration de données externes réelles, modélisation plus poussée).]

\[Rédiger les limites et perspectives ici\]

Ce document dynamique a été compilé en Quarto #cite(<quarto2024>);.

#horizontalrule

#block[
#heading(
level: 
1
, 
numbering: 
none
, 
[
Bibliographie
]
)
]
#block[
] <refs>



#bibliography("references.bib")

