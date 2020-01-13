# Challenge - Breadth First (Binary Tree Traversal & Maximum Value)

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
In this module, we are writing 2 additional methods for the BinaryTree class called breadth_first and find_maximum_value. 

**Breadth_first** takes the binary tree of nodes (its self) as an arguement and returns a list of the values inside of those nodes; starting from the root and stretching the width of the tree left to right and top to bottom. 

That is what "breadth first" is describing. The breadth of the tree starting at the top, going from left to right. First. Meaning before going to the next "level" in the height of the binary tree. Here is an example:
```
State of a given tree:
      root: [2]
           /   \
         [7]   [5]
        /  \      \
      [2]  [6]     [9]
          /  \     /
        [5]  [11] [4]

Expected output from breadth_first method:
  [2, 7, 5, 2, 6, 9, 5, 11, 4]
```
As you can see, the method is reading the value of each of the nodes in the tree, starting with the root's level, moving to the next level (7 and 5 -- left to right), then moving farther down to the next level (2, 6, and 9), and after that level we reach the final level (5, then 11, then 4).

This is traversing a Binary Tree **breadth first**.

**Find_maximum_value** also takes the binary tree (it self) as an arguement and returns the highest value contained in the tree. The entire tree is traversed in the process using an iterative level approach. The variable maximum_value is assigned to the current node's value during the traversal only if the value of that node is larger than the maximum_value.

```
Given the same tree example from above...

Expected output from find_maximum_value method: 11
```

## Approach & Efficiency
The most efficent way to keep track of each node on each level before moving on has to be by using a queue. When a node is reached that means that it is at the front of the queue. So it is then safe to remove it from the queue -- dequeue it. 

When we remove the node from the queue, we want to take its value and append it to our list that is keeping track of all the values in the binary tree (breadth first). Additionally we need to add any and all the immediate children of the dequeued node to the end of the queue -- enqueue them.

As nodes get removed from the queue, and their children are added, eventually the final "level" of the tree will be reached. Meaning to say that there are no further children, no further levels. So the nodes will be dequeued like normal and when the queue is empty, that is when we can return our list of values.

Both methods have a big O of O(n) for time. Beacuse, every node in the tree has to have its value read before the list can be returned, the time will scale the same (n). 

Both methods differ for big O of space. With breadth_first method it will have O(n), because we are creating a list of n values, there will be n space taken in memory.  

With find_maximum_value, we are only are ever keeping track of one variable, but are adding the nodes from each level to the queue. This means that at the worst case, our space complexity will be O(w) where w is the "widest" level in the tree and where width is the number of nodes. 
 
## Solution:
Breadth First:
![breadth_first_tree](../../assets/breadth_first.jpeg)

Return Max:
![find_maximum_value](../../assets/return_max.jpeg)

## Other Challenges
### 1. Code Challenge One - [Array_Reverse](https://github.com/kochsj/python-data-structures-and-algorithms/challenges/array_reverse.py)<br>2. Code Challenge Two - [Array_Shift](https://github.com/kochsj/python-data-structures-and-algorithms/challenges/array_shift)<br>3. Code Challenge Three - [Array_Binary_Search](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/array_binary_search)<br>4. Code Challenge Four - [Linked List Merge](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/ll_merge)<br>5. Code Challenge Five - [Queue with Stacks](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/queue_with_stacks)<br>6. Code Challenge Six - [FIFO Animal Shelter](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/fifo_animal_shelter)<br>7. Code Challenge Seven - [FizzBuzz Tree](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/fizz_buzz_tree)<br>8. Code Challenge Eight - [Multiple Bracket Validation](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/multi_bracket_validation)<br>9. Code Challenge Nine - [Binary Tree - Breadth_first_traversal & find_maximum_value](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/breadth_first_tree)<br>10. Code Challenge Ten - [Insertion Sort](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/insertion_sort)



