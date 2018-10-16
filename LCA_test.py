# Exhaustive Tester of the Lowest_Common_Ancestor class, (focus on LCA method implementation)

# Pytest framework used

from Lowest_Common_Ancestor import DirectedAcyclicGraph

# Method for all the add, addEdge and hasDirectPathTo cases.
# NOTE: hasDirectPathTo exists only to check if add and addEdge works
def test_all_basic_class_methods():
    #Creating empty graph - init method creates empty graph
    dag = DirectedAcyclicGraph()

    #populating graph - add() method to add nodes to graph
    assert dag.add('A') == True
    assert dag.add(1) == True
    assert dag.add('B') == True
    assert dag.add(2) == True
    assert dag.add('C') == True
    assert dag.add('D') == True
    assert dag.add(3) == True
    assert dag.add('E') == True
    assert dag.add('F') == True
    assert dag.add(4) == True

    #covering code for duplicate node value - NOTE: graph wont take non-unique values
    assert dag.add('C') == False

    #add Edges (connect nodes of the graph)
    assert dag.addEdge(1, 'E') == True
    assert dag.addEdge('A', 3) == True
    assert dag.addEdge('A', 'F') == True
    assert dag.addEdge('F', 4) == True
    assert dag.addEdge(4, 2) == True

    #src or dst doesn't exists in graph
    assert dag.addEdge(5, 'A') == False #5 not in graph
    assert dag.addEdge('F', 'Z') == False #Z not in graph
    assert dag.addEdge(47, 53) == False #both 47 and 53 not in graph (don't really need this test case!!)

    #add connection from 4 to 2 (BUT CONNECTION ALREADY CREATED!)
    assert dag.addEdge(4, 2) == False

    #Test Cyclic
    assert dag.addEdge('F', 'A') == False #'F' to 'A' when 'A' to 'F' exists
    assert dag.addEdge(4, 'A') == False #A-F-4-A cycle
    assert dag.addEdge(2, 'A') == False #A-F-4-2-A cycle

    #check has directPathTo for adequate cases
    #NOTE: these tests check if addEdge actually works properly
    assert dag.hasDirectPathTo(1, 'E') == True
    assert dag.hasDirectPathTo('A', 3) == True
    assert dag.hasDirectPathTo('A', 'F') == True
    assert dag.hasDirectPathTo('F', 4) == True
    assert dag.hasDirectPathTo(4, 2) == True
    assert dag.hasDirectPathTo('F', 2) == False #Path not direct!
    assert dag.hasDirectPathTo(3, 1) == False #no path exists
    assert dag.hasDirectPathTo(3, 7) == False #7 not in graph!
    assert dag.hasDirectPathTo('Z', 'F') == False  #'Z' not in graph
    assert dag.hasDirectPathTo(100, 'M') == False #100 and 'M' not in graph


