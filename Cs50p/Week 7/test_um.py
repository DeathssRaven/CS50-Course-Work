from um import count


def main():
    test_count()
    test_range()


def test_count():
    assert count("um") == 1
    assert count("Um, thanks for the album.") == 1
    assert count("Um, thanks, um...") == 2


def test_range():
    assert count("um") == 1
    assert count("Ummm") == 0
    assert count("ummmmmm") == 0


if __name__ == "__main__":
    main()
