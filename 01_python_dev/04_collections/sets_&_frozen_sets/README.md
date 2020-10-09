# Sets and frozen sets

## Timings

15 - 20 Mins

## This lesson includes

* sets and frozen sets
* set methods

This lesson will be relatively short as there are a lot of similarities between lists and sets.

the key areas to take into account in a set is that they're unordered and unindexed.

## Sets and Frozen Sets

to create a set you use curly brackets but treat it like a list rather than a dictionary:

```python
car_parts = {"wheels", "doors", "exhaust"}
print(car_parts)
```
which should yield `{'exhaust', 'doors', 'wheels'}`


To access elements in the list you will need to loop through the values and manage actions against them.

You can use the `add()` method on the set to add more details:

```python
car_parts.add("windows")
print(car_parts)
```

which should yield `{'windows', 'exhaust', 'doors', 'wheels'}`

and lastly you can remove with the `discard()` method:

```python
car_parts.discard("doors")
print(car_parts)
```

### Frozen sets
Frozen sets are merely immutable versions of the set list similar to a tuple although are not ordered or indexed. it will be relatively rare to use a frozen set without clear reasons for its use. 

```python
x = frozenset([1, 2, 3, 4])
```


## Summary

We have learned:
* sets and frozen sets
* set methods