#Testing if depths are right while creating graphs in different ways
#NOTE: Has 5 Kinds of tests!
def test_depth_maintenance():
    #1: Create and populate graph "normally" and test depth.
    dag_normal = DirectedAcyclicGraph()
    dag_normal.add(1)
    dag_normal.add(2)
    dag_normal.add(3)
    dag_normal.add(4)
    dag_normal.add(5)
    dag_normal.add(6)
    dag_normal.add(7)        # Graph respresentation
    dag_normal.addEdge(1, 2) #      3
    dag_normal.addEdge(1, 3) #      ^   (Root = 1)
    dag_normal.addEdge(1, 4) #      |
    dag_normal.addEdge(2, 5) # 4 <- 1 -> 2 -> 5 -> 6 -> 7
    dag_normal.addEdge(5, 6)
    dag_normal.addEdge(6, 7)

    #Test depth in normal case
    assert dag_normal.getDepth(1) == 1
    assert dag_normal.getDepth(4) == 2
    assert dag_normal.getDepth(3) == 2
    assert dag_normal.getDepth(2) == 2
    assert dag_normal.getDepth(5) == 3
    assert dag_normal.getDepth(6) == 4
    assert dag_normal.getDepth(7) == 5

    #2: Create and populate a graph, but connect in reverse order (root keeps changing)
    dag_reverse = DirectedAcyclicGraph()
    dag_reverse.add(8)
    dag_reverse.add(7)
    dag_reverse.add(6)
    dag_reverse.add(5)
    dag_reverse.add(4)
    dag_reverse.add(3)
    dag_reverse.add(2)
    dag_reverse.add(1)
    dag_reverse.addEdge(6, 2)
    dag_reverse.addEdge(5, 6) # Graph respresentation
    dag_reverse.addEdge(5, 7) #             7
    dag_reverse.addEdge(5, 8)  #            ^    (Root = 1)
    dag_reverse.addEdge(3, 5)  #            |
    dag_reverse.addEdge(3, 4)  #       8 <- 5 -> 6 -> 2
    dag_reverse.addEdge(1, 3)  #            ^
                               #            |
                               #       1 -> 3 -> 4

    #test depths of graph connected in reverse order
    assert dag_reverse.getDepth(1) == 1
    assert dag_reverse.getDepth(2) == 5
    assert dag_reverse.getDepth(3) == 2
    assert dag_reverse.getDepth(4) == 3
    assert dag_reverse.getDepth(5) == 3
    assert dag_reverse.getDepth(6) == 4
    assert dag_reverse.getDepth(7) == 4
    assert dag_reverse.getDepth(8) == 4

    #3: Create and populate graph, and then connect two components
    dag_cc = DirectedAcyclicGraph()
    dag_cc.add(1)
    dag_cc.add(2)
    dag_cc.add(3)
    dag_cc.add(4)
    dag_cc.add(5)
    dag_cc.add(6)
    #1st connected component
    dag_cc.addEdge(1, 2) #          4
    dag_cc.addEdge(3, 1) #          ^   (Root = 3)
    dag_cc.addEdge(1, 4) #          |
                         #     3 -> 1 -> 2
    #2nd connected component
    dag_cc.addEdge(5, 6)    # 5 -> 6

    #Joining both components
    dag_cc.addEdge(6, 1)

    #NOTE: A node always chooses a greater depth!

    assert dag_cc.getDepth(1) == 3
    assert dag_cc.getDepth(2) == 4
    assert dag_cc.getDepth(3) == 1
    assert dag_cc.getDepth(4) == 4
    assert dag_cc.getDepth(5) == 1
    assert dag_cc.getDepth(6) == 2


    #4: Create ad populate graph with multiple parents
    dag = DirectedAcyclicGraph()
    dag.add(1)
    dag.add(2)
    dag.add(3)
    dag.add(4)
    dag.add(5)
    dag.add(6)

    dag.addEdge(1, 2) # Graph representation
    dag.addEdge(1, 3) #  5     6     5  6 NOTE: just for represntation!
    dag.addEdge(3, 4) #  ^    ^      ^  ^      Duplicate ndoes dont exist!
    dag.addEdge(4, 5) #  |   /        \ |
    dag.addEdge(4, 6) #  | /           \|
    dag.addEdge(2, 5) #  2 <- 1 -> 3 -> 4
    dag.addEdge(2, 6) # (ROOT = 1)

    #test nodes with both having more than one parent
    assert dag.getDepth(1) == 1
    assert dag.getDepth(2) == 2
    assert dag.getDepth(3) == 2
    assert dag.getDepth(4) == 3
    assert dag.getDepth(5) == 4
    assert dag.getDepth(6) == 4


    #5: Test getDepth with nodes that don't exist
    assert dag.getDepth(None) == None
    assert dag.getDepth(10) == None




# ----------------------------- LCA Tests ----------------------------- #


