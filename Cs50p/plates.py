def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    if not s.isalnum():
        return False

    first_digit_index = -1
    for i, ch in enumerate(s):
        if ch.isdigit():
            first_digit_index = i
            break

    if first_digit_index != -1:
        if s[first_digit_index] == "0":
            return False

        for ch in s[first_digit_index:]:
            if ch.isalpha():
                return False

    return True


if __name__ == "__main__":
    main()
