lista = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

while True:
    try:
        date = input("Date: ").title()
        if '/' in date:
            month, day, year = date.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
            if day <= 31 and month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                pass
        elif ',' in date:
            month, day, year = date.replace(',', '').split(' ')
            year = int(year)
            day = int(day)
            month = lista[month]
            if day <= 31 and month <= 12:
                print(f"{year}-{month:02}-{day:02}")
                break
            else:
                pass

    except:
        pass
