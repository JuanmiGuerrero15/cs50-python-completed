import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".py"):
    sys.exit ("Not a Python file")

else:
    program = 0
    code = sys.argv[1]
    try:
        with open(code, "r") as file:
            for line in file:
                line = line.lstrip()
                if line.startswith('#'):
                    program += 0
                elif line == "":
                    program += 0
                else:
                    program += 1
        print(program)

    except FileNotFoundError:
        sys.exit ("File does not exist")

