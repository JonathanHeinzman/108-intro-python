words = ["pencil", "tape", "paper", "pen", "computer", "table", "desk", "guitar"]

count = 0

for word in words:
    if len(word) >= 5:
        count +=1

print("Number of words with 5 or more letters:", count)