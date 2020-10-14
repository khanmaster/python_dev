# Lambdas

## Timings

15 - 25 Mins

## This lesson includes

* What are Lambdas
* Where can they be useful

A Lambda (or simply another word for function) can be extremely powerful and useful but it is important to understand how they hang together and exactly how they fit in.

## Lambda

Lambda's are essentially `anonymous` functions that can talk multiple parameters but return only one expression. It's easier to see their value than simply explain it. Create a file `larking_with_lambda` and let's get into some examples:

```python
def add(num1, num2):
    return num1 + num2


addition = lambda num1, num2: num1 + num2


print(add(2, 2))
print(addition(2, 2))
```
We can see above that we have a function of add which is pretty self explanatory and below we have the lambda expression doing the exact same thing. 

Lambda's work on the bases of `lambda arguments : expression` and in this case we're doing nothing more than name a variable to include a Lambda and although this works, and looks kinda pretty in one line, it's not a clean nor understandable way of writing code.

## Where Lambda's can be useful

A better way of using a lambda are within transformational blocks such as using the function `map`:

```python
savings = [234.00, 555.00, 674.00, 78.00]

bonus = list(map(lambda x: x * 1.1, savings))

print(bonus)

```
As always let's step through the code:

* `savings = [234.00, 555.00, 674.00, 78.00]` here we have a simple list of savings
* `bonus = list(map(lambda x: x * 1.1, savings))` Let's say we want to add a 10% bonus to the savings of our customers.
    * We have our bonus variable to contain are mapping exercise
    * first of all we use the `list()` function to turn (cast) our `map()` or transformation functions to a list
    * then we use our `map()` function passing it the lamda that receives `x` and then adds the percentage bonus to our customers savings
    * lastly we pass our map function the list of savings to work through

if we then print out the `bonus` we should have a list of updated values.

This is were a lambda can be used to it's best potential as an anonymous function. If we were to write this out without the `map()` or lamba function it would look like below:

```python
savings = [234.00, 555.00, 674.00, 78.00]
bonus =[]

for account_balance in savings:
    bonus.append(account_balance * 1.1)
``` 
We achieve the same goal but using a lambda is much more efficient.

## Summary

You just:
* What are Lambdas
* Where can they be useful