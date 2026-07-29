def main():
    time = input("What time is it? ")
    time = convert(time)

    if time < 8.1 and time > 6.9:
        print("breakfast time")
    elif time < 13.1 and time > 11.9:
        print("lunch time")
    elif time < 19.1 and time > 17.9:
        print("dinner time")
    else:
        return 0


def convert(time):
    hours, minutes = map(int, time.split(":"))
    return hours + minutes / 60


if __name__ == "__main__":
    main()
