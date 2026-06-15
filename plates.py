def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(p):
    if len(p) < 2 or len(p) > 6:
        return False

    if not p[0:2].isalpha():
        return False

    seen_number = False

    for w in l:
        if w.isalpha():
            if seen_number:
                return False

        elif w.isdigit():
            if not seen_number:
                if w == "0":
                    return False
                seen_number = True

        elif w.isdecimal():








main()
