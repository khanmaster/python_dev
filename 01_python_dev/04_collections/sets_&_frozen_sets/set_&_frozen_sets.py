# We will briefly touch base on sets and frozen set as it is very similar to lists
# Set and Frozen Sets: The key difference between lists and sets is that sets are unordered and unindexed
# Syntax: We use {curly brackets} but treat it like a list rather than a dictionary

# Example:
car_part = {"wheels", "doors", "exhaust"}
print(car_part)
# Let's just re-run the file few times

# How can I add and item to our set
# add() method is used to add more details

car_part.add("windows")
print(car_part)

# Frozen sets are rarely used

index = frozenset([1, 23, 4])
print(index)

# There are several other methods available to use - visit python - documentation