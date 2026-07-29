from fractions import Fraction

def main():
    while True:
        try:
            i = input("Fraction: ")
            percent = convert(i)
            print(gauge(percent))
            break
        except (ValueError, ZeroDivisionError):
            pass

def convert(fraction):

    frac = Fraction(fraction)

    num = frac.numerator
    den = frac.denominator

    if den == 0:
        raise ZeroDivisionError
    if num < 0 or den < 0:
        raise ValueError
    if num > den:
        raise ValueError


    return int((num / den) * 100)


def gauge(percentage):

    if percentage <= 1:
        return("E")
    elif percentage >= 99:
        return("F")
    else:
        return(str(int(round(percentage, 0))) + "%")


if __name__ == "__main__":
    main()
