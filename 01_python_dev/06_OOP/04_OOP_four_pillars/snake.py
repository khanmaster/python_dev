# ENCAPSULATION relates to hiding certain details from users
# before we start let's go back to our diagram briefly

from reptile import Reptile

class Snake(Reptile):

      def __init__(self):
          super().__init__()
          self.cold_blooded = True
          self.forked_tongue = True
          self.venom = None
          self.limbs = False

      def use_tongue_to_smell(self):
          return "I can smell the taste ... :)"

# if we instantiate our snake as below
sidney = Snake()

print(sidney.use_tongue_to_smell())
# calling method from snake class

print(sidney.seek_heat())
# calling methods from parent class - this is now double inheritance

# to encapsulate (hide or make it private) we can add __before heat methods
# it should throw an error as it can't be found publically

# MOVING ONTO POLYMORPHISM
