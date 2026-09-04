list = {

}
while True:
    try:
        item = input().upper()
        if item in list:
            list[item] += 1
        else:
            list[item] = 1

    except EOFError:
        break
for food in sorted(list):
    print(list[food], food)
