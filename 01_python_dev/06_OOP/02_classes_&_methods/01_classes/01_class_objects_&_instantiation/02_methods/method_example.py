# Let's have a look at methods in a bit more details
# what is private and getters and setters

# STEP1
# class MethodExamples:
#     this_can_be_accessed_easily = "Hi, I can be found easily"
#
# method_example_object = MethodExamples()
#
# print(method_example_object.this_can_be_accessed_easily)
#
# method_example_object.this_can_be_accessed_easily = "I have changed"
# print(method_example_object.this_can_be_accessed_easily)

# # STEP-2
# # Let's resolve this issue by moving it inside an init method
# class MethodExamples:
#     def __init__(self):
#      self.this_can_be_accessed_easily = "Hi, I can be found easily"
#
# m = MethodExamples()
#
# print(m.this_can_be_accessed_easily)
#
# m.this_can_be_accessed_easily = "I have changed"
# print(m.this_can_be_accessed_easily)


# STEP 3


# Let's resolve this issue by moving it inside an init method
class MethodExamples:
    def __init__(self):
     self.this_can_be_accessed_easily = "Hi, I can be found easily"
     # put an _ sefl._and try the same code and it will give you the error
    def get_this_can_be_accessed_easily(self):
        return self.this_can_be_accessed_easily

    def set_this_can_be_accessed_easily(self, value_to_be_set):
        self.this_can_be_accessed_easily = value_to_be_set

m = MethodExamples()

print(m.get_this_can_be_accessed_easily())

m.set_this_can_be_accessed_easily = "I have changed"

print(m.get_this_can_be_accessed_easily())

# Lab
# Create a car class. Give the vehicle a maximum speed, and keep track of the current speed of the vehicle. It doesn't make sense for the speed to be adjusted directly, so put an underscore in front of it and implement a speed getter as well as accelerate and brake setter methods that change the speed in a logical way.
#
# Do your methods make sense? Does braking past 0 cause the speed to increase? Can you accelerate past the car's top speed?
#
# See car_class.py for an example answer
#
# Summary
# As briefly discussed good practice is always open for argument but the 'hiding' of code and particular variables/functions/methods can be very important in only exposing details that the user needs and prevents confusion with large amounts of methods that only do work within your object.
#
# This is a bit of a mind bender but hopefully more will become clear when we look into the 'four pillars of Dev' in the next lessons.
#
# But now we'll move onto a lab.
#
# You just:
#
# Methods in Python
# Pythonic Magic
# Understanding private and getters and setters