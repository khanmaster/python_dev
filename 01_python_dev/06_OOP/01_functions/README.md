# Function Introduction

## Timings

30 - 45 Minutes

## This lesson includes

* What is a function and why is it useful
* How to create a function
* Function structure and arguments
* Function good practices

We will be looking into the importance of functions and begin to learn about the core principles that will set you apart from others when architecting your code. 

## What is a Function and Why is it Useful?
You will have already seen that you have been repeating a lot of code up until this point such as multiple print statements, multiple adding to a list and the like. This is obviously inefficient and we need to understand one VERY important principle of coding which is:

![](../../assets/Dry.png)

Always keep this in mind when writing your code as it will leave you in good stead (we do love an idiom).

Functions are a tool, within python, that allows you to embed particular actions using code and make them reusable.

So, it's best we crack on with an example.

## Creating a function

Create a file called `general_functions.py` and we will step into a basic example.

Once we have our file set up let's begin creating our function:

```python
def print_something():
    print("something has been printed")
```

Let's break down what we have written:

* `def` -> def is a python keyword that tells the interpreter that we are creating a function and the the following section will be the name
* `print_something()` -> This is the name of the method and the empty parenthesis mean that it expected now argument (this will be explained very soon)
* `:` the colon states to the interpreter that the following that each indented line underneath, until a blank 'un-indented line' is found, is part of the function
* `print("something has been printed")` -> this is what we're asking our function to do

Let's run our program and what you should see is that nothing has happened. This is because you need to call the function for it to action what is within it:

```python
def print_something():
    print("something has been printed")


print_something()
```
We should now have the function printed our on our command line.

## Function structure and arguments

However, hopefully you would have seen a Huge! issue with the code? The function does one job and one job only, it prints the text `"something has been printed"` which if we're honest is pretty useless.

The aim of a function is to do a job based on being provided an argument. Let's improve our function by having it receive an argument to replace the 'hard coded' string.

```python
def print_something(print_string):
    print(print_string)
```
* `def print_something(print_string)` within the parenthesis we now have an argument called `print_string`.
* `print(print_string)` and our print function is receiving and using the argument.

Let's expand on arguments within functions as it will be a vital awareness moving forward!

So, to use our new function we need to give it an argument.

## Understanding Arguments

### Required arguments
```python
def print_something(print_string):
    print(print_string)
```

What we have in our argument is a `required argument` this means that you are unable to run the function without passing it an argument.

As we have mentioned python is a dynamically typed language and not a strongly typed language we can simply pass, what is essentially, a variable name.

Let's take a strong typed language example such as Java:

```java
public void print_string(String text)
```

As you can see above within the argument your are declaring that it is a string. Within Python you can pass anything to an argument and it's type is defined by the interpreter at runtime.

**Clear naming of your arguments IS vital!**

Let's now run our argument form our print statement:

```python
def print_something(print_string):
    print(print_string)


print_something("we can pass any string in here!")
``` 
If we run this it should print it to the command line.

Now, we could have just directly printed our string without that function, so let's add something new.

```python
def greeting(name):
    print("Hello, my name is " + name)

greeting("Susan")
```

### The Return Statement

Our previous function merely printed a string to the command line and in most development instances we will only be printing if we're debugging or providing user awareness to certain actions.

Within our `general_functions` file we're going to create a basic addition function that will add two numbers together:

```python
def addition(int1, int2):
    int1 + int2
```

In this instance we are now using 2 arguments to then add them together, nice and simple right? 

Run your programme as below as this time we need to print our function:

```python
def addition(int1, int2):
    int1 + int2

print(addition(2, 2))
```
I would hope you would see `None`? this is because we're not stating our program to actually `return` anything.

The action has taken place but the programme is not giving anything back at all therefore it is simply `None`.

We need to use the `return` statement which is key to python functions which means return the result of any function:

