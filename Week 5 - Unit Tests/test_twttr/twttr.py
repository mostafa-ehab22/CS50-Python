def main():
    no_vowels_word = shorten(input("Input: ").strip())
    print(f"Output: {no_vowels_word}")


def shorten(word):
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    output = [char for char in word if char not in vowels]
    return ( "".join(output) )


if __name__ == "__main__":
    main()
