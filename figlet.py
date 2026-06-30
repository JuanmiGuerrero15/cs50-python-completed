from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fonts = figlet.getFonts()
random_font = random.choice(fonts)


if len(sys.argv)== 1:
    texto = input("Input: ")
    figlet.setFont(font=random_font)
    print(figlet.renderText(texto))

elif sys.argv[1] == "-f" or sys.argv[1] == "--font":
    selected_font = sys.argv[2]
    if selected_font not in figlet.getFonts():
        sys.exit("Invalid usage")
    else:
        texto = input("Input: ")
        figlet.setFont(font=selected_font)
        print(figlet.renderText(texto))

else:
    sys.exit("Invalid usage")

