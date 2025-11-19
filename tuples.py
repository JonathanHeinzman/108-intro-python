# Tuples are just lik lists - they can store multiple items
# BUT!!! Tuples are IMUTABLE (you can't change them after creation)

my_tuple = ("apple", "banana", "cherry") 
print(my_tuple)

# accessing items
print(my_tuple[0])
print(my_tuple[2])

# check if an item exists
if "cherry" in my_tuple:
    print("Yes it is")

# length of tuple
print(len(my_tuple))

# single item tuple
# You must add a comma at the end to recognize it as a tuple
single = ("apple")
print(type(single)) # this is just a string
correct = ("apple",) # this is a tuple
print(type(correct))

# Nesterd tuple
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
combine = (tuple1,tuple2)
print(combine)

