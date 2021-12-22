# Import 
from artModule import *
import os

# Logo
print(logo)

bids = {}
bidding_finished = False

def winner(record):
    high = 0
    winner = ""
    for bidder in record:
        bid_amount = record[bidder]
        if bid_amount > high:
            high = bid_amount
            winner = bidder
    print(f"The winner is {winner} and won with a bid of {high}.")

while not bidding_finished:
    name = input("What's your name: ")
    price = int(input("What's your bid: "))
    bids[name] = price
    others = input("Are there any other bidders ('yes', 'no'): ")
    if others == 'no':
        bidding_finished = True
        winner(bids)
    elif others == 'yes':
        os.system("clear")