#test_empty_graph with None nodes
def test_empty_graph():
    #Test empty graph with None nodes
    dag = DirectedAcyclicGraph()
    assert dag.LCA(None, None) == None

    #Test empty graph with any Nodes (which obviously don't exist in the graph)
    assert dag.LCA('A', 'B') == None
    assert dag.LCA('F', 1) == None
    assert dag.LCA(7, 3) == None


# Test outcome of LCA for a populated graph with None(null) node/s passed
def test_none_nodes():
    #Create and populate graph
    dag = DirectedAcyclicGraph()
    dag.add(1)
    dag.add(2)
    dag.add(3)
    dag.add(4)
    dag.addEdge(1, 2)
    dag.addEdge(2, 3)
    dag.addEdge(3, 4)

    #Graph: 1-->2-->3-->4

    #Test val1 = None
    assert dag.LCA(None, 1) == None
    #Test val2 = None
    assert dag.LCA(1, None) == None
    #Test val1=val2=None (test not needed in this case with resp to algorithm)
    assert dag.LCA(None, None) == None
    #Test nodes which don't exist
    assert dag.LCA('A', 2) == None
    assert dag.LCA(3, 5) == None

    #same val nodes which don't exist!
    assert dag.LCA(7, 7) == None


# LCA Test with node1 == node2 (testing same node)
def test_same_nodes():
    #Create graph with one node
    dag = DirectedAcyclicGraph()
    dag.add(1)

    #Test root node
    assert dag.LCA(1, 1) == 1

    #populate graph further
    dag.add(2)
    dag.add(3)
    dag.add(4)
    dag.add(5)
    dag.add(6)
    dag.add(7)
    dag.addEdge(1, 2) #             Graph respresentation
    dag.addEdge(2, 3) #
    dag.addEdge(2, 6) #                       7       4 (isolated node)
    dag.addEdge(1, 3) #                       ^
    dag.addEdge(3, 5) #                       |
    dag.addEdge(1, 7) #             6 <- 2 <- 1 -> 3 -> 5

    #Test non-root nodes
    assert dag.LCA(3, 3) == 3
    assert dag.LCA(2, 2) == 2
    assert dag.LCA(6, 6) == 6
    assert dag.LCA(5, 5) == 5
    assert dag.LCA(7, 7) == 7
    assert dag.LCA(4, 4) == 4


# Test case where two nodes have the same 'parent' (hence LCA is parent)
def test_same_parent():
    #Create and populate graph
    dag = DirectedAcyclicGraph()
    dag.add(1)
    dag.add(2)
    dag.add(3)
    dag.add(4)
    dag.add(5)
    dag.add(6)
    dag.add(7)
    dag.add(8)

    #connect nodes of graph
    dag.addEdge(2, 1) # Graph respresentation
    dag.addEdge(2, 3) #        8    7    6
    dag.addEdge(2, 8) #        ^    ^    ^
    dag.addEdge(3, 4) #        |    |    |
    dag.addEdge(3, 7) #   1 <- 2 -> 3 -> 4 -> 5
    dag.addEdge(4, 5)
    dag.addEdge(4, 6) #         Root = 2

    #Test same parents
    assert dag.LCA(5, 6) == 4
    assert dag.LCA(4, 7) == 3
    assert dag.LCA(3, 8) == 2
    assert dag.LCA(1, 8) == 2
    assert dag.LCA(1, 3) == 2


