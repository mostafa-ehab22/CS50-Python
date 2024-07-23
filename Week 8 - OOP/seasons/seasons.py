import inflect
import re
import sys
from datetime import date, datetime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __sub__(self, other):
        """Calculate number of days between two Date objects."""
        # Using date() => Create date objects from year, month, day
        self_date = date(self.year, self.month, self.day)
        other_date = date(other.year, other.month, other.day)

        # Calculate difference in days
        difference = self_date - other_date
        return difference.days

    def to_datetime(self):
        """Convert Date object to datetime.datetime with time set to midnight."""
        return datetime(self.year, self.month, self.day)

    @classmethod
    def from_string(cls, date_string):
        """Create and return a Date object using the parsed year, month, and day."""
        try:
            year, month, day = map(int, date_string.split("-"))
            return cls(year, month, day)
        except ValueError:
            sys.exit("Date must be in YYYY-MM-DD format")


def valid_date_format(date):
    """Validates a date in the format YYYY-MM-DD"""
    match = re.match(r"^\d{4}-\d{2}-\d{2}$", date)
    if match:
        return True
    else:
        return False

def main():
    p = inflect.engine()

    # Get user input
    birth = input("Date of birth (YYYY-MM-DD): ").strip()

    if valid_date_format(birth):

        try:

            birth_date = Date.from_string(birth)

            # Get today's date
            today = date.today()

            # Create a Date object by directly accessing date.today() attributes
            today_date = Date(today.year, today.month, today.day)

            # Calculate days passed since birth
            days_passed = today_date - birth_date

            # Convert days to minutes (1440 minutes in a day)
            minutes_passed = days_passed * 1440

            # Convert minutes to words
            minutes_words = p.number_to_words(minutes_passed, andword="").capitalize()

            print(f"{minutes_words} minutes")

        except ValueError as e:
            print(e)
    else:
        sys.exit("Invalid date")


if __name__ == "__main__":
    main()
