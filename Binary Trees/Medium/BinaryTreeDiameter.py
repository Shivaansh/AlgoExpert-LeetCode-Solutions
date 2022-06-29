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
    #space: O(h) since we have a recursive call for each level of the tree
    if(tree is not None):
        #Get max depth of left subtree
        if(tree.left is not None):
            leftDepth = getMaxDepthInTree(tree.left)
        else:
            leftDepth = 0
        #Get max depth of right subtree
        if(tree.right is not None):
            rightDepth = getMaxDepthInTree(tree.right)
        else:
            rightDepth = 0
            
        #Get diameter in left and right trees, which is the longest path by combining both left and right subtrees' longest paths
        diameter = leftDepth + rightDepth

        #Return the max of the current diameter or the diameters of left and right subtrees
        return max(diameter, binaryTreeDiameter(tree.left), binaryTreeDiameter(tree.right))
    else:
        return 0

def getMaxDepthInTree(tree):
    if(tree is None):
        return 0
    if(tree.left is None and tree.right is None):
        return 1
    return 1 + max(getMaxDepthInTree(tree.left), getMaxDepthInTree(tree.right))
