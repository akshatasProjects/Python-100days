student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for score in student_scores:
  num = student_scores[score]
  if num > 91 and num < 100:
    student_grades[score] = "Outstanding"
  elif num > 81 and num < 90:
     student_grades[score] = "Exceeds Expectations"
  elif num > 71 and num < 80:
     student_grades[score] = "Acceptable"
  else:
     student_grades[score] = "Fail"
  
print(student_grades)