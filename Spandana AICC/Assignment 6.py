# Smart Input Program - Advanced Version

import sys

def get_valid_name():
    while True:
        name = input("Enter your name: ").strip()
        if name.isalpha():
            return name
        else:
            print("❌ Name should only contain letters. Try again.")

def get_valid_age():
    while True:
        try:
            age = int(input("Enter your age: "))
            if 0 < age < 120:
                return age
            else:
                print("❌ Age should be between 1 and 119.")
        except ValueError:
            print("❌ Please enter a valid number.")

def get_hobby():
    return input("Enter your hobby: ").strip()

def categorize_age(age):
    if age < 13:
        return "Child"
    elif age < 20:
        return "Teenager"
    elif age < 40:
        return "Young Adult"
    elif age < 60:
        return "Adult"
    else:
        return "Senior"

def hobby_suggestion(hobby):
    hobby_lower = hobby.lower()
    if "reading" in hobby_lower:
        return "📚 Keep exploring new books!"
    elif "sports" in hobby_lower or "football" in hobby_lower:
        return "🏆 Stay active and healthy!"
    elif "music" in hobby_lower or "singing" in hobby_lower:
        return "🎵 Keep enjoying your tunes!"
    elif "coding" in hobby_lower or "programming" in hobby_lower:
        return "💻 Keep building cool projects!"
    else:
        return "✨ That sounds fun!"

# Main program
users = []

print("=== Welcome to Smart Input Program ===\n")

while True:
    name = get_valid_name()
    age = get_valid_age()
    hobby = get_hobby()
    age_group = categorize_age(age)
    suggestion = hobby_suggestion(hobby)

    # Save user info
    users.append({"name": name, "age": age, "age_group": age_group, "hobby": hobby, "suggestion": suggestion})

    # Print personalized message
    print("\n------------------------------")
    print(f"Hello {name}!")
    print(f"You are {age} years old, which makes you a {age_group}.")
    print(f"Your hobby is {hobby}. {suggestion}")
    print("------------------------------\n")

    cont = input("Do you want to enter another user? (y/n): ").lower()
    if cont != 'y':
        break

# Print summary of all users
print("\n=== Summary of All Users ===")
print(f"{'Name':<15} {'Age':<5} {'Age Group':<12} {'Hobby':<20} {'Suggestion'}")
print("-"*70)
for u in users:
    print(f"{u['name']:<15} {u['age']:<5} {u['age_group']:<12} {u['hobby']:<20} {u['suggestion']}")
print("\n✅ Program Finished. Thank you!")