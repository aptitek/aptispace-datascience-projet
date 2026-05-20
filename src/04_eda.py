import os, sys
sys.path.append('/home/aptitek/Documents/Aptispace/datascience/lab/projet')

# Installation automatique des dépendances requises dans le noyau Jupyter actuel
# %pip install -r ../requirements.txt


import os
import sys
import pandas as pd
import numpy as np

sys.path.append(os.path.abspath('..'))
from src import data_clean as dc

print("Librairies importées pour l'EDA !")


df = pd.read_csv('../data/processed/cleaned_data_sample.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df.head()


# TODO: Utiliser df.describe() et des agrégationsgroupby()
df.describe()


# TODO: Appliquer votre ingénierie de variables
df_feat = dc.feature_engineering(df, 'timestamp')
df_feat.head()


# TODO: Calculer les corrélations linéaires (Pearson ou Spearman)
correlations = df_feat[['value', 'hour', 'dayofweek']].corr()
print("Matrice de corrélation de Pearson :")
print(correlations)

