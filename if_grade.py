score_user = input("Enter a number from 1-100:")
score= int(score_user)

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")

passed = True 
if score >= 70:
    print("Congratulations!")
else:
    print("Try Again!!!")
