import inflect

p = inflect.engine()

def main():
    names = []

    while True:
        try:
            name_input = input("Name: ").strip().title()
            names.append(name_input)

        except EOFError:
            print(f"Adieu, adieu, to {p.join(names)}")
            break

main()
