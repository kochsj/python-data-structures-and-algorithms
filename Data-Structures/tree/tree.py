class _Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None
    def pre_order(self):
        pass
    def post_order(self):
        pass
    def in_order(self):
        pass

class BinarySearchTree(BinaryTree):
    def add(self, value):
        node = _Node(value)
        if not self.root:
            self.root = node
        else:
            top = self.root
            while True:
                if value < top.value and top.left:
                    top = top.left
                elif value < top.value:
                    top.left = node
                    return
                elif value > top.value and top.right:
                    top = top.right
                else:
                    top.right = node
                    return
                    
