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
    #Creating and populating binary tree
    bt = BinaryTree()
    bt.add(7)
    bt.add(12)
    bt.add(232)
    bt.add(8)
    bt.add(2)

    #passing both node1 == node2 == None
    assert (bt.LCA(None, None) == None)

    #passing node2 == None
    assert (bt.LCA(bt.get(7), None) == None)

    #passing get(val) such that val not in tree
    #13 doesn't exist in tree
    assert (bt.LCA(bt.get(7), bt.get(13)) == None)


# LCA Test with node1 == node2 (testing same node)
def test_same_nodes():
    #Creating binary tree with one node
    bt = BinaryTree()
    bt.add(10)

    #Check LCA of root and root
    node = bt.get(10)
    assert (bt.LCA(node, node) == node)

    #Populating binary tree
    bt.add(8)
    bt.add(9)
    bt.add(12)
    bt.add(11)
    bt.add(24)
    bt.add(1)

    #Check LCA of node 11 and itself
    node_11 = bt.get(11);
    assert (bt.LCA(node_11, node_11) == node_11)


# LCA Test with only left children
def test_left_tree():
    #Creating and populating "left" Binary tree
    bt = BinaryTree()
    bt.add(100)
    #All values have to be lower from here on
    bt.add(50)
    bt.add(25)
    bt.add(75)
    bt.add(12)
    bt.add(30)
    bt.add(80)
    bt.add(60)

    #        100
    #       /   \
    #      50   None(null)
    #    /    \
    #   25     75
    #  /  \    / \
    # 12  30  60 80

    #Check LCA of 30 and 80 (should be 50)
    assert (bt.LCA(bt.get(30), bt.get(80)) == bt.get(50))

    #Check LCA of 12 and 30 (should be 25)
    assert (bt.LCA(bt.get(12), bt.get(30)) == bt.get(25))

    #Check LCA of 50 and 60 (should be 50)
    assert (bt.LCA(bt.get(50), bt.get(60)) == bt.get(50))

    #Check LCA of 100 and 12 (should be 100)
    assert (bt.LCA(bt.get(100), bt.get(12)) == bt.get(100))

# LCA Test with only right children
def test_right_tree():
    #Creating and populating "right" Binary tree
    bt = BinaryTree()
    bt.add(10)
    #All values have to be higher from here on
    bt.add(50)
    bt.add(25)
    bt.add(75)
    bt.add(12)
    bt.add(30)
    bt.add(80)
    bt.add(60)

    #        10
    #       /   \
    #    None    50
    #          /    \
    #         25     75
    #        /  \    / \
    #       12  30  60 80

    #Check LCA of 30 and 80 (should be 50)
    assert (bt.LCA(bt.get(30), bt.get(80)) == bt.get(50))

    #Check LCA of 12 and 30 (should be 25)
    assert (bt.LCA(bt.get(12), bt.get(30)) == bt.get(25))

    #Check LCA of 50 and 60 (should be 50)
    assert (bt.LCA(bt.get(50), bt.get(60)) == bt.get(50))

    #Check LCA of 10 and 12 (should be 10)
    assert (bt.LCA(bt.get(10), bt.get(12)) == bt.get(10))


# Test LCA for 2 nodes in sufficiently populated binary tree
def test_populated_tree():


# Test case where node1 and node2 are in different trees
def test_different_tree_nodes():
    #Create empty bt1 and populated bt2

    #bt1 empty, but pass actual nodes from bt2

    #populate bt1, test case with node1 from bt1 and node2 from bt2


# Method for all the add and get cases which weren't covered above, so as to achieve maximm code-coverage
# NOTE: No tests here! This is simply for code-coverage
def remaining_add_get_cases():
