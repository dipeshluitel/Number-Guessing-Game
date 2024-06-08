from random import randint
from os import system
NUM = randint(1,99)
LEVEL = input("Which level you eant to play on? Type 'e' for easy 'h' for hard:  ").lower()
if LEVEL == "e":
    LIVES = 10
else:
    LIVES = 5
print(NUM)
def check(guess):
    if guess == NUM:
        return "guessed"
    elif guess<1:
        return "invalid"
    elif guess> NUM:
        return "higher"
    else:
        return "lower"
while LIVES!=0:
    print(f"You've {LIVES} lives")
    guess = int(input("Guess the number:  "))
    decision = check(guess)
    if decision == "guessed":
        system('cls')
        print(f"CONGRATULATIONS! You've guessed the correct number {guess}")
        exit()
    elif decision == "invalid":
        system('cls')
        print("Invalid number guessed, should be between (0-100)")
        LIVES-=1
    elif decision == "higher":
        system('cls')
        print(f"Guess the number below than {guess}")
        LIVES-=1
    elif decision == "lower":
        system('cls')
        print(f"Guess the number higher than {guess}")
        LIVES-=1
if(LIVES == 0):
    print("You've lost try Again!")
