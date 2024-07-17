"""
Program counts file's lines excluding:
    Blank lines
    Single-line comments
"""
import sys

def main():
    # Command-line argv != 2
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")

    # Command-line argv == 2
    else:
        entry = sys.argv[1]
        lines_count = 0

        # Not Python file
        if not entry.endswith(".py"):
            sys.exit("Not a Python file")

        # Count lines of file
        try:
            with open(entry) as file:
                for line in file:
                    stripped_line = line.strip()
                    ## Not blank-line & Not single-line comment
                    if stripped_line and not stripped_line.startswith("#"):
                        lines_count += 1
            print(f"Lines count: {lines_count}")
        except FileNotFoundError:
            sys.exit("File does not exist")
        except Exception as e:
            sys.exit(f"An error occured: {e}")



if __name__ == "__main__":
    main()
