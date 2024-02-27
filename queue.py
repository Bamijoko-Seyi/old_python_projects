class Queue:
    def __init__(self):
        '''
        Create a new queue that is empty.
        It needs no parameters and returns an empty queue
        '''
        self.clear()

    def enqueue(self, item):
        '''
        Adds a new item to the rear of the queue.
        It needs an item and returns nothing
        '''
        # index 0 will be the back of the queue
        self._items.insert(0, item)

    def dequeue(self):
        '''
        Remove the front item from the queue
        It needs no parameters and returns the item.
        The queue is modified.
        '''
        return self._items.pop()

    def is_empty(self):
        return len(self._items) == 0
    def size(self):
        return len(self._items)
    def clear(self):
        self._items = list()
    def __str__(self):
        return "Queue " + str(self._items)

queue = Queue()
print("enqueue a")
queue.enqueue("a")
print(queue)
print("enqueue b")
queue.enqueue("b")
print(queue)
print("dequeue", queue.dequeue())
print(queue)
print("enqueue c")
queue.enqueue("c")
print(queue)
print("dequeue", queue.dequeue())
print(queue)
print("dequeue", queue.dequeue())
print(queue)

class BoundedQueueFullError(RuntimeError):
    pass
class BoundedQueueEmptyError(RuntimeError):
    pass


class BoundedQueue(Queue):
    def __init__(self, capacity):
        '''
        Create a new bounded queue that is empty.
        It needs the capacity and returns an empty queue
        '''
        self.capacity = capacity
        self.clear()
    
    def enqueue(self, item):
        '''
        Adds a new item to the rear of the queue.
        It needs an item and returns nothing
        '''
        # index 0 will be the back of the queue
        if self.is_full():
            raise BoundedQueueFullError()
        self._items.insert(0, item)

    def __str__(self):
        return "BoundedQueue " + str(self._items)

    def capacity(self):
        return self.capacity

    def is_full(self):
        return len(self._items) == self.capacity

queue = BoundedQueue(2)
print("enqueue a")
queue.enqueue("a")
print(queue)
print("enqueue b")
queue.enqueue("b")
print(queue)
#print("enqueue c")
#queue.enqueue("c")
print(queue)

class Nothing:
    pass

class CircularQueue(BoundedQueue):
    def clear(self):
        self.front = 0
        self.back = 0
        self._items = [Nothing] * self.capacity

    def enqueue(self, item):
        '''
        Adds a new item to the rear of the queue.
        It needs an item and returns nothing
        '''
        assert item is not Nothing
        if self.is_full():
            raise BoundedQueueFullError()
        self._items[self.back] = item
        self.back = (self.back + 1) % self.capacity
        
    def is_empty(self):
        return (self.front == self.back and
                self._items[self.front] is Nothing)

    def is_full(self):
        return (self.front == self.back and
                self._items[self.front] is not Nothing)

    def dequeue(self):
        '''
        Remove the front item from the queue
        It needs no parameters and returns the item.
        The queue is modified.
        '''
        if self.is_empty():
            raise BoundedQueueEmptyError()
        item = self._items[self.front]
        self._items[self.front] = Nothing
        self.front = (self.front + 1) % self.capacity
        return item
    def peek(self):
        if self.is_empty():
            raise BoundedQueueEmptyError()
        return self._items[self.front]

    def size(self):
        if self.is_full():
            return capacity
        size = self.back - self.front
        if size < 0:
            size += self.capacity
        return size
    def __str__(self):
        return "CircularQueue " + str(self._items)

print("------")
queue = CircularQueue(3)
print("enqueue a")
queue.enqueue("a")
print(queue)
print("enqueue b")
queue.enqueue("b")
print(queue)
print("dequeue", queue.dequeue())
print(queue)
print("enqueue c")
queue.enqueue("c")
print(queue)
print("dequeue", queue.dequeue())
print(queue)
print("dequeue", queue.dequeue())
print(queue)
queue.enqueue("d")
print(queue)
print("dequeue", queue.dequeue())
print(queue)
