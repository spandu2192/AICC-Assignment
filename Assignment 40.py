# Simple LLM simulation function
def simple_llm(prompt):
    if "detailed" in prompt or "step-by-step" in prompt:
        return "This is a well-structured and detailed response based on the given prompt."
    else:
        return "This is a basic response with limited information."

# Step 1: Define prompts
prompts = {
    "Resume": {
        "weak": "Write a resume",
        "strong": "Write a detailed resume for a computer science student including skills, projects, and achievements"
    },
    "Business Idea": {
        "weak": "Give business idea",
        "strong": "Give a detailed business idea for a startup in AI with problem, solution, and target market"
    },
    "Study Plan": {
        "weak": "Make study plan",
        "strong": "Create a step-by-step 30-day study plan for learning Python with daily tasks"
    }
}

# Step 2: Compare outputs
for category, types in prompts.items():
    print(f"\n--- {category} ---")
    
    for prompt_type, text in types.items():
        response = simple_llm(text)
        print(f"\n{prompt_type.upper()} PROMPT:")
        print("Prompt:", text)
        print("Response:", response)