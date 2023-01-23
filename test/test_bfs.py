# write tests for bfs
import networkx as nx
import pytest
from search import Graph

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    # initialize the graph read in as tiny_network
    G = nx.read_adjlist("./data/tiny_network.adjlist", create_using=nx.DiGraph, delimiter=";")
    # using nx.bfs_tree, check that the output is the same as my bfs function
    assert Graph.bfs(G, 'Atul Butte')==list(nx.bfs_tree(G, 'Atul Butte'))


def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """
    citation_graph = nx.read_adjlist("./data/citation_network.adjlist", create_using=nx.DiGraph, delimiter=";")
    assert Graph.bfs(citation_graph, 'Marina Sirota', 'Neil Risch')==nx.shortest_path(citation_graph, 'Marina Sirota', 'Neil Risch')

    # test for nodes that are not connected
    assert Graph.bfs(citation_graph, 'Reza Abbasi-Asl', 'Charles Chiu') == None


def test_edge_bfs():
    """
    Tests for edge cases: when start node does not exist in graph,
    when end node does not exist in graph,
    and a failed test case raising exception when the start and end node are the same
    """
    citation_graph = nx.read_adjlist("./data/tiny_network.adjlist", create_using=nx.DiGraph, delimiter=";")

    with pytest.raises(Exception):
        # start node not in graph
        Graph.bfs(citation_graph, 'Yaen Chen')
        # end node not in graph
        Graph.bfs(citation_graph, 'Marina Sirota', 'Yaen Chen')