import requests
import json
import sys

try:
    if len(sys.argv)== 1:
        sys.exit("Missing command-line argument")

    try:
        n = float(sys.argv[1])
        response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=b5dbea046685a9dc8e8631e4cdbc55946ac67682beea0c7202174f8295e2f77a")
        o = response.json()
        dentro = (o["data"])
        valor = float(dentro["priceUsd"])
        conversión = valor * n
        print(f"${conversión:,.4f}")
    except ValueError:
        sys.exit("Command-line is not a number")



except requests.RequestException:
    pass

