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

    assert graph._adj_list[start][0].value == 'start'
    assert graph._adj_list[start][1] == (end, 3)

