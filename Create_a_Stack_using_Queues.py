'''
Hayden Hartmann
Coding Problem: Create a Stack using Queues
6/1/2025
'''

from queue import Queue

# we are creating a class which resembles a Stack using two queues
class Stack:
    # constructor that creates two empty queue objects
    def __init__(self):
        self._queue1 = Queue()
        self._queue2 = Queue()

    def PushElement(self, e):
        # first we enqueue e to queue2
        self._queue2.put(e)
        # then we loop through queue1 and dequeue each element into queue2
        while not self._queue1.empty():
            # queue1 will be empty after this is done
            self._queue2.put(self._queue1.get())
        # we then flip the two so that queue2 is empty and ready for the next enqueue
        (self._queue1, self._queue2) = (self._queue2, self._queue1)

    def PopElement(self):
        # checks if queue1 is empty first
        if self._queue1.empty():
            return None
        else:
            # dequeues the first element put into the queue which is actually the last element due to the swap
            return self._queue1.get()

    def TopElement(self):
        # checks if queue1 is empty first
        if self._queue1.empty():
            return None
        else:
            # first we set e1 to the top element and then we must fix the queue because this should not alter the queue
            e1 = self._queue1.get()
            self._queue2.put(e1)
            # we then copy the code from PushElement to fix the queue1
            while not self._queue1.empty():
                self._queue2.put(self._queue1.get())
            (self._queue1, self._queue2) = (self._queue2, self._queue1)

    def IsEmpty(self):
        # we use the queue built in method .empty() to return the boolean
        return self._queue1.empty()

    def Size(self):
        # we use the queue built in method .qsize() to get the length
        return self._queue1.qsize()

test_stack = Stack()
test_stack.IsEmpty()
test_stack.PushElement(5)
test_stack.PushElement(10)
test_stack.PushElement(15)
print(test_stack.TopElement())
print(test_stack.PopElement())
print(test_stack.PopElement())
print(test_stack.PopElement())

