import os, sys
sys.path.append('/home/aptitek/Documents/Aptispace/datascience/lab/projet')

# Installation automatique des dépendances requises dans le noyau Jupyter actuel
# %pip install -r ../requirements.txt


import os
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sys.path.append(os.path.abspath('..'))
from src import data_clean as dc
from src import utils_viz as uv

# Activation du style premium personnalisé (light ou dark)
uv.set_custom_style(theme='light')
# %matplotlib inline
print("Librairies de visualisation prêtes !")


df = pd.read_csv('../data/processed/cleaned_data_sample.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df_feat = dc.feature_engineering(df, 'timestamp')
df_feat.head()


# TODO: Appeler uv.plot_generic_trends() pour tracer l'évolution temporelle
fig1 = uv.plot_generic_trends(df_feat, 'timestamp', 'value', group_col='category')
plt.show()


# TODO: Appeler uv.plot_correlation_matrix() pour les colonnes d'intérêt
fig2 = uv.plot_correlation_matrix(df_feat, ['value', 'hour', 'dayofweek'])
plt.show()


# TODO: Tracer un nuage de points heure vs valeur avec coloration
fig3 = uv.plot_bivariate_scatter(df_feat, 'hour', 'value', color_col='dayofweek')
plt.show()

