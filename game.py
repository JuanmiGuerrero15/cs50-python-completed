import random

while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except ValueError:
        pass


while True:
    try:

        level_random = random.randrange(1, level+1)
        guess = int(input("Guess: "))
        if guess > 0:
            if guess > level_random:
                print("Too large!")
            elif guess < level_random:
                print("Too small!")
            else:
                print("Just right!")
                break

    except ValueError:
        pass

