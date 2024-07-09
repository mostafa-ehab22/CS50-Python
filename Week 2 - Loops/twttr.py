def main():
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    user_input = input("Input: ")
    output = []
    for char in user_input:
        if char not in vowels:
            output.append(char)
    print("".join(output))


main()


