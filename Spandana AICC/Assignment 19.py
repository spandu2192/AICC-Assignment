# Loan Approval Predictor
# Decision Tree vs Random Forest

import numpy as np
import pandas as pd
import pickle
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# -------------------------
# 1. Create Sample Dataset
# -------------------------
data = {
    "Income":[40000,60000,80000,30000,50000,90000,100000,35000,45000,70000],
    "CreditScore":[650,700,750,600,720,780,800,640,690,730],
    "Age":[25,35,45,23,40,50,55,28,33,38],
    "LoanAmount":[200000,250000,300000,150000,220000,350000,400000,180000,210000,270000],
    "EmploymentYears":[2,5,10,1,6,15,20,3,4,8],
    "Approved":[0,1,1,0,1,1,1,0,1,1]
}

df = pd.DataFrame(data)

# -------------------------
# 2. Split Dataset
# -------------------------
X = df.drop("Approved", axis=1)
y = df["Approved"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -------------------------
# 3. Train Decision Tree
# -------------------------
dt_model = DecisionTreeClassifier(random_state=42)
dt_model.fit(X_train, y_train)

dt_pred = dt_model.predict(X_test)
dt_acc = accuracy_score(y_test, dt_pred)

# -------------------------
# 4. Train Random Forest
# -------------------------
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)
rf_acc = accuracy_score(y_test, rf_pred)

# -------------------------
# 5. Compare Accuracy
# -------------------------
print("Decision Tree Accuracy:", dt_acc)
print("Random Forest Accuracy:", rf_acc)

# -------------------------
# 6. Feature Importance
# -------------------------
importance = rf_model.feature_importances_

plt.bar(X.columns, importance)
plt.title("Feature Importance (Random Forest)")
plt.xlabel("Features")
plt.ylabel("Importance")
plt.show()

# -------------------------
# 7. Save Model using Pickle
# -------------------------
with open("loan_model.pkl","wb") as f:
    pickle.dump(rf_model,f)

print("Model saved as loan_model.pkl")