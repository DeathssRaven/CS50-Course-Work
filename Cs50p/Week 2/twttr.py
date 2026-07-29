i = input("Input:")

vowel = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

remove = ""

for letter in i:
    if letter not in vowel:
        remove += letter

print("Output:", remove)
