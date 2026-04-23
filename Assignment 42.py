# Import libraries
import pandas as pd
import numpy as np
import re
import string
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

import nltk
from nltk.corpus import stopwords

# Download stopwords (run once)
nltk.download('stopwords')

# Load stopwords
stop_words = set(stopwords.words('english'))

# -----------------------------
# STEP 1: Create Dataset
# -----------------------------
data = {
    "text": [
        "Government launches new health scheme for citizens",
        "Aliens spotted in New York city yesterday",
        "Economy is growing steadily according to reports",
        "Miracle weight loss pill approved overnight",
        "Scientists develop new AI technology for healthcare",
        "Fake news spreads rapidly on social media",
        "New education policy announced by government",
        "Cure for cancer found in a secret lab",
        "Stock market reaches all time high",
        "Celebrity adopts alien baby from Mars"
    ],
    "label": [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]  # 1 = Real, 0 = Fake
}

df = pd.DataFrame(data)

# -----------------------------
# STEP 2: Text Cleaning Function
# -----------------------------
def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", '', text)
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    
    # Remove stopwords
    words = text.split()
    words = [word for word in words if word not in stop_words]
    
    return " ".join(words)

# Apply cleaning
df["cleaned_text"] = df["text"].apply(clean_text)

# -----------------------------
# STEP 3: Train-Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    df["cleaned_text"], df["label"], test_size=0.2, random_state=42
)

# -----------------------------
# STEP 4: TF-IDF Vectorization
# -----------------------------
vectorizer = TfidfVectorizer(max_features=5000)
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# -----------------------------
# STEP 5: Model Training
# -----------------------------
model = LogisticRegression()
model.fit(X_train_vec, y_train)

# -----------------------------
# STEP 6: Model Evaluation
# -----------------------------
y_pred = model.predict(X_test_vec)

print("\nModel Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# -----------------------------
# STEP 7: Save Model
# -----------------------------
pickle.dump(model, open("fake_news_model.pkl", "wb"))
pickle.dump(vectorizer, open("vectorizer.pkl", "wb"))

print("\nModel and vectorizer saved successfully!")

# -----------------------------
# STEP 8: Load Model (Optional)
# -----------------------------
loaded_model = pickle.load(open("fake_news_model.pkl", "rb"))
loaded_vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# -----------------------------
# STEP 9: User Input Prediction
# -----------------------------
print("\n====== Fake News Detector ======")

while True:
    user_input = input("\nEnter news text (or type 'exit'): ")
    
    if user_input.lower() == "exit":
        print("Exiting...")
        break
    
    # Clean input
    cleaned_input = clean_text(user_input)
    
    # Transform input
    input_vec = loaded_vectorizer.transform([cleaned_input])
    
    # Predict
    prediction = loaded_model.predict(input_vec)
    
    if prediction[0] == 1:
        print("🟢 Result: Real News")
    else:
        print("🔴 Result: Fake News")