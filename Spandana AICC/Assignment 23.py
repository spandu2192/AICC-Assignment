# house_price_predictor.py
# Run in VS Code: python house_price_predictor.py

import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

print("=== House Price Predictor using Linear Regression ===\n")

# 1. Sample dataset: Features (Size in sqft, #Bedrooms) and Price (in $1000s)
data = {
    "Size(sqft)": [800, 1000, 1200, 1500, 1800, 2000],
    "Bedrooms": [2, 2, 3, 3, 4, 4],
    "Price($1000s)": [150, 180, 200, 250, 300, 320]
}

df = pd.DataFrame(data)
print("Dataset:\n")
print(df)

# 2. Identify features (X) and label (y)
X = df[["Size(sqft)", "Bedrooms"]]  # Features
y = df["Price($1000s)"]             # Label

# 3. Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

print("\nModel trained successfully!")

# 4. Predict price for new houses
new_houses = np.array([
    [1100, 2],
    [1600, 3],
    [2100, 4]
])

predicted_prices = model.predict(new_houses)

# 5. Display predictions
for house, price in zip(new_houses, predicted_prices):
    print(f"Predicted price for house with {house[0]} sqft and {house[1]} bedrooms: ${price*1000:.2f}")

# Optional: Show regression coefficients
print("\nRegression Coefficients:")
print(f"Size coefficient: {model.coef_[0]:.2f}")
print(f"Bedrooms coefficient: {model.coef_[1]:.2f}")
print(f"Intercept: {model.intercept_:.2f}")