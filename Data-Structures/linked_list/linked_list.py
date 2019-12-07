class Linked_List:
    """
    Requires two parameters: head, value
    Optional parameter: next
        Head = node address
        Value = value held in the node
        Next = value pointing to the next node
    """
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return "This is a linked list."

    def __str__(self):
        """
        Returns a string representing all values in the linked list.
        """
        return f"The values of this list are {values}. Which total {len(values)} add up to {sum}."

    def insert(self, value):
        """
        Takes any value as an argument and adds a new node with that value to the head of the list
        """
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node



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
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

    def get_data(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next


