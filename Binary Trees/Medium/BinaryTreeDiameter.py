# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    #Name: Binary Tree Diameter
    #Category and difficulty: Binary Trees, Medium
    #time: O(n) since we vist each node
    #space: O(n) since we have a recursive call for each node
    if(tree is None):
        return 0
    leftDepth = maxdepth(tree.left)
    rightDepth = maxdepth(tree.right)
    diameter = leftDepth + rightDepth
    return max(diameter, binaryTreeDiameter(tree.left), binaryTreeDiameter(tree.right))

def maxdepth(tree):
    if(tree is None):
        return 0
    if(tree.left is None and tree.right is None):
        return 1
    return 1 + max(maxdepth(tree.left), maxdepth(tree.right))
