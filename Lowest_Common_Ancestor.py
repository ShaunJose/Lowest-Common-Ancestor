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
# methods: isEmpty(self), size(self), add(self, val), delete(?), LCA(self, Node, Node)
