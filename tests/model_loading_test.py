import joblib

model = joblib.load("../models/random_forest_regressor.joblib")

# Exemple d'utilisation
y_pred = model.predict(X_test)