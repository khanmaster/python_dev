# Classes, class - objects and instantiation
# How to create a class and class objects

# Classes ae a way of bringing both data and functionality together
# Let's create a class called Dog

# Syntax - class Dog: (class is a key word - first letter is capital as a good practice of naming convention)
# STEP 1
# class Dog: # key word class followed by name of the class with : at the end
# # creating a class Dog
#
#     animal_kind = "canine" # creating a class variable called animal_kind
#
#     def bark(self): # method of our class - method not a function as it's inside our class
#         # self refers to current class meaning belongs to Dog class
#
#         return "woof"

class Dog: # key word class followed by name of the class with : at the end
# creating a class Dog

    animal_kind = "canine" # creating a class variable called animal_kind

    def bark(self): # method of our class - method not a function as it's inside our class
        # self refers to current class meaning belongs to Dog class
        self.animal_kind
        return "woof"

# creating an object from a class is called instantiaion
# we will create 2 dogs fido and lassie that will inherit from our Dog class

fido = Dog() # To instantiate a class it must be assigned to a variable
lassie = Dog() # To instantiate a class it must be assigned to a variable

print(Dog.animal_kind)
print(type(fido.bark()))
print(type(fido))
print(lassie.bark())
print(lassie.animal_kind)

# Very important to understand that despite deriving details from our Dog class
# fido and lassie are two completely diferent objects
# changing one will not impact the other

fido.animal_kind = "Big Dog"
print(fido.animal_kind) # changed to Big Dog
print(lassie.animal_kind) # no changes
# This is  the prime example of polymorphism

# Draw up a diagram for what has been covered so far

# Moving onto the DANGER of class variables

# what would happen if our class variable animal_kind got changed?
Dog.animal_kind = "Dolphin"

print(lassie.animal_kind)
# lassie has been changed to dolphin

print(lassie.bark())
# but our lassie still barks

# Time to take a break & we'll have a look at how to resolve this issue

# Summary
# You just:
#
# How to create a class and add class objects
# Class Creation & Attributes
# Understanding self
# Reviewing our Dog Class
# Instantiation of a class
# The DANGER of class variables