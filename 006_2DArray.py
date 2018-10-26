from array import *
'''
Two Dimensional arrays are arrays within arrays. It represents a table
with rows and columns of data.

Day 1 - 11 12 5 2 
Day 2 - 15 6 10 
Day 3 - 10 8 12 5 
Day 4 - 12 15 8 6 
'''
# Notice the way this is constructed
# 4 brackets within 1 bracket
T = [[11, 12, 5, 2], [15, 6, 10], [10, 8, 12, 5], [12,15,8,6]]

# Will print [11,12,5,2]
print(T[0])

# Will print 10
print(T[1][2])

# To print out the entire array
'''
for r in T
    -- These are your main arrays [[0],[1],[2],[3]]
    for c in r
        -- These are your values in your main arrays
    print()
'''
for r in T:
    for c in r:
        print(c,end=' ')
    print() # just prints a new line after each main array

print('\n')

# To update the array
# This will insert a new array into position 2
T.insert(2, [0,5,11,13,6])
for r in T:
    for c in r:
        print(c,end=' ')
    print()

print('\n')

# To delete a main array
# This deletes the last main array
del T[4] 
for r in T:
    for c in r:
        print(c,end=' ')
    print()