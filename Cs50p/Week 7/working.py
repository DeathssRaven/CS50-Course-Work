import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    matches = re.search(r"^(1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM) to (1[0-2]|[1-9])(:[0-5][0-9])? (AM|PM)$", s)
    if not matches:
        raise ValueError("Invalid format")
    else:
        hour1 = int(matches.group(1))
        hour2 = int(matches.group(4))
        minute1 = int(matches.group(2).split(":")[1]) if matches.group(2) else 0
        minute2 = int(matches.group(5).split(":")[1]) if matches.group(5) else 0

        if matches.group(3) == "PM" and hour1 != 12:
            hour1 += 12
        elif matches.group(3) == "AM" and hour1 == 12:
            hour1 = 0
        if matches.group(6) == "PM" and hour2 != 12:
            hour2 += 12
        elif matches.group(6) == "AM" and hour2 == 12:
            hour2 = 0

    return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"


...


if __name__ == "__main__":
    main()
