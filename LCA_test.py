# Exhaustive Tester of the Lowest_Common_Ancestor class, (focus on LCA method implementation)

# Pytest framework used

from Lowest_Common_Ancestor import BinaryTree, Node

# Method for all the add, addEdge and hasDirectPathTo cases.
# NOTE: hasDirectPathTo exists only to check if add and addEdge works
def test_all_basic_class_methods():
    #Creating empty graph - NOTE: init method creates empty graph

    #empty graph get test case - NOTE: way to retrieve nodes from graph

    #populating graph - NOTE: add() method to add nodes to graph

    #covering code for duplicate node value - NOTE: graph wont take non-unique values

    #trying get for all node values

    #trying get for values that don't exist


# -------- LCA Tests -------- #

#test_empty_graph with None nodes
def test_empty_graph():


# Test outcome of LCA for a populated graph with None(null) node/s passed
def test_none_nodes():


# LCA Test with node1 == node2 (testing same node)
def test_same_nodes():


# Test case where two nodes have the same 'parent' (hence LCA is parent)
def test_same_parent():


# Test LCA for 2 nodes in a sufficiently populated graph
def test_populated_graph():
    #Create and populate graph, add edges as well
    #Test node1 higher than node2
    #Test node2 higher than node1
    #Test node1 and node2 on the same level


# Test case where graph is cyclic - NOTE: method to check if graph is cyclic? or check if new node getting added makes graph cyclic and add/don't add accordingly.
def test_cyclic_graph():


# Test case where the two nodes are in different connected components (hence LCA should be None)
def test_diff_connected_comps():


# Test case where two nodes have more than one possible LCA. In this case, we'll accept either candidate of an LCA as a correct response
def test_multiple_LCA():
