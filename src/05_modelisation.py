import os, sys
sys.path.append('/home/aptitek/Documents/Aptispace/datascience/lab/projet')

# Installation automatique des dépendances requises dans le noyau Jupyter actuel
# %pip install -r ../requirements.txt


import os
import sys
import pandas as pd
import numpy as np

from sklearn.ensemble import RandomForestRegressor
import tensorflow as tf
from tensorflow.keras import layers, models

sys.path.append(os.path.abspath('..'))
from src import data_clean as dc

print("Librairies de modélisation importées avec succès !")
print("Version TensorFlow :", tf.__version__)


# Chargement des données propres et ingénierie des caractéristiques
df = pd.read_csv('../data/processed/cleaned_data_sample.csv')
df['timestamp'] = pd.to_datetime(df['timestamp'])
df_feat = dc.feature_engineering(df, 'timestamp')

features = ['hour', 'dayofweek']
target = 'value'

# Split chronologique simple pour l'entraînement
X_train = df_feat[features].iloc[:-4]
y_train = df_feat[target].iloc[:-4]

# TODO: Instancier et entraîner RandomForestRegressor sur (X_train, y_train)
rf_model = RandomForestRegressor(n_estimators=10, random_state=42)
rf_model.fit(X_train, y_train)
print("Modèle de forêt aléatoire entraîné !")


# Génération fictive d'un jeu d'images simples (64x64 pixels) de cercles (Classe 0) vs rectangles (Classe 1)
def generate_dummy_images(num_samples=100):
    images = np.zeros((num_samples, 64, 64, 3), dtype=np.float32)
    labels = np.zeros(num_samples, dtype=np.int32)
    for i in range(num_samples):
        label = np.random.choice([0, 1])
        labels[i] = label
        images[i, :, :, :] = 0.2 + np.random.normal(0, 0.01, (64, 64, 3))
        if label == 1:
            images[i, 10:30, 10:30, 0] = 0.8
        else:
            images[i, 20:40, 20:40, 1] = 0.8
    return images, labels

X_images, y_labels = generate_dummy_images(100)
split = int(0.8 * len(X_images))
X_img_train = X_images[:split]
y_img_train = y_labels[:split]

print(f"Dataset d'images brutes généré. Dimensions Train : {X_img_train.shape}")


# TODO: Définir l'architecture séquentielle du CNN avec layers.Conv2D et layers.MaxPooling2D
cnn_model = models.Sequential([
    layers.Conv2D(16, (3, 3), activation='relu', input_shape=(64, 64, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(16, activation='relu'),
    layers.Dense(1, activation='sigmoid')
])

cnn_model.summary()


# TODO: Compiler et entraîner le CNN avec l'optimiseur adam et une binary_crossentropy
cnn_model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
cnn_model.fit(X_img_train, y_img_train, epochs=2, batch_size=32, verbose=1)
print("CNN entraîné avec succès !")

