'''
Hayden Hartmann
Coding Problem: Create a Queue using Stacks
6/1/2025
'''

# This class will imitate a Queue by using two stacks, which together make the whole Queue. stack1 is holding
# the oldest elements, while stack2 holds the first added elements
class MyQueue:
    # constructor that creates two empty stacks (actually lists but with our methods they act as stacks)
    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    # adding element to end of queue (this is essentially the same)
    def EnqueueElement(self, e):
        self._stack1.append(e)

    # removing and returning first element added to queue
    def DequeueElement(self):
        # we first make a call to see if both stacks are empty
        if self.IsEmpty():
            return None
        # if stack2 is empty then we pop stack1's elements into stack2
        if len(self._stack2) == 0:
            while len(self._stack1) != 0:
                self._stack2.append(self._stack1.pop())
        # pop and return the last element from stack2
        return self._stack2.pop()


    # peeking (not removing) into first element added to queue, we use similar code as above but slight change
    def FirstElement(self):
        if self.IsEmpty():
            return None
        if len(self._stack2) == 0:
            while len(self._stack1) != 0:
                self._stack2.append(self._stack1.pop())
        # instead of popping the last element, we grab its index as to not remove it from stack2
        return self._stack2[-1]

    def IsEmpty(self):
        if (len(self._stack1) == 0 and len(self._stack2) == 0):
            return True
        else:
            return False

    def Size(self):
        # as both stacks make up the queue, we must add their lengths to get the queue length
        return len(self._stack1) + len(self._stack2)

test_queue = MyQueue()
test_queue.IsEmpty()
test_queue.EnqueueElement(1)
test_queue.EnqueueElement(2)
test_queue.EnqueueElement(3)
print("The size of the queue is:" + " " + str(test_queue.Size()))
print("The first element of the queue is:" + " " + str(test_queue.FirstElement()))
print(test_queue.DequeueElement())
print(test_queue.DequeueElement())
print(test_queue.DequeueElement())
