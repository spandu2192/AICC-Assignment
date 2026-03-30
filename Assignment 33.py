import string

# Sample text
text = "This is an Example! It shows how to CLEAN the text, and remove stopwords."

# Define simple stopwords list
stopwords = {
    "is", "an", "the", "and", "to", "it", "how"
}

# Function to clean text
def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Tokenize (split into words)
    words = text.split()
    
    # Remove stopwords
    cleaned_words = [word for word in words if word not in stopwords]
    
    # Join words back into sentence
    cleaned_text = " ".join(cleaned_words)
    
    return cleaned_text

# Apply cleaning
result = clean_text(text)

# Output
print("Original Text:")
print(text)

print("\nCleaned Text:")
print(result)