import re


def main():
    tiempo = input("Hours: ")
    print(convert(tiempo))


def convert(s):
    hora = re.search(r"^([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM) to ([1-9]|1[0-2])(?::([0-5][0-9]))? (AM|PM)$", s)

    if hora is None:
        raise ValueError

    else:
        hour1, min1, day1, hour2, min2, day2 = hora.groups()

        hour1 = int(hour1)
        hour2 = int(hour2)


        if min1 is None:
            min1 = 0
        else:
            min1 = int(min1)

        if min2 is None:
            min2 = 0
        else:
            min2 = int(min2)


        if day1 == "AM":
            if hour1 == 12:
                hour1 = 0
        else:
            if hour1 != 12:
                hour1 += 12

        if day2 == "AM":
            if hour2 == 12:
                hour2 = 0
        else:
            if hour2 != 12:
                hour2 += 12

        time1 = f"{hour1:02}:{min1:02}"
        time2 = f"{hour2:02}:{min2:02}"



        return f"{time1} to {time2}"







if __name__ == "__main__":
    main()
