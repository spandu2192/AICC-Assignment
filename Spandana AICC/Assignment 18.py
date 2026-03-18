# Build Your First Dataset
# Run in VS Code: python first_dataset.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import numpy as np

# 1. Create the dataset
data = {
    "Study Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [35, 40, 50, 55, 60, 65, 70, 75, 80, 85]
}

df = pd.DataFrame(data)

# 2. Identify features and labels
# Feature: Study Hours
X = df[["Study Hours"]]  # 2D array required by sklearn
# Label: Marks
y = df["Marks"]

# 3. Visualize the data
plt.scatter(df["Study Hours"], df["Marks"], color='blue')
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.grid(True)
plt.show()

# 4. Build a simple Linear Regression model
model = LinearRegression()
model.fit(X, y)

# 5. Predict marks for new study hours
new_hours = np.array([[2.5], [5.5], [7.5]])
predicted_marks = model.predict(new_hours)

# 6. Print predictions
for hours, marks in zip(new_hours.flatten(), predicted_marks):
    print(f"Predicted marks for {hours} study hours: {marks:.2f}")

# 7. Plot regression line
plt.scatter(df["Study Hours"], df["Marks"], color='blue', label='Actual Data')
plt.plot(df["Study Hours"], model.predict(X), color='red', label='Regression Line')
plt.title("Study Hours vs Marks with Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.legend()
plt.grid(True)
plt.show()