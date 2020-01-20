# Data-Structures-and-Algorithms - Challenge Thirteen

# Repeating Word Search
### Problem domain
This challenge asks us to write a function that takes a large string as an arguement and returns the first repeated word that is found.

### Challenge
Take a string and iterate through the words in the string. Return the first instance of a repeated word.
```
$ string = "Once upon a time, there was a brave princess who..."
$ result = repeated_word(string)
$ result
$ 'a'
```
### Approach & Efficiency
The approach here is to get an iterable for all of the words in the string. A list is best suited iterable for storing all of the words from the string. Before storing the words, the original string needs to be cleaned up a bit.

We are using re - Python's regular expression package to substitue any punctuation with a null string. When the string is just words and spaces we can split the string using the String.split method. 

We are returned a list of all of the words and can begin keeping track of what words we have seen and when we hit that first repeated word. Because we have a list of all words, we can iterate through them and append the words to new list. We check that new list for each iteration of the word-list. As soon as there is a match in the new list we return the word.

### Solution


### Other Challenges
#### 1. Code Challenge One - [Array_Reverse](https://github.com/kochsj/python-data-structures-and-algorithms/challenges/array_reverse.py)<br>2. Code Challenge Two - [Array_Shift](https://github.com/kochsj/python-data-structures-and-algorithms/challenges/array_shift)<br>3. Code Challenge Three - [Array_Binary_Search](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/array_binary_search)<br>4. Code Challenge Four - [Linked List Merge](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/ll_merge)<br>5. Code Challenge Five - [Queue with Stacks](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/queue_with_stacks)<br>6. Code Challenge Six - [FIFO Animal Shelter](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/fifo_animal_shelter)<br>7. Code Challenge Seven - [FizzBuzz Tree](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/fizz_buzz_tree)<br>8. Code Challenge Eight - [Multiple Bracket Validation](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/multi_bracket_validation)<br>9. Code Challenge Nine - [Breadth-First Binary Tree Traversal](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/breadth_first_tree)<br>10. Code Challenge Ten - [Insertion Sort](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/insertion_sort)<br>11. Code Challenge Eleven - [Merge Sort](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/merge_sort)<br>12. Code Challenge Twelve - [Quick Sort](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/quick_sort)<br>13. Code Challenge Thirteen - [Repeating Word Search](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/challenges/repeated_word)
