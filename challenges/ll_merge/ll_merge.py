class LinkedList:
    """
    Creates an instance of a linked list
    Optional parameter: head
        Head = node address (value)
    """
    def __init__(self, head=None):
        self.head = head

    def __repr__(self):
        return "This is a linked list."

    def __str__(self):
        """
        Returns a string representing all values in the linked list.
        """
        values = self.return_list()
        return f"The values of this list are {values}. A total of {len(values)} nodes."

    def insert(self, value):
        """
        Takes any value as an argument and adds a new node with that value to the head of the list
        """
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node

    def return_list(self):
        current = self.head
        collection_of_values = ''
        while current:
            collection_of_values += f"{current.value} -> "
            current = current.next_node
        return collection_of_values

class Node:
    """
    Requires two parameters: value, next
    Next_node = value pointing to the next node
    Value = value held in the node
    """
    def __init__(self, value, next_node=None):
        self.value = str(value)
        self.next_node = next_node      
    def __repr__(self):
        return self.value


def merge_list(ll_one, ll_two):
    new_ll = LinkedList(ll_one.head)
    current_one = ll_one.head
    current_two = ll_two.head

    while current_one and current_two:
        one_next = current_one.next_node
        two_next = current_two.next_node

        current_one.next_node = current_two
        if one_next == None:
            break
        current_two.next_node = one_next

        current_one = one_next
        current_two = two_next
  
    return new_ll
