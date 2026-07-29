e = input("Expression: ")

x, y, z = e.split(" ")

x = int(x)
z = int(z)

if y == "*":
    answer = x * z
    print(round(float(answer), 1))
elif y == "-":
    answer = x - z
    print(round(float(answer), 1))
elif y == "+":
    answer = x + z
    print(round(float(answer), 1))
elif y == "/":
    answer = x / z
    print(round(float(answer), 1))
