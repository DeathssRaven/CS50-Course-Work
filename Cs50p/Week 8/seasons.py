from datetime import date
import inflect
import sys

p = inflect.engine()


class CalcDate:
    def __init__(self, birthday):
        self.birthday = birthday
        self.today = date.today()

    @staticmethod
    def getbirth():
        birthday = input("Date: ")
        try:
            birthday = date.fromisoformat(birthday)
            return CalcDate(birthday)
        except ValueError:
            sys.exit("Invalid date")

    def convertdate(self):
        dayslived = (self.today-self.birthday).days
        minutes = dayslived * 24 * 60
        words = p.number_to_words(minutes, andword="")
        return words.capitalize() + " minutes"


def main():
    birthday = CalcDate.getbirth()
    result = birthday.convertdate()
    print(result)


if __name__ == "__main__":
    main()
