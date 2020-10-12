# understanding Name and Main in Python

## Timings

30 - 45 Mins

## This lesson includes

* Understanding `__name__` & `__main__` 
* Understanding `__name__` and `__main__` when importing
Why are `__name__` & `__main__` useful?


`__name__` & `__main__` are are part of Python execution/interpreter engine and sets these variables before running any other code within a file/function/method. Alongside a class `__init__` function it is very important to understand these key functions.

## Understanding `__name__` & `__main__` 

we're going to dive straight in as it's the easiest way to understand what is going on. Create two files one called `mod_1` and the other `mod_2`.

within `mod_1` we will right the below code and run:

```python
print(__name__)
```
the output should be `__main__`.

### Python interpreter / run

When python runs a file it sets some variables in teh background one of which is `__name__` variable and in this instance it is set to `__main__`.

Now to be 100% clear on what this means is that when we run `mod_1` the name variable is set to `__main__` because we're running the `mod_1` file. Therefore when running the `mod_1` file itself the `__name__` variable is being set to main.

Just to make this even clearer let's add a little more to our `mod_1`:

```python
print("This is mod_1's name -> " + __name__)
```

Which should return `This is mod_1's name -> __main__`

## Understanding `__name__` and `__main__` when importing

This is where the importance of the `__name__` comes into play. Head to our `mod_2` and apply the below code:

```python
import mod_1
``` 

Then run `mod_2` and what you should see is `This is mod_1's name -> mod_1` 

Now this is a pivotal moment of understanding, when a module is imported the code within that module is run and it is running the print statement within the file but the key difference here is that it no longer returns `__main__`!

This is because we are not running the `mod_1` file but it is the import statement running `mod_1` details and therefore is naming the fact that the name of this is `mod_1` and not `__main__`.... ok this can be a llttle confusing so let's add a little more code to our `mod_2`:

```python
import mod_1

print("This is mod_2's name -> " + __name__)
```
now run our `mod_2` file and the output should be:

```text
This is mod_1's name -> mod_1
This is mod_2's name -> __main__
``` 

Now we are accessing the `__name__` function from `mod_1` with the import statement in `mod_2` and we are also calling the `mod_2` print name statement which is of course outputting `__main__`.

## Why are `__name__` & `__main__` useful?

ok, let's dig into the core of why these actions within Python are useful.

Back in our `mod_1` file add the below code:

```python
print("This is mod_1's name -> " + __name__)


def main():
    pass


if __name__ == '__main__':
    main()
```

Let's step through what we are doing here:

* `def main()` This speaks for itself as we are setting up a function called `main`
* `pass` pass is a python statement which essentially means 'null' and is ignored by python, this can be very useful when building a skeleton group of functions before implementing
* `if __name__ == '__main__':` what we are saying here is key! we are telling python that if we run this file directly i.e. the `__name__` is `__main__` which means running this file directly. Action whatever code is in the if statement body. which in this case is the `main()` method that does nothing.

I can't highlight this enough and I repeat!!!!

This is extremely useful as we can understand by using the `__name__` variable whether this file being run directly by python or is it being imported.

So, if we run our `mod_1` file we should still get our print statement of `This is mod_1's name -> __main__`, now move the print statement into the `main()` method we created and run it again and we should see the same...

```python
def main():
    # pass
    print("This is mod_1's name -> " + __name__)


if __name__ == '__main__':
    main()
```
if we run the `mod_1` file we still get the statement as we run it directly. However, run the `mod_2` file and we should no longer see the `mod_1` print statement:

 `This is mod_2's name -> __main__`
 
 The reason this has changed is because it has been imported and the file `__name__` is now `mod_1` our code from `mod_1` is not executed.
 
 ### So, why is it useful???
 
 There will be times when you only want to run code if running the file directly and not have things run when imported by another file. We will see as we move through some of our lessons how this can be useful.  

## Summary

You just:
* Learned something
* Learned something else