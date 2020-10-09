# Loops are used to iterate through the data collections - lists -dictionaries etc
# Syntax: for is a key word used most OOP languages

# Let's use an example of our shopping list
#
# shopping_list = ["fruits", "milk", "cream", "bread"]
# print(shopping_list)
# for item in shopping_list:
#     print(item)

# # How can we loop though letters in string
# for letters in "fruits":
#     print(letters)
#
# # Using if statement to loop through our shopping list and "break" condition
#
# shopping_list = ["fruits", "milk", "cream", "bread"]
# print(shopping_list)
# for item in shopping_list:
#     print(item)
#     if item == "bread":
#         break

# Looping through the data in dictionary holding food bill

dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

for item in dict_data.values():
    print(item)

    # How can we get name and the bill amount owed for each person
    for embeded_value in item.values():
        print(embeded_value)

# Summary
# Mixing loops and if statements is pretty much what makes a developer. We will see how much of development as a whole hangs on the concepts of handling data types, within collections and that need to be parsed upon and decisions made.
#
# You just:
#
# Types of looping
# Creating a for loop
# nested for loops
# Loops and if statements