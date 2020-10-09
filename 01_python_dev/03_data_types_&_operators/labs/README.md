# There are many ways to deal with this as long as they details are being captured it is not a problem.

```python
print("Hi, what is your name?")
name = input() # String

print("What is your age?")
age = int(input()) # now casted to an int

print("and your date of birth")
dob = input() # string

print("please input your address")
print("Let's start with the house number")
house_num = int(input())

print("First line of address")
addr_first_line = input()

print("Second line of address")
addr_second_line = input()

print("postcode")
postcode = input()

print("Thanks for inputting the below details")
print("Your name is " + name + " and your age is" + " " + str(age))
print("Your address is:")
print(str(house_num))
print(addr_first_line)
print(addr_second_line)
print(postcode)
```
