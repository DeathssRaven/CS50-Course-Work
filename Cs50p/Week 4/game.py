import random
import sys


while True:
    try:
        level = int(input("Level:"))

        if level > 0:
            break

    except ValueError:
        pass


num = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess:"))

        if guess < 1:
            continue

        if guess < num:
            print("Too small!")
        elif guess > num:
            print("Too large!")
        else:
            print("Just right!")
            sys.exit(0)

    except ValueError:
        pass
        