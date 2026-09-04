import re

def main():
    print(parse(input("HTML: ")))


def parse(s):
    if src := re.search(r'<iframe[^>]*src="https?://(?:www\.)?youtube\.com/embed/([a-z0-9_-]+)', s, re.IGNORECASE):
        link = src.group(1)
        enlace = f"https://youtu.be/{link}"
        return enlace
    else:
        return None
...


if __name__ == "__main__":
    main()
