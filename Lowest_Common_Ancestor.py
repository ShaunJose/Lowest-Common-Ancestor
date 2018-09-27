# author : Shaun Jose
# Date created: 22/09/2018

# Lowest Common Ancestor class
# Finds the LCA of two nodes in a Binary Tree

# Node class
# Attributes: left, right, data, parent
# NOTE: data can be int, float, double, or char type

class Node:

    def __init__(self, data, parent):
        self.left = None
        self.right = None
        self.data = data
        self.parent = parent

# BinaryTree class (ordered Binary Tree i.e. Binary Search Tree)
# Methods: _isEmpty(self), add(self, val), get(self, val), (static) LCA(node_1, node_2)
# Attributes: root, size

class BinaryTree:

    # Initializes an Empty Binary Tree
    def __init__(self):
        self._root = None #'_' implies root should not be accesses from outside
        self._size = 0


    # '_' to imply that function should not be accessed from outside
    def _isEmpty(self):
        """
        Returns True if Tree is Empty, and False otherwise
        """


    # NOTE: adds nodes in binary search tree order i.e. nodes with lower values to the left and node with larger values to the right
    # NOTE: Also keeps record of parent node
    def add(self, val):
        """
        Adds a node to the Binary Tree
        Doesn't add duplicate nodes (Nodes with duplicate values)
        """


    # Returns node with value val, if found, else None
    def get(self, val):
        """
        Accepts a value and returns the node with that corresponding value
        Returns None if node not found
        """


    # NOTE: LCA is not found in two cases :
    # 1. when either node is None.
    # 2. when node1 and node2 are in different trees
    # None value returned when LCA not found
    @staticmethod
    def LCA(node_1, node_2):
        """
        Finds the lowest common ancestor of two nodes, (inclusive of the nodes themselves), and returns the node
        Returns None if LCA not found
        """

        #node1 == None || node2 == None

        #node1 == node2

        #normal case

        #return None when not found
