import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, classification_report
from sklearn.preprocessing import LabelEncoder
import numpy as np

df = pd.read_csv("students.csv")

features = ["age", "attendance_%", "study_hours_per_day",
            "math_score", "science_score", "english_score", "history_score"]

X = df[features]

# --- Regression: Predict final score ---
y_reg = df["final_score"]
X_train, X_test, y_train, y_test = train_test_split(X, y_reg, test_size=0.2, random_state=42)
reg = RandomForestRegressor(n_estimators=100, random_state=42)
reg.fit(X_train, y_train)
y_pred = reg.predict(X_test)
print("📊 REGRESSION — Final Score Prediction")
print(f"   R² Score : {r2_score(y_test, y_pred):.4f}")
print(f"   RMSE     : {np.sqrt(mean_squared_error(y_test, y_pred)):.4f}")

# --- Classification: Predict grade ---
le = LabelEncoder()
y_cls = le.fit_transform(df["grade"])
X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y_cls, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train2, y_train2)
y_pred2 = clf.predict(X_test2)
print("\n🎓 CLASSIFICATION — Grade Prediction")
print(f"   Accuracy : {accuracy_score(y_test2, y_pred2):.4f}")
print(classification_report(y_test2, y_pred2, target_names=le.classes_))
