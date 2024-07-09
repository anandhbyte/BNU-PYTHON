import re

def validate_data():
    email = input("Enter your email address: ")
    phone = input("Enter your phone number: ")
    url = input("Enter a URL: ")
    password = input("Enter your password: ")

    # Simple regular expressions for validation
    email_regex = r'\S+@\S+\.\S+'
    phone_regex = r'\d{10}'  # assuming a 10-digit phone number
    url_regex = r'https?://(www\.)?(\w+\.\S+)'
    password_regex = r'.{8,}'  # Any character, minimum length of 8

    if not re.fullmatch(email_regex, email):
        print("Invalid Email address")
    if not re.fullmatch(phone_regex, phone):
        print("Invalid Phone number")
    if not re.fullmatch(url_regex, url):
        print("Invalid URL")
    if not re.fullmatch(password_regex, password):
        print("Invalid password. It should be a minimum of 8 characters long.")

# Run the function
validate_data()