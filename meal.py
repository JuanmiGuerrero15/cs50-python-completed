def main():
    meal = convert(input("What time is it? "))
    if meal >= 7.0 and meal <= 8.0:
        print("Breakfast time")
    elif meal >= 12.0 and meal <= 13.0:
        print("Lunch time")
    elif meal >= 18.0 and meal <= 19.0:
        print("Dinner time")
    else:
        print(" ")

def convert(time):
    hour, minute = time.split(":")
    hour = float(hour)
    minute = float(minute)
    return hour + (minute / 60)

if __name__ == "__main__":
    main()
