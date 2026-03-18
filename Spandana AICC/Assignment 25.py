# customer_segmentation.py
# Run in VS Code: python customer_segmentation.py

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

print("=== Customer Segmentation Using K-Means ===\n")

# 1. Sample dataset
data = {
    "CustomerID": [1,2,3,4,5,6,7,8,9,10],
    "Age": [19,21,20,23,31,22,35,25,30,29],
    "AnnualIncome": [15,16,16,17,45,40,80,55,60,50],
    "SpendingScore": [39,81,6,77,40,76,94,20,35,50]
}

df = pd.DataFrame(data)
print("Dataset:\n", df)

# 2. Select features for clustering
X = df[["AnnualIncome", "SpendingScore"]]

# 3. Apply K-Means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

print("\nCluster assignments:\n", df[["CustomerID","Age","AnnualIncome","SpendingScore","Cluster"]])

# 4. Function to label clusters
def label_cluster(avg_income):
    if avg_income < 40:
        return "Budget Shoppers"
    elif avg_income < 60:
        return "Average Spenders"
    else:
        return "Premium Shoppers"

# 5. Describe each cluster
print("\nCustomer Group Descriptions:")
for i in range(3):
    cluster_customers = df[df['Cluster']==i]
    avg_income = cluster_customers['AnnualIncome'].mean()
    avg_score = cluster_customers['SpendingScore'].mean()
    avg_age = cluster_customers['Age'].mean()
    label = label_cluster(avg_income)
    print(f"Cluster {i}: {label} | Average Age = {avg_age:.1f}, Average Income = ${avg_income:.1f}k, Avg Spending Score = {avg_score:.1f}")

# 6. Visualize clusters
plt.figure(figsize=(8,6))
colors = ['red','blue','green']
for i in range(3):
    plt.scatter(
        df[df['Cluster']==i]['AnnualIncome'],
        df[df['Cluster']==i]['SpendingScore'],
        s=100,
        c=colors[i],
        label=f"{label_cluster(df[df['Cluster']==i]['AnnualIncome'].mean())}"
    )

plt.title("Customer Segmentation")
plt.xlabel("Annual Income ($1000s)")
plt.ylabel("Spending Score (1-100)")
plt.legend()
plt.grid(True)
plt.show()