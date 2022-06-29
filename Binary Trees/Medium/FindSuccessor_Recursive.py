# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    #Name: Find Successor
    #Category and difficulty: Binary Trees, Medium
    #time: O(n) since we vist each node
    #space: O(n) since we store the traversal of the whole tree and find it recursively
    traversal = []
    inOrderTraversal(tree, traversal)

    for index in range(len(traversal)):
        if(traversal[index] == node):
            if(index + 1 < len(traversal)):
                return traversal[index+1]
    return None

def inOrderTraversal(tree, array):
    if(tree is not None):
        if(tree.left is not None):
            inOrderTraversal(tree.left, array)
        array.append(tree)
        if(tree.right is not None):
            inOrderTraversal(tree.right, array)
    