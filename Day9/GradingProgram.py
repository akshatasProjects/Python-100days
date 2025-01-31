
# Grading Program
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores. 
# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values. 
# The final version of the student_grades dictionary will be checked. 

# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary. 

# This is the scoring criteria: 
# - Scores 91 - 100: Grade = "Outstanding" 
# - Scores 81 - 90: Grade = "Exceeds Expectations" 
# - Scores 71 - 80: Grade = "Acceptable" 
# - Scores 70 or lower: Grade = "Fail" 

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}

# for thing in ditionary: 
# print(thing) -- gives only key value
# print(ditionary[key]) -- will show the value

for item in student_scores:
  key = (item)
  value = (student_scores[item])
  print(key, value)

  if(value > 91 and value < 100):
    student_grades = value
    print(f"{value} Outstanding")
  elif(value > 81 and value < 90):
   print(f"{value} Exceeds Expectations")
  elif(value >71 and value < 80):
   print(f"{value} Acceptable")
  else:
    print("Fail")


print(student_grades)
