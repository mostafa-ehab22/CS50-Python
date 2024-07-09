def main():
    word = input("camelCase: ")

    snake_str = ""
    for char in word:
        if char.isupper():
            snake_str += "_" + char.lower()
        else:
            snake_str += char
    print( snake_str)


main()
