import numpy as np
from collections import defaultdict
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Dataset (15+ sentences)
sentences = [
    "sports improve physical fitness",
    "football is a popular sport",
    "cricket is loved by many people",
    "players practice daily to improve skills",
    "teamwork is important in sports",
    "exercise keeps the body healthy",
    "athletes train hard for competitions",
    "winning requires dedication and effort",
    "coaches guide players in training",
    "sports build confidence and discipline",
    "running is good for health",
    "practice makes players perfect",
    "sports events are exciting to watch",
    "fitness is important for athletes",
    "games bring people together",
    "sports teach teamwork and leadership"
]

# Step 2: Preprocess (tokenize)
processed = [s.lower().split() for s in sentences]

# Step 3: Build vocabulary
vocab = list(set(word for sent in processed for word in sent))
word_index = {word: i for i, word in enumerate(vocab)}

# Step 4: Create co-occurrence matrix
window_size = 2
matrix = np.zeros((len(vocab), len(vocab)))

for sent in processed:
    for i, word in enumerate(sent):
        for j in range(max(0, i - window_size), min(len(sent), i + window_size + 1)):
            if i != j:
                matrix[word_index[word]][word_index[sent[j]]] += 1

# Step 5: Get vector for a word
def get_vector(word):
    return matrix[word_index[word]]

# Step 6: Find similar words
def get_similar_words(word, top_n=5):
    vec = get_vector(word).reshape(1, -1)
    similarities = cosine_similarity(vec, matrix)[0]
    
    # Sort indices by similarity
    similar_indices = similarities.argsort()[::-1][1:top_n+1]
    
    return [(vocab[i], similarities[i]) for i in similar_indices]

# Step 7: Test
word = "sports"

print("Vector for word:", word)
print(get_vector(word))

print("\nTop 5 similar words:")
similar_words = get_similar_words(word)

for w, score in similar_words:
    print(w, ":", round(score, 2))