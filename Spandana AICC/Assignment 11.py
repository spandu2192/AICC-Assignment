import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Create dataset manually
data = {
    'hours_studied': [2, 3, 5, 1, 4, 6, 8, 7, 5, 9],
    'sleep_hours': [7, 6, 5, 8, 6, 5, 4, 5, 6, 3],
    'previous_score': [50, 55, 65, 45, 60, 70, 80, 75, 65, 85],
    'final_score': [55, 60, 70, 50, 65, 75, 85, 80, 70, 90]
}

df = pd.DataFrame(data)

# 2. Identify features and label
X = df[['hours_studied', 'sleep_hours', 'previous_score']]  # Features
y = df['final_score']  # Label

# 3. Split into train-test (70-30)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 4. Train Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# 5. Predictions
y_pred = model.predict(X_test)

# 6. Evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Evaluation Metrics:")
print(f"Mean Absolute Error (MAE): {mae:.2f}")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R²): {r2:.2f}")

# 7. Comment on model
if r2 > 0.7:
    print("\nModel performance is good.")
elif r2 > 0.4:
    print("\nModel performance is moderate.")
else:
    print("\nModel performance is poor.")