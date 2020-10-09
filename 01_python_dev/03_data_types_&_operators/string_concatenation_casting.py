# # creating string and deference between single and double quotes
# single_quotes = 'single quotes\'wow\''
# double_quotes = "double quotes"
#
# print(single_quotes)
# print(double_quotes)
#
# # slicing strings
# # Everything starts from 0 index in python
#
# slice_hello_world = "Hello world!"
#                   #  01234567891011
# # let's slice Hello only
# print(slice_hello_world[-5])
# # let's see how can we find out the length
# # to do that we will use a method called len()
# print(len(slice_hello_world))
# # outputs 12 the total number of characters
#
# # Lets move onto what else can we do with strings
# # how can we get rid of white/unwanted spaces from our string
#
# # Python has a method called strip which removes all white spaces at the end of a string
# White_space = "lot's of space at the end                 "
# # let's check the length of the string first
# print(len(White_space))
# print("total characters including white space")
# # outcome 42
# print("characters without white spaces")
# print(len(White_space.strip()))
#
# # Few more useful method
# # count() method counts a substring within a string
# example_text = "here's SOME text with lot's of text"
# print(example_text.count("text"))
# # give an int as an outcome - how many times "text" was written in the string
#
# # lower() method is used to bring everything to lower case
# print(example_text + "- actual string")
# print(example_text.lower() + " - changed with lower() method")
#
# # upper() method brings everything to upper case
# print(example_text.upper() + " - changed to upper case with upper() method")
#
# # capitalize() method capitalises the first letter in the sentence
# print(example_text.capitalize() + " - h of here's is changed to Here's with capitalize() method")
#
# # replace() method is used to replace text in the string
# print(example_text.replace("with", ",") + "- with has been replaced with , ")

# Moving on to Concatenation and Casting
# Concatenation is useful when we need to join 2 different strings/numeric types

first_name = "jame "
middle_name = " bond "
last_name = " 007 "

print(first_name + middle_name + last_name)
# how about adding different numeric types
age = 22
temperature = 36.8
#print("your age is " + age)
# we'll see a TypeError
# so how can we resolve it.. now the Casting comes into play
# To cast numeric into string we have a method called str()

print("your numeric age number is casted into string to concatenate " + str(age))
print(" your temperature today is " + str(temperature))

# How can we cast an string to numeric
int_string = "4"

print(int(int_string))

# Let's verify it with our type()
print(type(int(int_string)))

# Casting into float
print(float(int_string))
# result will be 4.0

# Let's verify with type()
print(type(float(int_string)))

# F-Srtings an Amazing python magical formating
# Formating strings were introduced in python 3.6 and make formatting a lot easier withou the need for casting
# It allows us to easily combine variables of different types within a single string by putting an f before first " mark
# Each variable is then enclosed in {curly brackets}

# Let's see it in action
city = "London"
city_age = 52
city_area = 60.2

print(f"{city} is {city_age} years old and the total area is {city_area}")

# We can also perform expression evaluation with f-strings
print(f"{city.upper()} IS {city_age * 7} YEARS OLD IN DOG YEARS!")

 # Finally, we can use f-string to specity the precision (number to decimal place)
 # we want for out floats, or fomart them as percentage
 # For Example

pi = 3.14159265359
print(f"Pi to 3 decimal places: {pi:.3f}")


score = 16
max_score = 26
print(f"You scored {score/max_score:%}")

# Lab
# Using what we have learned so far let's head back to our user_details_capture file
# Ensure we are using / casting the same type.
# Extend the capture further to grab details such as address
# (ensuring that a house number is correctly represented, hobbies,
# respond to the user the details they have provided.

# Ensure you use concatenation and casting!