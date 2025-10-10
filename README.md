<img width="1920" height="1280" alt="image" src="https://github.com/user-attachments/assets/c78027d0-8c62-407b-a08b-9689bf501f64" />

# Wine Quality Prediction

##  Description du projet

Ce projet vise à prédire la **qualité d’un vin** à partir de ses caractéristiques physico-chimiques (acidité, pH, teneur en alcool, sucre résiduel, etc.).  
C'est un projet supervisé de type **régression** basé sur le dataset public *Wine Quality* ([UCI](https://archive.ics.uci.edu/dataset/186/wine+quality)).

Objectifs :
- Explorer les données (EDA) pour comprendre les facteurs influençant la qualité.
- Entraîner et comparer plusieurs modèles de régression.
- Évaluer la performance via la **RMSE**.
- Sélectionner et interpréter le meilleur modèle.
## Structure fichiers

```
wine-quality-ml/
│
├── data/               # Données brutes et nettoyées
│   ├── raw/
│   └── processed/
│
├── notebooks/          # Notebooks Jupyter (EDA, entraînement)
│   ├── 01_eda.ipynb
│   └── 02_model_training.ipynb
│
├── src/                # Scripts Python
│   ├── data_preprocessing.py
│   └── model_training.py
│
├── models/             # modèles sauvegardés (.pkl, .joblib, ...)
├── tests/              # tests unitaires / smoke
├── docs/               # notes, rapports
├── README.md
└── .gitignore
```
## Installation

### 1. Cloner le dépôt
```bash
git clone https://github.com/<ton_nom_utilisateur>/wine-quality-ml.git
cd wine-quality-ml
```

### 2. Créer un environnement virtuel (recommandé)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Installer les dépendances
```bash
pip install -r requirements.txt
```

## Données
Sources (UCI) :
- Wine Quality – Red: https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv  
- Wine Quality – White: https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv

Chaque ligne = un échantillon de vin ; la colonne cible est `quality` (note généralement entre 0 et 10).

## Pipeline du projet (résumé)
1. **EDA** : statistiques descriptives, corrélations, visualisations.  
2. **Prétraitement** : nettoyage, traitement des valeurs manquantes, normalisation.  
3. **Modélisation** : régression linéaire, Ridge/Lasso, RandomForest, éventuellement XGBoost/LightGBM.  
4. **Évaluation** : RMSE (principal), MAE, analyse d’erreurs.  
5. **Optimisation** : recherche d’hyperparamètres (Grid/Random/Optuna).  
6. **Packaging** : script d’inférence `predict.py`, sauvegarde du modèle, README + Model Card.
## Technologies recommandées
- Python 3.9+
- pandas, numpy, scikit-learn
- matplotlib, seaborn
- (optionnel) xgboost / lightgbm, optuna
- Jupyter Notebook

## 🧾 Auteur
Projet réalisé par [Louis Quibeuf](https://github.com/Louisq05) / premier projet pratique en Machine Learning.
## 📜 Licence
MIT : réutilisation permise avec attribution.
