import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

os.makedirs("outputs", exist_ok=True)
df = pd.read_csv("students.csv")

# Plot 1: Grade Distribution
plt.figure(figsize=(8,5))
sns.countplot(x="grade", data=df, palette="viridis", order=["A","B","C","D","F"])
plt.title("Grade Distribution")
plt.savefig("outputs/grade_distribution.png")
plt.close()
print("✅ Saved: grade_distribution.png")

# Plot 2: Study Hours vs Final Score
plt.figure(figsize=(8,5))
sns.scatterplot(x="study_hours_per_day", y="final_score", hue="grade", data=df, palette="Set1")
plt.title("Study Hours vs Final Score")
plt.savefig("outputs/study_vs_score.png")
plt.close()
print("✅ Saved: study_vs_score.png")

# Plot 3: Attendance vs Final Score
plt.figure(figsize=(8,5))
sns.scatterplot(x="attendance_%", y="final_score", hue="grade", data=df, palette="Set2")
plt.title("Attendance vs Final Score")
plt.savefig("outputs/attendance_vs_score.png")
plt.close()
print("✅ Saved: attendance_vs_score.png")

# Plot 4: Subject Score Averages
plt.figure(figsize=(8,5))
subject_means = df[["math_score","science_score","english_score","history_score"]].mean()
subject_means.plot(kind="bar", color="steelblue")
plt.title("Average Subject Scores")
plt.xticks(rotation=45)
plt.savefig("outputs/subject_averages.png")
plt.close()
print("✅ Saved: subject_averages.png")
