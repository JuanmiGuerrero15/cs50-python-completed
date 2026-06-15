#Pedir Input
def main():
    text = input("Input: ")
    print(vocal(text))

def vocal(s):
    result = ""

    for c in s:
        if c in ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]:
            continue
        else:
            result += c
    return "Output: " + result



main()

