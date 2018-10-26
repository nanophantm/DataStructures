'''
3:42

A double queue is the same as a queue except that you can manipulate both ends of the
data structure.

Python has a built in double queue implementation in the collections library
'''
import collections
DE = collections.deque(["Mon","Tue","Wed"])
print(DE)

print("Add to the right")
DE.append("Thu")
print(DE)

print("Adding to the left")
DE.appendleft("Sun")
print(DE)

print("Removing from the right")
DE.pop()
print(DE)

print("Removing from the left")
DE.popleft()
print(DE)

print("Reversing the double queue")
DE.reverse()
print(DE)