# Working with files and Handling errors/exceptions
# It is an important part of our routine tasks to deal with files
# create a file - read - write - and dealing with any error/exception

# we will create a file called orders.py use a in built python function open()
# STEP 1
# file = open("orders.text")
# if we run it now it'll throw an error that it can't the file

# STEP 2 - put this code in a try and except block of code
try:
    file = open("orders.text")
except:
   print(" There has been an error!")

# STEP 3 - put this code in a try and get except block to print the error as well
try:
    file = open("orders.text")
except FileNotFoundError as errmsg:
   print(" There has been an error!" + str(errmsg))
#

STEP 4 using RAISE key word
#put this code in a try and get except and raise - to raise the exception
block to print the error as well
try:
    file = open("orders.text")
except FileNotFoundError as errmsg:
   print(" There has been an error!" + str(errmsg))
   raise
# this will result in raising back the actual exception


# STEP 5 READING FILES
# Let's touch base file mode r-read w-write x-create new file if already exists it fails
# a-open file in append mode - if file does not exist it creates a new one
# t-this is default mode- it opens in text mode
# b-binary mode. + will open file for reading and writing and updating

# Let's create a function to open and print file
def open_and_print_file(file):
 try:
    opened_file = open(file, 'r')
    # reading and storing the file content into a variable

    file_line_list = opened_file.readlines()
    # reading line by line and storing in a list

    for line in file_line_list:
    # iterating through all the lines

        print(line.rstrip('\n')) # '\n' generates a new space after each line of cldoe
        # printing each line

    opened_file.close()
    # IMPORTANT - to close the file in order to save the file

 except FileNotFoundError:
   print(" File can't be found!")
   raise
print(open_and_print_file("order.text"))

# Let's take it even further
# with statement and finnally

def open_and_print_file(file):
 try:
    with open(file, 'r') as file:
    # with open gives a same functionality as open file but more efficent
      file_data = file.readline()
      for line in file_data:
        print(line) # '\n' generates a new space after each line of cldoe
 except FileNotFoundError:
   print(" File can't be found!")
   raise
 finally:
     print("\n Execution complete")

print(open_and_print_file("order.text"))
#
def open_using_with_and_print(file):
    try:
        with open(file, "r") as file:
            for line in file.readlines():
                print(line.rstrip('\n'))
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise
    finally:
        return "\nExecution complete"


print(open_using_with_and_print("order.text"))

# task- research how  to write to this file to add more items
# read from the file
# solution:
def write_to_file(file, order_item):
    try:
        with open(file, "w") as file:
            file.write(order_item + '\n')
    except FileNotFoundError:
        print("file cannot be found or directory is incorrect, please check the details provided")
        raise
    finally:
        return order_item + " is added"
print(write_to_file("order.text", "biryani"))

#print(open_using_with_and_print("order.text"))

# Summary
# You just:
#
# working with files
# understand errors and exceptions
# handling errors and exceptions
# using try and except blocks
# opening files and accessing data using readlines
# using with as best practice
# using finally as a clean up function
# writing to files