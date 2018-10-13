# author: Shaun Jose
# Date created: 22/09/2018 (modified version of Binary Graph LCA)

# Lowest Common Ancestor class
# Finds the LCA of two nodes in a Graph

# Sources:
# 1. Graph respresentation idea source:
#    https://www.python.org/doc/essays/graphs/
# 2. _isCyclic implementation:
#    Gareth Rees's efficient implementation answer on https://codereview.stackexchange.com/questions/86021/check-if-a-directed-graph-contains-a-cycle

# DirectedAcyclicGraph class - Graph respresented as dictionary with data values, not node objects!
# Methods: add(self, val), addEdge(self, src, dst), _incrementNodeDepths(self, node, inc), getDepth(self, node), hasDirectPathTo(self, src, dst), _isCyclic(self), LCA(self, val_1, val_2)
# Attributes: _graph: is a dicitonary of data values an arrays with connections
#             _depth{}: dicitonary with key as node_val and val as node_depth

class DirectedAcyclicGraph:

    # Initializes an Empty graph
    def __init__(self):
        self._graph = {} # _ implies it shouldn't be accessed from outside
        self._depth = {}


    # NOTE: adds nodes to a graph. Doesn't accept nodes with vals that already exist
    def add(self, val):
        """
        Adds a node to the Directed Acyclic Graph
        Doesn't add duplicate nodes (Nodes with duplicate data values)
        Returns True if node was successful added, else False
        """

        # Check if key already exists in _graph.keys()
        if val in self._graph.keys():
            return False

        # Add if it doesn't
        self._graph[val] = [] #Node not connected to anything
        self._depth[val] = 1 #Depth of new node is always 1
        return True


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
        keys = self._graph.keys()
        if src not in keys or dst not in keys:
            return False

        # Check if SRC already connected to DST
        if dst in self._graph[src]:
            return False

        # Add dst to _graph[src] if reached here
        self._graph[src].append(dst)

        # Remove connection if it makes graph cyclic
        if self._isCyclic():
            self._graph[src].remove(dst)
            return False

        #update depth of destination node, and depth of all it's children by depth of src node
        self._incrementNodeDepths(dst, self._depth[src])

        return True #all 'troublesome' conditions passed if reached here


    #increments the depth of node and all it's children by the value inc, if the depth is greater than the previous depth.
    def _incrementNodeDepths(self, node, inc):
        self._depth[node] += inc
        parent = node
        queue = [node]
        while(queue != []):
            parent = queue.pop(0)
            children = self._graph[parent]
            for child in children:
                newDepth = self._depth[child] + inc
                if self._depth[child] < newDepth:
                    self._depth[child] += inc
                    queue.append(child)


    #Returns the depth of a node, if exists, else None
    def getDepth(self, node):
        #Check if node is in graph
        if node not in self._graph.keys():
            return None

        return self._depth[node]


    # Checks if src is directly connected to destination
    # NOTE: This methods exists only to check if add and addEdge work
    def hasDirectPathTo(self, src, dst):
        """
        Returns true if src exists in graph, and if src is directly connected to dst, else False.
        """
        # Check if src exists in graph
        if src not in self._graph:
            return False

        #Return true if src directly connected to dst
        if dst in self._graph[src]:
            return True

        #dst not directly connected to src or doesn't exists in graph
        return False


    # Checks if graph is cyclic and return True if cyclic, else False
    # NOTE: Source mentioned above
    def _isCyclic(self):
        path = set()
        visited = set()

        def visit(vertex):
            if vertex in visited:
                return False
            visited.add(vertex)
            path.add(vertex)
            for neighbour in self._graph.get(vertex, ()):
                if neighbour in path or visit(neighbour):
                    return True
            return False

        return any(visit(v) for v in self._graph) #returns True if True for atleast one v in self._graph


    # Find the LCA of two nodes of a graph
    def LCA(self, val_1, val_2):
        """
        Finds the lowest common ancestor of two nodes, (inclusive of the nodes themselves), and returns the node
        Returns None if LCA not found
        """

        # Empty graph check? NOTE: Not needed if next check is exists

        # Existing nodes check

        # Same node check

        # Same parent check

        # Normal check

        return None # nodes don't have a common ancestor
