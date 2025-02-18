def add(n1, n2):
  return n1 + n2

def substract(n1, n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def division(n1,n2):
  return n1/n2


math_dictionory = {
  "+":add,
  "-":substract,
  "*":multiply,
  "/":division,
}

def calculator():
  result_accumulate = True
  num1 = float(input("Enter a number for n1 :"))


  while result_accumulate:
    # Program asks the user to type the first number
    num2 = float(input("Enter a number for n2 : "))

    # to get each symbol from dictionary
    for symbol in math_dictionory:
      print(symbol)

    operation_symbol = input("Pick an operation")

    # getting the operation from dictionary
    result = math_dictionory[operation_symbol](num1, num2)
    print(f"{num1} {operation_symbol} {num2}={result}")

    choice =  input(f"Type 'y' to continue with {result} or type 'n' to start a new claculation").lower
    if choice == 'y':
      num1 = result
    else:
      result_accumulate = False
      print("\n"*20)
      calculator()


calculator()




