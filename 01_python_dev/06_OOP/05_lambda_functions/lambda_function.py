# Lambda are just another name for function
# can be very powerful and useful but it is important to understand how they fit in

# Lambda is anonymous functions and can take multiple parameters but return only one expression

# Example

def add(value1, value2):
    return value1 + value2

addition = lambda value1, value2: value1 + value2

# adding values of the add method
print(print(add(2, 2)))

# using lambda
print(addition(2, 2))
# so far not very clear

# so where can it be the best utilised
saving = [234.00, 555.00, 674.00, 78.00]

bonus = []
for account_balance in saving:
    bonus.append(account_balance * 1.1)
    print(account_balance)

# bonus = list(map(lambda x: x * 1.1, saving))
#using lambda
#print(bonus)

# using Lambda is very clearn and much more efficient
