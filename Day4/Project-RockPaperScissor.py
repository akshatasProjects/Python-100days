import random

game_images = ['rock','paper','scissor']

user_choice = int(input("What do you choose? Type 0: for ROCK, 1: for PAPER, 2:for Scissors."))

if user_choice >= 0 and user_choice <= 2:
  print(game_images[user_choice])

computer_choice = random.randint(0,2)
print(f"Computer chose {computer_choice}")

if(user_choice == 0 and computer_choice == 2):
  print("You Won!")
elif computer_choice == 0 and user_choice == 2:
  print("You lose!")
elif computer_choice > user_choice:
  print("You lost!")
elif computer_choice == user_choice:
  print("Its a Draw")  
elif user_choice >= 3 or user_choice < 0:
  print("you typed an invalid number")