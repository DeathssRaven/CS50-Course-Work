def convert(txt):
    return txt.replace(":)", "🙂").replace(":(", "🙁")


def main():
    txt = input()
    result = convert(txt)
    print(result)


main()
