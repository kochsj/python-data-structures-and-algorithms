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
        idx, current, new_nodes = 0, self.head, []
        while idx < len(value):
            if idx == (len(value) - 1):
                new_nodes.append(Node(value[idx]))
            else:
                new_node = Node(value[idx], value[idx+1])
                new_nodes.append(new_node)
            idx += 1
        idx = 0
        while current:
            if current.next_node == None:
                current.next_node = new_nodes[idx]
                break
            current = new_nodes[idx]
            idx += 1
    # .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
    def insertBefore(self, value, new_value):
        pass
    # .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node
    def insert_after(self, value, new_value):
        pass

class Node:
    """
    Requires two parameters: value, next
    Next = value pointing to the next node
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
