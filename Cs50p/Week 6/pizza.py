import sys
import csv
from tabulate import tabulate

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")


pizza_type = sys.argv[1]

with open(pizza_type, "r") as file:
    reader = csv.reader(file)
    table = list(reader)


print(tabulate(table, headers="firstrow", tablefmt="grid"))


