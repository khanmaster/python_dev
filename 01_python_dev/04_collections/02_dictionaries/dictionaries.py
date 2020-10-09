# # What is Dictionaries
# # How can we manage dictionaries
#
# # Dictionary: is another way to manage data but more DYNAMIC than other data types
# # use_cases: Very useful tool within any coding language and work on a very simple KEY VALUE pairs
# # Key: the reference of the object
# # value: whatever the data storage mechanism you wish to use i.e data type, list, another dictionary
# # Syntax: we use curly "{}" brackets to create a dictionary
#
# # Let's create a dictionary to store student data
#
devops_student_1 = {
    "key": "value",
    "name": "james",
    "stream": "tech",
    "completed_lesson": 4,
    "completed_lesson_names": ["variables", "data types", "lists"]
}
# # Here we have created a data structure using keys of name, stream, of which contain strings, int and a list
# # How can we access data using the key?
# # To access data within a dictionary we need to use the key to access data stored as a value of that key
#
# # Let's print out dictionary
# print(devops_student_1)
#
# # How can I get name of devops_student_1?
# print(devops_student_1["name"])
#
# # Let's access an element within the list stored under completed_lessons_names
# print(devops_student_1["completed_lesson_names"][0])
# # here we have to the list and then pass the reference/index of the list
#
# # How can I change the value in my dictionary?
# # What's the total number of our completed lesson = 4 let's change it to 3
# devops_student_1["completed_lesson"] = 3
# # let's verify it
# print(devops_student_1["completed_lesson"])
#
# # What if we wanted to remove an item "data types"
# devops_student_1["completed_lesson_names"].remove("data types")
# print(devops_student_1["completed_lesson_names"])

# Moving onto Dictionary Methods
# There are several methods associated with Dictionary and we will briefly touch base on some important ones
# How can I find out only keys of our dictionary
# keys() is used
print(devops_student_1.keys())

# values()
print(devops_student_1.values())

# closing notes for the students
# Spend some time creating your own dictionary example and sample some of the available methods, use online resources if necessary to help understand what is possible.
#
# Summary
# You just:
#
# What is a Dictionary
# Managing Dictionaries