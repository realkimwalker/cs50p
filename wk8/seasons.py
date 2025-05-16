from datetime import date, timedelta, datetime
import inflect
import sys
import operator


def main():
    year, month, day = get_todays_date()
    byear, bmonth, bday = get_birthdate(input("Date of Birth: ").split("-"))
    midnight_date = datetime(year, month, day)
    midnight_birthdate = datetime(byear, bmonth, bday)
    inflector = inflect.engine()
    days_in_mins = operator.__sub__(midnight_date, midnight_birthdate)
    days_int = (str(days_in_mins)).split(" ", 1)
    days_min = (int(days_int[0]) * 24 * 60)
    print(f'{inflector.number_to_words(days_min, andword="").capitalize()} minutes')


def get_birthdate(prompt):
        try:
            year, month, day = prompt
            return(int(year), int(month), int(day))
        except ValueError:
            sys.exit("Invalid date")


def get_todays_date():
    todays_date = date.today()
    year, month, day = str(todays_date).split("-")
    return(int(year), int(month), int(day))


if __name__ == "__main__":
    main()
