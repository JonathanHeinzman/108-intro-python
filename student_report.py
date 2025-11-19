# MINI Chalenge

report_card = {
    "name": "Jonny",
    "subject": "math",
    "grades": [90, 85, 88]
}


print(report_card["name"])
print(report_card["subject"])

# Calculate the average

average = sum(report_card["grades"]) / len(report_card["grades"]) 

print(average)

if average >= 90:
    print("Excellent!")

elif average >= 70:
    print("Good job!")

else:
    print("Needs Improvement!")

report_card.pop("subject")
print(report_card)

