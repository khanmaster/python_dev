# Classes, class objects and Instantiation

## Timings

30 - 45 Mins

## This lesson includes

* How to create a class and add class objects
* Class Creation & Attributes
* Understanding `self`
* Reviewing our Dog Class
* Instantiation of a class
* The DANGER of class variables

Classes are a way of bringing both data and functionality together and we will be looking at how it can work and the potential pitfalls of certain practices.

## Creating a class and it's attributes

Let's get straight into creating a class and we will use a dog as the object:

```python
class Dog:

    animal_kind = "canine" # class variable 

    def bark(self): # method 
        return "woof"
```

Let's step through the code line by line:

* `class Dog:` -> all classes are defined by using the `class` keyword followed by the name of the class. All class names follow what is referred to as 'Snake Case' i.e. if we had more than one word for the class it could be `WonderDog`. The class is finally closed off with a `:` similar to closing a function
* `animal_kind = "canine"` -> here we are setting a class variable and it looks like any other variable we have created but we will cover the scope of this through this walk through
* `def bark(self): return "woof"` -> ok, this looks a lot like a function but due to being within the scope of a class this is now known as a method. All the principles are exactly the same except for the `self` which has it's own section coming up.

But in terms of what we have just created can be visualised as below:

![](../../../../assets/OOP_dog_template.png)

We have created a template for a dog, a 'cookie cutter' if you will. We can use this class to create 100's, 1000's if not 1,000,000's of dogs all of which we be of `animal_type = "canine"` and have a method that will make them bark!

### Understanding 'Self' 

`self` can be a tough principle to grasp but essentially it means "I'm referring to the current class" i.e. In this case our Bark method is using self to say I am referring to the Dog class. 

We have our dog class and we have an class variable within it, and we have our bark method, let's just briefly step through how
our bark method could use the class variable:

```python
class Dog:

    animal_kind = "canine" # class variable which returns an attribute of String

    def bark(self):
        return "woof"
```

So, above we have our class variable and method. create an extra line above the bark method return statement and enter details as below:

```python
class Dog:

    animal_kind = "canine" # class variable which returns an attribute of String

    def bark(self):
        print(animal_kind)
        return "woof"
```

What you should find is that you have an `unresolved reference` error, which is essentially saying that it can't find it anywhere. This is because we need to use the `self` keyword to say "look at this current object" meaning the 'Dog' class:

```python
class Dog:

    animal_kind = "canine" # class variable which returns an attribute of String

    def bark(self):
        print(self.animal_kind)
        return "woof"
```

By applying the self keyword we have now resolved the issue because we've told our program to look into the 'Dog' class.

Let's see what happens when we take away the self reference in the method parenthesis:

```python
class Dog:

    animal_kind = "canine" # class variable which returns an attribute of String

    def bark():
        print(self.animal_kind)
        return "woof"
```

We should now see an error relating to an `unresolved reference` relating to self. Which means without self being declared in the method it will not be aware of the internal assets of the Dog class.

We will be revisiting this regularly throughout the rest of this course.

***Note to Trainer*** -> Ensure the program is reset to the below:

 ```python
class Dog:

    animal_kind = "canine" # class variable which returns an attribute of String

    def bark(self):
        return "woof"
```

## Reviewing our Dog Class

So, we have created our Dog class which we view as a template with things that we consider to be the core of a dog i.e. it's a canine and it can bark.

But what can we do with the template itself?

We ca call certain aspects of our template as below:

```python
print(Dog.animal_kind)
print(Dog.bark())
```  

We will see two things returned:

* `canine` This is the contents of ou class variable and as it's a variable it can be accessed easily 
* `<function Dog.bark at 0x103141400>` What we have received here is a reference to the function (which should be refered to as method because it is part of the Dog Object). The reference number at the end was it's storage location within memory when the program was run.

So, why didn't it print `"woof""`?

The reason is that methods only function when the a class (object) has been instantiated i.e. created. What we're doing is asking behaviour of template, we can request attributes of a template but you wouldn't ask a 'template' of a dog to bark..... You need a dog for that...

So, let's create a dog.

## Instantiation of a class

Creating an object from a class is called 'instantiation' or 'instantiating a class'. we're going to create two dogs called 'fido' and 'lassie' that will inherit from our dog class:

```python
class Dog:

    animal_kind = "canine" 

    def bark(self): 
        self.animal_kind
        return "woof"
        
fido = Dog()
lassie = Dog()

```

* `fido = Dog()` to instantiate a class it must be assigned to a variable and accessed using the class name itself followed by parenthesis. Without the parenthesis the interpreter will wait for you to use an attribute of the class similar to when we called the `animal_type` earlier.

Now we have created out two dogs let's take a look at some of the details:

```python
print(type(fido))
print(type(lassie))
print(fido.animal_kind)
print(lassie.animal_kind)
print(fido.bark())
print(lassie.bark())
```
The output should be:

```text
<class '__main__.Dog'>
<class '__main__.Dog'>
canine
canine
woof
woof
```

Now it's important to understand that despite deriving details from our Dog lass these are two completely distinct objects now. If we change one it will not affect the other:

```python
fido.animal_kind = "Big Dog"

print(fido.animal_kind) # output will be "Bid Dog"
print(lassie.animal_kind) # output will be canine
```

This is the benefit of instantiating objects as you can have multiple objects that can adapt and change (polymorphic).

so far things look like below visually:

***Note to Trainer*** -> draw out a basic flow similar to below to help visualise what's happening to the students:

![](../../../../assets/OOP_dogs_phase1.png)


### The DANGER of class variables

we have a Class variable called `animal_kind` so what would happen if we changed this?

```python
Dog.animal_kind = "Dolphin"

print(fido.animal_kind) # output will be "Dolphin"
print(lassie.animal_kind) # output will be "Dolphin"
```
If you run the above program our dogs should now be dolphins, however if you select and print our bark method our dolphins will bark!

 ```python
Dog.animal_kind = "dolphin"
#
print(fido.animal_kind)
print(lassie.animal_kind)
#
# # However, our dolphins still bark
print(fido.bark())
print(lassie.bark())
```
Output should be:

```text
dolphin
dolphin
woof
woof
```

![](../../../../assets/OOP_dogs_phase2.png)

As you can see there is a huge danger using class variables as they can change or be changed at various stages which could affect an entire program! 

Take a break and we'll show how this is solved in the following lesson.


## Summary

You just:
* How to create a class and add class objects
* Class Creation & Attributes
* Understanding `self`
* Reviewing our Dog Class
* Instantiation of a class
* The DANGER of class variables