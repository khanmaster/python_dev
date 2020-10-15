# Building useful JSON objects

## Timings

10 - 15 Mins

## This lesson includes

* Why build JSON readers into an object?
* Building a class around JSON


This will be a very short lesson around building useful class data objects around JSON 

## Why build JSON readers into an object?

JSON is a data structure much like any other and would have been constructed and documented. Therefore as an object we want to be able to deserialise the JSON and access the data and we can use a class to do that efficiently.

***Trainer note*** provide the students with the exchange_rates.json.

In this instance we will be using a JSON file with exchange rates and build our class around it. you will see from the exchange rates file that we will be accessing these data points as you would in a dictionary.

## Building a class around JSON

Let's dive straight in the code:

```python
import json

class RatesParser:

    def __init__(self, rates_file):
        rates_info = self._open_json_file(rates_file)
        self.base = rates_info['base']
        self.date = rates_info['date']
        self.rates = rates_info['rates']
        self.aud = self.rates['AUD']
        self.gbp = self.rates['GBP']

    def _open_json_file(self, file):
        with open(file) as rates:
            return json.load(rates)
```

The `_open_json_file` method is private because we want to create a method that will open the file and return the rates as a parsed JSON object using within our initialising of the class.

The key areas to note in the `__init__` areas is:

* `rates_info = self._open_json_file(rates_file)` here we are calling our private method to parse the file and we are storing the returned parse JSON object and holding it within the `rates_info variable

the rest of the details are nothing more than accessing the dictionary items and returning them the only area to highlight is that to access the embedded rates as they are a dictionary within a dictionary.

```python
self.rates = rates_info['rates']
self.aud = self.rates['AUD']
self.gbp = self.rates['GBP']
```
    
If we now run the below code:

```python
import json

class RatesParser:

    def __init__(self, rates_file):
        rates_info = self._open_json_file(rates_file)
        self.base = rates_info['base']
        self.date = rates_info['date']
        self.rates = rates_info['rates']
        self.aud = self.rates['AUD']
        self.gbp = self.rates['GBP']

    def _open_json_file(self, file):
        with open(file) as rates:
            return json.load(rates)


rate_reader = RatesParser("exchange_rates.json")

print(rate_reader.gbp)
print(rate_reader.rates)
```

We should return the GBP value and all of our rates!

```text
0.89275
{'AUD': 1.4717, 'BGN': 1.9558......
```

## Summary

This is would be considered a good practice as we have mapped the JSON file into a useful object that can receive a file and make all the data points avialable in a clean and efficient manner.

You just:
* why build JSON readers into an object?
* Building a class around JSON