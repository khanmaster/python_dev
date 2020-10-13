# The four pillars of development

## Timings

45 - 60 Mins

## This lesson includes

* abstraction
* inheritance
* encapsulation
* polymorphism

There are four key principles of development that we all need to keep in focus when planning, building and developing code and they are abstraction,   encapsulation, inheritance and polymorphism and we will investigate each of them now.

## A brief intro 

The four principles or 'pillar of development' will keep your code and mindset on the write path to keep your products built in a clean sensible manner.

throughout these examples we will be stepping through the below image:

![](../../assets/OOP_python.png)

### Abstraction

We have been using abstraction many times already, when using functions and methods within our code. When we look back to our dog class we had the method bark, now this method only had a print statement but a method could contain no limit of functionality.

we use methods to abstract functionality or data from the user and present it via a method.

So, Let's start a new class called `animal.py` and complete the below code:

```python
class Animal:

    def __init__(self):
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath in and one breath out")

    def eat(self):
        print("nom nom nom nom")

    def procreate(self):
        print("time to find a mate")

    def move(self):
        print("onwards and upwards")

```

Ok, so we now have 4 methods within the class which if we instantiate an animal, let's say a cat will now have methods to breathe, eat, etc. as all animals should:
```python
cat = Animal()
cat.breathe()
```
returns `One breath in and one breath out`

breathing is now **Abstracted** the user does not now how breath is implemented, how it works but they can use the method to achieve taking a breathe.

### Inheritance
Inheritance is one of the key aspects of the four pillars and pretty much drives everything else and drives the core principles of the other three pillars. 

Let's dive straight in to how we go about doing it!:

```python
from animal import Animal

class Reptile(Animal):

    def __init__(self):
        super().__init__()
        self.cold_blooded = True
        self.tetrapod = None # should be set as not all reptiles are tetrapods...
        self.heart_chambers = [3, 4]
        self.amniotic_eggs = None

    def seek_heat(self):
        print("it's chilly outside, where's the sun or a decent hot spring")

    def hunt(self):
        print("wait for it, wait for it..... and pounce")

    def use_venom(self):
        print("if I've got it I'm using it")

    def attract_mate_through_scent(self):
        print("time to throw on the eau de toilette")
```

Brief walk through the core part of the code:

* `from animal import Animal` here we are calling our 'animal' file with the `from` keyword and then we're calling the location of our file. You may need to provide the file path to the animal.py if you have it held elsewhere. We then use the `import` statement and call the `Animal` class itself.

* `class Reptile(Animal):` Here we are now inheriting the `Animal` class into our reptile class.  

* `super().__init__()` super in this context is a keyword relating to the base class, which in this instance is `animal` essentially this is python syntactic sugar for saying let's include and initialise everything in the base class of Animal for use in Reptile 

What we mean by inheritance is that all of the variables and methods within animal should now be available in reptile:

 ![](../../assets/inherited_methods.png)
 
 So, we have now inherited all of the methods/functions relating to animal in our reptile. so, you can now see how you can build a huge amount of functionality into a program through inheritance and it is one of the most important things to consider when breaking your program up into smaller more manageable parts.

### Encapsulation
Encapsulation relates to hiding certain details from users. We briefly highlighted the details around making variables or even methods private to hide various aspects of a class from a user. 

Let's create another class called snake as below:

```python
from reptile import Reptile

class Snake(Reptile):

    def __init__(self):
        super().__init__()
        self.forked_tongue
        self.cold_blooded = True
        self.venom = None
        self.limbs = False

    def use_tongue_to_smell(self):
        print("Do I say it smells or tastes nice...?")

```

If we instantiate our snake as below:

```python
sidney = Snake()
sidney.seek_heat()
```

we should see `it's chilly outside, where's the sun or a decent hot spring`

Now we have double inheritance from Animal, reptile and now we have Snake inheriting from the previous two classes! 

However, if we wanted to encapsulate (make private) the seek heat class we can essentially hide the method by using an underscore

### Polymorphism 

Polymorphism means that even when inheriting from previous classes, new object can inherit but still override particular attributes or behaviour without affecting the super or base class. So, Let's create our final class called Python (see what we've done here ;-))

```python
from snake import Snake

class Python(Snake):

    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        print("ok, hand me the stretchy pants")

    def constrict(self):
        print("and...squeeeeeze")

    def climb(self):
        print("up we go")

    def shed_skin(self):
        print("I'm growing out of this now")
```

```python
peter = Python()
peter.breathe()
```
running the above should produce the information `One breath in and one breath out` all the way back from the Animal class!

Also, if you attempt to find the `_use_tongue_to_smell` method it should not be available to the Python class.

The key to hiding certain details is if you are building functions or methods within a class/module from a user. As a metaphor we know how to drive cars but we do not need to know how the engine works to drive. 

## Summary

You just:

* abstraction
* encapsulation
* inheritance
* polymorphism