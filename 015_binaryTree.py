'''
3:05
Binary Tree

Tree represents the nodes connected by edges. It is a non-linear data structure.

    -- One node is marked as root
    -- Every node other than root is associated with one parent node
    -- Each node can have an arbitrary number of child nodes
5:01
'''
class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self, data):
        # compate the new value with the parent node
        if self.data:
            # less than is because we are inserting numeric values, so the
            # lesser values go to the left node.
            if data < self.data:
                # if the left node doesnt exist create it
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            # greater than is because are inserting numeric values, so the
            # greater values go to the right node.
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        # if the value already exist in the tree skip over this value            
        else:
            self.data = data
    
    # Find values in nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+ " Not found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')


    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

root = Node(10)
root.insert(6)
root.insert(14)
root.insert(3)
root.insert(20)
root.print_tree()

root.findval(10)
print(root.findval(22))
