# Start -> min 2 letters
# 2 <= characters <= 6
# Numbers cannot be used in the middle of a plate; they must come at the end. For example,
#       AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a 0.
# No periods, spaces, or punctuation marks are allowed.


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        # Return true if characters are all letters
        if s.isalpha():
            return True
        else:
            # Check for number in the middle
            # (only if the first two characters are letters and the last character is number)
            if s[:2].isalpha() and s[-2:].isdigit():
                for i in range(len(s)):
                    if s[i].isdigit():
                        # Return false if number starts with 0 or the following character is letter
                        if s[i] == "0" or s[i+1].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False




main()
