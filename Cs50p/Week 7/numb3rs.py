import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    if validate(ip):
        print(True)
        sys.exit(0)
    else:
        print(False)
        sys.exit(1)


def validate(ip):
    return bool(re.search(r"^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$", ip))


if __name__ == "__main__":
    main()

