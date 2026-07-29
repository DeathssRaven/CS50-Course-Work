c = input("camelCase: ")

l = 1
while l < len(c):
    if c[l].isupper():
        c = c[:l] + " " + c[l:]
        l += 1
    l += 1

s = c.lower().replace(" ", "_")

print("snake_case:", s)
