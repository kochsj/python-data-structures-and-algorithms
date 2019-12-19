import pytest
from tree import _Node, BinaryTree, BinarySearchTree


def test_binary_search_tree_instance():
    new_tree = BinarySearchTree()
    assert new_tree.root == None

def test_binary_search_tree_add_one():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    assert new_tree.root.value == 10

def test_binary_search_tree_add_three():
    new_tree = BinarySearchTree()
    new_tree.add(10)
    new_tree.add(5)
    new_tree.add(20)
    assert new_tree.root.value == 10
    assert new_tree.root.right.value == 20
    assert new_tree.root.left.value == 5