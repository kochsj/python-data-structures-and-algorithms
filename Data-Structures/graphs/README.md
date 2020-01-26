# Data Structures - Graph

**Author**: Stephen Koch
**Version**: 1.0.0

### Overview
In this module, we are creating a Graph class represented as an adjacency list:

```
Graphs
-- collection of vertices and edges
-- Many classifications
---- directed, undirected, cyclic, acyclic, connected, disconnected, complete
-- vertices are considered to have neighbors and degrees
---- degrees: number of edges connected to a vertex
---- neighbor: an adjacent/connected vertex

Directed vs undirected
-- Directed graphs are like trees
---- each vertex (node) points one direction (to the next node)
-- Undirected graphs have bi-directional edges
---- each edge points to both nodes

Complete, Connected, Disconnected
-- Complete graphs have each vertex pointing to every other vertex
-- connected graphs: every vertex has an edge
-- disconnected graphs: some vertexes do not have edges

Acyclic vs cyclic
-- Cyclic is synonymous with circle
---- In a cyclic graph the edges and directions make it circular
---- possible to end up at the same node that you started with
-- Acyclic is not circular
---- these do not have a cycle (way to get back to the start)

Graph representation
-- Adjacency matrix and adjacency list
-- adjacency matrix: two dimensional array of 1's and 0's
---- 1 signifies a connected node (edge)
---- 0 signifies no edge
-- Adjacency list: collection of linked lists
---- point to edges
```

### Approach & Efficiency
An adjacency list (hash table) was the chosen data structure to use for the Graph and a list was the chosen data structure for to use at each index of the Hash Table to handle collisions.

Adding key/value pairs and getting values from the adjacency list is essentially O(1) for time for both posting and getting. Big O is always looking for the worst case scenario. The worst case would be the length of the linked list at any given index. Say one index had 5 colisions, the Big O for time would be O(5) in that case for time. 


### API
Our Graph has six public methods:

1. add_node(value): adds a new vertex to the graph, returns the added vertex<br><br>
2. add_edge(vertex1, vertex2, [weight]): adds new edge between two virtices, takes in two verticies, has ability to add weight<br><br>
3. get_nodes( ) - returns all of the vertices as a collection<br><br>
4. get_neighbors(vertex): returns a collection of vertices (with weights) connected to a vertex, takes in a vertex<br><br>
5. get_values(vertex): returns the value from a given vertex<br><br>
6. size( ) - returns number of vertices in Graph; integer

## Other Data Structures
### 1. [Linked List](https://github.com/kochsj/python-data-structures-and-algorithms/tree/master/Data-Structures/linked_list)<br>2. [Stacks and Queues](https://github.com/kochsj/python-data-structures-and-algorithms/tree/stack-and-queue/Data-Structures/stacks_and_queues)<br>3. [Binary Tree](https://github.com/kochsj/python-data-structures-and-algorithms/tree/stack-and-queue/Data-Structures/tree)<br>4. [Hash Table](https://github.com/kochsj/python-data-structures-and-algorithms/tree/stack-and-queue/Data-Structures/hashtable)<br>5. [Graph](https://github.com/kochsj/python-data-structures-and-algorithms/tree/stack-and-queue/Data-Structures/graphs)


