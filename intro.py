print("Hello world from python!")
print(2)
print(2+3)
print(True) # doesnt work

# This is a comment

"""
This is a multi line comment
"""

# Create a variable
name = "Jonathan"
age = 27
middle_name = "David"
last_name = "Heinzman"
found = False
print(name)

# concatination (putting things together)
print("My name is: " + name + ", and i am " + str(age) + " years old." + middle_name)
print("Did he show up to class?" + str(found))


# f format
# f"" f"""
print(f"My name is: {name}, and i am {age} years old.")
print(f""" 
Jonathan
      middle{middle_name} 
            Heinzman
""")

# type() function helps us to know what type of data a variable is
print(type(name))
print(type(age))
print(type(found))

# casting
# helps us convert to different data types
print(20+int("20"))
print(10+age)

# input method
# is going to allow us to interact with the terminal and pass some variable
#print(input("Enter your name here: "))
#print(type(input("Enter your name here: ")))

new_age = (input("Enter your age here: "))
#print(new_age + age)
print(str(age) + new_age)

x = int(input("enter first value: "))
y = int(input("enter first value: "))
print(x+y)