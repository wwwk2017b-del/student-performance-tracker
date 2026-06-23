import pandas as pd
import numpy as np

np.random.seed(42)
n = 200

data = {
    "student_id": range(1, n+1),
    "name": [f"Student_{i}" for i in range(1, n+1)],
    "age": np.random.randint(15, 19, n),
    "gender": np.random.choice(["Male", "Female"], n),
    "attendance_%": np.round(np.random.uniform(50, 100, n), 1),
    "study_hours_per_day": np.round(np.random.uniform(1, 8, n), 1),
    "math_score": np.random.randint(30, 100, n),
    "science_score": np.random.randint(30, 100, n),
    "english_score": np.random.randint(30, 100, n),
    "history_score": np.random.randint(30, 100, n),
}

df = pd.DataFrame(data)
df["final_score"] = (
    df["math_score"] * 0.3 +
    df["science_score"] * 0.3 +
    df["english_score"] * 0.2 +
    df["history_score"] * 0.2 +
    df["attendance_%"] * 0.1 +
    df["study_hours_per_day"] * 0.5
).round(2)

def assign_grade(score):
    if score >= 85: return "A"
    elif score >= 70: return "B"
    elif score >= 55: return "C"
    elif score >= 40: return "D"
    else: return "F"

df["grade"] = df["final_score"].apply(assign_grade)

df.to_csv("students.csv", index=False)
print("✅ Dataset created: students.csv")
