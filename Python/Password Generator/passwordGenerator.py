import random

print("Welcome to Password Generator!")
lettersNo = int(input("How many letters should your password have: "))
symbolNo = int(input("How many symbols should your password have: "))
numberNo = int(input("How many numbers should your password have: "))
passwordLength = lettersNo + symbolNo + numberNo

letterCount = 0
symbolCount = 0
numberCount = 0

password = ""

letters = ['z', 'x', 'c', 'v', 'b', 'n', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k']
numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"]

for index in range(0, passwordLength):
    if letterCount < lettersNo:
       add = random.choice(letters)
       password += add
       letterCount += 1
    if symbolCount < symbolNo:
       add = random.choice(symbols)
       password += add
       symbolCount += 1
    if symbolCount < symbolNo:
       add = str(random.choice(numbers))
       password += add
       numberCount += 1

print(f"Generated Password is: {password}.")