from art import logo
import os

auction = {}


def add_bid():
    os.system('cls')
    print(logo)
    player_name = input("What is your name: ")
    player_bid = 0
    while player_bid < 1:
        player_bid = float(input("What is your bid? Minimum of $1 $"))
    auction[player_name] = player_bid


add_bid()


while True:
    more_bidders = input("Are there more bidders? Enter `no` to end auction or anything else to take another bid: ").casefold()
    if more_bidders == 'n' or more_bidders == 'no':
        break
    else:
        add_bid()


high_bid = 0
winner = None
tied_auction = False
for name, bid in auction.items():
    if bid > high_bid:
        high_bid = bid
        winner = name

# check for duplicate highest bid
num_bids = 0
for bid in auction.values():
    if bid == high_bid:
        num_bids += 1
if num_bids > 1:
    tied_auction = True

if tied_auction:
    print(f"There was more than one equal highest bid of ${high_bid:.2f}. We need to run the auction again!")
else:
    print(f"The winner is {winner} with a bid of ${high_bid:.2f}")
