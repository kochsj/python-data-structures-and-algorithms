# Challenge - FizzBuzz Tree

**Author**: Stephen Koch
**Version**: 1.0.0

## Overview
In this module, we are writing a function "fizz_buzz_tree" that takes a binary tree of integers as an arguement and does "FizzBuzz" to the values in the binary tree.

Looking at every value in the binary tree, our function will determine that, if a value is evenly divisible by 3 its value will be reassigned to "Fizz". If the value is evenly divisible by 5 then its value will be reassigned to "Buzz". If the value is both evenly divisible by 3 and by 5, then its value will be reassigned to "FizzBuzz". If none of these conditions are met, then our function will reassign the integer to a string of the same value.

Example:
```
Starting Values => [2] -> [3] -> [5] -> [10] -> [15] -> [19]
After fizz_buzz_tree:
Returns => ['2'] -> ['Fizz'] -> ['Buzz'] -> ['Buzz'] -> ['FizzBuzz'] -> ['19']
```

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

Navigate to your command line:
```
MacOS: Press command + space to open up the search feature
Search for "terminal" - This is your default command line on MacOS.
```
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

## Approach & Efficiency
It was decided that using a helper function was going to be the best way to make these functions readable. Reference to the original BinaryTree object has to be kept during recursive traversal of the binary tree, so a tree parameter is used in the fizz_buzz_tree function. The tree parameter is never mutated during the traversal and value reassignment which is important.

The next parameter that is adjusted during traversal is the root parameter. This gives reference to the position in the stack that the function is operating on.

At each step in the binary tree, before invoking the function again, the value is reassigned to the return value from the helper fiz_buzz_func. 

Big O for this function is a factor O(n) for time, because every node in the tree must be accessed. More nodes means more time. This function is O(h) for space, as the height of the tree determines how far up the stack the function calls need to go before their 'left' and 'right' are completed and can be popped off the stack. 
 
## Solution:
![fizz_buzz_tree](../../assets/fizz_buzz.jpeg)

## Change Log
Mon Dec 23 2019 15:49:50<br>Created fizz_buzz_tree function. Wrote testing for functionality and edge cases.


