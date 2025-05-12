# 🚢 Analyzing Titanic Survival Rates by Gender

## 📘 Project Overview

This project explores gender-based survival patterns in the Titanic disaster using historical passenger data. The primary objective is to determine if gender significantly influenced survival rates, supporting the hypothesis that women were more likely to survive due to the "Women and Children First" policy.

---

## 📊 Key Findings

- **Women Survival Rate:** ~74%
- **Men Survival Rate:** ~19%
- **Chi-Square Test Result:** p-value < 0.001 (statistically significant)
- Results suggest a strong association between gender and survival, validating historical reports and evacuation priorities.

---

## 📂 Dataset

**Source:** Titanic Dataset (2025)  
**Features Used:**
- `Sex` (Gender)
- `Survived` (Survival Status)
- `Pclass` (Passenger Class)
- `Age`
- `Fare`

---

## 🧪 Methods & Tools

- **Data Analysis:** Python, pandas
- **Visualization:** matplotlib, seaborn
- **Statistics:** Chi-square test for independence (with Bonferroni correction)
- **Data Cleaning:** Handling missing values via median imputation or row removal
- **Visualization:** Bar charts comparing survival rates by gender

---

## 📉 Limitations

- Age and class not fully explored in statistical modeling
- Correlation does not imply causation
- Dataset reflects historical biases and recording limitations

---

## 🔍 Future Improvements

- Add logistic regression to model survival with multiple predictors
- Use feature engineering (e.g., titles from names, family size)
- Incorporate interactive visualizations with `plotly` or `dash`
- Add survival breakdown by gender *and* class

---

## 📌 References

- Frey, B. S., Savage, D. A., & Torgler, B. (2011). *Behavior under Extreme Conditions: The Titanic Disaster*.
- Gleicher, D. (2018). *The Titanic Rules: Women and Children First?*
- Hall, W. (1986). *The Social Structure of Disasters: Evidence from the Titanic*.
- McPherson, G. (2001). *Statistical Analysis in Social Research*.
- Titanic Dataset (2025). *Historical Passenger Data on the Titanic*.

---

## 📎 File Structure

