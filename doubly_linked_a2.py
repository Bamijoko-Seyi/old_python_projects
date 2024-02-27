class SinglyLinkedNode:
    def __init__(self, item):
        # item is the thing stored at this position in the list
        self._item = item
        self._next = None

    def get_item(self):
        return self._item

    def set_item(self, item):
        self._item = item

    def get_next(self):
        return self._next

    def set_next(self, nxt):
        assert (nxt is None or
                isinstance(nxt, SinglyLinkedNode) )
        self._next = nxt

class DoublyLinkedNode(SinglyLinkedNode):
    def __init__(self, item):
        self._item = item
        self._next = None
        self._prev = None

    def get_prev(self):
        return self._prev

    def set_prev(self, prev):
        assert (prev is None or
                isinstance(prev, DoublyLinkedNode))
        self._prev = prev

from collections.abc import MutableSequence

class SinglyLinkedList(MutableSequence):
    def __init__(self):
        self._head = None

    def __len__(self): # called when you do len()
        # O(n) - n is size of the list
        current = self._head
        size = 0
        while current is not None:
            current = current.get_next()
            size += 1
        return size

    def __get_node_before(self, index):
        # O(n) - n is index < size of the list
        # if index is fixed (example index = 0)
        #  then its O(1)
        current = self._head
        while index > 1:
            if current is None:
                raise IndexError()
            current = current.get_next()
            index -= 1
        return current

    def insert(self, index, item):
        # O(n) - n is index < size of the list
        # if index is fixed (example index = 0)
        #  then its O(1)
        if self._head is None and index == 0:
            node = SinglyLinkedNode(item)
            self._head = node
        elif self._head is None:
            raise IndexError()
        elif index == 0:
            node = SinglyLinkedNode(item)
            old_head = self._head
            self._head = node
            node.set_next(old_head)
        else:
            current = self.__get_node_before(index)
            old_next = current.get_next()
            node = SinglyLinkedNode(item)
            current.set_next(node)
            node.set_next(old_next)

    def __delitem__(self, index):
        # O(n) - n is index < size of the list
        # if index is fixed (example index = 0)
        #  then its O(1)
        if self._head is None:
            raise IndexError()
        elif index == 0:
            self._head = self._head.get_next()
        else:
            current = self.__get_node_before(index)
            deleted = current.get_next()
            after = deleted.get_next()
            current.set_next(after)

    def __getitem__(self, index):
        # method called when you do instance[index]

        # O(n) - n is index < size of the list
        # if index is fixed (example index = 0)
        #  then its O(1)

        if self._head is None:
            raise IndexError()
        elif index == 0:
            return self._head.get_item()
        else:
            current = self.__get_node_before(index+1)
            return current.get_item()

    def __setitem__(self, index, item):
        # method called when you do
        #    instance[index] = "blah"

        # O(n) - n is index < size of the list
        # if index is fixed (example index = 0)
        #  then its O(1)

        if self._head is None:
            raise IndexError()
        elif index == 0:
            self._head.set_item(item)
        else:
            current = self.__get_node_before(index+1)
            current.set_item(item)

class DoublyLinkedList(SinglyLinkedList):
    def __init__(self):
        self._head = None
        self._tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def insert(self, index, item):
        index = __fix_index(index)
        # O(n) - n is index < size of the list
        # if index is fixed (example index = 0)
        #  then its O(1)
        if self._head is None and index == 0:
            node = DoublyLinkedNode(item)
            self._head = node
            self._tail = node
        elif self._head is None:
            raise IndexError()
        elif index == 0:
            node = DoublyLinkedNode(item)
            old_head = self._head
            self._head = node
            node.set_next(old_head)
            old_head.set_prev(node)
        elif index == len(self):
            node = DoublyLinkedNode(item)
            old_tail = self._tail
            self._tail = node
            node.set_prev(old_tail)
            old_tail.set_next(node)
        else:
            before = self.__get_node_before(index)
            after = before.get_next()
            node = DoublyLinkedNode(item)
            node.set_prev(before)
            node.set_next(after)
            after.set_prev(node)
            before.set_next(node)
        self._length += 1
            
    def __delitem__(self, index):
        index = __fix_index(index)
        # O(n) - n is index < size of the list
        # if index is fixed (example index = 0)
        #  then its O(1)
        if self._head is None:
            raise IndexError()
        elif index == 0:
            deleted = self._head
            self._head = deleted.get_next()
            if self._head is None:
                self._tail = None
            else:
                self._head.set_prev(None)
        elif index == len(self) - 1:
            deleted = self._tail
            self._tail = deleted.get_prev()
            if self._tail is None:
                self._head = None
            else:
                self._tail.set_next(None)
        else:
            before = self.__get_node_before(index)
            deleted = before.get_next()
            after = deleted.get_next()
            before.set_next(after)
            after.set_prev(before)
        self._length -= 1
            
    def __get_node_before(self, index):
        index = __fix_index(index)
        # O(n) - n is index < size of the list
        # if index is fixed (example index = 0)
        #  then its O(1)
        if index <= len(self)//2:
            current = self._head
            while index > 1:
                if current is None:
                    raise IndexError()
                current = current.get_next()
                index -= 1
        else:
            current = self._prev
            while index <= len(self)-1:
                if current is None:
                    raise IndexError()
                current = current.get_prev()
                index += 1
        return current

    def __fix_index(self, index):
        if index < 0:
            index += len(self)
        if index < 0:
            raise IndexError()
        if index >= len(self):
            raise IndexError()
        return index

            
        





    

