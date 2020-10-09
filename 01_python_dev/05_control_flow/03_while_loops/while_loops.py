# While loops are mostly used as a monitor rather than handling items

# x = 0
# while x < 10:
#     print(f"it's working ->{x}")
#     x += 1

# age = input("Please enter your age ")
# print(f" your age is {age}")
# user_prompt = True
#
# while user_prompt:
#     age = input("Please enter your age ")
#     if age.isdigit(): # isdigit() is to stop users entering strings
#         user_prompt = False
#     else:
#         print(" Please your answer in numbers")
# print(f"Your age is {age}")

user_prompt = True

while user_prompt:
    age = input("Please enter your age ")
    if age.isdigit() and int(age) < 117: # isdigit() is to stop users entering strings
        user_prompt = False
    else:
        print(" Please your answer in numbers")
print(f"Your age is {age}")

# Summary
# You just:
# While loops
# While loop uses
# while and if / break
# Verifying user input with while loops