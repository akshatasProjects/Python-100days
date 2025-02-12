programming_dictionary = {
  "Bug":"Error in program",
  "Function":"A piece of Code",
  "Loop":"The action of doing   something over and over again"
}

print(programming_dictionary["Bug"])

# creating empty dictionary
newDictionary = {}

# Adding new key value to dictionary
programming_dictionary["variable"] ="Container that contains the data"
print(programming_dictionary)

# Edit the item in dictionary
programming_dictionary["Bug"] ="A moth in your computer"
print(programming_dictionary)

# Looping through dictionary (prints the key not value)
for key in programming_dictionary:
  print(key)

# Looping through dictionary (prints the key and value)
for key in programming_dictionary:
  print(programming_dictionary[key])

