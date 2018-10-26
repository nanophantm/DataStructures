'''
3:27

Mathematically, sets are collections of items in no particular order.
Python sets have the following attributes

    - The elements in the set cannot be duplicates
    - The elements in the set are immutable but the set as a whole is mutable
    - There is no index attached to any element in a python set. So they do not
      support any indexing or slicing operation

Sets in python are typically used for mathematical operations like union, intersection,
difference, and complement etc. 
'''
Days = set(["mon","tue",'wed','thur','fri','sat','sun'])
Months = {"Jan","Feb","Mar"}
Dates = {21,22,17}
print(Days)
print(Months)
print(Dates)

# Individual elements of sets cannot be accessed, you can access all
# elements of a set through looping
for d in Days:
    print(d)

'''
Union
    -- Produces a new set containing all the distinct elements from both the sets
'''
# wednesday exists in both sets but only one wednesday appears in the final set
# because wednesday is the shared value
DaysA = set(["mon","tue",'wed'])
DaysB = set(['wed','thur','fri','sat','sun'])
AllDays = DaysA|DaysB
print(AllDays)

'''
Intersection
    -- Produces a new set containing only the common elements from both the sets.
'''
# The following will produce a set containing only wednesday as its the only 
# matching element in both sets.
SameDays = DaysA & DaysB
print(SameDays)

'''
Difference
    -- Produces a new set containing only the unique elements in the first set.
'''
# The following will produce tuesday and monday since the other days appear in the
# second set.
DiffDays = DaysA - DaysB
print(DiffDays)

'''
Compare
    -- Check if a set set is a subset or superset of another set.
       Produces true or false
'''
# The following will produce false, as the sets only have on common element
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SupersetRes)
print(SubsetRes)

DaysC = set(['mon','tue','wed','thur','fri','sat','sun'])
DaysD = set(['wed','thur','fri','sat','sun'])
# days c is a super set of days d
SubsetResA = DaysC >= DaysD
# days d is a sub set of days c
SupersetResB = DaysD <= DaysC
print(SubsetResA)
print(SupersetResB)