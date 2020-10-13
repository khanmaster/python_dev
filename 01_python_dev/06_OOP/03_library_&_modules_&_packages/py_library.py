# Python Library, Modules and packages
# what is PIP
# https://docs.python.org/3/library/random.html

# Python has immense built in library like any other languages
# how can we use python's in built function

# Syntax : - import is the key word that we use to import the package followed by the name of the package

# # STEP 1
# import random
# # importing random module here will make all functions of random available for us to use
#
#print(random.random())
# run it few times and you'll get random outcome figure everytime

# STEP 2

from random import random
import math

print(random())

# let's see what other functionalities we utilise here

num_float = 23.66

# we have ceil() function in math library and it rounds the value at the top end of the float figure
print(math.ceil(num_float))

# similarly, floor() will round our figure to bottom end
print(math.floor(num_float))

# what is the value of PI?
print(math.pi)
# default value is 3.141592653589793

# Moving onto Modules
# Let's create os_module.py