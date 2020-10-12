# Introduction to repr()

## Timings

30 Mins

## This lesson includes
* str
* repr
* format

## Representing objects

What happens when we print an object?  Let's demonstrate with a class that represents locations on the globe with latitude and longitude.

```python
class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

bham_academy = Location(52.488647, -1.887249)
print(bham_academy)
```

Your output will be something like: `<__main__.Location object at 0x0177C028>`.  This does tell us that it's a Location object, but it's not the most helpful output.

It would be better to have clearer string representations of our object.

### repr()

`repr()` gives us exactly that - a representation of our object.  Currently, repr will return exactly the same as what we see when we print our object, but we can give our class a dunder-repr method in order to produce an unambiguous representation of our object (i.e. the type of object, plus identifying fields).

```python
class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
    
    def __repr__(self):
        return f"Location(latitude={self.latitude}, longitude={self.longitude})"


bham_academy = Location(52.488647, -1.887249)
print(repr(bham_academy))
```

> Location(latitude=52.488647, longitude=-1.887249)

Some people argue that a good repr should look like source code - we could insert the output into Python and recreate the object.

repr() are designed for developers - they include all important identifying information and are very useful for debugging and logging, as the representation is what is shown in any debugging output.  Think about what information you would want to include whilst debugging your class - this is what you should include in the repr.

It's quick and easy to include a custom repr for your classes, so it's a good habit to develop!

### str()

Strings are designed to give readable, human-friendly output.  It defines the output for whenever the object is printed.  If there is no `__str__()` method, then the repr will be printed instead.

```python
class Location:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def __repr__(self):
        return f"Location(latitude={self.latitude}, longitude={self.longitude})"

    def __str__(self):
        return f"({self.latitude}, {self.longitude})"


bham_academy = Location(52.488647, -1.887249)
print(f"The Sparta Global Birmingham Academy is located at co-ordinates {bham_academy}")
```

### format()

When we print digits, we can easily change the format.  For example, we can format numbers as fixed-point or with exponential notation:

```python
n = 0.004837

print(f"Fixed Point: {n:f}")
print(f"Exponential Notation: {n:e}")
```

We can add custom formatting options to our classes.

```python
class Dog:
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f"A {self.age} year old Dog"

    def __format__(self, format_spec):
        if format_spec == "dog":
            return f"A {self.age * 7} dog-years old Dog"
        else:
            return self.__str__()


fido = Dog(5)
print(f"{fido}")
print(f"{fido:dog}")
```

f-strings give you the option of supplying `format_spec` after the colon.  This is a very simple example of what we can do with that spec.

## Summary

You just:
* Customised the repr, str and format methods for a class
