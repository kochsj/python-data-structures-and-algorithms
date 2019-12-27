from stack_and_node_classes import Stack, Node

class PseudoQueue:
    """
    Requires a stack of nodes as its only parameter.
    Creates an instance of a "PseudoQueue".
    Initialized with two stacks.
    """
    def __init__(self, stack_a):
        self.stack_a = stack_a
        self.stack_b = Stack()

    def enqueue(self, value):
        """
        Takes a value as an arguement.
        Creates an instance of a node with its value being the value given as an arguement.
        Adds the new node to the "end" of the PseudoQueue. Last in line. Top of stack_a.
        """
        new_node = Node(value)
        new_node.next = self.stack_a.top
        self.stack_a.top = new_node

    def dequeue(self):
        """
        Has no parameters.
        Removes the node from the "front" of the PseudoQueue. First in line. The bottom of stack_a.
        """
        while self.stack_a.top:
            value = self.stack_a.pop()
            # new_node = Node(value)
            self.stack_b.push(value)
        result = self.stack_b.pop()    
        while self.stack_b.top:
            value = self.stack_b.pop()
            # new_node = Node(value)
            self.stack_a.push(value)
        return result

if __name__ == "__main__":
    stack_a = Stack()
    stack_a.push(20)
    stack_a.push(15)
    stack_a.push(10)
    queue = PsudoQueue(stack_a)
    a = queue.dequeue()
    print(a.value)
    