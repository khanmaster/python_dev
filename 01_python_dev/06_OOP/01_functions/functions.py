# # What is a function and why is it useful
# # KEY PRINCIPLE OF CODING IS "DRY" DON'T REPEAT YOURSELF
# # coding best practice and naming conventions
# # Syntax: def name_of_function():
# # "def" is a key word used in python that tells the interpretor that we are creatin a function
#
# # Functions: are tools in python, that allows you to embed particular actions using code and make them reusable
# # How?
#
# Step 1
def greet_user():
    print("Wellcome")
# execute without calling the function

# Let's run our program
greet_user()

# Step 2
def greet_user(name):
    print("Wellcome Dear " + name)
# execute without calling the function

# Let's run our program
greet_user("shahrukh")

Step 3
create a funtion for addition

def add(num1, num2):
    print(num1 + num2)
add(3, 56)

# step 4 create a subtraction function to return value
def subtract(num1, num2):
    return (num1 - num2)
#subtract(4, 3)

# return statements returns the values to store in a variable
subtracted_value = subtract(33, 23)
print(subtracted_value)

# Function Good Practices
# So we have a whistle stop tour of functions but there are some important practices to keep in mind when creating functions:
# Name your methods clearly and using lower case with underscores i.e. def capture_first_name_from_cmd_line()
# All arguments should be clear in their need and where possible include their expected type i.e. add(int1, int2)
# remember the return statement or your function will return None
# Keep your functions small where feasible to ease readability and to keep things as simple as possible
# Use comments within your methods to help with instructions on their use
# Consider using Type Hints to avoid type errors when you run your code