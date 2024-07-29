import re


def main():
    hours = input("Hours: ").strip()

    if hours:
        print(convert(hours))
    else:
        raise ValueError("Invalid input")



def convert(string):
    # Capture hours and minutes using Regex
    pattern = r"(\d{1,2}):?(\d{1,2})? (AM|PM)"
    match = re.match(fr"^{pattern} to {pattern}$", string)

    if not match:
        raise ValueError("Invalid time format")

    # Assign Start & End hour/minutes
    start_hour, start_minutes, start_period, end_hour, end_minutes, end_period = match.groups()

    # Convert to 24H format
    start = format_to_24h(start_hour, start_minutes, start_period)
    end = format_to_24h(end_hour, end_minutes, end_period)

    return f"{start} to {end}"


def format_to_24h(hour, minutes, period):
    hour = int(hour)
    minutes = int(minutes) if minutes else 0

    if not (0 <= hour <= 12 and 0 <= minutes < 60):
        raise ValueError("Invalid time components")

    if period == "PM" and hour != 12:
        hour += 12
    elif period == "AM" and hour == 12:
        hour = 0

    return f"{hour:02}:{minutes:02}"



if __name__ == "__main__":
    main()
