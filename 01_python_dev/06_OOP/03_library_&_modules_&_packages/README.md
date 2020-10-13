# Python Library, Modules and Packages walk through

https://docs.python.org/3/library/random.html

## Timings

45 - 60 Mins

## This lesson includes

* The python built in library 
* What are modules?
* in built functions
* Packages
* What is pip?

Throughout this lesson we will be looking into Python's extensive libraries and how Python's external packages are managed by pip. We will also look into what makes a package and its structure in Python.


## The python in built library

Like all major languages they come with a host of useful integrated functions to make your life accelerate development and make standard repeatable practices simpler.


Create a python file called `py_lib.py` and let's take a look at some of the libraries available:

```python
import random

print(random.random())
```
as usual let's walk through what we have done:

* `import random` - we have already used the import statement to access some of our own modules when working with OOP but it also gives us access to many of the in built libraries available to us. In this instance we're important random  

* `print(random.random())` - We can then use the random package and by calling random we should get a random float between 0-1

We can simplify this even further by using the From and import statements together to remove the need to call the base random object:

```python
from random import random

print(random())
```
The above should produce the same result but keeps our code clean and readable.

Let's add another package:

```python
from random import random
import math

print(random())

num_float = 23.66

print(math.ceil(num_float))
print(math.floor(num_float))
print(math.pi)
```

step through the above code line by line as it is self explanatory here.

For a break have the students review the link below to the core library and practice using some of the internal library!

you can find the documentation for Python's core library [here](https://docs.python.org/3/library/) and there are many assisting functions available.


## Modules

We've already created loads when we have been created our classes!

A module is a piece of software that delivers a piece of functionality. We have imported modules when walking through our OOP four pillars so a module relates to python code whether that be functions or classes/methods.

Although we have discussed classes and objects at length that doesn't mean that a module has to be a class. If the use calls for it building functions can be just as useful, we will be using the `os` library import for python which relates to accessing data in the underlying OS.

Let's create a file called `os_module.py`:

```python
import os
 
working_directory = os.getcwd()
 
 
def return_user_id():
     print(os.getuid())
 
def operating_system_information():
    print(os.uname())

```  

So, we have created a simple variable that:

* `working_directory = os.getcwd()` returns our current working directory
* `def return_user_id():` created a method that returns our current system user IS
* `def operating_system_information():` returns details regarding the current operating system


Now let's create a another file called `use_os_module.py`:

```python
from os_module import *

return_user_id()

operating_system_information()


print(working_directory)
```

Step through the code with the students to show the outputs of the above code based on the module we have created.

It is very important when considering building your programmes what constitutes the need for a class and what could be handled by functions, this will be the ongoing conundrum and each team will come to the best way to work with things for themselves. Simply consider all of the important areas from the four pillars of dev. 

## Python's built in functions

Python has many built in functions that are part of the python standard library of which we have used a few such as:

* `type()`
* `len()`

allow the students more time to review the below link and see what in built functions are available, ensure they add links like below to their browser bookmarks to ensure they build their own reference guide for their new roles!

