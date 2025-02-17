def leapYear(year):
  if year % 4==0 and year%400==0:
    return "Its Leap"
  else:
    return "Its Not"

print(leapYear(2000))