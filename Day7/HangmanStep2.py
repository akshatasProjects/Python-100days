import random
# import hangman_words
from hangman_words import words_list
from hangman_art import hangman_stages , logo


# TODO-1
#  Create an empty string called placeholder.
# For each letter in chosen_word add a _ to placeholder
# So if the chosen_word was "apple" placeholder should be _ _ _ _ _
# ---------------------------------------------------------------


lives = 6
print(logo)
chosen_word = random.choice(words_list)
print(chosen_word)

# Create an empty string called placeholder.
placeholder = ""

# For each letter in chosen_word add a _ to placeholder
word_length = len(chosen_word)
for position in range(word_length):
  placeholder += "_"
print(placeholder)

gameOver = False
correct_guessed_letters = []

while not gameOver:
  guess = input("Guess a letter :").lower()

  # To check if user already guessed the letter
  if guess in correct_guessed_letters:
    print(f"You have already guessed {guess}")

  # TODO 2: create a "display" that puts the guess letter in the right positions and _
  display = " "

  for letter in chosen_word:
    if letter == guess:
      display += letter
      correct_guessed_letters.append(guess) #either letter or guess can be appended as both are same.
    # elif added to so that previous guessed letter added along with new correct letter, and also if letter is 
    # not equal to guess but that is inside the list correct_guesses_letters then it will be displayed with 
    # other remaining letters.
    elif letter in correct_guessed_letters:
      display += letter
    else:
      display += "_"
  print(display)

  if guess not in chosen_word:
      lives -= 1
      print(f"You guessed {guess}, that is not in the word. You lose a life")
      if lives == 0:
        gameOver = True    
        print(f"IT WAS {chosen_word} WORD YOU LOSE")


  if "_" not in display:
    gameOver = True
    print("You Win.")


# You can create a hangman art using ASCII art and add it to list called 'stages'

# Below code print the ASCII art from 'stages' that corresponds to the current number of 'lives' 
# the user has remaining 

print(hangman_stages[lives])