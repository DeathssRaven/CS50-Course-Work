import random


def main():
    l = get_level()
    score = 0

    for i in range(10):
        t = 0

        result1 = generate_integer(l)
        result2 = generate_integer(l)

        while t < 3:
            try:
                question = int(input(f"{result1} + {result2} = "))

                answer = result1 + result2

                if question == answer:
                    score += 1
                    break
                else:
                    print("EEE")
                    t += 1

            except ValueError:
                print("EEE")
                t += 1

        if t == 3:
            print(answer)

    print("Score:", score)


def get_level():
    while True:
        try:

            level = int(input("Level:"))

            if level in (1, 2, 3):
                return level

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randrange(0, 10)
    elif level == 2:
        return random. randrange(10, 100)
    else:
        return random.randrange(100, 1000)


if __name__ == "__main__":
    main()
