'''
1:45
A linked list is a series of data elements, which are connected together via links.

Each data element contains a connection to another data element in the form
of a pointer.

Nodes are Python's version of pointers. 
    -- Remember a pointer is an object that stores the memory address of another value located
       in the computer's memory.

Nodes are the foundations on which various other data structures such as linked list and tress
can be handled in python.

3:42
'''


class daynames:
    """
        Nodes are created by implementing a class which will hold the pointers
        along with the data element.

        nextval is your pointer, and is initiaized to null and three nodes are initialized
        with values.
    """
    def __init__(self, dataval=None):
        self.dataval = dataval
        # pointer
        self.nextval = None

# nodes
e1 = daynames('Mon')
e2 = daynames('Tue')
e3 = daynames('Wed')
e4 = daynames('Thur')

e1.nextval = e2
e2.nextval = e3
e3.nextval = e4
# e4.nextval = e1

thisvalue = e1

# This value will remain true until you reach the end of the linked list
# this.value.nextval - notice that e4 does not have a next value.
# If you were to set e4.nextval = e1 the loop would be infinite.
while thisvalue:
    print(thisvalue.dataval)
    thisvalue = thisvalue.nextval

print('\n')

class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    """
        This defines your root node
    """
    def __init__(self):
        self.headval = None
    
    """
        Methods defined for linked list functionality
    """
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval
    
    """
        Inserting at the beginning of a linked list involves pointing the next pointer of the new
        data node to the current head of the linked list.
            -- Current head becomes the second data element
            -- New node becomes the head
    """
    def AtBeginning(self, newdata):
        NewNode = Node(newdata)

        # The current head becomes the next value for the new head.
        # The new node becomes the nead.
        NewNode.nextval = self.headval
        self.headval = NewNode
    
    def AtEnd(self, newdata):
        # Create the new node to insert at the end of the list
        NewNode = Node(newdata)
        # Assign the last value to headval
        last = self.headval
        # Loops through the "last" node until it reaches the end of the list
        while(last.nextval):
            last = last.nextval
        # Now that the last node is at the end of the list assign it the value of NewNode
        last.nextval=NewNode
    
    def Inbetween(self, middle_node, newdata):
        # Create the new node to insert before a particular node
        NewNode = Node(newdata)
        # Make the next value of the new node equal to next value of the supplied node
        NewNode.nextval = middle_node.nextval
        # Set the value of the supplied node to the new node
        middle_node.nextval = NewNode
    
    """
        Removing an existing node is done by using the key for that node. 
            -- Locate the previous node of the node which is to be deleted
            -- Point the next pointer of this node to the next node of the node
               to be deleted
    """
    def RemoveNode(self, RemoveKey):
        # Assign headval to the head
        HeadVal = self.headval

        # Loop through Headval while its not none
        while (HeadVal is not None):
            # If headval is equal to the RemoveKey argument break out
            if HeadVal.dataval == RemoveKey:
                break
            # Set prev to the value of HeadVal
            prev = HeadVal
            # Move HeadVal to the next pointer
            HeadVal = HeadVal.nextval
        
        # If the next pointer is None then return
        if HeadVal == None:
            return
        
        # HeadVal is now equal to the RemoveKey
        # prev is set to the value before Remove key
        # Set it equal to the value after the original Headval 
        prev.nextval = HeadVal.nextval

        # Set HeadVal to none -- this is what removes the actual entry from the list
        HeadVal = None


list1 = SLinkedList()
# Notice the linking back to the Node class here
list1.headval = Node("Mon")

e02 = Node("Tue")
e03 = Node("Wed")

# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e02.nextval = e3

# Insert a new head node
list1.AtBeginning("Sun")

# Insert a new last node
list1.AtEnd("Sat")

# Insert a node before a node in the list
list1.Inbetween(list1.headval.nextval,"New day")

list1.RemoveNode("New day")

list1.listprint()