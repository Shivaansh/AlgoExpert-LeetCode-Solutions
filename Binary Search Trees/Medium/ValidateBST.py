# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    #Name: Validate BST
	#Category and difficulty: BSTs, Medium
    #time: O(n)
	#space: O(d) for recursion, where d is depth of tree

    #Can find minimum and maximum value in tree but it won't matter since for left nodes only max value matters (parent) 
    # and for right nodes only min value matters (parent)
    return isNodeValid(tree, -999999999999999, 999999999999999)

def isNodeValid(node, minValue, maxValue):
    if(node is None):
        return True
        
    if(node.value < minValue or node.value >= maxValue):
        return False
        
    isLeftValid = isNodeValid(node.left, minValue, node.value)
    isRightValid = isNodeValid(node.right, node.value, maxValue)
    
    #Node is valid is recursively, its left and right children are valid 
    return isLeftValid and isRightValid