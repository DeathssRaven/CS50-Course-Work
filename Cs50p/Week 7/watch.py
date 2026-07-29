import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if re.search(r"iframe.*src", s):
        matches = re.search(r"youtube\.com/embed/([a-zA-Z0-9_-]+)", s)
        if matches:
            return f"https://youtu.be/{matches.group(1)}"
        return None
    return None


...


if __name__ == "__main__":
    main()
