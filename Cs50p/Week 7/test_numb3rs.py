from numb3rs import validate


def main():
    test_ip()
    test_format()
    test_range()


def test_ip():
    assert validate("1.2.3.4") == True
    assert validate("256.100.50.25") == False
    assert validate("192.168.1") == False
    assert validate("abc.def.ghi.jkl") == False
    assert validate("000.001.010.100") == False


def test_format():
    assert validate(r"1.2.3.4") == True
    assert validate(r"1.2.3") == False
    assert validate(r"1.2") == False
    assert validate(r"1.2.3.") == False
    assert validate(r"1") == False


def test_range():
    assert validate(r"255.255.255.255") == True
    assert validate(r"255.255.500.500") == False
    assert validate(r"1000.1000.1000.1000") == False
    assert validate(r"255.1000.1000.1000") == False
    assert validate(r"255.255.255.256") == False


if __name__ == "__main__":
    main()
