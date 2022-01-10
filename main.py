from replit import clear
#HINT: You can call clear() to clear the output in the console.

#logo
import art
print(art.logo)

bids = {}
bidding_finished = False 

while not bidding_finished: 
  name = input("What is your name?\n")
  bid = input("What is your bid? \n€")
  bids[name] = bid 
  again = input("Are there others who want to bid? Type yes or no\n").lower()
  clear()
  if again == "no":
    bidding_finished = True
    



for name in bids:
  amount = int(bids[name])
  highest_bid = 0 
  highest_name = ""
  if amount > highest_bid:
    highest_bid = amount 
    highest_name = name

print(f"{highest_name} won with a bid of €{highest_bid}")






