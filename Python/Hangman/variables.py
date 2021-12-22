import random
from wordList import *

# Variables
display = []
endOfGame = False
lives = 6

# Randomly chose a word from the word list and assign it to a variable called chosen word.
chosenWord = random.choice(wordList)
wordLen = len(chosenWord)