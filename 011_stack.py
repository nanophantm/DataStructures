'''
3:42
Memory is allocated one over another in a stack.
In a stack you can only add or remove elements from the top of the stack.

In a stack the element inserted last in the sequence will come out first as we can remove
only from the top of the stack.

Last In First Out.

Adding an element is called PUSHing
Removing an element is called POPing
'''

class Stack:
    def __init__(self):
        self.stack = []
    
    def add(self, dataval):
        # Using the list append method to add an element
        # This functionality doesnt allow you to add a duplicate value to the top of the stack
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
    
    # Use peek to look at the top of the stack
    def peek(self):
        return self.stack[0]
    
    def view_stack(self):
        for x in self.stack:
            print(x)

    # Remember a stack removes from the bottom first so this will remove
    # the last entry in the stack (LIFO)
    def remove(self):
        # Test to make sure the stack isnt empty
        if len(self.stack) <= 0:
            return("No element in stack")
        else:
            return self.stack.pop()

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.add("Wed")
AStack.add("Thur")
# Only going to show you whats on top as the elements are being added
# one on top of each other.
print(AStack.peek())
print("\n")
AStack.view_stack()

# Testing adding a duplicate value
# Prints the same as before -- no dupe
AStack.add("Mon")
print("\n")
AStack.view_stack()

print("\n")
AStack.remove()
AStack.view_stack()