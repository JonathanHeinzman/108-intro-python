# operators are like "symbols" or "shortcuts"
# that tell the computer to do something with values

# 1. Arithmetic operator- used with numeric values (calculator)
x = 1
y = 2
res = 0

res = x + y
print(res)

res = x * y
print(res)

res = x + y
print(res)

res = x / y
print(res)

res = x % y # Modulus-> remainder after division
print(res)

res = x ** y # Exponentation-> x to the power of y
print(res)

res = x // y # Floor division-> divide and drop the decimal
print(res)


print("______________________________________")
# 2. Assignment operators - used to assign values to variables
# = means "put this balue inside the (variable)"

x = 5
x += 5
x -= 3
x *= 3
x /= 3
print(x)


print("______________________________________")
# 3. Comparison operator
# used to compare two values
# same as if else

z = 5 
p = 5
print(z == p) # equal to
print(z != p) # not equal to
print(z <= p) # less than / greater than
print(z >= p)


print("______________________________________")
# 4. Logical operators
# used to combine conditional statements

x = 3
y = 10
z = 3

print(x == y and y ==z) # False, both conditions are NOT true
# both conditions need to be true to execute "true"
print(x == y or y ==z) # True, at least 1 condition is true
print(not x == y) # True, because x == y is false,


print("______________________________________")
# 5. Identity operator
# used to compare the objects, not if they are equal
# are actually the same object with the same memory location

x = 3
y = 3

print(x is y) # Returns True if both variables are the same object
print(x is not y) # Returns True if bothe variables are NOT the same object


print("______________________________________")
# 6. Membership operator
# used to test if a sequence is presented in an oblect

x = [1, 2, 3, 4, 5] # this is a list

print(4 in x) # True, 4 is inside the lis
print(9 not in x) # True. 9 is not in the list