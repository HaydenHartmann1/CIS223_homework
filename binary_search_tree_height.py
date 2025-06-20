'''
Hayden Hartmann
Coding Problem: Binary Search Tree Height
6/19/2025
'''

#The binary search tree class
class MyBinarySearchTree:
    #The node class within
    class Node:
        def __init__(self, key):
            self.key = key
            self.left = None
            self.right = None

    #Constructor to set root to None
    def __init__(self):
        self.root = None

    #Insert method called when a key is added
    def InsertKey(self, key):
        self.root = self.RecursiveInsert(self.root, key)

    #Recursivly called insert method
    def RecursiveInsert(self, node, key):
        if node is None:
            return self.Node(key)
        if key < node.key:
            node.left = self.RecursiveInsert(node.left, key)
        else:
            node.right = self.RecursiveInsert(node.right, key)
        return node

    #Height method called initially
    def FindHeight(self):
        return self.RecursiveHeight(self.root)

    #Height method recursivly called
    def RecursiveHeight(self, node):
        if node is None:
            return -1
        return 1 + max(self.RecursiveHeight(node.left), self.RecursiveHeight(node.right))

#creates tree object
myTree = MyBinarySearchTree()
values = [33, 22, 41, 14, 27, 35, 57, 55, 56]
for x in values:
    myTree.InsertKey(x)

print("Tree Height: " + str(myTree.FindHeight()))

