# creating Animal class
class Animal:

    # __init__ to declare attributes
    def __init__(self):
        self.alive = True
        self.spine = True
        self.alive = True
        self.lungs = True

    # create methods of our animal
    def breathe(self):
        return "keep breathing to stay alive"

    # create methods of our animal
    def move(self):
        return "left right and centre"

    # create methods of our animal
    def eat(self):
        return "nom nom nom.... "


# Now we have 3 within the class and 4 attributes/variables

# if we instantiate our animal class with cat object cat will be able to ABSTRACT methods
cat = Animal()

# Let's abstract breathing method from Animal class
#print(cat.breathe())
# breathing is now ABSTRACTED the user does not know how breath is implemented
# how it works but they can use the method to achieve taking breath

# NEXT - Inheritance
# Let's create a file called reptile.py