# Test LCA for 2 nodes in a sufficiently populated graph containing ONLY ONE connected component
def test_populated_graph():
    #Create and populate graph
    dag = DirectedAcyclicGraph()
    dag.add(1)
    dag.add(2)
    dag.add(3)
    dag.add(4)
    dag.add(5)
    dag.add(6)
    dag.add(7)
    dag.add(8)
    dag.add(9)
    dag.add(10)
    dag.add(11)
    dag.add(12)

    #Add edges
    dag.addEdge(5, 11) # Graph respresentation
    dag.addEdge(5, 12) #         3    11   6 -> 9
    dag.addEdge(5, 2)  #         ^    ^    ^
    dag.addEdge(2, 4)  #         |    |    |
    dag.addEdge(2, 3)  #    4 <- 2 <- 5 -> 12 -> 1 -> 7
    dag.addEdge(2, 10) #         |               |
    dag.addEdge(12, 1) #         10              8
    dag.addEdge(12, 6) #    (child of 2)    (child of 1)
    dag.addEdge(1, 7)
    dag.addEdge(1, 8)  #   Root of graph = 5
    dag.addEdge(6, 9)

    #Test node1 = LCA
    assert dag.LCA(5, 12) == 5
    assert dag.LCA(5, 9) == 5
    assert dag.LCA(5, 4) == 5
    assert dag.LCA(2, 10) == 2
    assert dag.LCA(12, 7) == 12
    assert dag.LCA(6, 9) == 6

    #Test node2 = LCA
    assert dag.LCA(4, 5) == 5
    assert dag.LCA(12, 5) == 5
    assert dag.LCA(4, 2) == 2
    assert dag.LCA(3, 2) == 2
    assert dag.LCA(8, 12) == 12
    assert dag.LCA(9, 12) == 12
    assert dag.LCA(7, 1) == 1
    assert dag.LCA(9, 6) == 6

    #Test node1 higher than node2
    assert dag.LCA(2, 9) == 5
    assert dag.LCA(6, 8) == 12
    assert dag.LCA(4, 7) == 5
    assert dag.LCA(1, 9) == 12
    assert dag.LCA(11, 10) == 5
    assert dag.LCA(3, 9) == 5

    #Test node2 higher than node1
    assert dag.LCA(3, 11) == 5
    assert dag.LCA(9, 1) == 12
    assert dag.LCA(10, 2) == 2
    assert dag.LCA(8, 6) == 12
    assert dag.LCA(9, 10) == 5

    #Test node1 and node2 on the same level
    assert dag.LCA(2, 12) == 5
    assert dag.LCA(2, 11) == 5
    assert dag.LCA(11, 12) == 5
    assert dag.LCA(3, 4) == 2
    assert dag.LCA(1, 6) == 12
    assert dag.LCA(10, 6) == 5
    assert dag.LCA(8, 9) == 12
    assert dag.LCA(9, 7) == 12


# Test case where the two nodes are in different connected components (hence LCA should be None)
def test_diff_connected_comps():
    #Create and populate graph
    dag = DirectedAcyclicGraph()
    dag.add(1)
    dag.add(2)
    dag.add(3)
    dag.add(4)
    dag.add(5)
    dag.add(6)
    dag.add(7)
    dag.add(8)
    dag.add(9)
    dag.add(10)
    dag.add(11)
    dag.add(12)
    dag.add(13)
    dag.add(14)
    dag.add(15)
    dag.add(16)
    dag.add(17)

    #Create connections (add edges)
    #1st connected component
    dag.addEdge(1, 2) # 1st connected component respresentation
    dag.addEdge(1, 10) #          9         4    10
    dag.addEdge(1, 3)  #          ^         ^    ^
    dag.addEdge(2, 8)  #          |         |    |
    dag.addEdge(3, 4)  #     7 <- 6 <- 5 <- 3 <- 1 -> 2 -> 8
    dag.addEdge(3, 5)
    dag.addEdge(5, 6)  # Root = 1
    dag.addEdge(6, 9)
    dag.addEdge(6, 7)

    #2nd connected component
    dag.addEdge(13, 14) # 2nd connected component respresentation
    dag.addEdge(14, 15) #       15
    dag.addEdge(14, 16) #       ^           Root = 13
    dag.addEdge(16, 17) #       |
                        # 13 -> 14 -> 16 -> 17

    #Two isolated nodes - 11 & 12

    #Test two isolated nodes
    assert dag.LCA(11, 12) == None

    #Test one isolated node and one non-isolated node
    assert dag.LCA(11, 13) == None
    assert dag.LCA(12, 6) == None
    assert dag.LCA(12, 15) == None

    #Test both roots of diff connect components
    assert dag.LCA(13, 1) == None

    #Test a root of one connected component and a non-root of the other
    dag.LCA(1, 17) == None
    dag.LCA(3, 6) == None
    dag.LCA(13, 2) == None
    dag.LCA(19, 13) == None

    #Test two non-roots of different connected components
    dag.LCA(3, 14) == None
    dag.LCA(17, 7) == None
    dag.LCA(17, 4) == None
    dag.LCA(8, 15) == None
    dag.LCA(9, 16) == None

    #Test if LCA of two nodes in same connected components still works with the existence of different connected components
    dag.LCA(15, 16) == 14
    dag.LCA(14, 13) == 13
    dag.LCA(17, 14) == 14
    dag.LCA(7, 8) == 1
    dag.LCA(4, 8) == 1
    dag.LCA(10, 3) == 1
    dag.LCA(3, 9) == 3
    dag.LCA(5, 7) == 5
    dag.LCA(2, 8) == 2
    dag.LCA(9, 7) == 6


