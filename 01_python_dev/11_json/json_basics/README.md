# JSON basics

## Timings

20 - 30 Mins

## This lesson includes

* JSON encoding from a dictionary 
* Encoding and writing a json file 
* Decoding JSON into a dictionary

We will be looking how we use the json package in python to create and decode json all details regarding JSON management in python can be found [here](https://docs.python.org/3/library/json.html)

## JSON encoding from a dictionary and writing to a file

We would have already seen that JSON work with key value pairs and follow the same principles as a dictionary in terms of their construction and keu, value pairs.

create a file called `json_basics.py` and let's create a dictionary:

```python
car_data = {"name": "tesla", "engine": "electric"} 
```

Now we have our dictionary of data we we set up the json import and look into the methods available to encode our dictionary to a JSON object:

```python
import json


# encoding
car_data = {"name": "tesla", "engine": "electric"} # dictonary

print(type(car_data))
```
We have imported our JSON library and have put a quick type check on our dictionary and the response should be `<class 'dict'>`

Here we are going to be looking into 2 methods `json.dump()` and `json.dumps()`.

* `json.dumps()` - Serialises json to a formatted string
* `json.dump()` - creates a stream object and expects a file object to write to

Let's take a look at `json.dumps()` first:

```python
car_data = {"name": "tesla", "engine": "electric"}

car_data_json_string = json.dumps(car_data)

print(car_data_json_string)
```
should return:

`{"name": "tesla", "engine": "electric"}` - but this looks no different than our dictionary....?

this is where you want to check the type `print(type(car_data_json_string))` which should return `<class 'str'>`. So, our `json.dumps()` object has changed our dictionary object into that of a string which all JSON objects are in essence a string in pretty much all coding languages.

 Now let's take a look at `json.dump()`, as this is the function you will need to use to create a JSON file from various data sources:
 
 ```python
car_data = {"name": "tesla", "engine": "electric"}

with open('new_json_file.json', 'w') as jsonfile:
    json.dump(car_data, jsonfile)
```
 
 * `with open('new_json_file.json', 'w') as jsonfile:` we are using the with statement we have used many times before to manage our file, we are also providing the name of the file and the file method we wish to use which is `w` meaning write. We want to be able to overwrite the file if any changes are made so write is the best option.
    * `json.dump(car_data, jsonfile)` here we are using the `json.dump()` which stakes two arguments. The first argument is the dictionary that needs to transformed into JSON and the second being the file_type object to be written to which in this case is our `new_json_file.json` file.

If we run our module it should product our file with the contents of our dictionary with the below contents.

```json
{"name": "tesla", "engine": "electric"}
```

## JSON Decoding / reading json

The reading of JSON is very simple and we will need to use the methods `json.load()` let's use the file we have just created and now read the information back in:

```python
with open("new_json_file.json") as jsonfile:
    car = json.load(jsonfile)
    print(type(car))
    print(car['name'])
    print(car['engine'])
```
If you run the code above you should see:

```text
<class 'dict'>
tesla
electric
```

you can see that the information has now been set back to a dictionary and we can access the details as we would any other dictionary.

## Third subheading

## Summary

You just:
* JSON encoding from a dictionary 
* Encoding and writing a json file 
* Decoding JSON into a dictionary 