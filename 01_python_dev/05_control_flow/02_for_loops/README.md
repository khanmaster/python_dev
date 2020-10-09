# For loops

## Timings

20 - 30 Mins

## This lesson includes

* Types of looping
* Creating a for loop
* nested for loops
* Loops and if statements

most work within coding and data is looping through a list of details and making a decision, change or action against those values.

## Types of looping
In many languages there are a couple of loop structure types, the most common being a `for` loop where you define an iterator number and cycle through and a `foreach` which merely steps through each member of a list or dictionary.

Python being as wonderful as it is does away with all the different types and simply uses `for` in the context of 'for each item in this object' and that's it. 

## Creating a for loop

create a file as below and we will step through a loop:

```python

list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}


for num in list_data:
    print(num * 2)
```

* `for num in list_data:` - here we initialise the for loop with the keyword `for` then we use a variable named `num` to represent each iteration of the loop. It's important to note that the variable name of the loop can be called anything but make sure it is representative of the data that is being handled for readability purposes. Next we're using the keyword `in` that directs the following option which must be the collection we want to work with in this instance it's our `list_data`
    * `print(num * 2)` - all we are asking here is for the print statement to take our iterable value of `num` and times it by 2
    
When running our file we are getting 2,4,6,8,10. so, through each pass of the loop we have grabbed the number and provided an action against it.

***note to trainer*** - use the IDE debugger to step through and visually see how the loop is iterating.

## nested for loops

### nested lists
there are instances where we can have nested lists which need to be handled. Input the following code and we will step through:

```python
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

# for num in list_data:
#     print(num * 2)

for data in embedded_lists:
    print(data)
```

* `for data in embedded_lists:` our for loop is being created and our variable referenced as `data` and our collection as `embedded_lists`.

and we're merely printing our data which should return:

```text
[1, 2, 3]
[4, 5, 6]
``` 
this is fine but we need to access the data within the lists which is where our embedded loops come in:

```python
list_data = [1, 2, 3, 4, 5]
embedded_lists = [[1,2,3],[4,5,6]]
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}


# for num in list_data:
#     print(num * 2)

for data in embedded_lists:
    print(data)
    for num in data:
        print(num)
```
which should now return:

```text
[1, 2, 3]
1
2
3
[4, 5, 6]
4
5
6
```

feel free to comment out the print statement in the `data` loop, the first for loop, to receive the plain lit of numbers.

### loops for dictionaries

dictionaries will be another common loop that will likely require a nested loop to handle the data within them.

input the below code alongside the `dict_data` and we will step through the code:

```python
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

for value in dict_data:
    print(value)
```

```text
1
2
3
```
however, you can use a lot fo the methods available to the dictionary object to make  parsing of the object easier. As you can see in our dictionary the keys relate to another dictionary within it. So, we can use the `value()` method to return all of the values:

```python
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

for item in dict_data.values():
    print(item)
```

will return:

```text
{'name': 'Bronson', 'money': '$0.05'}
{'name': 'Masha', 'money': '$3.66'}
{'name': 'Roscoe', 'money': '$1.14'}
```

Now we can generate an embedded for loop to review either the keys or values within the dictionary:

```python
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

for item in dict_data.values():
    for embed_value in item.values():
        print(embed_value)
```

will return:

```text
Bronson
$0.05
Masha
$3.66
Roscoe
$1.14
```

if we needed a loop that only needs to return the money responses we can call the key directly as part of the loop"

```python
dict_data = {1: {"name": "Bronson", "money": "$0.05"}, 2: {"name": "Masha", "money": "$3.66"}, 3: {"name": "Roscoe", "money": "$1.14"}}

for items in dict_data.values():
    print(items['money'])
```

There are many many ways to access and utilise dict data within loops and many more can be reviewed in the python documentation. 

## Loops and if statements

It is when loops and if statements come together where the real control of code comes into play. the loops manage the accessing of the data and the if statements manage the logic. We will only go through a brief example as these concepts will be utilised consistently throughout the whole course.

```python
list_data = [1, 2, 3, 4, 5]

for num in list_data:
    if num == 3:
        print('I found three')
    elif num > 3:
        print('gone too far')
    else:
        print("too soon")

```

The code above and the running of it should be relatively self explanatory.

## Summary

Mixing loops and if statements is pretty much what makes a developer. We will see how much of development as a whole hangs on the concepts of handling data types, within collections and that need to be parsed upon and decisions made.


You just:
* Types of looping
* Creating a for loop
* nested for loops
* Loops and if statements