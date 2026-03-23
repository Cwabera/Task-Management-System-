# validation.py

import re


def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))


def validate_phone(phone):
    pattern = r'^07\d{8}$'
    return bool(re.match(pattern, phone))


def validate_password(password):
    if len(password) < 8:
        return False
    
    has_letter = any(c.isalpha() for c in password)
    has_number = any(c.isdigit() for c in password)
    
    return has_letter and has_number


if __name__ == "__main__":
    email = input("Enter email: ")
    phone = input("Enter phone: ")
    password = input("Enter password: ")

    print("Email:", "Valid" if validate_email(email) else "Invalid")
    print("Phone:", "Valid" if validate_phone(phone) else "Invalid")
    print("Password:", "Valid" if validate_password(password) else "Invalid")