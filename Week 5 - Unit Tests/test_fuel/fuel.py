def main():
    percentage = convert(input("Fraction: "))
    print(gauge(percentage))


def convert(fraction):
    x, y = fraction.split("/")
    if int(x)/int(y) > 1:
        raise ValueError
    elif int(y) == 0:
        raise ZeroDivisionError
    return (int(x)/int(y) * 100)


def gauge(percentage):
        try:
            if 0 <= percentage <= 1:
                return "E"
            elif 99 <= percentage <= 100:
                return "F"
            elif 1 < percentage < 99:
                return f"{int(percentage)}%"

if __name__ == "__main__":
    main()
