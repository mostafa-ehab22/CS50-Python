"""
1) Start -> min 2 letters
2) 2 <= characters <= 6
3) No periods, spaces, or punctuation marks are allowed.
4) Numbers cannot be used in the middle of a plate; they must come at the end.
   For example:
      AAA222 would be an acceptable vanity plate; AAA22A would not be acceptable. The first number used cannot be a 0.
"""

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s.isalnum():
        # If characters are all letters -> True
        if s.isalpha():
            return True
        else:
            ## Check for number in the middle
            #  ONLY if First two characters are letters & Last character is number
            if s[:2].isalpha() and s[-2:].isdigit():
                for i in range(len(s)):
                    if s[i].isdigit():
                        # Return False if number starts with 0 OR following character is letter
                        if s[i] == "0" or s[i+1].isalpha():
                            return False
                        else:
                            return True
            else:
                return False
    else:
        return False



if __name__ == "__main__":
    main()
