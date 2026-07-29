from datetime import date
import inflect


def main():
    minutes = calc_minutes()
    print(inflect.engine().number_to_words(minutes).capitalize() + " minutes")


# get date of birth from user and validate it
def get_date():
    while True:
        try:
            year, month, day = map(int, input("Date: ").split("-"))
            return date(year, month, day)
        except ValueError:
            print("Invalid date")


# check if leap year
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# number of leap years since birth


def leap_years(start_year):
    count = 0
    for year in range(start_year, date.today().year):
        if is_leap(year):
            count += 1
    return count


def calc_minutes():
    today = date.today()
    birth_date = get_date()
    diff = today - birth_date
    minutes = diff.days * 24 * 60
    return minutes


if __name__ == "__main__":
    main()
