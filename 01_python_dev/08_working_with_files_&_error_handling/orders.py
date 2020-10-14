# Working with files and Handling errors/exceptions
# It is an important part of our routine tasks to deal with files
# create a file - read - write - and dealing with any error/exception

# we will create a file called orders.py use a in built python function open()
# STEP 1
# file = open("orders.text")
# if we run it now it'll throw an error that it can't the file

# STEP 2 - put this code in a try and except block of code
# try:
#     file = open("orders.text")
# except:
#    print(" There has been an error!")

# STEP 3 - put this code in a try and get except block to print the error as well
try:
    file = open("orders.text")
except FileNotFoundError as errmsg:
   print(" There has been an error!" + str(errmsg))


# STEP 4 - put this code in a try and get except block to print the error as well
try:
    file = open("orders.text")
except FileNotFoundError as errmsg:
   print(" There has been an error!" + str(errmsg))
