# Working with files and handling errors/exceptions

## Timings

60 - 75 Mins

## This lesson includes

* working with files
* understand errors and exceptions
* handling errors and exceptions
* using `try` and `except` blocks
* opening files and accessing data using readlines
* using `with` as best practice
* using `finally` as a clean up function
* writing to files

The programs you create will, at some point, need to open, read and write to files which in turn will generate certain errors/exceptions whether files are found or have encountered issues. How you manage those errors/exceptions can be the difference to a customer staying with your product or helping a platform/operational engineer solve a critical issue.

We have discussed many aspects of coding, all of which are important, although this has a special place in managing expectations and the quality of products. 

In this lesson we will be looking into reading and writing to files and handling errors that may return.

There will be a lot to take in during this lesson so take it slowly and ensure students understand all the concepts.

## Working with files and errors

We will be bringing the use files in line with managing errors and exceptions as when using certain utilities within Python or creating user interfaces you may need to be planning your product in a 'defensive' manner.

Let's start by creating a file called `orders.py` and in here we'll be managing the list orders that will be sent out to a kitchen within a restaurant.

Let's start off by using the below code:

```python
file = open("order.txt")
```

* the `open` built in function relates to file opening as a stream of which we can do things with the file and we have passed in the name of the file we wish to access.

If we run this code we should see an error similar to below:

```text
Traceback (most recent call last):
  File <file path>, line 2, in <module>
    file = open("order.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'order.txt'
```

We were unable to locate the file in this instance and it has generated an error. It is worth noting that we have not specified a path only a file name and therefore it will be created in the location that the program is run.

Let's solve the issue by manually creating a text file with the aforementioned name and run the program again and this time we should see no error.

## Exceptions and errors

You would have seen many of these when first starting out with Python whether it be a syntax error or an exception and let's investigate both.

In this instance we will use an interactive python session.

Type Python into a command line / terminal and you should be met with  `>>>` this is the python interpreter and we can run arbitrary code and see the values.


#### Syntax Errors  

You would have mostly seen syntax errors when you first started out with python as you would be expected to make a few mistakes and although the IDE picks up a lot of the issues some fall through the net.

an example being missing a semi colon in a loop:

```python
>>> x = 10
>>> if x < 10
  File "<stdin>", line 1
    if x < 10
            ^
SyntaxError: invalid syntax
```
as you can see in the error above it provides the location of where the offence occurred using the `^` symbol. that's pretty much it for errors and to be honest they do the job they're meant to do which is highlight where you have gone wrong. Again as mentioned we use IDE's to reduce to potential of this happening.

#### Exceptions

Exceptions are more common place as you get further into python coding and general development. 

```python
>>> 1/0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```  
 
or trying to add a string to a float:
 
 ```python
>>> '4' + 1.5
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "float") to str
```

As you can see the two 'built-in exceptions' are `ZeroDivisionError` and `TypeError`.

Built in errors can be viewed [here](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)

## Try / Exception blocks

The error message we received was fine if it were a simple hack task but if we will be looking to introduce useful functions we need to be a little more intelligent with our coding.

Handling exceptions will be vital moving forward and providing useful information in your code to help others solve issues or understand the problem without having to gain access to and read the code.

let's head back to our `orders.py` file and also let's delete our `order.txt` file in preparation to receive an error.

Let's run our code again and ensure we get an error stating that our file does not exist.

Now let's step into creating our try block:

```python
try:
    file = open("order.txt")
except:
    print("There has been an error! Panic")
```

What we should now see is `There has been an error! Panic`

Let's step through the code:

*  `try:` this is the start of our try block and will set up the rest of the syntax. A try block will expect at least one exception to be handled as we have done. **NOTE FOR TRAINER** -> have the students comment out the `except:` block and print statement and the interpreter should complain.
* `except:` The except without anything else is the default statement or catch all, essentially the `else` of the statement.

As you can see this message is of no help at all!

But we can capture specific 'built-in' exceptions by adding it to the `except:` clause:

```python
try:
    file = open("order.txt")
except FileNotFoundError:
    print("File cannot be found")
# except:
#     print("There has been an error! Panic")
``` 

Now we have been more specific in our error message, but when we first found our error is already had a useful `FileNotFoundError` block of text.

```text
Traceback (most recent call last):
  File <file path>, line 2, in <module>
    file = open("order.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'order.txt'
```

Arguably, that was a very useful error and we would really like to continue to use it in addition to our own message, we can do this suing the below code:

```python
try:
    file = open("order.txt")
except FileNotFoundError as errmsg:
    print("File cannot be found")
    print(errmsg)
# except:
#     print("There has been an error! Panic")
```

We should now receive an error as below:

```text
File cannot be found
[Errno 2] No such file or directory: 'order.txt'
```
arguably a little less dramatic than a large red failure! however, you can use the `raise` keyword as below to bring back the exception captured and have it exit as an exception.

```python
try:
    file = open("order.txt")
except FileNotFoundError as errmsg:
    print("File cannot be found", errmsg)
    raise
# except:
#     print("There has been an error! Panic")
```

Should return:

```text
Traceback (most recent call last):
File cannot be found [Errno 2] No such file or directory: 'order.txt'
  File <file path>, line 3, in <module>
    file = open("order.txt")
FileNotFoundError: [Errno 2] No such file or directory: 'order.txt'
```

We will continue to use our new exception management skills throughout this section on files. 

## Handling files

###Reading files

We have already opened a file and we have begun to handle some of the errors that can come from it but there are many more options to be applied to the opening of a file. The key part is adding a mode to the file opening

`open(file, mode)`

