import pytest
from graph import Graph, Vertex

def test_add_vertex():
    graph = Graph()
    expected = 'spam'
    actual = graph.add_node('spam').value
    assert actual == expected

def test_size():
    graph = Graph()
    graph.add_node('spam')
    expected = 1
    actual = graph.size()
    assert actual == expected

def test_add_edge_start():
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')
    
    graph.add_edge(start, end, 3)

def test_add_edge_end():
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')
    
    graph.add_edge(end, start, 3)

def test_edge_is_added():
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')
    
    graph.add_edge(start, end, 3)

    assert graph._adj_list[start][0] == [start, end, 3]

def test_get_nodes():
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')

    assert graph.get_nodes() == [start, end]

def test_get_neighbors():
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')

    graph.add_edge(start, end, 3)

    assert graph.get_neighbors(start) == [end, 3]
    assert graph.get_nodes() == [start, end]

def test_get_values():
    graph = Graph()
    start = graph.add_node('start')
    end = graph.add_node('end')

    assert graph.get_values(start) == 'start'
    
