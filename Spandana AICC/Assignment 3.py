import hashlib
import secrets
import string
import getpass

# ----------------------------
# Helper functions
# ----------------------------

def hash_password(password, salt=None):
    """Hash a password with SHA-256 and a salt."""
    if salt is None:
        salt = secrets.token_hex(16)  # 32-character random salt
    hashed = hashlib.sha256((salt + password).encode()).hexdigest()
    return salt, hashed

def generate_strong_password(length=16):
    """Generate a strong random password."""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(chars) for _ in range(length))

# ----------------------------
# User Database (in-memory)
# ----------------------------
# Format: {username: (salt, hashed_password)}
user_db = {}

# ----------------------------
# Registration
# ----------------------------
def register_user():
    print("\n=== User Registration ===")
    username = input("Enter username: ").strip()
    if username in user_db:
        print("❌ Username already exists!")
        return

    choice = input("Do you want to generate a strong password automatically? (y/n): ").lower()
    if choice == 'y':
        password = generate_strong_password()
        print("🔐 Generated password:", password)
    else:
        password = getpass.getpass("Enter password: ")

    # Hash password
    salt, hashed = hash_password(password)
    user_db[username] = (salt, hashed)
    print("✅ Registration successful!\n")

# ----------------------------
# Login
# ----------------------------
def login_user():
    print("\n=== User Login ===")
    username = input("Enter username: ").strip()
    if username not in user_db:
        print("❌ Username not found!")
        return

    password = getpass.getpass("Enter password: ")
    salt, stored_hash = user_db[username]
    _, hashed = hash_password(password, salt)

    if hashed == stored_hash:
        print("\n==============================")
        print("✅ ACCESS GRANTED")
        print("==============================\n")
    else:
        print("\n❌ ACCESS DENIED\n")

# ----------------------------
# Main Program
# ----------------------------
def main():
    while True:
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Select option: ").strip()

        if choice == '1':
            register_user()
        elif choice == '2':
            login_user()
        elif choice == '3':
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.\n")

if __name__ == "__main__":
    main()