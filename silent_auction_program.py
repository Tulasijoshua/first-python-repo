import os
print("********Welcome to The Silent Auction Program*********")
def find_winner(bidder_details):
    highest_bid = 0
    winner = ""
    for bidder in bidder_details:
        bidding_price  = bidder_details[bidder]
        if bidding_price > highest_bid:
            highest_bid = bidding_price
            winner = bidder
    print(f"Her is the list of all the bidders {bidder_details}")
    print(f"The winner is {winner} with a bid price of {highest_bid}")

silent_bids = {}
end_of_bidding = False
while not end_of_bidding:
    name = input('What is your name? ')
    bid = int(input('What is your bid? '))
    silent_bids[name] = bid
    another_bid = input("Do you have another bid? 'yes' or 'no':").lower()
    if another_bid == 'no':
        end_of_bidding = True
        find_winner(silent_bids)
    elif another_bid == 'yes':
        os.system('cls')

# while(another_bid == 'yes'):
#     name = input('What is your name? ')
#     bid = input('What is your bid? ')
#     silent_bids[name] = bid
#     another_bid = input('Do you have another bid? yes or no')
#
# print(silent_bids)