#Test LCA on nodes with multiple parents
def test_multiple_parent_nodes():
    #4: Create ad populate graph with multiple parents
    dag = DirectedAcyclicGraph()
    dag.add(1)
    dag.add(2)
    dag.add(3)
    dag.add(4)
    dag.add(5)
    dag.add(6)

    dag.addEdge(1, 2) # Graph representation
    dag.addEdge(1, 3) #  5     6     5  6 NOTE: just for represntation!
    dag.addEdge(3, 4) #  ^    ^      ^  ^      Duplicate ndoes dont exist!
    dag.addEdge(4, 5) #  |   /        \ |
    dag.addEdge(4, 6) #  | /           \|
    dag.addEdge(2, 5) #  2 <- 1 -> 3 -> 4
    dag.addEdge(2, 6) # (Root = 1)

    #test nodes with both having more than one parent
    assert dag.LCA(5, 6) == 4
    #test node_1 with multiple parents
    assert dag.LCA(6, 3) == 3
    assert dag.LCA(6, 2) == 2
    #test node_2 with multiple parents
    assert dag.LCA(2, 5) == 2
    assert dag.LCA(3, 6) == 3


#Test nodes which are connected in reverse
#Tested because adding in reverse could affect depths of nodes
def test_reverse_constructed_graph():
    #Create and populate graph
    dag = DirectedAcyclicGraph()
    dag.add(1)
    dag.add(2)
    dag.add(3)
    dag.add(4)
    dag.add(5)
    dag.add(6)

    #Construct graph in reverse
    dag.addEdge(5, 6) # Graph representation
    dag.addEdge(4, 6) #    4 -> 6<- 5  (5 = child of 3)
    dag.addEdge(3, 4) #     ^      ^
    dag.addEdge(3, 5) #      \   /
    dag.addEdge(1, 3) #        3 <- 1 -> 2
    dag.addEdge(1, 2) #  Root = 1

    #Test LCA
    assert dag.LCA(3, 4) == 3
    assert dag.LCA(4, 5) == 3
    assert dag.LCA(1, 3) == 1
    assert dag.LCA(3, 2) == 1
    assert dag.LCA(6, 6) == 6
    assert dag.LCA(6, 3) == 3
    assert dag.LCA(6, 5) == 5
    assert dag.LCA(6, 4) == 4


