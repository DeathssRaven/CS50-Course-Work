from fractions import Fraction

# Loop through reprompting until no error with input
while True:
    try:
        item = input("Fraction:")
        frac = Fraction(item)
        num = (frac.numerator)  # Split top and bottom numbers
        den = (frac.denominator)
        if num > den:
            pass
        elif num < 0 or den < 0:
            pass
        else:
            break
    except (ValueError, ZeroDivisionError):
        pass

percentage = (num / den) * 100

if percentage <= 1:
    print("E")
elif percentage >= 99:
    print("F")
else:
    print(str(int(round(percentage, 0))) + "%")
