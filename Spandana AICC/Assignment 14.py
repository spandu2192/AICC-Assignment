import pandas as pd

# Load dataset
df = pd.read_csv('data_doctor_sample.csv')

print("Original Dataset:\n", df, "\n")

# --------------------------
# 1. Handle missing values
# --------------------------
# Fill missing numeric values with mean
df['age'].fillna(df['age'].mean(), inplace=True)
df['salary'].fillna(df['salary'].mean(), inplace=True)

# --------------------------
# 2. Remove duplicates
# --------------------------
# Standardize text before removing duplicates
df['name'] = df['name'].str.title()
df['department'] = df['department'].str.title()

# Drop duplicates
df.drop_duplicates(inplace=True)

# --------------------------
# 3. Standardize text
# --------------------------
# Already done: title case for name and department

# --------------------------
# 4. Final Cleaned Dataset
# --------------------------
print("Cleaned Dataset:\n", df, "\n")

# --------------------------
# 5. Why cleaning matters
# --------------------------
explanation = """
Data cleaning is essential because:
1. Missing values can skew analyses and predictions.
2. Duplicates can inflate counts or distort results.
3. Standardized text ensures consistency, making searches, grouping, and visualization accurate.
4. Clean data leads to better insights and more reliable decisions.
"""
print(explanation)