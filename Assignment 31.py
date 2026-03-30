# Import libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load dataset
data = pd.read_csv('Student_Performance.csv')

# Display data
print(data.head())

# Select features (Study Hours & Marks)
X = data[['Study Hours', 'Marks']]

# Elbow Method
wcss = []
for i in range(1, 8):
    kmeans = KMeans(n_clusters=i, random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

# Plot elbow graph
plt.figure()
plt.plot(range(1, 8), wcss, marker='o')
plt.title('Elbow Method')
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')
plt.show()

# Apply K-Means (K=3)
kmeans = KMeans(n_clusters=3, random_state=42)
data['Cluster'] = kmeans.fit_predict(X)

# Plot clusters
plt.figure()
plt.scatter(X['Study Hours'], X['Marks'], c=data['Cluster'])
plt.scatter(kmeans.cluster_centers_[:, 0],
            kmeans.cluster_centers_[:, 1],
            s=200, marker='X')

plt.xlabel('Study Hours')
plt.ylabel('Marks')
plt.title('Student Segmentation')
plt.show()

# Cluster count
print("\nStudents in each cluster:")
print(data['Cluster'].value_counts())