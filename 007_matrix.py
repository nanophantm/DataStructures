'''
3:27

A Matrix is a special case of two dimensional array where each data element is of 
strictly the same size. So every matrix is also a two dimensional array nut not vice
versa.

Matrices are important in mathematical and scientific calculations.


'''
# numpy is being used for matrix manipulation
from numpy import *

'''
Recording temperature for 1 week measured in the morning, mid-day, evening,
and mid-night. This is represented as a 7x5 matrix.

7 -- days in the week
5 -- the number of records in a day
'''
a = array([['Monday', 18,20,22,17],['Tue', 11,18,21,18],
            ['Wed', 15,21,20,19], ['Thu', 11,20,22,21],
            ['Fri', 18,17,23,22],['Sat', 12,22,20,18],
            ['Sun', 13,15,19,16]])

# reshape defines the structure in columns and rows of your data
# this give us 7 rows and 5 columns.         
m = reshape(a,(7,5))
print(m)

# accessing data in a matrix is the same as accessing it in a 2 dimensional array
# access the full contents of Wednesday
print(m[2])
# access the third entry on friday (remember the first entry is the name of the day)
print("Day: ", m[4][0], "Temp: ", m[4][3])

'''
Adding rows and columns
'''
# adding a row (append)
a_r = append(a, [['Avg', 12,15,13,11]],0)
print(a_r)

# adding a column (insert)
# (a) = name of the array we are inserting the column into
# ([5]) = the index of the column we wil be adding -- currently the array has 4 columns
# ([],[],[]...) = the values that will be going into the column
a_c = insert(a, [5],[[1],[2],[3],[4],[5],[6],[7]],1)
print(a_c)

# delete a row
# this will remove wednesday from the matrix
a_c = delete(a_c,[2],0)
print(a_c)

# delete a column
# this will remove the third column from the matrix
a_c = delete(a_c,[2],1)
print(a_c)