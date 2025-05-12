# titanic_gender_analysis.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import chi2_contingency

# Load dataset
# Replace 'titanic_dataset.csv' with your file path
df = pd.read_csv('titanic_dataset.csv')

# Preview data
print("First 5 rows of the dataset:")
print(df.head())

# Basic cleaning
df = df[['Sex', 'Survived']].dropna()

# Convert gender to lowercase (optional for consistency)
df['Sex'] = df['Sex'].str.lower()

# Create a contingency table
contingency_table = pd.crosstab(df['Sex'], df['Survived'])
print("\nContingency Table:")
print(contingency_table)

# Chi-square test for independence
chi2, p, dof, expected = chi2_contingency(contingency_table)
print(f"\nChi-square test results:\nChi2 = {chi2:.4f}, p-value = {p:.4e}, Degrees of Freedom = {dof}")

# Survival percentages by gender
survival_rates = df.groupby('Sex')['Survived'].mean() * 100
print("\nSurvival Rates by Gender (%):")
print(survival_rates)

# Visualization: Survival rate by gender
plt.figure(figsize=(8, 5))
sns.barplot(x=survival_rates.index, y=survival_rates.values, palette='pastel')
plt.title('Titanic Survival Rates by Gender')
plt.ylabel('Survival Rate (%)')
plt.xlabel('Gender')
plt.ylim(0, 100)
for index, value in enumerate(survival_rates.values):
    plt.text(index, value + 2, f'{value:.1f}%', ha='center')
plt.tight_layout()
plt.savefig("figures/survival_by_gender.png")
plt.show()
