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
    #space: O(n) since we store the traversal of the whole tree
    ##Note: Here we find the in-order traversal of the tree iteratively, to prevent multiple recrusive
    traversal = inOrderTraversal(tree)

    for index in range(len(traversal)):
        if(traversal[index] == node):
            if(index + 1 < len(traversal)):
                return traversal[index+1]
    return None

def inOrderTraversal(tree):
    array = []
    stack = []
    if(tree is not None):
        currentPointer = tree
        while(currentPointer is not None or len(stack) > 0):
            
            if(currentPointer is not None):
                stack.append(currentPointer)
                currentPointer = currentPointer.left
            else:
                currentPointer = stack.pop()
                array.append(currentPointer)
                currentPointer = currentPointer.right
    return array
    