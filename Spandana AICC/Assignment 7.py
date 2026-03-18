import pandas as pd

# Read CSV file (replace 'students.csv' with your actual file path)
df = pd.read_csv('students.csv')

# Handle missing values: fill numeric NaNs with 0
for col in ['maths', 'science', 'english']:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)

# Add 'total' column = sum of all subjects
df['total'] = df[['maths', 'science', 'english']].sum(axis=1)

# Add 'average' column
df['average'] = df[['maths', 'science', 'english']].mean(axis=1)

# Top 3 students based on total marks
top_3_students = df.nlargest(3, 'total')[['name', 'total']]

# Department-wise average marks
dept_avg = df.groupby('dept')[['maths', 'science', 'english', 'total', 'average']].mean()

# Students scoring above 75 in all subjects
students_above_75 = df[(df['maths'] > 75) & (df['science'] > 75) & (df['english'] > 75)]

# Output results
print("Top 3 Students based on Total Marks:")
print(top_3_students.to_string(index=False))

print("\nDepartment-wise Average Marks:")
print(dept_avg.round(2))

print("\nStudents scoring above 75 in all subjects:")
print(students_above_75[['name', 'maths', 'science', 'english', 'total', 'average']].to_string(index=False))