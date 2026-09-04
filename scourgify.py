import sys
import csv

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) >= 4:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit ("Not a CSV file")

else:
    code = sys.argv[1]
    code2 = sys.argv[2]
    try:
        file = open(code)
        reader = csv.DictReader(file)
        with open(code2, "w") as file:
            writer = csv.DictWriter(file, fieldnames=['first', 'last', 'house'])
            writer.writeheader()
            for row in reader:
                nombre = row['name']
                last, first = nombre.split(",")
                first = first.strip()
                writer.writerow({"first": first, "last": last, "house": row['house']})
        file.close()





    except FileNotFoundError:
        sys.exit (f"Could not read {code}")
