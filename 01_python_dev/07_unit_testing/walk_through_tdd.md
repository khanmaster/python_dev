# Unit Testing in Python

## Timings

45 - 60 Mins

## This lesson includes

* Available frameworks
* unittest
* Setting up Pytest
* Some simple examples

As discussed unit testing is vital in any kind of code productions and we will be looking into the available frameworks and practices.

## Available frameworks

There are a numerous amounts of Python unit test frameworks and through this particular lesson we will focus on PyTest as it's one of the widest used packages although we will also take a look at unittest as it's part of the python library.

## Unittest introduction

next lets's create our unit test file and call it `test_unittest_simplecalc.py` there is a reason for this being quite long... you will see later

The set up we will create for our unittest example will be pretty simple but it is worth being aware of the simple usage of this in built framework.

And we are following what is a TDD process here ad we're writing our tests before writing the actual code:

```python
from simple_calc import SimpleCalc
import unittest

class Calctests(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2, 2), 4)

    def test_divide(self):
        self.assertEqual(self.calc.divide(6, 3), 2)
```

* `from simple_calc import SimpleCalc` here we are importing our SimpleCalc class
* `import unittest` we also need to import the unittest library
* `class Calctests(unittest.TestCase):` with the unittest framework works from a base class of TestCase with the tests (methods) themselves are built within the subclasses to TestCase. Therefore we need to pass the base class of `unittest.Testcase`. **It is important to note that the assertion methods are inherited from the Testcase class which you will see below 
* `calc = SimpleCalc()` Here we are instantiating our calculator class to be used within the TestCase methods.
* `def test_add(self):
          self.assertEqual(self.calc.add(2, 4), 6)` This particular method is our test itself, we have inherited the base class and now we are implementing the tests themselves. The `self.assertEqual()` method expects to validate that whatever is passed in arg1 will match arg2.

**Running the tests** we will go deeper into running tests shortly but for now we need to run our tests and make sure that our tests are failing. You can simple use the green arrows on the IDE to run or head to the folder where your tests are located and run `python -m unittest`:

output should lead to something as below:

```text
ImportError: cannot import name 'SimpleCalc' from 'simple_calc' (/Users/<username>/workspace/Python_Dev_Curriculum/07_Unit_Testing/simple_calc.py)


Ran 1 test in 0.003s

FAILED (errors=1)
```
   
Unit testing can be relatively simple but can expand in difficulty very quickly.

There are also numerous assertions that are inherited from the TestCase base class, assertions are everything in testing...

|Method |	Checks that|	New in |
|:---|:---|:---|
|assertEqual(a, b)        | a == b              ||
|assertNotEqual(a, b)     |	a != b              ||	 
|assertTrue(x)            |	bool(x) is True     ||	 
|assertFalse(x)           |	bool(x) is False    ||	 
|assertIs(a, b)           |	a is b	            |3.1|
|assertIsNot(a, b)        |	a is not b          |3.1|
|assertIsNone(x)          |	x is None           |3.1|
|assertIsNotNone(x)       |	x is not None       |3.1|
|assertIn(a, b)           |	a in b              |3.1|
|assertNotIn(a, b)        |	a not in b	        |3.1|
|assertIsInstance(a, b)   |	isinstance(a, b)    |3.2|
|assertNotIsInstance(a, b)|	not isinstance(a, b)|3.2| 


Let's step straight into a building our class and create a file called `calc.py` and add the below code:

***Note to Trainer*** run the tests for each stage of implementation i.e. class creation, method by method to show TDD in action.

```python
class SimpleCalc:

    def add(self, int1, int2):
        return int1 + int2

    def subtract(self, int1, int2):
        return int1 - int2

    def multiply(self, int1, int2):
        return int1 * int2

    def divide(self, int1, int2):
        return int1 / int2
```


## running the tests

You will be able to run the tests from the IDE but it's best to get used to running the tests in the command line as standard:

if you access the folder in which your tests are located and run:

`python -m unittest` 

your tests should run and produce:

```text
....
----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

You can add more details by providing the flag of `-v` for verbose:

`python -m unittest` 

should produce:

```text
test_add (test_unittest_simplecalc.Calctests) ... ok
test_divide (test_unittest_simplecalc.Calctests) ... ok
test_multiply (test_unittest_simplecalc.Calctests) ... ok
test_subtract (test_unittest_simplecalc.Calctests) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

You can also specify specific methods you wish to test which can be extremely useful:

`python -m unittest test_unittest_simplecalc.CalcTests.test_add -v` 

```text
test_add (test_unittest_simplecalc.CalcTests) ... ok

----------------------------------------------------------------------
Ran 1 test in 0.000s

OK
```

lastly, if you have multiple files you can use the `discover` argument that will search for all files with the name of `test*.py` which is why we used the large name in the first place :-)

`python -m unittest discover -v`

should produce:

```text
test_add (test_unittest_simplecalc.CalcTests) ... ok
test_divide (test_unittest_simplecalc.CalcTests) ... ok
test_multiply (test_unittest_simplecalc.CalcTests) ... ok
test_subtract (test_unittest_simplecalc.CalcTests) ... ok

----------------------------------------------------------------------
Ran 4 tests in 0.000s

OK
```

## Implementing PyTest

first of all we need to install the PyTest package using pip:

`pip install -U pytest`

We are using the -U flag to upgrade to the latest version if necessary, if successful you should see something as below:

