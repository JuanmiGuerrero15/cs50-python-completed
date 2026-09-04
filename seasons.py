from datetime import date
import sys
import inflect

def main():
    try:
        fecha = input("Date of Birth: ")
        fecha = date.fromisoformat(fecha)
        print(int_str(calculator(fecha)))

    except ValueError:
        sys.exit("Invalid date")

def calculator(d):
    today = date.today()
    time = today - d
    dias = int(time.days)
    minutos = dias * 24 * 60
    return minutos

def int_str(m):
    p = inflect.engine()
    result = p.number_to_words(m)
    result = result.replace(" and ", " ")
    result = result.capitalize()
    return f"{result} minutes"







...


if __name__ == "__main__":
    main()
