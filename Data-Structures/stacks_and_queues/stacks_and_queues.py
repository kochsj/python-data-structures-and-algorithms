class Node:
    """
    An instance of a node
    Has a value and a pointer to the next node
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def __repr__(self):
        return self.value

class Stack:
    """
    An instance of a Stack
    Has a top property that points to the top Node
    push method adds a Node to the top of the stack
    pop method removes a Node from the top of the stack, returns its value
    peek method returns the value of the top node in the stack
    is_empty method returns True or False if the stack is empty
    """        
    def __init__(self, top=None):
        self.top = top

    def __repr__(self):
        return 'This is an instance of a Stack'

    def push(self, value):
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        try:
            top_node = self.top
            self.top = top_node.next
            top_node.next = None
            return top_node.value
        except AttributeError:
            return None
    
    def peek(self):
        try:
            return self.top.value
        except AttributeError:
            return None

    def is_empty(self):
        if self.top == None:
            return True
        else:
            return False

class Queue:
    """
    An instance of a Queue
    Has a front property that points to the front of the queue
    enqueue method takes a value and adds a node to the end of the queue (O(1))
    dequeue method removes the front node of the queue, returns its value
    peek method returns the value of the front node in the queue
    is_empty method returns True or False if the queue is empty
    """
    def __init__(self, front=None):
        self.front = front
        self.end = None
    
    def enqueue(self, value):
        new_node = Node(value)
        if self.end == None:
            self.front = new_node
            self.end = new_node
        else:
            self.end.next = new_node
            self.end = new_node

    def dequeue(self):
        try:
            first_node = self.front
            self.front = first_node.next
            first_node.next = None
            return first_node.value
        except AttributeError:
            return None
    def peek(self):
        try:
            return self.front.value
        except AttributeError:
            return None

    def is_empty(self):
        if self.front == None:
            return True
        else:
            return False

if __name__ == "__main__":
    new_stack = Stack()
    print(new_stack)