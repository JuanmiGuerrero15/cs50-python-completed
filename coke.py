result = 50

while result > 0:
    print("Amount Due:", result)
    coin = int(input("Insert Coin: "))
    if coin in [5, 10, 25]:
        result -= coin
print("Change Owed:", abs(result))










