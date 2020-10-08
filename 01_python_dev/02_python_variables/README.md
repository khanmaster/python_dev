# Python Variables

## Timings

20 - 30 Mins

## This lesson includes

* What is a variable?
* Dynamically typed languages
* Overwriting variables 
* Getting User input from the command line

In this lesson we will fully understand variables, why they're important and will form the core of everything you do within programming.

We will learn briefly about some data types but will go into more detail in later lessons.

## What are variables?

Put very simply a variable is somewhere to store and label data within a program and as per the word 'variable' some of them are flexible to change. 

Let's get straight to an example. Have the students create a new folder called  in their 'Hello world project called 'variables'. Then inside the variables folder create a python file called `variables_examples`.

### setting a variable

Once we have our `variable_examples.py` file open we're now going to set some variables. All variables follow a simple pattern of:

`{variable name} = {variable data}`

The single equals sign in pretty much all languages relates to variable assignment. `==` as an example means 'equal to' i.e. are these two things equal to each other and we will revisit this later in the course.

Let's begin as with some basic number variables:

```python
# Setting variables
name = "john" # string
age = 22 # Integer
hourly_wage = 15.5 # float
travel_allowance = 10
print(name)
print(age)
print(hourly_wage)
print(age>hourly_wage)
#
# a = 1
# b = 2
# c = 3.5 # float
# hi = "Hello World!"
#
# print(hi)
# print(type(hi))
#
# print("What is your name? ")
# name = input()
# print("hi ")
# print(name)
#
# # overwriting  a variable
# name = "khan"
# # print(name)
```

### The most important method you will ever use!

One of the numerous methods within the Python base library that is available to you one will always stand out the most for begginers and take note!

The method is `type()`. This method will print out the type of the object:

wrap is around your `hi` variable as below and run the program:

`print(type(hi))`

and you should see:

`<class 'str'>`

Now try it for your other variables.

**Note for the trainer** -> allow students to try out different variables and print out their types, push them to be creative with their variables.
## Getting User Input

Another useful tool will be gathering information from a command prompt and to do this we use a method called `input()`.

Ensure that all of your print statement are commented out and let's start by asking someone's name with print:

`print("Hi, what is your name?)`
 
 Then, let's use the `input()` method but remember we need to store the response.
 
 **Note** Ask the Students how we will store the response.
 
 We will use a variable called `name` that will receive the receive the response and then print two messages to say hello to the person using the name variable.
 
 Your final code should look like below:
 
```python

print("What is your name?")
name = input()
print("hi")
print(name)

```

## Lab - Get name, age and DOB details from a user 
 
Now have the Students expand on what they've done by creating user input for additional age and DOB fields. Ensure they know what types are being captured.

## Summary

You just:
* learned What is a variable is and how to use them?
* learned what dynamically typed languages are
* learned how to get user input from the command line and store it for use.  