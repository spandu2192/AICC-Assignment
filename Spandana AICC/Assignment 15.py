# KNN Breast Cancer Classification
# Try K values from 1 to 15 and compare Euclidean vs Manhattan distance

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Load dataset
data = load_breast_cancer()
X = data.data
y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

euclidean_acc = []
manhattan_acc = []
k_values = range(1, 16)

# Train models with different K values
for k in k_values:
    
    # Euclidean distance
    knn_euclidean = KNeighborsClassifier(n_neighbors=k, metric='euclidean')
    knn_euclidean.fit(X_train, y_train)
    y_pred_e = knn_euclidean.predict(X_test)
    euclidean_acc.append(accuracy_score(y_test, y_pred_e))
    
    # Manhattan distance
    knn_manhattan = KNeighborsClassifier(n_neighbors=k, metric='manhattan')
    knn_manhattan.fit(X_train, y_train)
    y_pred_m = knn_manhattan.predict(X_test)
    manhattan_acc.append(accuracy_score(y_test, y_pred_m))

# Print results
print("K\tEuclidean\tManhattan")
for i in range(len(k_values)):
    print(f"{k_values[i]}\t{euclidean_acc[i]:.4f}\t\t{manhattan_acc[i]:.4f}")

# Plot Accuracy vs K
plt.figure(figsize=(8,5))
plt.plot(k_values, euclidean_acc, marker='o', label="Euclidean Distance")
plt.plot(k_values, manhattan_acc, marker='s', label="Manhattan Distance")

plt.xlabel("K Value")
plt.ylabel("Accuracy")
plt.title("Accuracy vs K for KNN")
plt.legend()
plt.grid(True)
plt.show()

# Best K values
best_e_k = k_values[np.argmax(euclidean_acc)]
best_m_k = k_values[np.argmax(manhattan_acc)]

print("\nBest Euclidean Accuracy:", max(euclidean_acc), "at K =", best_e_k)
print("Best Manhattan Accuracy:", max(manhattan_acc), "at K =", best_m_k)

print("\nExplanation:")
print("Accuracy changes with K because small K may overfit (too sensitive to noise),")
print("while large K may underfit by averaging too many neighbors.")
print("An optimal K balances bias and variance.")