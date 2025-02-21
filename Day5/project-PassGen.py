#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


# password = ""
# # Here char holds the value of the range from 0 to user entered value that many time loop will run
# for char in range(0, nr_letters):
#   print(char)
#   password += random.choice(letters)

# for char in range(0, nr_symbols):
#   print(char)
#   password += random.choice(symbols)
  
# for char in range(0, nr_numbers):
#    print(char)
#    password += random.choice(numbers)

# print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []
# Here char holds the value of the range from 0 to user entered value that many time loop will run
for char in range(0, nr_letters):
  # print(char)
  # password_list += random.choice(letters)
  password_list.append(random.choice(letters))

for char in range(0, nr_symbols):
  # print(char)
  password_list += random.choice(symbols)
  password_list.append(random.choice(symbols))
  
for char in range(0, nr_numbers):
  #  print(char)
   password_list.append(random.choice(numbers))

print(password_list)
random.shuffle(password_list)
print(password_list)

# combining / joining the each character
password_combined = ""

for char in password_list:
  password_combined += char

print(f'Your password is {password_combined}')