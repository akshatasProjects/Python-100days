import random
word_list = ['aardvark','baboon','camel']

#TODO 1: - Randomly choose a word from the word_list and assign it to the variable called "chosen_word". print it
chosen_word = random.choice(word_list)
print(chosen_word)
print("------------------")

#TODO 2: - Ask the user to guess the letter and assign their answer to a variable called guess.Make guess lowercase
guess = input("Guess the letter :").lower()
print(guess)
print("------------------")

#TODO 3: - Check if the letter user guessed(guess) is one of the letter in the chosen_word. Print "Right" if it is else Print "Wrong" 

for letter in chosen_word:
  if letter == guess:
    print("Right")
  else:
    print("Wrong")
  