```python
def addition(int1, int2):
    return int1 + int2


print(addition(2, 2))
```
This time we should have a 4 printed to our command line, we can see that it is important to return an action within our functions.

### Default Arguments

So far we have asked for required variables but sometimes we may with to create a method that has a default or optional arguments:

```python
def addition(int1=2, int2=2):
    return int1 + int2


print(addition())
```

As you can see above we have simply added default values to the arguments, if you then pass arguments the default/optional inputs are overridden:
 
```python
def addition(int1=2, int2=2):
    return int1 + int2


print(addition(4, 4))
```
### Multiple Arguments

Last but not least we have multiple arguments. 

```python
def multi_args(*multiargs):
    
    print(type(multiargs))

    for arg in multiargs:
        print(arg)
```

* `*multiargs` -> the `*` next to a name means you can pass any number and types of variable to this list and it will generate a Tuple to be iterated over.

if we run the function as below:

`multi_args(1, 2, 2, 3, 3, 4, 5, 5)`

we should see:

```text
<class 'tuple'>
1
2
2
3
3
4
5
5
```

## Type Hints

As we mentioned earlier, Python is a dynamically typed language.  Type errors are only raised when the code runs, and variables can change types.  This allows much faster and more flexible writing of code, but also makes it more likely that our code will throw up errors.

There is a movement in the Python community at the moment towards introducing stricter typing.  It might be that Python becomes a static typed language one day, but in the meantime we can remove some of the ambiguity from dynamic typing using Type Hints.

Let's bring back our greeting example from earlier, and show what happens if we use this function with the wrong variable type.

```python
def greeting(name):
    print("Hello, my name is " + name)

greeting(24601)
```

We get the error: 
`TypeError: can only concatenate str (not "int") to str`

Our function was only designed to be used with strings, so calling it with an integer gave us a Type Error at runtime.

We can add type hinting through the use of annotations, introduced in Python 3.0 (though type hinting was introduced around the time of Python 3.5).  To do this, we add colon-space-type after our function arguments like so:

```python
def greeting(name: str):
    print("Hello, my name is " + name)

greeting(24601)
```

We can still run our code and get the same error, but notice that PyCharm has highlighted 24601 with a warning: `Expected type 'str', got 'int' instead`.

We can also add type hints for the output from a function using `-> type` between the closed bracket and the colon.

```python
def division(denom: int, num: int) -> float:
    return denom / num
```

And they can be combined with default values too. (Put spaces around your = sign when using type hinting, otherwise it becomes hard to read).  You can also use type hints for variables.

```python
def subtraction(int1: int = 5, int2 = 2) -> int:
    return int1 - int2

a: int = 10
b: int = 7

print(subtraction(10, 7))
```

Type hints are currently an optional extra, although there's chance that they'll gain popularity in coming years until they're expected or required.  The examples we show you will probably leave them out in favour of simplicity, but you are encouraged to make use of them to help document and maintain clean code.  The theory and practices behind types and typing go much much deeper.  If you want to look into typing further, as an example, the `typing` module will let you specify more complex type combinations, such as:

```python
from typing import Dict, List

names = List[str] = ["Tom", "Dick", "Harry"]
options = Dict[str, bool] = {"subtitles": True, "colourblind_mode": False}
```

## Function Good Practices

So we have a whistle stop tour of functions but there are some important practices to keep in mind when creating functions:

1. Name your methods clearly and using lower case with underscores i.e. `def capture_first_name_from_cmd_line()`
2. All arguments should be clear in their need and where possible include their expected type i.e. `add(int1, int2)`
3. remember the `return` statement or your function will return `None`
4. Keep your functions small where feasible to ease readability and to keep things as simple as possible
5. Use comments within your methods to help with instructions on their use 
6. Consider using Type Hints to avoid type errors when you run your code

#Lab

Create a file called Calculator and complete a viable basic calculator using functions.

## Summary

You just learned:
* What is a function and why is it useful
* How to create a function
* Function structure and arguments
* Type hints
* Function good practices