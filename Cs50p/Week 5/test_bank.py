from bank import value


def main():
    test_bank()


def test_bank():
    assert value("Hello") == 0
    assert value("Greetings") == 100
    assert value("Howdy") == 20


if __name__ == "__main__":
    main()
