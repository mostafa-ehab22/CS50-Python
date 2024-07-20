from tabulate import tabulate
import sys
import csv

def main():
    # Exactly 1 file is given by user
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    else:
        filename = sys.argv[1]
        # Check File Type
        if not filename.endswith(".csv"):
            sys.exit("Not a CSV file")

        try:
            # Read File
            with open(filename) as file:
                    reader = csv.reader(file)
                    rows = [row for row in reader]

            # Tabulate data
            print(tabulate(rows,headers="firstrow",tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()

