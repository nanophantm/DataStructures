'''
Lists are similar to arrays except they can contain different data types and in
python have different methods.

List operations

Python Expression 	            Results 	                    Description
len([1, 2, 3]) 	                3 	                            Length

[1, 2, 3] + [4, 5, 6] 	        [1, 2, 3, 4, 5, 6] 	            Concatenation

['Hi!'] * 4 	                ['Hi!', 'Hi!', 'Hi!', 'Hi!'] 	Repetition

3 in [1, 2, 3] 	                True 	                        Membership

for x in [1, 2, 3]: print x, 	1 2 3 	                        Iteration

'''
list1 = ['physics','chemistry',1997,2000]
list2 = [1,2,3,4,5]
list3 = ['a','b','c','d']

# Accessing values in a list is the same as arrays
print("list1[0]: ", list1[0])
#  Print indices 1 - 5
print("list2[1:5]: ", list2[1:5])

# Updading values in a list is the same as arrays
list1[2] = 2001
print(list1[2])

# There are two ways to remove elements from a list
#   1. If you know which element(s) you are deleting use del
#   2. If not use remove()
print(list1)
del list1[2]
print(list1)