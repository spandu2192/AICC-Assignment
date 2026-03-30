from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Context sentences for each word
texts = [
    "king is a royal male ruler",
    "queen is a royal female ruler",
    "car is a road vehicle",
    "bus is a large public vehicle",
    "teacher teaches students in school",
    "student learns in school",
    "happy means feeling joy",
    "joyful means full of happiness",
    "computer is an electronic device",
    "banana is a fruit"
]

# Apply TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(texts)

# Function to calculate similarity
def get_similarity(i, j):
    return cosine_similarity(tfidf_matrix[i], tfidf_matrix[j])[0][0]

# Compare pairs
pairs = [
    (0, 1),  # king-queen
    (2, 3),  # car-bus
    (4, 5),  # teacher-student
    (6, 7),  # happy-joyful
    (8, 9)   # computer-banana
]

print("Improved Similarity Scores:\n")

for (i, j) in pairs:
    sim = get_similarity(i, j)
    print(f"{texts[i]}  <->  {texts[j]}")
    print(f"Similarity: {sim:.2f}\n")