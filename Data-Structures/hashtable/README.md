# Data Structures - Hash Table

**Author**: Stephen Koch
**Version**: 1.0.0

### Overview
In this module, we are writing about hash tables:

```
Hash Tables
-- Data Structure used to store data
-- Stores data that has key/value pairs
---- Maps key to value and returns an index
-- Hash table is a large empty array
-- Takes advantage of array O(1) to get data
---- Knowing the index

Hash Function
-- Hash function evaluates key/value and returns index
---- The same index every time for the same key
-- When adding to a hash table key is passed to hash function
---- also when getting a key from the hash table

Collisions
-- Occur when two or more key/values are mapped to the same index in the hash table
---- Common to make the index a linked list
---- Thought of like "buckets" that store reference to linked nodes with key/values
------ called chaining
```

### Approach & Efficiency
An array was the chosen data structure to use for the HashTable and a linked list was the chosen data structure for to use at each index of the Hash Table to handle collisions.

Adding key/value pairs and getting values from the Hash Table is essentially O(1) for time for both posting and getting. Big O is always looking for the worst case scenario. The worst case would be the length of the linked list at any given index. Say one index had 5 colisions, the Big O for time would be O(5) in that case for time. 


### API
Three public methods for this Hash Table.
```
1. HashTable.add(key, value)
2. HashTable.get(key)
3. HashTable.contains(key)
```
Add: Takes key and value as arguements, hashes the key, returns hash-index, and adds the key/value pair to the HashTable at hash-index. Also handles collisions.

Get: Takes key as arguement, hashes key; assigns a hash-index, returns value from table at the hash-index.

Contains: Takes in a key as arguement and returns a boolean if key is already in HashTable.

## Other Data Structures
### 1. [Linked List](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/Data-Structures/linked_list)<br>2. [Stacks and Queues](https://github.com/kochsj/python-data-structures-and-algorithms/tree/stack-and-queue/Data-Structures/stacks_and_queues)<br>3. [Binary Tree](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/Data-Structures/tree)<br>4. [Hash Table](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/Data-Structures/hashtable)<br>5. [Graph](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/Data-Structures/graphs/breadth_first)


