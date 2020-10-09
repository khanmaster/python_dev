# # Boolean and None
#
# # What are Boolean values
# # Boolean in data types
# # None
#
# # We'll learn about the use of Boolean values (True and False)
# # Their usage within data types and values of None within Python
#
# a = True
# b = False
# print(a == b) # is a equals (==)b? no result False
# print(a != b) # is a not (!=) to b? True
# print(a >= b) # is a greater than b? no outcome True
# print(a >= True) # is a greater or equal to True? result True

# Moving onto Boolean within Data Types
# Python has several methods within strings
# Let's dive straight into it with our evergreen Hello world string

greeting = "Hello World!"

print(greeting.isalpha())
# isalpha() checks if all letters in our string are letters and return True or False
# Charactors that are not considered as letters i.e !#%&? etc.

print(greeting.islower())
# islower() checks if everything in our string in lower case

print(greeting.endswith("!"))
# endswith() checks if the string ends with specific character

print(greeting.startswith("H"))
# startswith() checks if the first letter starts with specific letter

# Let's see how can use Boolean with values and numbers
# IMPORTANT: It is vital to understand that within coding the value of 0 and other value
# i.e 1. -10 have a very specific meaning " a = 0 " value will always be false
# Any other value within the numeric area be it positive or negative will yield a True value

x = -2
y = 10
print(bool(x))
# Casting with bool() to get boolean outcome - False

print(bool(y))
# Casting with bool() to get boolean outcome - True

# The value of None?
# None is an object type like any other and is used as a place holder that could be replaced later
# it means exactly what it says in that the value is "None" which is also known as null in some other languages

# let'see the value of none
print(bool(None))

x = None
print(x == False)
print(x == True)

# How can we check if a variable is None?
# we can use identity operator "is None" rather than equality operator "=="
print(x is None) # result True
print(x == None) # result True
print(type(x))

# Summary

# You just learned about:
# Boolean values
# Boolean in data types
# None