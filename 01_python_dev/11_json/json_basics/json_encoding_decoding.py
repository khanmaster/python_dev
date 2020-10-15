import json

# lets create a varialbel with some key value data
car_data = {"name": "tesla", "engine": "electric"}

print(type(car_data))
# type dictionary

# Let's check some json methods
# json.dumps() serialises jso to formatted string
# json dump() creates a stream objet and expects a file object to write

# first json.dumps()
car_data_json_string = json.dumps(car_data)
print(car_data_json_string)
# looks no different to as we declared..?

print(type(car_data_json_string))
# so it confirms that json.dumps has changed our dictonary to string

# moving onto json.dump() which takes 2 arguments
# json encoding from dictionary and wiriting to a file
with open("json_file.json", 'w') as jsonfile:
    json.dump(car_data, jsonfile)

# Json Decoding reading from a file is very simple

with open("json_file.json") as jsonfile:
     car = json.load(jsonfile)
     # reading and storing json file

     print(type(car))
     # type chanded back to dict

     print(car['name'])
     # getting value of name

     print(car['engine'])
     # getting value of engine

JSON encoding from a dictionary
Encoding and writing a json file
Decoding JSON into a dictionary