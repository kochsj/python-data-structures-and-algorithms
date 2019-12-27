class LinkedList:
    """
    Creates an instance of a linked list
    Optional parameter: head
        Head = node address (value)
    """
    def __init__(self):
        self.head = None

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
            if str(current.value) == value:
                return True
            else:
                current = current.next_node
        return False

    def return_list(self):
        """
        Returns a list of all of the nodes in the linked list. The actual nodes themselves.
        """
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
        """
        Method that takes a value as its only arguement.
        Creates a Node object.
        Adds the new node to the end of the linked list.
        """
        node = Node(value)
        if self.head:
            current = self.head
            while current:
                if current.next_node:
                    current = current.next_node
                else:
                    break
            current.next_node = node

        else:
            self.head = node

    # .insertBefore(value, newVal) which add a new node with the given newValue immediately before the first value node
    def insert_before(self, value, new_value):
        """
        Method that takes a targeted node value and a new node value as arguements.
        Creates a new node from the new_value.
        Traverses the linked list and stops when it finds the targeted node value.
        Inserts the new node into the linked list BEFORE the targed node value.
        """
        node = Node(new_value)
        if self.head:
            if self.head.value == value:
                node.next_node = self.head
                self.head = node
                return
            current = self.head
            while current:
                if current.next_node.value == value:
                    node.next_node = current.next_node
                    current.next_node = node
                    return
                current = current.next_node
        else:
            return "Not found"


    # .insertAfter(value, newVal) which add a new node with the given newValue immediately after the first value node
    def insert_after(self, target, new_value):
        """
        Method that takes a targeted node value and a new node value as arguements.
        Creates a new node from the new_value.
        Traverses the linked list and stops when it finds the targeted node value.
        Inserts the new node into the linked list AFTER the targed node value.
        """
        node = Node(new_value)
        if self.head:
            current = self.head
            while current:
                if current.value == target:
                    node.next_node = current.next_node
                    current.next_node = node
                current = current.next_node
        else:
            return "Not found"

    def kth_from_end(self, k):
        """
        Traverses the linked list.
        Returns the node value k-indexes from the end of the linked list.
        """
        value_list = []
        current = self.head
        while current.next_node:
            value_list.append(current.value)
            current = current.next_node
        value_list.append(current.value)
        if 0 <= k < len(value_list):
            return value_list[-(k+1)]
        else:
            return 'K is out of range'

    def find_middle_node(self):
        """
        Traverses the linked list.
        Returns the value of the node in the middle of the linked list (ceiling).
        """
        value_list = []
        current = self.head
        while current.next_node:
            value_list.append(current.value)
            current = current.next_node
        value_list.append(current.value)
        middle = (len(value_list)+1)//2
        return value_list[middle]

# at any time you know 4 things. where you are, 'who' is next, and the values of both. head is a Node. head.value would be the value
class Node:
    """
    Requires two parameters: value, next
    Next_node = value pointing to the next node
    Value = value held in the node
    """
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def __repr__(self):
        return self.value
    def get_data(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self, new_next):
        self.next_node = new_next

if __name__ == "__main__":
    empty_list = LinkedList()
    empty_list.insert('Node_1')
    empty_list.insert('Node_2')
    empty_list.append('Node_X')
    print(empty_list)
