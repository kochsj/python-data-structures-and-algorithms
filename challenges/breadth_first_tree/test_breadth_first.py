import pytest
from breadth_first import BinaryTree

def test_add_one_to_tree():
    new_tree = BinaryTree()
    new_tree.add(2)
    assert new_tree.root.value == 2

def test_add_three_to_tree():
    new_tree = BinaryTree()
    new_tree.add(2)
    assert new_tree.root.value == 2
    new_tree.add(7)
    assert new_tree.root.left.value == 7
    new_tree.add(5)
    assert new_tree.root.right.value == 5

