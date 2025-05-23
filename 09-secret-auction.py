bids = {}


def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  for bidder in bidding_record:
    if bidding_record[bidder] > highest_bid:
      highest_bid = bidding_record[bidder]
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

bidding_finished = False
while not bidding_finished:
  name = input("Enter your name? ")
  bid = int(input("Enter your bid? $"))
  bids[name] = bid
  should_continue = input("Are there any other bidders? Type 'yes' or 'no'. ")
  if should_continue == "no":
    bidding_finished = True
  elif should_continue == "yes":
    pass
  
find_highest_bidder(bids)