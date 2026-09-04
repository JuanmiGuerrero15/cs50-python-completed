while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        y= int(y)
        x= int(x)
        if x > -1 and y > -1:
            if x <= y:
                fuel = x / y
            else:
                fuel = 0/0
        else:
            fuel = 0/0
    except ValueError:
        pass
    except ZeroDivisionError:
        pass
    else:
        break

percent = round(fuel * 100)


if percent >= 99:
    print("F")
elif percent <= 1:
    print("E")
else:
    print(f"{percent}%")
