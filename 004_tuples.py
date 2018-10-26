'''
Tuples are similar to lists except tuples cannot be changed and tuples use parenthesis.

Notes:
Empty tuple         : tup1 = ()
Single value tuble  : tup1 = (50,) -- must contain the comma

'''
tup1 = ('physics','chemistry',1997,2000)
tup2 = (1,2,3,4,5)
tup3 = ('a','b','c','d')

# Accessing values in a tuple is the same as arrays
print("tup1[0]: ", tup1[0])
#  Print indices 1 - 5
print("tup2[1:5]: ", tup2[1:5])

# Creating new tuples from existing tuples
tup4 = (12, 34.56) 
tup5 = ('abc', 'xyz')
tup9 = tup4 + tup5
print(tup9)