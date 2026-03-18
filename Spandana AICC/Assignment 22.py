# knn_real_life.py
# Run in VS Code: python knn_real_life.py

import pandas as pd
import numpy as np

print("=== Netflix-Like Movie Recommendation Using KNN ===\n")

# 1. Sample dataset: Movies and ratings by 3 users
data = {
    "Movie": ["Movie A", "Movie B", "Movie C", "Movie D", "Movie E"],
    "User1": [5, 3, 0, 0, 2],
    "User2": [4, 0, 0, 2, 3],
    "User3": [0, 0, 5, 4, 0]
}

df = pd.DataFrame(data)
df.set_index("Movie", inplace=True)

print("Movie Ratings Dataset:\n")
print(df)

# 2. Function to calculate Euclidean distance between movies
def euclidean_distance(movie1, movie2):
    vec1 = df.loc[movie1].values
    vec2 = df.loc[movie2].values
    return np.sqrt(np.sum((vec1 - vec2) ** 2))

# 3. Function to find K nearest neighbors (most similar movies)
def knn_recommend(target_movie, k=3):
    distances = {}
    for movie in df.index:
        if movie != target_movie:
            distances[movie] = euclidean_distance(target_movie, movie)
    # Sort movies by similarity (smallest distance first)
    nearest = sorted(distances, key=distances.get)[:k]
    return nearest

# 4. Explain the concept in a short paragraph
print("\nExplanation:")
print("Netflix recommends movies by finding similar movies or users using KNN.")
print("If a user likes a movie, KNN finds K nearest movies based on ratings from all users.")
print("Movies with the closest ratings are recommended to the user.\n")

# 5. Interactive input for user
print("Enter a movie you like from the dataset (Movie A, Movie B, Movie C, Movie D, Movie E):")
target_movie = input().strip()

if target_movie not in df.index:
    print("Movie not found in the dataset! Please run again with a valid movie name.")
else:
    recommended = knn_recommend(target_movie, k=3)
    print(f"\nTop 3 movies similar to '{target_movie}': {recommended}")