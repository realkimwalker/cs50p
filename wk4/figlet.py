import sys
from pyfiglet import Figlet
import random

def main():
    figlet = Figlet()
    fonts = []
    fonts = figlet.getFonts()
    if len(sys.argv) == 1:
        font = random.choice(fonts)
        figlet.setFont(font=font)
    elif len(sys.argv) == 3:
        if ((sys.argv[1] == "-f") or (sys.argv[1] == "--font")):
            font = sys.argv[2]
            if font in fonts:
                figlet.setFont(font=font)
            else:
                sys.exit("Invalid Usage")
        else:
            sys.exit("Invalid Usage")
    else:
        sys.exit("Invalid Usage")

    text = (str(input("Input: ")))
    print("Output: ")
    print(figlet.renderText(text))


main()
