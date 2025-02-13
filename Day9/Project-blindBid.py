# STEP 1 : GET THE USER INPUT FOR NAME, BID
# userName = input("What is your Name ? : \n")
# userBid = int(input("What is your bid : $"))
# STEP 2 : SAVE THE USER DATA INTO A DICTIONARY {name: price}
# name as key , price as value
# bids ={}
# bids[userName] = userBid

# STEP 4 : COMPARE ALL THE BIDS, WHICH IS HIGHEST IN DICTIONARY
def find_highest_bidder(bidding_dictionary):
    highest_bid = 0
    for bidder in bidding_dictionary:
       bid_amount = bidding_dictionary[bidder] #gives the value of the each key , key is bidder
       if bid_amount > highest_bid:
          highest_bid = bid_amount
          winner = bidder  
    
    print(f"The winner is {winner} with bid Amount of ${highest_bid}")

# STEP 3 : whether if user wants to continue adding new bid ADD IT.

bids ={}
continue_bidding = True
while continue_bidding :
  userName = input("What is your Name ? : \n")
  userBid = int(input("What is your bid : $"))
  bids[userName] = userBid
  should_continue = input("Are there any more bidders? type 'Yes' or 'No'. \n").lower()
  if should_continue == 'no':
     continue_bidding = False
     find_highest_bidder(bids)
  elif should_continue == 'yes':
     # to clear the screen 
     print("\n" * 20) 


# Alternatively we can use max function of python which gives the highest value in dictionary
# Syntax is -- max(dictionary_name, key=dictionary_name.get) -- which gives name of the key which has highest value