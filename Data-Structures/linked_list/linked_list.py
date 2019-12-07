class Linked_List:
    """
    Requires two parameters: head, value
    Optional parameter: next
        Head = node address
        Value = value held in the node
        Next = value pointing to the next node
    """
    def __init__(self, head, value, next=''):
        self.head = head
        self.linked_list = []
    def __repr__(self):
        pass
    def __str__(self):
        """
        Returns a string representing all values in the linked list.
        """
        pass
    def insert(self):
        """
        Takes any value as an argument and adds a new node with that value to the head of the list
        """
    def includes(self):
        """
        Takes any value as an argument and returns true or false
        Checks if that value exists as a Node’s value somewhere within the list.
        """
        pass

class Node:
    """
    Requires two parameters: value, next
    Next = value pointing to the next node
    Value = value held in the node
    """
    def __init__(self, value, next):
        self.value = value
        self.next = next

# help(Linked_List)
