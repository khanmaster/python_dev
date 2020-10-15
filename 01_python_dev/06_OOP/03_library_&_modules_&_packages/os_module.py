# Module is a piece of software that delivers a piece of functionality
import os
import math, datetime, sys
# let's create a variable to store the working dir location using os.getcwd()
working_dir = os.getcwd()
print(working_dir)
# output should be your current dir destination

# let's create a method that returns user id
# def return_user_id():
#     print(os.uname())
# # # os.uname works in Linux
# return_user_id()




def operating_system_information():
    print(os.cpu_count())

print(datetime.date.today())
# gives us today's date

print((sys.path))
# gives us the current path

print(math.remainder(1, 5))
#print(return_user_id())

print(operating_system_information())
# total CPU available in the system