import os                                                                               # imports os library for clearing the screen
from art import logo                                                                    # import the ASCII logo

# Create a function for clearing the screen, with logic for the particular OS being used.
def clear():
    os.system('cls' if os.name=='nt' else 'clear')

# Print the ASCII logo
print(logo)

# Print the introductory message.
print("Welcome to the secret auction program.")
bidders = {}                                                                            # Dictionary for bids.
bidding = True                                                                          # Boolean to determine whether the loop runs.

# The loop continues as long as "yes" is entered by the user at the final question
while bidding:
    name = input("What is your name?: ")                                                # Get the current user's name.
    bid = int(input("What's your bid?: $"))                                             # Get the current user's bid.
    bidders[name] = bid                                                                 # Store the user's bid in the dictionary.
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()  # Prompt the user to continue the loop if there are more bidders.
    if more_bidders != "yes":
        bidding = False
    clear()                                                                             # Clear the console.
    
max_bid = -1                                                                            # The maximum bid all users made.
winner = ""                                                                             # The name of the winning bidder.

# For every entry in the dictionary, find the highest bid and its corresponding bidder.
for buyer in bidders:
    if bidders[buyer] > max_bid:
        max_bid = bidders[buyer]
        winner = buyer
        
print(f"The winner is {winner} with a bid of ${max_bid}.")
