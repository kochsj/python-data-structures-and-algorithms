class _Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def add(self, value, root=None):
        node = _Node(value)
        root = root or self.root

        if not root:
            self.root = node
            return

        if value < root.value:
            if root.left:
                self.add(value, root.left)
            else:
                root.left = node
        if value > root.value:
            if root.right:
                self.add(value, root.right)
            else:
                root.right = node


def fizz_buzz_tree():
    pass

def fizz_buzz_func():
    pass
            

