class BinaryTree:
    def __init__(self):
        self.root = None

    

class _TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class _QueueNode:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self)
        def.front = None
        def.end = None

    def enqueue(self, value):
        node = _QueueNode(value)

        if not self.front:
            self.front = node
            self.end = node
        
        if self.end:
            self.end.next = node
            self.end = node  

    def dequeue(self):
        if not self.front:
            return None
        node = self.front
        self.front = node.next
        return node

    def is_empty(self):
        if not self.front:
            return True
        return False