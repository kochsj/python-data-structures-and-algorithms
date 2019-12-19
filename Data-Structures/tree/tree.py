class _Node:
    """
    Creates an instance of a node.
    Has value, left, and right properties.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    """
    Creates an instance of a Binary tree.
    Has a root property.
    Has three methods: pre_order, in_order, and post_order.
    """
    def __init__(self):
        self.root = None

    def pre_order(self, root, arr=[]):
        """
        Method that takes no parameters.
        Returns an array of the values, ordered from the start, going far left, then finishing to the right.
        """
        arr.append(root.value)

        if root.left:
            self.pre_order(root.left, arr)

        if root.right:
            self.pre_order(root.right, arr)

    def post_order(self, arr=[]):
        """
        Method that takes no parameters.
        Returns an array of the values, ordered starting from the far left, traversing to the top, then finishing to the right.
        """
        pass
    def in_order(self, arr=[]):
        """
        Method that takes no parameters.
        Returns an array of the values, ordered starting from the far left, traversing to the far right, then finishing to at the root.
        """
        pass

class BinarySearchTree(BinaryTree):
    def add(self, value):
        """
        Method that accepts one value.
        Adds a node to the binary search tree
        Conditionals that check if the node's value is greater than or less than the "top" node
        Greater values go to the right. Lesser values go to the left.
        Continues until leaf is hit
        """
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
    
    def contains(self, value):
        """
        Method that accepts one value.
        Traverses the tree untill it reaches a node with the value that was sent in as an arguement
        Returns True or False if the value is in the tree at least once
        """

                    
