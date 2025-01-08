print("Welcome to Tip Calculator.💰")
bill = float(input("What is the total bill? 💲 "))
tip = int(input("What percentage tip would you like to give ? 10 12 15"))
people = int(input("How many people to split the bill?"))
bill_with_tip = tip/100 * bill + bill

bill_per_person = bill_with_tip / people
final_amount = round(bill_per_person, 2)

print(f"Each Person Should Pay {final_amount} 💲")