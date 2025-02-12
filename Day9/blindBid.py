name = input("Enter your Name :\n")
bidPrice = int(input("Enter your bid Value : $"))

# Saving / Adding bid and name to dictionary
bids={}
bids[name] = bidPrice

# Whether if new bids need to be added
should_continue = input("Are there are any other bidders? Type 'Yes' or 'No'. \n ")

# Compare bids in dictionary
