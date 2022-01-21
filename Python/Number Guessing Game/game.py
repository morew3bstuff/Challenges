# Import
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(guess, answer, turns):
    if guess > answer:
        print(f"Too high!")
        return turns - 1
    elif answer > guess:
        print(f"Too low!")
        return turns - 1
    else:
        print(f"You got it!")

def set_difficulty():
    level = input("Choose a difficulty.Type 'easy' or 'hard': ")
    if level == 'easy':
        return EASY_LEVEL_TURNS
    elif level == 'hard':
        return HARD_LEVEL_TURNS

def game():
    answer = randint(1, 100)
    print("Welcome To Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    turns = set_difficulty()

    guess = 0
    while answer != guess:
        print(f"You have {turns} attempts remaning.")
        guess = int(input("Make a guess:"))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print(f"Out of attemps, you lose!")
            # To exit and end the function
            return
game()