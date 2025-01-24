# Create a function called life_in_weeks() using maths and f-Strings that 
# tells us how many weeks we have left, if we live until 90 years old.

# It will take your current age as the input and output a message with our time left in this format:
# You have x weeks left.

def life_in_weeks(age):
    weeksLeft = 90 - age 
    print(f'You have {weeksLeft} weeks left.\n')
    
life_in_weeks(12)