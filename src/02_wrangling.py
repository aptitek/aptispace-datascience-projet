import os, sys
sys.path.append('/home/aptitek/Documents/Aptispace/datascience/lab/projet')

# Installation automatique des dépendances requises dans le noyau Jupyter actuel
# %pip install -r ../requirements.txt


import os
import sys
import pandas as pd
import numpy as np

# Ajout du dossier parent pour importer 'src'
sys.path.append(os.path.abspath('..'))
from src import data_clean as dc

print("Librairies prêtes pour le Wrangling !")


raw_data_path = '../data/raw/raw_data_sample.csv'
df_raw = dc.load_raw_data(raw_data_path)

# TODO: Effectuer un audit rapide avec .info(), .isnull().sum() et .duplicated().sum()
df_raw.info()


# TODO: Appeler votre fonction dc.clean_dates() sur la colonne correspondante
df_clean = dc.clean_dates(df_raw, 'timestamp')
df_clean.head()


# TODO: Utiliser dc.handle_outliers() avec les seuils minimum et maximum plausibles
df_no_outliers = dc.handle_outliers(df_clean, ['value'], 0.0, 100.0)
df_no_outliers.describe()


# TODO: Appliquer dc.impute_missing_values() avec la méthode de votre choix
df_final = dc.impute_missing_values(df_no_outliers, ['value'], 'interpolate')
print("Anomalies restantes après imputation :", df_final.isnull().sum())


processed_path = '../data/processed/cleaned_data_sample.csv'
# TODO: Sauvegarder avec df.to_csv()
df_final.to_csv(processed_path, index=False)
print(f"💾 Données propres sauvegardées dans : {processed_path}")

