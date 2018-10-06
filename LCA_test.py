# Exhaustive Tester of the Lowest_Common_Ancestor class, (focus on LCA method implementation)

# Pytest framework used

from Lowest_Common_Ancestor import BinaryTree, Node

#test_empty_graph? -> if LCA method is non-static
#def test_empty_graph():

# Method for all the add and get cases.
def test_all_add_get_cases():
    #Creating empty graph - NOTE: init method creates empty graph

    #empty graph get test case - NOTE: way to retrieve nodes from graph

    #populating graph - NOTE: add() method to add nodes to graph

    #covering code for duplicate node value - NOTE: graph wont take non-unique values

    #trying get for all node values

    #trying get for values that don't exist

# Test outcome of LCA for a populated with None(null) node/s passed
#def test_none_nodes():


# LCA Test with node1 == node2 (testing same node)
def test_same_nodes():

# LCA Test with only left children?
#def test_left_tree():

# LCA Test with only right children?
#def test_right_graph():

# Test LCA for 2 nodes in sufficiently populated graph
def test_populated_graph():

# Test case where node1 and node2 are in different graphs? -> if LCA method is static
# def test_different_graph_nodes():


# Test case where graph is cyclic - NOTE: method to check if graph is cyclic? or check if new node getting added makes graph cyclic and add/don't add accordingly.
def test_cyclic_graph():

#TODO: Plan out more test cases
