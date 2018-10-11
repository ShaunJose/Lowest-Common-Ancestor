# Exhaustive Tester of the Lowest_Common_Ancestor class, (focus on LCA method implementation)

# Pytest framework used

from Lowest_Common_Ancestor import DirectedAcyclicGraph

# Method for all the add, addEdge and hasDirectPathTo cases.
# NOTE: hasDirectPathTo exists only to check if add and addEdge works
def test_all_basic_class_methods():
    #Creating empty graph - NOTE: init method creates empty graph
    dag = DirectedAcyclicGraph()

    #populating graph - NOTE: add() method to add nodes to graph
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

    # add Edges (connect nodes of the graph)
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

# -------- LCA Tests -------- #

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


# LCA Test with node1 == node2 (testing same node)
def test_same_nodes():
    #Create graph with one node
    dag = DirectedAcyclicGraph()
    dag.add(1)

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

    assert dag.LCA(3, 3) == 3
    assert dag.LCA(2, 2) == 2
    assert dag.LCA(6, 6) == 6
    assert dag.LCA(5, 5) == 5
    assert dag.LCA(7, 7) == 7
    assert dag.LCA(4, 4) == 4


# Test case where two nodes have the same 'parent' (hence LCA is parent)
def test_same_parent():


# Test LCA for 2 nodes in a sufficiently populated graph
def test_populated_graph():
    #Create and populate graph, add edges as well
    #Test node1 higher than node2
    #Test node2 higher than node1
    #Test node1 and node2 on the same level


# Test case where the two nodes are in different connected components (hence LCA should be None)
def test_diff_connected_comps():


# Test case where two nodes have more than one possible LCA. In this case, we'll accept either candidate of an LCA as a correct response
def test_multiple_LCA():
