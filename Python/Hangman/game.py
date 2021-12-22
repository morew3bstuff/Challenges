# Import
from artModule import *
from variables import *

# Game logo
print(logo)

# Create an empty list called display, for each letter in the chosen word add a "_" to "display".
for _ in range(wordLen):
    display += '_'

# Use a loop to let the user guess again
while not endOfGame:
    # Ask the user to guess a letter and assign thier answer to a variable called guess.
    guess = input("Guess a letter: ").lower()
    guessLen = len(guess)

    if guess in display:
        print(f"You've allready guessed {guess}.")

    # One letter at a time
    if guessLen == 1:
        # Check if the letter the user guessed is one of the letters in the chosen word.
        # Loop throught each position in the chosen word:
        # If the letter at the position matches 'guess' then reveal the latter in the display
        for position in range(wordLen):
            letter = chosenWord[position]
            if letter == guess:
                display[position] = letter

        # Remove a live if letter not in chosen word
        if guess not in chosenWord:
            print(f"You've guessed {guess} and it's not in the word, you lose a live!")
            lives -= 1
            # If no lives left exit the while loop
            if lives == 0:
                endOfGame = True
                print("You lose!")

        # Print 'display' and you should see the guessed letter in the correct position and every other letter '_'.
        print(f"{' '.join(display)}")

        if '_' not in display:
            endOfGame = True
            print("You win!")

        print(stages[lives])        
    # If more than one letter provided
    else:
        print("Just one letter at a time!")
