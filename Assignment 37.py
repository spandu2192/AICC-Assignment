# Import libraries
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Step 1: Training data
reviews = [
    "this movie is amazing and wonderful",
    "i love this film it is fantastic",
    "what a great and inspiring movie",
    "this movie is terrible and boring",
    "i hate this film it is bad",
    "worst movie ever not interesting"
]

# Labels (1 = Positive, 0 = Negative)
labels = [1, 1, 1, 0, 0, 0]

# Step 2: Convert text to numbers
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(reviews)

# Step 3: Train model
model = MultinomialNB()
model.fit(X, labels)

# Step 4: Test on new reviews
test_reviews = [
    "this movie is fantastic",
    "i hate this movie",
    "it was a wonderful film",
    "boring and bad movie",
    "great acting and amazing story"
]

# Convert test data
X_test = vectorizer.transform(test_reviews)

# Predict
predictions = model.predict(X_test)

# Output results
for review, pred in zip(test_reviews, predictions):
    sentiment = "Positive" if pred == 1 else "Negative"
    print(f"Review: {review}")
    print(f"Sentiment: {sentiment}\n")