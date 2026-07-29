from twttr import shorten


def main():
    test_twttr()


def test_twttr():
    assert shorten("Hello") == "Hll"
    assert shorten("Python") == "Pythn"
    assert shorten("Bye.") == "By."
    assert shorten("J0E") == "J0"

if __name__ == "__main__":
    main()
