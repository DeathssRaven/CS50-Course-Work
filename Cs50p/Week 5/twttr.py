

def main():
    i = str(input("Input:"))

    print("Output:", shorten(i))


def shorten(word):

    new_word= ""

    for char in word:
        if char.lower() not in ["a", "e", "i", "o", "u"]:
            new_word += char
    return new_word


if __name__ == "__main__":
    main()
