from validator_collection import validators, checkers


def main():
    print(validate(input("What's your email address? ")))


def validate(s):
    try:
        if checkers.is_email(s) == True:
            return ("Valid")
        else:
            return ("Invalid")
    except validators.EmailNotValidError:
        return ("Invalid")


if __name__ == "__main__":
    main()
