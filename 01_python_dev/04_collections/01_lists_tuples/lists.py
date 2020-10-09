# # Lists concepts are same as arrays in other languages
# # What is a List
# # Lists are a staple of data management within programmes and expands the ability to captrue and manage inbound data
# # Lists are mutable meaning we can change-add-delete elements for our list
# # Syntax: we use [] brackets to create a list so let's create one now
# # lists indexing - IMPORTANT - INDEXING STARTS FROM 0
#
# shopping_list = ["eggs", "bread, banana", "milk"]
# # let's print our list
# print(shopping_list)
#
# # How can we verify it's type?
# print(type(shopping_list))
#
# # How can I print only eggs and milk from our list?
# print(shopping_list[0])
# print(shopping_list[-1])
#
# # How can we change the value of index 0
# shopping_list[0] = "fruits"
# print(str(shopping_list) + " eggs have been replaced with fruits")

# Now we have our final list so we can start to manage it with some built in lists methods
# How can we add and item to our list?

shopping_list = ["fruits", "bread, banana", "milk"]
# we have an append() to add an item to our list
shopping_list.append("ice cream")
print(shopping_list)
print(len(shopping_list))

# How can we remove an item from our list
shopping_list.remove("fruits")
print(shopping_list)

# How can we remove the last entry from list
# we have a pop() that deletes the last item from the list
shopping_list.pop()
print(shopping_list)

# Can we mix data types in a list? yes
mixed_list = [1, 2, 3, "one", "two", "tree"]
print(mixed_list)

# List slicing is an important part of managing lists and allows us to carve out various area of an array
# how can we slice our lists?

print(mixed_list[1:3]) # outcome [2,3]
# slice two and three
print(mixed_list[-2::]) # double :: reverses the order of the slice
print(mixed_list[0:2])

# Time to Move onto Tuples