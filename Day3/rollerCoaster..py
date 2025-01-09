print("Welcome to the Rollercoaster")
height = int(input("What is your height in CM ?"))
bill = 0
if height >= 120:
  print("You can ride rollercoaster")
  age = int(input("What is your age?"))

  if(age <= 12):
    print("Child tickets are $5.")
    bill = 5
  elif age <=18 :
    print("Youth tickets are $7.")
    bill = 7
  else:
    print("Adults tickets are $12.")
    bill = 12

    wants_photo = input("Do you want a photo? type Y or N")
    if(wants_photo == 'Y'):
      # add 3$ to bill
      bill += 3
      
  print(f"The total bill amount is {bill}")


else:
  print("Sorry you have to grow taller before you take a ride.")    