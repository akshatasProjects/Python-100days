# FizzBuzz
# You are going to write a program that automatically 
# prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:

#1 Your program should print each number from 1 to 100 in turn and include number 100.
for num in range(1, 101):
  print(num)

  if(num % 3 == 0):
    print("Fizz")
  
  if(num % 5 == 0):
    print("Buzz")

  if(num % 3==0 and num %5 == 0):
    print("FizzBuzz")
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".

# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`

# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

