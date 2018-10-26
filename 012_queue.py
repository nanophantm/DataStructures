'''
3:42

A queue data structure is similar to a stack except that it is First in First Out (FIFO) as
opposed to (LIFO).
'''

class Queue:
    def __init__(self):
        self.queue = list()

    def addtoq(self, dataval):
        if dataval not in self.queue:
            self.queue.insert(0,dataval)
            return True
        return False
    
    def size(self):
        return len(self.queue)

    def peek(self):
        return self.queue[0]
    
    def viewqueu(self):
        for x in self.queue:
            print(x)
    
    def removefromq(self):
        if len(self.queue) > 0:
            return self.queue.pop()
        return ("No elements in queue")

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
TheQueue.addtoq("Thur")

print(TheQueue.size())
# Notice unlike a stack our peed method shows the last entry in the list.
# The person at the head of the queue is the first out so this makes sense.
print(TheQueue.peek())
print("\n")
# Will print from last to first
TheQueue.viewqueu()

# Will remove the first element in the list.
TheQueue.removefromq()

print("\n")
# Will print from last to first with the first entry removed. 
TheQueue.viewqueu()