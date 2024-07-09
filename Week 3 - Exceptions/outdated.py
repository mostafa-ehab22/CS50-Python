months_name = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# MM/DD/YYYY --> YYYY/MM/DD

def main():
    while True:
        try:
            date = input("Date: ").strip()
            if not is_valid_format(date):
                raise ValueError
            converted_date = get_date(date)
            print(converted_date)
            break

        except ValueError:
            print("Invalid data")
            pass



def is_valid_format(d):
    if "/" in d:
        parts = d.split("/")
        if len(parts) != 3:
            return False
        else:
            month = parts[0]
            day = parts[1]
            return month.isdigit() and (1 <= int(month) <= 12 and 1 <= int(day) <= 31)

    elif "," in d:
        parts = d.replace("," , "").split()
        month = parts[0]
        day = parts[1]
        return month in months_name and 1 <= int(day) <= 31

    return False


def get_date(d):
    if "/" in d:
        month, day, year = d.split("/")
    else:
        month, day, year = d.replace("," , "").split()
        if month in months_name:
            month = months_name.index(month) + 1

    month = int(month)
    day = int(day)
    year = int(year)

    return f"{year:04}-{month:02}-{day:02}"





if __name__ == "__main__":
    main()
