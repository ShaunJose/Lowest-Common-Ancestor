# author: Shaun Jose
# Date created: 22/09/2018 (modified version of Binary Graph LCA)

# Lowest Common Ancestor class
# Finds the LCA of two nodes in a Graph

# Graph respresentation idea source:
# https://www.python.org/doc/essays/graphs/

# DirectedAcyclicGraph class - Graph respresented as dictionary with data values, not node objects!
# Methods: add(self, val), addEdge(self, src, dst), hasDirectPathTo(self, src, dst), _isCyclic(self), LCA(self, val_1, val_2)
# Attributes: _graph: is a dicitonary of data values an arrays with connections

class DirectedAcyclicGraph:

    # Initializes an Empty graph
    def __init__(self):
        self._graph = {} # _ implies it shouldn't be accessed from outside


    # NOTE: adds nodes to a graph. Doesn't accept nodes with vals that already exist
    def add(self, val):
        """
        Adds a node to the Directed Acyclic Graph
        Doesn't add duplicate nodes (Nodes with duplicate data values)
        Returns True if node was successful added, else False
        """

        # Check if key already exists in _graph.keys()

        # Add if it doesn't


    # Connects node src to node dst (one way route)
    # Checks if graph is cyclic before connecting nodes?
    def addEdge(self, src, dst):
        """
        Creates a connection from node src to node dst.
        Does not create duplicate connections if node src is already directly
        connected to node dst
        Does not create a connection which would lead to a cyclic graph
        Returns true if connection succesfully created, False otherwise
        """

        # Check if src and dst both exist in graph

        # Check if DST key doesn’t already exist in array of src key (i.e. _graph[src])

        # Check if this connection will make graph cyclic

        # Add dst to _graph[src] if reached here


    # Checks if src is directly connected to destination
    # NOTE: This methods exists only to check if add and addEdge work
    def hasDirectPathTo(self, src, dst):
        """
        Returns true if src exists in graph, and if src is directly connected to dst, else False.
        """
        # Check if src exists in graph

        # Return dst in _graph[src]


    # Checks if graph is cyclic
    def _isCyclic(self):
        #TODO: find a way


    # Find the LCA of two nodes of a graph
    def LCA(self, val_1, val_2):
        """
        Finds the lowest common ancestor of two nodes, (inclusive of the nodes themselves), and returns the node
        Returns None if LCA not found
        """

        # Existing nodes check

        # Same node check

        # Same parent check

        # Normal check

        return None # nodes don't have a common ancestor
