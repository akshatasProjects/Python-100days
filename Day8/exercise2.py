def calculate_love_score(name1="Angela Yu", name2 = "Jack Bauer"):
    combined_name = (name1 + name2).lower()
    
    true_count = sum(combined_name.count(letter) for letter in "true")
    love_count = sum(combined_name.count(letter) for letter in "love")
    
    score = int(str(true_count) + str(love_count))
    print(f"Love Score = {score} ")
    


calculate_love_score()