punishemnt_text = "I will not litter."
number_of_repetitions = 25


def bart_cheat_while():
    reps = 0
    while reps < number_of_repetitions:
        print(f"{reps}: {punishemnt_text}")
        reps += 1

def bart_cheat_for():        
    for i in range(number_of_repetitions):
        print(f"{i+1}: {punishemnt_text}")
