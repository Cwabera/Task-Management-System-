# validation.py

import re

# Validate email
def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

# Validate Kenyan phone number (07XXXXXXXX)
def validate_phone(phone):
    pattern = r'^07\d{8}$'
    return bool(re.match(pattern, phone))

# Validate password (at least 8 chars, letters + numbers)
def validate_password(password):
    if len(password) < 8:
        return False
    
    has_letter = any(char.isalpha() for char in password)
    has_number = any(char.isdigit() for char in password)
    
    return has_letter and has_number


# Main program
if __name__ == "__main__":
    email = input("Enter email: ")
    phone = input("Enter phone number: ")
    password = input("Enter password: ")

    print("Email:", "Valid" if validate_email(email) else "Invalid")
    print("Phone:", "Valid" if validate_phone(phone) else "Invalid")
    print("Password:", "Valid" if validate_password(password) else "Invalid")