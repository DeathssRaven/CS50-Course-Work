import sys

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a python file")

code = sys.argv[1]
count = 0

with open(code, "r") as file:
    lines = file.readlines()

for line in lines:
    if not line.isspace() and not line.lstrip().startswith("#"):
        count += 1



print(count)
