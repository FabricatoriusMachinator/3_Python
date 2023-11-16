import random


dice = [1, 2, 3, 4, 5, 6]
n_dices = 5

i = 0
yhatzee = False
while yhatzee != True:
    i += 1
    rand_dices = random.choices(dice, k=n_dices)

    for d in range(len(rand_dices)):
        if rand_dices[0] != rand_dices[d]:
            break
    else:
        yhatzee = True
        print(i)

    

