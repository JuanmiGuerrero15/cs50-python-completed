import re

def main():
    print(count(input("Text: ")))


def count(s):
    counter = 0
    for word in s.split():
        if re.search(r"\bum\b", word, re.IGNORECASE):
            counter += 1

    return counter


if __name__ == "__main__":
    main()
