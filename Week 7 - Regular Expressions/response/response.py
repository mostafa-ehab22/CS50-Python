import validators


def main():
    email_address = input("What's your email address? ") 
    print(validate(email_address))


def validate(string):
    if validators.email(string):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
