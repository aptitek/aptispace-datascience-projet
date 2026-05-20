import os, sys
sys.path.append('/home/aptitek/Documents/Aptispace/datascience/lab/projet')

# Installation automatique des dépendances requises dans le noyau Jupyter actuel
# %pip install -r ../requirements.txt


import os
import sys
import pandas as pd
import numpy as np

# Ajout du dossier parent au chemin de recherche des modules
sys.path.append(os.path.abspath('..'))

print("Libraries importées avec succès ! Prêt pour l'étape d'Acquisition des Données.")


# Spécifiez le chemin vers votre jeu de données principal
main_data_path = '../data/raw/raw_data_sample.csv'

# TODO: Charger le dataset à l'aide de Pandas
df_main = pd.read_csv(main_data_path)

# Affichez la taille et les premières lignes
print(f"Dimensions du dataset principal : {df_main.shape}")
df_main.head()


# TODO: Récupérer/générer ou charger vos données secondaires
# Exemple fictif : création d'un DataFrame complémentaire avec des catégories/labels
categories_info = pd.DataFrame({
    'category': ['A', 'B', 'C'],
    'description': ['Premium', 'Standard', 'Basique'],
    'coef_multiplicateur': [1.5, 1.0, 0.8]
})

print("Données secondaires prêtes :")
categories_info.head()


# TODO: Effectuer la jointure de vos tables si nécessaire
df_merged = pd.merge(df_main, categories_info, on='category', how='left')
df_merged.head()


# Sauvegarde du fichier brute fusionné si applicable
print("Acquisition terminée avec succès !")

