import random

# generating random integer numbers
# randomInteger = random.randint(1,10)
# print(randomInteger)

# Generating random numbers between 1 to 10
# random1_to_10 = random.random()
# print(random1_to_10)

# Generating uniform generates the floating point numbers
# randomFloat = random.uniform(1,10)
# print(randomFloat)

# Program to generate Heads or Tails
random_heads_tails = random.randint(0,1)
if(random_heads_tails == 0):
  print("Heads")
else:
  print("Tails")