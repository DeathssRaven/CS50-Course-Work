from seasons import CalcDate
from datetime import date


def test_initiate():
    valid_birthday = CalcDate(date(2000, 1, 2))
    assert valid_birthday.birthday.year == 2000
    assert valid_birthday.birthday.month == 1
    assert valid_birthday.birthday.day == 2
