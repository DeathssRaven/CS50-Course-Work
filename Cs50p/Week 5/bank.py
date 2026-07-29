def main():
    greet = input("Greetings: ")
    print("$", value(greet))


def value(greeting):

    if greeting.strip().lower().startswith("hello"):
        return("$0")

    elif greeting[0].lower() in ("h"):
        return("$20")

    else:
        return("$100")


if __name__ == "__main__":
    main()
