import requests

url = 'http://api.postcodes.io/postcodes/'
postcode = 'e147le'
# postcode = input("please enter your postcode ")

url_arg = url + postcode
print(url_arg)

# make request and capture response
response = requests.get(url_arg)

# print(response)

# print(type(response))
# how can we parse the data
# print(response.json())

# let's store this data into a variable so we can iterate through it
response_dic = response.json()
print(type(response_dic))

# now we know the type is dic and we also know how to iterate through it and get keys
result_dic = response_dic['result']
print(result_dic)

# how can get the keys and a specific value of any key
for keys in result_dic.keys():
    print(keys)#,'the value inside is ', result_dic[keys])

# How can we the longitude of our postcodd
    if keys == 'longitude':
        print('longitude is ' + str(result_dic['longitude']))

# How can we the latitude of our postcodd
    if keys == 'latitude':
        print('latitude is ' + str(result_dic['latitude']))

# How can we the postcode of
    elif keys == 'postcode':
        print('postcode is ' + str(result_dic['postcode']))
