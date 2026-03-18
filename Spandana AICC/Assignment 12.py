import pandas as pd
from sklearn.linear_model import LinearRegression

# 1. Create DataFrame manually
data = {
    'engine_size': [1300, 1500, 1600, 1400, 1700, 1800, 2000, 2100, 1900, 2200],
    'mileage': [30, 20, 25, 22, 18, 15, 10, 12, 8, 5],
    'age': [5, 3, 4, 6, 2, 1, 3, 2, 1, 0],
    'price': [5000, 7000, 6500, 6000, 7500, 8000, 9000, 8500, 9500, 10000]
}

df = pd.DataFrame(data)

# 2. Features and label
X = df[['engine_size', 'mileage', 'age']]
y = df['price']

# 3. Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# 4. Predict price for given input
input_data = [[1500, 20, 3]]
predicted_price = model.predict(input_data)[0]

print(f"Predicted Price for Engine=1500, Mileage=20, Age=3: ${predicted_price:.2f}")

# 5. Print coefficients
coefficients = model.coef_
features = ['engine_size', 'mileage', 'age']

print("\nFeature Coefficients:")
for feature, coef in zip(features, coefficients):
    print(f"{feature}: {coef:.2f}")

# 6. Interpret feature impact
max_impact_feature = features[abs(coefficients).argmax()]
print(f"\nFeature impacting price the most: {max_impact_feature}")