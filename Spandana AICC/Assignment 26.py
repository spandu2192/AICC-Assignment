# decision_tree_play.py
# Run in VS Code: python decision_tree_play.py

import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_text

print("=== Decision Tree: Should You Play Outside? ===\n")

# 1. Sample dataset
data = {
    "Weather": ["Sunny", "Sunny", "Rainy", "Sunny", "Cloudy", "Rainy", "Cloudy", "Sunny"],
    "Temperature": ["Hot", "Hot", "Mild", "Cold", "Mild", "Cold", "Hot", "Mild"],
    "Windy": ["No", "Yes", "No", "Yes", "No", "Yes", "Yes", "No"],
    "HomeworkDone": ["Yes", "No", "Yes", "Yes", "No", "No", "Yes", "Yes"],
    "PlayOutside": ["Yes", "No", "No", "No", "No", "No", "Yes", "Yes"]
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

# 2. Convert categorical features to numeric
features = ["Weather", "Temperature", "Windy", "HomeworkDone"]
df_encoded = pd.get_dummies(df[features])
X = df_encoded
y = df["PlayOutside"]

# 3. Train Decision Tree
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X, y)

# 4. Print tree rules
tree_rules = export_text(clf, feature_names=list(X.columns))
print("\nDecision Tree Rules:\n")
print(tree_rules)

# 5. Predict for new scenario
print("\nTest Prediction:")
new_scenario = pd.DataFrame({
    "Weather_Cloudy": [0],
    "Weather_Rainy": [0],
    "Weather_Sunny": [1],
    "Temperature_Cold": [0],
    "Temperature_Hot": [1],
    "Temperature_Mild": [0],
    "Windy_No": [1],
    "Windy_Yes": [0],
    "HomeworkDone_No": [0],
    "HomeworkDone_Yes": [1]
})
prediction = clf.predict(new_scenario)
print(f"Scenario: Sunny, Hot, Not Windy, Homework Done -> PlayOutside = {prediction[0]}")