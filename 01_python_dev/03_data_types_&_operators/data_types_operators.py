# Ints

a = 24
b = 16
print(a+b)
print(a>b)
print(a<b)
# These are base usage but will be the most common
# Uncomment / use the below for step by step examples

# print(a + b)  # should yield 40 to the command line
# print(a > b)  # should yield true
# print(a < b)  # should yield false

# Floating point numbers / Floats

# Floating point numbers or simply float/s are real numbers that use the decimal point to split the number.


FloatNum = 1.356

# print(type(FloatNum))

# You are able to add floats to Ints

IntNum = 4

# print(FloatNum + IntNum)

# It's important to note that, as with fractions, there could be no limit to the but python does round things up

One_third = 1 / 3

print(One_third)
print(One_third * 3)

# It is possible to deal with larger fractional numbers but for this level of coding it will be enough

# Long numbers

"""
We have already discussed that Python is an interpreted language and Longs are essentially a big num implementation.
In older versions of Python (approx pre v3.0) the L was a supported offering but this is now no longer the case.
Int numbers are no unbounded and have no limit.
In fact if you use the below example it's very hard to get a Long number as most are managed by int!!!!
"""


# c = 900000000001234567823456781234567892345678235456758677643534612345678902345678923456789021345678902314567875432145678907654324567890876574635243435465768798090908976857465436576879809090897
# d = 976435235467876987097867564567897865746354214354657687987687546352465768798786734534765877543214563456787654345678765434567876543456787654345676544567654345654345654345654345654565434567888
#
# print(type(c * d))
