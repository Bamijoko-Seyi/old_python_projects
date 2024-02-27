
# based on python 3.10 documentation: https://docs.python.org/3/library/abc.html 2022-05-18
from abc import ABC
from abc import abstractmethod

# this class will be our informal stack ADT
class StackABC(ABC):
    # This is the abstract base class which
    # fills the role of an informal ADT for a stack

    # Properties: when an element is pushed onto a stack
    # it should become the new top of the stack
    # and the stack should remember that element, even if
    # other elements are pushed on top of it
    
    @abstractmethod
    def push(self, element):
        # add an element to the top of the stack
        # element - the element to add to the top of the stack
        # returns None
        pass

    @abstractmethod
    def pop(self):
        # removes the element on the top of the stack
        # and returns it
        # returns the element that was on the top of the stack
        pass

    @abstractmethod
    def top(self):
        # returns the element on the top of the stack
        # but does not remove it
        pass

    @abstractmethod
    def is_empty(self):
        # returns True if the stack does not have elements
        # returns False if the stack has one or more elements
        pass

    @abstractmethod
    def make_empty(self):
        # removes all elements from the stack
        # returns None
        pass
