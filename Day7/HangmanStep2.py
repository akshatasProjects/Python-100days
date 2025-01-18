import random

# TODO-1
#  Create an empty string called placeholder.
# For each letter in chosen_word add a _ to placeholder
# So if the chosen_word was "apple" placeholder should be _ _ _ _ _
# ---------------------------------------------------------------

wordList = ['Apple', 'Orange', 'Sunset','Banana','Tree', 'Sea']
chosen_word = random.choice(wordList)
print(chosen_word)

# Create an empty string called placeholder.
placeholder = ""

# For each letter in chosen_word add a _ to placeholder
word_length = len(chosen_word)
for position in range(word_length):
  placeholder += "_"
print(placeholder)

