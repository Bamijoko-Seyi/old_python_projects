from collections.abc import MutableSequence

class SinglyLinkedNode:
    def __init__(self, element):
        self.element = element
        self.next = None
    def get_element(self):
        return self.element
    def set_element(self, element):
        self.element = element
    def set_next(self, node):
        self.next = node
    def get_next(self):
        return self.next

class SinglyLinkedList(MutableSequence):
    def __init__(self):
        self.head = None # reference to the first node
        self.tail = None # reference to the last node
        self.size = 0

    def append(self, item):
        self.size += 1
        node = SinglyLinkedNode(item)
        if self.head is None:
            self.head = node
        if self.tail is None:
            self.tail = node
        else:
            self.tail.set_next(node)
            self.tail = node

    def insert(self, index, item):
        self.size += 1
        node = SinglyLinkedNode(item)
        if index == 0:
            if self.tail is None:
                self.tail = node
            if self.head is None:
                self.head = node
            else:
                node.set_next(self.head)
                self.head = node
        else:
            prev_node = self.get_node(index - 1)
            next_node = prev_node.get_next()
            prev_node.set_next(node)
            node.set_next(next_node)

    def get_node(self, index):
        if index < 0:
            index = self.size + index
        count = 0
        position = self.head
        while position is not None:
            if index == count:
                return position
            position = position.get_next()
            count += 1
        raise IndexError()
        
    def __len__(self):
        return self.size

    def __getitem__(self, index):
        return self.get_node(index).get_element()

    def __setitem__(self, index, item):
        self.get_node(index).set_element(item)

    def __delitem__(self, index):
        if index == 0 and self.size == 1:
            self.head = None
            self.tail = None
        elif index == 0:
            node = self.head
            next_node = node.get_next()
            self.head = next_node
        elif index == self.size - 1:
            prev_node = self.get_node(index - 1)
            prev_node.set_next(None)
            self.tail = prev_node
        else: # middle of a list with multiple items
            prev_node = self.get_node(index - 1)
            node = prev_node.get_next()
            next_node = node.get_next()
            prev_node.set_next(next_node)
        self.size -= 1

    def __str__(self):
        node = self.head
        string = "["
        while node is not None:
            string += f" {node.get_element()} ->"
            node = node.get_next()
        return string + " ]"

linked = SinglyLinkedList()
print(linked)
linked.append("apple")
print(linked)
print(linked[0])
linked.append("banana")
print(linked)
print(linked[0] == "apple")
print(linked[1] == "banana")
linked.insert(0, "mango")
print(linked)
print(linked[0] == "mango")
print(linked[1] == "apple")
print(linked[2] == "banana")
linked.insert(2, "blueberry")
print(linked)
print(linked[0] == "mango")
print(linked[1] == "apple")
print(linked[2] == "blueberry")
print(linked[3] == "banana")
del linked[1]
print(linked)
print(linked[0] == "mango")
print(linked[1] == "blueberry")
print(linked[2] == "banana")
del linked[0]
print(linked)
print(linked[0] == "blueberry")
print(linked[1] == "banana")
del linked[1]
print(linked)
print(linked[0] == "blueberry")
del linked[0]
print(linked)
print(len(linked))
linked = SinglyLinkedList()
linked.append("apple")
linked.append("banana")
linked.insert(0, "mango")
linked.insert(2, "blueberry")
print(linked)
print(linked.pop(1))
print(linked)
print(linked.index("blueberry"))
linked[1] = "raspberry"
print(linked)


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
        self._items = SinglyLinkedList()
    def __str__(self):
        return "Queue " + str(self._items)
