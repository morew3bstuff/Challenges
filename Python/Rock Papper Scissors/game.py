# Imports
import random

# Input And Variables
choice = input("What do you chose? Rock Paper or Scissors?:").lower()
print()

# Computer Choice
computerPickList = ["rock", "papper", "scissors"]
computerPick = random.choice(computerPickList)

# ASCII Art
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papper = '''
    _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

artDict = {"rock" : rock, "papper": papper, "scissors" : scissors}

# Output
print(f"You chose {choice}.")
print(artDict[choice])
print()
print(f"Computer chose {computerPick}.")
print(artDict[computerPick])
print()

if choice == "rock" and computerPick == "scissors":
    print("You win!")
elif choice == "rock" and computerPick == "papper":
    print("You lose!")
elif choice == "rock" and computerPick == "rock":
    print("It's a draw!")
elif choice == "papper" and computerPick == "scissors":
    print("You lose!")
elif choice == "papper" and computerPick == "papper":
    print("It's a draw!")
elif choice == "papper" and computerPick == "rock":
    print("You win!")
elif choice == "scissors" and computerPick == "scissors":
    print("It's a draw!")
elif choice == "scissors" and computerPick == "papper":
    print("You win!")
elif choice == "scissors" and computerPick == "rock":
    print("You lose!")