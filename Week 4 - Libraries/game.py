import sys
from random import randint


def main():
    while True:
        try:
            level = int(input("Level: "))
            random_num = randint(1,level)

            while True:
                guess = int(input("Guess: "))
                if guess > random_num:
                    print("Too large!")
                elif guess < random_num:
                    print("Too small!")
                else:
                    print("Just right!")
                    sys.exit()

        except ValueError:
             print("Enter an integer")


main()
