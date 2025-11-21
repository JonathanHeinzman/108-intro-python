# WHILE LOOPS
# A While loops repeats a block of code as long as a condition is True
# Be careful - if the condition never becomes False, you'll get an Infinite loop (CTRL + "C" stops an infinite loop)

count = 1

while count <= 5:
    print("Count is: ", count)
    count += 1 # Assignment operator which adds one until it equals to 5

print("-----------------------------------------------")

# using break to stop the loop

count = 1

while count <= 10: # loops when count is 10
    if count == 5: # checks when count is 5
        print("Break at 5!")
        break      # exits loop early
    print(count)
    count += 1

print("-----------------------------------------------")

# using CONTINUE to skip an iteration

count = 0 # initializes the count as 0

while count < 5:
    count += 1
    if count == 3:
        continue # skips 3
    print(count)


print("-----------------------------------------------")

# Else with while
# The else block runs when the loop condition becomes False (not by break)

count = 1
while count < 3:
    print(count)
    count += 1
else:
    print("Loop is finished!")

print("-----------------------------------------------")

# FOR LOOPS
# A for loop is used for looping over a sequence:
# a list, tuple, dictionary, string, etc.

# Loop through a list

fruits = ["apple", "banana", "cherry"]
for fruit in fruits: # for each fruit in the list fruits (returns each fruit on a seperate line)
    print(fruit)


print("-----------------------------------------------")

# Loop through a string

for letter in "Hello":
    print(letter) # returns each letter on a seperate line


print("-----------------------------------------------")

# Using range()
# range() generates a sequence of numbers

for x in range(5):
    print(x)


print("-----------------------------------------------")

# Start and end range

for x in range(2, 6):
    print(x)

print("-----------------------------------------------")

# step (skips numbers)

for x in range(0, 10, 2):
    print(x)

print("-----------------------------------------------")

# Else in for loop

for x in range(3):
    print(x)
else: # runs when loop is done
    print("Loop is done")

print("-----------------------------------------------")

# Break and Contine in for loops
for x in range(10):
    if x == 5:
        continue
    if x == 8:
        break
    print(x)

