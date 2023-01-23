import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start=None, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """

        # handle edge cases first
        # edge case for empty graph
        G = self
        if nx.is_empty(G):
            raise Exception("This graph is empty!")

        # edge case for unconnected undirected or directed graph
        # need to first check whether the graph is directed or undirected
        if nx.is_directed(G):
            if nx.is_weakly_connected(G)==False:
                raise Exception("This graph is not connected!")
        else:
            if nx.is_connected(G)==False:
                raise Exception("This graph is not connected!")

        # edge case for start node that doesn't exist in the graph
        if start and G.has_node(start)==False:
            raise Exception("The start node doesn't exist in the graph!")

        # edge case for end node that doesn't exist in the graph
        if end and G.has_node(end)==False:
            raise Exception("The end node doesn't exist in the graph!")

        # edge case for when no start node was inputted
        if start==None:
            raise Exception("You need to put a starting node when calling the function!")

        # now for the actual bfs implementation
        # initialize queue, visited nodes, and predecessors dictionary (used to find path from start to end)
        Q = []
        visited = []
        predecessors = dict()
        predecessors[start] = None

        # add the current starting node to the queue and visited
        Q.append(start)
        visited.append(start)

        # while there are items in the queue
        while Q:
            # get the neighbors of the oldest item in the queue, or the first element in the list
            current_node = str(Q.pop(0))
            neighbors = G.neighbors(current_node)

            # for all the neighbors
            for neighbor in neighbors:
                # if it hasn't been visited, visit the node and add it to the queue
                if neighbor not in visited:
                    visited.append(neighbor)
                    Q.append(neighbor)
                    # in our predecessors dictionary, add the neighbor as key and current node as value to keep track
                    predecessors[neighbor] = current_node

        # return visited nodes if no end point was given
        if end == None:
            return(visited)

        # if end exists and a path exists
        elif end and nx.has_path(G, start, end):
            # initialize list of nodes with the shortest path
            path = []
            # start the path from the end node to trace back to the start
            path.append(end)
            # initialize next_node to differentiate from end variable
            next_node = end
            # while there is a next node to go to from our traversal
            while predecessors[next_node]:
                # add the next node to the path
                path.append(predecessors[next_node])
                next_node = predecessors[next_node]

            # return the reversed path since we worked backwards
            # this works because our graph is unweighted. if it were weighted, we would need to implement dijkstra's algorithm
            return path[::-1]

        # if there was an end input but no path exists
        else:
            return None