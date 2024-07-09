from random import choice
from sys import argv
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

def main():
    if len(argv) == 1:
        text = input("Input: ")
        random_font = choice(fonts)
        figlet.setFont(font=random_font)
        print(f"Output:\n{figlet.renderText(text)}")

    elif len(argv) == 3 and (argv[1] == "-f" or argv[1] == "--font"):
        chosen_font = argv[2]
        if chosen_font in fonts:
            text = input("Input: ")
            figlet.setFont(font=chosen_font)
            print(f"Output:\n{figlet.renderText(text)}")
        else:
            exit("Invalid usage")
    else:
        exit("Invalid usage")


main()
