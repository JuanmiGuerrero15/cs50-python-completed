

saludo = input("Greeting: ").lower().strip()
if saludo.startswith("hello"):
    print("$0")
elif saludo.startswith("h"):
    print("$20")
else:
    print("$100")

