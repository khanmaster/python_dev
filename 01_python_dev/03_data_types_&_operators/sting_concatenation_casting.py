# creating string and deference between single and double quotes
single_quotes = 'single quotes\'wow\''
double_quotes = "double quotes"

print(single_quotes)
print(double_quotes)

# slicing strings
# Everything starts from 0 index in python

slice_hello_world = "Hello world!"
                  #  01234567891011
# let's slice Hello only
print(slice_hello_world[-5])
# let's see how can we find out the length
# to do that we will use a method called len()
print(len(slice_hello_world))
# outputs 12 the total number of characters

# Lets move onto what else can we do with strings
# how can we get rid of white/unwanted spaces from our string

# Python has a method called strip which removes all white spaces at the end of a string
White_space = "lot's of space at the end                 "
# let's check the length of the string first
print(len(White_space))
print("total characters including white space")
# outcome 42
print("characters without white spaces")
print(len(White_space.strip()))

# Few more useful method
# count() method counts a substring within a string
example_text = "here's SOME text with lot's of text"
print(example_text.count("text"))
# give an int as an outcome - how many times "text" was written in the string

# lower() method is used to bring everything to lower case
print(example_text + "- actual string")
print(example_text.lower() + " - changed with lower() method")

# upper() method brings everything to upper case
print(example_text.upper() + " - changed to upper case with upper() method")

# capitalize() method capitalises the first letter in the sentence
print(example_text.capitalize() + " - h of here's is changed to Here's with capitalize() method")

# replace() method is used to replace text in the string
print(example_text.replace("with", ",") + "- with has been replaced with , ")

# Moving on to Concatenation and Casting

