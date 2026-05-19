

import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

print("📢 Communication & Storytelling")

# Chargement
df = pd.read_csv('../data/processed/cleaned_data_sample.csv')

# Top quartiers
top_neighborhoods = (
    df.groupby('Neighborhood')['SalePrice']
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop quartiers les plus chers :")
print(top_neighborhoods)

# Graphique
plt.figure(figsize=(12,6))

top_neighborhoods.plot(kind='bar')

plt.title("Top 10 quartiers les plus chers")
plt.ylabel("Prix moyen")

plt.tight_layout()

plt.show()

print("""
📌 Recommandations :

- Les quartiers premium ont les prix les plus élevés.
- La surface habitable influence fortement le prix.
- Les garages et sous-sols augmentent la valeur immobilière.
- Le modèle RandomForest fournit de bonnes prédictions.
""")

print("✅ Storytelling terminé")