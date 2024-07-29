import re
import sys


def main():
    user_input = input("Text: ")

    if user_input:
        print(count(user_input))
    else:
        print("No input provided")


def count(string):
    # Using word boundary matching isolated "um" only
    pattern = r"\bum\b"

    matches = re.findall(pattern, string, re.IGNORECASE)


    return len(matches)



if __name__ == "__main__":
    main()
