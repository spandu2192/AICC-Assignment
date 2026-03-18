# Input from user
num = int(input("Enter a number: "))

# Check even or odd
if num % 2 == 0:
    print(f"{num} is Even ✅")
else:
    print(f"{num} is Odd ❌")

# Print numbers from 10 to 1
for i in range(10, 0, -1):
    print(i)


total = 0  # Initialize sum

while True:
    try:
        num = float(input("Enter a number (0 to stop): "))
    except ValueError:
        print("❌ Please enter a valid number!")
        continue

    if num == 0:
        break  # Stop the loop when user enters 0

    total += num  # Add to total

print(f"\n✅ Total sum of entered numbers: {total}")      