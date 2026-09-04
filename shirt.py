import sys
from PIL import Image, ImageOps

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) >= 4:
    sys.exit("Too many command-line arguments")

else:

    code = sys.argv[1]
    code2 = sys.argv[2]
    input_extension = code.lower().rsplit(".", 1)[1]
    output_extension = code2.lower().rsplit(".", 1)[1]

    if input_extension not in ("jpg", "jpeg", "png"):
        sys.exit ("Invalid Input")

    elif input_extension != output_extension:
        sys.exit ("Input and output have different extensions")

    else:
        try:
            muppet = Image.open(code)
            shirt = Image.open("shirt.png")
            size = shirt.size
            muppet = ImageOps.fit(muppet, size)
            muppet.paste(shirt, shirt)
            muppet.save(code2)

        except FileNotFoundError:
            sys.exit (f"Could not read {code}")
