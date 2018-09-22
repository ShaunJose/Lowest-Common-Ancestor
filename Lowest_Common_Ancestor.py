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
# Methods: isEmpty(self), add(self, val), LCA(self, Node, Node)
# Attributes: root, size

class BinaryTree:

    # Initializes an Empty Binary Tree
    def __init__(self):
        self.root = None
        self.size = 0


    # returns True if Tree is Empty, False otherwise
    def isEmpty(self):


    # adds a node in the Binary Tree
    def add(self, val):


    # finds the lowest common ancestor of two nodes, (inclusive of the nodes themselves)
    def LCA(self, node_1, node_2):
