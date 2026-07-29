def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):

    number = d.replace("$", "")
    return round(float(number), 2)


def percent_to_float(p):

    perc = p.replace("%", "")
    return round(float(perc) / 100, 2)


main()
