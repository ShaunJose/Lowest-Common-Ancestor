# author : Shaun Jose
# Date created: 22/09/2018

# Node class
# Attributes: left, right, data
# NOTE: data can be int, float, double, or char type

class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

# Lowest Common Ancestor class
# Finds the LCA of two nodes in a Binary Tree

# BinaryTree class (ordered Binary Tree i.e. Binary Search Tree)
# Methods: isEmpty(self), add(self, val), LCA(self, node_1, node_2)
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
    def add(self, val):
        """
        Adds a node to the Binary Tree
        Doesn't add duplicate nodes (Nodes with duplicate values)
        """

    # NOTE: LCA is not found in two cases :
    # 1. when either node is null.
    # 1. when node1 and node2 are in different trees
    # Null value returned when LCA not found
    def LCA(self, node_1, node_2):
        """
        Finds the lowest common ancestor of two nodes, (inclusive of the nodes themselves), and returns the node
        Returns null if LCA not found
        """

        #empty tree case (self.root == null)

        #node1 == null || node2 == null

        #node1 == node2

        #normal case

        #return null when not found
