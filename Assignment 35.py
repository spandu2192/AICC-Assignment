# Import libraries
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Step 1: Create 5 documents
documents = [
    "machine learning is very useful in data science",
    "data science involves machine learning and data analysis",
    "python is widely used for machine learning",
    "data analysis helps in understanding data patterns",
    "machine learning models improve with more data"
]

# Step 2: Apply TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(documents)

# Convert to DataFrame
feature_names = vectorizer.get_feature_names_out()
df = pd.DataFrame(tfidf_matrix.toarray(), columns=feature_names)

print("TF-IDF Matrix:\n")
print(df)

# Step 3: Find top keywords in each document
print("\nTop Keywords per Document:\n")

for i in range(len(documents)):
    doc = df.iloc[i]
    top_words = doc.sort_values(ascending=False).head(3)
    
    print(f"Document {i+1}:")
    print("Text:", documents[i])
    print("Top Keywords:", list(top_words.index))
    print()