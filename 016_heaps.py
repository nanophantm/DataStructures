'''
Heap is a special tree structure in which each parent node is less than or equal to
its child node. This is called a min heap.

If each parent node is greater than or equal to its child node. This is called a max heap.

Heaps are very useful when implementing a queue where the item with a higher weightage is
given more priority in processing.

Its a special case of balanced binary tree where the root node is compared with its children
and arranged accordingly.

Python has a built in library named heapq. This library has the relevant functions to 
carry out various operations on heap data structures.

Use heaps whever you need quick access to the largest or smallest item (using min or max heaps),
because that item will always be the first element in the array or at the root of tree. Insertions
in a heap are fast so its a good way to deal with incoming events or data and always have access
to the earliest/biggest.
'''
import heapq

H = [21,1,45,78,5,27]
# Use heapify to rearrange the elements. The smallest elements gets pushed to the
# index position. But the rest of the data elements are randomly sorted.
heapq.heapify(H)

# Add element to the heap, will automaticaly at an element that is < the existing root
# element to the root if it is smaller.
heapq.heappush(H,8)
print(H)

# Removing from the heap. This removes the element at the first index.
# 5 will become the root node.
heapq.heappop(H)
print(H)

# Turn the min heap into a max heap
heapq._heapify_max(H)
print(H)