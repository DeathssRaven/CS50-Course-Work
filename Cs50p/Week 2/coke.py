due = 50

print("Amount Due:", due)

while due > 0:
    given = int(input("Insert Coin: "))
    if given in (25, 10, 5):
        due = due - given
    if due > 0:
        print("Amount Due:", due)
    elif due <= 0:
        print("Change Owed:", abs(due))
