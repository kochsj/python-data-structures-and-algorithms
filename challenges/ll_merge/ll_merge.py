class LinkedList:
    """
    Creates an instance of a linked list
    Optional parameter: head
        Head = node address (value)
    """
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        """
        Takes any value as an argument and adds a new node with that value to the head of the list
        """
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

class Node:
    """
    Requires two parameters: value, next
    Next_node = value pointing to the next node
    Value = value held in the node
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node        