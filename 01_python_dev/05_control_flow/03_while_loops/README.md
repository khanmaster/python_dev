# While

## Timings

10 - 15 Mins

## This lesson includes

* While loops
* While loop uses
* while and if / break
* Verifying user input using while loop

This is a very brief introduction to the while loop as they're relatively simple and there are only a few 'gotcha's' to be careful of.

## While loops

While loops will crop up every now and then, although they're common place in code they have limited and bespoke uses.

A while loop is essentially a monitor, rather than handling items within a collection you can set criteria for the loop:

```python
x = 0

while x < 10:
    print(f"it's working -> {x}")
    x += 1
```
* `x = 0` this is our count variable

* `while x < 10:` this is where our while statement begins and will continue to execute until the conditional of `x < 10` is no longer true

* `print(f"it's working -> {x}")` now we are simply using interpolation to print out x variable

* `x += 1` this is probably the most important part of our loop, our incrementer. Without this we would end up in an infinite loop as the statement will always be true.

running this code should produce:


```text
it's working -> 0
it's working -> 1
it's working -> 2
it's working -> 3
it's working -> 4
it's working -> 5
it's working -> 6
it's working -> 7
it's working -> 8
it's working -> 9
```

## While loop uses

We mentioned briefly the infinite loop and let's try this out... remove the incrementer or comment it out and run the code... what you should get is the continual print statement of `it's working -> 0` and you will need to stop the program as it will never end.

While loops can be useful when polling a particular process such as calling a particular service or API to see whether the call has been completed and then close the loop and move on and this is where using an if statement and then using the break keyword can be beneficial.

## While if and break

Let's head back to our code and change is slightly:

```python
x = 0

while x < 10:
    print(f"it's working -> {x}")
    if x == 4:
        break
    x += 1
```

This time we should only get the below output due to the fact we had reached break statement:

```text
it's working -> 0
it's working -> 1
it's working -> 2
it's working -> 3
it's working -> 4
```

## Verifying user input

We can use while loops to verify user input. What happens when we use user input and we get the wrong value or the wrong format?

```python
# Asking for someone's age
# This can either be an integer (20) or a string (twenty), and it can be written in many ways
age = input("What is your age? ")

print(f" Your age is {age}")
```
What do we do if we want to standardise what input we get from everyone who puts their age in? Let's say we want the age as an integer. We can use a while loop:

```python
user_prompt = True

while user_prompt:
    age = input("What is your age? ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please provide your answer in digits")

print(f"Your age is {age}")
```

What happens if we get the correct data type, but it is in the wrong range? The `isdigit()` method returns True if all the characters are digits, otherwise False. Therefore, `.isdigit()` is stopping people from inputting strings, floats, and negative numbers, but we are able to input digits as high as 1000000 or higher!

No one is that old. Let's fix it. The oldest person alive today is 117, this will be a safe maximum number!

```python
user_prompt = True
while user_prompt:
    age = input("What is your age? ")
    # Note that input is always str, we need to convert it before we can compare it
    if age.isdigit() and int(age) < 117:
        user_prompt = False
    else:
        print("Please provide your answer in digits, below 117")

print(f"Your age is {age}")
```

## Summary

You just:
* While loops
* While loop uses
* while and if / break
* Verifying user input with while loops
