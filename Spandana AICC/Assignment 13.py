import pandas as pd

# Load the dataset
df = pd.read_csv('dataset_detective_sample.csv')

# 1. Display top 5 rows
print("Top 5 rows of the dataset:")
print(df.head(), "\n")

# 2. Find the column with highest single value (numeric columns only)
max_values = df.max(numeric_only=True)
max_col = max_values.idxmax()
max_val = max_values.max()
print(f"Column with highest single value: '{max_col}' with value {max_val}\n")

# 3. Count missing values per column
missing_counts = df.isnull().sum()
print("Missing values per column:")
print(missing_counts, "\n")

# 4. Five insights:
print("Five Insights:")

# Insight 1: Dataset shape
print(f"1. The dataset has {df.shape[0]} rows and {df.shape[1]} columns.")

# Insight 2: Number of unique values per column
unique_counts = df.nunique()
print("2. Unique values per column:")
print(unique_counts)

# Insight 3: Mean values of numeric columns
print("3. Mean values of numeric columns:")
print(df.mean(numeric_only=True))

# Insight 4: Columns with more than 50% missing data
high_missing = missing_counts[missing_counts > 0.5 * df.shape[0]]
if not high_missing.empty:
    print("4. Columns with more than 50% missing values:")
    print(high_missing)
else:
    print("4. No columns with more than 50% missing data.")

# Insight 5: Top 5 absolute correlations (excluding self-correlation)
corr = df.corr()
corr_pairs = corr.unstack()
corr_pairs = corr_pairs[corr_pairs < 1].abs().sort_values(ascending=False).drop_duplicates()
print("5. Top 5 correlations between features:")
print(corr_pairs.head(5))