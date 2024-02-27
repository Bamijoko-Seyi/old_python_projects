
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

    @abstractmethod
    def size(self):
        # returns the number of elements in the stack
        pass

class Stack(StackABC):
    def __init__(self):
        self._elements = list()

    def push(self, element):
        # add an element to the top of the stack
        # element - the element to add to the top of the stack
        # returns None
        self._elements.append(element)

    def pop(self):
        # removes the element on the top of the stack
        # and returns it
        # returns the element that was on the top of the stack
        return self._elements.pop()

    def top(self):
        # returns the element on the top of the stack
        # but does not remove it
        return self._elements[-1]

    def is_empty(self):
        # returns True if the stack does not have elements
        # returns False if the stack has one or more elements
        return len(self._elements) == 0

    def make_empty(self):
        # removes all elements from the stack
        # returns None
        self._elements = list()

    def size(self):
        # returns the number of elements in the stack
        return len(self._elements)

    def __str__(self):
        return str(self._elements)
        
stack = Stack()
stack.push("hello")
print(stack)

def check_brackets(string):
    stack = Stack()
    OPENS = "({[<"
    CLOSES = ")}]>"
    for character in string:
        if character in OPENS:
            stack.push(character)
        elif character in CLOSES:
            opening = OPENS[CLOSES.index(character)]
            if stack.top() == opening:
                stack.pop()
            else:
                print("Unclosed " + stack.top())
                print(character)
                print(stack)
                return False
    if stack.is_empty():
        return True
    else:
        print("Unclosed " + stack.top())

assert check_brackets("({[]})") == True
assert check_brackets("({[}])") == False
# https://eclass.srv.ualberta.ca/pluginfile.php/8328211/mod_tab/content/199619/C175-05-2022-Stacks.pdf


check_brackets("}")

