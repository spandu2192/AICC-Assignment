# ML Idea Generator
# Run in VS Code: python ml_idea_generator.py

ml_ideas = [
    {
        "Domain": "College",
        "Problem": "Predict student performance in a course",
        "Input": ["Attendance percentage", "Assignment scores", "Hours of study per week", "Class participation"],
        "Output": "Pass / Fail (binary classification)",
        "ML_Type": "Supervised learning"
    },
    {
        "Domain": "Healthcare",
        "Problem": "Predict diabetes risk",
        "Input": ["Age", "Gender", "BMI", "Blood sugar levels", "Family history of diabetes"],
        "Output": "Risk score (High / Medium / Low)",
        "ML_Type": "Supervised learning"
    },
    {
        "Domain": "Shopping",
        "Problem": "Product recommendation",
        "Input": ["User purchase history", "Items viewed", "Ratings/reviews", "Time spent on product pages"],
        "Output": "List of recommended products",
        "ML_Type": "Recommender system"
    },
    {
        "Domain": "College / Healthcare",
        "Problem": "Predict attendance for online lectures",
        "Input": ["Previous attendance", "Lecture topic", "Time of day", "Notification sent or not"],
        "Output": "Will attend / Will not attend (binary classification)",
        "ML_Type": "Supervised learning"
    }
]

# Function to print ML ideas nicely
def print_ml_ideas(ideas):
    for idx, idea in enumerate(ideas, 1):
        print(f"\nIdea {idx}:")
        print(f"Domain   : {idea['Domain']}")
        print(f"Problem  : {idea['Problem']}")
        print(f"Input    : {', '.join(idea['Input'])}")
        print(f"Output   : {idea['Output']}")
        print(f"ML Type  : {idea['ML_Type']}")
        print("-" * 50)

# Run the generator
print("=== ML Idea Generator ===")
print_ml_ideas(ml_ideas)