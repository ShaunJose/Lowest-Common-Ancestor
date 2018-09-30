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
# Methods: add(self, data), _add(self, data, node, parent), get(self, data), _get(self, data, node), (static) LCA(node_1, node_2)
# Attributes: _root, size

class BinaryTree:

    # Initializes an Empty Binary Tree
    def __init__(self):
        self._root = None #'_' implies _root should not be accesses from outside
        self._size = 0


    # NOTE: adds nodes in binary search tree order i.e. nodes with lower data values to the left and node with larger data values to the right
    # NOTE: Also keeps record of parent node
    def add(self, data):
        """
        Adds a node to the Binary Tree
        Doesn't add duplicate nodes (Nodes with duplicate values)
        """
        self._root = self._add(data, self._root, None)

    # Recursive inner _add method
    def _add(self, data, node, parent):

        #Found a place to store the node
        if(node == None):
            node = Node(data, parent)
            self._size += 1
            return node

        #Traversing the tree to find an empty place for the new node
        if(data < node.data):
            node.left = self._add(data, node.left, node)
        elif(data > node.data):
            node.right = self._add(data, node.right, node)
        #equals to case -> don't add duplicate node (i.e. do nothing)

        return node


    # Returns node with data, if found, else None
    def get(self, data):
        """
        Accepts a value and returns the node with that corresponding value
        Returns None if node not found
        """
        return self._get(data, self._root)

    # Recursive get method
    def _get(self, data, node):

        if(node == None): #node doesn't exist
            return None

        if(data == node.data):
            return node

        if(data < node.data):
            return self._get(data, node.left)
        else: #Node can only be greater than now as equal data values not      allowed
            return self._get(data, node.right)


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

        return None

        #node1 == None || node2 == None

        #node1 == node2

        #normal case

        #return None when not found
