# Mall Customer Segmentation using KMeans

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# -----------------------------
# 1. Create Dataset
# -----------------------------
data = {
    "Age":[19,21,20,23,31,22,35,23,64,30,67,35,58,24,37],
    "AnnualIncome":[15,15,16,16,17,17,18,18,19,19,20,20,21,21,22],
    "SpendingScore":[39,81,6,77,40,76,6,94,3,72,14,99,15,77,13]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)

# -----------------------------
# 2. Select Features
# -----------------------------
X = df[["Age","AnnualIncome","SpendingScore"]]

# -----------------------------
# 3. Apply KMeans
# -----------------------------
kmeans = KMeans(n_clusters=3, random_state=42)
df["Cluster"] = kmeans.fit_predict(X)

# -----------------------------
# 4. Display Centroids
# -----------------------------
print("\nCentroids:")
print(kmeans.cluster_centers_)

# -----------------------------
# 5. Plot Clusters
# -----------------------------
plt.figure(figsize=(7,5))

plt.scatter(df["AnnualIncome"], df["SpendingScore"],
            c=df["Cluster"], cmap="viridis", s=100)

plt.scatter(kmeans.cluster_centers_[:,1],
            kmeans.cluster_centers_[:,2],
            color="red", marker="X", s=200, label="Centroids")

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Mall Customer Segmentation (KMeans)")
plt.legend()

plt.show()