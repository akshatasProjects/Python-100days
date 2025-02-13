capitals = {
  "France":"Paris",
  "Germany":"Berlin"
}

# Nested list in Dictionary

# travel_log = {
#   "France":["Paris","Lille", "Dijon"],
#   "Germany":["Stuttgart",'Berlin']
# }

# print Lille
# print(travel_log["France"])
# print(travel_log["France"][1])

# Nested List
nested_list = ["A","B",["C","D"]]
# print(nested_list[2][1])

# nested Dictionary
travel_log = {
  "France":{
      "cities_visites":["Paris","Lille", "Dijon"],
      "total_visits":12
  },
  "Germany":{
      "cities_visited":["Stuttgart",'Berlin'],
      "total_visits":5
  }
}

# Print Stuttgart from travel_log dictionary
print(travel_log["Germany"]["cities_visited"][0])