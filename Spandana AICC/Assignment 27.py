# text_preprocessing.py

import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import nltk

# Download required resources (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Input text
text = "I am learning NLP and it is very exciting!!!"

# Step 1: Convert to lowercase
text = text.lower()

# Step 2: Remove punctuation
text = text.translate(str.maketrans('', '', string.punctuation))

# Step 3: Tokenize
tokens = word_tokenize(text)

# Step 4: Remove stopwords
stop_words = set(stopwords.words('english'))
tokens = [word for word in tokens if word not in stop_words]

# Step 5: Apply stemming
stemmer = PorterStemmer()
processed = [stemmer.stem(word) for word in tokens]

# Output
print("Processed Output:", processed)