```text
Collecting pytest
  Downloading https://files.pythonhosted.org/packages/51/b2/2fa8e8b179c792c457c2f7800f1313bfbd34f515e3a833e6083121844c14/pytest-4.3.0-py2.py3-none-any.whl (219kB)
    100% |████████████████████████████████| 225kB 13.3MB/s 
Requirement already satisfied, skipping upgrade: py>=1.5.0 in /usr/local/lib/python3.7/site-packages (from pytest) (1.7.0)
Requirement already satisfied, skipping upgrade: pluggy>=0.7 in /usr/local/lib/python3.7/site-packages (from pytest) (0.8.1)
Requirement already satisfied, skipping upgrade: setuptools in /usr/local/lib/python3.7/site-packages (from pytest) (40.6.3)
Requirement already satisfied, skipping upgrade: atomicwrites>=1.0 in /usr/local/lib/python3.7/site-packages (from pytest) (1.2.1)
Requirement already satisfied, skipping upgrade: more-itertools>=4.0.0; python_version > "2.7" in /usr/local/lib/python3.7/site-packages (from pytest) (5.0.0)
Requirement already satisfied, skipping upgrade: attrs>=17.4.0 in /usr/local/lib/python3.7/site-packages (from pytest) (18.2.0)
Requirement already satisfied, skipping upgrade: six>=1.10.0 in /usr/local/lib/python3.7/site-packages (from pytest) (1.12.0)
Installing collected packages: pytest
  Found existing installation: pytest 4.1.1
    Uninstalling pytest-4.1.1:
      Successfully uninstalled pytest-4.1.1
Successfully installed pytest-4.3.0
```

### PyTest and unittest support

out of the box pytest supports unittest as a runner, we should still be in the pathway of our tests. To run pytest you simply write pytest in the command line and you should see that it will run out unittest tests:

```text
======================================================================================== test session starts ========================================================================================
platform darwin -- Python 3.7.2, pytest-4.3.0, py-1.7.0, pluggy-0.8.1
rootdir: /Users/kierancornwall/workspace/Python_Dev_Curriculum/07_Unit_Testing, inifile:
collected 4 items                                                                                                                                                                                   

test_unittest_simplecalc.py ....                                                                                                                                                              [100%]

===================================================================================== 4 passed in 0.02 seconds ======================================================================================
```

We can also provide the -v flag for a verbose output:

`pytest -v`

```text
collected 4 items                                                                                                                                                                                   

test_unittest_simplecalc.py::CalcTests::test_add PASSED                                                                                                                                       [ 25%]
test_unittest_simplecalc.py::CalcTests::test_divide PASSED                                                                                                                                    [ 50%]
test_unittest_simplecalc.py::CalcTests::test_multiply PASSED                                                                                                                                  [ 75%]
test_unittest_simplecalc.py::CalcTests::test_subtract PASSED                                                                                                                                  [100%]

===================================================================================== 4 passed in 0.02 seconds ======================================================================================
```

When running `pytest` it will automatically search for any files that have `test_*.py` or `_test*.py` in the files name and run it.  

## Where pytest truly differs from unittest

Pytest focuses on simlicity and whereas unittest relies on create classes with the inheritance of `unittest.TestCase` pytest can be used in an easier manner.

**Note** -> At this stage you can leave your unittest file in place or move it to another folder to make the lesson easier. The file structure in this lesson keeps the tests in place.

Pytest will allow you to add assertions directly into a module and functions without the need to create a class and inherit the assert functions.

let's create a new file and call it `sci_calc.py` and add the below:

```python
import math


def find_sqrt(num):
    return math.sqrt(num)


def find_ceil(num):
    return math.ceil(num)
```

we now have some basic functions to test and yes we are not doing this in a TDD fashion, the major argument being pragmatism. If you are building small pieces of code it makes more sense to understand what is taking place and build sensible tests rather than assuming and have a long time debiggong particular areas.

Now let's create our unit test file `sci_calc_test.py` and input the following:

```python
from sci_calc import *


def test_find_sqrt():
    assert find_sqrt(100) == 10.0


def test_find_ceil():
    assert find_ceil(12.7) == 13
```

As you can see above we merely have to use the assert keyword and use `==` to check the value. This is part of the 'syntactic sugar' so to speak which makes pytest stand apart.

running the file using pytest should yield:

```text
======================================================================================== test session starts ========================================================================================
platform darwin -- Python 3.7.2, pytest-4.3.0, py-1.7.0, pluggy-0.8.1 -- /usr/local/opt/python/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/kierancornwall/workspace/Python_Dev_Curriculum/07_Unit_Testing, inifile:
collected 6 items                                                                                                                                                                                   

sci_calc_test.py::test_find_sqrt PASSED                                                                                                                                                       [ 16%]
sci_calc_test.py::test_find_ceil PASSED                                                                                                                                                       [ 33%]
test_unittest_simplecalc.py::CalcTests::test_add PASSED                                                                                                                                       [ 50%]
test_unittest_simplecalc.py::CalcTests::test_divide PASSED                                                                                                                                    [ 66%]
test_unittest_simplecalc.py::CalcTests::test_multiply PASSED                                                                                                                                  [ 83%]
test_unittest_simplecalc.py::CalcTests::test_subtract PASSED                                                                                                                                  [100%]

===================================================================================== 6 passed in 0.07 seconds ======================================================================================
```

What we have built here so far is pretty basic and as we move through our python careers we will need more in depth knowledge of the framework but for now we will be implementing unit tests as much as possible throughout our coding practice.

## Summary

You just:
* Available frameworks
* unittest
* Setting up Pytest
* Some simple examples