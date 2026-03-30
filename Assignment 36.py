import random

# Sample training data (can be expanded)
text_data = [
    "college life is fun and full of learning",
    "students study hard to achieve their goals",
    "machine learning is an interesting subject",
    "python is widely used in data science",
    "data science helps in analyzing information",
    "students enjoy participating in college events",
    "learning new skills improves career opportunities",
    "friends support each other during exams",
    "practice makes a person perfect in coding",
    "projects help students gain practical knowledge"
]

# Step 1: Build word transition dictionary
word_dict = {}

for sentence in text_data:
    words = sentence.lower().split()
    for i in range(len(words) - 1):
        if words[i] not in word_dict:
            word_dict[words[i]] = []
        word_dict[words[i]].append(words[i + 1])

# Step 2: Function to generate sentence
def generate_sentence(start_word, length=10):
    sentence = [start_word.lower()]
    
    for _ in range(length - 1):
        current_word = sentence[-1]
        
        if current_word in word_dict:
            next_word = random.choice(word_dict[current_word])
        else:
            next_word = random.choice(list(word_dict.keys()))
        
        sentence.append(next_word)
    
    return " ".join(sentence)

# Step 3: Take input from user
start_word = input("Enter a starting word: ")

# Step 4: Generate 10-word sentence
generated = generate_sentence(start_word, 10)

print("\nGenerated Sentence:")
print(generated)