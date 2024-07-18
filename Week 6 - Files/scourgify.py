import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    else:
        file_1 = sys.argv[1]
        file_2 = sys.argv[2]


        try:
            with open(file_1) as input_file, open(file_2, "w") as output_file:
                reader = csv.DictReader(input_file)

                # Write new headers to output file 
                # Used as keys when writing rows
                headers = ["first","last","house"]
                writer = csv.DictWriter(output_file, fieldnames=headers)
                writer.writeheader()

                # Read input file
                for student in reader:
                    full_name = student["name"]
                    house = student["house"]

                    # Split full name into last name & first name
                    last_name, first_name = full_name.split(",")
                    first_name = first_name.strip()
                    last_name = last_name.strip()

                    # Write first, last & house to output file
                    writer.writerow({"first": first_name, "last": last_name, "house": house})

        except FileNotFoundError:
            sys.exit(f"Could not read {file_1}")


if __name__ == "__main__":
    main()
