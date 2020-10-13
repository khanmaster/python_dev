# our reptile class will inherit everything from Animal class

from animal import Animal
# Let's go back to our diagram

class Reptile(Animal):

    def __init__(self):

# Python has a keyword super().__init__()
# super in this context is a keyword relating to the base class
# which in this instance is animal
# essentially this is python syntactic sugar for saying
# let's include and initialise everything in the base class of Animal for use in Reptile

        super().__init__() # super is used?
        self.cold_blooded = True
        self.tetrapod = None # should be set to None as not all reptiles are tetrapods
        self.heat_chambers = [3, 4]

    # let's add our reptile behaviours
    def seek_heat(self):
        return "it freezing ... looking for a sub shine"

    def hunt(self):
        return "working hard to catch next meal"

    def use_venom(self):
        return "if I've got it I'm using it"

# Let's see the amazing benefits of Inheritance
# all methods attributes are now available in reptile - try now

# create an object of reptile
reptile_object = Reptile()

# let's utilise methods variables from our Animal class by inheriting it inside Reptile
print(reptile_object.eat())
# eat method is inherited from Animal class

print(reptile_object.move())
# from Animal
print(reptile_object.use_venom())

print(reptile_object.seek_heat())
# from reptile

# Moving on to ENCAPSULATION
# LET'S CREATE A CLASS CALLED SNAKE

# dog = Animal()
# print(dog.eat())