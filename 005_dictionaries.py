'''
Dictionaries have the following structure
{'Key1': 'Value1','Key2': 'Value2','Key3': 'Value3'}

Keys must be of an immutable data type such as strings, numbers or even tuples.
'''
dict1 = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# Print the value associated with the keys
print(dict1['Name'])
print(dict1['Age'])


# Updating is done like lists, arrays, or tuples except you use the key
# instead of the index number
dict1['Age'] = 8 # update existing entry
dict1['School'] = "DPS School" # Add new entry

print ("dict['Age']: ", dict1['Age'])
print ("dict['School']: ", dict1['School'])

# Deleting elements
del dict1['Name'] # remove Key 'Name' and its 'Value'
print(dict1)
dict1.clear() # Remove all entries in dict
print(dict1)