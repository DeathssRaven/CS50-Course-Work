from working import convert
import pytest


def main():
    test_valid()
    test_invalid()
    test_range()


def test_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("10:30 PM to 8:15 AM") == "22:30 to 08:15"
    assert convert("12 PM to 12 AM") == "12:00 to 00:00"
    assert convert("1 AM to 11 PM") == "01:00 to 23:00"
    assert convert("11:45 AM to 2:30 PM") == "11:45 to 14:30"


def test_invalid():
    with pytest.raises(ValueError):
        convert("9AM to 5PM")
    with pytest.raises(ValueError):
        convert("10:30PM to 8:15AM")
    with pytest.raises(ValueError):
        convert("12PM to 12AM")
    with pytest.raises(ValueError):
        convert("1AM to 11PM")
    with pytest.raises(ValueError):
        convert("11:45AM to 2:30PM")
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
    with pytest.raises(ValueError):
        convert("10:30 PM - 8:15 AM")
    with pytest.raises(ValueError):
        convert("12 PM - 12 AM")



def test_range():
    with pytest.raises(ValueError):
        convert("13 PM to 5 PM")
    with pytest.raises(ValueError):
        convert("10:60 PM to 8:15 AM")
    with pytest.raises(ValueError):
        convert("0 PM to 12 AM")
    with pytest.raises(ValueError):
        convert("1 AM to 13 PM")
    with pytest.raises(ValueError):
        convert("11:45 AM to 2:60 PM")







if __name__ == "__main__":
    main()
