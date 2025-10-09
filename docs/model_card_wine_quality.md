# 🍷 Model Card — Wine Quality Regressor

## 1. Informations générales

- **Nom du modèle :** RandomForestRegressor (Optimisé)
- **Version :** 1.0
- **Date :** 2025-10-06
- **Auteur :** Louis
- **But du modèle :** Prédire la qualité d’un vin à partir de ses caractéristiques physico-chimiques.

---

## 2. Données utilisées

- **Source du dataset :** UCI Machine Learning Repository – Wine Quality Dataset  
- **Taille du jeu de données :** ~1599 échantillons (vins rouges)  
- **Variables d’entrée (features) :**
  - fixed acidity  
  - volatile acidity  
  - citric acid  
  - residual sugar  
  - chlorides  
  - free sulfur dioxide  
  - total sulfur dioxide  
  - density  
  - pH  
  - sulphates  
  - alcohol  

- **Variable cible :** `quality` (note de qualité comprise entre 0 et 10)  
- **Type de tâche :** Régression

---

## 3. Détails du modèle

- **Algorithme :** Random Forest Regressor  
- **Bibliothèque :** scikit-learn  
- **Hyperparamètres clés :**
  - n_estimators ≈ 99 (optimisé)
  - max_depth ≈ 17
  - min_samples_split = 5
  - min_samples_leaf = 1
  - max_features = 'log2'

---

## 4. Performance du modèle

| Jeu de données | MAE ↓ | RMSE ↓ | R² ↑ |
|----------------|--------|--------|------|
| Train (CV mean) | ≈ 0.52 | ≈ 0.70 | ≈ 0.49 |
| Test final | **0.526** | **0.707** | **0.494** |

➡️ Le modèle explique environ **49 % de la variance** de la qualité du vin.  
Il offre une **précision moyenne de ±0.5 point** sur la note de qualité.

---

## 5. Interprétabilité

**Top 5 variables les plus importantes :**
1. `alcohol`  
2. `sulphates`   
3. `volatile acidity` 
4. `density` 
5. `total sulfure dioxide`

Ces variables influencent le plus la prédiction de la qualité.

---

## 6. Limites connues

- Le score R² < 0.5 indique qu’une partie significative de la qualité est influencée par **des facteurs non mesurés** (jugement humain, contexte sensoriel, etc.).
- Le modèle peut **généraliser modérément** sur de nouveaux types de vins (blancs, rosés).
- Dataset relativement **petit** → attention à la variance des résultats.
- Pas d’analyse de biais approfondie (mais pas de données sensibles non plus).

---

## 7. Utilisation recommandée

- Outil éducatif ou démonstratif pour la régression supervisée.
- Base de référence pour expérimenter d’autres algorithmes (XGBoost, LightGBM…).
- Ne pas utiliser pour des décisions commerciales ou qualitatives réelles sur le vin 🍇.

---

## 8. Reproductibilité

- **Langage :** Python 3.11  
- **Librairies principales :** pandas, numpy, scikit-learn, matplotlib, seaborn  
- **Seed :** 42  
- **Fichiers associés :**
  - `02_preprocessing.ipynb`
  - `03_modelisation_regression.ipynb`
  - `README.md`
  - `requirements.txt`

