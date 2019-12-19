# Data Structures - Stacks and Queues

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
In this file of the data structures, stacks and queues are created and tested.

Stacks and queues are a collection of nodes - Each in different orientation. 

Stacks are like a stack of plates. The first node being both the top and the bottom. The first stays as the 'bottom' or end. Each node added after makes the newest node the 'top'. Again, like a stack of plates, adding to the top of the stack. Stacks have a top property to keep track of what 'plate' is on top.

Queues are like a line at a bank. The first node being the front of the queue and the end of the queue (line). As nodes are added, they are 'enqueued' and join the line. The new node is now the end of the queue and the first node is still the front of the queue. Each additional node becomes the end of the queue as the 'line' gets longer. When dequeuing from the queue, the front node is removed and the 'next in line' then becomes the front of the queue. Just like standing in line at a bank. 

## Getting Started
Running tests is straight forward and involves using pytest.

First, make sure that you have python3 installed:
```
$ python3 --version
Python 3.7.5
```
If you do not:
```
$ brew install python
```
You need to have the files locally. Click on the green clone or download button and Download ZIP:

![Click_to_download](../../assets/Click_to_download.png)


In your command line, navigate to this directory:
```
$ cd ~  ##this is your root directory
$ cd Downloads  ##by default: Downloads is a directory inside of your root; and where your file will be downloaded
$ cd python_data_structures_and_algorithims ##and now you are in this directory
```
This module is running tests on given data imputs. Install [pytest](https://docs.pytest.org/en/latest/getting-started.html) to get started:
Installing pytest:
```
$ pip install -U pytest
```
Running tests:
```
$ pytest
```
## Functionality/Architecture
This application is running tests on Stacks and Queues. The sack class is defined, the queue class is defined and so is the node class.

Creating - When an instance of a stack or queue is created, it is created without any nodes i.e an empty stack or queue. Nodes can be created and added by using the push or enqueue methods of the stack or queue classes. By passing in a value as an arguement for the node, these methods define the 'next' node.

Push(stack) - Pushing to a stack adds a node to the top of the stack. The top property of the Stack instance is now set to the newly created node on the top. The next property of that new node is set to the previous top of the stack. O(1) performace

Enqueue(queue) - Enqueuing to a queue adds a node to the end of the queue. It keeps reference to the previous end of the queue. It makes the previous end point to the new node. The end property of the queue points to the new node. The new node points to none. O(1) performace

Removing - Both the stack and queue classes have methods to remove nodes. Stacks can pop nodes off of the top of the stack. Queues can dequeue nodes from the front of the stack.

Pop(stack) - Popping off of a stack targets the top property of the Stack instance. The next node in the stack becomes the new top. The top's next property is set to None, effectively removing it from the stack. O(1) performace

Dequeue(queue) - Dequeuing from a queue, removes the front node from the queue. The next property of the front node is set to None. The front of the queue now points to the previous front's next node. O(1) performace

Peek and is_empty - Both stacks and queues have peek and is_empty methods. The peek methods are both O(1) performace, and look at the top of the Stack and the front of the queue respectively. Peek returns the value of the top/front node. The is_empty methods are also O(1) performace, returning True only if the top of the stack points to None and if the front of the queue points to None. Other wise is_empty returns false.

## Change Log
Sun Dec 15 2019 18:42:41<br>Created Node, Stack, and Queue classes. Wrote testing for adding, removing, and reading the classes.


