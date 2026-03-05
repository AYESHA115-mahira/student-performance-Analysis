import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("dataset.csv")

print("First 5 rows of dataset:")
print(data.head())

# Average Scores
print("Average Math Score:", data['math_score'].mean())
print("Average Reading Score:", data['reading_score'].mean())
print("Average Writing Score:", data['writing_score'].mean())

# Scatter Plot
plt.scatter(data['study_hours'], data['math_score'])
plt.xlabel("Study Hours")
plt.ylabel("Math Score")
plt.title("Study Hours vs Math Score")
plt.show()

# Correlation Heatmap
corr = data.corr(numeric_only=True)

sns.heatmap(corr, annot=True)
plt.title("Correlation Matrix")
plt.show()