import re

# Sample messy sentences
sentences = [
    "omg this movie is sooo goooood!!! 😍",
    "I cant beleive this happend lol",
    "u r amazing bro 👍",
    "this is the worsttt service ever!!! 😡",
    "had a gr8 day at clg today"
]

# Slang dictionary
slang_dict = {
    "omg": "oh my god",
    "lol": "laughing out loud",
    "u": "you",
    "r": "are",
    "gr8": "great",
    "idk": "I don't know",
    "pls": "please",
    "thx": "thanks",
    "rn": "right now",
    "wat": "what",
    "wid": "with"
}

# Function to clean text
def clean_text(text):
    text = text.lower()
    
    # Replace slang
    for word in text.split():
        if word in slang_dict:
            text = text.replace(word, slang_dict[word])
    
    # Remove emojis
    text = re.sub(r'[^\x00-\x7F]+', '', text)
    
    # Remove repeated characters (soooo → soo)
    text = re.sub(r'(.)\1+', r'\1\1', text)
    
    # Remove punctuation
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    
    return text

# Apply cleaning
cleaned_sentences = [clean_text(s) for s in sentences]

# Print results
for i in range(len(sentences)):
    print("Original:", sentences[i])
    print("Cleaned :", cleaned_sentences[i])
    print()