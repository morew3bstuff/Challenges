print("Welcome To Python Pizza Delivery!")
# Input and Variables
size = input("What size pizza do you want?(S, M, L):")
add_pepperoni = input("Add pepperoni?(Y, N):")
extra_cheese = input("Do you want extra cheese?(Y, N):")

# Small Pizza
if size == "S":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print(f'Your bill is {15 + 2 + 1}$, pizza {15}$, pepperoni {2}$, cheese {1}$.')
        elif extra_cheese == "N":
            print(f'Your bill is {15 + 2}$, pizza {15}$, pepperoni {2}$.')
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            print(f'Your bill is {15 + 1}$, pizza {15}$, cheese {1}$.')
        elif extra_cheese == "N":
             print(f'Your bill is {15}$, pizza {15}$.')
# Medium Pizza
elif size == "M":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print(f'Your bill is {20 + 3 + 1}$, pizza {20}$, pepperoni {3}$, cheese {1}$.')
        elif extra_cheese == "N":
            print(f'Your bill is {20 + 3}$, pizza {20}$, pepperoni {3}$.')
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            print(f'Your bill is {20 + 1}$, pizza {20}$, cheese {1}$.')
        elif extra_cheese == "N":
             print(f'Your bill is {20}$, pizza {20}$.')
# Large Pizza
elif size == "L":
    if add_pepperoni == "Y":
        if extra_cheese == "Y":
            print(f'Your bill is {25 + 3 + 1}$, pizza {25}$, pepperoni {3}$, cheese {1}$.')
        elif extra_cheese == "N":
            print(f'Your bill is {25 + 3}$, pizza {25}$, pepperoni {3}$.')
    elif add_pepperoni == "N":
        if extra_cheese == "Y":
            print(f'Your bill is {25 + 1}$, pizza {25}$, cheese {1}$.')
        elif extra_cheese == "N":
             print(f'Your bill is {25}$, pizza {20}$.')