import re

def check_password_strength(password):
    # Check minimum length
    if len(password) < 8:
        return False

    # Check for uppercase and lowercase letters
    if not any(char.isupper() for char in password) or not any(char.islower() for char in password):
        return False

    # Check for at least one digit
    if not any(char.isdigit() for char in password):
        return False

    # Check for at least one special character
    if not re.search(r'[!@#$%^&*()_+{}:;<>,.?~\-=\[\]\'"]', password):
        return False

    # If all criteria are met, return True
    return True

# Input from the user
password = input("Enter a password: ")

# Check password strength
is_strong = check_password_strength(password)

# Provide feedback to the user
if is_strong:
    print("Password is strong and meets all criteria.")
else:
    print("Password is weak. Make sure it has at least 8 characters, both uppercase and lowercase letters, at least one digit, and at least one special character.")
