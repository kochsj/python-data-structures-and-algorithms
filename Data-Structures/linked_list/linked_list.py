class Linked_List:
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

    def includes(self, value):
        """
        Takes any value as an argument and returns true or false
        Checks if that value exists as a Node’s value somewhere within the list.
        """
        current = self.head
        while current:
            if str(current) == value:
                return True
            else:
                current = current.next_node
        return False
    def return_list(self):
        try:
            current = self.head
            collection_of_values = []
            while current:
                collection_of_values.append(str(current))
                current = current.next_node
            return collection_of_values
        except TypeError:
            return 'For testing, Please input strings.'
    # .append(value) which adds a new node with the given value to the end of the list
    def append(self, value):
        node = Node(value)
        current = self.head
        while current and current.next_node != None:
            current = current.next_node
        current.next_node = node

    # .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
    def insert_before(self, value, new_value):
        node = Node(new_value)
        current = self.head
        if current.value == value:
            node.next_node = self.head
            self.head = node
        while current.next_node and self.head.value != new_value:
            if current.next_node.value != value:
                current = current.next_node
            else:
                node.next_node = current.next_node
                current.next_node = node
                break

    # .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node
    def insert_after(self, value, new_value):
        node = Node(new_value)
        current = self.head
        while current.value != value:
            current = current.next_node
        node.next_node = current.next_node
        current.next_node = node
# at any time you know 4 things. where you are, 'who' is next, and the values of both. head is a Node. head.value would be the value
class Node:
    """
    Requires two parameters: value, next
    Next_node = value pointing to the next node
    Value = value held in the node
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def __repr__(self):
        return self.value
    def get_data(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next

if __name__ == "__main__":
    empty_list = Linked_List()
    empty_list.insert('Node_1')
    empty_list.insert('Node_2')
    empty_list.append('Node_X')
    print(empty_list)
