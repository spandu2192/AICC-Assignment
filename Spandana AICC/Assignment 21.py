# placement_prediction.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# Dataset
data = {
    "cgpa": [7.5, 6.2, 8.1, 5.9, 7.8, 6.5, 8.5, 7.0, 6.8, 8.2],
    "aptitude": [78, 65, 90, 55, 85, 70, 92, 75, 68, 88],
    "projects": [3, 2, 4, 1, 3, 2, 5, 3, 2, 4],
    "internship": [1, 0, 1, 0, 1, 0, 1, 0, 0, 1],
    "communication": [7, 6, 8, 5, 8, 6, 9, 7, 6, 8],
    "placed": [1, 0, 1, 0, 1, 0, 1, 1, 0, 1]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and target
X = df.drop("placed", axis=1)
y = df["placed"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", accuracy)

# Predict for a new student
new_student = [[8.0, 85, 4, 1, 8]]  # cgpa, aptitude, projects, internship, communication
prediction = model.predict(new_student)

print("Prediction (1 = Placed, 0 = Not Placed):", prediction[0])