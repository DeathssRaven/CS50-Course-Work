count = {}

while True:
    try:
        item = input().upper()
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    except EOFError:
        for item in sorted(count):
            print(f"{count[item]} {item}")
        break
