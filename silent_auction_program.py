silent_bids = {}

name = input('What is your name? ')
bid = input('What is your bid? ')
silent_bids[name] = bid
print(silent_bids)

another_bid = input('Do you have another bid? yes or no')

while(another_bid == 'yes' or another_bid == 'Yes' or another_bid == 'YES'):
    name = input('What is your name? ')
    bid = input('What is your bid? ')
    silent_bids[name] = bid
    another_bid = input('Do you have another bid? yes or no')

print(silent_bids)