More in built functions and their uses can be found [here](https://docs.python.org/3/library/functions.html) in the online python docs.

## What is pip?

pip is python's package manager to install and manage packages that are not part of the base Python library. There are an incredible of amount of packages out there ranging from playing audio files to machine learning algorithms!

when you install python, pip should be installed with it and we can check this by typing `pip -V` into the command line, you should see something like below:

`pip 18.1 from /usr/local/lib/python3.7/site-packages/pip (python 3.7)`

type in in `pip -V` will list all of the packages available to you.


Let's install what will be a very valuable package in the future called `Requests`.

`pip install requests`

Let's create a file called `requests_example.py`:

```python
import requests

request_bbc = requests.get("https://www.bbc.co.uk/")

print(request_bbc.status_code)

print(request_bbc.content)
```

We should be used to the import statement now and we are then creating the get request and printing the response code and content of the message.

The call we have made above is the equivalent typing `bbc.co.uk` into the browser.


## Packages

Packages are a way of structuring your Python programs in a form to be reused and included in other programmes.

We will be using some interesting Python functionality with the `__init__.py` file (note not the initialisation of a class...) and the dot notation of using your modules within your package as well as including a file called `setup.py` file to configure your package.

The official documentation on python packaging can be found [here](https://python-packaging.readthedocs.io/en/latest/minimal.html) and should be shared and stored, although can be found easily within a google search.

Build the below structure with the students or a new project with all the files being empty for the time being:

```text
python_package (Root folder)
-- app (folder)
----__init__.py
----fizzbuzz.py
program.py
setup.py
``` 

### The __init__.py file

The __init__.py files are required to make Python treat the directories as containing packages; this is done to prevent directories with a common name, such as string, from unintentionally hiding valid modules that occur later (deeper) on the module search path. In the simplest case, `__init__.py` can just be an empty file, but it can also execute initialization code for the package.

### setup.py

The `setup.py` file is to describe your module and the details regarding it's ownership and distribution. In the early stages of your career it will be unlikely that you'll be creating many but it is worth being aware of as a Python developer!

In it's basic format you can get away with the below as your `setup.py` file:

```python
from setuptools import setup

setup(name="app")
```

There is all sorts of information you could / probably should provide such as:

* version='1.0'
* description='Python app'
* author='John Smith'
* author_email='JohnS@gmail.com'
* url='https://www.python.org/sigs/distutils-sig/'

However, in this instance we will keep the `setup.py` as is.

The next step is to utilise pip to install our package, this is to ensure that the Python interpreter is aware of our package and has referenced it into the local library.

* `pip install .` - what we are saying here is install the setup file from the local directory and pip looks for this file as part of it's standard search.

what you should see is something like the below output:

```text
Processing /Users/kierancornwall/workspace/Python_Dev_Curriculum/06_OOP/03_library_modules_&_packages/python_package
Building wheels for collected packages: app
  Running setup.py bdist_wheel for app ... done
  Stored in directory: /private/var/folders/g5/2kx9t92510gd0qx86hmtmc240000gn/T/pip-ephem-wheel-cache-tuo2rz7h/wheels/04/f7/81/9cf56a15687fc12b0a3147b518bbb8fa3cc983102a9dbcfa3d
Successfully built app
Installing collected packages: app
  Found existing installation: app 0.0.0
    Uninstalling app-0.0.0:
      Successfully uninstalled app-0.0.0
Successfully installed app-0.0.0
```

This shows that your app is successfully installed locally and will now be made available in your python library.


### app folder inputs


Within the app folder input the below into the fizzbuzz_oop.py file:

```python
class Fizzbuzz:

    def __init__(self, start_of_range, end_of_range):
        self.fizzrange = range_gen(start_of_range, end_of_range)
        self.fizzbuzz_list = []
        self._fizzbuzz_iterator()

    def _divisible_by(self, num1, num2):
        if num1 % num2 == 0:
            return True
        else:
            return False

    def _fizzbuzz_iterator(self):

        for num in self.fizzrange:
            if self._divisible_by(num, 15):
                self.fizzbuzz_list.append("fizzbuzz")
            elif self._divisible_by(num, 5):
                self.fizzbuzz_list.append("buzz")
            elif self._divisible_by(num, 3):
                self.fizzbuzz_list.append("fizz")
            else:
                self.fizzbuzz_list.append(num)
```


Let's now update our `program.py` file to invoke the fizzbuzz solution:

```python
from app.fizzbuzz_oop import Fizzbuzz

one_to_100 = Fizzbuzz(1, 100)

print(one_to_100.fizzbuzz_list)
```

* `from app.fizzbuzz_oop import Fizzbuzz` within our module importing we should now be able to reference and call our module using the 'dot' notation from our app folder.

When completing the rest of our code and run the file we should see the output of our fizzbuzz program. 

## Summary

You just:
* The python built in library 
* What are modules?
* pythons in built functions
* What is pip?
* Packages
