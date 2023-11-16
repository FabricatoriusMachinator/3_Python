import random

i = 0
yhatzee = False
while yhatzee != True:
    i += 1
    diceCup = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]

    for dice in range(len(diceCup)):
        if diceCup[0] != diceCup[dice]:
            break
    else:
        yhatzee = True
        print(i)

    

