# Data Structures - Tree, Binary Tree, Binary Search Tree

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
In this data structure module, binary trees and binary search trees are created and tested.

Trees are generally a collection of nodes - In a "tree" or branching orientation. 

Trees have a single root and then branching nodes. The connections between the nodes are called edges.

In a Binary Tree, each node can have between zero and two connections (edges), generally described as the "left" or "right" node. Each node can have a 'right' or 'left' but no more. We can traverse the depth of the Binary Tree using the in_order, pre_order, or post_order methods of the Binary Tree class.

In a Binary Search Tree (BST), the tree is 'organized' with a root node at the "top" and lesser values to the left and greater values to the right. This is true for every node in the BST.

## Approach & Efficiency
In this module we take a recursive approach to traversing the trees. Conditionals qualify when the recursion ends. If there are no more left nodes or right nodes for example. 

We are able to add to the BST with O(height) time efficency. We can search for a value with O(log(n)) time efficency. Trees are O(n) space efficency. 

## API
This module has a BinaryTree class and BinarySearchTree sub-class publicly available. BinaryTrees have three methods available; pre_order, post_order, and in_order
```
pre_order(root, arr):
    Method that takes no parameters.
    Returns an array of the values, ordered from the start, 
    going far left, then finishing to the right.
```
```
in_order(root, arr):
    Method that takes no parameters.
    Returns an array of the values, ordered starting from the far left,
     traversing to the far right, then finishing to at the root.
```
```
post_order(root, arr):
    Method that takes no parameters.
    Returns an array of the values, ordered starting from the far left,
    traversing to the top, then finishing to the right.
```

BinarySearchTrees are a sub-class of the BinaryTree and have two methods publicly available: add and contains.
```
add(value):
    Method that accepts one value.
    Adds a node to the binary search tree
    Conditionals that check if the node's value is greater than or less than the "top" node
    Greater values go to the right. Lesser values go to the left.
    Continues until leaf is hit
```
```
contains(value):
    Method that accepts one value.
    Traverses the tree untill it reaches a node with the value that was sent in as an arguement
    Returns True or False if the value is in the tree 
```

## Change Log
Thu Dec 19 2019 19:50:08<br>Created Node, Stack, and Queue classes. Wrote testing for adding, removing, and reading the classes.

## Other Data Structures
### 1. [Linked List](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/Data-Structures/linked_list)<br>2. [Stacks and Queues](https://github.com/kochsj/python-data-structures-and-algorithms/tree/stack-and-queue/Data-Structures/stacks_and_queues)<br>3. [Binary Tree](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/Data-Structures/tree)<br>4. [Hash Table](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/Data-Structures/hashtable)<br>5. [Graph](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/Data-Structures/graphs/breadth_first)

