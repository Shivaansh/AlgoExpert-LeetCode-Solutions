# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    #Name: Height Balanced Binary Tree
    #Category and difficulty: Binary Trees, Medium
    #time: O(n) since we vist each node
    #space: O(h) since we have a recursive call for each level of the tree
    if(tree is not None):
        #Get depth of left subtree
        if(tree.left is not None):
            leftDepth = getTreeHeight(tree.left)
        else:
            leftDepth = 0
        #Get depth of right subtree
        if(tree.right is not None):
            rightDepth = getTreeHeight(tree.right)
        else:
            rightDepth = 0
            
        #Check if current node is balanced
        isTreeBalanced = abs(leftDepth - rightDepth) <= 1

        #Return if current node is balanced and both left and right subtrees are balanced
        return (isTreeBalanced and heightBalancedBinaryTree(tree.left) and heightBalancedBinaryTree(tree.right))
    else:
        #Empty tree is always balanced
        return True

def getTreeHeight(tree):
    if(tree is None):
        return 0
    if(tree.left is None and tree.right is None):
        return 1
    return 1 + max(getTreeHeight(tree.left), getTreeHeight(tree.right))