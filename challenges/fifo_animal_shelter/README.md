# Challenge - FIFO Animal Shelter

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
In this module, an AnimalShelter class is defined with two methods enqueue and dequeue. Dog classes and cat classes are defined and have a name and next property.

Queues only have access to the enqueue and dequeue methods can can not be traversed.

Enqueue - Adds an animal to the end of the queue. O(1) performance.

Dequeue - Removes an animal to the front of the queue. O(1) performance.

## Functionality/Architecture
This application is creating instances of Stacks, Nodes, and PseudoQueues.

Creating - When an instance of an AnimalShelter is created, it is created without any animal objects i.e an empty queue. Animal objects can be created and added by using the enqueue method of the AnimalShelter instance. By passing in 'dog' or 'cat' it creates a dog or a cat. If neither are specified, then no animal is added.

Enqueue('cat'/'dog') - In general, enqueuing to a queue adds a node to the end of the queue. It keeps reference to the previous end of the queue. It makes the previous end point to the new node. The end property of the queue points to the new node. The new node points to none. In the case of the AnimalShelter, enqueuing is adding a cat or a dog to the end of the AnimalShelter queue.

Dequeue('cat'/'dog') - In general, what we want to do when dequeuing from a queue, is to remove the front node from the queue. The next property of the front node is set to None. The front of the queue now points to the previous front's next node. In this case, with the AnimalShelter, we can pass dequeue the value 'dog' or 'cat' and it will remove the first dog or cat from the start of the line.

## Solution
![FIFO Animal Shelter](../../assets/FIFO_animal_shelter.jpeg)

## Other Challenges
### 1. Code Challenge One - [Array_Reverse](https://github.com/kochsj/python-data-structures-and-algorithms/challenges/array_reverse.py)<br>2. Code Challenge Two - [Array_Shift](https://github.com/kochsj/python-data-structures-and-algorithms/challenges/array_shift)<br>3. Code Challenge Three - [Array_Binary_Search](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/array_binary_search)<br>4. Code Challenge Four - [Linked List Merge](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/ll_merge)<br>5. Code Challenge Five - [Queue with Stacks](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/queue_with_stacks)<br>6. Code Challenge Six - [FIFO Animal Shelter](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/fifo_animal_shelter)<br>7. Code Challenge Seven - [FizzBuzz Tree](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/fizz_buzz_tree)<br>8. Code Challenge Eight - [Multiple Bracket Validation](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/multi_bracket_validation)<br>9. Code Challenge Nine - [Binary Tree - Breadth_first_traversal & find_maximum_value](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/breadth_first_tree)<br>10. Code Challenge Ten - [Insertion Sort](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/insertion_sort)


