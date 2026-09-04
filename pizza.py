import sys
import csv
from tabulate import tabulate

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

elif len(sys.argv) >= 3:
    sys.exit("Too many command-line arguments")

elif not sys.argv[1].endswith(".csv"):
    sys.exit ("Not a CSV file")

else:
    code = sys.argv[1]
    try:
        with open(code) as file:
            reader = csv.DictReader(file)
            headers = reader.fieldnames
            table = []
            for row in reader:
                table.append(list(row.values()))



            print(tabulate(table, headers, tablefmt="grid"))



    except FileNotFoundError:
        sys.exit ("File does not exist")
