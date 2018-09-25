# Exhaustive Tester of the Lowest_Common_Ancestor class, (focus on LCA method implementation)

# Pytest framework used

from Lowest_Common_Ancestor import BinaryTree, Node

# Test outcome of LCA for an empty binary tree with None(null) Nodes
def test_empty_tree():
    bt = BinaryTree()

    assert (bt.LCA(None, None) == None)

# Test outcome of LCA for an empty tree with nodes that exist
#def test_empty_tree_with_existing_nodes():
# NOTE: same outcome as previous method, so not needed


# Test outcome of LCA for a populated binary tree with None(null) node/s passed
def test_None_nodes():
    #Creating binary tree
    bt = BinaryTree()
    bt.add(7) #non-empty binary tree
    bt.add(12)
    bt.add(232)
    bt.add(8)
    bt.add(2)

    #passing both node1 == node2 == None
    assert (bt.LCA(None, None) == None)

    #passing node2 == None
    assert (bt.LCA(bt.get(7), None) == None)

    #passing get(val) such that val not in tree
    #neither 7 nor 13 exists in tree
    assert (bt.LCA(bt.get(7), bt.get(13)) == None)


# LCA Test with node1 == node2 (testing same node)
def test_same_nodes():
    #with one node bt

    #with sufficiently populated bt


# LCA Test with only left children
def test_left_tree():


# LCA Test with only right children
def test_right_tree():


# Test LCA for 2 nodes in sufficiently populated binary tree
def test_populated_tree():


# Test case where node1 and node2 are in different trees
def test_different_tree_nodes():


#Test case for all the add and get cases which weren't covered above, so as to achieve maximm code-coverage
def remaining_add_get_cases():
