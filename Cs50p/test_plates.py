from plates import is_valid


def test_length():
    assert is_valid("CS50") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False


def test_start_with_letters():
    assert is_valid("CS50") == True
    assert is_valid("50CS") == False
    assert is_valid("C550") == False


def test_numbers_position():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("CS50P") == False


def test_no_punctuation():
    assert is_valid("CS50") == True
    assert is_valid("CS50!") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS-50") == False
