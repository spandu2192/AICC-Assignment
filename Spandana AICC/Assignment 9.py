# Define student data: dictionary with name as key and marks as values
students = {
    "Alice": {"maths": 85, "science": 78, "english": 92},
    "Bob": {"maths": 67, "science": 89, "english": 73},
    "Charlie": {"maths": 90, "science": 88, "english": 95},
    "David": {"maths": 72, "science": 75, "english": 80},
    "Eva": {"maths": 88, "science": 76, "english": 85}
}

def calculate_total_and_average(marks):
    total = sum(marks.values())
    average = total / len(marks)
    return total, average

def assign_grade(avg):
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    else:
        return "F"

# Calculate total, average, and grades for each student
for name, marks in students.items():
    total, avg = calculate_total_and_average(marks)
    students[name]["total"] = total
    students[name]["average"] = avg
    students[name]["grade"] = assign_grade(avg)

# Find topper (highest total)
topper = max(students.items(), key=lambda x: x[1]["total"])

# Calculate class average (average of averages)
class_avg = sum(s["average"] for s in students.values()) / len(students)

# Print results
print("Student Details:\n")
print(f"{'Name':<10} {'Total':<6} {'Average':<8} {'Grade'}")
print("-" * 35)
for name, data in students.items():
    print(f"{name:<10} {data['total']:<6} {data['average']:<8.2f} {data['grade']}")

print("\nClass Average:", round(class_avg, 2))
print(f"Topper: {topper[0]} with Total Marks = {topper[1]['total']}")