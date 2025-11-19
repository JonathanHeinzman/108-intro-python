# Dictionaries store data in KEY:VALUE pairs {}

students = {
    "name": "Jonathan",
    "age": 27,
    "major": "computer science"
}

print(students)

# Accessing items
print(students["name"])      # access by key
print(students.get("major")) # access another way (.get)

# Add new item
students["graduation_year"] = 2025
print(students)

# Changing values
students["age"] = 23
print(students)

# Remove item
students.pop("major")
print(students)

# Check if KEY exists
if "name" in students:
    print("Key 'name' is in the dictionary")

# Nested dictionary
students = {
    "student1": {"name": "Jonathan", "age:": 27},
    "student2": {"name": "Alex", "age:": 30},
}

print(students["student1"]["name"]) # Access nested value

