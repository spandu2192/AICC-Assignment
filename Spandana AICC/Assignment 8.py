def fizz_buzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

def main():
    fizz_count = 0
    buzz_count = 0
    fizzbuzz_count = 0

    for i in range(1, 51):
        result = fizz_buzz(i)
        print(result)
        
        if result == "Fizz":
            fizz_count += 1
        elif result == "Buzz":
            buzz_count += 1
        elif result == "FizzBuzz":
            fizzbuzz_count += 1

    print("\n--- Occurrences ---")
    print(f"Fizz: {fizz_count}")
    print(f"Buzz: {buzz_count}")
    print(f"FizzBuzz: {fizzbuzz_count}")

if __name__ == "__main__":
    main()