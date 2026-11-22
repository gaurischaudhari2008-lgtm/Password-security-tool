import random
import string

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password must be at least 8 characters long.")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter (A-Z).")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter (a-z).")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one number (0-9).")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character (@, #, $, %, etc.).")

    if score == 5:
        return "Strong Password! Your password is secure.", []
    elif score >= 3:
        return "Medium Password. Consider these improvements:", feedback
    else:
        return "Weak Password! Please change it immediately:", feedback

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Main Program
print("--- Cyber Security Password Tool ---")
choice = input("1. Check Password Strength\n2. Generate Strong Password\nEnter your choice (1 or 2): ")

if choice == '1':
    user_pwd = input("Enter your password: ")
    status, tips = check_password_strength(user_pwd)
    print("\nResult:", status)
    for tip in tips:
        print("-", tip)
elif choice == '2':
    new_pwd = generate_strong_password()
    print("\nYour new strong password is:", new_pwd)
else:
    print("Invalid choice selected.")