| Mode	 |Description|
| :----: |:----                                                    |
|'r'	 |This is the default mode. It Opens file for reading.       |
|'w'	 |This Mode Opens file for writing.  If file does not exist, it creates a new file. If file exists it truncates the file.|
|'x'	 |Creates a new file. If file already exists, the operation fails.|
|'a'	 |Open file in append mode. If file does not exist, it creates a new file.|
|'t'	 |This is the default mode. It opens in text mode.|
|'b'	 |This opens in binary mode.
|'+'	 |This will open a file for reading and writing (updating)|


It is worth noting that the `+` operator can be used with 

Let's start tidying our code up into functions:

```python
def open_and_print_file(file):
    try:
        opened_file = open(file, "r")
        file_line_list = opened_file.readlines()

        for line in file_line_list:
            print(line.rstrip('\n'))
        
        opened_file.close()
        
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise
```

* `opened_file = open(file, "r")` here we are using the `open()` functions and passing the mode of the file as `r` for read. 
* `file_line_list = opened_file.readlines()` we are then using Readlines() which actually returns the line as a list. We are then iterating through this list and printing out each element of the list.
* `opened_file.close()` This is a very important line of code as if you are running this within a program and you do not close the file it could cause a lock in the file (you sometimes see this while attempting to delete a file while it's open)

running the above code will generate our error so let's create our `order.txt` and input the some details for the order:

```text
Cheese burger

Fries

Diet coke
```

in fact if you provide a print line as below to print the opened_file:

```python
def open_and_print_file(file):
    try:
        opened_file = open(file, "r")
        file_line_list = opened_file.readlines()

        print(file_line_list)

        for line in file_line_list:
            print(line.rstrip('\n'))
        
        opened_file.close()
        
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise
```

should return the list with the newline characters in a list:

```text
['Cheese burger\n', 'Fries\n', 'Diet coke']
Cheese burger

Fries

Diet coke
```

what you will find is that there are spaces within the output due to the `\n` character generated a new space. We can handle this by stripping the newline character feed from the string as below:

```python
def open_and_print_file(file):
    try:
        opened_file = open(file, "r")
        file_line_list = opened_file.readlines()

        # print(file_line_list)

        for line in file_line_list:
            print(line.rstrip('\n'))
        
        opened_file.close()
        
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise
```

* `print(line.rstrip('\n'))` here we are merely using the string function `rstrip` to remove the new character line feed from the string in printing.

what we should be left with:

```text
Cheese burger
Fries
Diet coke
```

However!!!! We can make it better!!!!

##The all important `with` statement and `finally:`

The `with` statement is a very handy built-in within python that handles the close statement within a block of code and it can also be used with a try or catch block. 

In short the `with` statement uses `__entry__` and `__exit__` functions. There is a layer of complexity within the statement but in this instance we need to know how to use them, know that they're best practice and that they take care of the `close()` statement automatically preventing any user mistakes from not closing at the right stage.

```python
def open_using_with_and_print(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise
    finally:
        print("\nExecution complete")
```
You can see our `try:` block remains the same as does our `except` although when opening the file we are now using the `with` statement.

* `with open(file, "r") as file:` This is the equivalent of our previous methods opening and managing of the file although here in one line we are opening the file in prep for access/work without having to bind to a variable. Python does this for us as part of a loop of sorts, in fact more of a try/except block.

Now we have a brief and simple introduction to the `finally:` function of the try catch block.

* `finally:` this is a block for cleanup i.e. once completed with the block be it pass or fail, in this instance we're merely asking it to print that execution is complete.


**NOTE FOR TRAINER** The `with` details can be found [here](https://docs.python.org/3/reference/compound_stmts.html) under compound statements.

## Writing to a file

Writing to a file will follow all of the same principles as we have already delivered in the above context of opening files.

Let's get straight into writing some code:

```python
def write_to_file(file, order_item):
    try:
        with open(file, "w") as file:
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise
```

* `with open(file, "w") as file:` The only major change from previous functions is that we're using the `w` mode for write, the rest of the with statement is the same as before.
* `file.write(order_item + '\n')` then we are calling the `file.write()` function as part of the file built-in functions to write to the file passed to it.

Our error statements remain the same.

Now let's try and write to our file and immediately use our `open_using_with_and_print()` function we created previously.

 ```python
write_to_file("order.txt", "Lasagna")
open_using_with_and_print("order.txt")
```

The output should be `Lasagna`... so, what happened to the rest of our order?:

 ```text
Cheese burger
Fries
Diet coke
```

this is where you need to be very careful with the options you use, if you look at the `w` mode the explanation of it's function is:

| Mode	 |Description|
| :----: |:----                                                    |
|'w'	 |This Mode Opens file for writing.  If file does not exist, it creates a new file. If file exists it truncates the file.|

We have now overwritten out order which is far from ideal. We need to use the `a` mode for `append` to allow us to add to the file without removing it's content.

Add the details back into our order file and remove the Lasagna text, and let's update our mode with `a` instead of `w`.

When we run the file again we should see that Lasagna has been appended to the file.  

### Creating a new file automatically if it doesn't exist

Once of the areas you need to be very careful about when working with certain modes is that if the file does not exist some modes will create a new file:

| Mode	 |Description|
| :----: |:----                                                    |
|'w'	 |This Mode Opens file for writing.  If file does not exist, it creates a new file. If file exists it truncates the file.|
|'a'	 |Open file in append mode. If file does not exist, it creates a new file.|

as you can see using either of the above options will create a new file if it does not exist so use caution when using these and plan your program sensibly using the `x` option as an example.

| Mode	 |Description|
| :----: |:----                                                    |
|'x'	 |Creates a new file. If file already exists, the operation fails.|


## Summary

You just:
* working with files
* understand errors and exceptions
* handling errors and exceptions
* using `try` and `except` blocks
* opening files and accessing data using readlines
* using `with` as best practice
* using `finally` as a clean up function
* writing to files  