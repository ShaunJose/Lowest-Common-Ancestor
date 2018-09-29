# Exhaustive Tester of the Lowest_Common_Ancestor class, (focus on LCA method implementation)

# Pytest framework used

from Lowest_Common_Ancestor import BinaryTree, Node

#test_empty_tree not applicable for LCA

# Method for all the add and get cases which weren't covered above, so as to achieve maximm code-coverage
# NOTE: No tests here! This is simply for code-coverage
def remaining_add_get_cases():

    bt = BinaryTree()
    node1 = bt.add(7)
    node2 = bt.add(10)
    node3 = bt.add(5)
    node4 = bt.add(11)
    node5 = bt.add(9)
    node6 = bt.add(4)
    node7 = bt.add(6)

    #covering code for duplicate node value
    bt.add(5) #shouldn't change the tree, duplicate value

    #trying get for all 7 node values
    assert (bt.get(7) == node1)
    assert (bt.get(10) == node2)
    assert (bt.get(5) == node3)
    assert (bt.get(11) == node4)
    assert (bt.get(9) == node5)
    assert (bt.get(4) == node6)
    assert (bt.get(6) == node7)

    #trying get for values that doesn't exist
    #assert not used because done purely for code-coverage
    assert (bt.get(1) == None)
    assert (bt.get(100) == None)


# Test outcome of LCA for a populated binary tree with None(null) node/s passed
def test_none_nodes():
    #Creating and populating binary tree
    bt = BinaryTree()
    bt.add(7)
    bt.add(12)
    bt.add(232)
    bt.add(8)
    bt.add(2)

    #passing both node1 == node2 == None
    assert (BinaryTree.LCA(None, None) == None)

    #passing node2 == None
    assert (BinaryTree.LCA(bt.get(7), None) == None)

    #passing node1 == None (not really needed)
    assert (BinaryTree.LCA(None, bt.get(7)) == None)

    #passing get(val) such that val not in tree
    #13 doesn't exist in tree
    assert (BinaryTree.LCA(bt.get(7), bt.get(13)) == None)


# LCA Test with node1 == node2 (testing same node)
def test_same_nodes():
    #Creating binary tree with one node
    bt = BinaryTree()
    bt.add(10)

    #Check LCA of root and root
    node = bt.get(10)
    assert (BinaryTree.LCA(node, node) == node)

    #Populating binary tree
    bt.add(8)
    bt.add(9)
    bt.add(12)
    bt.add(11)
    bt.add(24)
    bt.add(1)

    #Check LCA of node 11 and itself
    node_11 = bt.get(11);
    assert (BinaryTree.LCA(node_11, node_11) == node_11)

    #Check LCA of node 1 and itself
    node_1 = bt.get(1);
    assert (BinaryTree.LCA(node_1, node_1) == node_1)


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
    assert (BinaryTree.LCA(bt.get(30), bt.get(80)) == bt.get(50))

    #Check LCA of 12 and 30 (should be 25)
    assert (BinaryTree.LCA(bt.get(12), bt.get(30)) == bt.get(25))

    #Check LCA of 60 and 80 (should be 75)
    assert (BinaryTree.LCA(bt.get(60), bt.get(80)) == bt.get(75))

    #Check LCA of 50 and 60 (should be 50)
    assert (BinaryTree.LCA(bt.get(50), bt.get(60)) == bt.get(50))

    #Check LCA of 100 and 12 (should be 100)
    assert (BinaryTree.LCA(bt.get(12), bt.get(100)) == bt.get(100))


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
    assert (BinaryTree.LCA(bt.get(30), bt.get(80)) == bt.get(50))

    #Check LCA of 12 and 30 (should be 25)
    assert (BinaryTree.LCA(bt.get(12), bt.get(30)) == bt.get(25))

    #Check LCA of 50 and 60 (should be 50)
    assert (BinaryTree.LCA(bt.get(50), bt.get(60)) == bt.get(50))

    #Check LCA of 10 and 12 (should be 10)
    assert (BinaryTree.LCA(bt.get(10), bt.get(12)) == bt.get(10))


# Test LCA for 2 nodes in sufficiently populated binary tree
def test_populated_tree():
    bt = BinaryTree()
    bt.add(100)         #
    bt.add(50)          # Representation of Binary Tree
    bt.add(150)         #
    bt.add(25)          #        100
    bt.add(75)          #      /     \
    bt.add(180)         #     50     150
    bt.add(125)         #     / \    /  \
    bt.add(10)          #   25  75  125 180
    bt.add(80)          #   /    \    \    \
    bt.add(200)         #  10    80   127  200
    bt.add(127)         #             / \
    bt.add(126)         #           126 142
    bt.add(142)

    #exhaustive testing

    #nodes at same 'depth'
    assert (BinaryTree.LCA(bt.get(80), bt.get(10)) == bt.get(50))
    assert (BinaryTree.LCA(bt.get(126), bt.get(142)) == bt.get(127))
    assert (BinaryTree.LCA(bt.get(10), bt.get(200)) == bt.get(100))
    assert (BinaryTree.LCA(bt.get(50), bt.get(150)) == bt.get(100))

    #node1 higher in the tree than node2
    assert (BinaryTree.LCA(bt.get(100), bt.get(10)) == bt.get(100))
    assert (BinaryTree.LCA(bt.get(100), bt.get(126)) == bt.get(100))
    assert (BinaryTree.LCA(bt.get(10), bt.get(142)) == bt.get(100))
    assert (BinaryTree.LCA(bt.get(125), bt.get(142)) == bt.get(125))
    assert (BinaryTree.LCA(bt.get(75), bt.get(10)) == bt.get(50))

    #node1 deeper than node2
    assert (BinaryTree.LCA(bt.get(200), bt.get(125)) == bt.get(150))
    assert (BinaryTree.LCA(bt.get(142), bt.get(180)) == bt.get(150))
    assert (BinaryTree.LCA(bt.get(10), bt.get(75)) == bt.get(50))
    assert (BinaryTree.LCA(bt.get(142), bt.get(80)) == bt.get(100))
    assert (BinaryTree.LCA(bt.get(142), bt.get(125)) == bt.get(125))


# Test case where node1 and node2 are in different trees
def test_different_tree_nodes():
    #Create bt1 and populate it
    bt1 = BinaryTree()
    bt1.add(50)
    bt1.add(25)
    bt1.add(75)
    bt1.add(10)
    bt1.add(30)
    bt1.add(95)
    bt1.add(63)

    #Create bt2 and populate it
    #NOTE: populating bt2 IDENTICAL to bt1, BUT : bt1 != bt2 (diff references)
    bt2 = BinaryTree()
    bt2.add(50)
    bt2.add(25)
    bt2.add(75)
    bt2.add(10)
    bt2.add(30)
    bt2.add(95)
    bt2.add(63)

    #   Tree bt1
    #        50
    #      /    \
    #    25      75
    #   / \     /  \
    # 10  30   63  95

    #   Tree bt2
    #        50
    #      /    \
    #    25      75
    #   / \     /  \
    # 10  30   63  95

    #normal test case (node1 and node2 from bt1)
    assert (BinaryTree.LCA(bt1.get(30), bt1.get(63)) == bt1.get(50))

    #normal test case (node1 and node2 from bt2)
    assert (BinaryTree.LCA(bt2.get(30), bt2.get(63)) == bt2.get(50))

    #test case with node1 from bt1 and node2 from bt2
    assert (BinaryTree.LCA(bt1.get(30), bt2.get(63)) == None)
