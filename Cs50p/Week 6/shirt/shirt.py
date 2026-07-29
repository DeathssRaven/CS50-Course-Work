from PIL import Image, ImageOps
import sys


input_file = sys.argv[1]
output_file = sys.argv[2]


if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

inName, inExtention = input_file.split(".")
outName, outExtention = output_file.split(".")
extentionsType = ["jpg", "jpeg", "png"]

if inExtention.lower() and outExtention.lower() not in extentionsType:
    sys.exit("Invalid output")

try:
    photo = Image.open(input_file)
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    sys.exit("Input does not exist")


if inExtention != outExtention:
    sys.exit("Input and output have different extensions")

shirtSize = shirt.size

photo_out = ImageOps.fit(photo, shirtSize)
photo_out.paste(shirt, shirt)
photo_out.save(output_file)
