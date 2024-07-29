import validators


def main():
    print(validate(input("What's your email address? ")))


def validate(string):
    if validators.email(string) == True:
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
