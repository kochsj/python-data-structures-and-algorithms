# Data Structures - Stacks and Queues

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
In this file of the data structures, stacks and queues are created and tested.



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

![Click_to_download](assets/Click_to_download.png)


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
This application is running tests on Linked Lists. The linked list class is defined and so is the node class.

Creating - When an instance of a list is created it is created without any nodes i.e an empty linked list. Nodes can be created and added by using the insert method of the linked list class. By passing in a value as an arguement for the node, the insert method defines the next_node as the current node and then sets the head of the list to be the inserted node.

Searching - A linked list can be searched for a specific node using the includes method of the linked list. By passing in the search parameter as an arguement, includes will traverse the linked list and return "True" if the search value is found and "False" if not found by the end of the list.

Printing - The values of every node in the linked list can be determined in two separate ways. Using python's built in global object method, print, you can create a linked list and invoke print(name of your list). This will return every value as a string and total the number of values. Additionally the return list method of a linked list can be invoked, which will return an array of the values.

Append - A method of the linked list class. Accepts one parameter, value, and creates a new instance of a Node and adds that new Node instance to the end of the linked list.

Insert Before/After - Methods of the linked list class. They both accept two parameters, a target Node value and a new node value. The linked list instance is traversed by these methods. When the target value is found, the methods add the new node before or after that target value.

Kth from end - A method of the linked list class. Accepts one parameter, 'k', representing the number of indices from the last index. This method traverses the entire linked list, creates a list of values, and returns the value at reverse-index 'k'.

Find middle node - A method of the linked list class that finds the middle Node's value. Takes no parameters. This method traverses an entire instance of a linked list and creates a list of values. Taking the length of that value list and floor deviding by two gives a consistent middle (ceiling). Returns the value of the middle Node.

## Change Log
Sat Dec 07 2019 14:24:42<br>Created linked list and node classes. Developed tests to ensure proper functionality.

Tue Dec 10 2019 13:37:24<br>Created new linked list methods. Append, insert_before, insert_after, kth_from_end, and find_the_middle. Devloped tests to ensure proper functionality.

![Class 07](../../assets/kth_value.jpeg)

