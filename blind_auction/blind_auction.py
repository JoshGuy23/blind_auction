from art import logo
import os

def clear():
    os.system('cls')

print(logo)

print("Welcome to the secret auction program.")
bidders = {}
bidding = True

while bidding:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidders[name] = bid
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders != "yes":
        bidding = False
    clear()
    
max_bid = -1
winner = ""
for buyer in bidders:
    if bidders[buyer] > max_bid:
        max_bid = bidders[buyer]
        winner = buyer
        
print(f"The winner is {winner} with a bid of ${max_bid}.")