# sentiment_vectorization.py

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# Dataset
documents = [
    "I love this movie",
    "This movie is terrible",
    "Amazing acting",
    "Worst film ever"
]

# -------------------------------
# 1. Bag of Words (CountVectorizer)
# -------------------------------
bow_vectorizer = CountVectorizer()
bow_matrix = bow_vectorizer.fit_transform(documents)

print("=== Bag of Words ===")
print("Vocabulary:", bow_vectorizer.get_feature_names_out())
print("Matrix:\n", bow_matrix.toarray())

# Convert to DataFrame
bow_df = pd.DataFrame(bow_matrix.toarray(), columns=bow_vectorizer.get_feature_names_out())
print("\nBoW DataFrame:\n", bow_df)

# -------------------------------
# 2. TF-IDF
# -------------------------------
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

print("\n=== TF-IDF ===")
print("Vocabulary:", tfidf_vectorizer.get_feature_names_out())
print("Matrix:\n", tfidf_matrix.toarray())

# Convert to DataFrame
tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=tfidf_vectorizer.get_feature_names_out())
print("\nTF-IDF DataFrame:\n", tfidf_df)

# -------------------------------
# 3. Comparison
# -------------------------------
print("\n=== Comparison ===")
print("BoW counts raw frequency of words.")
print("TF-IDF gives importance by reducing common words and boosting rare ones.")