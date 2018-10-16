# author: Shaun Jose
# Date created: 22/09/2018 (modified version of Binary Graph LCA)

# Lowest Common Ancestor class
# Finds the LCA of two nodes in a Graph

# Sources:
# 1. Graph respresentation idea source:
#    https://www.python.org/doc/essays/graphs/
# 2. _isCyclic implementation:
#    Gareth Rees's Recursion Limit implementation answer on https://codereview.stackexchange.com/questions/86021/check-if-a-directed-graph-contains-a-cycle
# 3. BeyondRubicon's answer on finding common elements of two lists for finding common elements of two lists, on:
#https://stackoverflow.com/questions/2864842/common-elements-comparison-between-2-lists

# DirectedAcyclicGraph class - Graph respresented as dictionary with data values, not node objects!
# Methods: add(self, val), addEdge(self, src, dst), _incrementNodeDepths(self, node, inc), getDepth(self, node), hasDirectPathTo(self, src, dst), _isCyclic(self), LCA(self, val_1, val_2)
# Attributes: _graph: is a dictionary of data values an arrays with connections
#             _depth: a dictionary with key as node_val and val as node_depth

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


    #Increments the depth of node and all it's children by the value inc, if the depth is greater than the previous depth
    #NOTE: in the event that a node has two depths (because of the existence of two or more roots of a connected components), the greater depth is chosen for the node
    def _incrementNodeDepths(self, node, inc):
        flag = False
        if self._depth[node] < inc + 1: #record greatest depth
            del self._depth[node]
            self._depth[node] = inc + 1
            flag = True
        parent = node
        queue = [node]
        while queue != []:
            parent = queue.pop(0)
            children = self._graph[parent]
            for child in children:
                if flag:
                    del self._depth[child]
                    self._depth[child] = self._depth[parent] + 1
                    queue.append(child)


    #Returns the depth of a node, if exists, else None
    def getDepth(self, node):
        #Check if node is in graph
        if node == None or node not in self._graph.keys():
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
        visited = set()
        path = [object()]
        path_set = set(path)
        stack = [iter(self._graph)]
        while stack:
            for v in stack[-1]:
                if v in path_set:
                    return True
                elif v not in visited:
                    visited.add(v)
                    path.append(v)
                    path_set.add(v)
                    stack.append(iter(self._graph.get(v, ())))
                    break
            else:
                path_set.remove(path.pop())
                stack.pop()
        return False #returns True if True for atleast one v in self._graph


    def _getParentsOf(self, val):#TODO: add queue here
        parents = [val]
        queue = [val]

        #get all ancestors
        while queue != []:
            curr_node = queue.pop(0) #TODO: recall parentsOf from here with node as val and pass in new queue
            for node in self._graph.keys():
                if curr_node in self._graph[node] and node not in parents:
                    parents.append(node)
                    queue.append(node)

        return parents


    # Find the LCA of two nodes of a graph
    def LCA(self, val_1, val_2):
        """
        Finds the lowest common ancestor of two nodes, (inclusive of the nodes themselves), and returns the node
        Returns None if LCA not found
        """

        # Empty graph check
        if len(self._graph) == 0: # Not needed if next check is exists
            return None

        # Existing nodes check
        nodes = self._graph.keys()
        if val_1 not in nodes or val_2 not in nodes:
            return None

        # Same node check
        if val_1 == val_2:
            return val_1

        parents_1 = self._getParentsOf(val_1)
        parents_2 = self._getParentsOf(val_2)

        #NOTE: line of code below, sourced in beginning of file
        common_ancestors = set(parents_1) - (set(parents_1) - set(parents_2))
        common_ancestors = list(common_ancestors)

        if common_ancestors == []:
            return None # nodes don't have a common ancestor

        deepest = common_ancestors.pop(0)

        #find common ancestor with greates depth
        while common_ancestors != []:
            nextAnc = common_ancestors.pop(0)
            if self._depth[nextAnc] > self._depth[deepest]:
                deepest = nextAnc

        return deepest