#Test LCA of connected components before and after joining them
def test_cc_LCA():
    dag_cc = DirectedAcyclicGraph()
    dag_cc.add(1)
    dag_cc.add(2)
    dag_cc.add(3)
    dag_cc.add(4)
    dag_cc.add(5)
    dag_cc.add(6)
    dag_cc.add(7)
    #1st connected component
    dag_cc.addEdge(1, 2) #          4
    dag_cc.addEdge(3, 1) #          ^   (Root = 3)
    dag_cc.addEdge(1, 4) #          |
                         #     3 -> 1 -> 2
    #2nd connected component
    dag_cc.addEdge(5, 6)    # 5 -> 6 -> 7 (Root = 5)
    dag_cc.addEdge(6, 7)

    #Testing 1st component briefly
    assert dag_cc.LCA(1, 2) == 1
    assert dag_cc.LCA(4, 2) == 1
    assert dag_cc.LCA(3, 1) == 3

    #Testing 2nd component briefly
    assert dag_cc.LCA(5, 6) == 5
    assert dag_cc.LCA(6, 6) == 6
    assert dag_cc.LCA(7, 6) == 6

    #Joining both components
    dag_cc.addEdge(6, 1)

    #NOTE: note that depths of nodes 1 and 7, will be 3 (and not 2) since nodes always chooses the greater depth out of 'candidate depths'

    #Test LCA of joined components
    assert dag_cc.LCA(7, 1) == 6 #NOTE: should choose 6 over 3 because node 6 has a greater depth(=2) than node 3 does(depth = 1)!
    assert dag_cc.LCA(2, 4) == 1
    assert dag_cc.LCA(1, 3) == 3
    assert dag_cc.LCA(1, 6) == 6


# Test case where two nodes have more than one possible LCA. In this case, we'll accept either candidate of an LCA as a correct response
def test_multiple_LCA():
    #Create and populate graph
    dag = DirectedAcyclicGraph()
    dag.add(1)
    dag.add(2)
    dag.add(3)
    dag.add(4)
    dag.add(5)
    dag.add(6)

    #Create connections
    dag.addEdge(5, 2) # Graph represntation
    dag.addEdge(2, 1) #   4     6 (4 and 6 = children of both, 1 and 3)
    dag.addEdge(2, 3) #   ^     ^
    dag.addEdge(1, 4) #   | / \ |
    dag.addEdge(1, 6) #    1   3
    dag.addEdge(3, 4) #    ^   ^
    dag.addEdge(3, 6) #     \ /
                      #      2 <- 5
                      # Root = 5

    #NOTE that candidate LCAs for 4 and 6 are both, 1 and 3
    #We accept either one.
    result = dag.LCA(4, 6)
    assert result == 1 or result == 3


#Test char and int data types for LCA
def test_diff_data_types():
    #Create and populate graph
    dag = DirectedAcyclicGraph()
    dag.add(1)
    dag.add('A')
    dag.add(3)
    dag.add(4)
    dag.add('B')
    dag.add('Z')

    #NOTE: if 97 is chosen and 'a' is chosen. Values might clash because of unicode value of 'a'. Thus, values which do not clash must be chosen for this test.

    #Add edges
    dag.addEdge(1, 4)       # graph respresentation
    dag.addEdge(1, 'A')     #        4
    dag.addEdge(1, 3)       #        ^
    dag.addEdge('A', 'Z')   #        |
    dag.addEdge(3, 'Z')     #   A <- 1 -> 3 -> B
    dag.addEdge(3, 'B')     #    \       /
                            #     \    /
                            #       Z (Z = child of 3 and A)
                            #
                            # Root = 1

    #LCA Tests
    #One node char, One node int
    assert dag.LCA('A', 3) == 1
    assert dag.LCA(4, 'Z') == 1
    assert dag.LCA(3, 'Z') == 3
    assert dag.LCA('B', 4) == 1
    #Both nodes int
    assert dag.LCA(4, 3) == 1
    assert dag.LCA(4, 4) == 4
    assert dag.LCA(1, 3) == 1
    #Both nodes char
    assert dag.LCA('B', 'Z') == 3
    assert dag.LCA('A', 'Z') == 'A'
    assert dag.LCA('B', 'B') == 'B'
    assert dag.LCA('A', 'B') == 1
