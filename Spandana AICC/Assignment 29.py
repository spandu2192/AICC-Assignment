# Import libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Dataset
data = {
    "text": [
        "I love this product",
        "This is amazing",
        "Worst experience ever",
        "I hate this",
        "Very good service",
        "Not satisfied",
        "Excellent quality",
        "Bad product",
        "It is okay"
    ],
    "label": [
        "positive",
        "positive",
        "negative",
        "negative",
        "positive",
        "negative",
        "positive",
        "negative",
        "neutral"
    ]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    df["text"], df["label"], test_size=0.2, random_state=42
)

# TF-IDF Vectorization
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# Prediction
y_pred = model.predict(X_test_vec)

# Accuracy
print("Accuracy:", accuracy_score(y_test, y_pred))