# Program welcome message
print("Welcome to Tip Calculator!")

# Inputs and variables
billAmount = round(float(input("What is the bill amount: ")), 2)
numberOfPeople = int(input("How many people are splitting the bill: "))
tip = int(input("What percentage of tip would you like to give: "))

# Calculations
billAmountTip = round(billAmount + (billAmount * tip / 100), 2)
paymentAmountWithoutTip = round(billAmount / numberOfPeople, 2)
paymentAmountWithTip = round(billAmountTip / numberOfPeople, 2)

# Results
print("* Input Data")
print("-" * 100)
print(f"Bill amount without tips: {billAmount}$.")
print(f"Bill amount with tips: {billAmountTip}$.")
print(f"Number of people that pay: {numberOfPeople}.")
print(f"Tipping {tip}%.")
print()

print("* Results")
print("-" * 100)
print(f"Each person needs to pay {paymentAmountWithoutTip}$ if no tips are given.")
print(f"Each person needs to pay {paymentAmountWithTip}$ if a {tip}% tip is given.")
print()

print("* Comparison")
print("-" * 100)
print(f"It would cost each person an additional {paymentAmountWithTip - paymentAmountWithoutTip}$ to tip with a {tip}% tip percentage. ")