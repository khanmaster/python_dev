#Unit Testing and TDD

## Timings

This lesson should take between 15 to 20 minutes to complete.


## This lesson covers
The below concepts will be discussed: -

* Unit testing
* TDD

The aim of this lesson is to bring the concepts and ideas of each which will be backed up throughout all of the practicals across the SDET course.

# What is unit testing
Before we fly into coding let's define exactly what unit testing is and why it's worth doing.

* At a high-level, unit testing refers to the practice of testing certain functions and areas – or units – of our code. This gives us the ability to verify that our functions work as expected. That is to say that for any function and given a set of inputs, we can determine if the function is returning the proper values and will gracefully handle failures during the course of execution should invalid input be provided.

These tests help us validate the logic of our implementation. As you write more tests, you end up creating a suite of tests that you can run at any time during development to continually verify the quality of your work.

A second advantage to approaching development from a unit testing perspective is that you'll likely be writing code that is easy to test. Since unit testing requires that your code be easily testable, it means that your code must support this particular type of evaluation. As such, you're more likely to have a higher number of smaller, more focused functions that provide a single operation on a set of data rather than large functions performing a number of different operations.

A third advantage for writing solid unit tests and well-tested code is that you can prevent future changes from breaking functionality. Since you're testing your code as you introduce your functionality, you're going to begin developing a suite of test cases that can be run each time you work on your logic. When a failure happens, you know that you have something to address.

Of course, this comes at the expense of investing time to write a suite of tests early in development, but as the project grows you can simply run the tests that you've developed to ensure that existing functionality isn't broken when new functionality is introduced.

# What is TDD

The idea of test-driven development (TDD) was first brought to a wider audience by Kent Beck in his 2000 book Extreme Programming Explained. Instead of always writing tests for some code we already have, we work in a red-green loop:

* Write the smallest possible test case that matches what we need to program.
* Run the test and watch it fail. This gets you into thinking how to write only the code that makes it pass.
* Write some code with the goal of making the test pass.
* Run your test suite. Repeat steps 3 and 4 until all tests pass.
* Go back and refactor your new code, making it as simple and clear as possible while keeping the test suite green.

# Why TDD
 
 Unit testing is the 'cheapest' form of testing. What this means is that it is, at least when written correctly, abstracted as it will belong to the functionality of individual objects, will run fast as they're often lightweight and lastly can provide excellent coverage.
 
 *__Important Note__* - Unit tests, dependant on their quality, they should be providing fast feedback to developers and give confidence that nothing is broken.
 
 You will here this many times in your career: -
 
 "We don't need to unit test we deliver working code"
 
 This style of development serves several purposes: -
 1. Naturally makes you think about what you are doing
 2. By it's nature develops unit test coverage
 3. Gives confidence in changing areas of code because if the test works, the code (should work)
 
 #The How of TDD
 
 Common practice in a TDD environment means writing a test before you write any functional code. There are various stated reasons for doing this but in general it helps: -
 
 1. you think about what you intend to build
 2. separate tasks into logical testable blocks
 3. ensure that the tests can run against your class to make sure it does what it is meant to do
  
 Other benefits often are that developers, QA's and in some cases customers can read through your tests and understand the function of the class
 
 ##Red, Green and Refactor
 
 You will come across this terminology regularly in any form of coding:
 
 • **Red** - Right a test before writing any functional code. Run the test and it will fail (Show as red)
 * **Green** - Now begin to write your code/object to make the test pass
 * **Refactor** - now you have a layer of confidence in that your class/object does what it is meant to do you can begin to look into refactoring (improving) your code and if the test passes the functionality will still work.

![TDD](../assets/TDD.png)