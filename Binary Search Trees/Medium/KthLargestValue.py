# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    #Name: Kth largest value in BST
    #Category and difficulty: BSTs, Medium
    #Time: O(h + k) where h is height of tree, k is the input parameter provided
    #space: O(h + k) for size of array used and depth of recursion
    array = []
    if(tree is None):
        return -1
    return findKthLargestHelper(tree, k, array)[-1]

def findKthLargestHelper(tree, k, array):
    if(tree is not None and len(array) < k):
        findKthLargestHelper(tree.right, k, array)
        if(len(array) < k):
            array.append(tree.value)
        findKthLargestHelper(tree.left, k, array)
    return array
        
    
