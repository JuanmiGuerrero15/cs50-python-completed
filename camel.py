def main():
    text = input("camelCase: ")
    print(where(text))

def where(s):
    result = ""

    for c in s:
        if c.isupper():
            result +=  "_" + c.lower()
        else:
            result += c
    return "snake_case: " + result



main()
