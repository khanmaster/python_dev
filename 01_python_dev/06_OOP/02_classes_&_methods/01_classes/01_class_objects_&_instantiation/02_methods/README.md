# Methods, getters and setters 

## Timings

15 - 25 Mins

## This lesson includes

* Methods in Python
* Pythonic Magic
* Understanding private and getters and setters


In this lessons we will elaborate a little further into methods in Python, introduce the concept of making variables private

## Methods

This will be a very brief step and methods are functions that are part of an object and require self to be passed to them as an argument. 

Everything we learned about functions i.e. passing arguments, providing defaults and multiple arguments are exactly the same. We do need to elaborate on the concept of private variables and getter and setters.


## Pythonic magic

We would have seen that we're able to access our initialised data variables simply by setting them, example below:

```python
class MethodExamples:

    this_can_be_accessed_easily = "Hi, here I am easily found"
    

x = MethodExamples()
# type in x. and the below image should appear on the IDE

```
![](../../../assets/pythonic_mag.png)

You will be able to see that an 'f' function has appeared around our string variable. This is Pythonic wonderment as the Python interpreter automatically generates accessors for you. Let's take a look at the below code:

```python
class MethodExamples:

    this_can_be_accessed_easily = "Hi, here I am easily found"


x = MethodExamples()

print(x.this_can_be_accessed_easily)
x.this_can_be_accessed_easily = "I have changed"
print(x.this_can_be_accessed_easily)

```
As we can see in this class we are printing the variable using, what can be referred to as the 'getter' function that python automatically generates for us `print(x.this_can_be_accessed_easily)`.

We can also change the value by calling the method and setting and changing it - `x.this_can_be_accessed_easily = "I have changed"`

and when we print this we should see:

```text
Hi, here I am easily found
I have changed
```

This Pythonic magic saves us a lot of time but this relates to a class variable and is accessible anywhere as we know. Let's move it into the `__init__` method as we should use for created data within our objects:

```python
class MethodExamples:

    # this_can_be_accessed_easily = "Hi, here I am easily found"

    def __init__(self):
        self.this_can_be_accessed_easily = "Hi, here I am easily found"


x = MethodExamples()

print(x.this_can_be_accessed_easily)
x.this_can_be_accessed_easily = "I have changed"
print(x.this_can_be_accessed_easily)
```

again nothing should change... but what it Python didn't deliver all the above magic?

```python
class MethodExamples:

    # this_can_be_accessed_easily = "Hi, here I am easily found"

    def __init__(self):
        self.this_can_be_accessed_easily = "Hi, here I am easily found"

    def get_this_can_be_accessed_easily(self):
        return self.this_can_be_accessed_easily

    def set_this_can_be_accessed_easily(self, value_to_be_set):
        self.this_can_be_accessed_easily = value_to_be_set

x = MethodExamples()

print(x.get_this_can_be_accessed_easily())
x.set_this_can_be_accessed_easily("I have changed")
print(x.get_this_can_be_accessed_easily())
```

so, let us be grateful for Pythonic magic but it is very important to understand what happens behind the scenes.

## The idea of private with getters and setters

This a discussion around a convention more than anything else. Many strong typed languages such as Java and C# have the concept of a setting a variable or methods accessibility status with the terms `public` (open to change) i.e. open to the instantiation of a class or `private` (protected from change) i.e. it will only be available to the class itself.

The reason for this action of making something private is open to much debate in coding communities and in particular specific languages. Java as a language demands you explicitly type whether your variable / method will be private of public to the class. Python does not use this concept particularly often as it is viewed as 'defensive' coding, this is not part of this course but it is important to be aware of the principle and how to create private methods / variables within Python.

 This practice in stronger typed languages forms part of the encapsulation principle and this will be discussed in following lessons.

Let's take our previous code and add an underscore `_` to our variable in self:

`self._this_can_be_accessed_easily = "Hi, here I am easily found"`

```python
class MethodExamples:

    # this_can_be_accessed_easily = "Hi, here I am easily found"

    def __init__(self):
        self._this_can_be_accessed_easily = "Hi, here I am easily found"

    # def get_this_can_be_accessed_easily(self):
    #     return self.this_can_be_accessed_easily
    #
    # def set_this_can_be_accessed_easily(self, value_to_be_set):
    #     self.this_can_be_accessed_easily = value_to_be_set

x = MethodExamples()

print(x.get_this_can_be_accessed_easily())
x.set_this_can_be_accessed_easily("I have changed")
print(x.get_this_can_be_accessed_easily())
```

The interpreter will no longer deliver the pythonic magic of generating our getter and setter automatically. If we now uncomment our manual methods and amend the details correctly we should be able to access the details:

```python
class MethodExamples:

    # this_can_be_accessed_easily = "Hi, here I am easily found"

    def __init__(self):
        self._this_can_be_accessed_easily = "Hi, here I am easily found"

    def get_this_can_be_accessed_easily(self):
        return self._this_can_be_accessed_easily

    def set_this_can_be_accessed_easily(self, value_to_be_set):
        self._this_can_be_accessed_easily = value_to_be_set

x = MethodExamples()

print(x.get_this_can_be_accessed_easily())
x.set_this_can_be_accessed_easily("I have changed")
print(x.get_this_can_be_accessed_easily())
```

by using the underscore at the start of the variable you are telling the python interpreter to, essentially, not generate the getters and setters automatically.

The same can be said for methods however in this instance we will use a double underscore:

```python
class MethodExamples:

    # this_can_be_accessed_easily = "Hi, here I am easily found"

    def __init__(self):
        self._this_can_be_accessed_easily = "Hi, here I am easily found"

    def __get_this_can_be_accessed_easily(self):
        return self._this_can_be_accessed_easily

    def set_this_can_be_accessed_easily(self, value_to_be_set):
        self._this_can_be_accessed_easily = value_to_be_set

x = MethodExamples()

print(x.get_this_can_be_accessed_easily())
x.set_this_can_be_accessed_easily("I have changed")
print(x.get_this_can_be_accessed_easily()
```
The moment you use the double underscore the method the interpreter should highlight that it can no longer find our get variable and we would need to create another method that would be deemed public to access it.

## Lab

Create a car class.  Give the vehicle a maximum speed, and keep track of the current speed of the vehicle.  It doesn't make sense for the speed to be adjusted directly, so put an underscore in front of it and implement a speed getter as well as accelerate and brake setter methods that change the speed in a logical way.

Do your methods make sense?  Does braking past 0 cause the speed to increase?  Can you accelerate past the car's top speed?

> See car_class.py for an example answer

## Summary

As briefly discussed good practice is always open for argument but the 'hiding' of code and particular variables/functions/methods can be very important in only exposing details that the user needs and prevents confusion with large amounts of methods that only do work within your object.

This is a bit of a mind bender but hopefully more will become clear when we look into the 'four pillars of Dev' in the next lessons.

But now we'll move onto a lab.

You just:
* Methods in Python
* Pythonic Magic
* Understanding private and getters and setters