# There are several python unit test frame-works and we will focus on pytest as it's one the widest used
# although we will also take a look at unittest as it's part of python library

# Let's dive straight into creating test using TDD process
# we write the tests before we writing actual code

from calc import SimpleCalc
import unittest

class Calctests(unittest.TestCase):
# unittest.TestCase works with unittest frame work from a base class tests
    cacl = SimpleCalc()
    # creating object of simplecalc class

# Lets create our first test for add function using asserEqual method
# IMPORTATN WE MUST USE test work in our functions so python interpretor knows what are we testing

    def test_add(self):
        self.assertEqual(self.cacl.add(2, 4), 6)
        # testing if  2 + 4 = 6? True so the test will pass

# run pytest command: python -m pytest
# now code an add function in calc.py
    def test_subtract(self):
        self.assertEqual(self.cacl.subtract(4, 2), 2)
    # testing if 4-2 = 2? True - test passed

# run pytest command: python -m pytest
# now code an subtract function in calc.py

    def test_multiply(self):
        self.assertEqual(self.cacl.multiply(2, 2), 4)
    # testing if 2 * 2 = 4 True - test passed

    def test_divide(self):
        self.assertEqual(self.cacl.divide(6, 3), 2)
    # testing if 6 / 3 = 2 - outcome - True - Test passed

# command - python -m pytest -v
# if __name__ == '__main__':
    if __name__ == '__main__':
        unittest.main()

