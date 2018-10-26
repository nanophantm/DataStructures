from array import *

# Arrays

array1 = array('i', [10,20,30,40,50,40])

array1.insert(1,60)

# Notice that .remove() removes the first occurance of the value
# not the value at a particular index.
array1.remove(40)

for x in array1:
    print(x, end=' ')

# The following is a way of performing a search on an array
# it returns the last index at which the value appears.
# Notice that 40 is at index 3 and 5 -- the following returns 5.
print('\n')
print(array1.index(40))

# The following is just updating the value at a given index.
# This is just overwriting.
array1[2] = 80
for x in array1:
    print(x, end=' ')

# Just printing values at a specific index in the array.
print('\n')
print(array1[0])
print(array1[2])
