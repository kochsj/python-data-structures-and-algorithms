class Graph:
    """
    [method] - add_node(value): adds a new vertex to the graph, returns the added vertex
    [method] - add_edge(vertex1, vertex2, [weight]): adds new edge between two virtices, takes in two verticies, has ability to add weight
    [method] - get_nodes - returns all of the vertices as a collection
    [method] - get_neighbors(vertex): returns a collection of vertices (with weights) connected to a vertex, takes in a vertex

    """
    def __init__(self):
        self._adj_list = {}

    def add_node(self, value):
        """
        Adds a new vertex to the graph.
        Parameters:
            [value] - value to be assigned to the vertex
        Returns: 
            vertex - the vertex that was created
        """
        vertex = Vertex(value)
        try:
            self._adj_list[vertex].append(vertex)
        except:
            self._adj_list[vertex] = [vertex]

        return vertex

    def add_edge(self, start_vertex, end_vertex, weight=0):
        """
        Adds an edge between two existing vertices in the Graph.
        Parameters:
            [start_vertex] - First vertex to start edge from
            [end_vertex] - Second vertex to point edge to
            [[weight]] - Adds a weight to the edge (default 0)
        No return
        """
        if start_vertex not in self._adj_list or end_vertex not in self._adj_list:
            raise KeyError(f'{start_vertex.value} is not in {self}')
        
        adjacencies = self._adj_list[start_vertex]
        adjacencies.append((end_vertex, weight))



    def size(self):
        """
        Returns: Total number of vertices in the graph
        """
        return len(self._adj_list)

    def get_value(self, vertex):
        """
        Gets a value from the graph at a given vertex
        Parameters:
            [vertex] - The vertex to get value from
        Return:
            value - value from the vertex
        """



class Vertex:
    """
    Instance of a vertex
    [init] - requires a value to init
    """
    def __init__(self, value):
        self.value = value

