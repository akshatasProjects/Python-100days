student_score = [150,240,432,234,654,987,213,345,765,233,654]
# total_score=sum(student_score)
# max_num = max(student_score)
# print(total_score)
# print(max_num)

# replicating the sum and max numbers

max_score =0
for score in student_score:
  if score > max_score:
    max_score = score
    

print(max_score)

