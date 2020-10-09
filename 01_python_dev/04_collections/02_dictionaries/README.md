# Dictionaries

## Timings

20 - 40 Mins

## This lesson includes

* What is a Dictionary
* Managing Dictionaries

Dictionaries are another way to manage data but can be a little more dynamic in their uses as you will see as we investigate.

## What is a Dictionary in Python

Dictionaries are a very useful tool within any coding language and work on a very simple of key and value pairs.

* key = the reference of the object
* value = whatever the data storage mechanism you wish to use i.e. data type, list, another dictionary

Dictionaries are extremely wide and varied in their utilisation.

### Creating a dictionary

Dictionaries are structured as below:

```python
student_1 = {
    "name": "susan",
    "stream": "tech",
    "completed_lesxfssons": 4,
    "completed_lesson_names": ["variables", "data_types", "set up"]
}
```
As you can see we've created a data structure using the keys of name, stream, completed_lessons & completed_lesson_names. Of which contain strings, ints and a list.

### Accessing data using the key

To access data within a dictionary you need to use the key to access the data:

```python
print(student_1["stream"])
```
The above statement when printed should yield "tech"

However, let's say we want to access and an element within the list stored under `completed_lesson_names`?:

```python
print(student_1["completed_lesson_names"][0])
```
we need to access the list and then pass the reference of the list you wish to access.

### Changing a value

Let's take a look into the number of lessons completed an it states 4 however we've only captured 3. Let's change that value:

```python
student_1["completed_lessons"] = 3
print(student_1["completed_lessons"])
```
We should now see 3 lessons being printed.

If we wanted to change the value in a list we would need to treat things in exactly the same way, but we should be able to access methods relating to the lists:

```python
student_1["completed_lesson_names"].remove("data_types")
print(student_1["completed_lesson_names"])
```
The above should yield the list of `['variables', 'set up']` and we have used the lists remove method to do so.

## Dictionary Methods

Much like all types in Python there will be methods associated to their type so let's take a look at those available in Dictionaries.

### Getting keys

The `keys()` method is extremely useful to bring back and look through all of the keys available:

```python
print(student_1.keys())
```

the above should return `dict_keys(['name', 'stream', 'completed_lessons', 'completed_lesson_names'])`

The dict_keys type has a list within it which could be looped through and we will be looking at loops very soon. Which should yield:

`dict_items([('name', 'susan'), ('stream', 'tech'), ('completed_lessons', 4), ('completed_lesson_names', ['variables', 'set up'])])` 

As you can see the type is `dict_items` and contains an array of tuples for you to use.


# closing notes for the students

Spend some time creating your own dictionary example and sample some of the available methods, use online resources if necessary to help understand what is possible.

## Summary

You just:
* What is a Dictionary
* Managing Dictionaries