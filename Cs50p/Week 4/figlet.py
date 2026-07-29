import pyfiglet
import sys
import random


f = pyfiglet.Figlet()
fonts = f.getFonts()


if len(sys.argv) == 1:
    font = random.choice(fonts)
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
    font = sys.argv[2]
    if font not in fonts:
        sys.exit(1)
else:
    sys.exit(1)

text = input("Input:")

f.setFont(font=font)
print(f.renderText(text))
