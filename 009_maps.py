'''
Maps or ChainMaps are data structures that are used to manage multiple dictionaries
together as one unit.

The combined dictionary contains key and value pairs in a specific sequence eliminating
any duplicate keys.

The best use of ChainMap is to search through multiple dictionaries at a time and get the 
proper key-value pair mapping. 

Note : ChainMaps behave as stack data structures
       When outputting the keys and values they are not sorted
'''
import collections

dict1 = {'day1':'mon','day2':'tue'}
dict2 = {'day3':'wed','day1':'thur'}

res = collections.ChainMap(dict1, dict2)

# creating a single dictionary
#   -- all this does is combine the two dictionaries into a single dictionary
print(res.maps,'\n')

# identifies the keys that exist in both lists
print('Keys = {}'.format(list(res.keys())))
# identifies the values that exist in both lists
print('Values = {}'.format(list(res.values())))
print()

# print all the elements shared in the dictionaries
print('elements:')
for key, val in res.items():
    print('{} = {}'.format(key, val))
print()

# search for a specific value in the result
print('day3 in res: {}'.format(('day1' in res)))
print('day4 in res: {}'.format(('day4' in res)))