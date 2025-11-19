# MINI Chalenge

report_card = {
    "name": "Jonny",
    "subject": "math",
    "grades": [90, 85, 88]
}


print(report_card["name"])
print(report_card["subject"])

report_card
# Calculate the average

report_card["average"] = "grades"

if "grades" >= "90":
    print("Excellent!")

elif "grades" >= "70-89":
    print("Good job!")

else:
    print("Needs Improvement!")

report_card.pop("subject")
print(report_card)

