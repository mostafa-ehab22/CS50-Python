import random


def main():
    level = get_level()
    problems_count = 0
    score = 0


    while problems_count < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 0


        while tries < 3:
            try:
                answer = int(input(f"{x} + {y} = "))

                if answer == (x + y):
                    score += 1
                    break
                else:
                    print("EEE")
                    tries += 1
            except ValueError:
                print("Invalid input. Please enter a number!")

        if tries == 3:
                print(f"{x} + {y} = {x + y}")

        problems_count += 1

    print(f"Score: {score}")


def get_level():
        while True:
            try:
                level = int(input("Level: "))
                if level in range(1,4):
                    return level
            except ValueError:
                 print("Please Choose Valid Level (1-3)")


def generate_integer(level):
    if level == 1:
         return random.randint(0,9)
    elif level == 2:
        return random.randint(10,99)
    else:
        return random.randint(100,999)



if __name__ == "__main__":
    main()






