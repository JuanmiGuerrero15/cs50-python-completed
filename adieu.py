import inflect

p = inflect.engine()
list = []

while True:
    try:
        name = input("Name: ")
        list.append(name)

    except EOFError:
        print((), sep='')
        break

final = p.join(list)

print(f"Adieu, adieu, to {final}")
