import os

os.system('cls')
guessed_number = None
num_to_guess = int(input("Enter a number for Player 2 to guess: "))
os.system('cls')
tries = 10

while guessed_number != num_to_guess and tries >= 0:
    print(f"You have {tries} tries")
    guessed_number = int(input("Enter your guess: "))
    tries -= 1
    if guessed_number == num_to_guess:
        print(f"You did it! Number of tries: {11-tries}")
    elif guessed_number > num_to_guess:
        print("Try again! The number is lower")
    elif guessed_number < num_to_guess:
        print("Try again! The number is highers")
if tries <= 0 and guessed_number != num_to_guess:
    print("Game Over")