import secrets
import string
import time

def generate_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

def loading_effect():
    print("Checking credentials", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()

# Main program
loading_effect()

password = generate_password()

print("\n==============================")
print("✅ ACCESS GRANTED")
print("==============================")
print("🔐 Your Secure Password:")
print(password)
print("==============================")