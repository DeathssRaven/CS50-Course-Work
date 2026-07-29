import inflect
p = inflect.engine()

names = []

while True:
    try:
        name = input("Name:").capitalize()

        names.append(name)

    except EOFError:
        s = p.join(names)
        print("\nAdieu, adieu, to", s)
        break
